import mongoose from 'mongoose';

export const connectMongoDB = async () => {
    try {
        await mongoose.connect(`${process.env.MONGODB_URI}`);
        console.log('MongoDB connection established successfully.');
    } catch (error) {
        console.error('Unable to connect to MongoDB:', error);
    }
};
export default connectMongoDB;