
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class benzhuEmail():

    def send(item):
        # 发信方的信息：发信邮箱，QQ 邮箱授权码
        from_addr = '发件的邮件'
        password = '邮箱密码'

        # 收信方邮箱
        to_addr = '收件的邮箱'

        # 发信服务器
        smtp_server = '发信的服务器'

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
        msg = MIMEText('服务器价格：'+item['price']+'美元/年'+
                       '</br>架构：'+item['virt']+
                       '</br>运行内存：' + item['ram'] +'MB'+
                       '</br>cpu数量：' + item['cpu'] +
                       '</br>硬盘：'+item['hdd']+'G'+
                       '</br>流量：' + item['bw']+'G'+
                       '</br>IPV4数量：' + item['ips']+
                       '</br>地区：' + item['addres'] +
                       '</br><a href="https://virmach.com/black-friday-cyber-monday/">购买链接</a>'
                       , 'html', 'utf-8')

        # 邮件头信息
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('Virmach优惠')

        # 开启发信服务，这里使用的是加密传输
        server = smtplib.SMTP_SSL(host='发信的服务器')
        #注意端口 这里默认465
        server.connect(smtp_server, 465)
        # 登录发信邮箱
        server.login(from_addr, password)
        # 发送邮件
        try:
            server.sendmail(from_addr, to_addr, msg.as_string())
            print('发送邮件成功')
        except smtplib.SMTPException:
            print('发送邮件失败')
        # 关闭服务器
        server.quit()