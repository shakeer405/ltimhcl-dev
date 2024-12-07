from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, App Engine Flexible! version 1'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    print (port)
    app.run(host='0.0.0.0', port=8080)
