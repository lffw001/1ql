import os
import urllib.parse
import click
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from updateCookie_Util import *

app = FastAPI()
目前电话 = ""


def get_list_item_by_index(data_list):
    """根据索引获取列表项"""
    cnt = 0
    for x in data_list:
        print(f"{cnt} -- {x}")
        cnt += 1
    index = int(input("请输入要获取的列表项索引:"))
    if index < 0 or index >= len(data_list):
        raise Exception("索引超出范围")

    return data_list[index]


def addEnv(file_path, name, value, run=False, taskName=""):
    global 目前电话
    文件路径 = (
        os.path.dirname(os.path.abspath(__file__)) + "\\" + 目前电话 + "-" + file_path
    )
    if not os.path.exists(文件路径):
        # 文件不存在,创建文件并写入内容
        with open(文件路径, "w") as f:
            content = {
                "name": name,
                "value": value,
                "remark": 目前电话,
                "run": run,
                "taskName": taskName,
            }
            json.dump(content, f)

    else:
        # 文件已存在,判断内容是否相同
        with open(文件路径, "r") as f:
            content = json.load(f)

        if content["value"] != value:
            content["value"] = value
            content["remark"] = 目前电话
            content["run"] = run
            content["taskName"] = taskName
            # 内容不同,修改内容
            with open(文件路径, "w") as f:
                f.write(json.dumps(content, ensure_ascii=False))


class Buffer(BaseModel):
    url: str
    method: str
    host: str
    path: str
    body: str
    headers: dict
    queries: dict
    context: dict


@app.post("/xapi.weimob.com")
def 好人家美味生活馆(data: Buffer):
    # return ;
    name = "X-WX-Token"
    addEnv(
        f"{data.headers['Host']}.txt",
        "hrjmwshg",
        data.headers[name],
        True,
        "好人家美味生活馆",
    )
    return data.headers[name]


@app.post("/ucode-openapi.aax6.cn")
def 甄爱粉俱乐部(data: Buffer):
    name = "Authorization"
    addEnv(
        f"{data.headers['Host']}.txt",
        "zaf_auth",
        data.headers[name],
        True,
        "微信小程序-甄爱粉俱乐部",
    )
    return data.headers[name]


@app.post("/m.jissbon.com")
def 杰士邦安心福利社(data: Buffer):
    name = "Access-Token"
    addEnv(
        f"{data.headers['Host']}.txt",
        "jsbaxfls",
        data.headers[name],
        True,
        "杰士邦安心福利社",
    )
    return data.headers[name]


@app.post("/www.kozbs.com")
def 植白说(data: Buffer):
    name = "X-Dts-Token"
    addEnv(f"{data.headers['Host']}.txt", "zbsxcx", data.headers[name], True, "植白说")
    return data.headers[name]


@app.post("/kraftheinzcrm.kraftheinz.net.cn")
def 卡夫味(data: Buffer):
    name = "token"
    addEnv(
        f"{data.headers['Host']}.txt", "kfw_data", data.headers[name], True, "卡夫味"
    )
    return data.headers[name]


@app.post("/api.wincheers.net")
def 罗技粉丝俱乐部(data: Buffer):
    name = "Authorization"
    addEnv(
        f"{data.headers['Host']}.txt",
        "ljfsjlbCookie",
        data.headers[name],
        True,
        "罗技粉丝俱乐部",
    )
    return data.headers[name]


@app.post("/web.meituan.com")
def 美团(data: Buffer):
    name = "token"
    addEnv(f"{data.headers['Host']}.txt", "bd_mttoken", data.headers[name])
    return data.headers[name]


@app.post("/api.yqslmall.com")
def 元气森林(data: Buffer):
    name = "Authorization"
    addEnv(
        f"{data.headers['Host']}.txt",
        "yqsl",
        data.headers[name].replace("Bearer ", ""),
        True,
        "微信小程序-元气森林",
    )
    return data.headers[name]


@app.post("/apichuanti.scleader.cn")
def 引体向上(data: Buffer):
    name = "Authorization"
    addEnv(
        f"{data.headers['Host']}.txt",
        "gfq",
        data.headers[name].replace("Bearer ", ""),
        True,
        "引体向上",
    )
    return data.headers[name]


@app.post("/consumer-api.quncrm.com")
def 雀巢专业餐饮大厨精英荟(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "qczy_token",
        f"{data.headers['X-Access-Token']}#{data.headers['X-Account-Id']}",
        True,
        "微信小程序-雀巢专业餐饮大厨精英荟",
    )
    return ""


