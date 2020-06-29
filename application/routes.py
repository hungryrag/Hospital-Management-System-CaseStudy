from application import app
from flask import render_template, flash, jsonify, request, redirect, url_for
from application.models import User, Patient, Medicine, Diagnostic
from application.schema import (
    users_schema,
    patients_schema,
    medicines_schema,
    diagnostics_schema,
)


@app.route("/")
@app.route("/index")
def index():
    return "<h1>Welcome!!</h1>"


@app.route("/view-patient", methods=["GET", "POST"])
def viewPatient():
    if request.method == "POST":
        patient_id = request.form.get("patient_id")
        patient = Patient.query.filter_by(ws_pat_id=patient_id).first()
        if patient:
            return render_template(
                "view-patient.html", title="View Patient", patient=patient
            )
        else:
            flash("Patient ID does not exist. Enter corrent Patient ID", "danger")
            return render_template(
                "view-patient.html", title="View Patient", patient=None
            )
    else:
        return render_template("view-patient.html", title="View Patient", patient=None)


@app.route("/add-diagnostics", methods=["GET", "POST"])
def addDiagonostics():
    return render_template("add-diagnostics.html")
