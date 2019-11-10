import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from forms import PredictdataForm
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('xgb_model.joblib')
transformer = joblib.load('transformer.joblib')


app.config['SECRET_KEY'] = 'afd80f2fd7117ec41f2640d78a11a4e1'

@app.route('/',methods=['GET','POST'])
def index():
    form = PredictdataForm()
    return render_template('indextrans.html',form = form)

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    form = PredictdataForm()
    if request.method == 'POST':
        int_features = request.form.to_dict()
        df = pd.DataFrame(int_features,index=[0])
        trans = transformer.transform(df)
        prediction = model.predict(trans)
        prediction = (prediction>0.20)


    loan = ' Approved ' if prediction == True else ' Rejected '
    return render_template('indextrans.html', prediction_text='Loan status $ {}'.format(loan),form=form)


if __name__ == '__main__':
    app.run(debug=True)
