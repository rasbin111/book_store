export type UserRole = "ADMIN" | "EDITOR" | "VIEWER";

export interface AuthUser {
    id: number;
    username: string;
    email: string;
    role: UserRole;
    isActive: boolean;
    isVerfied: boolean;
}

export interface AuthContextType{
    user: AuthUser | null;
    setUser: (user: AuthUser | null) => void;
}
