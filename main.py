from flask import Flask
app = Flask(__name__)

@app.route('/')
def hola():
    return '<html><body><h1>¡Hola Mundo!</h1></body></html>'

@app.route('/sorpresa')
def sorpresa():
    return '<html><body><h1>¡Sorpresa!</h1></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
