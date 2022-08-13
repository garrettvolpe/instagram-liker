from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome(executable_path="/home/dev/Projects/chromedriver")

username = 'username'
password =  "password"
##########################
# Logging in
#########################
def login():
   browser.set_window_size(654, 687)
   browser.get("https://www.instagram.com/accounts/login/")
   time.sleep(1)
   #user and pass entered here
   browser.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input").send_keys(username)
   browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input').send_keys(password)
   browser.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div').click()
   time.sleep(3)
   not_now_button = '#react-root > section > main > div > div > div > div > button'
   browser.find_element(By.CSS_SELECTOR, not_now_button).click()
login()
time.sleep(2)
#############################
# Liker
#########################
hashtag_list = ['likeforlike', 'likeforlikes', 'likeforlikealways', 'likeforlikeback', 'likeforliketeam', 'likeforlikesback', 'likeforlikeandfollow', 'likeforlikers', 'likeforlikesfromme', 'likeforlikebackandfollow', 'likeforlikeforfollow', 'likeforlikebackandfoll', 'likeforlikesalways', 'likeforlikesbackandfollow', 'likeforlikebackandpfollow', 'likeforlikefromme', 'likeforlikebackalways', 'likeforlikealwaysback', 'likeforlikee', 'likeforlikees', 'likeforliketag', 'likeforlikephoto', 'likeforliketeams', 'likeforlikealway', 'likeforlikeindonesia', 'likeforlikersback', 'likeforlikebac', 'likeforlikealeays', 'likeforlikealwaysi', 'follow']
heart_icon = "#mount_0_0_HU > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > main > div._aa6b._aa6d > div._aa6e > article > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm > div > div > section._aamu._aaz9 > span._aamw > button > div._abm0._abm1 > svg"
first_pic_on_page = """/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]"""
color_of_heart = """#mount_0_0_r9 > div > div > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aa-d > div > div > div._aaz4 > section._aamu._aaz9 > span._aamw > button > div._abm0._abl_ > span > svg"""
next_button_when_one_arrow = """/html/body/div[5]/div[1]/div/div/a"""
next_button_when_two_arrow ="""/html/body/div[5]/div[1]/div/div/a[2]"""
likes = 0

number_of_pics_to_like_per_hashtag = 5

for hashtag in hashtag_list:
   browser.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
   time.sleep(5)
   first_pic = browser.find_element_by_xpath(first_pic_on_page)
   first_pic.click()
   time.sleep(random.randint(2,4))
   try:
       heart_pic =  browser.find_element(By.CLASS_NAME, '_aamw')
       time.sleep(1)
       is_pic_hearted = browser.find_element(By.CLASS_NAME, '_ab6-').get_attribute('fill')
       if is_pic_hearted != '#ed4956':
           time.sleep(random.randint(2, 3))
           heart_pic.click()
           likes += 1
       time.sleep(random.randint(2, 6))
#        print("testing1")
#        next_button = browser.find_element(By.CLASS_NAME, "_abl-").click()
#        print("testing2")
   except:
        print("failed to like")
