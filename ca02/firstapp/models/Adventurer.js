'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var adventurerSchema = Schema( {
  items: String,
  name: String,
  class: String,
  race: String,
  background: String,
  alignment: String,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'Adventurer', adventurerSchema );
