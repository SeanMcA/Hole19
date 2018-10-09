from H19SignIn import *
from H19GetCourses import *
from H19GetActivitiesHome import *
import requests



class start:
	sess = requests.Session()	
	
	h19 = H19SignIn()
	cookies = h19.getSignInCookies(sess)
	for x in cookies:
		print("\nCookies returned from SignIn: ")
		print(x) # prints the key
		print(cookies[x]) # prints the value



	h19GetActivities = H19GetActivitiesHome(cookies[x])
	activitiesCookies = h19GetActivities.getActivityCookies(sess)
	for x in activitiesCookies:
		print("\nCookies returned from Activities: ")
		print(x) # prints the key
		print(activitiesCookies[x]) # prints the value



	#h19Courses = H19GetCourses(cookies[x])
	#courseCookies = h19Courses.getCourseCookies(sess)
	#for x in courseCookies:
		#print("Cookies returned from GetCourses")
		#print(x) # prints the key
		#print(courseCookies[x]) # prints the value
				
				
		
