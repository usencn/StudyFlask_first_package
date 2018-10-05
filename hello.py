from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '这个是几乎不可能被别人知道的哈呢'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
	name = StringField('请问您的名字是什么？',validators=[DataRequired()])
	submit = SubmitField('提交')

@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name  != form.name.data:
			flash('貌似修改了名字哈')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.htm',form=form,name=session.get('name'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.htm',name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.htm'),404

if __name__ == '__main__':
	app.run(host='0.0.0.0',port='80')