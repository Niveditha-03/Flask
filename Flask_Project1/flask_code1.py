from flask import Flask, render_template

# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'hello test'
# if __name__ == '__main__':
#     app.run(debug = True)

# Method-2:direct redering of html file
# app = Flask(__name__)
# @app.route('/')
# def hello_html():
#     return """
#     <!doctype html>
#     <html>
#     <head>
#         <title> Welcome</title>
#     </head>
#     <body>
#     Hello  My first HTML PAGE!!
#     </body>
#     </html>
#     """
#
# if __name__ == "__main__":
#     app.run(debug = True)

# # ------------------------------------------------------------------------------------------------
# # Method - 3: Rendering html file- "home.html" inside templates directory.
# app = Flask(__name__)
#
# @app.route('/')
# def hello_html():
#     return render_template("home.html")
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

##Method - 4: Rendering html file- "home.html" inside templates directory.
app = Flask(__name__)


@app.route('/')
def hello_html():
    return render_template("index.html")


@app.route('/feedback')
def feedback():
    return render_template("feedback.html")


if __name__ == '__main__':
    app.run(debug=True)
