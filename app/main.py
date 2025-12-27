from flask import Flask, request, render_template, session
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_string'

from app.torch_utils import transform_image, get_prediction
from app.scraper import build_url, extract_information

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'heic']
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    file_form = PhotoForm()
    zip_form = ZipForm()

    if file_form.submit1.data and file_form.validate_on_submit(): #new line added here!
        if request.method == "POST":
            file = file_form.file.data
            if file is None or file.filename == "":
                return render_template("index.html", file_form = file_form, prediction = "no file uploaded")
            if not allowed_file(file.filename):
                return render_template("index.html", file_form = file_form, prediction = "format not supported")
            try:
                img_bytes = file.read()
                tensor = transform_image(img_bytes)
                prediction = get_prediction(tensor)
                session['prediction'] = prediction
                return render_template("index.html", file_form = file_form, zip_form = zip_form, prediction = prediction)
            except Exception:
                return render_template("index.html", file_form = file_form, prediction = "error during prediction")
    
    if zip_form.submit2.data:
        prediction = session.get('prediction')
        zip = zip_form.zip.data
        url = build_url(prediction, zip)
        facilities = extract_information(url)
        return render_template("index.html",file_form=file_form,zip_form=zip_form,prediction=prediction,facilities=facilities)
    else:
        return render_template("index.html", file_form = file_form)

class PhotoForm(FlaskForm):
    file = FileField("file", validators=[FileRequired()], render_kw={"accept": "image/*", "class": "file-input"})

    submit1 = SubmitField('upload', render_kw={"class": "file-submit-btn"})

class ZipForm(FlaskForm):
    zip = StringField("zip", render_kw={"class": "zip-input"}, validators = [validators.DataRequired(), validators.Length(min=5, max=5)], )
    submit2 = SubmitField('Upload', render_kw={"class": "zip-submit-btn"})

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(port=5000)