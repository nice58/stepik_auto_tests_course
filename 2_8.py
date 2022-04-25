from selenium import webdriver
from selenium.webdriver.common.by import By
import os  # для добавления файла
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)


input1 = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
input1.send_keys("ИМЯ")

input2 = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
input2.send_keys("ФАМИЛИЯ")

input3 = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
input3.send_keys("email@email.ru")

button_file = browser.find_element(By.ID, "file")
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_name = "File1.txt"  # присваиваем имя файла
file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
button_file.send_keys(file_path)  # нажатие кнопки для добавления файла

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

time.sleep(30)
browser.quit()
