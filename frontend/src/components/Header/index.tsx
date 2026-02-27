import "./styles.scss";
import { useContext } from "react";
import { AuthContext } from "../../context/AuthProvider/AuthContext";
import { Input, Menu, UnstyledButton } from "@mantine/core";
import { Link, useNavigate } from "react-router";
import { IoSettingsOutline } from "react-icons/io5";
import { CgProfile } from "react-icons/cg";
import { LuLogOut } from "react-icons/lu";
const Header = () => {
  const context = useContext(AuthContext);

  if (context == undefined) {
    throw new Error("Auth Context error");
  }

  const { setUser } = context;

  const navigate = useNavigate();

  const handleLogOut = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("user");
    setUser(null);
    navigate("/login", { replace: true });
  };
  return (
    <div className="header-main">
      <div className="header-box">
        <a href="/">
          <p className="logo"> Book Store </p>
        </a>

        <Input type="search" placeholder="Search books" />

        <Menu shadow="md" width={200}>
          <Menu.Target>
            <div className="user-icon">U</div>
          </Menu.Target>

          <Menu.Dropdown>
            <Menu.Label>User Menu</Menu.Label>
            <Menu.Item leftSection={<CgProfile size={14} />}>
              <Link to="/profile">Profile </Link>
            </Menu.Item>
            <Menu.Item leftSection={<IoSettingsOutline size={14} />}>
              <Link to="/settings">  Settings </Link>
            </Menu.Item>
            <Menu.Item leftSection={<LuLogOut size={14} />}>
              <UnstyledButton onClick={handleLogOut}>Logout</UnstyledButton>
            </Menu.Item>
          </Menu.Dropdown>
        </Menu>
      </div>
    </div>
  );
};

export default Header;
