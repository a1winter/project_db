import sys
from db_connector import DatabaseConnector
from gui import YogaDatabaseGUI
from PyQt6.QtWidgets import QApplication



def main():
    db = DatabaseConnector(
        host='localhost',
        user='root',
        password='12345678',
        database=''
    )

    db.connect()
    db.execute_query('CREATE DATABASE IF NOT EXISTS Yoga_Manager_DB;')
    db.close()

    db = DatabaseConnector(
        host='localhost',
        user='root',
        password='12345678',
        database='Yoga_Manager_DB'
    )

    db.connect()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS participants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            full_name VARCHAR(100),
            contact_number VARCHAR(30),
            birthday DATE,
            health_info TEXT,
            city VARCHAR(100),
            yoga_style VARCHAR(100),
            training_type VARCHAR(100),
            days_time TEXT,
            contact_channel VARCHAR(50)
        )"""

    db.execute_query(create_table_query)

    app = QApplication(sys.argv)
    window = YogaDatabaseGUI(db_connector=db)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
