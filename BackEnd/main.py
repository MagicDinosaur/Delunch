from flask import Flask

app = Flask(__name__)

# import models, routes
from routes.user import user_view
from routes.stream import stream_view


#register blueprints
app.register_blueprint(user_view)
app.register_blueprint(stream_view)

if __name__ == '__main__':
    app.run(port = 8000, debug=True)
