import tornado.ioloop
import tornado.web
import tornado.template

class MainHandler(tornado.web.RequestHandler):
    def get(self):
		loader = tornado.template.Loader(".")
		self.write(loader.load("index.html").generate())

	
application = tornado.web.Application([(r"/", MainHandler),
										(r"/images/(.*)", tornado.web.StaticFileHandler, {"path":"./images"}),
										(r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path":"./fonts"}),
										(r"/css/(.*)", tornado.web.StaticFileHandler, {"path":"./css"}),
										(r"/js/(.*)", tornado.web.StaticFileHandler, {"path":"./js"}),
										(r"/sass/(.*)", tornado.web.StaticFileHandler, {"path":"./sass"}),
										])
if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
