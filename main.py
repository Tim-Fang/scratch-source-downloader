# Scratch Source Downloader V0.1
# By TimFang4162
# Warning:
#    only for learning and communication
#    Please do not use for illegal purposes
#    All consequences are at your own risk
# How to use:
#    Double click to run this program
#    Please do not open in IDLE
import json
import zipfile
import requests
import os
import time

CommunityList = [
    "aerfaying.com", "kada.163.com", "world.xiaomawang.com", "scratch-cn.cn",
    "scratch.mit.edu"
]

AssetCdnList = ["", "https://steam.nosdn.127.net/", "", "", "", "", "", ""]

CommunityNameList = ["阿儿法营", "有道卡搭", "小码王", "ScratchCN", "MIT"]

httpsession = requests.session()
project_url = input("Project url: ")
starttime = time.time()
# Get commuinty
temp = 0
Community = -1
for Communitys in CommunityList:
    if (project_url.find(Communitys) != -1):
        print("Community:", CommunityNameList[temp])
        Community = temp
    temp += 1
# commuinty error
if (Community == -1):
    print("Url Error")
    os.system("pause")
    os._exit(0)
# community:aerfaying
if (Community == 0):
    os.system("aerfa --clone " + project_url)
    print("Time:", starttime - time.time() + "s")
# commuinty:kada
elif (Community == 1):
    project_htm = httpsession.get(url=project_url)
    project_name = project_htm.text[project_htm.text.find('<title>') +
                                    7:project_htm.text.find('网易有道卡搭</title>')]
    temp = project_htm.text.find('"projectUrl": "\//steam.nosdn.127.net/')
    print("Project name:", project_name)
    if (project_htm.text[temp + 33 + 38:temp + 37 + 38] == "json"):
        print("Project json:", project_htm.text[temp + 38:temp + 37 + 38])
        print("Project version: 3.0")
        f_out = open(project_name + ".sb3", "w")
        f_out.close()
        f_out = zipfile.ZipFile(project_name + ".sb3", "w")
        project_json = httpsession.get(
            url="https://steam.nosdn.127.net/" +
            project_htm.text[temp + 38:temp + 37 + 38]).text
        f_out.writestr("project.json", data=project_json, compress_type=8)
        project_json = json.loads(project_json)['targets']
        project_md5_list = []
        for project_costume in project_json:
            for project_costume_md5 in project_costume['costumes']:
                project_md5_list.append(project_costume_md5['md5ext'])
        for project_sound in project_json:
            for project_sound_md5 in project_sound['sounds']:
                project_md5_list.append(project_sound_md5['md5ext'])
        project_md5_list = list(set(project_md5_list))
        md5num = 1
        for md5 in project_md5_list:
            print("Downloading: ",
                  md5,
                  " (",
                  md5num,
                  "/",
                  len(project_md5_list),
                  ")",
                  sep="")
            f_out.writestr(
                md5,
                data=httpsession.get("https://steam.nosdn.127.net/" +
                                     md5).content,
                compress_type=8)
            md5num = md5num + 1
        f_out.close()
        print("Download completed!", "\nFile saved in:",
              os.getcwd() + "\\" + project_name + ".sb3 ")
        print("Time:", str(time.time() - starttime) + "s")
    else:
        '''
        print(
            "Ooooooooops!\nScratch 2.0 Projects are not supported")
        os.system("pause")
        os._exit(0)
        '''

        # Scratch 2.0 DEMO
        # Bug Bug Bug
        # Do not run this

        print("Project json:", project_htm.text[temp + 38:temp + 37 + 37])
        print("Project version: 2.0")
        f_out = open(project_name + ".sb2", "wb")
        f_out.write(
            requests.get(url="https://steam.nosdn.127.net/" +
                         project_htm.text[temp + 38:temp + 37 + 37]).content)
        f_out.close()
        '''
        f_out = zipfile.ZipFile(project_name + ".sb2", "a")
        project_json = json.loads(f_out.read(f_out.namelist()[0]).decode())
        project_md5_list = []
        if ('sounds' in project_json):
            for project_sound in project_json['sounds']:
                project_md5_list.append(project_sound['md5'])
        if ('costumes' in project_json):
            for project_costume in project_json['costumes']:
                project_md5_list.append(project_costume['baseLayerMD5'])
        project_json = project_json['children']
        for project_costume in project_json:
            if ('costumes' in project_json):
                for project_costume_md5 in project_costume['costumes']:
                    project_md5_list.append(
                        project_costume_md5['baseLayerMD5'])
        for project_sound in project_json:
            if ('sounds' in project_json):
                for project_sound_md5 in project_sound['sounds']:
                    project_md5_list.append(project_sound_md5['md5'])
        project_md5_list = list(set(project_md5_list))
        md5num = 1
        for md5 in project_md5_list:
            print("Downloading: ", md5, " (", md5num,
                  "/", len(project_md5_list), ")", sep="")
            f_out.writestr(md5, data=httpsession.get(
                "https://steam.nosdn.127.net/"+md5).content)
            md5num = md5num + 1
        f_out.close()
        '''
        print("Download completed!", "\nFile saved in:",
              os.getcwd() + "\\" + project_name + ".sb2 ")
        print("Time:", str(time.time() - starttime) + "s")
        print(
            "Warning: This file is incomplete",
            "\nPlease open this file in kada editor to complete the missing file"
        )
