import { createContext } from "react";
import { type AuthContextType } from "../../types/userTypes";

export const AuthContext = createContext<AuthContextType | undefined>(undefined);
