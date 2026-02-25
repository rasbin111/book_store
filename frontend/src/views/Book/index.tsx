import { useParams } from "react-router";
import "./styles.scss";
import { useQuery } from "@apollo/client/react";
import { BOOKSBYID } from "../../graphql/book/queries";
import CustomLoadinOverlay from "../../components/CustomLoadingOverlay";
import type { BookData } from "../../types/bookTypes";
import { Carousel } from "@mantine/carousel";
import { Rating } from "@mantine/core";

const MEDIA_URL = "http://localhost:8000/media/";

const BookPage = () => {
  const { bookId } = useParams();

  const { data, loading, error } = useQuery<BookData>(BOOKSBYID, {
    variables: {
      id: bookId,
    },
  });

  if (loading) return <CustomLoadinOverlay />;
  if (error) console.log("Error(Book Page): ", error);

  return (
    <div className="book-main">
      <div className="book-container">
        {data && (
          <div className="book-item">
            <Carousel
              withIndicators
              height={250}
              slideGap="sm"
              emblaOptions={{
                loop: true,
                dragFree: true,
                align: "center",
              }}
              className="book-images"
            >
              <Carousel.Slide>
                <img
                  className="book-primary-img carousel-book-img"
                  src={
                    data.bookById.primaryImage?.imageFile
                      ? `${MEDIA_URL}${data.bookById.primaryImage.imageFile}`
                      : "/books.png"
                  }
                  alt={data.bookById.title}
                />
              </Carousel.Slide>
              {data.bookById.images.length > 0 &&
                data.bookById.images
                  .filter((image) => image.id != data.bookById.primaryImage?.id)
                  .map((image, idx: number) => {
                    return (
                      <Carousel.Slide key={idx}>
                        <img
                          className="carousel-book-img"
                          src={`${MEDIA_URL}${image.imageFile}`}
                          alt={data.bookById.title + " " + idx}
                        />
                      </Carousel.Slide>
                    );
                  })}
            </Carousel>

            <div className="book-info">
              <div className="basic-info">
                <h1>{data.bookById.title}</h1>
                <div className="basic-info-body">
                  <div className="book-rating">
                    <Rating defaultValue={4} readOnly />
                    <span> {data.bookById.numOfRatings}</span>
                  </div>
                  <p> Price: {data.bookById.price}</p>
                  <p>
                    {" "}
                    Author:{" "}
                    {data.bookById.authors.map((author) => {
                      return <span> {author.name} </span>;
                    })}
                  </p>
                  <p>
                    {" "}
                    Num of Pages: <span> {data.bookById.numOfPages} </span>
                  </p>
                  <p>
                    {" "}
                    Language:{" "}
                    <span>
                      {" "}
                      {data.bookById.language
                        ? data.bookById.language.name
                        : "English"}
                    </span>
                  </p>
                </div>
              </div>
              <div className="detail-info">
                <p> {data.bookById.description} </p>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default BookPage;
