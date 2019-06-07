from flask import jsonify
from flask_restful import Resource, reqparse


class Fibonacci(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('n',
                        type=int,
                        location='args',
                        required=True,
                        help="This field cannot be left blank!"
                        )
        
        data = parser.parse_args()
        n = data["n"]

        def fib(n):
            if n <= 1:
                return n
            return fib(n-1) + fib(n - 2)

        return {"n": fib(n)}

class ReverseWords(Resource):
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sentence',
                        type=str,
                        location='args',
                        required=True,
                        help="This field cannot be left blank!"
                        )

        data = parser.parse_args()
        new_sentence = ""
        for c in reversed(data["sentence"]):
            new_sentence += c

        return {"sentence": new_sentence}

class Token(Resource):

    def get(self):
        return {"Token": "865a6eea-ee00-4cee-ad75-9ec6a170d4e7"}

class TriangleType(Resource):
        
    def get(self):    
        parser = reqparse.RequestParser()
        parser.add_argument('a',
                        type=int,
                        location='args',
                        required=True,
                        help="This field cannot be left blank!"
                        )
        parser.add_argument('b',
                        type=int,
                        location='args',
                        required=True,
                        help="This field cannot be left blank!"
                        )
        parser.add_argument('c',
                        type=int,
                        location='args',
                        required=True,
                        help="This field cannot be left blank!"
                        )
        data = parser.parse_args()
        a = data["a"]
        b = data["b"]
        c = data["c"]
        
        if a == b == c:
            return {"Triangle Type": "Equilateral"}
        elif a == b or a == c or b == c:
            return {"Triangle Type": "Isosceles"}
        else:
            return {"Triangle Type": "Scalene"}
        
