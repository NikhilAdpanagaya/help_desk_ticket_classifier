from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__, template_folder='./templates')
# model = pickle.load(open("model.pkl", "rb"))
# #The logistic regression model was used as it was determined to be the best fit based on evaluation.
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

FASTAPI_URL = "http://127.0.0.1:8000/predict/"


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    ticket_text = ""
    if request.method == 'GET':
        return render_template('index.html', prediction=None)
    if request.method == 'POST':
        ticket_text = request.form['text'].strip()
        if ticket_text:
            try:
                response = requests.post(FASTAPI_URL, json={"text":ticket_text})
                if response.status_code== 200:
                    data = response.json()
                    prediction = data.get('prediction', '')
                else:
                    prediction = f"Error occurred: {response.status_code}"
            except Exception as e:
                prediction = f"Error in loading FAST API Url: {e}"
        else:
            prediction = 'Please enter a valid description.'

    return render_template('index.html', prediction=prediction, ticket_text =ticket_text)


if __name__ == '__main__':
    app.run(debug=True)
