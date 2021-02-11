from selenium import webdriver
#Javascript를 이용한 동적 웹페이지로 파악되어, selenium을 사용함.
import time
import requests
from bs4 import BeautifulSoup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
#chrome을 기반으로한 크롤링을 사용하였고, 크롤링 옵셥으로 굳이 브라우저를 열지 않고 명령을 실행할 수 있는 headless옵션을 넣어줌.
browser = webdriver.Chrome('./chromedriver', options=chrome_options)
browser.set_window_size(1920, 1080)

url = 'https://pubchem.ncbi.nlm.nih.gov/compound/3401#section=13C-NMR-Spectra&fullscreen=true'
browser.get(url)
browser.implicitly_wait(time_to_wait=5)
#로딩이 되면서 웹페이지 내용이 로드되는 동적 웹페이지로 판단되어, 5초의 딜레이를 주었음.
soup = BeautifulSoup(browser.page_source,'html.parser')
#딜레이 이후, 얻어진 웹페이지의 페이지 소스를 html형식으로 로드하여 soup라는 변수에 저장
try:
    img = soup.select('div>div>div>table>tbody>tr>td>div>div>a>img')[0]
    print(img.get('src'))
except IndexError:
    print('검색 결과가 없습니다.')
# pubchem에 nmr spectrum에 대한 정보가 탑재할 경우, 올바르게 url을 출력하나
# nmr spectrum이 없을 경우, img라는 변수에 indexerror가 발생함. 이 오류를 그대로 출력하지 않고
#try except문을 활용하여 예외처리시키고, 직접 문구를 출력하도록 설정