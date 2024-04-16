from flask import Flask

app = Flask(__name__)

#@app.route('/') is actually a decorator and it is used to tell flask that this function is a route. the route is blank as it is the default route/homepage
@app.route("/")
def hello_world():
    return "<p>Hello World!, I'm Srinidhi</p>"

if __name__ == "__main__":
# 0.0.0.0 refers to it running locally
    app.run(host='0.0.0.0', debug=True)