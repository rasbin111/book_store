import { Navigate, Outlet, useNavigate } from "react-router";
import useAuth from "../../hooks/useAuth";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthProvider/AuthContext";

const Layout = () => {
  const { isLoggedIn } = useAuth();
  const navigate = useNavigate();
  const context = useContext(AuthContext);

  if (context == undefined) {
    throw new Error("Auth Context error");
  }

  const { setUser } = context;

  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }

  const handleLogOut = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    setUser(null);
    navigate("/login", { replace: true });
  };
  return (
    <div>
      <div className="header-main">
        <button onClick={handleLogOut}> Logout</button>
      </div>
      <div className="outlet-main">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
