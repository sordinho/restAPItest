#Created by Davide Sordi in 24/04/2018 at 14.59

import requests

base_url = 'http://localhost:5000'

if __name__ == '__main__':
	#get list of users
	users = requests.get(base_url+'/users').json()
	print(users)

	for user in users:
		userinfo = requests.get(base_url+'/users/'+user['name']).json()
		print(userinfo)

	# add a new user
	new_user = {'name':'LDR', 'firstname':'luigi', 'lastname':'de russis'}
	requests.post(base_url+'/users',json=new_user)

	# get list of users
	users = requests.get(base_url + '/users').json()
	print(users)

	for user in users:
		userinfo = requests.get(base_url + '/users/' + user['name']).json()
		print(userinfo)
