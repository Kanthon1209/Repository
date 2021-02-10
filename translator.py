import urllib.request
import urllib.parse
import json
import easygui as g
import time
print("翻译在线")


while True:

    
    info_1 = input("请输入翻译内容:")


    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    data = {}
    data["i"] = info_1
    data["from"]= "AUTO"
    data["to"]=  "AUTO"
    data["smartresult"]=  "dict"
    data["client"]="fanyideskweb"
    data["salt"]=  "16111400139765"
    data["sign"]=  "25cb4c828e28e39d0e070edfa5df237d"
    data["lts"]= "1611140013976"
    data["bv"]=  "02c2dd94fb562b4304f9b0c657990444"
    data["doctype"]=  "json"
    data["version"]=  "2.1"
    data["keyfrom"]=  "fanyi.web"
    data["action"]=  "FY_BY_REALTlME"

    data = urllib.parse.urlencode(data).encode("utf-8")
    response = urllib.request.urlopen(url,data)
    html = response.read().decode("utf-8")
    target = json.loads(html)
    result = target["translateResult"][0][0]["tgt"]
    print("\n")
    print("翻译的结果是:")
    print(result)
    print("\n")
    file = open("vocabulary.txt","a",encoding = "utf-8")
    file.writelines(info_1 + "\n" + result +"\n\n")
    file.close()
