## 通知推送类型
## 可选：DingDing / Mail / PushPlus / None
notify = "DingDing"

## 钉钉机器人配置:
# access_token
dingding_access_token = "9b121xxxxxxxxxxxxxx508be80a2097xxxxxxxxx"
# secret
dingding_secret = "SEC324xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx260243754ac07708ebb905"

## 邮箱配置：
# 发信人
mail_sender = "xiluokey@163.com"
# 授权码
mail_auth_code = "EFZHSYUKTSZWSQGG"
# 收件人
mail_receiver = "2784631189@qq.com"
# smtp地址
mail_smtp_link = "smtp.163.com"
# smtp端口
mail_smtp_port = 465

# PushPlus配置：
# token
pushplus_token = "8ae89df12f18463b8317c50dabfd922d"

## 打卡信息配置：
# 打卡的accessToken
null=None
accessToken = ""
# 打卡数据
punch_in_data = {
    "questionnairePublishEntityId": "1001640744275339000980000000001",
    "answerInfoList":[
  {
    "subjectId": "1001641265120727001760000000001",
    "subjectType": "multiSelect",
    "simpleFill": null,
    "signleSelect": null,
    "signleSelectOutSideOptions": null,
    "multiSelect": {
      "optionAnswerList": [
        {
          "beSelectValue": "NotThing",
          "fillContent": "",
          "imgList": null,
          "attachmentList": null
        }
      ]
    },
    "location": null,
    "area": null,
    "date": null
  },
  {
    "subjectId": "1001641265120735001760000000001",
    "subjectType": "location",
    "simpleFill": null,
    "signleSelect": null,
    "signleSelectOutSideOptions": null,
    "multiSelect": null,
    "location": {
      "address": "广南县人民政府",
      "province": "云南省",
      "city": "文山壮族苗族自治州",
      "street": "莲城镇",
      "longitude": "105.05516",
      "latitude": "24.04645",
      "locationRangeId": "1001639551775320000050000000001",
      "deviationDistance": 238943,
      "area": "广南县"
    },
    "area": null,
    "date": null
  },
  {
    "subjectId": "1001641520558478002960000000001",
    "subjectType": "signleSelect",
    "simpleFill": null,
    "signleSelect": {
      "beSelectValue": "2",
      "fillContent": "",
      "imgList": null,
      "attachmentList": null
    },
    "signleSelectOutSideOptions": null,
    "multiSelect": null,
    "location": null,
    "area": null,
    "date": null
  },
  {
    "subjectId": "1001641520609587002900000000001",
    "subjectType": "signleSelect",
    "simpleFill": null,
    "signleSelect": {
      "beSelectValue": "2",
      "fillContent": "",
      "imgList": null,
      "attachmentList": null
    },
    "signleSelectOutSideOptions": null,
    "multiSelect": null,
    "location": null,
    "area": null,
    "date": null
  },
  {
    "subjectId": "1001642750163964005360000000001",
    "subjectType": "signleSelect",
    "simpleFill": null,
    "signleSelect": {
      "beSelectValue": "flag1646985570827",
      "fillContent": "",
      "imgList": null,
      "attachmentList": null
    },
    "signleSelectOutSideOptions": null,
    "multiSelect": null,
    "location": null,
    "area": null,
    "date": null
  },
  {
    "subjectId": "1001646985729226012700000000001",
    "subjectType": "signleSelect",
    "simpleFill": null,
    "signleSelect": {
      "beSelectValue": "1",
      "fillContent": "",
      "imgList": null,
      "attachmentList": null
    },
    "signleSelectOutSideOptions": null,
    "multiSelect": null,
    "location": null,
    "area": null,
    "date": null
  }
]
}