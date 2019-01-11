from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
app = Flask(__name__)

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/adminpage')
def adminpage():
    return render_template('basic.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/print')
def print():
    return render_template('print.html')

@app.route('/logout')
def logout():
    return render_template('basic.html')

@app.route('/')
def main():
    return render_template('print.html')
if __name__ == "__main__":
    app.run()
