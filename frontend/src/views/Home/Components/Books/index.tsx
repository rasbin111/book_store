import { useQuery } from "@apollo/client/react";
import { type BooksData } from "../../../../types/bookTypes";
import { BOOKS } from "../../../../graphql/book/queries";
import CustomLoadinOverlay from "../../../../components/CustomLoadingOverlay";
import { IoMdOptions } from "react-icons/io";
import "./styles.scss";
import { useState } from "react";
import CustomPagination from "../../../../components/Pagination";
import { useDisclosure } from "@mantine/hooks";
import { Drawer, ScrollArea, Select } from "@mantine/core";
import FilterBooks from "./filterBooks";

const MEDIA_URL = "http://localhost:8000/media/";

const BooksHome = ({category}: {category: string}) => {
  const [opened, { open, close }] = useDisclosure(false);
  const [sortValue, setSortValue] = useState("");
  const [pageSize, setPageSize] = useState(10);
  const [page, setPage] = useState(1);

  const { loading, error, data, } = useQuery<BooksData>(BOOKS, {
    variables: {
      offset: (page - 1) * pageSize,
      first: pageSize,
      categorySlug: category,
      orderBy: sortValue
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
          <Select placeholder="Sort"
           value={sortValue}
           onChange={(value)=>{
            setSortValue(value ?? "title")
           }}
           data={[
            {value: "title", label: "A - Z"},
            {value: "-title", label: "Z - A"},
            {value: "-price", label: "Price (High to Low) "},
            {value: "price", label: "Price (Low to High) "},
            {value: "-createdAt", label: "Newest"},
            {value: "createdAt", label: "Oldest"},
           ]}
           />
          <IoMdOptions size="24" className="filter-icon" onClick={open} />
          <Drawer
            opened={opened}
            onClose={close}
            position="right"
            styles={{
              content: {
                marginTop: "75px",
                borderRadius: "5px 0 0 5px"
              },
            }}
            title="Filter Books"
            scrollAreaComponent={ScrollArea.Autosize}
            
          >
            <FilterBooks />
          </Drawer>
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
                    <p className="book-price"> NRs. {book.price} </p>
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
