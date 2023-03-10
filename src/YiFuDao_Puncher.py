import requests
import json
from utils.logger import logger
from default_data import punch_in_data, accessToken
from utils.pushplus import PushPlus

class YiFuDao_Puncher:
    def __init__(self):
        self.logger = logger('YiFuDaoPuncher.log')
        self.base_url = "https://yfd.ly-sky.com"
        self.header = {
            "accessToken": accessToken,
            "userAuthType": "MS"
        }
        self.puncher_status = "ð æå¡èæ¬åå§åä¸­"
        self.logger.info("ð æå¡èæ¬åå§åä¸­")
        self.check_in_index()

    def check_in_index(self):
        try:
            url = "/ly-pd-mb/form/api/healthCheckIn/client/stu/index"
            id=None
            retry=3
            while id is None and retry>=0:
                retry-=1
                res = requests.get(self.base_url+url, headers=self.header)
                parse_data = json.loads(res.text)
                detail = dict.get(parse_data,"data")
                id = dict.get(detail,"questionnairePublishEntityId")        # è¡¨åIDï¼æ¯æ¥ä¸å
                filling_status = dict.get(detail, "hadFill")                # å¡«åç¶æ
                start_time = dict.get(detail, "fillStartTime")  # è·åé®å·å¼å§æ¶é´
                if start_time:
                    break
            self.logger.info("â å·²è·åå¥åº·æå¡ä¿¡æ¯")
            self.logger.info(str(detail))
            self.puncher_status = "â å·²è·åå¥åº·æå¡ä¿¡æ¯"
            if id is None:
                if start_time is not None:
                    self.logger.war("â è¿æªå°æå¡æ¶é´ï¼èæ¬èªå¨ç»æ")
                    self.puncher_status = "â è¿æªå°æå¡æ¶é´ï¼èæ¬èªå¨ç»æ"
                else:
                    self.logger.error("â è·åé®å·å¤±è´¥ï¼è¯·ç¨åéè¯")
                    self.logger.error(str(parse_data))
                    self.puncher_status = "â è·åé®å·å¤±è´¥ï¼è¯·ç¨åéè¯"
                return 0
            if filling_status is False:
                self.logger.info("â ä»å¤©ææªæå¡ï¼å°è¯è¿è¡æå¡")
                self.puncher_status = "â ä»å¤©ææªæå¡ï¼å°è¯è¿è¡æå¡"
                self.check_in_detail(str(id))
            else:
                self.logger.war("â ä»å¤©å·²ç»æå¡ï¼èæ¬èªå¨ç»æ")
                self.puncher_status = "â ä»å¤©å·²ç»æå¡ï¼èæ¬èªå¨ç»æ"
                return 0
        except Exception as e:
            self.logger.error("â è·åå¥åº·æå¡ä¿¡æ¯å¤±è´¥")
            self.logger.error(str(parse_data))
            self.logger.error(e)
            self.puncher_status = "â è·åå¥åº·æå¡ä¿¡æ¯å¤±è´¥"

    def check_in_detail(self,id):
        try:
            url = "/ly-pd-mb/form/api/questionnairePublish/" + str(id) + "/getDetailWithAnswer"
            res = requests.get(self.base_url+url,headers=self.header)
            parse_data = json.loads(res.text)
            subjectList = dict.get(dict.get(dict.get(parse_data,"data"),"questionnaireWithSubjectVo"),"subjectList")

            question_id_list = []
            answer_id_list = []
            for i in subjectList:
                question_id_list.append(i["id"])
            for i in punch_in_data["answerInfoList"]:
                answer_id_list.append(i["subjectId"])

            # å¤æ­é¢è®¾ç­æ¡ä¸å½åé®å·çé¡¹æ¯å¦ç¸ç¬¦
            if answer_id_list == question_id_list:
                punch_in_data["questionnairePublishEntityId"] = str(id)
                self.logger.info("â é¢è®¾ç­æ¡ä¸å½åé®å·çé¡¹ç¸ç¬¦ï¼æ¬æ¬¡æå¡çé®å·idä¸º{}".format(punch_in_data["questionnairePublishEntityId"]))
                self.puncher_status = "â é¢è®¾ç­æ¡ä¸å½åé®å·çé¡¹ç¸ç¬¦ï¼æ¬æ¬¡æå¡çé®å·idä¸º{}".format(punch_in_data["questionnairePublishEntityId"])
                self.check_in_save()
            else:
                self.logger.error("â é¢è®¾ç­æ¡ä¸å½åé®å·çé¡¹ä¸ç¸ç¬¦,èæ¬å·²ç»æ")
                self.puncher_status = "â é¢è®¾ç­æ¡ä¸å½åé®å·çé¡¹ä¸ç¸ç¬¦,èæ¬å·²ç»æ"
                return 0
        except Exception as e:
            self.logger.error(e)

    def check_in_save(self):
        try:
            url = "/ly-pd-mb/form/api/answerSheet/saveNormal"
            header = self.header
            header["Content-Type"] = "application/json"
            res = requests.post(self.base_url+url,data=json.dumps(punch_in_data),headers=header)
            parse_data = json.loads(res.text)
            if parse_data["code"] == 200:
                self.logger.info("â æå¡æåï¼{}".format(parse_data["message"]))
                self.puncher_status = "â æå¡æåï¼{}".format(parse_data["message"])
            else:
                self.logger.error("â æå¡å¤±è´¥ï¼{}".format(parse_data["message"]))
                self.puncher_status = "â æå¡å¤±è´¥ï¼{}".format(parse_data["message"])
                self.logger.error(parse_data)
        except Exception as e:
            self.logger.error(e)