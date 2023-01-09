 # Using flask to make an api
# import necessary libraries and functions
from flask import Flask,request,jsonify,request
import os
import urllib3
import re
import json
import requests
import urllib3
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.

global dataFromReq
@app.route('/', methods = ['GET', 'POST'])
def home():
        if(request.method == 'GET'):
                os.system('nft -f TextFirewall.nft')
                data = request.host
                #global dataFromReq
                file_name = "TextFirewall.nft"
                file_content = ''
                f = open("./TextFirewall.nft", "r")
                text = str(f.read())
                text = re.sub(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', dataFromReq["remote_daddr"], text)
                f = open("./TextFirewall.nft", "w")
                f.write(text)
                f.close()
                os.system('nft -f TextFirewall.nft')
                return jsonify({'data': data,'data1': request.remote_addr})
        elif(request.method == 'GET'):
                return jsonify(dataFromReq)
@app.route('/process', methods = ['GET', 'POST'])
def process():
        if(request.method == 'POST'):
                global dataFromReq
                data1 = request.json
                dataFromReq = data1
                print(type(request),"request")
#return jsonify({'data': json.dumps(data),'data1':data})
                return jsonify({'data1': request.json})
                #return jsonify(dataFromReq)
        elif(request.method == 'GET'):
                return jsonify(dataFromReq)
if __name__ == '__main__':
        app.run(debug = True, host="0.0.0.0", port=5034)

