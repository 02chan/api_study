import requests
import json
from tokens import lostark_token

headers = {
    'accept': 'application/json',
    'authorization': lostark_token
}

# 사용자가 입력한 캐릭터 이름을 기반으로 URL 생성
def create_url(character_name):
    base_url = "https://developer-lostark.game.onstove.com/armories/characters/{}/profiles"
    return base_url.format(character_name)

# 사용자 입력 받기
character_name = input("캐릭터 이름을 입력하세요: ")

# URL 생성
url = create_url(character_name)

# API 요청 보내기
response = requests.get(url, headers=headers)

# 응답 상태 코드 확인
if response.status_code == 200:
    # JSON 응답 파싱
    jsonObject = response.json()

    # 결과값 표시
    print("Server Name:", jsonObject.get("ServerName"))
    print("Character Name:", jsonObject.get("CharacterName"))
    print("Character Class Name:", jsonObject.get("CharacterClassName"))
    print("Item Max Level:", jsonObject.get("ItemMaxLevel"))
    print("Character Image URL:", jsonObject.get("CharacterImage"))
else:
    print("Error:", response.status_code, response.text)