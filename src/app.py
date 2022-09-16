from flask import Flask
from flask_restful import Api
from routes import init_routes

app = Flask(__name__)
api = Api(app)

# Initialize routes
init_routes(api)


app.run(debug=True)