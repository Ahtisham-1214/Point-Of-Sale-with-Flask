import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pos"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100),
    name VARCHAR(100),
    price DECIMAL(10,2),
    image_path VARCHAR(255)
)
""")

conn.commit()
conn.close()

print("Table 'stock' created successfully!")
