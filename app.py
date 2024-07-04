import time as time1
from jinja2 import Environment, FileSystemLoader
from flask import Flask,request,jsonify

from pymongo import MongoClient
import re
client = MongoClient('localhost', 27017)
db = client.dblearningmate
app = Flask(__name__)

# 템플릿 디렉토리를 설정합니다.
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

time = time1.strftime('%c', time1.localtime(time1.time()))

# @app.route('/login')
# def login():
#     template = env.get_template('login.html')
#     return template.render()

@app.route('/matching')
def matching():
    template = env.get_template('matching.html')
    locations =["서울","수원","인천","대구","부산","울산","광주","전주","대전","세종","천안","청주","원주","춘천","제주","기타"]
    platforms = ["전체","슬랙","디스코드","zoom","기타"]
    week =["월","화","수","목","금","토","일"]
    levels = ["상","중상","중","중하","하"]
    moods =["몰입하는 분위기","사람들과 친해지는 분위기"]
    return template.render(moods=moods,levels=levels,week=week,locations=locations,platforms=platforms)

@app.route('/matching_result')
def matching_result():
    template = env.get_template('matching_result.html')

    UserSubject = UserData0["subject"] # 유저데이터로 탐색

    temp = subjectMatcher(StudyDB, UserSubject)
   
    if not temp:
       Matcher(StudyDB, UserData0)
    else:
       ans = Matcher(temp, UserData0)

    return template.render(ans)



@app.route('/')
def login():
   return env.get_template('login.html').render()

@app.route('/make')
def make():
   week =["월","화","수","목","금","토","일"]
   return env.get_template('create.html').render(week=week)


@app.route('/make', methods = ['POST'])
def make_groups():
    #  1. 클라이언트로부터 데이터를 받기
    mode = request.form['mode']
    
    print(mode)
    
    group={}
    group2={}
    
    if mode =='ajax':
        subject1 = request.form['keyword1']
        subject2 = request.form['keyword2']
        subject3 = request.form['keyword3']
        
        subject = [subject1, subject2, subject3]
        
        week1 = request.form['week1']
        week2 = request.form['week2']
        week3 = request.form['week3']
        # week4 = request.form['week4']
        # week5 = request.form['week5']
        # week6 = request.form['week6']
        # week7 = request.form['week7']
        
        week = [week1, week2, week3]
        
        on_off = request.form['on_off_give']
        location = request.form['location_give']
        level = request.form['level']
        mood = request.form['mood']

        group = {
            'subject' : subject,
            'time' : time,
            'on_off':on_off,
            'loc': location,
            'level': level,
            'mood': mood,
            'week': week
		}
        print("group : ", group)
        db.groups.insert_one(group)
        print(time)

    else:
        name = request.form['topic']
        content = request.form['content']
        start_period = request.form['start_period']
        link = request.form['link']
   
        end_period = request.form['end_period']
            
        group2 = {
        	'name' : name,
        	'start_period' : start_period,
        	'content' : content,
        	'link' : link,
        	'end_period' : end_period,

		}


        print("group : ", group)
        latest_document = db.groups.find_one(sort=[("_id", -1)])
        filter_query = {"_id": latest_document["_id"]}

        db.groups.update_one(filter_query,{"$set" : group2})
	
    return main()

@app.route('/MyStudy')
def MyStudy():
    template = env.get_template('MyStudy.html')
    return template.render()

@app.route('/edit')
def edit():
    template = env.get_template('edit.html')
    return template.render()

@app.route('/change_profile')
def change_profile():
    template = env.get_template('change_profile.html')
    # id=db.userInfo.find_one()
    return template.render(id='www.gmail.com')

@app.route('/check_pw')
def chaeck_pw():
    template = env.get_template('check_pw.html')
    return template.render()

@app.route('/change_pw')
def change_pw():
    template = env.get_template('change_pw.html')
    return template.render()

