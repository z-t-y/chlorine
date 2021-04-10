#-*- coding:utf-8 -*-

from flask import Flask, render_template, request, url_for, redirect
from chlorine.chlorine import Translate,v
import time

app = Flask(__name__)

@app.route('/api')
def api():
    if request.args['word'] is not None:
        word = request.args['word']

        print(str(time.time())+'    word='+word+'    trans='+Translate(word).translate(), file=log)
        return {word: Translate(word).translate()}

@app.route('/',methods=('GET','POST'))
def index() -> 'html':
    if request.method == 'POST':
        word = request.form['input']
        return redirect(url_for('trans',word=word))
    return render_template('base.html',
                        the_title='首页',
                        word='Welcome to Fluorine!',
                        word_trans='在页面最下方输入内容，返回结果！',
                        text_content='你好，我们是Fluorine团队！',
                        )

@app.route('/trans',methods=('GET','POST'))
def trans() -> 'html':
    try:
        word_ = request.args['word']
    except:
        return redirect(url_for('index'))

    if request.method == 'POST':
        word = str(request.form['input'])
        return redirect(url_for('trans',word=word))
    return render_template('base.html',
                        the_title='转换',
                        word='转换结果',
                        word_trans='转换结果：'+Translate(word_).translate(),
                        text_content=word_,
                        )

if __name__ == '__main__':
    app.run(debug=True)