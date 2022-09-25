from flask import Flask, render_template, request, jsonify

import os
import socket
import platform

app = Flask(__name__, template_folder='.')

@app.route('/json', methods = ['GET'])

def helloJSON():
    host = socket.gethostname()
    os = (platform.system()) + " - " + (platform.release()) + " - " + (platform.version()) + " - " + (platform.platform())
    ip_addr = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    local_ip = socket.gethostbyname(socket.gethostname())

    if(request.method == 'GET'):
        data = {
            "Host" : host,
            "Platform" : os,
            "Local IP" : local_ip,
            "Remote IP" : ip_addr,
            "User Agent" : user_agent
        }
        return jsonify(data)


@app.route('/')

def hello():
    host = socket.gethostname()
    os = (platform.system()) + " - " + (platform.release()) + " - " + (platform.version()) + " - " + (platform.platform())
    ip_addr = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    local_ip = socket.gethostbyname(socket.gethostname())

    return render_template('index.html', host=host, os=os, ip_addr=ip_addr, user_agent=user_agent, local_ip=local_ip)

if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(debug=True)

