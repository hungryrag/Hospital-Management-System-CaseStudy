from application import app, db
from flask import render_template, flash, jsonify, request, redirect, url_for
from application.models import (
    User,
    Patient,
    Medicine,
    Diagnostic,
    DiagsIssue,
    MedsIssue,
)
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
def addDiagnostics():
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


@app.route("/update-success", methods=["GET", "POST"])
def updateSuccess():
    if request.method == "POST":
        patient_id = request.form.get("patient_id")
        # print(patient_id)
        test_id = request.form.get("test_id")
        # print(test_id)

        patient = Patient.query.filter_by(ws_pat_id=patient_id).first()
        diagnostic = Diagnostic.query.filter_by(ws_test_id=test_id).first()

        diag_issue = DiagsIssue()
        diag_issue.diagnostic_issued = diagnostic
        patient.diagnostics.append(diag_issue)

        db.session.commit()
        flash("Updated Successfully!", "success")
        return render_template("update-success.html")
    else:
        return redirect(url_for("addDiagnostics"))
