from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get("name") or 'visitor'
    return 'Hello World! (and {} too)'.format(name)


if __name__ == '__main__':
    app.run()
