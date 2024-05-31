
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time as t
from datetime import datetime
import codecs

# 뷰티풀수프 임포트
from bs4 import BeautifulSoup

d = datetime.today()

file_path = f'C:/MyWorkspace/upload/알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.txt'

# 셀레늄 사용 중 브라우저 꺼짐 현상 방지 옵션
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)

# 크롬 드라이버를 별도로 설치하지 않고 버전에 맞는 드라이버를 사용하게 해 주는 코드
service = webdriver.ChromeService(ChromeDriverManager().install())

# 크롬 드라이버를 활용하여 웹 브라우저를 제어할 수 있는 객체를 리턴
driver = webdriver.Chrome(options=option, service=service)

driver.get('https://www.aladin.co.kr')

# 베스트셀러 탭 클릭
driver.find_element(By.XPATH, '//*[@id="Wa_header1_headerTop"]/div[2]/div[3]/ul[1]/li[3]/a').click()

t.sleep(2)


with codecs.open(file_path, mode='w', encoding='utf-8') as f:

    cur_page_num = 2 # 현재 페이지 번호
    target_page_num = 9 # 목적지 페이지 번호
    rank = 1 # 순위

    while cur_page_num <= target_page_num:
        # selenium으로 현재 페이지의 html 소스 코드를 전부 불러오기
        src = driver.page_source

        soup = BeautifulSoup(src, 'html.parser')

        div_list = soup.find_all('div', class_='ss_book_box')

        for div in div_list:
            book_info = div.find_all('li')

            if book_info[0].find('span', class_='ss_ht1') == None:
                # 첫번째 li에 span class="ss_ht1"이 없다면 (사은품 없는 책)
                book_title = book_info[0].text
                book_author = book_info[1].text
                book_price = book_info[2].text
            else:
                # 사은품이 있는 책(span class="ss_ht1"이 존재함)
                book_title = book_info[1].text
                book_author = book_info[2].text
                book_price = book_info[3].text

            auth_info = book_author.split(' | ')

            f.write(f'# 순위: {rank}위\n')
            f.write(f'# 제목: {book_title}\n')
            f.write(f'# 저자: {auth_info[0]}\n')
            f.write(f'# 출판사: {auth_info[1]}\n')
            f.write(f'# 출판년월: {auth_info[2]}\n')
            f.write(f'# 가격: {book_price.split(", ")[0]}\n')
            f.write('-' * 40 + '\n')

            rank += 1

        # 다음 페이지(탭)로 전환
        cur_page_num += 1
        driver.find_element(By.XPATH, f'//*[@id="newbg_body"]/div[3]/ul/li[{cur_page_num}]/a').click()
        del soup
        t.sleep(3)

