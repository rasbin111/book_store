import { useContext } from "react";
import { AuthContext } from "../context/AuthProvider/AuthContext";
import { type AuthUser } from "../types/userTypes";

export const useAuth = () => {
  const context = useContext(AuthContext);

  if (context == undefined) {
    throw new Error("Auth context error");
  }

  const { user }: { user: AuthUser | null } = context;
  
  if (user) {
    return {
      isLoggedIn: true,
      isAdmin: user?.userRole === "admin",
      isHost: user?.userRole === "host",
      isTenant: user?.userRole === "tenant",
      canPostRoom: user?.userRole === "host" || user?.userRole === "admin",
      canBook: !!user,
    };
  }

  return {
    isLoggedIn: false,
    isAdmin: false,
    isHost: false,
    isTenant: false,
    canPostRoom: false,
    canBook: false,
  };
};

export default useAuth;
