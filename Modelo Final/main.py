from flask import Flask, jsonify, request
# importamos de la libreria flask el constructor Flask
from load_books import load_books, save_purchase_order

app = Flask(__name__)
# con el constructor creamos una instancia de un objeto especial y la guardamos en la variable llamada app

libros = load_books()


# [GET]

@app.route('/api/academic-books/books', methods=['GET'])
def get_books():
    language_param = request.args.get('language', '')

    language_books = []

    if language_param == 'ES' or language_param == 'EN':
        for book in libros:
            if book.language == language_param:
                language_books.append(book)
        return jsonify([li.serialize() for li in language_books])
    else:
        return jsonify([li.serialize() for li in libros])


@app.route('/api/academic-books/books/<ISBN>', methods=['GET'])
def get_books_details(ISBN):
    selected_book = []
    for book in libros:
        if book.ISBN == ISBN:
            selected_book.append(book)
            return jsonify([li.serialize_details() for li in selected_book])
        else:
            return jsonify(status=404, description='Book not found'), 404


# POST

@app.route('/api/academic-books/purchase-orders', methods=['POST'])
def create_purchase_orders():

    if request.args['user_id']:
        req_json = request.json
        save_purchase_order(req_json)

        return jsonify({'Purchase Order': req_json})

    else:
        return jsonify(status=404, description= "User not found"), 404



if __name__ == '__main__':
    app.run(debug=True, port=5000)
