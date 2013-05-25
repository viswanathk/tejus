import tornado.ioloop
import tornado.web
import tornado.template
import communicate
import os
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		loader = tornado.template.Loader(".")
		self.write(loader.load("index.html").generate())
class SpeechRecognition(tornado.web.RequestHandler):
	def get(self):
		value = self.get_argument("value",True)
		if value == "on":
			communicate.speechRecognition = 1
		else:
			communicate.speechRecognition = 0
		print communicate.speechRecognition
			

application = tornado.web.Application([(r"/", MainHandler),
										(r"/speechRecognition", SpeechRecognition),
										(r"/web/(.*)", tornado.web.StaticFileHandler, {"path":"web"}),
										])
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

