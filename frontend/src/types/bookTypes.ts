import { type AuthorType } from "./authorTypes";
import { type Language } from "./languageType";
import { type AuthUser } from "./userTypes";

interface BookImage{
    id: number;
    isPrimary: boolean;
    imageFile: string;
}

export interface Book{
    id: number;
    title: string;
    price: number;
    review_stars: number;
    images: BookImage[];
    primaryImage: BookImage | null;
    authors: AuthorType[];
    language: Language;
    addedBy: AuthUser;
    numOfRatings: number;
    averageRating: number;
    numOfPages: number;
    description: string;
}

interface BookNode{
    node: Book;
}

interface BookEdges{
    edges: BookNode[];
    totalCount: number;
}

export interface BooksData{
    books: BookEdges;
}

export interface BookData{
    bookById: Book;
}