# community:xiaomawang
elif (Community == 2):
    project_htm = httpsession.get(url=project_url)
    project_name = project_htm.text[project_htm.text.find('"title":') +
                                    9:project_htm.text.find('"description":') -
                                    2]
    print("Project name:", project_name)
    temp1 = project_htm.text.find('"fileKey":"')
    temp2 = project_htm.text.find('.sb3",')
    # project_htm.text[temp1+11:temp2+4]
    print("Project json:", project_htm.text[temp1 + 62:temp2 + 4])
    print("Project version: 3.0")
    f_out = open(project_name + ".sb3", "w")
    f_out.close()
    f_out = zipfile.ZipFile(project_name + ".sb3", "w")
    header = {
        "Accept":
        "*/*",
        "Accept-Encoding":
        "gzip, deflate, br",
        "Accept-Language":
        "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Cache-Control":
        "max-age=0",
        "Connection":
        "keep-alive",
        "Host":
        "community-wscdn.xiaomawang.com",
        "Origin":
        "https://world.xiaomawang.com",
        "Referer":
        project_url,
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36/8mqQhSuL-09"
    }
    project_json = httpsession.get(url=project_htm.text[temp1 + 11:temp2 + 4],
                                   headers=header).text
    f_out.writestr("project.json", data=project_json, compress_type=8)
    project_json = json.loads(project_json)['targets']
    project_md5_list = []
    for project_costume in project_json:
        for project_costume_md5 in project_costume['costumes']:
            project_md5_list.append(project_costume_md5['md5ext'])
    for project_sound in project_json:
        for project_sound_md5 in project_sound['sounds']:
            project_md5_list.append(project_sound_md5['md5ext'])
    project_md5_list = list(set(project_md5_list))
    md5num = 1
    for md5 in project_md5_list:
        print("Downloading: ",
              md5,
              " (",
              md5num,
              "/",
              len(project_md5_list),
              ")",
              sep="")
        if (md5[-3:] == "png" or md5[-3:] == "jpg"):
            f_out.writestr(
                md5,
                data=httpsession.get(
                    "https://community-wscdn.xiaomawang.com/picture/" +
                    md5).content,
                compress_type=8)
        if (md5[-3:] == "wav" or md5[-3:] == "mp3"):
            f_out.writestr(
                md5,
                data=httpsession.get(
                    "https://community-wscdn.xiaomawang.com/audio/" +
                    md5).content,
                compress_type=8)
        md5num = md5num + 1
    f_out.close()
    print("Download completed!", "\nFile saved in:",
          os.getcwd() + "\\" + project_name + ".sb3 ")
    print("Time:", str(time.time() - starttime) + "s")
