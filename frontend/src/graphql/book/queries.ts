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
query bookList($offset: Int!, $first: Int!) {
  books(offset:$offset, first:$first){
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