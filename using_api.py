import requests
import json
import os
saral_url="http://saral.navgurukul.org/api/courses"
def request_to_api(url):
	if os.path.exists('courses.josn'):
		print("hai")
	else:
		p=requests.get(url)
		a=json.dumps(p.text)
	with open("courses.json","w") as file1:
		file1.write(a)
		file1.close()
	f1=open("courses.json")
	f=f1.read()
	a=json.loads(f)
	b=json.loads(a)
	# f1.close()
	q=b['availableCourses']
	a=1
	for i in range(len(q)):	
		print(str(a)+q[i]['name'])
		a+=1
	w= int(input("which course you want to enroll\n"))
	id_q=(b['availableCourses'][w-1]['id'])
	url1='http://saral.navgurukul.org/api/courses/'+str(id_q)+'/exercises'
	p1=requests.get(url1)
	a1=json.dumps(p1.text)
	with open("courses1.json","w") as file2:
		file2.write(a1)
		file2.close()
	f2=open("courses1.json")
	l=f2.read()
	h=json.loads(l)
	b1=json.loads(h)
	len_data=b1['data']
	c=1
	for x in range(len(len_data)):
		print (str(c)+ b1['data'][x]['name'])
		c+=1
	user=int(input("In which topic you want to enter\n"))	
	slug_id=(b1['data'][user]['slug'])
	url3='http://saral.navgurukul.org/api/courses/'+str(id_q)+('/exercise/getBySlug?slug=')+str(slug_id)
	#print(url3)
	p2=requests.get(url3)
	a2=json.dumps(p2.text)
	with open("courses2.json","w") as file3:
		file3.write(a2)
		file3.close()
	f0=open("courses2.json")
	r=f0.read()
	a=json.loads(r)
	d=json.loads(a)
	#print(d)
	print (d['content'])
request_to_api(saral_url)