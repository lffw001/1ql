"""
cron: 0 3 * * *
new Env("微信小程序-陈子壹")
env add wx_czy

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""
import ApiRequest
import mytool

tokenName = 'wx_czy'
msg = ''


class czy(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'h5.youzan.com',
            'Connection': 'keep-alive',
            'xweb_xhr': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI '
                          'MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b17)XWEB/9185',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://servicewechat.com/wxa0461394dd59e7cf/15/page-frame.html',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        self.access_token = data.split("#")[0]
        self.sid = data.split("#")[1]
        self.uuid = data.split("#")[2]
        self.sec.headers[
            'Extra-Data'] = f'{{"is_weapp":1,"sid":"{self.sid}","version":"2.195.7.101","client":"weapp","bizEnv":"wsc","uuid":"{self.uuid}","ftime":{mytool.getMSecTimestamp()}}}'

    def login(self):
        params = {
            'checkinId': '3903109',
            'app_id': 'wxa0461394dd59e7cf',
            'kdt_id': '129428237',
            'access_token': self.access_token,
        }

        rj = self.sec.get('https://h5.youzan.com/wscump/checkin/checkinV2.json', params=params).json()
        print(rj)


if __name__ == '__main__':
    ApiRequest.ApiMain(['login']).run(tokenName, czy)
