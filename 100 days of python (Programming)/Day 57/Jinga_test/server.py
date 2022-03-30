
from flask import Flask, render_template
import random
from datetime import datetime
import requests

'''
Jinga
https://jinja.palletsprojects.com/en/2.11.x/templates/
'''

app = Flask(__name__)
print(app)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.today().year
    return render_template("index.html", num=random_number, CURRENT_YEAR=year)

@app.route('/guess/<name>')
def guess(name):
    '''Gender'''
    response = requests.get(f"https://api.genderize.io/?name={name}")
    gender = response.json()['gender']
    '''Age'''
    response = requests.get(f"https://api.agify.io/?name={name}")
    age = response.json()['age']
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    '''Multi line code in HTML, look at blog.html'''
    print(num)
    blog_url = "https://api.npoint.io/82975389c85afb34e389"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)