from flask import Flask, jsonify, request

app = Flask(__name__)

user1 = {'name': 'DS', 'firstname': 'davide', 'lastname': 'sordi'}  # name is used as identifier
user2 = {'name': 'FC', 'firstname': 'fulvio', 'lastname': 'corno'}

users = [user1, user2]

"""
Resource = user -> /user/DS -> Get (GET) (Not implemented put and updated)
Collection = users -> /users -> List (GET) , Create (POST)
"""


@app.route('/users')
def listUsers():
	# get the list of obj in a python variable
	# usernames = [user['name'] for user in users]  # a list composed by the names of the users (ez)
	usernames = [{'name': user['name']} for user in users]  # a list composed by the names of the users (ez)
	return jsonify(usernames)


@app.route('/users/<name>')
def getUsers(name):
	# return user info given the ID
	user = [user for user in users if user['name'] == name]
	if len(user) == 1:
		return jsonify(user)
	else:
		response = jsonify({'message': 'user not found: ' + name})
		response.status_code = 404
		return response

@app.route('/users',methods=['POST'])
def createUsers():
	new_user = request.json
	# new user is representing a user
	# new user['name'] should not already be in DB
	users.append(new_user)
	return jsonify(new_user)





@app.route('/')
def hello_world():
	return 'Hello World!'


if __name__ == '__main__':
	app.run()
