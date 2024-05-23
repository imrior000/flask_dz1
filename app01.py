from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/str1/')
def str1():
    return render_template('str1.html')

@app.route('/str2/')
def str2():
    return render_template('str2.html')

@app.route('/str3/')
def str3():
    return render_template('str3.html')

if __name__ == '__main__':
    app.run()