@app.post("/smp-api.iyouke.com")
def meiyang会员积分(data: Buffer):
    if data.headers["appId"] == "wxa20c0c10a072172e":
        addEnv(
            f"{data.headers['Host']}_wxa20c0c10a072172e.txt",
            "wx_xt",
            data.headers["Authorization"],
            True,
            "微信小程序-向太的会客厅会员中心",
        )
        pass
    else:
        addEnv(
            f"{data.headers['Host']}.txt",
            "my_auth",
            data.headers["Authorization"],
            True,
            "微信小程序-meiyang会员积分",
        )
    return ""


@app.post("/app.fjxzj.com")
def 康佰家(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "kbj_token",
        data.headers["token"],
        True,
        "微信小程序-康佰家",
    )
    return ""


@app.post("/uic.youzan.com")
def 朵茜情调生活馆(data: Buffer):
    if "Extra-Data" in data.headers:
        extra = json.loads(data.headers["Extra-Data"])
        addEnv(
            f"{data.headers['Host']}.txt",
            "dqqdshgck",
            f"{data.queries['access_token']}#{extra['sid']}#{extra['sid']}",
            True,
            "微信小程序-朵茜情调生活馆",
        )
    return ""


@app.post("/api.gaojihealth.cn")
def 高济健康(data: Buffer):
    if "userId" in data.queries:
        addEnv(
            f"{data.headers['Host']}.txt",
            "wx_gjjkpro_data",
            f"{data.queries['userId']}&{data.headers['Authorization']}",
            True,
            "高济健康pro小程序签到",
        )
    return ""


@app.post("/channel.cheryfs.cn")
def 好奇车生活(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "hqcshck",
        data.headers["accountId"],
        True,
        "好奇车生活签到",
    )
    return data


@app.post("/yx.jsh.com")
def 卡萨帝(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "ksdck",
        data.headers["Authorization"],
        True,
        "卡萨帝",
    )
    return ""


@app.post("/fscrm.kraftheinz.net.cn")
def 卡夫亨(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt", "kfh_data", data.headers["token"], True, "卡夫亨"
    )
    return ""


@app.post("/clubwx.hm.liby.com.cn")
def 立白小白白会员(data: Buffer):
    try:
        addEnv(
            f"{data.headers['Host']}.txt",
            "lbvip",
            f"{data.headers['unionId']}#{data.headers['X-wxde54fd27cb59db51-Token']}",
            True,
            "立白小白白会员俱乐部",
        )
    except:
        pass
    try:
        addEnv(
            f"{data.headers['Host']}_wx_miss.txt",
            "wx_miss",
            f"{data.headers['unionId']}#{data.headers['X-wx8465e1173d1e11b0-Token']}",
            True,
            "微信小程序-蜜丝miss",
        )
    except:
        pass
    return ""


@app.post("/mmembership.lenovo.com.cn")
def 联想(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lx_data",
        f"{data.headers['accessToken']}#{data.headers['serviceToken']}#{data.headers['SERVICE-AUTHENTICATION']}#{data.headers['lenovoId']}",
    )
    return ""


@app.post("/www.milkcard.mall.ryytngroup.com")
def 认养一头牛(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "ryytn_data",
        data.headers["X-Auth-Token"],
        True,
        "微信小程序-认养一头牛商城",
    )
    return ""


@app.post("/apis.folidaymall.com")
def 托迈酷客(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "tmkk",
        data.headers["Authorization"].replace("Bearer ", ""),
        True,
        "托迈酷客",
    )
    return ""


@app.post("/fwdt.shengongshe.org")
def 申工社(data: Buffer):
    addEnv(f"{data.headers['Host']}.txt", "sgs", data.headers["token"], True, "申工社")
    return ""


@app.post("/qualcomm.growthideadata.com")
def 骁龙骁友会(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "wx_xlxyh_data",
        f"{data.headers['sessionKey']}&{data.headers['userId']}",
        True,
        "微信小程序_骁龙骁友会",
    )
    return ""


@app.post("/customer.yueyequan.cn")
def 悦野圈(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "yyq_data",
        f"{data.headers['cookie']}&{data.headers['cookie'].split('userid=')[1].split(';')[0]}",
        True,
        "悦野圈",
    )
    return ""


@app.post("/mystore-01api.watsonsvip.com.cn")
def 屈臣氏(data: Buffer):
    addEnv(
        f"{data.headers['Host']}1.txt",
        "qcsAuthorization",
        data.headers["Authorization"],
    )
    addEnv(
        f"{data.headers['Host']}2.txt",
        "qcsunionId",
        data.headers["unionId"],
        True,
        "屈臣氏",
    )
    return ""


@app.post("/wx-fulishe.msx.digitalyili.com")
def 伊利会员福利社(data: Buffer):
    encryptsessionid = urllib.parse.parse_qs(data.body).get("encryptsessionid", [])[0]
    addEnv(
        f"{data.headers['Host']}.txt",
        "ylhyencryptsessionid",
        encryptsessionid,
        True,
        "伊利会员福利社",
    )
    return ""


@app.post("/midend.icar-ecology.com")
def 奇瑞EV(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "cheryev",
        data.headers["Authorization"].replace("Bearer ", ""),
        True,
        "V3",
    )
    return ""


@app.post("/hweb-mbf.huazhu.com")
def 华住(data: Buffer):
    # pprint.pprint(data.headers)
    addEnv(
        f"{data.headers['Host']}.txt",
        "huazhu_cookies",
        data.headers["Cookie"],
        True,
        "微信小程序-华住签到",
    )
    return ""


@app.post("/mvip.midea.cn")
def 美的会员(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "wx_midea",
        data.headers["Cookie"],
        True,
        "微信小程序-美的会员",
    )
    return ""


@app.post("/durex.ixiliu.cn")
def 杜蕾斯会员中心(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "dlshyzx",
        data.headers["Access-Token"],
        True,
        "杜蕾斯会员中心",
    )
    return ""


@app.post("/cps.hisense.com")
def 海信爱家(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "HISENSE_CPS",
        data.headers["Cookie"],
        True,
        "海信爱家",
    )
    return ""


@app.post("/pepcoinnew.pepcoinbypepsico.com.cn")
def 百事乐元(data: Buffer):
    jsonBody = json.loads(data.body)
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_bsly_Cookie",
        jsonBody["token"],
        True,
        "百事乐元",
    )
    return ""


@app.post("/ksfshopapp.2qrs.cn")
def 康师傅饮品(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_ksfyp_Cookie",
        data.headers["Authorization"],
        True,
        "康师傅饮品",
    )
    return ""


@app.post("/member-api.mengniu.cn")
def 蒙牛营养生活家(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_mnflag_Cookie",
        f"{data.headers['X-Token'].replace('Bearer ', '')}&{data.queries['unionId']}",
        True,
        "蒙牛营养生活家",
    )
    return ""


@app.post("/mc.kukahome.com")
def 顾家家居会员俱乐部(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_gjjjhyjlb_Cookie",
        f"{data.headers['X-Customer']}&{data.headers['AccessToken']}",
        True,
        "顾家家居会员俱乐部",
    )
    return ""


@app.post("/www.jumpingcarp.cn")
def 庙友之家(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "miaoyouHome",
        data.headers["Cookie"].replace("JSESSIONID=", ""),
        True,
        "wx_庙友之家",
    )
    return ""


@app.post("/jjw.jingjiu.com")
def 劲友家(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_jyj_Cookie",
        data.headers["Authorization"],
        True,
        "劲友家",
    )
    return ""


@app.post("/member.kwwblcj.com")
def 口味王(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "lekebo_kww_Cookie",
        f"{data.queries['memberId']}&{data.queries['kwwMember.unionid']}",
        True,
        "口味王",
    )
    return ""


@app.post("/club.biqr.cn")
def 康师傅畅饮社(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "ksfcys_data",
        data.headers["Token"],
        True,
        "微信小程序-康师傅畅饮社",
    )
    return ""


@app.post("/zm.t7a.cn")
def 战马能量星球(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "zmnlxq",
        data.queries["safe"],
        True,
        "新战马能量星球.js",
    )
    return ""


@app.post("/shopapi.yxtmart.cn")
def 一心堂(data: Buffer):
    UserGuid = urllib.parse.parse_qs(data.body).get("UserGuid", [])[0]
    addEnv(
        f"{data.headers['Host']}.txt", "yxtGUid", UserGuid, True, "微信小程序-一心堂"
    )
    return ""


@app.post("/scrm-prod.shuyi.org.cn")
def 书亦烧仙草(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "sysxc_data",
        data.headers["auth"],
        True,
        "书亦烧仙草",
    )
    return ""


@app.post("/bg-hardcore.ab-inbev.cn")
def HAPI哈啤硬核街(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "wx_hapi_cookie",
        f"{data.headers['openId']}&{data.headers['sign']}&{data.headers['timestamp']}",
        True,
        "HAPI哈啤硬核街",
    )
    return ""


@app.post("/jsapi.58moto.com")
def 摩托范(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "mtf_data",
        f"{data.headers['token']}&{data.headers['uid']}",
        True,
        "摩托范",
    )
    return ""


@app.post("/activity.yonghuivip.com")
def 永辉生活(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "yhsh",
        f'{data.queries["deviceid"]}&{data.queries["access_token"]}',
        True,
        "永辉生活",
    )
    return ""


@app.post("/tc.qzfwckj.com")
def 青柳同城圈(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "qltcq",
        data.headers["token"],
        True,
        "青柳同城圈",
    )
    return ""


@app.post("/miniapp.yaduo.com")
def 亚朵(data: Buffer):
    cookie = data.headers["Cookie"].split(";")
    for x in cookie:
        if "user-valid=" in x:
            addEnv(
                f"{data.headers['Host']}.txt",
                "yd_wxcookies",
                f'{x.strip().replace("user-valid=", "")}#{data.queries["token"]}',
                True,
                "微信小程序-亚朵",
            )
    return ""


@app.post("/wx-center.zippo.com.cn")
def zippo(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "zippo_auth",
        data.headers["Authorization"],
        True,
        "微信小程序-zippo",
    )
    return ""


@app.post("/gateway.jmhd8.com")
def 农夫山泉2024(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "nfsqCookie",
        data.headers["apitoken"],
        True,
        "农夫山泉2024",
    )
    return ""


@app.post("/m.tk.cn")
def 泰康在线保险(data: Buffer):
    jsonbody = json.loads(data.body)
    addEnv(
        f"{data.headers['Host']}.txt",
        "tkzxbxCookie",
        jsonbody["body"]["unionId"],
        True,
        "泰康在线保险",
    )
    return ""


@app.post("/msmarket.msx.digitalyili.com")
def 伊利奶粉积分商城(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "yljf_token",
        data.headers["access-token"],
        True,
        "微信小程序-伊利积分",
    )
    return ""


@app.post("/wechatec.brand.wljhealth.com")
def 王老吉(data: Buffer):
    possessor = urllib.parse.parse_qs(data.body).get("possessor", [])[0]
    userCode = urllib.parse.parse_qs(data.body).get("userCode", [])[0]
    addEnv(
        f"{data.headers['Host']}.txt",
        "wljgfsc",
        f"{possessor}#{userCode}",
        True,
        "王老吉",
    )
    return ""


@app.post("/qmwebapi.qmai.cn")
@app.post("/webapi.qmai.cn")
def 霸王茶姬(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "bwcjCookie",
        data.headers["Qm-User-Token"],
        True,
        "霸王茶姬",
    )
    addEnv(
        f"{data.headers['Host']}_bwcjqq.txt",
        "bwcjqq",
        data.headers["Qm-User-Token"],
        True,
        "霸王茶姬签到",
    )
    return ""


@app.post("/superapp.jmc.com.cn")
def 江铃智行(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "jlzx",
        data.headers["Access-Token"],
        True,
        "江铃智行",
    )
    return ""


@app.post("/mk-platform.haier.net")
def 卡萨帝2(data: Buffer):
    jsonbody = json.loads(data.body)
    addEnv(
        f"{data.headers['Host']}.txt",
        "ksd",
        f'{data.headers["MK-U-User-Token"]}#{jsonbody["openId"]}',
        True,
        "海尔-卡萨帝.js",
    )
    return ""


@app.post("/mxsa.mxbc.net")
def 蜜雪冰城(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "mxbc_data",
        data.headers["Access-Token"],
        True,
        "蜜雪冰城",
    )
    return ""


@app.post("/member-pro.zhengjiamax.com")
def 正佳(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "wx_zj",
        data.headers["MemberSession"],
        True,
        "微信小程序-正佳",
    )
    return ""


@app.post("/api.pinduoduo.com")
def pdd(data: Buffer):
    addEnv(
        f"{data.headers['Host']}.txt",
        "ddgyck",
        data.headers["AccessToken"],
        True,
        "拼多多果园",
    )
    return ""


@click.command()
@click.option("--phone", default=None)
def loadPhone(phone: str):
    global 目前电话
    if phone is not None:
        目前电话 = phone
    else:
        with open("config.json", "r") as f:
            config = json.load(f)
        目前电话 = get_list_item_by_index(config["phoneList"])

    print("目前电话:" + 目前电话)
    隐藏cmd对话框()
    uvicorn.run(app, host="0.0.0.0", port=8989)


if __name__ == "__main__":
    loadPhone()
