import sqlite3


#  Connect to the SQLite database
connection = sqlite3.connect('student.db')


# Create a cursor object using the connection to insert data, create tables, etc.
cursor = connection.cursor()


table_info='''
        CREATE TABLE IF NOT EXISTS students 
            (name VARCHAR(25) NOT NULL,
            age VARCHAR(3) NOT NULL,
            sec VARCHAR(10) NOT NULL,
            marks INTEGER NOT NULL);
        
    '''
cursor.execute(table_info)
# Insert data into the table

cursor.execute('''INSERT INTO students values('adarsh', 24, 'Data science',90)''')
cursor.execute('''INSERT INTO students values('darshn', 25, 'Data Engineer',95)''')
cursor.execute('''INSERT INTO students values('mithun', 29, 'Artist',100)''')
cursor.execute('''INSERT INTO students values('Kumar', 19, 'Dancer',70)''')
cursor.execute('''INSERT INTO students values('Yogi', 29, 'Business',80)''')



print("Table created successfully")
data = cursor.execute('SELECT * FROM students')
for row in data:
    print(row)
connection.commit()
connection.close()