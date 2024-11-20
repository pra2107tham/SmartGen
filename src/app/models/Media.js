import { Schema } from 'mongoose';

const MediaSchema = new Schema({
    user_id: { 
        type: Schema.Types.ObjectId, 
        ref: 'User', 
        required: true 
    },
    media_type: { 
        type: String, 
        enum: ['image', 'video'], 
        required: true 
    },
    media_url: { 
        type: String, 
        required: true 
    },
    caption: { 
        type: String 
    },
    hashtags: { 
        type: [String] 
    },
    engagement_metrics: {
        likes: { 
            type: Number, 
            default: 0 
        },
        comments: { 
            type: Number, 
            default: 0 
        }
    },
    created_at: { 
        type: Date, 
        default: Date.now 
    },
    processed: { 
        type: Boolean, 
        default: false 
    },
    connected_product: { 
        type: Schema.Types.ObjectId, 
        ref: 'Product' 
    }
});

export default mongoose.models.Media || mongoose.model('Media', MediaSchema);