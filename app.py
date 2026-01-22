from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/second/<name>')
def name (name):
    length = len(name)
    if length > 4:
        return f"Hello, {name}! Your name has 4 characters."
    else:
        return f"Hello, {name}! Your name has {length} characters."

if __name__ == '__main__':
    app.run(debug=True)