
import flask
import blogs.router


application = flask.Flask(__name__)
application.register_blueprint(blogs.router.blog)

application.debug = True

if __name__ == '__main__':
	application.run()
