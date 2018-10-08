from H19SignIn import *
from H19GetCourses import *
import requests

#sess = requests.Session()


h19 = H19SignIn()
cookies = h19.getCookies()
for x in cookies:
	print("Cookies returned from SignIn")
	print(x) # prints the key
	print(cookies[x]) # prints the value

	
	
h19Courses = H19GetCourses(cookies[x])
courseCookies = h19Courses.getCookies()
for x in courseCookies:
	print("Cookies returned from GetCourses")
	print(x) # prints the key
	print(courseCookies[x]) # prints the value