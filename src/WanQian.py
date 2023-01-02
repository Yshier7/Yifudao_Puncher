import requests
import json
from urllib.parse import urlencode
import jsonpath
# -*- encoding:utf-8 -*-

# 抓包获取个人token
accesstoken = ''
base_url = "https://yfd.ly-sky.com/" # 奕辅导主域名
## 发送通知函数
class WanQian:
def send(code):
    dk = {
        'title': '⏰ YSHIER',
        'desp': '',
    }
    dkurl = 'https://sctapi.ftqq.com/SCT104304TAmhC9xe9VLMc5wbsNfY11usJ.send'
    body = "{}"
    if code == 200:
        print('签到成功')
        dk['desp'] = "温馨提示：奕辅导签到成功 ✔"
        re = requests.post(url=dkurl, data=dk)
        return re.text
    else:
        print('签到失败')
        dk['desp'] = "温馨提示：奕辅导签到失败 ❌"
        re = requests.post(url=dkurl, data=dk)
        return re.text

## 获取签到列表函数
def get_List(base_url):
    list_url = base_url + 'ly-pd-mb/form/api/questionnairePublish/pagelistByFill'
    sign_data = {
        "pageWith": {"page": 1, "pageSize": 10},
        "scene": "LocationCheckIn",
        "title": ""
    }
    header = {
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "charset": "utf-8",
        "userauthtype": "MS",
        "Host": "yfd.ly-sky.com",
        "Content-Length": "74",
        "content-type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://servicewechat.com/wx217628c7eb8ec43c/55/page-frame.html",
        "accesstoken": accesstoken
    }
    data = urlencode(sign_data)
    response = requests.post(url=list_url, data=json.dumps(sign_data), headers=header)

    r = json.loads(response.text)
    # print(r)
    # print(r['data']['list'][0]['questionnairePublishEntityId'])
    location_list = jsonpath.jsonpath(r,'$..questionnairePublishEntityId')

    return (location_list[0])

def get_subId():
    sub_url = base_url + 'ly-pd-mb/form/api/questionnairePublish/' + str(newList) + '/getDetailWithAnswer'
    heaader = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; 2106118C Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3225 MMWEBSDK/20220303 Mobile Safari/537.36 MMWEBID/1401 MicroMessenger/8.0.21.2120(0x2800153B) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
        'accesstoken': accesstoken,
        'userauthtype': 'MS',
        'Referer': 'https://servicewechat.com/wx217628c7eb8ec43c/58/page-frame.html'
    }

    sub_request = requests.get(url=sub_url, headers=heaader)
    # return sub_request.text
    sub_json = json.loads(sub_request.text)
    print(sub_json)
    return sub_json['data']['questionnaireWithSubjectVo']['subjectList'][0]['id']


## 模拟签到请求
def sign_In(base_url,location_list,newid):
    sign_url = base_url + 'ly-pd-mb/form/api/answerSheet/saveNormal'
    sign_data = {
      "questionnairePublishEntityId": location_list,
      "answerInfoList": [
        {
          "subjectId": newid,
          "subjectType": "location",
          "location": {
            "address":"(汇通街)" ,
            "city": "昆明市",
            "province": "云南省",
            "area": "呈贡区",
            "latitude":24.83524658203125,
            "longitude":102.86132025824652,
            "street": "吴家营街道",
            "deviationDistance": "",
            "locationRangeId": "1001639551775320000050000000001"
          }
        }
      ]
    }
    header = {
        "Accept-Encoding": "gzip,compress,br,deflate",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "charset": "utf-8",
        "userauthtype": "MS",
        "Host": "yfd.ly-sky.com",
        "Content-Length": "390",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wx217628c7eb8ec43c/39/page-frame.html",
        "accesstoken": accesstoken
    }

    data = urlencode(sign_data)
    response = requests.post(url=sign_url, data=json.dumps(sign_data), headers=header)
    print(response.text)
    r = json.loads(response.text)
    return (r['code'])




if __name__ == '__main__':
    newList = get_List(base_url)
    newid = get_subId()
    res = sign_In(base_url,newList, newid)
    result = send(res)
    print(result)






