import requests
import json
from tokens import lostark_token
 
headers = {
    'accept' : 'application/json',
    'authorization' : lostark_token
}
 

# 사용자가 입력한 캐릭터 이름을 기반으로 URL 생성
def create_url(character_name):
    base_url = "https://developer-lostark.game.onstove.com/characters/{}/siblings"
    return base_url.format(character_name)

# 사용자 입력 받기
character_name = input("캐릭터 이름을 입력하세요: ")

# URL 생성
url = create_url(character_name)
 
response = requests.get(url, headers=headers)
jsonObject = response.json()
 
#결과값 표시 (결과값의 내용은 https://developer-lostark.game.onstove.com/usage-guide#http-basic 참조)
print(response)
 
# json 출력 코드
for list in jsonObject :
    print(list.get("ServerName"))
    print(list.get("CharacterName"))
    print(list.get("CharacterClassName"))
    print(list.get("ItemMaxLevel"))
