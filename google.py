from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import *
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.carefor.co.kr/login.php")
time.sleep(2)

###################################################
dress = randint(3,4) # 몸단장 3~4
helping_move = randint(6,10) # 이동도움 6~10
helping_act = randint(8,10) #신체기능 유지 및 증진 8~10
###################################################

######################################################################################################
#미완성 > 추후 for문을 통해 재구현
def insertNumReverse():

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~일요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~토요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~금요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~목요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~수요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(randint(3,4)) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~화요일
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(randint(3,4))
    time.sleep(0.2) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(randint(6,10))
    time.sleep(0.2) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~월요일
def insertNum():
    #케어포 숫자 넣기 > 저장 > 지난주로 이동
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[1]/div/div[2]/input[1]').send_keys(randint(3,4))
    time.sleep(0.2) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[1]/div/div[2]/input[1]').send_keys(randint(6,10))
    time.sleep(0.2) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[1]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~월요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[2]/div/div[2]/input[1]').send_keys(randint(3,4)) 

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[2]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[2]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~화요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[3]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[3]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[3]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~수요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[4]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[4]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[4]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~목요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[5]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[5]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[5]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~금요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[6]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[6]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[6]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~토요일

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #몸단장
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[7]/td[7]/div/div[2]/input[1]').send_keys(randint(3,4))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #이동도움
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[13]/td[7]/div/div[2]/input[1]').send_keys(randint(6,10))

    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.DELETE) #신체건강
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/table/tbody/tr[14]/td[7]/div/div[2]/input[1]').send_keys(randint(8,10))
    time.sleep(0.2) 
    ############################## ~일요일
    #케어포 숫자 넣기 끝#############################
def act():
    try:
        insertNum()
        driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/div[2]/span[2]').click() #저장
        time.sleep(1.5)
    except Exception as error:
        try:
            insertNumReverse()
            driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/div[2]/span[2]').click() #저장
            time.sleep(1.5)
        except Exception as error:
            driver.find_element_by_xpath('//*[@id="serviceMasterForm"]/div[2]/span[2]').click() #저장
            time.sleep(1.5)
######################################################################################################


##
##
##

##코드 시작##

#홈페이지 로그인 시도
driver.find_elements_by_name("ctmnumb")[0].send_keys("요양기관번호")
driver.find_elements_by_name("stmiden")[0].send_keys("아이디")
driver.find_elements_by_name("stmpass")[0].send_keys("패스워드")
driver.find_element_by_css_selector("input[src='/img_work/bt_login.gif']").click()
time.sleep(3)
#로그인 성공


#요양급여제공 접속
driver.find_element_by_xpath('//*[@id="left_area"]/div[4]/ul/li[2]').click()
driver.find_element_by_xpath('//*[@id="left_sub2"]/div[2]/table/tbody/tr[2]/td/div/ul/li[1]').click()
time.sleep(3)
#접속 성공


#날짜 3주전으로 이동
driver.find_element_by_xpath('//*[@id="r_padding"]/div[1]/div[4]/div[1]/div/div[1]/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="r_padding"]/div[1]/div[4]/div[1]/div/div[1]/span[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="r_padding"]/div[1]/div[4]/div[1]/div/div[1]/span[1]').click()
time.sleep(3)
#01.18~

#######################################################################3

def run():
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[1]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[2]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[3]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[4]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[5]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[6]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[7]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[8]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[9]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[10]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[11]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[12]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[13]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[14]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[15]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[16]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[17]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[18]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[19]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[20]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[21]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[22]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[23]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[24]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[25]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[26]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[27]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[28]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[29]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[30]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[31]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[32]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[33]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[34]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[35]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[36]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[37]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[38]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[39]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[40]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[41]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[42]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[43]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[44]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[45]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[46]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[47]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[48]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[49]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[50]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[51]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[52]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[53]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[54]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[55]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[56]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[57]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[58]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[59]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[60]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[61]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[62]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[63]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[64]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[65]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
    driver.find_element_by_xpath('//*[@id="care_service_list_table"]/tbody/tr[66]').click()
    time.sleep(1.5)
    act()
    time.sleep(1.5)
#1~66명 어르신 작성 후 저장
    
for i in range(1,50): #1~66명 어르신 작성 > 날짜 전으로 이동 > 작성 반복
    try:
       run()
    except Exception as error:
        #날짜 전으로 이동
        driver.find_element_by_xpath('//*[@id="r_padding"]/div[1]/div[4]/div[1]/div/div[1]/span[1]').click()
        time.sleep(1.5)
        