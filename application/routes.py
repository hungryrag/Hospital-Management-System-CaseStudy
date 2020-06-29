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
    if request.method == "POST":
        patient_id = request.form.get("patient_id")
        patient = Patient.query.filter_by(ws_pat_id=patient_id).first()

        diagnostic = Diagnostic.query.all()
        diags = {}
        # cost = []
        for diag in patient.diagnostics:
            diags[
                diag.diagnostic_issued.ws_diagn
            ] = diag.diagnostic_issued.ws_test_charge

        # print(diags)

        if patient:
            return render_template(
                "add-diagnostics.html",
                title="Diagnostics",
                patient=patient,
                diagnostic=diagnostic,
                diag_issued=diags,
            )
        else:
            flash("Patient ID does not exist. Enter corrent Patient ID", "danger")
            return render_template(
                "add-diagnostics.html",
                title="Diagnostics",
                patient=None,
                diagnostic=None,
                diag_issued=None,
            )
    else:
        return render_template(
            "add-diagnostics.html",
            title="Diagnostics",
            patient=None,
            diagnostic=None,
            diag_issued=None,
        )


@app.route("/update-diagnostics", methods=["GET", "POST"])
@app.route("/update-diagnostics/<patient_id>", methods=["GET", "POST"])
def updateDiagnostics(patient_id):
    patient_id = request.args.get("patient_id")
    print(patient_id)
    patient = Patient.query.filter_by(ws_pat_id=patient_id).first()
    return render_template(
        "update-diagnostics.html", title="Diagnostics", patient=patient
    )

