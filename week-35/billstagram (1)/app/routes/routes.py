from flask import Blueprint, redirect, render_template, session, send_from_directory, current_app
from app.models import User, Post, db
from app.forms import PostForm
from werkzeug.utils import secure_filename
import os


app_routes = Blueprint("app", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@app_routes.route('/')
def home():
    if 'home_views' in session:
        session['home_views'] = session['home_views'] + 1
    else:
        session['home_views'] = + 1
    # user = {
    #     "username" : "Biff",
    #     "bio" : "Definitely not Bill, definitely not.",
    #     "img": "img/profile.jpg"
    # }
    user = User.query.get(1).to_dict()
    posts = [post.to_dict() for post in Post.query.all()]
    return render_template("page.html", user=user, posts=posts)

@app_routes.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Add route for each user
@app_routes.route("/<int:id>")
def user_page(id):
    user = User.query.get(id).to_dict()
    posts = [post.to_dict() for post in Post.query.filter(Post.user_id == id).all()]
    return render_template("page.html", user=user, posts=posts)

@app_routes.route("/<int:id>/new", methods=["GET", "POST"])
def user_post(id):
    form = PostForm()
    if form.validate_on_submit():
        # image = form.image.data
        # image_path = 'static/img/' + image.filename
        # image.save(image_path)
        image_file = form.image.data
        if image_file:
            print(current_app.config["UPLOAD_FOLDER"])
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image_file.save(image_path)
        else:
            image_path = None
        new_post = Post(
            user_id=id,
            caption = form.caption.data,
            image="/img/"+filename,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(f"/{id}")
    user = User.query.get(id)
    return render_template("page.html", form=form, user=user)
