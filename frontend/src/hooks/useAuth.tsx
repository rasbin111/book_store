import { useContext } from "react";
import { AuthContext } from "../context/AuthProvider/AuthContext";
import { type AuthUser } from "../types/userTypes";

export const useAuth = () => {
  const context = useContext(AuthContext);

  if (context == undefined) {
    throw new Error("Auth context error");
  }

  const { user }: { user: AuthUser | null } = context;
  console.log(user);
  if (user) {
    return {
      isLoggedIn: true,
      isAdmin: user?.role === "ADMIN",
      isEditor: user?.role === "EDITOR",
      isViewer: user?.role === "VIEWER",
    };
  }

  return {
    isLoggedIn: false,
    isAdmin: false,
    isEditor: false,
    isViewer: false,
  };
};

export default useAuth;
