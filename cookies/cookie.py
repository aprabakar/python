from flask import Flask,make_response,request,render_template

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login",methods=['POST','GET'])
def setcookie():
	if request.method=='POST':
	    user=request.form['n']
	    
    	r=make_response(render_template('link.html'))
    	r.set_cookie('UserId',user)
    	return r
@app.route("/get")
def getcookie():
   u=request.cookies.get('UserId')
   return "cookie is:" + u

if __name__=='__main__':
    app.run(debug=True)  