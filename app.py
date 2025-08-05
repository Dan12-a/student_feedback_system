from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

subjects = ['PCS551', 'PCS552', 'PCS553', 'PCS561', 'PCS573']
feedback_data = []

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        feedback = {'name': name}
        for subject in subjects:
            feedback[subject] = int(request.form.get(subject, 0))
        feedback_data.append(feedback)
        return render_template('thankyou.html', name=name)
    return render_template('index.html', subjects=subjects, error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect('/admin')
        else:
            error = 'Invalid credentials'
    return render_template('login.html', error=error)

@app.route('/admin')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect('/login')
    return render_template('feedbacks.html', feedbacks=feedback_data, subjects=subjects)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
