import requests
import json
import time
import trace
import random
import os
from bibibi.img_locate import ImgProcess
from bibibi.decrypt import Encrypyed
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# 轨迹处理来自FanhuaandLuomu/geetest_break
def cal_userresponse(a, b):
    d = []
    c = b[32:]
    for e in range(len(c)):
        f = ord(str(c[e]))
        tmp = f - 87 if f > 57 else f - 48
        d.append(tmp)

    c = 36 * d[0] + d[1]
    g = int(round(a)) + c
    b = b[:32]

    i = [[], [], [], [], []]
    j = {}
    k = 0
    e = 0
    for e in range(len(b)):
        h = b[e]
        if h in j:
            pass
        else:
            j[h] = 1
            i[k].append(h)
            k += 1
            k = 0 if (k == 5) else k

    n = g
    o = 4
    p = ""
    q = [1, 2, 5, 10, 50]
    while n > 0:
        if n - q[o] >= 0:
            m = int(random.random() * len(i[o]))
            p += str(i[o][m])
            n -= q[o]
        else:
            del (i[o])
            del (q[o])
            o -= 1
    return p


# 由challenge+track ==> 解析得到  userresponse 和 a
def get_userresponse_a(initData, track_list):
    # 路径需要自己拟合
    challenge = initData['challenge']
    l = track_list[-1][0]

    a = fun_f(track_list)
    arr = [12, 58, 98, 36, 43, 95 ,62, 15, 12]
    s = initData['s']
    a = fun_u(a, arr, s)
    userresponse = cal_userresponse(l, challenge)
    return userresponse, a

def fun_u(a, v1z, T1z):
    while not v1z or not T1z:
        pass
    else:
        x1z = 0
        c1z = a
        y1z = v1z[0]
        k1z = v1z[2]
        L1z = v1z[4]

        i1z = T1z[x1z:x1z+2]
        while i1z:
            x1z += 2
            n1z = int(i1z, 16)
            M1z = chr(n1z)
            I1z = (y1z * n1z * n1z + k1z * n1z + L1z) % len(a)
            c1z = c1z[0:I1z] + M1z + c1z[I1z:]  # 插入一个值
            i1z = T1z[x1z:x1z + 2]
        return c1z

# 计算每次间隔   相当于c函数
def fun_c(a):
    g = []
    e = []
    f = 0
    for h in range(len(a) - 1):
        b = int(round(a[h + 1][0] - a[h][0]))
        c = int(round(a[h + 1][1] - a[h][1]))
        d = int(round(a[h + 1][2] - a[h][2]))
        g.append([b, c, d])

        if b == c == d == 0:
            pass
        else:
            if b == c == 0:
                f += d
            else:
                e.append([b, c, d + f])
                f = 0
    if f != 0:
        e.append([b, c, f])
    return e


def fun_e(item):  # 相当于e函数
    b = [[1, 0], [2, 0], [1, -1], [1, 1], [0, 1], [0, -1], [3, 0], [2, -1], [2, 1]]
    c = 'stuvwxyz~'
    for i, t in enumerate(b):
        if t == item[:2]:
            return c[i]
    return 0


def fun_d(a):
    b = '()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr'
    c = len(b)
    d = ''
    e = abs(a)
    f = int(e / c)
    if f >= c:
        f = c - 1
    if f > 0:
        d = b[f]
    e %= c
    g = ''
    if a < 0:
        g += '!'
    if d:
        g += '$'
    return g + d + b[e]


