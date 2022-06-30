class Libros:
    def __init__(self, isbn, title, author, price, published, language, number_pages, press, ranking):
        self.ISBN = isbn
        self.title = title
        self.author = author
        self.price = price
        self.published = published
        self.language = language
        self.number_pages = number_pages
        self.press = press
        self.ranking = ranking

    def serialize(self):
        return {
            'ISBN': self.ISBN,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            }


    def serialize_details(self):
        return {
            'ISBN': self.ISBN,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'published': self.published,
            'language': self.language,
            'number of pages': self.number_pages,
            'press': self.press,
            'ranking': self.ranking
        }