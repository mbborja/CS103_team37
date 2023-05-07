
'use strict';

const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var adventurerSchema = Schema( {
  item: String,
  item_num: Number,

  date: Date,
  
  selected: Boolean,
  name: String,
  game_class: String,
  background: String,
  race: String,
  alignment: String,
  

  completed: Boolean,



  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'Adventurer_Model', adventurerSchema );
