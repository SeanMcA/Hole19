import requests

class H19SignIn(object):

	#sess = ""
	POST_url = "https://appws.hole19golf.com/api/v2/users/sign_in"
	#POST_url = "https://webws.hole19golf.com/api/v2/courses/106752"
	cookiesDict = {'_h19_session': 'fuckYOU',}
	

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
		"User-Agent": "okhttp/3.8.0"	
	}
	 
	def getSignInCookies(self, sess):
		thisdict = {}
		print("\nThe cookies dictionary  sent to Sign In is: ")
		print(self.cookiesDict)
		a = sess.post(self.POST_url,  headers = self.browser_headers, data = self.params)
		print(a.text) # this confirms that login was successful
		#print("Cookies")
		for c in a.cookies:
			thisdict =	{c.name : c.value}
		print('\nSession: ')
		print(a.cookies)
		return thisdict
		
