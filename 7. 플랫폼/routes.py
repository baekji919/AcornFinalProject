from flask import Flask , render_template, redirect, session, url_for, flash, request
from flask_wtf.csrf import CSRFProtect
from models import db, Fcuser
from forms import RegisterForm, LoginForm
import os
from DBDATA import cafedata, storedata, hospitaldata, depstoredata, fooddata, schooldata, breaddata, cinemadata
import logging
import matplotlib.pyplot as plt

logging.basicConfig(filename='log/project.log', level=logging.DEBUG)
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

@app.route('/start', methods=['GET', 'POST'])
def start():
    from graph import schoolgrp, busgrp, securitygrp, publicgrp, convingrp
    if request.method == 'GET':
        value = request.args.get("value")

        schoolgrp.school(value)
        plt.cla()
        plt.clf()
        busgrp.traffic(value)
        plt.cla()
        plt.clf()
        securitygrp.security(value)
        plt.cla()
        plt.clf()
        publicgrp.public(value)
        plt.cla()
        plt.clf()
        convingrp.convin(value)
        plt.cla()
        plt.clf()

    if 'useremail' in session:
        store_lat = storedata.store_lat_lng_data()[0]
        store_lng = storedata.store_lat_lng_data()[1]

        cafe_lat = cafedata.cafe_lat_lng_data()[0]
        cafe_lng = cafedata.cafe_lat_lng_data()[1]

        hos_lat = hospitaldata.hosp_lat_lng_data()[0]
        hos_lng = hospitaldata.hosp_lat_lng_data()[1]

        dep_lat = depstoredata.deps_lat_lng_data()[0]
        dep_lng = depstoredata.deps_lat_lng_data()[1]

        food_lat = fooddata.food_lat_lng_data()[0]
        food_lng = fooddata.food_lat_lng_data()[1]

        brd_lat = breaddata.bread_lat_lng_data()[0]
        brd_lng = breaddata.bread_lat_lng_data()[1]

        cine_lat = cinemadata.cinema_lat_lng_data()[0]
        cine_lng = cinemadata.cinema_lat_lng_data()[1]

        sch_lat = schooldata.school_lat_lng_data()[0]
        sch_lng = schooldata.school_lat_lng_data()[1]
        return render_template('start.html',
                               store_lat=store_lat, store_lng=store_lng,
                               cafe_lat=cafe_lat, cafe_lng=cafe_lng,
                               hos_lat=hos_lat, hos_lng=hos_lng,
                               dep_lat=dep_lat, dep_lng=dep_lng,
                               food_lat=food_lat, food_lng=food_lng,
                               brd_lat=brd_lat, brd_lng=brd_lng,
                               cine_lat=cine_lat, cine_lng=cine_lng,
                               sch_lat=sch_lat, sch_lng=sch_lng,
                               value=value)
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