# commuinty:scratch cn
elif (Community == 3):
    project_htm = httpsession.get(url=project_url)
    project_name = project_htm.text[project_htm.text.
                                    find('<div class="work-title">') +
                                    43:project_htm.text.find('</h3>') - 15]
    print("Project name:", project_name)
    temp1 = project_htm.text.find('<input type="hidden" id="_s_" value="')
    temp2 = project_htm.text.find('<div class="f-l">')
    print("Project json:", project_htm.text[temp1 + 37:temp2 - 9] + ".json")
    f_out = open(project_name + ".sb3", "w")
    f_out.close()
    f_out = zipfile.ZipFile(project_name + ".sb3", "w")
    project_json = httpsession.get(
        url="https://www.scratch-cn.cn/userfile/scratch/" +
        project_htm.text[temp1 + 37:temp2 - 9]).text
    f_out.writestr("project.json", data=project_json, compress_type=8)
    project_json = json.loads(project_json)['targets']
    project_md5_list = []
    for project_costume in project_json:
        for project_costume_md5 in project_costume['costumes']:
            project_md5_list.append(project_costume_md5['md5ext'])
    for project_sound in project_json:
        for project_sound_md5 in project_sound['sounds']:
            project_md5_list.append(project_sound_md5['md5ext'])
    project_md5_list = list(set(project_md5_list))
    md5num = 1
    for md5 in project_md5_list:
        print("Downloading: ",
              md5,
              " (",
              md5num,
              "/",
              len(project_md5_list),
              ")",
              sep="")
        if (md5[-3:] == "png" or md5[-3:] == "jpg"):
            f_out.writestr(
                md5,
                data=httpsession.get(
                    "https://nicecode.oss-cn-hangzhou.aliyuncs.com/scratch/00a6ad64232a90b4f6f5cc859b9d7f53/"
                    + md5).content,
                compress_type=8)
        if (md5[-3:] == "wav" or md5[-3:] == "mp3"):
            f_out.writestr(
                md5,
                data=httpsession.get(
                    "https://nicecode.oss-cn-hangzhou.aliyuncs.com/scratch/00a6ad64232a90b4f6f5cc859b9d7f53/"
                    + md5).content,
                compress_type=8)
        md5num = md5num + 1
    f_out.close()
    print("Download completed!", "\nFile saved in:",
          os.getcwd() + "\\" + project_name + ".sb3 ")
    print("Time:", str(time.time() - starttime) + "s")
# commuinty:MIT
elif (Community == 4):
    #port=input("Your proxy port?")
    port = str(10809)
    proxies = {'http': "localhost:10809", 'https': "localhost:10809"}
    project_url = project_url.replace("scratch.mit.edu", "api.scratch.mit.edu")
    project_htm = json.loads(
        httpsession.get(url=project_url, proxies=proxies).text)
    project_name = project_htm['title']
    print("Project name:", project_name)
    print("Project version: 3.0")
    f_out = open(project_name + ".sb3", "w")
    f_out.close()
    f_out = zipfile.ZipFile(project_name + ".sb3", "w")
    project_json = httpsession.get(url="https://projects.scratch.mit.edu/" +
                                   project_htm['id'],
                                   proxies=proxies).text
    f_out.writestr("project.json", data=project_json, compress_type=8)
    project_json = json.loads(project_json)['targets']
    project_md5_list = []
    for project_costume in project_json:
        for project_costume_md5 in project_costume['costumes']:
            project_md5_list.append(project_costume_md5['md5ext'])
    for project_sound in project_json:
        for project_sound_md5 in project_sound['sounds']:
            project_md5_list.append(project_sound_md5['md5ext'])
    project_md5_list = list(set(project_md5_list))
    md5num = 1
    for md5 in project_md5_list:
        print("Downloading: ",
              md5,
              " (",
              md5num,
              "/",
              len(project_md5_list),
              ")",
              sep="")
        f_out.writestr(
            md5,
            data=httpsession.get(
                "https://assets.scratch.mit.edu/internalapi/asset/" + md5 +
                "/get",
                proxies=proxies).content,
            compress_type=8)
        md5num = md5num + 1
    f_out.close()
    print("Download completed!", "\nFile saved in:",
          os.getcwd() + "\\" + project_name + ".sb3 ")
    print("Time:", str(time.time() - starttime) + "s")