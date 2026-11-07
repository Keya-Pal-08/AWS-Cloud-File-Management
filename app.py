
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import boto3
import os
from io import BytesIO
from werkzeug.utils import secure_filename
from botocore.exceptions import ClientError

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-this-secret")

# AWS S3 Configuration
S3_BUCKET = "keya-s3-project-2026"
AWS_REGION = "ap-southeast-2"

# Connect to S3 using EC2 IAM Role
s3 = boto3.client(
    "s3",
    region_name=AWS_REGION
)

@app.route("/")
def home():
    try:
        response = s3.list_objects_v2(Bucket=S3_BUCKET)
        files = [
            item["Key"]
            for item in response.get("Contents", [])
        ]
        return render_template("index.html", files=files)

    except ClientError as e:
        app.logger.exception("S3 listing failed")
        flash("Unable to load files from S3.")
        return render_template("index.html", files=[])

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        flash("No file selected!")
        return redirect(url_for("home"))

    file = request.files["file"]

    if file.filename == "":
        flash("Please select a file!")
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)

    if not filename:
        flash("Invalid file name!")
        return redirect(url_for("home"))

    try:
        s3.upload_fileobj(
            file,
            S3_BUCKET,
            filename
        )
        flash("File uploaded successfully to AWS S3!")

    except ClientError:
        app.logger.exception("S3 upload failed")
        flash("Upload failed. Please check S3 permissions.")

    return redirect(url_for("home"))

@app.route("/download/<path:filename>")
def download_file(filename):
    try:
        response = s3.get_object(
            Bucket=S3_BUCKET,
            Key=filename
        )

        return send_file(
            BytesIO(response["Body"].read()),
            as_attachment=True,
            download_name=filename
        )

    except ClientError:
        app.logger.exception("S3 download failed")
        flash("Unable to download this file.")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
