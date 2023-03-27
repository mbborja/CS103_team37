'''
transaction.py is an Object Relational Mapping to the tracker database

The ORM will work map SQL rows with the schema

to Python Dictrionaries as follows:
('item #', 'amount', 'category', 'date', 'description'),
'''
import sqlite3

def to_dict(t):
    '''t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    transaction = {'item_number':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

class Transaction():
    def __init__(self, db_location):
        '''
        Initializes Transaction Class with db file location
        '''
        self.con = sqlite3.connect(db_location)
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
            item_number INTEGER,
            amount REAL,
            category TEXT,
            date TEXT,
            description TEXT
            )
            '''
        )
        self.con.commit()
    
    def print_menu(self):
        '''
        Prints a menu of all available commands
        '''
        print('''1. show categories
        2. add category
        3. modify category
        4. show transactions
        5. add transaction
        6. delete transaction
        7. summarize transactions by date
        8. summarize transactions by month
        9. summarize transactions by year
        10. summarize transactions by category''')

    def show_categories(self):
        '''
        Shows the distict categories stored in the db
        '''
        self.cursor.execute('SELECT DISTINCT category FROM transactions')
        rows = self.cursor.fetchall()
        categories = [row[0] for row in rows]
        return categories

    def add_category(self, category):
        '''
        Adds categories into the db
        '''
        self.cursor.execute('INSERT INTO transactions (category) VALUES (?)', (category))
        self.con.commit()

    def modify_category(self, old, new):
        '''
        Modifies category to new category
        '''
        self.cursor.execute('UPDATE transactions SET category=? WHERE category=?', (new, old))
        self.con.commit()

    def show_transactions(self):
        '''
        Returns all transactions as a dict
        '''
        self.cursor.execute('SELECT * FROM transactions')
        rows = self.cursor.fetchall()
        transactions = [to_dict(row) for row in rows]
        return transactions

    def add_transaction(self, transaction):
        '''
        Adds a transaction
        '''
        self.cursor.execute('INSERT INTO transactions VALUES(?,?,?,?,?)', (transaction['item_number'], transaction['amount'], transaction['category'], transaction['date'], transaction['description']))
        self.con.commit()

    def delete_transaction(self, number):
        '''
        Deletes a transaction with a specified number
        '''
        self.cursor.execute('DELETE FROM transactions WHERE item_number=?', (number))
        self.con.commit()

    def summarize_by_date(self):
        '''
        Summarizes all transactions by date. Date: ?, total: ?
        '''
        self.cursor.execute('SELECT date, SUM(amount) FROM transactions GROUP BY date')
        rows = self.cursor.fetchall()
        sum = [{'date': row[0], 'total': row[1]} for row in rows]
        return sum

    def summarize_by_month(self): #Noah - DATES MUST BE FORMATTED AS MM*DD*YYYY WHERE * CAN BE ANY CHARACTER
        '''
        Summarizes all transactions by date. MONTH: ?, total: ?
        '''
        self.cursor.execute('SELECT SUBSTR(date, 1, 2) AS month, SUM(amount) FROM transactions GROUP BY month')
        rows = self.cursor.fetchall()
        sum = [{'month': row[0], 'total': row[1]} for row in rows]
        return sum
    
    def summarize_by_year(self): #Noah   
        '''
        Summarizes all transactions by date. YEAR: ?, total: ?
        '''
        self.cursor.execute('SELECT SUBSTR(date, 7, 10) AS year, SUM(amount) FROM transactions GROUP BY year')
        rows = self.cursor.fetchall()
        sum = [{'year': row[0], 'total': row[1]} for row in rows]
        return sum
    
    def summarize_by_category(self): #Noah
        '''
        Summarizes all transactions by categpory. category: ?, total: ?
        '''
        self.cursor.execute('SELECT category, SUM(amount) FROM transactions GROUP BY category')
        rows = self.cursor.fetchall()
        sum = [{'category': row[0], 'total': row[1]} for row in rows]
        return sum
    

  
