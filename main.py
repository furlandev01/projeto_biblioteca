import sqlite3
from tkinter import *
from tkinter import messagebox

# Conexão com o banco de dados
def create_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        quantity INTEGER NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        email TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS loans (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book_id INTEGER NOT NULL,
                        user_id INTEGER NOT NULL,
                        FOREIGN KEY (book_id) REFERENCES books (id),
                        FOREIGN KEY (user_id) REFERENCES users (id_user))''')
    conn.commit()
    conn.close()

# Funções para o gerenciamento de livros
def add_book_ui():
    def add_book():
        title = title_entry.get()
        author = author_entry.get()
        year = year_entry.get()
        quantity = quantity_entry.get()
        
        if title and author and year.isdigit() and quantity.isdigit():
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year, quantity) VALUES (?, ?, ?, ?)", 
                           (title, author, int(year), int(quantity)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
            add_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

    add_window = Toplevel(root)
    add_window.title("Adicionar Livro")

    Label(add_window, text="Título:").pack()
    title_entry = Entry(add_window)
    title_entry.pack()

    Label(add_window, text="Autor:").pack()
    author_entry = Entry(add_window)
    author_entry.pack()

    Label(add_window, text="Ano:").pack()
    year_entry = Entry(add_window)
    year_entry.pack()

    Label(add_window, text="Quantidade:").pack()
    quantity_entry = Entry(add_window)
    quantity_entry.pack()

    Button(add_window, text="Adicionar", command=add_book).pack()

def view_books_ui():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()

    view_window = Toplevel(root)
    view_window.title("Lista de Livros")

    for book in books:
        Label(view_window, text=f"ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Ano: {book[3]}, Quantidade: {book[4]}").pack()

def remove_book_ui():
    def remove_book():
        book_id = book_id_entry.get()
        if book_id.isdigit():
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM books WHERE id=?", (int(book_id),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
            remove_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, insira um ID válido.")

    remove_window = Toplevel(root)
    remove_window.title("Remover Livro")

    Label(remove_window, text="ID do Livro:").pack()
    book_id_entry = Entry(remove_window)
    book_id_entry.pack()

    Button(remove_window, text="Remover", command=remove_book).pack()

# Funções para gerenciamento de usuários
def add_user_ui():
    def add_user():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        
        if name and phone and email:
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, phone, email) VALUES (?, ?, ?)", 
                           (name, phone, email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            add_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

    add_window = Toplevel(root)
    add_window.title("Adicionar Usuário")

    Label(add_window, text="Nome:").pack()
    name_entry = Entry(add_window)
    name_entry.pack()

    Label(add_window, text="Celular:").pack()
    phone_entry = Entry(add_window)
    phone_entry.pack()

    Label(add_window, text="Email:").pack()
    email_entry = Entry(add_window)
    email_entry.pack()

    Button(add_window, text="Adicionar", command=add_user).pack()

def view_users_ui():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    view_window = Toplevel(root)
    view_window.title("Lista de Usuários")

    for user in users:
        Label(view_window, text=f"ID: {user[0]}, Nome: {user[1]}, Celular: {user[2]}, Email: {user[3]}").pack()

def remove_user_ui():
    def remove_user():
        user_id = user_id_entry.get()
        if user_id.isdigit():
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id_user=?", (int(user_id),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
            remove_window.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, insira um ID válido.")

    remove_window = Toplevel(root)
    remove_window.title("Remover Usuário")

    Label(remove_window, text="ID do Usuário:").pack()
    user_id_entry = Entry(remove_window)
    user_id_entry.pack()

    Button(remove_window, text="Remover", command=remove_user).pack()

# Configuração da Janela Principal
root = Tk()
root.title("Sistema de Biblioteca")
root.geometry("600x400")

Button(root, text="Adicionar Livro", command=add_book_ui).pack(pady=10)
Button(root, text="Ver Livros", command=view_books_ui).pack(pady=10)
Button(root, text="Remover Livro", command=remove_book_ui).pack(pady=10)
Button(root, text="Adicionar Usuário", command=add_user_ui).pack(pady=10)
Button(root, text="Ver Usuários", command=view_users_ui).pack(pady=10)
Button(root, text="Remover Usuário", command=remove_user_ui).pack(pady=10)

create_db()
root.mainloop()