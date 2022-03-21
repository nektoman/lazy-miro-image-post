import requests
import json
url = "https://api.miro.com/v2/boards/uXjVOEBUXOY%3D/images"
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer pk8JgpUGobrZHKfAjpRdAaoVX9s"
}
jdata = {
        "title": "kk.png",
        "position": {
            "x": 100,
            "y": 200,
            "origin": "center"
        },
        "geometry": {
            "width": 100,
            "height": 100,
            "rotation": 0
        }
    }
data = {
    'data': json.dumps(jdata)
}
files = {
    'resource': ('kk.png', open('kk.png', 'rb'), 'image/png'),
}
response = requests.post(url, headers=headers, files=files, json=jdata)
print(response.text)
print(response.request.body)
