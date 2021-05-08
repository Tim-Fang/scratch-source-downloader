import requests
import json
import zipfile
import os
import time

httpSession = requests.session()


def downloadJson(jsonUrl, projectName, assetCdn, soundCdn):
    f_out = open(projectName + '.sb3', 'w')
    f_out.close()
    f_out = zipfile.ZipFile(projecName + '.sb3', 'w')
    projectJson = httpSession.get(url=jsonUrl).text
    f_out.writestr('project.json', data=projectJson, compress_type=8)
    projectJson.json.loads(projectJson)['tagets']
    projectCostumeMd5List = []
    projectSoundMd5List = []
    for eachCostume in projectJson:
        for eachMd5 in eachCostume['costumes']:
            projectCostumeMd5List.append(eachMd5['md5ext'])
    for eachSound in projectJson:
        for eachMd5 in eachSound:
            projectSoundMd5List.append(eachMd5['md5ext'])
    projectCostumeMd5List = list(set(projectCostumeMd5List))
    projectSoundMd5List = list(set(projectSoundMd5List))

