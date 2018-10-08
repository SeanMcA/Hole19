import requests

class H19SignIn:

	#sess = ""
	POST_url = "https://webws.hole19golf.com/api/v2/users/sign_in"
	#POST_url = "https://webws.hole19golf.com/api/v2/courses/106752"
	cookies = "_h19_session=T1FyNWxqUmdZcjhhZXVON2diMVR0aEVTV2QzZUlwcVBIYWxJWDV4djJ0ZTVDNlZ1NHl4WHVVYXVXa2Uvb0NjR0tKQU5vc1hVakJCU3JZc0JaTjdGUUE9PS0tTVFtUUFQaisyOGJxdDlhT21tVHREdz09--107a38991a2d811c8fa4be3c2615bd82dfae29cc; __cfduid=deb24d0e3ce1ac2f40be82b4f81479bde1538586041";


	params = {
		"email": "pmumbles@yahoo.co.uk",
		"password" : "guiness",
		"locale": "en_GB",
		"timezone": "Europe/Dublin"
	}
	 
	browser_headers = {
		"X-App-Version": "4.7.6",
		"X-Device-Model": "CUBOT RAINBOW",
		"X-Os-Version": "6.0",
		"X-Platform": "android",
		"Content-Type": "application/x-www-form-urlencoded",
		"Content-Length": "83",
		"Host": "appws.hole19golf.com",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"Cookie" : cookies,
		"User-Agent": "okhttp/3.8.0"	
	}
	 
	 
	  	# The class "constructor" - It's actually an initializer 
	#def __init__(self, sess):
		#self.cookie = cookie
		#self.sess = sess		
		#print("Cookie sent into GetCourses")		
		#print(cookie + self.cfduid)
	 
	def getCookies(self):
		thisdict = {}
		sess = requests.Session()
		a = sess.post(self.POST_url,  headers = self.browser_headers, data = self.params)
		#print(a.text)
		#print("Cookies")
		for c in a.cookies:
			thisdict =	{c.name : c.value}
		#print(thisdict)
		return thisdict
		
