from PyQt6.QtWidgets import (QWidget, QFormLayout, QLineEdit,
                             QComboBox, QDateEdit, QPlainTextEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton, QLabel)
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtGui import QFont, QPalette, QColor


class YogaDatabaseGUI(QWidget):
    def __init__(self, db_connector):
        super().__init__()
        self.db_connector = db_connector
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Анкета')
        self.setFixedSize(600, 700)

        font = QFont("Arial", 10)
        self.setFont(font)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor('#f0f0f0'))
        self.setPalette(palette)

        title = QLabel('Регистрация ученика йоги')
        title.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText('Введите полное имя')
        form_layout.addRow('ФИО:', self.name_edit)

        self.contact_edit = QLineEdit()
        self.contact_edit.setPlaceholderText('Например: +7 999 123-45-67')
        form_layout.addRow('Контактный номер:', self.contact_edit)

        self.birthday_edit = QDateEdit()
        self.birthday_edit.setCalendarPopup(True)
        self.birthday_edit.setDate(QDate.currentDate().addYears(-20))  # По умолчанию 20 лет назад
        form_layout.addRow('Дата рождения:', self.birthday_edit)

        self.health_edit = QPlainTextEdit()
        self.health_edit.setPlaceholderText('Укажите травмы, операции, заболевания (если есть)')
        self.health_edit.setFixedHeight(60)
        form_layout.addRow('Противопоказания:', self.health_edit)

        self.city_edit = QLineEdit()
        self.city_edit.setPlaceholderText('Введите ваш город')
        form_layout.addRow('Город:', self.city_edit)

        self.yoga_style_combo = QComboBox()
        self.yoga_style_combo.addItems(
            ['Хатха-йога', 'Аштанга-йога', 'Кундалини-йога', 'Йога Айенгара', 'Йога для начинающих'])
        form_layout.addRow('Направление в йоге:', self.yoga_style_combo)

        self.training_type_combo = QComboBox()
        self.training_type_combo.addItems(['Групповые занятия', 'Индивидуальные занятия'])
        form_layout.addRow('Тип занятий:', self.training_type_combo)

        self.days_edit = QPlainTextEdit()
        self.days_edit.setPlaceholderText('Например: Пн, Ср, Пт после 18:00')
        self.days_edit.setFixedHeight(50)
        form_layout.addRow('Удобные дни/время:', self.days_edit)

        self.contact_channel_combo = QComboBox()
        self.contact_channel_combo.addItems(['WhatsApp', 'Telegram', 'ВКонтакте', 'Instagram'])
        form_layout.addRow('Предпочитаемый канал связи:', self.contact_channel_combo)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton('Сохранить')
        cancel_btn = QPushButton('Отмена')

        save_btn.clicked.connect(self.handle_save)
        cancel_btn.clicked.connect(self.handle_cancel)

        btn_layout.addStretch(1)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(title)
        main_layout.addLayout(form_layout)
        main_layout.addStretch(1)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)

    def handle_cancel(self):
        self.close()

    def handle_save(self):
        full_name = self.name_edit.text()
        contact_number = self.contact_edit.text()
        birthday = self.birthday_edit.date().toString('yyyy-MM-dd')
        health_info = self.health_edit.toPlainText()
        city = self.city_edit.text()
        yoga_style = self.yoga_style_combo.currentText()
        training_type = self.training_type_combo.currentText()
        days_time = self.days_edit.toPlainText()
        contact_channel = self.contact_channel_combo.currentText()


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

        self.db_connector.execute_query(insert_query, params)

    def clear_fields(self):
        self.name_edit.clear()
        self.health_edit.clear()
        self.days_edit.clear()
        self.city_edit.clear()
        self.contact_edit.clear()
        self.birthday_edit.setDate(QDate.currentDate().addYears(-20))


        self.yoga_style_combo.setCurrentIndex(0)
        self.training_type_combo.setCurrentIndex(0)
        self.contact_channel_combo.setCurrentIndex(0)
