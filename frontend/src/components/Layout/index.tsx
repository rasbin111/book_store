import "./styles.scss";
import { Navigate, Outlet, useNavigate } from "react-router";
import useAuth from "../../hooks/useAuth";
import { useContext, useState } from "react";
import { AuthContext } from "../../context/AuthProvider/AuthContext";
import { Button, Input } from "@mantine/core";

const Layout = () => {
  const { isLoggedIn } = useAuth();
  const navigate = useNavigate();
  const [showUserMenu, setShowUserMenu] = useState(false);
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
        <div className="header-box">
          <a href="/">
            <p className="logo"> Book Store </p>
          </a>

          <Input type="search" placeholder="Search books" />

          <div
            onClick={() => setShowUserMenu((prev) => !prev)}
            className="user-icon"
          >
            U
          </div>
        </div>
        {showUserMenu && <Button onClick={handleLogOut}> Logout</Button>}
      </div>
      <div className="outlet-main">
        <Outlet />
      </div>
    </div>
  );
};

export default Layout;
