import psycopg2
from tkinter import *
windows = Tk()
windows.geometry("800x600")
host_name = "localhost"
data_base = "LIBRARY"
user_name = "postgres"
password = "123456"
port_id = 5432
conn = psycopg2.connect(host = host_name, dbname = data_base, user = user_name, password = password, port = port_id)
cur = conn.cursor()


class Book:
    def __init__(self, name, author, genre):
        self.name = name
        self.author = author
        self.genre = genre

def insert_book(book, cur):
    insert_query = '''
    insert into books(
    name, author, genre) values(
    ''' +"'"+ book.name +"'"+ "," + "'"+book.author +"'"+ "," + "'"+book.genre +"'"+ ")"
    cur.execute(insert_query)
def show_all(cur):
    cur.execute("select * from Books")
    for record in cur.fetchall():
        print(record[0], record[1], record[2])
def find_book_by_name(name, cur):
    query = "select * from Books where name = " + "'"+ name +"'"
    cur.execute(query)
    d = cur.fetchone()
    book = Book(d[0], d[1], d[2])
    return book
def find_all_books_by_auothor(auothor, cur):
    query = "select * from Books where author = " + "'" + auothor + "'"
    cur.execute(query)
    d = cur.fetchall()
    l = []
    for value in d:
        book = Book(value[0], value[1], value[2])
        l.append(book)
    return l
def delete_book(name, cur):
    delete_query = "delete from Books where name = " + "'" + name + "'"
    cur.execute(delete_query)

def save_book():
    title = ent_book_name.get()
    auothor = ent_author_name.get()
    genre = ent_genre_name.get()
    new_book = Book(title, auothor, genre)
    insert_book(new_book, cur)
    ent_book_name.delete(0, END)
    ent_author_name.delete(0, END)
    ent_genre_name.delete(0, END)

def search_book():
    title = ent_book_name_find.get()
    book = find_book_by_name(title, cur)
    Label(windows, text="I found your book: " + title + " Author:" + book.author + "Genre:" + book.genre, font="arial 11").place(x=60, y=220)

def search_all_by_author():
    author = ent_book_author_find.get()
    books = find_all_books_by_auothor(author,cur)
    i = 320
    for book in books:
        Label(windows, text="I found your book: " + book.name + " Author:" + author + "Genre:" + book.genre,
              font="arial 11").place(x=90, y=i)
        i = i + 20

def book_delete():
    title = ent_book_delete.get()
    delete_book(title,cur)
    ent_book_delete.delete(0,END)

windows.title("Library")
Label(windows, text = "Insert book:", font = "arial 17 bold").place(x = 40, y = 30)
ent_book_name = Entry(windows,width = 53)
Label(windows, text = "Title: ", font = "arial 13").place(x = 40,y = 60)
ent_book_name.place(x = 85, y = 60)
ent_author_name = Entry(windows,width = 50)
Label(windows, text = "Author: ", font = "arial 13").place(x = 40,y = 85)
ent_author_name.place(x = 105, y = 85)
ent_genre_name = Entry(windows,width = 50)
Label(windows, text = "Genre: ", font = "arial 13").place(x = 40,y = 110)
ent_genre_name.place(x = 103, y = 110)
Button(windows, text = "Save book", font = "arial 10 bold", background = "red", foreground = "white", command = save_book).place(x = 40, y = 145)

Label(windows, text = "Find book by title:", font = "arial 17 bold").place(x = 40, y = 175)
ent_book_name_find = Entry(windows,width = 53)
Label(windows, text = "Title: ", font = "arial 13").place(x = 40,y = 205)
ent_book_name_find.place(x = 85, y = 205)
Button(windows, text = "Submit", font = "arial 10 bold", background = "red", foreground = "white", command = search_book).place(x = 40, y = 240)

Label(windows, text = "Find all books by author:", font = "arial 17 bold").place(x = 40, y = 275)
ent_book_author_find = Entry(windows,width = 53)
Label(windows, text = "Author: ", font = "arial 13").place(x = 40,y = 305)
ent_book_author_find.place(x = 120, y = 305)
Button(windows, text = "Submit", font = "arial 10 bold", background = "red", foreground = "white", command = search_all_by_author).place(x = 40, y = 340)

Label(windows, text = "Delete book:", font = "arial 17 bold").place(x = 40, y = 375)
ent_book_delete = Entry(windows,width = 53)
Label(windows, text = "Title: ", font = "arial 13").place(x = 40,y = 405)
ent_book_delete.place(x = 85, y = 405)
Button(windows, text = "Submit", font = "arial 10 bold", background = "red", foreground = "white",command = book_delete).place(x = 40, y = 440)



windows.mainloop()

conn.commit()
cur.close()
conn.close()