from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# [1] 브라우저 옵션 설정
# 브라우저가 실행되자마자 닫히는 것을 방지 ("detach" 옵션)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# [불필요한 로그 제거 옵션 - 선택사항]
chrome_options.add_argument("--log-level=3")

# [2] 브라우저 실행 (Selenium Manager가 드라이버 자동 설치함)
print("브라우저를 실행합니다...")
driver = webdriver.Chrome(options=chrome_options)

# [3] 웹페이지 이동
url = "https://kream.co.kr/"
driver.get(url)
sleep(2)

driver.find_element(By.CSS_SELECTOR, "button.btn_search").click()

sleep(1)
input_tag = driver.find_element(By.CSS_SELECTOR, "input.input_search")
input_tag.send_keys("슈프림")
input_tag.send_keys(Keys.ENTER)

sleep(1)
for i in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)

html = driver.page_source
html = BeautifulSoup(html, "lxml")
wrapper = html.find("div", {"class" : "layout-grid-horizontal-equal"})
items = wrapper.find_all("a", {"class": "product_card"})
product_links = []
for item in items:
    product_link = "https://kream.co.kr/" + item.get("href").strip()
    product_links.append(product_link)
    product_detail_div = item.find("div",{"class" : "layout_list_vertical"})
    product_strings = [p.get_text(strip=True) for p in product_detail_div.find_all("p")]

    if len(product_strings) < 6 :
        continue

    brand, name, price,likes, review, trade = product_strings

    if "후드" in product_strings[1]:
        print("===========================================")
        print(product_link)
        print(
            brand,
            name,
            price,
            likes,
            review,
            trade
        )

driver.quit()

# counter = 0

# while counter <= 10:
#     driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.PAGE_DOWN)
#     sleep(1.5)
#     counter += 1

def fetch_product_page(url : str) :
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "priority": "u=0, i",
        "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    }
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return res.content[100:200]
    except Exception as e:
        print(f"에러 발생 >> {e}")

results = []

# product_links
with ThreadPoolExecutor(max_workers=4) as ex:
    futures = [ex.submit(fetch_product_page, link) for link in product_links]
    for fut in as_completed(futures):
        try:
            results.append()
        except Exception as e:
            print(f"동시 실행에 에러 발생 >>{e}")

print(results)