@app.route('/find_pw')
def find_pw():
    template = env.get_template('find_pw.html')
    return template.render()


@app.route('/sign_up', methods=['GET'])
def sign_up():
    template = env.get_template('sign_up.html')

    return template.render()
#아이디중복체크
@app.route('/idCheck',methods=['POST'])
def  IdCheck():
     id = request.form['currentID']
     if id =="":
        return '이메일을 입력해주세요.'
     email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
     if not re.match(email_pattern, id):
        return '유효하지 않은 이메일 형식입니다.'
     result = db.userInfo.find_one({"id": id}, {'_id': 0})
     if result:
        return "이 아이디는 이미 사용중입니다."
     else:
        return "이 아이디는 사용이 가능합니다."


@app.route('/nickCheck',methods=['POST'])
def  NickCheck():
     nickName = request.form['currentNickname']
     if nickName =="":
        return '닉네임을 입력해주세요.'
     result = db.userInfo.find_one({"nickname": nickName}, {'_id': 0})
     if result:
        return "이 닉네임은 이미 사용중입니다."
     else:
        return "이 닉네임은 사용이 가능합니다."



@app.route('/submit',methods=['POST'])
def submit():
    template = env.get_template('login.html')
    id = request.form['email']
    pw = request.form['password']
    nickname = request.form['nickname']
    data = {
    'id': id,
    'pw': pw,
    'nickname':nickname,
    }
    email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    
    result = db.userInfo.find_one({"id": id}, {'_id': 0})

    if id !="" and re.match(email_pattern, id) and not result:
        print('not null and match')
        db.userInfo.insert_one(data)
    else : 
        template = env.get_template('sign_up.html')

    #매칭페이지 데이터
    locations =["서울","수원","인천","대구","부산","울산","광주","전주","대전","세종","천안","청주","원주","춘천","제주","기타"]
    platforms = ["전체","슬랙","디스코드","zoom","기타"]
    week =["월","화","수","목","금","토","일"]
    levels = ["상","중상","중","중하","하"]
    moods =["몰입하는 분위기","사람들과 친해지는 분위기"]
    
    return template.render(moods=moods,levels=levels,week=week,locations=locations,platforms=platforms)
    
    


from jinja2 import Environment, FileSystemLoader
from flask import Flask, request, jsonify
from datetime import datetime
import smtplib  # SMTP 사용을 위한 모듈
import re  # Regular Expression을 활용하기 위한 모듈
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.image import MIMEImage  # 메일의 이미지 파일을 base64 형식으로 변환하기 위한 모듈
from flask_jwt_extended import *


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
    "week": "Wednesday"
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
    "week": "Wednesday"
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
    "week": "Wednesday"
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
    "week": "Wednesday"
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
    "week": "Wednesday"
}

StudyData5 = {
    "name": "컴퓨터 구조 공부 합시다[인천]",
    "content": "필독!! 1. 컴퓨터 구조 개요 \n2. 심화 과정",
    "period": "2024-07-15",
    "link": "www.nate.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "경기",
    "mood": "True",
    "level": "중상",
    "leader": "user5",
    "time": "2024.07.03 12:00:00",
    "week": "Wednesday"
}

StudyData16 = {
    "name": "컴퓨터 구조 공부 합시다[서울]",
    "content": "필독!! 1. 컴퓨터 구조 개요 \n2. 심화 과정",
    "period": "2024-07-18",
    "link": "www.studygroup1.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "서울",
    "mood": "True",
    "level": "중상",
    "leader": "user1",
    "time": "2024.07.03 13:00:00",
    "week": "Monday"
}

StudyData17 = {
    "name": "알고리즘 심화학습[부산]",
    "content": "필독!! 1. 알고리즘 기초 \n2. 고급 알고리즘",
    "period": "2024-07-20",
    "link": "www.studygroup2.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "부산",
    "mood": "True",
    "level": "상",
    "leader": "user2",
    "time": "2024.07.03 14:00:00",
    "week": "Tuesday"
}

