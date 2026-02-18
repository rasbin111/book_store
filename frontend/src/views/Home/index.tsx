import { useAuth } from "../../hooks/useAuth";
import BooksHome from "./Components/Books";
import CategoryHome from "./Components/Categories";
import "./styles.scss";

const HomePage = () => {
  const { isEditor, isAdmin } = useAuth();

  return (
    <div className="home-main">
      <CategoryHome />
      <BooksHome />
      {(isEditor || isAdmin) && <div> Edit options </div>}
    </div>
  );
};

export default HomePage;
