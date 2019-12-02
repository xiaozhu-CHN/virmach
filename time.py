import time
import os

if __name__ == "__main__":
    print("定时任务开始")
    while True:
        os.system("scrapy crawl virmach")
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"完成一次查询")
        time.sleep(60)  #每隔1分钟循环查询一次