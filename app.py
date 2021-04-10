from flask import Flask, request, render_template, abort
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from chlorine import Translate

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


class TranslateForm(FlaskForm):
    text = TextAreaField('在下方输入内容，返回结果', validators=[DataRequired()])
    submit = SubmitField()


@app.route('/api')
def api():
    word = request.args.get('word')
    if word is None:
        abort(400)
    return Translate(word).translate()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TranslateForm()
    if form.validate_on_submit():
        translate = Translate(form.text.data)
        return render_template('index.html', form=form, translated=translate.translate())
    form.text.data = '你好，我们是Fluorine团队！'
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
