from flask import Flask
from flask_restful import Api



from tasks import Fibonacci, ReverseWords, Token, TriangleType



app = Flask(__name__)

app.secret_key = 'jose'
api = Api(app)





api.add_resource(Fibonacci, '/api/fibonacci')
api.add_resource(ReverseWords, '/api/ReverseWords')
api.add_resource(Token, '/api/Token')
api.add_resource(TriangleType, '/api/TriangleType')

if __name__ == '__main__':
    app.run()
