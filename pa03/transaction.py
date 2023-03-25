'''
transaction.py is an Object Relational Mapping to the transaction database

The ORM will work map SQL rows with the schema

to Python Dictrionaries as follows:
('item #', 'amount', 'category', 'date', 'description'),
'''
import sqlite3
import os

def toDict(t):
    '''t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    todo = {'item_number':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return todo

class Transaction():
    def __init__(self, db_location):
        self.conn = sqlite3.connect(db_location)
        self.cursor.execute('''CREAT TABLE IF NOT EXISTS transactions (
        item_number INTEGER,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
        )
        ''')
        self.conn.commit()
    
    def show_categories(self):
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        rows = self.cursor.fetchall()
        categories = [row[0] for row in rows]
        return categories

    def add_category(self):
        self.cursor.execute('INSERT INTO transactions (category) VALUES (?)', (category,))
        self.conn.commit()

    def modify_category(self, old, new):
        self.cursor.execute('UPDATE transactions SET category=? WHERE category=?', (new, old))
        self.conn.commit()

    def show_transactions(self):
        self.cursor.execute('SELECT * FROM transactions')
        rows = self.cursor.fetchall()
        transactions = [toDict(row) for row in rows]
        return transactions

    def add_transaction(self, transaction):
        self.cursor.execute('INSERT INTO transactions VALUES(?,?,?,?,?)', (transaction['item_number'], transaction['amount'], transaction['category'], transaction['date'], transaction['description']))
        self.conn.commit()

    def delete_transaction(self, number):
        self.cursor.commit('DELETE FROM transactions where item_n')
