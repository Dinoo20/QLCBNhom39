from urllib.parse import quote

import cloudinary
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "KJGHJG^&*%&*^T&*(IGFG%ERFTGHCFHGF^&**&TYIU"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/baydb?charset=utf8mb4" % quote('Nhom39@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app)
login = LoginManager(app)

cloudinary.config(
    cloud_name="djnja1wo5",
    api_key="535756611533541",
    api_secret="PtV3fkD64XC7sAJvNCC4JjDA",  # Click 'View API Keys' above to copy your API secret
    secure=True
)
