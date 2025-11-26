import requests                    # бібліотека для HTTP-запитів (наприклад отримати дані з веб-сайтів або API)
import numpy as np                 # бібліотека для роботи з масивами, матрицями та числовими обчисленнями
import pandas as pd                # бібліотека для обробки та аналізу табличних даних (DataFrame)
from PIL import Image              # робота із зображеннями
from faker import Faker            # генерація фейкових даних: імена, адреси, email тощо
from bs4 import BeautifulSoup      # парсинг HTML-сторінок
import lxml                        # обробка XML/HTML (швидкий парсер)
import seaborn as sns              # бібліотека для побудови статистичних графіків
from flask import Flask            # фреймворк для створення веб-сайтів/веб-сервісів у Python
import matplotlib.pyplot as plt    # побудова графіків, візуалізація даних

# 1. requests — робимо HTTP-запит на GitHub API
try:
    response = requests.get("https://api.github.com")
    print("Requests status code:", response.status_code)
except Exception as e:
    print("Requests error:", e)
# 2. numpy — демонстрація створення масиву і обчислення суми
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Numpy sum:", np.sum(arr))
except Exception as e:
    print("Numpy error:", e)
# 3. pandas — створення DataFrame і виведення перших рядків
try:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("Pandas DataFrame:\n", df.head())
except Exception as e:
    print("Pandas error:", e)
# 4. Faker — генерація випадкового імені
try:
    fake = Faker()
    print("Fake name:", fake.name())
except Exception as e:
    print("Faker error:", e)
# 5. lxml — парсинг XML-структури
try:
    from lxml import etree
    xml_data = "<root><item>Test 1</item><item>Test 2</item></root>"
    root = etree.fromstring(xml_data)
    items = [elem.text for elem in root.findall("item")]
    print("lxml parsed items:", items)
except Exception as e:
    print("lxml error:", e)