def fun_f(track_list):
    skip_list = fun_c(track_list)
    # success_list = [
    #     [23, 21, 0],[1, -1, 196],[4, 0, 17],[6, -1, 17],[3, 0, 33],[3, 0, 15],[1, 0, 51],[1, 0, 18],[3, 0, 16],[2, 0, 33],[2, 0, 16],[0, -1, 16],[1, 0, 17],[3, 0, 17],[1, 0, 16],[2, 0, 17],[7, 0, 16],[1, 0, 17],[7, 0, 17],[4, 0, 16],[2, 0, 17],[3, 0, 16],[1, -2, 16],[2, 0, 18],[1, 0, 23],[1, 0, 48],[1, 0, 10],[2, 0, 51],[1, 0, 16],[1, 0, 33],[1, 0, 26],[1, 0, 24],[1, 0, 16],[2, 0, 18],[2, 0, 30],[1, 0, 20],[1, 0, 16],[1, 0, 16],[1, 0, 17],[1, 0, 259],[1, 0, 72],[1, 0, 17],[1, 0, 17],[2, 0, 16],[1, 0, 17],[1, -1, 16],[2, 0, 37],[2, 0, 120],[1, 0, 64],[1, 0, 24],[1, 0, 8],[1, 0, 16],[1, 0, 80],[0, 0, 560]
    #
    # ]
    # for i in range(1, len(skip_list)):
    #     if skip_list[i] != success_list[i]:
    #         print('Flase' , skip_list[i], success_list[i], i)
    #     break
    # print(len(skip_list), skip_list)
    g, h, i = [], [], []
    for j in range(len(skip_list)):
        b = fun_e(skip_list[j])
        if b:
            h.append(b)
        else:
            g.append(fun_d(skip_list[j][0]))
            h.append(fun_d(skip_list[j][1]))
        i.append(fun_d(skip_list[j][2]))
    # g_cuccess_list =  ["D", "-", "/", "0", "0", "-", ")", "("]
    # for _ in range(0, len(g)):
    #     if g[_] != g_cuccess_list[_]:
    #         print('g, Flase' , g[_], g_cuccess_list[_], _)
    #         break
    # h_success_list = [
    #     "B", "u", "(", "!)", "y", "y", "s", "s", "y", "t", "t", "x", "s", "y", "s", "t", "(", "s", "(", "(", "t", "y",
    #      "!*", "t", "s", "s", "s", "t", "s", "s", "s", "s", "s", "t", "t", "s", "s", "s", "s", "s", "s", "s", "s", "t",
    #      "s", "u", "t", "t", "s", "s", "s", "s", "s", "("
    # ]
    # for _ in range(0, len(g)):
    #     if h[_] != h_success_list[_]:
    #         print('h, Flase' , h[_], h_success_list[_], _)
    #         break
    # i_success_list = [
    #     "(", "$,)", ":", ":", "N", "8", "e", "?", "9", "N", "9", "9", ":", ":", "9", ":", "9", ":", ":", "9", ":", "9",
    #      "9", "?", "D", "b", "3", "e", "9", "N", "G", "E", "9", "?", "K", "A", "9", "9", ":", "$,r", "$)0", ":", ":",
    #      "9", ":", "9", "R", "$)i", "r", "E", "1", "9", "$)8", "$1U"
    # ]
    # for _ in range(0, len(g)):
    #     if i[_] != i_success_list[_]:
    #         print('i, Flase' , i[_], i_success_list[_], _)
    #         break
    return ''.join(g) + '!!' + ''.join(h) + '!!' + ''.join(i)


