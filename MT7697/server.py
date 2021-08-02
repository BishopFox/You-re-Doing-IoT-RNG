import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        print("Got", len(self.request.body), "new numbers")
        file = open("randomnumbers.bin", "ab")
        file.write(self.request.body)
        file.close()


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
