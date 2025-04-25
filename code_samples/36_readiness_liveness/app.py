from flask import Flask
import time

app = Flask(__name__)
start_time = time.time()

@app.route('/ready')
def ready():
    # Simulates readiness only after 10 seconds
    if time.time() - start_time > 10:
        return "Ready", 200
    else:
        return "Not Ready", 500

@app.route('/health')
def health():
    # Simulate failure after 30 seconds (crash/hang)
    if time.time() - start_time < 30:
        return "Alive", 200
    else:
        return "Crashed", 500

@app.route('/')
def hello():
    return "Welcome to the Demo App", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
