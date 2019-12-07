# virmach
功能：virmach黑五促销页面监控 低于设定的价格发送邮件提醒并记录所有的服务器价格

<h3>1.环境安装</h3>
切换到本项目根目录运行</br>
pip install -r requirements.txt

<h3>2.修改邮件配置</h3>
位于benzhu\email.py文件。</br> 修改发信方的邮箱、发信方的密码或者授权码、收信方的邮箱、发信服务器、发信端口。

<h3>3.修改微信提醒配置</h3>
<a href="http://sc.ftqq.com/?c=wechat&a=bind">点开链接前往Server酱官网</a></br>
登陆github然后微信绑定后得到链接放入benzhu\message.py的47行。</br>
解开benzhu/spiders/itcast.py的59行注解

<h3>4.修改设定的价格</h3>
修改benzhu/spiders/itcast.py文件的44行数字15。</br>
<img src="https://ae01.alicdn.com/kf/U6deffc8db2374314b59bd4b424a2a5dbo.png"  alt="修改设定的价格" />

<h3>5.启动</h3>
启动位于根目录的time.py即可启动本程序。

<h3>6.日志、文件</h3>
记录的历史的价格位于benzhu/data/textLog.txt。</br>
日志文件位于根目录all.log。

<h3>7.邮件效果图</h3>
<img src="https://ae01.alicdn.com/kf/U3d36e354d76f45348db948f9e78af3e8h.png"  alt="邮件效果图" />
