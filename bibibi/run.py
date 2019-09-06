import geetest
import requests

total = 0
suc = 0
referer = "https://www.tianyancha.com/"
data = {'uuid':'"1567667683435"'}
headers = {
        "Referer": referer,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Content-Type":"application/json; charset=UTF-8",
        "Cookie":"aliyungf_tc=AQAAAC5hGzTlNwIASFfU3uAVPAP1efmA; ssuid=5689407811; _ga=GA1.2.560332842.1567482068; csrfToken=75IdN5-VrGBNY2cyvM1_Nax2; TYCID=a9743a10cdfc11e98a202b8661be8d5a; undefined=a9743a10cdfc11e98a202b8661be8d5a; jsid=SEM-BAIDU-PZ1907-SY-000100; token=41c7ea2717c7471ab5e2c9b18159b7af; _utm=d0dd9b7de3ea468a8f1ee7b53b63c1a0; _gid=GA1.2.1197026298.1567650904; RTYCID=94950c135ae0443088a2ebb91f2bbc56; CT_TYCID=e6673be627ab4f0095688d1b1689e545; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1567482068,1567561423,1567651961; bannerFlag=true; refresh_page=0; cloud_token=e6c2770fd7904ba587223c8f20381eb6; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1567667671; _gat_gtag_UA_123487620_1=1",
        "Host":"www.tianyancha.com",
        "Origin":"https://www.tianyancha.com"
    }
while True:
    total = total + 1
    geeData = requests.post(
        #"https://passport.bilibili.com/captcha/gc?cType=2&vcType=2&_=1539152432261"
        "https://www.tianyancha.com/verify/geetest.xhtml?uuid=1567667683435", headers=headers
    ).json()["data"]
    print("geeData:" + str(geeData))
    #referer = "https://passport.bilibili.com/login"
    #referer = "https://www.tianyancha.com/"
    ans = geetest.crack(geeData["gt"], geeData["challenge"], referer)
    print(ans)
    #if "success" in ans.keys() and ans["success"] == 1:
    #    suc += 1
    #print("Acc", "%.2f" % (suc * 1.00 / total), suc, total, ans)
