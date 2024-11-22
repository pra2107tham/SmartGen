const RefinedProductSchema = new Schema({
    user_id: {
      type: Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    media_files: {
      type: [Schema.Types.ObjectId],
      ref: "Media", // Links back to media entries
      required: true,
    },
    media_type: {
        type: String,
        enum: ["image", "video"],
        required: true,
    },
    media_url: {
        type: String,
        required: true,
    },
    product_name: {
      type: String,
      required: true,
    },
    description: {
      type: String,
    },
    keywords: {
      type: [String],
    },
    category: {
      type: String,
      required: true,
    },
    processed_at: {
      type: Date,
      default: Date.now,
    },
    amazon_ready_product: {
      type: Schema.Types.ObjectId,
      ref: "AmazonListedReady", // Links to the Amazon Listed Ready schema,
      required: false,
    },
  });
  
  const RefinedProduct = mongoose.model("RefinedProduct", RefinedProductSchema);
  export default RefinedProduct;  