StudyData18 = {
    "name": "프로그래밍 기초 배우기[대구]",
    "content": "필독!! 1. 프로그래밍 입문 \n2. 기본 문법",
    "period": "2024-07-22",
    "link": "www.studygroup3.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "대구",
    "mood": "False",
    "level": "하",
    "leader": "user3",
    "time": "2024.07.03 15:00:00",
    "week": "Wednesday"
}

StudyData19 = {
    "name": "데이터베이스 기본[광주]",
    "content": "필독!! 1. 데이터베이스 개념 \n2. SQL",
    "period": "2024-07-25",
    "link": "www.studygroup4.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "광주",
    "mood": "True",
    "level": "중",
    "leader": "user4",
    "time": "2024.07.03 16:00:00",
    "week": "Thursday"
}

StudyData20 = {
    "name": "네트워크 기초 이해[인천]",
    "content": "필독!! 1. 네트워크 기본 \n2. OSI 모델",
    "period": "2024-07-27",
    "link": "www.studygroup5.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "인천",
    "mood": "False",
    "level": "하",
    "leader": "user5",
    "time": "2024.07.03 17:00:00",
    "week": "Friday"
}

StudyData6 = {
    "name": "운영체제 심화학습[대전]",
    "content": "필독!! 1. 운영체제 기초 \n2. 심화 과정",
    "period": "2024-07-29",
    "link": "www.studygroup6.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "경기",
    "mood": "True",
    "level": "상",
    "leader": "user6",
    "time": "2024.07.03 18:00:00",
    "week": "Saturday"
}

StudyData7 = {
    "name": "자료구조와 알고리즘[울산]",
    "content": "필독!! 1. 자료구조 개념 \n2. 알고리즘 기초",
    "period": "2024-08-01",
    "link": "www.studygroup7.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "울산",
    "mood": "False",
    "level": "중",
    "leader": "user7",
    "time": "2024.07.03 19:00:00",
    "week": "Sunday"
}

StudyData8 = {
    "name": "컴퓨터 아키텍처 심화[수원]",
    "content": "필독!! 1. 아키텍처 개념 \n2. 고급 아키텍처",
    "period": "2024-08-03",
    "link": "www.studygroup8.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "수원",
    "mood": "True",
    "level": "상",
    "leader": "user8",
    "time": "2024.07.03 20:00:00",
    "week": "Monday"
}

StudyData9 = {
    "name": "웹 개발 입문[성남]",
    "content": "필독!! 1. HTML/CSS \n2. JavaScript 기초",
    "period": "2024-08-05",
    "link": "www.studygroup9.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "경기",
    "mood": "False",
    "level": "하",
    "leader": "user9",
    "time": "2024.07.03 21:00:00",
    "week": "Tuesday"
}

StudyData10 = {
    "name": "모바일 앱 개발[안양]",
    "content": "필독!! 1. 안드로이드 개발 \n2. iOS 개발",
    "period": "2024-08-07",
    "link": "www.studygroup10.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "경기",
    "mood": "True",
    "level": "중",
    "leader": "user10",
    "time": "2024.07.03 22:00:00",
    "week": "Wednesday"
}

StudyData11 = {
    "name": "머신러닝 입문[천안]",
    "content": "필독!! 1. 머신러닝 기초 \n2. 알고리즘",
    "period": "2024-08-09",
    "link": "www.studygroup11.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "천안",
    "mood": "False",
    "level": "하",
    "leader": "user11",
    "time": "2024.07.03 23:00:00",
    "week": "Thursday"
}

StudyData12 = {
    "name": "딥러닝 심화학습[청주]",
    "content": "필독!! 1. 딥러닝 기초 \n2. 고급 과정",
    "period": "2024-08-11",
    "link": "www.studygroup12.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "청주",
    "mood": "True",
    "level": "상",
    "leader": "user12",
    "time": "2024.07.03 10:00:00",
    "week": "Friday"
}

