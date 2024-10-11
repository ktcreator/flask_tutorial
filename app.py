from flask import Flask, render_template,jsonify

app = Flask(__name__)

# print(app)
# print(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Anlayst',
    'location':'Bengaluru',
    'salary':'Rs 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bengaluru'
    
  },
  {
    'id':1,
    'title':'Data Anlayst',
    'location':'Bengaluru',
    'salary':'Rs 10,00,000'
  }
]
@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS,company_name='KTC')

@app.route("/api/jobs")
def job():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
