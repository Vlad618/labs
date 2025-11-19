import requests
import numpy as np
import pandas as pd
from PIL import Image
from faker import Faker
from bs4 import BeautifulSoup
import lxml
import seaborn as sns
from flask import Flask
import matplotlib.pyplot as plt

# 1. requests
try:
    response = requests.get("https://api.github.com")
    print("Requests status code:", response.status_code)
except Exception as e:
    print("Requests error:", e)
# 2. numpy
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("Numpy sum:", np.sum(arr))
except Exception as e:
    print("Numpy error:", e)
# 3. pandas
try:
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    print("Pandas DataFrame:\n", df.head())
except Exception as e:
    print("Pandas error:", e)
# 4. Faker
try:
    fake = Faker()
    print("Fake name:", fake.name())
except Exception as e:
    print("Faker error:", e)
# 5. lxml
try:
    from lxml import etree
    xml_data = "<root><item>Test 1</item><item>Test 2</item></root>"
    root = etree.fromstring(xml_data)
    items = [elem.text for elem in root.findall("item")]
    print("lxml parsed items:", items)
except Exception as e:
    print("lxml error:", e)