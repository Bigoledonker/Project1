from flask import Flask, redirect, request, send_file
import os
app = Flask(name)

@app.route('/')
def index():
    index_html = '''<form enctype="multipart/form-data" action="/upload" method="post">
  <div>
    <label for="file">Choose file to upload</label>
    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
  </div>
  <div>
    <button>Submit</button>
  </div>
</form> 
'''

    for file in list_files():
        index_html += "<li><a href="/files/" + file + "">" + file + "</a></li>\n"

    return index_html


@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['form_file']  # item name must match name in HTML form
    file.save(os.path.join("./files", file.filename))

    return redirect("/")

@app.route('/files/<filename>')
def get_file(filename):


    return send_file('./files/'+filename)
def list_files():
    files = os.listdir("./files")
    jpegs = []
    for file in files:
        if file.endswith(".jpeg") or file.endswith(".jpg"):
            jpegs.append(file)

    return jpegs

app.run(host='0.0.0.0', port=8080)


