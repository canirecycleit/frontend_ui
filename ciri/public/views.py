# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
import ciri.settings as settings
import requests
from ciri.public.forms import UploadImageForm
from flask import Blueprint, render_template, request

blueprint = Blueprint("public", __name__, static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    return render_template("public/home.html")


@blueprint.route("/upload", methods=["GET", "POST"])
def upload():
    """Upload new image & category."""
    form = UploadImageForm()

    if request.method == "POST" and form.validate_on_submit():
        # Handle api call to upload image:
        img = form.file.data.stream

        payload = {"file": img}
        result = requests.post(
            f"{settings.API_ENDPOINT}/image/upload?category={form.category.data}",
            files=payload,
        )

        # TODO: Validate success

        return render_template("public/success_upload.html", form=form)

    return render_template("public/upload.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    return render_template("public/about.html")