StudyData13 = {
    "name": "빅데이터 분석[전주]",
    "content": "필독!! 1. 빅데이터 개념 \n2. 데이터 분석",
    "period": "2024-08-13",
    "link": "www.studygroup13.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "전주",
    "mood": "False",
    "level": "중",
    "leader": "user13",
    "time": "2024.07.03 11:00:00",
    "week": "Saturday"
}

StudyData14 = {
    "name": "인공지능 기본 개념[세종]",
    "content": "필독!! 1. 인공지능 개요 \n2. 기본 알고리즘",
    "period": "2024-08-15",
    "link": "www.studygroup14.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "세종",
    "mood": "True",
    "level": "하",
    "leader": "user14",
    "time": "2024.07.03 12:00:00",
    "week": "Sunday"
}

StudyData15 = {
    "name": "클라우드 컴퓨팅[제주]",
    "content": "필독!! 1. 클라우드 개념 \n2. 실습",
    "period": "2024-08-17",
    "link": "www.studygroup15.com",
    "subject": "알고리즘",
    "on_off": "False",
    "location": "제주",
    "mood": "False",
    "level": "중",
    "leader": "user15",
    "time": "2024.07.03 13:00:00",
    "week": "Monday"
}

StudyData16 = {
    "name": "IoT 기초 배우기[원주]",
    "content": "필독!! 1. IoT 개요 \n2. 기초 실습",
    "period": "2024-08-19",
    "link": "www.studygroup16.com",
    "subject": "알고리즘",
    "on_off": "True",
    "location": "원주",
    "mood": "True",
    "level": "하",
    "leader": "user16",
    "time": "2024.07.03 14:00:00",
    "week": "Tuesday"
}


UserDB = [UserData0] # 로그인 데이터 위치!!!
groups_collection = db.groups
groups = groups_collection.find()
StudyDB = []
for group in groups:
    StudyDB.append(group)
    
StudyDB = [StudyData0, StudyData1, StudyData2, StudyData3, StudyData4, StudyData5, StudyData6, StudyData7, StudyData8, StudyData9, StudyData10, StudyData11, StudyData12, StudyData13, StudyData14, StudyData15, StudyData16, StudyData17, StudyData18, StudyData19, StudyData20]
print(StudyDB)
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
    print("시간")
    return sorted(study_list, key=lambda x: datetime.strptime(x[time_key], '%Y.%m.%d %H:%M:%S'))

def locdef(location, Userdata): # 장소, 난이도
    print("장소-난이도")
    locans=[]
    level=["하", "중하", "중", "중상", "상"]
    for i in location:
        if i["level"] == Userdata["level"]:
            locans.append(i)
        elif level.index(i["level"])+1 == level.index(Userdata["level"])+1 or level.index(i["level"])-1 == level.index(Userdata["level"])-1:
            locans.append(i)

        if len(locans) ==7:
            return locans
        
    return locans

def weekdef(week, Userdata): # 요일, 러프장소
    print("요일-러프한장소")
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
    print("메인함수")
    ans = []
    on_off = []
    loc = []
    week = []

    for i in List:

        if i["location"] == Userdata["location"]:
            loc.append(i)
            
        elif i["on_off"] == Userdata["on_off"]:
            if len(on_off) != 7:
               on_off.append(i)

        elif i["week"] == Userdata["week"]:
            week.append(i)

        locans = locdef(loc, Userdata)

        weekans = weekdef(week, Userdata)
        print(weekans)

    on_off = sort_by_time(on_off, 'time')
    locans = sort_by_time(locans, 'time')
    weekans = sort_by_time(weekans, 'time')
    
    ans = {"on_off" : on_off, "location": loc, "week":week, "User":Userdata}

    return ans



