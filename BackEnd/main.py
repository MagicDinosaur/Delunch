from flask import Flask

app = Flask(__name__)

# import models, routes
from routes.user import user_view



#register blueprints
app.register_blueprint(user_view)


if __name__ == '__main__':
    app.run(debug=True)
