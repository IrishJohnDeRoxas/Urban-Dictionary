from flask import Flask, render_template
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os, utils

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

if __name__ == '__main__':
    app.run(debug=True)
    
load_dotenv()

class searchForm(FlaskForm):
    searchBar = StringField('string', validators=[DataRequired()])
    submit = SubmitField('Search')
    
@app.route('/', methods=['POST', 'GET'])
def index():
    form = searchForm()
    
    if form.validate_on_submit():
        query = form.searchBar.data
        searchQuery, definitions = utils.getDefinition(query)
        form.searchBar.data = ''
        return render_template('index.html',
                                form=form,
                                searchQuery=searchQuery,
                                definitions=definitions)
        
    return render_template('index.html',
                           form=form)