# ============================================================


@app.route('/main')
def main():

   # 템플릿 파일을 로드합니다.

    template = env.get_template('main.html')

   # 템플릿에 전달할 데이터를 정의합니다.

    UserSubject = UserData0["subject"] # 유저데이터로 탐색

    temp = subjectMatcher(StudyDB, UserSubject)

   
    if not temp:
       Matcher(StudyDB, UserData0)
    else:
       ans = Matcher(temp, UserData0)

    return template.render(ans)


# ============================================================

@app.route('/find')
def findPw():
   template = env.get_template('find_pw.html')
   return template.render()

@app.route('/mail', methods=['POST'])
def mail():

   response = request.form['email']
   print(response)
   # 템플릿 파일을 로드합니다.
   template = env.get_template('login.html')

   # 템플릿에 전달할 데이터를 정의합니다.
   def sendEmail(addr):
      reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 유효성 검사를 위한 정규표현식
      if re.match(reg, addr):
         smtp.sendmail(my_account, to_mail, msg.as_string())
         print("정상적으로 메일이 발송되었습니다.")
      else:
         print("받으실 메일 주소를 정확히 입력하십시오.")
 
      # smpt 서버와 연결
   gmail_smtp = "smtp.gmail.com"  # gmail smtp 주소
   gmail_port = 465  # gmail smtp 포트번호. 고정(변경 불가)
   smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
      
   # 로그인
   my_account = "dlstjd222"
   my_password = "qsknpkpolvgwymgt"
   smtp.login(my_account, my_password)
      
      # 메일을 받을 계정
   to_mail = response

      # 메일 기본 정보 설정
   msg = MIMEMultipart()
   msg["Subject"] = f"러닝메이트 인증 메일입니다."  # 메일 제목
   msg["From"] = my_account
   msg["To"] = to_mail
      
   # 메일 본문 내용
   content = "안녕하세요. \n\n\
   링크를 전달드립니다.\n\n\
   http://192.168.1.131:5000/change \n\n\
   감사합니다\n\n\
   "
   content_part = MIMEText(content, "plain")
   msg.attach(content_part)
      
   # 이미지 파일 추가
   # image_name = "test.png"
   # with open(image_name, 'rb') as file:
   #     img = MIMEImage(file.read())
   #     img.add_header('Content-Disposition', 'attachment', filename=image_name)
   #     msg.attach(img)
      
      # 받는 메일 유효성 검사 거친 후 메일 전송
   sendEmail(to_mail)
      
   # smtp 서버 연결 해제
   smtp.quit()

   return template.render()


# ============================================================

app.config.update(
			DEBUG = True,
			JWT_SECRET_KEY = "I'M IML"
		)
jwt = JWTManager(app)

@app.route('/change')
def change():
    template = env.get_template('change_pw.html')
    return template.render()

@app.route('/jwt', methods=['POST'])
def jmt():
   user_id = request.form['email']
   user_pw = request.form['password']

   result = db.userInfo.find_one({"id":user_id},{'_id':0})

   print(result)
   if user_pw==result['pw']:
       access_token = create_access_token(identity = user_id,
											expires_delta = False)

   else:
      return jsonify(
			result = "Invalid Params!"
		)
       

   # 템플릿 파일을 로드합니다.
   template = env.get_template('main.html')
   # 템플릿에 전달할 데이터를 정의합니다.

   UserSubject = UserData0["subject"] # 유저데이터로 탐색

   temp = subjectMatcher(StudyDB, UserSubject)

   ans = Matcher(temp, UserData0)

   return template.render(ans)

@app.route('/classified')
@jwt_required()
def classified():

   cur_user = get_jwt_identity()
   if cur_user is None:
      return "User Only!"
   else:
      return "Hi!," + cur_user




# ============================================================
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)





# 템플릿을 렌더링하고 결과를 출력합니다.
# output = template.render(data)
# print(output)