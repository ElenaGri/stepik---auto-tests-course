from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # рассчитать значение x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)


    # указать ответ
    answerField = browser.find_element_by_id("answer")
    answerField.send_keys(y)

    # Отметить checkbox "I'm the robot".
    notRobot = browser.find_element_by_id("robotCheckbox")
    notRobot.click()

    # Выбрать radiobutton "Robots rule!".
    robotRules = browser.find_element_by_id("robotsRule")
    robotRules.click()

    #нажать Submit
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()