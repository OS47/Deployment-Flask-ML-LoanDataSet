from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, FloatField

class PredictdataForm(FlaskForm):
    gender = SelectField('Gender',choices=[('Male', 'Male'), ('Female', 'Female')])
    married = SelectField('Married',choices=[('Yes', 'Yes'), ('No', 'No')])
    dependents = SelectField('Dependents',choices=[('0', '0'), ('1', '1'),('2','2'),('3+','3+')])
    education = SelectField('Education',choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')])
    self_employed = SelectField('Self_Employed',choices=[('Yes', 'Yes'), ('No', 'No')])
    applicantincome = IntegerField('ApplicantIncome')
    coapplicantincome = FloatField('CoapplicantIncome')
    loanamount = FloatField('LoanAmount')
    loan_amount_term = FloatField('Loan_Amount_Term')
    credit_history = SelectField('credit_history',choices=[('0', '0'), ('1', '1')])
    property_area = SelectField('Property_Area',choices=[('Semiurban', 'Semiurban'), ('Urban', 'Urban'),('Rural','Rural')])


    
