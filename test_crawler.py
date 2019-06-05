# coding: utf-8
from selenium import webdriver
import time
import unicodecsv

"""
note: 需要使用selenium，chrome版本需要与chromedriver版本对应。具体见https://chromedriver.storage.googleapis.com/
"""

def login(username, password):
    #打开微信公众号登录页面
    driver.get('https://mp.weixin.qq.com/')
    driver.maximize_window()
    time.sleep(3)
    # 自动填充帐号密码
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[1]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[1]/div/span/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[2]/div/span/input").clear()
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[1]/div[2]/div/span/input").send_keys(password)

    time.sleep(1)
    #自动点击登录按钮进行登录
    driver.find_element_by_xpath("//*[@id=\"header\"]/div[2]/div/div/form/div[4]/a").click()
    # 拿手机扫二维码
    time.sleep(15)

def open_link(nickname):
    # 进入新建图文素材
    driver.find_element_by_xpath('//*[@id="menuBar"]/li[5]/ul/li[3]/a/span/span').click()
    driver.find_element_by_xpath('//*[@id="js_main"]/div[3]/div[1]/div[2]/div[2]/div/button[1]').click()
    time.sleep(10)

    # 切换到新窗口
    for handle in driver.window_handles:
        if handle != driver.current_window_handle:
            driver.switch_to_window(handle)

    # 点击超链接
    driver.find_element_by_xpath('//*[@id="edui24_body"]/div').click()
    time.sleep(3)
    # 点击查找文章
    driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[1]/div/label[2]/span').click()
    # 输入公众号名称
    driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[3]/div[1]/div/span[1]/input').clear()
    driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[3]/div[1]/div/span[1]/input').send_keys(nickname)
    # 点击搜索
    driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[3]/div[1]/div/span[1]/a[2]').click()
    time.sleep(3)
    # 点击第一个公众号
    driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[3]/div[2]/div/div[1]/div/div[1]/div[3]/p[2]').click()
    time.sleep(3)

def get_url_title(html):
    lst = []
    for item in driver.find_elements_by_class_name('my_link_item'):
        temp_dict = {
            'date': item.text.split('\n')[0],
            'url': item.find_element_by_tag_name('a').get_attribute('href'),
            'title': item.text.split('\n')[1],
        }
        lst.append(temp_dict)
    return lst



#用webdriver启动谷歌浏览器，记得修改路径哈
driver = webdriver.Chrome(executable_path='/Users/lara/Downloads/chromedriver')

#这个需要通过老师扫码，会有点麻烦，可以用自己或朋友的微信公众号试试看
# nickname = '中国传媒大学'# 公众号名称，想查谁都行
# username =  'cuc-1954'# 账号
# password = 'cucby65783912' # 密码

login(username, password)
open_link(nickname)
page_num = int(driver.find_elements_by_class_name('page_num')[-1].text.split('/')[-1].lstrip())

# 点击下一页
url_title_lst = get_url_title(driver.page_source)

for _ in range(1, page_num):
    try:
        pagination = driver.find_elements_by_class_name('pagination')[1]
        pagination.find_elements_by_tag_name('a')[2].click()
        time.sleep(6)#如果这里数值太小很可能会导致操作频繁不能抓取
        url_title_lst += get_url_title(driver.page_source)
    except:
        print("第{}页失败".format(_))
        break

#print(url_title_lst)
#将结果写入csv文件
with open('test_articles.csv',"wb+") as f:
    writer = unicodecsv.writer(f)
    writer.writerow(['date','url','title'])
    for item in url_title_lst:
        writer.writerow([item['date'],item['url'],item['title']])
f.close()

