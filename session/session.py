from flask import Flask,request,session,redirect,url_for,render_template,escape

app=Flask(__name__)
app.secret_key = "life"

@app.route('/login', methods = ['GET', 'POST'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['n']
      return redirect(url_for('index'))
   return render_template('login.html')
	
@app.route('/')
def index():
   if 'username' in session:
      user= session['username']
      return 'Logged in as ' + user+ '<br>' + \
            "<b><a href = '/logout'>click here to log out</a></b>"
   return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
  

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('index'))      


if __name__=='__main__':
    app.run(debug=True)  