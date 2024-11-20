import mongoose, { Schema } from 'mongoose';

const UserSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true,
        index: true
    },
    password: {
        type: String,
        required: true
    },
    instagram_connected: {
        type: Boolean,
        default: false
    },
    instagram_access_token: {
        type: String,
        required: false
    },
    instagram_id: {
        type: String,
        required: false
    },
    instagram_username: {
        type: String,
        required: false
    },
    access_token_expiry: {
        type: Date,
        required: false
    },
    media: [{
        type: Schema.Types.ObjectId,
        ref: 'Media'
    }],
    products: [{
        type: Schema.Types.ObjectId,
        ref: 'Product'
    }],
    created_at: {
        type: Date,
        default: Date.now
    }
});

export default mongoose.models.User || mongoose.model('User', UserSchema);