const AmazonListedReadySchema = new Schema({
    user_id: {
      type: Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    refined_product: {
      type: Schema.Types.ObjectId,
      ref: "RefinedProduct", // Links to Refined Product schema
      required: true,
    },
    product_name: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    keywords: {
      type: [String],
      required: true,
    },
    images: {
      type: [String],
      required: true,
    },
    primary_image: {
      type: String,
      required: true,
    },
    category: {
      type: String,
      required: true,
    },
    dimensions: {
      height: {
        type: String,
        required: true,
      },
      width: {
        type: String,
        required: true,
      },
      depth: {
        type: String,
        required: true,
      },
      weight: {
        type: String,
        required: true,
      },
    },
    price: {
      type: String,
      required: true,
    },
    stock_quantity: {
      type: Number,
      required: true,
    },
    compliance_check: {
      type: Boolean,
      required: true,
    },
    amazon_listing_id: {
      type: String,
      unique: true,
    },
    listing_status: {
      type: String,
      required: true,
    },
    brand: {
      type: String,
      required: true,
    },
    bullet_points: {
      type: [String],
      required: true,
    },
    asin: {
      type: String,
      unique: true,
    },
    created_at: {
      type: Date,
      default: Date.now,
    },
  });
  
  const AmazonListedReady = mongoose.model(
    "AmazonListedReady",
    AmazonListedReadySchema
  );
  export default AmazonListedReady;
  