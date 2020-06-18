# encoding:utf-8

import json, pip._vendor.requests as requests, time, random, datetime, chinese_calendar

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
time.sleep(random.randint(1, 9) * 60)
r = requests.post(loginUrl, data=loginData)
cookie = r.headers._store['set-cookie'][1]
pubchOutUrl = 'http://oa.ittx.com.cn/api/hrm/kq/attendanceButton/punchButton'

# 打卡
r = requests.post(pubchOutUrl, headers={'Cookie': cookie})


