from flask import Flask, render_template
import requests

BLOG_URL = "https://api.npoint.io/82975389c85afb34e389"
response = requests.get(url=BLOG_URL)
blog_data = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=blog_data )

@app.route('/post/<index>')
def show_post(index):
    blog_dict = blog_data['id'==index]
    title = blog_dict["title"]
    subtitle = blog_dict["subtitle"]
    body = blog_dict["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
