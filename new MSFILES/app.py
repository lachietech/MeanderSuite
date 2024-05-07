from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add your authentication logic here
        # For example, you could check against a database of users

        # For simplicity, dummy check
        if username == 'user' and password == 'password':
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials. Please try again.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
