import { useState, type ReactNode } from "react";
import { type AuthUser } from "../../types/userTypes";
import { AuthContext } from "./AuthContext";


export const AuthProvider = ({children}: {children: ReactNode}) =>{
    const [user, setUser] = useState<AuthUser | null>(() => {
        const storedUser = localStorage.getItem("user");

        if (storedUser){
            try{
                return JSON.parse(storedUser);
            } catch(error){
                console.error("Auth initialization error: ", error)
                return null;
            }
        }
        return null;
    });

    return (
        <AuthContext.Provider value={{user, setUser}}>
            {children}
        </AuthContext.Provider>
    )
}