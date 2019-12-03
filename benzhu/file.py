import json
import os
import time

class JsonFile():
    path = os.path.split(os.path.realpath(__file__))[0]

    #保存本次读取到的数据
    def setJsonFile(slef,response):
        filename = os.path.join(JsonFile.path,'data','data.json')
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

    #获取上一次获取到的价格数据
    def getJsonFile(self):
        if(os.path.exists(os.path.join(JsonFile.path,'data','data.json'))):
            with open(os.path.join(JsonFile.path,'data','data.json'), 'r') as load_f:
                date = json.load(load_f)
        else:
            return "0"
        str1 = "."
        number = str(date['price'])
        if(number == 'None' or number ==''):
            return "0"
        else:
            number = number[1:number.index(" ")]
            return number

    #将服务器信息保存进.txt文件
    def textLog(self,newprice,oldnumber,item):
        if(newprice!=oldnumber):
            filename = os.path.join(JsonFile.path,'data','textLog.txt')
            with open(filename, "a", encoding="utf-8") as f:
                f.write("时间："+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+
                       "  服务器价格："+item['price']+'美元/年'+
                       "  架构："+item['virt']+
                       "  运行内存：" + item['ram'] +"MB"+
                       "  cpu数量：" + item['cpu'] +
                       "  硬盘："+item['hdd']+"G"+
                       "  流量：" + item['bw']+"G"+
                       "  IPV4数量：" + item['ips']+
                       "  地区：" + item['addres']+ "\n")