import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='msearch',
        password='msearchpasswd',
        database='vidhyanagari'
    )
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")
finally:
    connection.close()
