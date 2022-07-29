
from flask import Flask, render_template, flash, redirect, request, send_from_directory, url_for
from logging import FileHandler , WARNING
import urllib.request
import os
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__, template_folder='template')

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'

app.secret_key = 'avin.chelseafc'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 *1024

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/',methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash("No File Part")
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash("No Image Selected for Uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        sketch_image(os.path.join(app.config['UPLOAD_FOLDER'], filename),filename)
        #print('upload image filename : ' + filename)
        flash('Image successfully uploaded')
        return render_template('index.html',  filename = filename)
    else:
        flash("Allowed image types are - png, jpeg, jpg, gif ")
        return redirect(request.url)

def invert_blend(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

def sketch_image(path,filename):
	img=cv2.imread(path)
	#cv2.imshow(img)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_gray_inv = 255 - img_gray
	img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(21, 21),
	                            sigmaX=0, sigmaY=0)
	img_blend = invert_blend(img_gray, img_blur)
	cv2.imwrite(os.path.join(app.config['DOWNLOAD_FOLDER'] + filename),img_blend)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
    #return send_from_directory(app.config['DOWNLOAD_FOLDER'],filename,as_attachment=True)

@app.route('/sketch/<filename>')
def display_sketch_img(filename):
    return redirect(url_for('static',filename='downloads/' + filename),code=301)
if __name__ == '__main__':
    app.run(debug=True)