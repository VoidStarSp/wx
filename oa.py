# encoding:utf-8

import json, pip._vendor.requests as requests, time, random, datetime, chinese_calendar
from twilio.rest import Client

account_sid = 'AC7ff1591a89b231529de00fac7dbe536b'
auth_token = '207a2e947866657876178eb50a087a8d'
client = Client(account_sid,auth_token)

# 判断是否工作日
today = datetime.datetime.today()
if not chinese_calendar.is_workday(today):
    quit()
loginUrl = 'http://oa.ittx.com.cn/api/hrm/login/checkLogin'

loginData = {
    'islanguid': 7,
    'loginid': 'qzou@ittx.com.cn',
    'userpassword': '963016a59a68a9e55b6d563403ce8863_random_',
    'dynamicPassword': '',
    'tokenAuthKey': '',
    'validatecode': '',
    'validateCodeKey': '',
    'logintype': 1,
    'messages': '',
    'isie': False
}
# 延迟几分钟再登陆
time.sleep(random.randint(1, 540))
r = requests.post(loginUrl, data=loginData)
cookie = r.headers._store['set-cookie'][1]
pubchOutUrl = 'http://oa.ittx.com.cn/api/hrm/kq/attendanceButton/punchButton'

# 打卡
r = requests.post(pubchOutUrl, headers={'Cookie': cookie})

# 打卡成功发短信
def sendMsg(phone_number, text):
    '发送短信'
    mes = client.messages.create(
        from_='+12039027934',
        body=text,
        to=phone_number
    )
    print("send msg OK!")

sendMsg('+8618516144675', '打卡成功')

