from jinja2 import Environment, FileSystemLoader
from flask import Flask,request,jsonify
from pymongo import MongoClient
import re
client = MongoClient('localhost', 27017)
db = client.db
app = Flask(__name__)

# 템플릿 디렉토리를 설정합니다.
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


@app.route('/login')
def login():
    template = env.get_template('login.html')
    return template.render()

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
    return template.render()


@app.route('/')
def home():
    template = env.get_template('main.html')
    return template.render()

@app.route('/create')
def create():
    template = env.get_template('create.html')
    return template.render()

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
    return template.render()

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
    #매칭페이지 데이터
    locations =["서울","수원","인천","대구","부산","울산","광주","전주","대전","세종","천안","청주","원주","춘천","제주","기타"]
    platforms = ["전체","슬랙","디스코드","zoom","기타"]
    week =["월","화","수","목","금","토","일"]
    levels = ["상","중상","중","중하","하"]
    moods =["몰입하는 분위기","사람들과 친해지는 분위기"]
    db.userInfo.insert_one(data)
    return template.render(moods=moods,levels=levels,week=week,locations=locations,platforms=platforms)
    
    
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)