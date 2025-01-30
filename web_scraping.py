import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

# Настраиваем Selenium
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Запуск без открытия окна браузера
driver = webdriver.Chrome(options=options)

# Открываем страницу
url = "https://yandex.ru/pogoda/moscow"
driver.get(url)

# Ждем несколько секунд, чтобы контент загрузился
time.sleep(5)

# Заголовки (чтобы сайт не блокировал запрос)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Отправляем GET-запрос
response = requests.get(url, headers=HEADERS)


# Получаем HTML страницы
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Извлекаем температуру
#temperature = soup.select_one(".temp__value").text
#condition = soup.select_one(".link__condition").text

weather = soup.select("tbody.lister-list tr")

weather_data = []

state = soup.select_one(".link__condition").text.strip("()")
humidity = soup.select_one(".term__value").text.strip()
temp = soup.select_one(".temp__value").text.strip()

weather_data.append([state, humidity, temp])

# Закрываем браузер
driver.quit()

# Сохраняем в CSV
with open("weather.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Погода", "Влажность", "Температура"])  # Заголовки
    writer.writerows(weather_data)  # Данные

print("Данные успешно сохранены в weather.csv!")
