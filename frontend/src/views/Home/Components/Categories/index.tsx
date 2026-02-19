import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";
import { CATEGORIES } from "../../../../graphql/category/queries";

import { useQuery } from "@apollo/client/react";
import "./styles.scss";
import { type CategoriesData } from "../../../../types/categoryTypes";

const CategoryHome = () => {
  const { loading, error, data } = useQuery<CategoriesData>(CATEGORIES);

  if (loading) return <CustomLoadinOverlay />;
  if (error) console.log(error);
  return (
    <div className="category-home">
      <h2> Categories </h2>
      <ul className="category-list">
        {data &&
          data.categories.length > 0 &&
          data.categories.map((item) => {
            return (
              <li>
                <a href="">{item.name}</a>
              </li>
            );
          })}
      </ul>
    </div>
  );
};

export default CategoryHome;
