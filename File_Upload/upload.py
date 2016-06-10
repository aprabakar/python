from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route('/upload')
def upload():
   return '''
   		<!doctype html>
    	<title>Upload new File</title>
    	<h1>Upload new File</h1>
    	<form action="http://localhost:5000/uploader" method=post enctype=multipart/form-data>
      		<p><input type=file name=file accept=images/*>
         	<input type=submit value=Upload>
    	</form>
    	'''
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    target = os.path.join(APP_ROOT, 'static')
    
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
   
    f = request.files['file']
    filename=f.filename
    print filename
    destination='/'.join([target,filename])
    print destination
    f.save(secure_filename(destination))
    return render_template("complete.html",filename=filename)

#def print_file(image_name):
 #   return send_from_directory('images',image_name)

		
if __name__ == '__main__':
   app.run(debug = True)