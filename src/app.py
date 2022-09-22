from flask import Flask
from flask_restful import Api
from routes import init_routes
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# app.secret_key = 'test12345'
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
api = Api(app)

# Initialize routes
init_routes(api)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000,debug=True)