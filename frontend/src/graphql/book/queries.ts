import { gql } from "@apollo/client";

export const BOOKS = gql`
    query bookList {
        books {
            id
            title
            price
            authors {
                id
                name
            }
            primaryImage {
                imageFile
            }
            language {
                name
            }
        }
    }
`