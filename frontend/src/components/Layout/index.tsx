import { Navigate, Outlet, useNavigate } from "react-router"
import useAuth from "../../hooks/useAuth";

const Layout = () => {
    const {isLoggedIn} = useAuth();
    const navigate = useNavigate();

    if (!isLoggedIn){
        return <Navigate to="/login" replace />
    }

    const handleLogOut = () =>{
       navigate("/login", {replace: true})
    }
  return (
    <div>
        <div className="header-main">
            <button onClick={handleLogOut}> Logout</button>
        </div>
        <div className="outlet-main">
            <Outlet />
        </div>
    </div>
  )
}

export default Layout