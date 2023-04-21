
'use strict';

const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var transactionSchema = Schema( {
  item: String,
  item_num: Number,
  amount: Number,
  category: String,
  date: Date,
  description: String,
  completed: Boolean,
  createdAt: Date,
  userId: {type:ObjectId, ref:'user' }
} );

module.exports = mongoose.model( 'Transaction_Model', transactionSchema );
