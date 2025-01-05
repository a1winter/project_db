from faker import Faker
import random
from db_connector import DatabaseConnector



fake = Faker("ru_RU")

db = DatabaseConnector(
    host='localhost',
    user='root',
    password='12345678',
    database='Yoga_Manager_DB'
)

db.connect()

def generate_data(n=200):
    yoga_styles = ['Хатха-йога', 'Аштанга-йога', 'Кундалини-йога', 'Йога Айенгара', 'Йога для начинающих']
    training_types = ['Групповые занятия', 'Индивидуальные занятия']
    contact_channels = ['WhatsApp', 'Telegram', 'ВКонтакте', 'Instagram']

    for _ in range(n):
        full_name = fake.name()
        contact_number = fake.phone_number()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime('%Y-%m-%d')
        health_info = random.choice(
            ['Нет противопоказаний', "Хроническая усталость", "Травма колена", "Недавняя операция", None]
        )
        city = fake.city_name()
        yoga_style = random.choice(yoga_styles)
        training_type = random.choice(training_types)
        days_time = random.choice(
            [
                'Пн-Пт: 9:00-12:00, 14:00-17:00',
                'Сб-Вс: 9:00-12:00, 14:00-17:00',
                'Пн-Сб: 10:00-13:00, 15:00-18:00',
                'Пн-Вс: 11:00-14:00, 16:00-19:00',
                'В любое время',
                'По договоренности',
            ]
        )
        contact_channel = random.choice(contact_channels)

        params = (
            full_name,
            contact_number,
            birthday,
            health_info,
            city,
            yoga_style,
            training_type,
            days_time,
            contact_channel
        )

        insert_query = """
            INSERT INTO participants (
                full_name, contact_number, birthday, health_info, city, yoga_style,
                training_type, days_time, contact_channel 
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        db.execute_query(insert_query, params)

generate_data()
db.close()