import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";
import { CATEGORIES } from "../../../../graphql/category/queries";

import { useQuery } from "@apollo/client/react";
import "./styles.scss";
import { type CategoriesData } from "../../../../types/categoryTypes";
import { UnstyledButton } from "@mantine/core";

const CategoryHome = ({
  setCategory,
}: {
  setCategory: (category: string) => void;
}) => {
  const { loading, error, data } = useQuery<CategoriesData>(CATEGORIES);

  if (loading) return <CustomLoadinOverlay />;
  if (error) console.log(error);
  return (
    <div className="category-home">
      <div className="category-container">
        <h2> Categories </h2>
        <ul className="category-list">
          <li>
            <UnstyledButton onClick={() => setCategory("")}>
              {" "}
              All{" "}
            </UnstyledButton>
          </li>
          {data &&
            data.categories.length > 0 &&
            data.categories.map((item) => {
              return (
                <li>
                  <UnstyledButton onClick={() => setCategory(item.name)}>
                    {item.name}
                  </UnstyledButton>
                </li>
              );
            })}
        </ul>
      </div>
    </div>
  );
};

export default CategoryHome;
