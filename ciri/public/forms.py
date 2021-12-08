# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import SubmitField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired


class UploadImageForm(FlaskForm):
    """Form for image and category upload."""

    class Meta:
        """Meta config."""

        csrf = False

    category = SelectField(
        "Image Category",
        id="image_category",
        validators=[DataRequired()],
        choices=[("trash", "Trash"), ("organic", "Organic"), ("test", "Test")],
    )

    file = FileField(
        "Image",
        validators=[FileRequired(), FileAllowed(["jpg", "jpeg"], "JPG files only.")],
    )

    submit = SubmitField("Submit")
