import mongoose from "mongoose";
const { Schema } = mongoose;

const MediaSchema = new Schema({
  user_id: {
    type: Schema.Types.ObjectId,
    ref: "User",
    required: true,
  },
  media_id: {
    type: String,
    required: true
  },
  media_type: {
    type: String,
    enum: ["image", "video"],
    required: true,
  },
  media_url: {
    type: [String],
    required: true,
  },
  caption: {
    type: String,
  },
  hashtags: {
    type: [String],
  },
  engagement_metrics: {
    likes: {
      type: Number,
      default: 0,
    },
    comments: {
      type: Number,
      default: 0,
    },
  },
  created_at: {
    type: Date,
    default: Date.now,
  },
  processed: {
    type: Boolean,
    default: false,
  },
  refined_product: {
    type: Schema.Types.ObjectId,
    ref: "RefinedProduct", // Links to Refined Product schema
  },
});

const Media = mongoose.model("Media", MediaSchema);
export default Media;