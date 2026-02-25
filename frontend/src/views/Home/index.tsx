import { useState } from "react";
import { useAuth } from "../../hooks/useAuth";
import BooksHome from "./Components/Books";
import CategoryHome from "./Components/Categories";
import "./styles.scss";

const HomePage = () => {

  const [category, setCategory] = useState("");

  return (
    <div className="home-main">
      <div className="main-content">
        <CategoryHome setCategory={setCategory}/>
        <BooksHome category={category}/>
      </div>
    </div>
  );
};

export default HomePage;
