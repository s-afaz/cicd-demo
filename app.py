from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Shahriar's CI/CD Pipeline! v3</h1>"
@app.route('/health-sensor')
def health():
	return "OK", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
