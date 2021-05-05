# This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle
# import logging
# from logging import Formatter, FileHandler

print("Test")
print("Test 2")
print(os.getcwd())
path = os.getcwd()

with open('Models/lr.sav', 'rb') as f:
    logistic = pickle.load(f)

with open('Models/rf.sav', 'rb') as f:
    randomforest = pickle.load(f)


def get_predictions(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,req_model):
    mylist = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    mylist = [float(i) for i in mylist]
    vals = [mylist]

    if req_model == 'Logistic':
        #print(req_model)
        return logistic.predict(vals)[0]

    elif req_model == 'RandomForest':
        #print(req_model)
        return randomforest.predict(vals)[0]
    else:
        return "Cannot Predict"
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']
        req_model = request.form['req_model']


        target = get_predictions(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal, req_model)

        if target==1:
            have_disease = 'Customer is likely to have heart disease'
        else:
            have_disease = 'Customer is unlikely to have heart disease'

        return render_template('home.html', target = target, have_disease = have_disease)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
