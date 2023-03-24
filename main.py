import datetime
import sys
import threading
import time

from PyQt6 import QtWidgets

from dns import parser_dns
from file_pars import file
from video_folder import video_scanner, img_scanner
from valyt import pogoda, valyt
from txt import file_1


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self, window_title: str):
        super().__init__()

        global headers
        self.headers = headers

        self.layout = QtWidgets.QGridLayout(self)

        self.label_url = QtWidgets.QLabel("url")
        self.layout.addWidget(self.label_url, 0, 0)

        self.line_edit_url = QtWidgets.QLineEdit("https://jsonplaceholder.typicode.com/todos/")
        self.layout.addWidget(self.line_edit_url, 1, 0)

        self.label_status = QtWidgets.QLabel("...")
        self.layout.addWidget(self.label_status, 0, 1)

        self.button_start = QtWidgets.QPushButton("start download")
        self.button_start.clicked.connect(self.start)
        self.layout.addWidget(self.button_start, 1, 3)

        self.setWindowTitle(window_title)
        self.resize(640, 480)
        self.show()

    def start(self):
        self.label_status.setText("идёт загрузка")
        new_thread = threading.Thread(target=self.start_data_analyse)

        new_thread.start()

    def finish(self, message="загрузка завершена"):
        self.label_status.setText(f"{message} [{datetime.datetime.now().strftime('%H:%M:%S')}]")

    def start_json_download(self):
        try:
            url = str(self.line_edit_url.text())
            file.start(url="https://jsonplaceholder.typicode.com/posts/1", headers=self.headers)
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_weather_monitoring(self):
        try:
            while True:
                time.sleep(2.0)
                pogoda.get_weather_data(url="https://www.gismeteo.kz/weather-astana-5164/", headers=self.headers)
                self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_currency_monitoring(self):
        try:
            while True:
                time.sleep(2.0)
                parser_dns.start(url="https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/", headers=self.headers)
                self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_image_scanner(self):
        try:
            img_scanner.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_video_scanner(self):
        try:
            video_scanner.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")

    def start_data_analyse(self):
        try:
            file_1.start()
            self.finish()
        except Exception as error:
            self.finish(f"ошибка: {error}")


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow("пример приложений python")
    sys.exit(pyqt_app.exec())
