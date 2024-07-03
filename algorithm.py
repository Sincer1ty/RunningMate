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
    "mood": "True",
    "level": "중상",
    "leader": "person",
    "time": "2024.07.01 21:51:01",
    "week": "Monday"
}

StudyData1 = {
    "name": "자료구조 공부 같이하실분[서울]",
    "content": "필독!! 1. 자료구조 기초 \n2. 알고리즘 기본",
    "period": "2024-07-05",
    "link": "www.daum.net",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "서울",
    "mood": "True",
    "level": "중상",
    "leader": "user1",
    "time": "2024.07.02 15:30:00",
    "week": "Sunday"
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
    "time": "2024.07.02 16:00:00",
    "week": "Tuesday"
}

StudyData3 = {
    "name": "네트워크 공부 합시다[대구]",
    "content": "필독!! 1. 네트워크 기초 \n2. 응용",
    "period": "2024-07-07",
    "link": "www.github.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "대구",
    "mood": "True",
    "level": "중상",
    "leader": "user3",
    "time": "2024.07.03 10:00:00",
    "week": "Thursday"
}

StudyData4 = {
    "name": "운영체제 공부 하실분[광주]",
    "content": "필독!! 1. 운영체제 기본 \n2. 고급 과정",
    "period": "2024-07-12",
    "link": "www.reddit.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "광주",
    "mood": "False",
    "level": "중상",
    "leader": "user4",
    "time": "2024.07.01 18:00:00",
    "week": "Friday"
}

StudyData5 = {
    "name": "컴퓨터 구조 공부 합시다[인천]",
    "content": "필독!! 1. 컴퓨터 구조 개요 \n2. 심화 과정",
    "period": "2024-07-15",
    "link": "www.nate.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "인천",
    "mood": "True",
    "level": "중상",
    "leader": "user5",
    "time": "2024.07.03 12:00:00",
    "week": "Saturday"
}

from datetime import datetime

UserDB = [UserData0]
StudyDB = [StudyData0, StudyData1, StudyData2, StudyData3, StudyData4, StudyData5]

#여기까지 데이터 정의

# 과목으로 탐색
def subjectMatcher(List, Subject): 
    ans = []
    for i in List:
        if i["subject"] == Subject:
            ans.append(i)
    
    if ans:
        return ans
    else:
        print("과목 매칭 실패!")
        return False

# 시간순 정렬 함수
def sort_by_time(study_list, time_key):
    return sorted(study_list, key=lambda x: datetime.strptime(x[time_key], '%Y.%m.%d %H:%M:%S'))

def locdef(location, Userdata): # 장소, 난이도
    locans=[]
    level=["하", "중하", "중", "중상", "상"]
    for i in location:
        if i["level"] == Userdata["level"]:
            locans.append(i)
        elif level.index(i["level"])+1 == level.index(Userdata["level"])+1 or level.index(i["level"])-1 == level.index(Userdata["level"])-1:
            locans.append(i)

        
        if len(locans) ==7:
            return locans

    # for i in location:
 
    #     if len(locans) == 7:
    #         return locans
        
    return locans
    # while len(locans)!=7:
        

def ondef(): # 대면/비대면
    1

def weekdef(week, Userdata): # 요일, 러프장소
    weekans=[]
    area=["서울","수원","인천","대구","부산","울산","광주","전주","대전","세종","천안","청주","원주","춘천","제주","기타"]

    for i in week:
        if i["location"] == Userdata["location"]:
            weekans.append(i)
        else:
            if Userdata["location"] == "서울":
                if i["location"] == "수원" or i["location"] == "인천":
                    weekans.append(i)
            elif Userdata["location"] == "수원":
                if i["location"] == "서울" or i["location"] == "인천":
                    weekans.append(i)
            elif Userdata["location"] == "인천":
                if i["location"] == "서울" or i["location"] == "수원":
                    weekans.append(i)
            elif Userdata["location"] == "대전":
                if i["location"] == "세종" or i["location"] == "청주":
                    weekans.append(i)
            elif Userdata["location"] == "세종":
                if i["location"] == "대전" or i["location"] == "청주" or i["location"]=="천안":
                    weekans.append(i)
            elif Userdata["location"] == "청주":
                if i["location"] == "세종" or i["location"] == "대전" or i["location"]=="천안":
                    weekans.append(i)
            elif Userdata["location"] == "천안":
                if i["location"] == "세종" or i["location"] == "청주":
                    weekans.append(i)
        
        if len(weekans) ==7:
            return weekans
    
    for i in week:
        if i not in weekans:
            weekans.append(i)

        if len(weekans) ==7:
            break

    return weekans

# 통합 함수
def Matcher(List, Userdata):
    ans = []
    on_off = []
    location = []
    week = []

    for i in List:

        if i["location"] == Userdata["location"]:
            location.append(i)
            
        elif i["on_off"] == Userdata["on_off"]:
            on_off.append(i)

        elif i["week"] == Userdata["week"]:
            week.append(i)

        locans = locdef(location, Userdata)

        weekans = weekdef(week, Userdata)

    on_off = sort_by_time(on_off, 'time')
    locans = sort_by_time(locans, 'time')
    weekans = sort_by_time(weekans, 'time')

    


    ans.append(on_off)
    ans.append(location)
    ans.append(week)

    return ans


UserSubject = UserData0["subject"] # 유저데이터로 탐색

temp = subjectMatcher(StudyDB, UserSubject)

ans = Matcher(temp, UserData0)

print(ans)

