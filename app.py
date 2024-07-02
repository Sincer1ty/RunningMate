from jinja2 import Environment, FileSystemLoader
from flask import Flask, request, render_template
app = Flask(__name__)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('login.html')

@app.route('/')
def login():
   return render_template('login.html')

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
   


data={

}

output = template.render(data)