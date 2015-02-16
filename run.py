from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('template.html',
                              name=None,
                              jedi=None)

@app.route("/hello/<name>")
def hello_person(name):
    name = name.capitalize()
    return render_template('template.html',
                              name=name,
                              jedi=None)

@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi = (first[0:3] + last[0:2]).capitalize()
    return render_template('template.html',
                             name=None,
                             jedi=jedi)

if __name__ == "__main__":
    app.run(debug='True', host="0.0.0.0", port=8080)
    