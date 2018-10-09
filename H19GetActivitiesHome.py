import requests

class H19GetActivitiesHome:

	POST_url = "https://appws.hole19golf.com/api/v3/activities/home"
	cookiesDict = {'_h19_session': '',
					'__cfduid': 'deb24d0e3ce1ac2f40be82b4f81479bde1538586041'}
	 
	 
	 
	browser_headers = {
		"X-App-Version": "4.7.6",
		"X-Device-Model": "CUBOT RAINBOW",
		"X-Os-Version": "6.0",
		"X-Platform": "android",
		"Host": "appws.hole19golf.com",
		"Connection": "Keep-Alive",
		#"Accept-Encoding": "gzip",
		"User-Agent": "okhttp/3.8.0"	
	}
	 
	 
	 	# The class "constructor" - It's actually an initializer 
	def __init__(self, cookie):	
		self.cookiesDict['_h19_session'] = cookie;
		print("\nCookie sent into GetActivities")		
		print(cookie)
		
	
		
	def getActivityCookies(self, sess):
		mydict = {}
		print("\nThe cookies dictionary used to get the Activities is: ")
		print(self.cookiesDict)
		a = sess.post(self.POST_url,  headers = self.browser_headers, cookies = self.cookiesDict)
		print('\nReturned data: ')
		print(a.text)
		print("Activity Cookies")
		for c in a.cookies:
			mydict = {c.name : c.value}
		#print(mydict)
		return mydict
		
