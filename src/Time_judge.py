import datetime
import requests
from WanQian import WanQian
# 范围时间
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '21:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '21:40', '%Y-%m-%d%H:%M')

# 当前时间
n_time = datetime.datetime.now()

# 判断当前时间是否在范围时间内
if n_time > d_time and n_time < d_time1:
    wanqian = WanQian()
    else:
    dk = {
        'title': '⏰ YSHIER',
        'desp': '',
    }
    dkurl = 'https://sctapi.ftqq.com/SCT171678Tl3VASs0Y6qtq9s4rEbwwNBZH.send'
    body = "{}"
    print('签到成功')
    dk['desp'] = "温馨提示：签到时间未到"
    re = requests.post(url=dkurl, data=dk)
#return re.text
