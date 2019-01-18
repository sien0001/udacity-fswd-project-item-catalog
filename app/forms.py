from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class AddItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    categories = SelectField(
        label="Categories",
        choices=[],
        validators=[DataRequired()]
    )
    submit = SubmitField("Submit")
