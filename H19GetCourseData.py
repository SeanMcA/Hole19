import requests

class H19GetCourseData:
	POST_url = "https://webws.hole19golf.com/api/v2/courses/106752"
	cookie = ""
	 
	browser_headers = {
		"X-App-Version": "4.7.6",
		"X-Device-Model": "CUBOT RAINBOW",
		"X-Os-Version": "6.0",
		"X-Platform": "android",
		"Host": "appws.hole19golf.com",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"Cookie": "_h19_session=T1FyNWxqUmdZcjhhZXVON2diMVR0aEVTV2QzZUlwcVBIYWxJWDV4djJ0ZTVDNlZ1NHl4WHVVYXVXa2Uvb0NjR0tKQU5vc1hVakJCU3JZc0JaTjdGUUE9PS0tTVFtUUFQaisyOGJxdDlhT21tVHREdz09--107a38991a2d811c8fa4be3c2615bd82dfae29cc; __cfduid=deb24d0e3ce1ac2f40be82b4f81479bde1538586041";
		"User-Agent": "okhttp/3.8.0"	
	}
	
	# The class "constructor" - It's actually an initializer 
	def __init__(self, cookie):
		self.cookie = cookie
		
	
	def getInfo(self):	 
		sess = requests.Session()
		a = sess.post(self.POST_url,  headers = self.browser_headers)
		print(a.text)
		
