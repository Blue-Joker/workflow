import requests
import json

def push(status):
    if status:
        datas = json.dumps({
                        "appToken":"AT_xxx",
                        "content":"十八更新了！",
                        "contentType": 1,
                        "summary":"十八更新了!",
                        "uids":["UID_xxxx"],
                        "url":"https://www.18art.art/html/notices/"
                    })
    else:
        datas = json.dumps({
            "appToken": "AT_u6qkyo9ru57wNmQvZMRKmJPmrjKUXjBi",
            "content": "十八躺了",
            "contentType": 1,
            "summary": "十八躺了",
            "uids": ["UID_UJBFH9mjseILfxLTYa1hcRA0ZuxG"],
            "url": "https://www.18art.art/html/notices/"
        })
    headers = {'Content-Type': 'application/json'}
    r = requests.post("http://wxpusher.zjiecode.com/api/send/message", data=datas,headers=headers)
    print(r.text)
    print(r.status_code)
