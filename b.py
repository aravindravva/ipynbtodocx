import os
from flask import *  
import pypandoc

app = Flask(__name__) 
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 
UPLOAD_DIRECTORY = "/uploaded files"



@app.route('/')  
def upload():  
    return render_template("index.html")  
 
@app.route('/uploadfiles', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  

        f.save(os.path.join(UPLOAD_DIRECTORY, f.filename)) 
        
        fn=os.path.join(UPLOAD_DIRECTORY, f.filename)
        ra=f.filename[:-6]+".docx"
        op=os.path.join(UPLOAD_DIRECTORY, ra)
        try:
            pypandoc.convert_file(fn,"docx",outputfile=op)
        except:
            print("cant do task")
    return send_from_directory(UPLOAD_DIRECTORY, ra, as_attachment=True)






if __name__ == '__main__':  
    app.run(debug = True)  