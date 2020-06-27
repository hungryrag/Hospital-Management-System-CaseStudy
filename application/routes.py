from application import app
from flask import render_template


@app.route("/view-patient", methods=["GET", "POST"])
def viewPatient():
    return render_template("view-patient.html", title="View Patient")


@app.route("/add-diagonostics", methods=["GET", "POST"])
def addDiagonostics():
    return render_template("add-diagonostics.html")
