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
  product_name: { 
    type: String, 
    required: true 
  },
  description: { 
    type: String, 
    required: true 
  },
  keywords: { 
    type: [String], 
    required: true 
  },
  images: { 
    type: [String], 
    required: true 
  },
  primary_image: { 
    type: String, 
    required: true 
  },
  category: { 
    type: String, 
    required: true 
  },
  dimensions: {
    height: { 
      type: String, 
      required: true 
    },
    width: { 
      type: String, 
      required: true 
    },
    depth: { 
      type: String, 
      required: true 
    },
    weight: { 
      type: String, 
      required: true 
    }
  },
  price: { 
    type: String, 
    required: true 
  },
  stock_quantity: { 
    type: Number, 
    required: true 
  },
  compliance_check: { 
    type: Boolean, 
    required: true 
  },
  amazon_listing_id: { 
    type: String, 
    unique: true 
  },
  listing_status: { 
    type: String, 
    required: true 
  },
  brand: { 
    type: String, 
    required: true 
  },
  bullet_points: { 
    type: [String], 
    required: true 
  },
  asin: { 
    type: String, 
    unique: true 
  },
  created_at: { 
    type: Date, 
    default: Date.now 
  }
});

const Product = mongoose.model('Product', ProductSchema);

export default Product;
