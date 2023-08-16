from flask import Flask,render_template

app=Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/ht.jpg",
        "hero": "img/habit_tracker_bullet.jpg",
        "categories": ["python", "web"],
        "slug": "habit-tracker",
        "prod": "https://habit-tracker-av3s.onrender.com",
    },
    {
        "name": "Micro Blog app with Python and MongoDB",
        "thumb": "img/micro-blog.png",
        "hero": "img/mb.jpg",
        "categories": ["python", "web"],
        "slug": "micro-blog",
        "prod":"https://pthon-microblog.onrender.com",
    },
    {
        "name": "Youtube Clone with HTML and CSS",
        "thumb": "img/ut.jpg",
        "hero": "img/yt.jpg",
        "categories": ["HTML","CSS"],
        "slug": "youtube-clone",
        "prod":"https://shany-shan.github.io/youtube-clone/",

    },
]

slug_to_project = {project["slug"]: project for project in projects}

@app.route("/")
def home():
    return render_template("index.html",projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug in slug_to_project:
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])
