import { useQuery } from "@apollo/client/react";
import { type BooksData } from "../../../../types/bookTypes";
import { BOOKS } from "../../../../graphql/book/queries";
import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";
import { IoMdOptions } from "react-icons/io";

import "./styles.scss";
import { useState } from "react";
import CustomPagination from "../../../../components/Pagination";

const MEDIA_URL = "http://localhost:8000/media/";

const BooksHome = () => {
  const [pageSize, setPageSize] = useState(10);
  const [page, setPage] = useState(1);

  const { loading, error, data } = useQuery<BooksData>(BOOKS, {
    variables: {
      offset: (page - 1) * pageSize,
      first: pageSize,
    },
  });

  if (loading) return <CustomLoadinOverlay />;
  if (error) console.log(error);

  return (
    <div className="book-home">
      <div className="book-home-nav">
        <div className="book-home-nav-left">
          <h2> Books </h2>
        </div>
        <div className="book-home-nav-right">
          <IoMdOptions size="24" />
        </div>
      </div>
      <div className="book-home-body">
        <ul className="book-list">
          {data &&
            data.books?.edges?.length > 0 &&
            data.books?.edges?.map((item) => {
              const book = item.node;

              return (
                <li className="book-item">
                  <div className="book-img">
                    <img
                      src={
                        book.primaryImage?.imageFile
                          ? `${MEDIA_URL}${book.primaryImage.imageFile}`
                          : "/books.png"
                      }
                      alt={book.title}
                    />
                  </div>
                  <div className="book-info">
                    <a href="">{book.title}</a>
                    <p> {book.price} </p>
                    <ul>
                      {book.authors.length > 1 ? `Authors` : `Author:`}
                      {book.authors.length > 0 ? (
                        book.authors?.map((author) => {
                          return <li> - {author.name} </li>;
                        })
                      ) : (
                        <li> - Unknown </li>
                      )}
                    </ul>
                    <p className="lang">Language: {book.language.name} </p>
                  </div>
                </li>
              );
            })}
        </ul>
        {data && (
          <CustomPagination
            totalCount={data.books.totalCount}
            pageSize={pageSize}
            activePage={page}
            setPage={setPage}
          />
        )}
      </div>
    </div>
  );
};

export default BooksHome;
