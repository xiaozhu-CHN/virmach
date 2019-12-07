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

    def sendServerFtqq(self, item):
        # Server酱微信推送模板
        #官网链接：http://sc.ftqq.com/?c=wechat&a=bind
        desp = '服务器价格：' + item['price'] + '美元/年' + \
               '\n\n\n架构：' + item['virt'] + \
               '\n\n\n运行内存：' + item['ram'] + 'MB' + \
               '\n\n\nncpu数量：' + item['cpu'] + \
               '\n\n\n硬盘：' + item['hdd'] + 'G' + \
               '\n\n\n流量：' + item['bw'] + 'G' + \
               '\n\n\nIPV4数量：' + item['ips'] + \
               '\n\n\n地区：' + item['addres'] + \
               '\n\n\n[购买链接1](https://virmach.com/black-friday-cyber-monday/)'
        payload = {'text': 'virmach优惠', 'desp': desp}
        #把链接放入下面即可
        response = requests.post("https://sc.ftqq.com/[SCKEY(登入后可见)].send", data=payload)
        # 解析json数据
        print(response.text)
        if (response.text != 'None' or response.text != ''):
            jsobj = json.loads(response.text)
            if (jsobj['errmsg'] == 'success'):
                print('微信推送成功')
            else:
                print('微信推送失败')
        else:
            print('微信推送反馈失败')