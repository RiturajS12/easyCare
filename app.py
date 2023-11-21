from flask import Flask,render_template,request
from dotenv import load_dotenv
import os
import openai

app = Flask(__name__)


load_dotenv()

openai.organization= "org-Z2IRBwP0NiTk6MvZbhj8J5uu"
openai.api_key = os.environ.get("OPENAI_API_KEY")
@app.route('/')
def intro():
    return render_template('index.html')
@app.route('/data',methods=["POST"])   
def data():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    disease = request.form.get("disease")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Hey I am {name} and I am {age} years old and I am a {gender} and I am suffering from {disease} and please provide me some cure"}
    ]
    )
    return render_template('chat.html',data={"solve":completion['choices'][0]['message']['content']})

if __name__=="__main__":
    app.run(debug=True,port=8000,host='0.0.0.0')
