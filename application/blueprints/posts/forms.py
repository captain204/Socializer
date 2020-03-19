from wtforms import (Form,
                     TextAreaField,
                     StringField, 
                     PasswordField,
                     HiddenField, 
                     validators, 
                     SubmitField)
from wtforms.validators import (ValidationError, 
                                DataRequired,  
                                EqualTo, 
                                Length, 
                                Optional)







class PostForm(Form):
    body = TextAreaField("Body",validators=[DataRequired(message=('Enter your post')),Length(1,256)])
    