from flask import Flask
app = Flask(__name__)

@app.route('/')
def response():
  return "Hello world from a Flask container. Newly added. 2nd added"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
