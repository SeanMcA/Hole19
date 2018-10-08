import requests

class H19GetCourses:

	POST_url = "https://webws.hole19golf.com/api/v3/home?latitude=53.3331&longitude=-6.2489"
	cookie = ""
	cfduid = "; __cfduid=deb24d0e3ce1ac2f40be82b4f81479bde1538586041"
	 
	 
	 
	browser_headers = {
		"X-App-Version": "4.7.6",
		"X-Device-Model": "CUBOT RAINBOW",
		"X-Os-Version": "6.0",
		"X-Platform": "android",
		"Host": "appws.hole19golf.com",
		"Connection": "Keep-Alive",
		"Accept-Encoding": "gzip",
		"Cookie": cookie + cfduid, 
		"User-Agent": "okhttp/3.8.0"	
	}
	 
	 
	 	# The class "constructor" - It's actually an initializer 
	def __init__(self, cookie):
		self.cookie = cookie	
		print("Cookie sent into GetCourses")		
		print(cookie + self.cfduid)
		
	
		
	def getCookies(self):
		mydict = {}
		a = requests.post(self.POST_url,  headers = self.browser_headers)
		print(a.text)
		print("Cookies")
		for c in a.cookies:
			mydict = {c.name : c.value}
		#print(mydict)
		return mydict
		
