from jinja2 import Environment, FileSystemLoader
from flask import Flask

app = Flask(__name__)

# 템플릿 디렉토리를 설정합니다.
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)



@app.route('/')
def home():

   # 템플릿 파일을 로드합니다.
   template = env.get_template('example.html')

   # 템플릿에 전달할 데이터를 정의합니다.
   data = {
    'title': 'Jinja2 Example',
    'headline': 'Welcome to Jinja2',
    'content': 'This is an example of Jinja2 template rendering.',
    'items': ['item1', 'item2', 'item3'],
    'user': {
        'is_logged_in': True,
        'name': 'John Doe'
        }
    }

   return template.render(data)

@app.route('/mail')
def home():

   # 템플릿 파일을 로드합니다.
   template = env.get_template('example.html')

   # 템플릿에 전달할 데이터를 정의합니다.
   data = {
    'title': 'Jinja2 Example',
    'headline': 'Welcome to Jinja2',
    'content': 'This is an example of Jinja2 template rendering.',
    'items': ['item1', 'item2', 'item3'],
    'user': {
        'is_logged_in': True,
        'name': 'John Doe'
        }
    }

   return template.render(data)




if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)





# 템플릿을 렌더링하고 결과를 출력합니다.
# output = template.render(data)
# print(output)