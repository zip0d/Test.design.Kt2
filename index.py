import json
import csv
from csv import DictReader
import os.path
import math

DIRECTORY_PATH = os.path.dirname(__file__)

def get_file_path(file_name: str):
    return os.path.join(DIRECTORY_PATH, file_name)

JSON_FILE_PATH = get_file_path(file_name="users.json")
CSV_FILE_PATH = get_file_path(file_name="books.csv")

with open(CSV_FILE_PATH, newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)
    books_data = []
    for row in csv_reader:
        books_data.append(dict(zip(csv_header, row)))

with open(JSON_FILE_PATH, "r") as json_file:
    users_data = json.loads(json_file.read())

num_users = len(users_data)
num_books = len(books_data)
difference = math.floor(num_books / num_users)

user_index = 0
for i in range(0, num_books + difference - 1, difference):
    print("ind: ", i, "user: ", user_index)
    if user_index == num_users:
        break
    users_data[user_index]["BOOKS"] = []
    for book_index in range(i, i + difference):
        users_data[user_index]["BOOKS"].append(books_data[book_index])
    user_index += 1

for i in range(0, num_users):
    if user_index * difference + i < num_books:
        users_data[i]["BOOKS"].append(books_data[user_index * difference + i])

with open("result.json", "w") as result_file:
    json_string = json.dumps(users_data, indent=4)
    result_file.write(json_string)
