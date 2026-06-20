from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard01')
def dashboard01():
    return render_template('dashboard01.html')

@app.route('/dashboard02')
def dashboard02():
    return render_template('dashboard02.html')

@app.route('/story')
def story():
    return render_template('story.html')

if __name__ == '__main__':
    app.run(debug=True)