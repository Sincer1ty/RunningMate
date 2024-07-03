from jinja2 import Environment, FileSystemLoader
from flask import Flask,request,redirect, url_for
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.db
app = Flask(__name__)

# 템플릿 디렉토리를 설정합니다.
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


@app.route('/')
def home():
    template = env.get_template('index.html')
    return template.render()

@app.route('/sign_up')
def sign_up():
    template = env.get_template('sign_up.html')
    return template.render()

@app.route('/submit',methods=['POST'])
def submit():
    id = request.form['email']
    pw = request.form['password']
    nickname = request.form['nickname']
    subject = request.form['nickname']
    data = {
    'id': id,
    'pw': pw,
    'nickname':nickname,
    }

    db.userInfo.insert_one(data)
    return redirect(url_for('sign_up'))
if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)




# 템플릿을 렌더링하고 결과를 출력합니다.
# output = template.render(data)
# print(output)