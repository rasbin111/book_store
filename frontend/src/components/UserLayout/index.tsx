import "./styles.scss";
import { Navigate, Outlet } from "react-router";
import useAuth from "../../hooks/useAuth";

import Header from "../Header";
import Footer from "../Footer";

const UserLayout = () => {
  const { isLoggedIn } = useAuth();


  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }



  return (
    <div>
      <Header/>
      <div className="outlet-main">
        <Outlet />
      </div>
      <Footer/>
    </div>
  );
};

export default UserLayout;
