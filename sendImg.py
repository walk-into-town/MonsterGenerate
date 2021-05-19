
def sendImg():
    import json
    import os
    import requests
    from time import sleep

    from collections import OrderedDict
    # imagefolder에 있는 모든 사진들 1개씩 put으로 보내기
    file_data = OrderedDict()
    #폴더에서 png 파일 하나씩 불러와서 이름 입력해 줘야함;;
    print(os.listdir('imagefolder'))
    file_path = './imagefolder/'
    pnglist = os.listdir('imagefolder')
    nameNum=0
    url_items = "https://walk-into-town.kro.kr/game/monster/img"

    for png in pnglist:
        file_data["number"] = nameNum
        name=str(nameNum)+'.png'
        #print(name)
        files ={'img':(name, open(file_path+png,'rb').read(),'image/png',{})}
        file_data["img"] = name
        nameNum+=1
        #print(files)
        testjson = json.dumps(file_data,ensure_ascii=False,indent="\t")
        testjson= json.loads(testjson)
        #100ms로 타임아웃 걸기
        response = requests.put(url_items, data=testjson,files=files)
        sleep(0.1)
        

    

