from flask import Flask, render_template, redirect, session, url_for, flash, request
from flask_wtf.csrf import CSRFProtect
from models import db, Fcuser
from forms import RegisterForm, LoginForm
import os
from DBDATA import cafedata, storedata

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        if error is None:
            session.clear()
            session['useremail'] = Fcuser.query.filter_by(useremail=form.useremail.data).first().useremail
            return redirect(url_for('main'))
    return render_template('sign.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        if not (Fcuser.query.filter_by(useremail=form.useremail.data).first()):
            fcuser = Fcuser(useremail=form.useremail.data,
                            password=form.password.data,
                            username=form.username.data)
            db.session.add(fcuser)
            db.session.commit()
            return '''
            <script> alert("회원가입 성공");
            location.href="/"
            </script>'''
        elif (Fcuser.query.filter_by(useremail=form.useremail.data).first()):
            error = "이미 존재하는 이메일입니다."
        else:
            error = "잘못된 접근입니다."
        flash(error)
    elif form.password.data != form.re_password.data:
        error = "비밀번호를 확인해주세요."
        flash(error)
    return render_template('signup.html', form=form)

@app.route('/signout')
def signout():
    session.pop('useremail', None)
    return '''
    <script> alert("로그아웃 하셨습니다.");
    location.href="/"
    </script>'''

@app.route('/start')
def start():
    if 'useremail' in session:
        store_lat = storedata.store_lat_lng_data()[0]
        store_lng = storedata.store_lat_lng_data()[1]

        cafe_lat = cafedata.cafe_lat_lng_data()[0]
        cafe_lng = cafedata.cafe_lat_lng_data()[1]

        return render_template('start.html',
                               store_lat=store_lat, store_lng=store_lng,
                               cafe_lat=cafe_lat, cafe_lng=cafe_lng)
    return '''
    <script> alert("로그인 필요!");
    location.href="/sign"
    </script>'''

@app.errorhandler(Exception)
def all_exception_handler(error):
    return redirect('#')

if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))
    dbfile = os.path.join(basedir, 'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'wcsfeufhwiquehfdx'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()

    app.run(debug=True, host='0.0.0.0')