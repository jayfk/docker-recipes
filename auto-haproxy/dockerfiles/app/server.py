from flask import Flask, request
import socket
app = Flask(__name__)

@app.route("/")
def index():
    return """
    Hostname: {hostname}<br/>
    IP: {ip}<br/>
    Requesting IP: {requesting_ip}<br/>

    """.format(
        hostname=socket.gethostname(),
        ip=socket.gethostbyname(socket.gethostname()),
        requesting_ip=request.remote_addr,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)