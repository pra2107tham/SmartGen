import mongoose from 'mongoose';

const { Schema } = mongoose;

const ProductSchema = new Schema({
  _id: { 
    type: Schema.Types.ObjectId, 
    required: true, 
    unique: true 
  },
  user_id: { 
    type: Schema.Types.ObjectId, 
    ref: 'User', 
    required: true 
  },
  media_id:{
    type: [Schema.Types.ObjectId],
    ref: 'Media',
    required: true
  },
  product_name: { 
    type: String, 
    required: true 
  },
  description: { 
    type: String, 
    required: true 
  },
  media_url: { 
    type: [String], 
    required: true 
  },
  product_category: { 
    type: String, 
    required: true 
  },
  price: { 
    type: Number, 
    required: false 
  },
  brand: { 
    type: String, 
    required: true 
  },
  created_at: { 
    type: Date, 
    default: Date.now 
  }
});

const Product = mongoose.model('Product', ProductSchema);

export default Product;