def crack(gt, challenge, referer):
    headers = {
        "Referer": referer,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Content-Type":"application/json; charset=UTF-8",
        "Cookie":"aliyungf_tc=AQAAAC5hGzTlNwIASFfU3uAVPAP1efmA; ssuid=5689407811; _ga=GA1.2.560332842.1567482068; csrfToken=75IdN5-VrGBNY2cyvM1_Nax2; TYCID=a9743a10cdfc11e98a202b8661be8d5a; undefined=a9743a10cdfc11e98a202b8661be8d5a; jsid=SEM-BAIDU-PZ1907-SY-000100; token=41c7ea2717c7471ab5e2c9b18159b7af; _utm=d0dd9b7de3ea468a8f1ee7b53b63c1a0; _gid=GA1.2.1197026298.1567650904; RTYCID=94950c135ae0443088a2ebb91f2bbc56; CT_TYCID=e6673be627ab4f0095688d1b1689e545; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1567482068,1567561423,1567651961; bannerFlag=true; refresh_page=0; cloud_token=e6c2770fd7904ba587223c8f20381eb6; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1567667671; _gat_gtag_UA_123487620_1=1",
        "Host":"www.tianyancha.com",
        "Origin":"https://www.tianyancha.com"
    }

    # 获取初始化数据
    uri = "gt=" + gt + \
          "&challenge=" + challenge + \
          "&width=100%&product=float&offline=false&protocol=https://&voice=/static/js/voice.1.1.3.js" \
          "&type=slide&pencil=/static/js/pencil.1.0.1.js&path=/static/js/geetest.6.0.9.js&callback=geetest"
    print(uri)
    response = requests.get(
        "https://api.geetest.com/get.php?" + uri,
        headers=headers,
    )
    print("response:"+str(response))
    print("response_text:"+response.text)
    print("response_text_replace:"+response.text.replace("geetest(", ""))
    initData = json.loads(response.text.replace("geetest(", "")[:-1])
    print('initData', initData)
    # 下载图片
    fullbg = str(time.time()) + str(random.random())
    bg = str(time.time()) + str(random.random())
    open("Image/" + fullbg + ".jpg", "wb").write(
        requests.get("https://static.geetest.com/" + initData["fullbg"]).content)
    open("Image/" + bg + ".jpg", "wb").write(requests.get("https://static.geetest.com/" + initData["bg"]).content)

    # 图片处理
    # 代码改自 OSinoooO/bilibili_geetest
    img_process = ImgProcess()
    img1 = img_process.get_merge_image('Image/' + fullbg + '.jpg')
    img2 = img_process.get_merge_image('Image/' + bg + '.jpg')
    os.remove("Image/" + fullbg + ".jpg")
    os.remove("Image/" + bg + ".jpg")
    distance = int(img_process.get_gap(img1, img2) - 7)

    track = trace.choice_track(distance)
    userresponse, aa = get_userresponse_a(initData, track)
    passtime = track[-1][-1]
    time.sleep(1)
    ep = Encrypyed()
    params = ep.encrypted_request(initData, userresponse, passtime, aa)
    response = requests.get(
        "https://api.geetest.com/ajax.php",
        headers=headers,
        params=params
    )
    try:
        return response.json()
    except:
        if 'geetest' in response.text:
            print(response.text)
            text = re.sub("geetest_\d*\(", "", response.text)
            return json.loads(text[:-1])
        else:
            return json.loads(response.text[1:-1])

browser = webdriver.Chrome()
browser.maximize_window()#将浏览器最大化
wait = WebDriverWait(browser, 10)

def login():
    try:
        userInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.pb30.position-rel > input')))
        passwordInput = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.pb40.position-rel > input')))
        userInput.send_keys('15881172050')#账号
        passwordInput.send_keys('Aa123456')#密码
        changeLoginWay = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#web-content > div > div > div > div.position-rel.container.company_container > div > div.in-block.vertical-top.float-right.right_content.mt50.mr5.mb5 > div.module.module1.module2.loginmodule.collapse.in > div.modulein.modulein1.mobile_box.pl30.pr30.f14.collapse.in > div.c-white.b-c9.pt8.f18.text-center.login_btn')))
        changeLoginWay.click()
    except TimeoutException:
        login()

login()
while True:
    referer= "https://www.tianyancha.com/"
    headers = {
        "Referer": referer,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Content-Type":"application/json; charset=UTF-8",
        "Cookie":"aliyungf_tc=AQAAAC5hGzTlNwIASFfU3uAVPAP1efmA; ssuid=5689407811; _ga=GA1.2.560332842.1567482068; csrfToken=75IdN5-VrGBNY2cyvM1_Nax2; TYCID=a9743a10cdfc11e98a202b8661be8d5a; undefined=a9743a10cdfc11e98a202b8661be8d5a; jsid=SEM-BAIDU-PZ1907-SY-000100; token=41c7ea2717c7471ab5e2c9b18159b7af; _utm=d0dd9b7de3ea468a8f1ee7b53b63c1a0; _gid=GA1.2.1197026298.1567650904; RTYCID=94950c135ae0443088a2ebb91f2bbc56; CT_TYCID=e6673be627ab4f0095688d1b1689e545; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1567482068,1567561423,1567651961; bannerFlag=true; refresh_page=0; cloud_token=e6c2770fd7904ba587223c8f20381eb6; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1567667671; _gat_gtag_UA_123487620_1=1",
        "Host":"www.tianyancha.com",
        "Origin":"https://www.tianyancha.com"
    }
    geeData = requests.post(
        #"https://passport.bilibili.com/captcha/gc?cType=2&vcType=2&_=1539152432261"
        "https://www.tianyancha.com/verify/geetest.xhtml?uuid=1567667683435", headers=headers
    ).json()["data"]
    result = crack(geeData["gt"], geeData["challenge"], referer)
    print("result_Json:"+str(result))
    if result["validate"] != None:
        print("validate:"+result["validate"])
        break
    login_json = {

    }
    login_response = requests.post("https://www.tianyancha.com/cd/login.json")

