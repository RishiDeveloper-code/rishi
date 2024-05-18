from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        # Handle the login logic here (e.g., checking credentials)
        flash(f'{username} logged in successfully!', 'success')
        # Notify the admin (you) that a user has logged in
        notify_admin(username)
        return redirect(url_for('dashboard', username=username))
    return render_template('index.html', form=form)

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

def notify_admin(username):
    # This is a simple print statement to simulate notification
    # In a real-world scenario, you might send an email or log to a file
    print(f'Notification: {username} has logged in.')

if __name__ == '__main__':
    app.run(debug=True)