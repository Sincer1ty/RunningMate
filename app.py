import time as time1
from jinja2 import Environment, FileSystemLoader
from flask import Flask, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dblearningmate

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

time = time1.strftime('%c', time1.localtime(time1.time()))

@app.route('/')
def login():
   return env.get_template('login.html').render()

@app.route('/make')
def make():
   return env.get_template('create.html').render()

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
            'mood': mood
		}
		print("group : ", group)
		db.groups.insert_one(group)
		print(time)
            
	else:
		name = request.form['topic']
		content = request.form['content']
		start_period = request.form['start_period']
		link = request.form['link']
        
		# location = request.form['location']
	# mood = request.form['content']
	# level = request.form['content']
    
	# leader = request.form['content']
	
		end_period = request.form['end_period']
            
		group2 = {
        	'name' : name,
        	'start_period' : start_period,
        	'content' : content,
        	'link' : link,
        	'end_period' : end_period,
        	# 'on_off' : on_off,
        	# 'location' : location
			
		}

		# group.update(group2)
		# result = group
		print("group : ", group)
		latest_document = db.groups.find_one(sort=[("_id", -1)])
		filter_query = {"_id": latest_document["_id"]}

		db.groups.update_one(filter_query,{"$set" : group2})
		
	# week = request.form['content']

	# print("group2 : ", group2)
	
	# print('result : ', result)
    
    # 2. mongoDB에 데이터 넣기
	
	# print("group2 : ", group2)
    
	return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
