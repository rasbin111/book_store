import { gql } from "@apollo/client";

// export const BOOKS = gql`
//     query bookList {
//         books {
//             id
//             title
//             price
//             authors {
//                 id
//                 name
//             }
//             primaryImage {
//                 imageFile
//             }
//             language {
//                 name
//             }
//         }
//     }
// `

export const BOOKS = gql`
query bookList($offset: Int!, $first: Int!, $categorySlug: String, $orderBy: String) {
  books(offset:$offset, first:$first, categorySlug: $categorySlug, orderBy: $orderBy ){
    totalCount
    pageInfo{
      hasNextPage
      hasPreviousPage
    }
    edges {
      node {
        id
        title
        price
        authors{
          id
          name
        }
        primaryImage{
          imageFile
        }
        language{
          name
        }
      }
    }
  }
}
`

export const BOOKSBYID = gql`
  query bookById($id:ID!){
    bookById(id: $id){
      id
      title
      price
      description
      numOfRatings
      numOfPages
      averageRating
      primaryImage{
          id
          imageFile
      }
      images{
        id
        imageFile
      }
      authors{
        id
        name
      }
    }
  }
`