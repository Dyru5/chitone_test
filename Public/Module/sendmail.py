import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
class SendMail(object):
    def __init__(self,file=None,
                 username='18365025357@163.com',
                 passwd='FLVWNNJCHEUFGAHI',
                 recv=['dg6366@job5156.com'],
                 title='Job5156自动化测试报告',
                 content='Job5156自动化测试报告-魏东宇',
                 ssl=False,
                 email_host='smtp.163.com',port=25,ssl_port=465):
        '''
        :param username: 发件人邮箱
        :param passwd: 授权码
        :param recv: 收件人，多个要传list ['a@qq.com','b@qq.com]
        :param title: 邮件标题
        :param content: 邮件正文
        :param file: 附件路径，如果不在当前目录下，要写绝对路径，默认没有附件
        :param ssl: 是否安全链接，默认为普通
        :param email_host: smtp服务器地址，默认为163服务器
        :param port: 非安全链接端口，默认为25
        :param ssl_port: 安全链接端口，默认为465
        '''
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
        self.ssl = ssl
        self.ssl_port = ssl_port
    def send_mail(self):
        msg = MIMEMultipart()
        #发送内容的对象
        if self.file:#处理附件的
            file_name = os.path.split(self.file)[-1]#只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f,"base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                #base64.b64encode(file_name.encode()).decode()
                new_file_name='=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                #这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"'%(new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))#邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host,port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host,port=self.port)
        #发送邮件服务器的对象
        self.smtp.login(self.username,self.passwd)
        try:
            self.smtp.sendmail(self.username,self.recv,msg.as_string())
            pass
        except Exception as e:
            print('出错了。。',e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendMail(
        ssl=True,
    )
    m.send_mail()