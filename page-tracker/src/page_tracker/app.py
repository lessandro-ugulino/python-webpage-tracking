# import the modules Flask, functools and Redis
from flask import Flask
from redis import Redis
from functools import cache

# instantiate a Flask application and a Redis client
app = Flask(__name__)
# redis = Redis()

# define a controller function to handle HTTP requests arriving at /


@app.get("/")
def index():
    # page_views = redis.incr("page_views")
    page_views = redis().incr("page_views")
    return f"This page has been seen {page_views} times."


@cache
def redis():
    return Redis()
