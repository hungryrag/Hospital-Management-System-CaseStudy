from application import app, db
from sqlalchemy import Column, Integer, Float, String, DateTime, Date
from datetime import datetime


@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database Created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database Dropped!')


@app.cli.command('db_seed')
def db_seed():
    user1 = User(user_login_id='sdutta',
                 password='superman',
                 timestamp=datetime.utcnow())

    db.session.add(user1)
    db.session.commit()

    user2 = User(user_login_id='soham_h',
                 password='hazard',
                 timestamp=datetime.utcnow())

    db.session.add(user2)
    db.session.commit()

    patient_ = Patient(ws_pat_id=100000001,
                       ws_ssn=123456789,
                       ws_pat_name='Haripada Bandwala',
                       ws_age=22,
                       ws_doj=datetime.utcnow().date(),
                       ws_rtype='Semi Room',
                       ws_adrs='108, Chinar Park',
                       patient_city='Kolkata',
                       patient_state='West Bengal',
                       patient_status='Active')

    patient1 = Patient(ws_ssn='123556789',
                       ws_pat_name='Ambar Chatterjee',
                       ws_age=22,
                       ws_doj=datetime.utcnow().date(),
                       ws_rtype='Semi Room',
                       ws_adrs='108, Chinar Park',
                       patient_city='Kolkata',
                       patient_state='West Bengal',
                       patient_status='Active')

    patient2 = Patient(ws_ssn='768556789',
                       ws_pat_name='Supriyo Jana',
                       ws_age=24,
                       ws_doj=datetime.utcnow().date(),
                       ws_rtype='Semi Room',
                       ws_adrs='69, Pabitra Road',
                       patient_city='Kolkata',
                       patient_state='West Bengal',
                       patient_status='Active')

    patient3 = Patient(ws_ssn='394860212',
                       ws_pat_name='John Doe',
                       ws_age=28,
                       ws_doj=datetime.utcnow().date(),
                       ws_rtype='Single Room',
                       ws_adrs='99, Brooklyn Drive',
                       patient_city='New York',
                       patient_state='New York State',
                       patient_status='Active')

    db.session.add(patient_)
    db.session.add(patient1)
    db.session.add(patient2)
    db.session.add(patient3)
    db.session.commit()

    medicine1 = Medicine(ws_med_name='Calpol',
                         ws_qty_avbl=2000,
                         ws_med_rate=20)

    medicine2 = Medicine(ws_med_name='Honitus',
                         ws_qty_avbl=1200,
                         ws_med_rate=210)

    medicine3 = Medicine(ws_med_name='Pudin Hara',
                         ws_qty_avbl=1420,
                         ws_med_rate=60)

    medicine4 = Medicine(ws_med_name='Burnol',
                         ws_qty_avbl=580,
                         ws_med_rate=70)

    db.session.add(medicine1)
    db.session.add(medicine2)
    db.session.add(medicine3)
    db.session.add(medicine4)
    db.session.commit()

    diagnostic1 = Diagnostic(ws_diagn='X-Ray',
                             ws_test_charge=150)

    diagnostic2 = Diagnostic(ws_diagn='CT Scan',
                             ws_test_charge=700)

    diagnostic3 = Diagnostic(ws_diagn='USG',
                             ws_test_charge=910)

    diagnostic4 = Diagnostic(ws_diagn='Blood Test',
                             ws_test_charge=80)

    db.session.add(diagnostic1)
    db.session.add(diagnostic2)
    db.session.add(diagnostic3)
    db.session.add(diagnostic4)
    db.session.commit()

    med_issue1 = MedsIssue(qty_issued=10)
    med_issue1.medicine_issued = medicine3
    patient1.medicines.append(med_issue1)
    db.session.commit()

    med_issue2 = MedsIssue(qty_issued=1)
    med_issue2.medicine_issued = medicine4
    patient1.medicines.append(med_issue2)
    db.session.commit()

    med_issue3 = MedsIssue(qty_issued=6)
    med_issue3.medicine_issued = medicine1
    patient2.medicines.append(med_issue3)
    db.session.commit()

    diag_issue1 = DiagsIssue()
    diag_issue1.diagnostic_issued = diagnostic1
    patient1.diagnostics.append(diag_issue1)
    db.session.commit()

    diag_issue2 = DiagsIssue()
    diag_issue2.diagnostic_issued = diagnostic3
    patient3.diagnostics.append(diag_issue2)
    db.session.commit()

    diag_issue3 = DiagsIssue()
    diag_issue3.diagnostic_issued = diagnostic4
    patient3.diagnostics.append(diag_issue3)

    db.session.commit()

    print('Database Seeded!')


# Database Models

class MedsIssue(db.Model):
    __tablename__ = 'medsissue'
    ws_pat_id = Column(Integer, db.ForeignKey('patient.ws_pat_id'), primary_key=True)
    ws_med_id = Column(Integer, db.ForeignKey('medicine.ws_med_id'), primary_key=True)
    qty_issued = Column(Integer)
    medicine_issued = db.relationship('Medicine')


class DiagsIssue(db.Model):
    __tablename__ = 'diagsissue'
    ws_pat_id = Column(Integer, db.ForeignKey('patient.ws_pat_id'), primary_key=True)
    ws_test_id = Column(Integer, db.ForeignKey('diagnostic.ws_test_id'), primary_key=True)
    diagnostic_issued = db.relationship('Diagnostic')


class User(db.Model):
    __tablename__ = 'userstore'
    user_id = Column(Integer, primary_key=True)
    user_login_id = Column(String, unique=True)
    password = Column(String)
    timestamp = Column(DateTime)


class Patient(db.Model):
    __tablename__ = 'patient'
    ws_pat_id = Column(Integer, primary_key=True)
    ws_ssn = Column(Integer, unique=True)
    ws_pat_name = Column(String)
    ws_age = Column(Integer)
    ws_doj = Column(Date)
    ws_rtype = Column(String)
    ws_adrs = Column(String)
    patient_city = Column(String)
    patient_state = Column(String)
    patient_status = Column(String)
    medicines = db.relationship('MedsIssue')
    diagnostics = db.relationship('DiagsIssue')


class Medicine(db.Model):
    __tablename__ = 'medicine'
    ws_med_id = Column(Integer, primary_key=True)
    ws_med_name = Column(String, unique=True)
    ws_qty_avbl = Column(Integer)
    ws_med_rate = Column(Float)


class Diagnostic(db.Model):
    __tablename__ = 'diagnostic'
    ws_test_id = Column(Integer, primary_key=True)
    ws_diagn = Column(String, unique=True)
    ws_test_charge = Column(Integer)
