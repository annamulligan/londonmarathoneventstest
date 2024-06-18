import sqlite3
import os
import random

CUSTOMER_NAMES = ['riley', 'james', 'ryan', 'joshi', 'andrew']

class CustomerDatabase:
  def __init__(self, database_location=None):
    if database_location:
      self.database_location = database_location
    else:
      self.database_location = "./"
    self.__create_database()
    self.__add_customer_table()

  
  def __create_database(self):
    if os.path.exists(f'{self.database_location}/customers.db'):
      pass
    else:
      conn = None
      try:
        conn = sqlite3.connect(f'{self.database_location}/customers.db')
        print(sqlite3.sqlite_version)
      except sqlite3.Error as e:
        print(e)
      finally:
        if conn:
          conn.close()
  
  def __add_customer_table(self):
     
    conn = None
    try:
      conn = sqlite3.connect(f'{self.database_location}/customers.db')
    except sqlite3.Error as e:
      print(e)
    finally:
      if conn:
        sql_statement = """CREATE TABLE IF NOT EXISTS customers (
                ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                FirstName text NOT NULL, 
                LastName text NOT NULL, 
                InsertDateTime DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
        );"""
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()
        conn.close()
  
  def generate_1000_customers(self):

    len_names = len(CUSTOMER_NAMES)-1
    sql_statement = """
      INSERT INTO customers (FirstName, LastName)
      Values
    """
    names = []
    for i in range(1000):
      first_name = random.randint(0, len_names)
      last_name = random.randint(0, len_names)
      while first_name == last_name:
        last_name = random.randint(0, len_names)
      names.append(f"('{CUSTOMER_NAMES[first_name]}', '{CUSTOMER_NAMES[last_name]}')")

    sql_statement += ",".join(names)

    conn = None
    try:
      conn = sqlite3.connect(f'{self.database_location}/customers.db')
    except sqlite3.Error as e:
      print(e)
    finally:
      if conn:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()
        conn.close()

  def return_customer_list(self):
    sql_statement = """
      SELECT * From Customers
    """
    try:
      with sqlite3.connect(f'{self.database_location}/customers.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        
        return cursor.fetchall()
    except sqlite3.Error as e:
      print(e)

def truncate_table(self):
  sql_statement = "TRUNCATE TABLE CUSTOMERS"
  try:
      with sqlite3.connect(f'{self.database_location}/customers.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        conn.commit()
  except sqlite3.Error as e:
    print(e)


if __name__ == '__main__':
  new_db  = CustomerDatabase()
  #new_db.generate_1000_customers()
  print(new_db.return_customer_list())




      
    