import requests
import re
# from getIpDict import getIpDict


def getRefererUrl():
    ipdict = getIpDict()
    strIp = list(ipdict.keys())[2]
    final = "http://" + strIp + ":" + ipdict[strIp]
    return final

def getIpDict():
    obj = re.compile(r"<tr><td>(?P<ip>.*?)</td><td>(?P<port>.*?)</td><td>(?P<respTime>.*?)</td><td>("
                     r"?P<area>.*?)</td><td>(?P<lasttime>.*?)</td></tr>", re.S)

    url = "https://proxy.seofangfa.com/"
    resp = requests.get(url)
    resp.encoding = re.search(r'charset="(?P<charset>.*?)"', resp.text).group("charset")
    # print(resp.text)
    trs = obj.finditer(resp.text)
    iplist = list()
    ipdict = dict()  # 声明一个空字典
    for tr in trs:
        # print(tr.groups())
        # print(tr.groups()[0]) # 拿到所有的代理服务器ip
        # iplist.append(tr.groups()[0])
        ipdict[tr.group("ip")] = tr.group("port")
    # print(iplist)
    resp.close()
    # return iplist
    return ipdict
