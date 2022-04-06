from turtle import backward, forward
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://localhost:3000/introduction/"
driver = webdriver.Firefox()
driver.get(url)
forwardLink = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/main/div/div/div[1]/div/nav/div/a")

while forwardLink:
    forwardLink[0].click()
    forwardLink = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/main/div/div/div[1]/div/nav/div/a")

if driver.current_url == "http://localhost:3000/interviewer-cheatsheet/":
    print("Forwards buttons working, continuing test")

    backwardLink = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/main/div/div/div[1]/div/article/div[2]/div/nav/div/a")

    while backwardLink:
        backwardLink[0].click()
        backwardLink = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/main/div/div/div[1]/div/article/div[2]/div/nav/div/a")

    if driver.current_url == "http://localhost:3000/introduction/":
        print("Backwards buttons working")
    else:
        print("Backwards buttons not working, broke on URL:")
        print(driver.current_url)
else:
    print("Forwards buttons not working, broke on URL:")
    print(driver.current_url)