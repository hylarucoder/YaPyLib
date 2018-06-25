import psutil

from yapylib.helpers.datetime import fmt_cur_date_time
from yapylib.helpers.osx import get_internal_ip

mail_template = {
    "title": "[爬虫][某潜力数据][某网]小时报 {}".format(fmt_cur_date_time()),
    "summary_title": "[某网]小时报",
    "summary_introduction": "[某网]小时报简单报到",
    "head_image_link": "http://oh1n2bfoj.bkt.clouddn.com/mail_header.png",
    "avatar_link": "http://oh1n2bfoj.bkt.clouddn.com/avatar.png",
    "ip_address": get_internal_ip(),
    "os_version": "Mac",
    "gen_time": "{}".format(fmt_cur_date_time()),
    "status": "运行正常",
    "cn_name": "无与童比",
    "en_name": "Micheal Garder",
    "nickname": "twocucao",
    "blog_url": "http://dwz.cn/45rppG",
    "github_url": "https://github.com/twocucao",
    "private_email": "twocucao@gmail.com",
    "company_email": "twocucao@gmail.com",
    "introduction": "ROR程序员, 现专攻Python方向, Python Web, 爬虫, 数据分析与数据仓库." +
    "现在某潜力数据做爬虫工程师兼数据挖掘工程师. 如果有技术问题, 请及时联系我.",
    "sections": [
        {
            "title": "节点状态",
            "body": """
        <p> 1. cpu_percent -> {cpu_percent} </p>
        <p> 2. cpu_count   -> {cpu_count} </p>
        <p> 3. vitual_memory -> {vitual_memory} </p>
        <p> 4. disk_partitions -> {disk_partitions} </p>
        """.format(
                cpu_percent=psutil.cpu_percent(),
                cpu_count=psutil.cpu_count(),
                vitual_memory=psutil.virtual_memory(),
                disk_partitions=psutil.disk_partitions())
        },
        {
            "title": "数据仓库状态",
            "body": """
            <table bounder="1">
            <thead>
                <tr>
                    <th></th>
                    <th>新增数据</th>
                    <th>更新数据</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>爬虫2</td>
                    <td>200条</td>
                    <td>400条</td>
                </tr>
                <tr>
                    <td>爬虫3</td>
                    <td>200条</td>
                    <td>400条</td>
                </tr>
                <tr>
                    <td>爬虫7</td>
                    <td>200条</td>
                    <td>400条</td>
                </tr>
                <tr>
                    <td>爬虫8</td>
                    <td>200条</td>
                    <td>400条</td>
                </tr>
            </tbody>
            </table>
            """,
        },
        {
            "title": "爬虫抓取状态",
            "body": """
            <p> 1. 现在正在抓取的任务为: {tasks_name} </p>
            <p> 2. 最近抓取数量为: {latest_stats} </p>
        """.format(tasks_name=",".join(["猫眼数据", "其他数据"]), latest_stats="1999w")
        }
    ]
}


def test_mail_util():
    # attachments = [
    # ]
    # flag = Mail(mail_type=MAIL_TYPE_HTML).setContent(
    #     mail_template["title"], mail_template).attach_files(attachments).send()

    assert True
