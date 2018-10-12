# BreatheSense: SRM Hackathon 2018
# Developer : Dhairya Parikh
from flask import Flask, jsonify, request
import random
import time
from os import system
app = Flask(__name__)

@app.route('/isTyping', methods=['GET'])
def isTyping():
    f = open("istyping.txt", "r")
    stat=f.read()
    return stat

@app.route('/getMessage', methods=['GET'])
def getMessage():
    f = open("speathe.txt", "r")
    msg=f.read()
    return msg

@app.route('/isLive',methods=["GET"])
def welcome():
    return 1

@app.route('/addMessage',methods=["GET"])
def addMessage():
    print("************************************************************")
    a=request.args
    msg=str(a.get("msg"))
    tts='"espeak \''+ msg + '\'"'
    os.system(tts)
    return str(1)

if __name__ == '__main__':
    app.run(host='192.168.43.211', port=80)
