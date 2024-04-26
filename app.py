from flask import Flask, render_template
app =Flask(__name__)

FOODS = [
  {
    'id':1,
    'name':'tomato',
    'date':'2024-05-03',
    'quntity':'5'
  },
  {
    'id':2,
    'name':'potato',
    'date':'2024-05-07',
    'quntity':'18'
  },
  {
    'id':4,
    'name':'milk',
    'date':'2024-05-07',
    'quntity':'3'
  },
  {
    'id':5,
    'name':'bread',
    'date':'2024-05-05',
    'quntity':'5'
  }, 
  {
    'id':6,
    'name':'apple',
    'date':'2024-05-05',
    'quntity':'7'
  }, 
  {
    'id':7,
    'name':'orange',
    'date':'2024-05-04',
    'quntity':'8'
  },
  {
    'id':8,
    'name':'Banana',
    'date':'2024-05-04',
    'quntity':'20'
  },
  {
    'id':9,
    'name':'Egg',
    'date':'2024-05-05',
    'quntity':'15'
  },
  {
    'id':10,
    'name':'berry',
    'date':'2024-05-04',
    'quntity':'9'
  }
]

@app.route('/')
def hello_world():
    return render_template('home.html',foods=FOODS)
if __name__=='__main__':
  app.run(host='0.0.0.0',debug=True)
