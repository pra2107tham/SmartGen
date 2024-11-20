import User from "@/app/models/User";
import connectMongoDB from "@/app/utils/db";
import { NextResponse } from "next/server";
import bcrypt from "bcryptjs";

export const POST = async (request: any) => {
    const { firstName, lastName, email, password } = await request.json();
    try {
        await connectMongoDB();
        
        const existingUser = await User.findOne({ email });
        if(existingUser) {
            return new NextResponse("User already exists", { status: 400 });
        }
        
        const hashedPassword = await bcrypt.hash(password, 12);
        const name = `${firstName} ${lastName}`;
        const user = new User({ name, email, password: hashedPassword });
        await user.save();

        return new NextResponse("User created", { status: 201 });
    } catch (error: any) {
        console.error(error);
        return new NextResponse(error.message || "Internal Server Error", { status: 500 });
    }
}
