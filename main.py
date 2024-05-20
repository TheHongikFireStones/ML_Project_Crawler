from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request


# 자신의 크롬 브라우저와 일치하는 버전의 크롬 드라이버를 다운받고 프로젝트 폴더 내에 넣어야함.
driver = webdriver.Chrome() #크롬 웹드라이버를 열기
driver.get("https://www.google.co.kr/imghp?hl=en&tab=ri&ogbl") #구글이미지검색 창으로
elem = driver.find_element(By.NAME, "q") #검색창을 찾기
elem.send_keys("Varun Dhawan face") #우리의 키워드 입력하기
elem.send_keys(Keys.RETURN) #enter키

# [스크롤 내리기]
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") #자바스크립트 코드 실행, 브라우저의 높이 알아내는 것

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR,'.mye4qd').click() #결과 더보기 버튼이 있으면 클릭하라
        except:
            break #결과 더보기 버튼이 없으면 스크롤하는 반복문 빠져나가
    last_height = new_height
print("-----")

# 검색했을 때 나오는 작은 이미지들이 가지는 공통된 클래스를 입력
images = driver.find_elements(By.CSS_SELECTOR,'.YQ4gaf') #검색했을 때 나오는 작은 썸네일의 사진들 class 지정
print(images)
for image in images:
    className = image.get_dom_attribute("class")
    if len(className) > 6:
        images.remove(image)


count = 1 #이미지의 개수
for image in images:
    try:
        if count == 300:
            exit()
#         # image.click() #이미지들 중 하나를 클릭
#         # time.sleep(1.3) #큰 이미지가 나오는데 로딩될 때까지 기다려줌 (3초) (로딩되는데 시간 걸리므로)
#         # 작은 이미지를 클릭했을 때 나오는 큰 이미지들의 xpath
#         # imgUrl = driver.find_element(By.XPATH ,'/html/body/div[4]/div/div[13]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[4]/div[2]/h3/a/div/div/div/g-img/img').get_attribute("src") #큰 이미지의 src가져오기
        imgUrl = image.get_attribute('src')
        urllib.request.urlretrieve(imgUrl, 'C:\\Users\\MINUK\\Desktop\\CS 2023-2\\db\\pythonProject\\img' + '/Varun_Dhawan/' +str(count) + ".jpg") #이미지 다운로드 받기
        count = count + 1
    except Exception as e:
        print(e)
        pass

driver.close() #브라우저 창을 닫아주기