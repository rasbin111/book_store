
def increase_book_review(sender, instance, created, **kwargs):
    book = instance.book

    book_reviews_count = book.reviews.filter(is_deleted=False).count()
    book.num_of_ratings = book_reviews_count
    
    reviews = book.reviews.filter(is_deleted=False)

    total_rating = 0
    for review in reviews:
        total_rating += review.rating
    if book.num_of_ratings > 0:
        book.average_rating =  total_rating / book.num_of_ratings
    else:
        pass
    
    book.save()


def decrease_book_review(sender, instance, **kwargs):
    book = instance.book
    book_reviews_count = book.reviews.filter(is_deleted=False).count()

    book.num_of_ratings = book_reviews_count
    reviews = book.reviews.filter(is_deleted=False)

    total_rating = 0
    for review in reviews:
        total_rating += review.rating

    if book.num_of_ratings > 0:
        book.average_rating =  total_rating / book.num_of_ratings
    else:
        pass

    book.save()