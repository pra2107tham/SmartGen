import NextAuth from "next-auth";
import { Account, User as AuthUser } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import bcrypt from "bcryptjs";
import User from "@/app/models/User";
import connect from "@/app/utils/db";

const authOptions = {
    providers: [
        CredentialsProvider({
            id: "credentials",
            name: "Credentials",
            credentials: {
                email: { label: "Email", type: "email" },
                password: { label: "Password", type: "password" },
            },
            async authorize(credentials) {
                try {
                    await connect();
                    if(!credentials || !credentials.email || !credentials.password) {
                        throw new Error("Email and password are required");
                    }
                    const user = await User.findOne({ email: credentials.email });
                    if (!user) {
                        throw new Error("No user found");
                    }
                    const isValid = await bcrypt.compare(credentials.password, user.password);
                    if(!isValid) {
                        throw new Error("Invalid password");
                    }
                    return { id: user._id, name: user.name, email: user.email, image: user.image };
                }
                catch (error:any) {
                    throw new Error(error.message);
                }
            }
        })
    ]
}

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };
