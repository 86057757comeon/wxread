# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 120)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

# headers、cookies是一个省略模版，本地或者docker部署时对应替换
cookies = {
    'RK': 'oxEY1bTnXf',
    'ptcz': '53e3b35a9486dd63c4d06430b05aa169402117fc407dc5cc9329b41e59f62e2b',
    'pac_uid': '0_e63870bcecc18',
    'iip': '0',
    '_qimei_uuid42': '183070d3135100ee797b08bc922054dc3062834291',
    'wr_avatar': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FeEOpSbFh2Mb1bUxMW9Y3FRPfXwWvOLaNlsjWIkcKeeNg6vlVS5kOVuhNKGQ1M8zaggLqMPmpE5qIUdqEXlQgYg%2F132',
    'wr_gender': '0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ko;q=0.5',
    'baggage': 'sentry-environment=production,sentry-release=dev-1730698697208,sentry-public_key=ed67ed71f7804a038e898ba54bd66e44,sentry-trace_id=1ff5a0725f8841088b42f97109c45862',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
}


"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
# data = {
#     "appId": "wb182564874663h152492176",
#     "b": "ce032b305a9bc1ce0b0dd2a",
#     "c": "7cb321502467cbbc409e62d",
#     "ci": 70,
#     "co": 0,
#     "sm": "[插图]第三部广播纪元7年，程心艾AA说",
#     "pr": 74,
#     "rt": 30,
#     "ts": 1727660516749,
#     "rn": 31,
#     "sg": "991118cc229871a5442993ecb08b5d2844d7f001dbad9a9bc7b2ecf73dc8db7e",
#     "ct": 1727660516,
#     "ps": "b1d32a307a4c3259g016b67",
#     "pc": "080327b07a4c3259g018787",
# }
data1 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 5120,
    'sm': '最多计算，守军三万，陈友谅六十万大军打个',
    'pr': 2,
    'rt': 43,
    'ts': 1744343419730,
    'rn': 704,
    'sg': 'b470ff10fb6817747b2761486100e9fcd8d8aae5e49931c9166f001fd438bb84',
    'ct': 1744343419,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',
}
data2 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 5915,
    'sm': '这一仗打得天昏地暗，日月无光，双方足足打',
    'pr': 2,
    'rt': 52,
    'ts': 1744343513916,
    'rn': 92,
    'sg': '89be7fae9b3f293b822463bc2bd13afee5887f57fcbf75c6c8b300ae6fe8ff63',
    'ct': 1744343513,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',
}
data3 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 6711,
    'sm': '破了战局，也给老朱找好了台阶下。回头老朱',
    'pr': 2,
    'rt': 36,
    'ts': 1744343575599,
    'rn': 698,
    'sg': '15a5dfe04be7d384bb79343a2037d15e97130bc4e0656603f0d526733d230125',
    'ct': 1744343575,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',
}
data4 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 7480,
    'sm': '旁边开过。常遇春并不擅长水战，帮不了宕机',
    'pr': 3,
    'rt': 41,
    'ts': 1744343636384,
    'rn': 710,
    'sg': '23a4ab03a17122250ee18e4f83d68fab5b519fe3ab443eae6b691dc466e212a4',
    'ct': 1744343636,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',
}
data5 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 8315,
    'sm': '壁之战。陈友谅那个时代，\u200b《三国演义》还',
    'pr': 3,
    'rt': 33,
    'ts': 1744343702154,
    'rn': 919,
    'sg': 'a0ca73b446feed5bb512d1eb375acf16d4c6d3989254b3df846124875a942eaf',
    'ct': 1744343702,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',

}
data6 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 9061,
    'sm': '个个都颓了。这么一来，战场形势悄然间发生',
    'pr': 3,
    'rt': 42,
    'ts': 1744343761670,
    'rn': 812,
    'sg': '08baf1b3bb582d108ffc152a28c720a2508ff7bf8e76e7fc1573e3ac198804b4',
    'ct': 1744343761,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',

}
data7 = {
    'appId': 'wb182564874663h1484727348',
    'b': '2ba32d00813ab9142g013a3c',
    'c': 'a87322c014a87ff679a21ea',
    'ci': 4,
    'co': 9850,
    'sm': '忘我工作的老朱感觉莫名其妙，在小艇上一个',
    'pr': 3,
    'rt': 38,
    'ts': 1744343832426,
    'rn': 61,
    'sg': 'b843b3040070324f171b1583e1871257cbde312041927fd0792cb2a1e2a894ea',
    'ct': 1744343832,
    'ps': '813323507a65a6ffg015fcd',
    'pc': '33e321407a65a6ffg01121d',
}


def convert(curl_command):
    """提取bash接口中的headers与cookies
    支持 -H 'Cookie: xxx' 和 -b 'xxx' 两种方式的cookie提取
    """
    # 提取 headers
    headers_temp = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_temp[match[0]] = match[1]

    # 提取 cookies
    cookies = {}
    
    # 从 -H 'Cookie: xxx' 提取
    cookie_header = next((v for k, v in headers_temp.items() 
                         if k.lower() == 'cookie'), '')
    
    # 从 -b 'xxx' 提取
    cookie_b = re.search(r"-b '([^']+)'", curl_command)
    cookie_string = cookie_b.group(1) if cookie_b else cookie_header
    
    # 解析 cookie 字符串
    if cookie_string:
        for cookie in cookie_string.split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies[key.strip()] = value.strip()
    
    # 移除 headers 中的 Cookie/cookie
    headers = {k: v for k, v in headers_temp.items() 
              if k.lower() != 'cookie'}

    return headers, cookies


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
