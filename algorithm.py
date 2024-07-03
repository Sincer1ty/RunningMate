UserData0={
    "id": "admin",
    "pw": "1234",
    "nickname": "관리자",
    "subject": "알고리즘",
    "on_off": "True", # 여기 논의 필요
    "week": "Wednesday",
    "location": "경기",
    "level": "중상",
    "mood": "False" # 여기 논의 필요
}

StudyData0={
    "name": "알고리즘 공부 같이하실분[수원]",
    "content": "필독!! 1. 가나다라 \n2. 마바사 ",
    "start period": "2024-07-03 ~ 2024-07-05", # 여기 논의 필요
    "end": "1515",
    "link": "www.naver.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "경기", # 논의필요
    "mood": "False",
    "level": "중상",
    "leader": "person",
    "time": "2024.07.01 21:51:01"
}

UserData1 = {
    "id": "user1",
    "pw": "abcd",
    "nickname": "참가자1",
    "subject": "알고리즘",
    "on_off": "True",
    "week": "Monday",
    "location": "서울",
    "level": "중상",
    "mood": "True"
}

UserData2 = {
    "id": "user2",
    "pw": "efgh",
    "nickname": "참가자2",
    "subject": "자료구조",
    "on_off": "False",
    "week": "Tuesday",
    "location": "부산",
    "level": "초급",
    "mood": "False"
}

UserData3 = {
    "id": "user3",
    "pw": "ijkl",
    "nickname": "참가자3",
    "subject": "알고리즘",
    "on_off": "True",
    "week": "Wednesday",
    "location": "대구",
    "level": "고급",
    "mood": "True"
}

UserData4 = {
    "id": "user4",
    "pw": "mnop",
    "nickname": "참가자4",
    "subject": "네트워크",
    "on_off": "False",
    "week": "Thursday",
    "location": "광주",
    "level": "중급",
    "mood": "False"
}

UserData5 = {
    "id": "user5",
    "pw": "qrst",
    "nickname": "참가자5",
    "subject": "운영체제",
    "on_off": "True",
    "week": "Friday",
    "location": "인천",
    "level": "중상",
    "mood": "True"
}

StudyData1 = {
    "name": "자료구조 공부 같이하실분[서울]",
    "content": "필독!! 1. 자료구조 기초 \n2. 알고리즘 기본",
    "period": "2024-07-05",
    "link": "www.daum.net",
    "subject": "자료구조",
    "on_off": "False",
    "location": "서울",
    "mood": "True",
    "level": "초급",
    "leader": "user1",
    "time": "2024.07.02 15:30:00"
}

StudyData2 = {
    "name": "알고리즘 스터디[부산]",
    "content": "필독!! 1. 알고리즘 개요 \n2. 문제 풀이",
    "period": "2024-07-10",
    "link": "www.google.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "부산",
    "mood": "False",
    "level": "중상",
    "leader": "user2",
    "time": "2024.07.02 16:00:00"
}

StudyData3 = {
    "name": "네트워크 공부 합시다[대구]",
    "content": "필독!! 1. 네트워크 기초 \n2. 응용",
    "period": "2024-07-07",
    "link": "www.github.com",
    "subject": "네트워크",
    "on_off": "False",
    "location": "대구",
    "mood": "True",
    "level": "중급",
    "leader": "user3",
    "time": "2024.07.03 10:00:00"
}

StudyData4 = {
    "name": "운영체제 공부 하실분[광주]",
    "content": "필독!! 1. 운영체제 기본 \n2. 고급 과정",
    "period": "2024-07-12",
    "link": "www.reddit.com",
    "subject": "운영체제",
    "on_off": "True",
    "location": "광주",
    "mood": "False",
    "level": "중상",
    "leader": "user4",
    "time": "2024.07.01 18:00:00"
}

StudyData5 = {
    "name": "컴퓨터 구조 공부 합시다[인천]",
    "content": "필독!! 1. 컴퓨터 구조 개요 \n2. 심화 과정",
    "period": "2024-07-15",
    "link": "www.nate.com",
    "subject": "컴퓨터 구조",
    "on_off": "True",
    "location": "인천",
    "mood": "True",
    "level": "고급",
    "leader": "user5",
    "time": "2024.07.03 12:00:00"
}

UserDB = [UserData0, UserData1, UserData2, UserData3, UserData4, UserData5]
StudyDB = [StudyData0, StudyData1, StudyData2, StudyData3, StudyData4, StudyData5]


#여기까지 데이터 정의

# 과목으로 탐색
def subjectMatcher(List, Subject): 
    ans = []
    for i in List:
        if i["subject"] == Subject:
            ans.append(i)
    
    if ans != False:
        return ans
    else:
        print("과목 매칭 실패!")
        return False

# 대면/비대면탐색
def on_offMatcher(List, Subject):
    ans = []
    for i in List:
        if i["on_off"] == Subject:
            ans.append(i)
    
    if ans != False:
        return ans
    else:
        print("대면/비대면 매칭 실패!")
        return False
    
# 장소탐색
def locationMatcher(List, Subject):
    ans = []
    for i in List:
        if i["location"] == Subject:
            ans.append(i)
    
    if ans != False:
        return ans
    else:
        print("장소 매칭 실패!")
        return False
    
# 시간탐색
def weekMatcher(List, Subject):
    ans = []
    for i in List:
        if i["week"] == Subject:
            ans.append(i)
    
    if ans != False:
        return ans
    else:
        print("장소 매칭 실패!")
        return False

UserSubject = UserData0["subject"] # 유저데이터로 탐색


temp = subjectMatcher(StudyDB, UserSubject)

on_off = on_offMatcher(temp, UserData0["on_off"])
location = locationMatcher(temp, UserData0["location"])
# week = weekMatcher(temp, UserData0["week"])

print(location)


