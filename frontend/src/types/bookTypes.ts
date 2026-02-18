export interface Book{
    id: number;
    title: string;
    price: number;
}

export interface BooksData{
    books: Book[];
}