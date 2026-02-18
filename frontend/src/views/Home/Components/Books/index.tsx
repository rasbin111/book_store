import { useQuery } from "@apollo/client/react";
import { type BooksData } from "../../../../types/bookTypes";
import { BOOKS } from "../../../../graphql/book/queries";
import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";

import "./styles.scss";

const MEDIA_URL = "http://localhost:8000/media/";

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
              <li className="book-item">
                <div className="book-img">
                  <img
                    src={
                      item.primaryImage?.imageFile
                        ? `${MEDIA_URL}${item.primaryImage.imageFile}`
                        : "/books.png"
                    }
                    alt={item.title}
                  />
                </div>
                <div className="book-info">
                  <a href="">{item.title}</a>
                  <p> {item.price} </p>
                  <ul>
                    {item.authors.length > 1? `Authors`: `Author:`} 
                    {item.authors.length > 0? (item.authors?.map((author)=>{
                      return <li> - {author.name} </li>
                    })): <li> - Unknown </li>}
                  </ul>
                  <p className="lang">Language: {item.language.name} </p>
                </div>
              </li>
            );
          })}
      </ul>
    </div>
  );
};

export default BooksHome;
