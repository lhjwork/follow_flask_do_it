from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_pybo():
     return 'Hello, Pybo!'


if __name__ == '__main__':
     app.secret_key='app.secert_kep'
     app.run(host='0.0.0.0', port=5000, debug=True)


