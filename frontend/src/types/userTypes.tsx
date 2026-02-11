export type UserRole = "admin" | "host" | "tenant";

export interface AuthUser {
    id: number;
    username: string;
    email: string;
    userRole: UserRole;
    isActive: boolean;
    isVerfied: boolean;
}

export interface AuthContextType{
    user: AuthUser | null;
    setUser: (user: AuthUser | null) => void;
}
