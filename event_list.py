import requests
import json
from tokens import lostark_token
 
headers = {
    'accept' : 'application/json',
    'authorization' : lostark_token
}
 
 #이벤트 리스트를 받아오는 site
url = 'https://developer-lostark.game.onstove.com/news/events'
 
response = requests.get(url, headers=headers)
jsonObject = response.json()
 
#결과값 표시 (결과값의 내용은 https://developer-lostark.game.onstove.com/usage-guide#http-basic 참조)
#print(response)
 
# json 출력 코드
for list in jsonObject :
    print(list.get("Title"))