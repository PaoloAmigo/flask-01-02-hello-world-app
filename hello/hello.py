from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World I am Paolo, page one Test3!</p>"

@app.route('/my_page')
def second():
    return 'This is second page... is my Test'

@app.route('/my_template')
def my_template():
    name = 'Paolo'
    return render_template('my_template.html', name=name)

@app.route('/dynamic/<int:id>')
def dynamic(id):
    return render_template('dynamic.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host= '0.0.0.0', port=80)