# from bs4 import BeautifulSoup
# import requests
# from openpyxl import Workbook
# response = requests.get("https://workey.codeit.kr/music")
# music_page = response.text
# soup = BeautifulSoup(music_page,'html.parser')
#
#
# print(soup.select('ul.popular__order li'))
# popular_artists = []
# for tag in soup.select('ul.popular__order li'):
#     popular_artists.append(tag.get_text().strip())
#     popular_artists.append(list(tag.stripped_strings)[1])
#
# print(soup.select_one('img')['src'])
# print(soup.select_one('img').attrs)
#
# #데이터를 엑셀 파일로
# wb = Workbook(write_only=True)
# ws = wb.create_sheet('TV Rating')
# ws.append(['순위','채널','프로그램','시청률'])
# response = requests.get("https://workey.codeit.kr/ratings/index")
# rating_page = response.text
# soup = BeautifulSoup(rating_page, 'html.parser')
# for tag in soup.select('tr')[1:]:
#     td_tag = tag.select('td')
#     row = [
#         td_tag[0].get_text(), #순위
#         td_tag[1].get_text(), #채널
#         td_tag[2].get_text(), #프로그램
#         td_tag[3].get_text() #시청률
#     ]
#     ws.append(row)
# wb.save('시청률_2010년1월1주차.xlsx')
# wb.close()
#
# response1 = requests.get("https://workey.codeit.kr/orangebottle/index")
# # BeautifulSoup 사용해서 HTML 코드 정리
# soup = BeautifulSoup(response1.text, 'html.parser')
#
# branch_infos = []
# # 엑셀
# wb = Workbook(write_only=True)
# ws = wb.create_sheet()
# ws.append(['지점 이름', '주소', '전화번호'])
# # 모든 지점에 대한 태그 가져오기
# branch_tags = soup.select('div.branch')
#
# for branch_tag in branch_tags:
#     # 각 태그에서 지점 이름, 전화번호 가져오기
#     branch_name = branch_tag.select_one('p.city').get_text()
#     address = branch_tag.select_one('p.address').get_text()
#     phone_number = branch_tag.select_one('span.phoneNum').get_text()
#     ws.append([branch_name, address, phone_number])
# wb.save('오렌지_보틀.xlsx')
#
# wb = Workbook(write_only=True)
# for year in range(2010,2019):
#     ws = wb.create_sheet("{}년".format(year))
#     ws.append(['기간','순위','채널','프로그램','시청률'])
#     for month in range(1,13):
#         for weekIndex in range(0,5):
#             url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year,month,weekIndex)
#             response = requests.get(url)
#             rating_page = response.text
#             soup = BeautifulSoup(rating_page,'html.parser')
#             for tr_tag in soup.select('tr')[1:]:
#                 td_tag = tr_tag.select('td')
#                 period = "{}년 {}월 {}주차".format(year,month,weekIndex+1)
#                 row = [
#                     period,
#                     td_tag[0].get_text(),
#                     td_tag[1].get_text(),
#                     td_tag[2].get_text(),
#                     td_tag[3].get_text(),
#
#                 ]
#                 ws.append(row)
# wb.save('시청률.xlsx')
#
#
# #실습
# wb = Workbook(write_only=True)
# for year in range(2010,2019):
#     ws = wb.create_sheet()
#     ws.append(['기간', '순위', '프로그램', '시청률'])
#     for month in range(1,13):
#         for weekIndex in range(0,5):
#             url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(year, month, weekIndex)
#             response = requests.get(url)
#             soup = BeautifulSoup(response.text,'html.parser')
#             for tr_tag in soup.select('tr')[1:]:
#                 period = "{}년 {}월 {}주차".format(year,month,weekIndex+1)
#                 td_tag = tr_tag.select('td')
#                 if td_tag[1].get_text() == 'SBS':
#                     row = [
#                         period,
#                         td_tag[0].get_text(),
#                         td_tag[2].get_text(),
#                         td_tag[3].get_text(),
#                     ]
#                 else:
#                     continue
#                 ws.append(row)
# wb.save('SBS_데이터.xlsx')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# url = "https://workey.codeit.kr/costagram/index"
# driver = webdriver.Chrome()
# driver.implicitly_wait(3)
# driver.get(url)
# #driver.find_element_by_css_selector() #soup.select_one과 비슷 버전4부터 사라짐
# driver.find_element(By.CSS_SELECTOR,".top-nav__login-link").click()
# driver.find_element(By.CSS_SELECTOR,".login-container__login-input").send_keys('codeit')
# driver.find_element(By.CSS_SELECTOR,".login-container__password-input").send_keys('datascience')
# driver.find_element(By.CSS_SELECTOR,".login-container__login-button").click()
# time.sleep(3)
