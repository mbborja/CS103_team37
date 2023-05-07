/*
  Adventure_router.js -- Router for the Adventure Generator
*/
const express = require('express');
const router = express.Router();
const session = require('express-session');
const Adventurer_Model = require('../models/Adventurer_Model')
const User = require('../models/User')
const axios = require('axios')
/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

// get the value associated to the key
router.get('/adventure/',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
      const completed = show=='completed'
      const selected = show=='roster'
      
      const roster = await Adventurer_Model.find();
      req.session.adventurers = roster;
      
      let items=[]
      
      if (show=='roster') {
        items = 
          await Adventurer_Model.find({userId:req.user._id, selected:true})
                        .sort({name:1})     
      }else {
        items = 
          await Adventurer_Model.find({userId:req.user._id})
                        .sort({name:1})
      }
      
      res.render('adventure_view',{items,show,selected,completed,roster});
});



/* add the value in the body to the list associated to the key */
router.post('/adventure',
  isLoggedIn,
  async (req, res, next) => {
      const adventurer = new Adventurer_Model(
        {
          item: req.body.item,
          date: req.body.date,
          selected: false,
          name: req.body.name,
          game_class: req.body.game_class,
          background: req.body.background,
          race: req.body.race,
          alignment: req.body.alignment,

          userId: req.user._id,
        })
      await adventurer.save();
      res.redirect('/adventure')
});

router.get('/adventure/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /adventure/remove/:itemId")
      await Adventurer_Model.deleteOne({_id:req.params.itemId});
      res.redirect('/adventure')
});

router.get('/adventure/roster_add/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /adventure/complete/:itemId")
      await Adventurer_Model.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {selected:true}} );
      res.redirect('/adventure')
});

router.get('/adventure/roster_remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /adventure/complete/:itemId")
      await Adventurer_Model.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {selected:false}} );
      res.redirect('/adventure/?show=roster')
});

router.get('/adventure/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /adventure/edit/:itemId")
      const item = 
       await Adventurer_Model.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('adventure_edit')
      //res.json(item)
});

router.post('/adventure/updateAdventure',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,name,game_class,background,race,alignment} = req.body;
      console.log("inside /adventure/complete/:itemId");
      await Adventurer_Model.findOneAndUpdate(
        {_id:itemId},
        {$set: {name, game_class,background,race,alignment}} );
      res.redirect('/adventure')
});

router.get('adventure/:itemId', (req, res, next) => {
  const selectedId = req.params.id;
  if (!req.session.selectedIds) {
    req.session.selectedIds = []; // initialize an empty array
  }
  const index = req.session.selectedIds.indexOf(selectedId);
  if (index === -1) {
    req.session.selectedIds.push(selectedId); // add selectedId to the array
  } else {
    req.session.selectedIds.splice(index, 1); // remove selectedId from the array
  }
  res.redirect('/adventure'); // redirect to the adventure page
})


router.get('/adventure/start',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
      const completed = show=='completed'
      const selected = show=='roster'
      const axios = require('axios')
      
      let active_roster=[]

      active_roster = 
          await Adventurer_Model.find({userId:req.user._id, selected:true})
                        .sort({category:1,amount:1,date:1})

      adventure_prompt = "Write me a rougly 2000 word custom random adventure with the following adventurers: "
      
      active_roster.forEach(item => {
        adventure_prompt += ("Adventurer:")
        adventure_prompt += ("\nName: " + item.name);
        adventure_prompt += ("\ngame_class: " + item.game_game_class);
        adventure_prompt += ("\nBackground: " + item.background);
        adventure_prompt += ("\nRace: " + item.race);
        adventure_prompt += ("\nAlignment " + item.alignment)

      });

      response =
      await axios.post('http://gracehopper.cs-i.brandeis.edu:3500/openai',
      {prompt:adventure_prompt})
      const message = response.data.choices[0].message.content;
      
      res.render('adventure_start',{message,response,show,selected,active_roster});
});


module.exports = router;
