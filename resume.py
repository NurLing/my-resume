from flask import Flask, session, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to get secure key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/courses')
def show_all_courses():
    courses = [
        'ACCT207',
        'ACCT208',
        'ACCT209'
    ]

    return render_template('course.html', courses=courses)
	
	
@app.route('/about')
def about():
    return render_template('about.html')
	
@app.route('/users')
def show_all_users():
    return render_template('user-all.html')


@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        # return render_template('form-demo.html', first_name=first_name)
        return redirect(url_for('form_demo'))


@app.route('/user/<string:name>/')
def get_user_name(name):
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('user.html', name=name)


@app.route('/song/<int:id>/')
def get_song_id(id):
    # return "This song's ID is " + str(id)
    return "Hi, this is %s and the song's id is %d" % ('administrator', id)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)