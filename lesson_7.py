# import sqlite3
#
#
# def create_connection(db_file):
#     connection = None
#     try:
#         connection = sqlite3.connect(db_file)
#     except sqlite3.Error as error:
#         print(f'{error} in create_connection function')
#     return connection
#
#
# def create_table(connection, create_table_sql):
#     try:
#         cursor = connection.cursor()
#         cursor.execute(create_table_sql)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in create_table function')
#
#
# def add_product(connection, product):
#     sql = '''INSERT INTO products (product_title, price, quantity)
#              VALUES (?, ?, ?)'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in add_product function')
#
#
# def id_update(connection, product):
#     sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in id_update function')
#
#
# def update_price(connection, product):
#     sql = '''UPDATE products SET price = ? WHERE id = ?'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, product)
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in update_price function')
#
#
# def delete_product(connection, id):
#     sql = '''DELETE FROM products WHERE id = ?'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, (id,))
#         connection.commit()
#     except sqlite3.Error as error:
#         print(f'{error} in delete_product function')
#
#
# def print_all_products(connection):
#     sql = '''SELECT * FROM products'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in print_all_products function')
#
#
# def select_(connection, price_limit, quantity_limit):
#     sql = '''SELECT * FROM products WHERE price <= ? AND quantity >= ?'''
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql, (price_limit, quantity_limit))
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in select function')
#
#
# def search_by_word(conn, word):
#     try:
#         sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
#         cursor = conn.cursor()
#         cursor.execute(sql, ('%' + word + '%',))
#
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)
#     except sqlite3.Error as error:
#         print(f'{error} in search_by_word function')
#
#
# sql_products = '''
# CREATE TABLE IF NOT EXISTS products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_title TEXT NOT NULL,
#     price REAL NOT NULL DEFAULT 0.0,
#     quantity INTEGER DEFAULT 0
# )
# '''
#
# my_conn = create_connection('hw.db')
#
# if my_conn is not None:
#     print('Successfully connected to database')
#
#     create_table(my_conn, sql_products)
#
#     products_to_add = [
#         ('Broccoli', 200.0, 5),
#         ('Spinach', 70.0, 45),
#         ('Radish', 40.0, 20),
#         ('Zucchini', 35.0, 50),
#         ('Lettuce', 25.0, 30),
#         ('Ginger', 60.0, 25),
#         ('Chili', 90.0, 15),
#         ('Pear', 130.0, 10),
#         ('Grapes', 100.0, 20),
#         ('Mango', 140.0, 12),
#         ('Kiwi', 85.0, 18),
#         ('Plum', 160.0, 8),
#         ('Melon', 280.0, 5),
#         ('Coconut', 220.0, 6),
#         ('Blueberry', 200.0, 7)
#     ]
#
#     for product in products_to_add:
#         add_product(my_conn, product)
#
#     id_update(my_conn, (10, 1))
#     update_price(my_conn, (100.0, 1))
#     delete_product(my_conn, 2)
#
#     print("\nВсе товары:")
#     print_all_products(my_conn)
#
#     print("\nТовары с ценой <= 100 и количеством >= 5:")
#     select_(my_conn, 100.0, 5)
#
#     print("\nИщем товары с ключевым словом 'Tomato':")
#     search_by_word(my_conn, 'Tomato')
#
#     my_conn.close()


