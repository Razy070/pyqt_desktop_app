import requests
# подключаем бибилиотеку BeautifulSoup
from bs4 import BeautifulSoup
def start(url):
    d = []

# получаем страницы при помощи цикла
for j in range(50):
    # указываем url и get параметры запроса
    url = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
    # указываем get параметр с помощью которого определяется номер страницы
    par = {'p': j}
    # записываем ответ сервера в переменную r
    r = requests.get(url, params=par)
    # получаем объект  BeautifulSoup и записываем в переменную soup
    soup = BeautifulSoup(r.text, 'html.parser')
    # с помощью циклам перебераем товары на странице и получаем из них нужные параметры
    for i in range(20):
        # получаем название товара
        product = soup.find_all('h3')[i].get_text()
        # получаем цену товара
        price = soup.find_all(class_='price_g')[i].get_text()
        # удаляем пробел из цены
        price = price.replace(" ", "")
        # получаем ссылку на товар
        link = soup.find_all(class_='show-popover ec-price-item-link', attrs={'data-role': 'product-cart-link'})[i][
            'href']
        # добавляем домен к ссылке
        link = 'www.dns-shop.ru' + link
        # добавляем данные о товаре в список
        d.append([product, price, link])

# открываем файл на запись
with open('C:/Users/admin1/Desktop/dns.csv', 'w') as ouf:
    # перебираем элементы списка d
    for i in d:
        # преобразуем элемент списка в строку
        i = str(i)
        # очищаем строку от ненужных символов
        i = i.replace("\'", "")
        i = i.replace("[", "")
        i = i.replace("]", "")
        # записываем строку в файл
        ouf.write(i + '\n')
