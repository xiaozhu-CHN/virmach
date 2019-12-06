import requests
import xml.dom.minidom
import json

class Message:

    def sendMessage(self,newprice):
        #post接口的短信发送
        payload = {'userid': '', 'account': '', 'password': '', 'mobile': '',
                   'content': '【笨猪网】您设置的到货提醒已到货，价格为'+newprice+'。感谢您的支持。', 'sendTime': '', 'action': 'send', 'extno': ''
                   }
        response = requests.post("", data=payload)
        doc = xml.dom.minidom.parseString(response.text).documentElement
        returnstatus = doc.getElementsByTagName("returnstatus")
        returnstatus = returnstatus[0].firstChild.data
        if(returnstatus == 'Success'):
            print("短信发送成功")
        else:
            print("短信发送失败")

    def sendTencentMessage(self):
        #腾讯云短信发送模板
        payload = {'Action': 'SendSms', 'Version': '2019-07-11', 'Region': '', 'PhoneNumberSet.0': '',
                   'TemplateID': '', 'SmsSdkAppid': '', 'Sign': '笨猪网', 'TemplateParamSet.0': '12.66'
                   }
        response = requests.post("sms.tencentcloudapi.com", data=payload)
        jsobj = json.loads(response.body)
        if(jsobj['SendStatusSet'][0]['Code'] == 'ok'):
            print("短信发送成功")
        else:
            print("短信发送失败")

if __name__ == '__main__':
    message = Message()
    message.sendMessage()