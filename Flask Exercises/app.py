from flask import Flask, request, abort, render_template

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    name = request.args.get("name") or 'visitor'
    return 'Hello World! (and {} too)'.format(name)


@app.route('/type1/<string:string_param>', methods=["GET"])
def type1(string_param):
    """Returns the text of the last part of the URL"""
    return string_param


@app.route('/type2/<int:int_param>', methods=["GET"])
def type2(int_param):
    """Returns the int number forming last part of the URL converted to text"""
    return str(int_param)


@app.route('/type3/<float:float_param>', methods=["GET"])
def type3(float_param):
    """Returns the float number forming last part of the URL converted to text"""
    return str(float_param)


@app.route('/type4/<path:path_param>', methods=["GET"])
def type4(path_param):
    """Returns the specified path forming last part of the URL"""
    return path_param


@app.route('/type5/<any("option1", "option2"):list_param>', methods=["GET"])
def type5(list_param):
    """Returns only if option1 or option2 are the accessed URLs"""
    return list_param


@app.route('/type6/<uuid:uuid_param>', methods=["GET"])
def type6(uuid_param):
    """Returns the UUID forming the end of the URL"""
    return uuid_param


@app.route('/params', methods=["GET", "POST"])
def params():
    """Returns the parameters coming with the request"""
    return request.args


@app.route('/template', methods=["GET"])
def template():
    """Returns a template with some params"""
    return render_template("index.html", name="Edu", list=[1, 2, 3, 4, 5])


@app.route('/error', methods=["GET", "POST"])
def error():
    """Returns an error depending on the code specified when aborting.The error is handled by the code of the
    handlers """
    return abort(403)


@app.errorhandler(403)
def error_not_found(error):
    """Basic error handler for 404 errors, overwrites the default behavior"""
    print(error)
    return "Page forbidden", 403


@app.errorhandler(404)
def error_not_found(error):
    """Basic error handler for 404 errors, overwrites the default behavior"""
    print(error)
    return "Page not found", 404


if __name__ == '__main__':
    app.run()
