import mysql.connector

def kgns_data():
    kgns = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'root',
            port = 3306,
            database = 'kgns'
        )
    cursor = kgns.cursor()
    cursor.execute('select * from vendors')
    vendors = cursor.fetchall()
    cursor.close()
    kgns.close()

    return vendors
