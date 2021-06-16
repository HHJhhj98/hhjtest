# coding:utf-8
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class emailUtil():
    '''兼容163和QQ邮箱发送邮件的封装类'''
    def send_mail(self,smtpserver,port,sender,psw,receiver,file_path,subject,filename):
        '''兼容163和QQ邮箱发送邮件的方法
        :param smtpserver: 发件服务器
        :type path: str
        :param port: The :端口
        :type port: int
        :param sender: 发件人账号
        :type sender: str
        :param psw: The :密码
        :type psw: str
        :param receiver: 收件人账号
        :type receiver: list
        :param file_path: The :附件地址
        :type file_path: str
        :param subject: The :主题
        :type subject: str
        :param filename: The :附件重命名
        :type filename: str
        '''

        with open(file_path, "rb") as fp:
            mail_body = fp.read()
            msg = MIMEMultipart()
            msg["from"] = sender  # 发件人
            msg["to"] = ";".join(receiver) # 多个收件人 list 转 str
            msg["subject"] = subject  # 主题
            # 正文
            body = MIMEText(mail_body, "html", "utf-8")
            msg.attach(body)  # 附件
            att = MIMEText(mail_body, "base64", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = 'attachment; filename='+filename+''
            msg.attach(att)
            # ----------3.发送邮件------
            try:
                smtp = smtplib.SMTP()
                smtp.connect(smtpserver)  # 连服务器
                smtp.login(sender, psw)
            except:
                smtp = smtplib.SMTP_SSL(smtpserver, port)
                smtp.login(sender, psw)  # 登录
            smtp.sendmail(sender, receiver, msg.as_string())  # 发送
            smtp.quit()