from flask import Flask, render_template, request
import time

app = Flask(__name__)

def comp(str_a, str_b):
    if len(str_a) != len(str_b):
        return False
    for i in range(len(str_a)):
        if str_a[i] != str_b[i]:
            return False
        time.sleep(0.01)
    return True

@app.route('/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        user_password = request.form['password']
        result = login(user_password)
        return render_template('result.html', result=result)
    return render_template('login.html')

def login(user_password):
    secret = 'username'
    if comp(secret, user_password):
        return 'User has been granted access permission.'
    return 'User does not have access permission.'

if __name__ == '__main__':
    app.run(debug=True)
