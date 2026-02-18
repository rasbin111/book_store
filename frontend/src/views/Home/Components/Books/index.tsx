import { useQuery } from "@apollo/client/react";
import { type BooksData } from "../../../../types/bookTypes";
import { BOOKS } from "../../../../graphql/book/queries";
import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";

import "./styles.scss";

const BooksHome = () => {
  const { loading, error, data } = useQuery<BooksData>(BOOKS);

  if (loading) return <CustomLoadinOverlay />;
  if (error) console.log(error);

  return (
    <div className="book-home">
      <h2> Books </h2>
      <ul className="book-list">
        {data &&
          data.books.length > 0 &&
          data.books.map((item) => {
            return (
              <li>
                <a href="">{item.title}</a>
                <p> {item.price} </p>
              </li>
            );
          })}
      </ul>
    </div>
  );
};

export default BooksHome;
