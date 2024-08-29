from flask import Flask
from web.routes import configure_routes

app = Flask(__name__, static_folder='web/static/', template_folder='web/templates/')

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)