import csv
import json
from libros import Libros


def load_books():
    books = []

    with open(r'C:\Users\alejo\PycharmProjects\pythonProject\Modelo Final\books.csv', 'r') as file:
        rows = csv.DictReader(file)
        for row in rows:
            books.append(Libros(
                row['ISBN'],
                row['title'],
                row['author'],
                row['price'],
                row['published'],
                row['language'],
                row['number_pages'],
                row['press'],
                row['ranking']
            ))
        return books


def save_purchase_order(purchase):
    with open(r'C:\Users\alejo\PycharmProjects\pythonProject\Modelo Final\pruchase_order.csv', 'a') as purchase_file:
        header = ['purchase_date', 'ISBN', 'user_id', 'full_address']
        writer = csv.DictWriter(purchase_file, fieldnames=header)

        if purchase_file.tell() == 0:
            writer.writeheader()

        writer.writerow(purchase)
