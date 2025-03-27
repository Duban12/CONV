from flask import Flask, request, render_template, send_file, redirect, url_for, flash
from pdf2docx import Converter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["RESULT_FOLDER"] = RESULT_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No se ha seleccionado ningún archivo", "error")
            return redirect(url_for("upload_file"))

        file = request.files["file"]

        if file.filename == "":
            flash("No se ha seleccionado ningún archivo", "error")
            return redirect(url_for("upload_file"))

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            docx_filename = filename.rsplit(".", 1)[0] + ".docx"
            docx_path = os.path.join(app.config["RESULT_FOLDER"], docx_filename)

            try:
                cv = Converter(file_path)
                cv.convert(docx_path, start=0, end=None)
                cv.close()
                return send_file(docx_path, as_attachment=True)
            except Exception as e:
                flash(f"Error en la conversión: {str(e)}", "error")
                return redirect(url_for("upload_file"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
