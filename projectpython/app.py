from flask import Flask, render_template
import socket
import datetime
import random

app = Flask(__name__)

# Sample data for demonstration
QUOTES = [
    "Cloud-native applications are the future of software development.",
    "Containerization simplifies deployment and scaling.",
    "DevOps is all about automation and efficiency.",
    "Microservices architecture enables flexible scaling."
]

TECHNOLOGIES = [
    "Docker", "Flask", "Python", "Cloud Computing",
    "Microservices", "Containerization", "DevOps"
]

@app.route('/')
def home():
    return render_template('index.html',
                           quote=random.choice(QUOTES),
                           technologies=TECHNOLOGIES,
                           hostname=socket.gethostname(),
                           current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                           container_ip=socket.gethostbyname(socket.gethostname()))

@app.route('/health')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)