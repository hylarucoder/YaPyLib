import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from yapylib.decorators.retries import retries
from yapylib.settings import MAIL_SERVER, MAIL_DEFAULT_SENDER, MAIL_PASSWORD, SENDER, RECEIVERS, DEBUG
from yapylib.utils.template_util import render_template

MAIL_TYPE_TEXT = 1
MAIL_TYPE_TEXT_ATTACHMENT = 2
MAIL_TYPE_HTML = 3
MAIL_TYPE_HTML_ATTACHMENT = 4

mail_smtp_host = MAIL_SERVER
mail_user = MAIL_DEFAULT_SENDER
mail_password = MAIL_PASSWORD


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


class Mail(object):
    """
    1.发送普通邮件
    2.发送带有样式的邮件
    3.发送固定某几个模板的邮件.
    4.发送定制的邮件.

    USAGE:
        sender = {
        'name':'Micheal gardner',
        'email':'1xxxxx@qq.com'
        }
        receivers = [
            {
                'name':'Micheal gardner',
                'email':'1xxxxxx@qq.com'
            }
            ,
            {
                'name':'twocucao',
                'email':'17xxxx@qq.com'
            }
        ]
        Mail(sender,receivers).setContentText().send()
        Mail(sender,receivers).setContentHTML().send()

    """

    def __init__(self, sender=None, receivers=None, mail_type=MAIL_TYPE_TEXT):
        """
        :param sender:
        :param receivers:
        """
        if sender is None or receivers is None:
            self.LOCAL_SENDER = SENDER
            self.LOCAL_RECEIVERS = RECEIVERS
        else:
            self.LOCAL_SENDER = sender
            self.LOCAL_RECEIVERS = receivers

        self.sender = self.LOCAL_SENDER["email"]
        self.receivers = [mail['email'] for mail in self.LOCAL_RECEIVERS]
        self.mail_type = mail_type
        self.msg = MIMEMultipart('alternative')

        pass

    def setContentText(self, mail_subject, content_text):
        self.msg["Subject"] = Header(mail_subject, 'utf-8').encode()
        self.msg["From"] = _format_addr('Micheal Gardner <%s>' % self.LOCAL_SENDER["email"])
        self.msg["To"] = _format_addr('管理员 <%s>' % [receiver["email"] for receiver in self.LOCAL_RECEIVERS][0])
        # print([receiver["email"] for receiver in self.LOCAL_RECEIVERS][0])
        text_part = MIMEText(content_text, 'plain', _charset="utf-8")
        self.msg.attach(text_part)
        # print(self.msg)
        return self

    def setContent(self, mail_subject, content):
        self.msg["Subject"] = Header(mail_subject, 'utf-8').encode()
        self.msg["From"] = _format_addr('Micheal Gardner <%s>' % self.LOCAL_SENDER["email"])
        self.msg["To"] = _format_addr('管理员 <%s>' % [receiver["email"] for receiver in self.LOCAL_RECEIVERS][0])
        # print([receiver["email"] for receiver in self.LOCAL_RECEIVERS][0])
        text = content
        text_part = MIMEText(str(text), 'plain', _charset="utf-8")
        self.msg.attach(text_part)
        html = self.get_rendered_html(content)
        html_part = MIMEText(html, 'html', _charset="utf-8")  # 实例化为html部分
        self.msg.attach(html_part)  # 绑定到message里
        # print(self.msg)
        return self

    def get_rendered_html(self, content):
        return render_template("daliy_report_tpl.html",
                               title=content["title"],
                               summary_title=content["summary_title"],
                               summary_introduction=content["summary_introduction"],
                               head_image_link=content["head_image_link"],
                               avatar_link=content["avatar_link"],
                               ip_address=content["ip_address"],
                               os_version=content["os_version"],
                               gen_time=content["gen_time"],
                               status=content["status"],
                               cn_name=content["cn_name"],
                               en_name=content["en_name"],
                               nickname=content["nickname"],
                               blog_url=content["blog_url"],
                               github_url=content["github_url"],
                               private_email=content["private_email"],
                               company_email=content["company_email"],
                               introduction=content["introduction"],
                               sections=content["sections"]
                               )

    def send_error_mail(self):
        pass

    def send_warning_mail(self):
        pass

    def send_daily_notifications_mail(self):
        pass

    def send_hourly_notifications_mail(self):
        pass

    def send_monthly_notifications_mail(self):
        pass

    def attach_files(self, files):
        for f in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(f, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
            self.msg.attach(part)
        return self

    @retries(3)
    def send(self):
        try:
            smtpObj = smtplib.SMTP_SSL()
            if DEBUG:
                pass
                # smtpObj.set_debuglevel(1)
            smtpObj.connect(mail_smtp_host)
            smtpObj.login(mail_user[1], mail_password)
            smtpObj.sendmail(self.sender, self.receivers, self.msg.as_string())
            smtpObj.close()
            return True
        except smtplib.SMTPException:
            return False
        pass
