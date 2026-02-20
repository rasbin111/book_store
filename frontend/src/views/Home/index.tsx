import { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import BooksHome from "./Components/Books";
import CategoryHome from "./Components/Categories";
import "./styles.scss";

const HomePage = () => {
  const { isEditor, isAdmin } = useAuth();
  const [category, setCategory] = useState("");

  return (
    <div className="home-main">
      <div className="main-content">
        <CategoryHome setCategory={setCategory}/>
        <BooksHome category={category}/>
      </div>
      {(isEditor || isAdmin) && <div> Edit options </div>}
    </div>
  );
};

export default HomePage;
