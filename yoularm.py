from selenium import webdriver
from time import sleep

delay =  int(1.5 * 3600)# + 20 * 60

for i in range(delay):
    sleep(1)
    print delay - i,


# Delay about 20 minuntes plus 3 hours, the time it takes to fall asleep plus two sleep cycles
browser = webdriver.Firefox()
browser.get('https://www.youtube.com/watch?v=6Ejga4kJUts')
sleep(1000)
browser.quit()
