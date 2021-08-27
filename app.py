from flask import Flask

# 9.4.3 create a new Flask App Instance
# __name__ denotes the name of the current function - can determine if code being
#     run from command line or imorted into anoher piece of code - magic methods (underscores)
app = Flask(__name__)
# create route starting at root ('/')
@app.route('/')
# create a function called hello_world()
def hello_world():
    return 'Hello world'