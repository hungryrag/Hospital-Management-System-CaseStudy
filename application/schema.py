from application import app
from flask_marshmallow import Marshmallow


ma = Marshmallow(app)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_login_id', 'password', 'timestamp')


class PatientSchema(ma.Schema):
    class Meta:
        fields = ('ws_pat_id', 'ws_ssn', 'ws_pat_name', 'ws_age', 'ws_doj',
                  'ws_rtype', 'ws_adrs', 'patient_city', 'patient_state', 'patient_status')


class MedicineSchema(ma.Schema):
    class Meta:
        fields = ('ws_med_id', 'ws_med_name', 'ws_qty_avbl', 'ws_med_rate')


class DiagnosticSchema(ma.Schema):
    class Meta:
        fields = ('ws_test_id', 'ws_diagn', 'ws_test_charge')


# Schema Instantiation
user_schema = UserSchema()
users_schema = UserSchema(many=True)

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)

medicine_schema = MedicineSchema()
medicines_schema = MedicineSchema(many=True)

diagnostic_schema = DiagnosticSchema()
diagnostics_schema = DiagnosticSchema(many=True)
