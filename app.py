import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from forms import SignupForm, SigninForm
from holidays import get_holidays_by_year
from models import User, Plan,  db
from pathlib import Path
from pico_placa import scrap_pyphoy_page
from send_email import send_email
from sqlalchemy.exc import IntegrityError
from weather import get_city_lat_long


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
if not app.config['SECRET_KEY']:
    raise RuntimeError("SECRET_KEY is not set (check your .env file)")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iguanaplan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG'] = True

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'signin_form'


@login_manager.user_loader
def load_user(user_id):
    print('🌵 Loading user ID', user_id)
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def index():
    user_name = current_user.name if current_user.is_authenticated else "Jon Doe"
    
    print(f'current_user --> {current_user}')
    return render_template('index.html', user_name=user_name, plans=current_user.plans)
    # return redirect(url_for('signup_form'))
    # return redirect(url_for('signin_form'))


@app.route('/signin', methods=["GET", "POST"])
def signin_form():
    form = SigninForm()
    action = request.form.get("action")
    
    if action == 'signup':
        return redirect(url_for('signup_form'))
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password_hash(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        
        form.password.errors.append('Incorrect email or password. Try again.')
    
    return render_template('signin_form.html', form = form)


@app.route('/signup', methods=["GET", "POST"])
def signup_form():
    
    form = SignupForm()
    action = request.form.get("action")
    
    if action == 'signin':
        return redirect(url_for("signin_form"))
    
    if form.validate_on_submit():       
        new_user = User(name=form.name.data, email=form.email.data)
        new_user.set_password_hash(form.password.data)
        db.session.add(new_user)
        
        try:
            db.session.commit()
            return redirect(url_for('signin_form'))
        except IntegrityError as e:
            print(f"🚩 An error occurred: {e.args[0]}")
            db.session.rollback()
            form.email.errors.append('Email already exists.')
        
    return render_template('signup_form.html', form = form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    print(f'🚀 User logged out successfully')
    return redirect(url_for('signin_form'))


@app.route('/add_plan', methods=['POST'])
@login_required
def add_plan():
    description = 'This is a test'
    new_plan = Plan(user_id=current_user.id, description=description)
    db.session.add(new_plan)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_all_plans', methods=["GET"])
def delete_all_plans():
    db.session.query(Plan).delete()
    db.session.commit()
    return redirect(url_for('index'))



@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")


def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)


# # # from flask import Flask, redirect, render_template
# # # from blueprints.books.routes import books_bp
# # # from blueprints.movies.routes import movies_bp
# # # from models.movies import Movie
# # # from models.books import Book


# # # app = Flask(__name__)
# # # app.config['ENV'] = "development"
# # # app.config['DEBUG'] = True

# # # app.register_blueprint(books_bp, url_prefix = '/books')
# # # app.register_blueprint(movies_bp, url_prefix = '/movies')


    
    # scrap_pyphoy_page("Medellín")
    # while True:
    #     clean_terminal()
    #     city = input('Input a City >_ ')
    #     if city == 'q':
    #         break
    #     scrap_pyphoy_page(city)
        



    # send_email()


    # print(get_holidays_by_year(2025)
    # today = datetime.now().date().strftime('%Y-%m-%d')
    # print(f'today --> {today}')
    # for holiday in get_holidays_by_year(2025):
    #     print(f'holidays --> {holiday['date'].split('T')[0]}')
    #     if(today == holiday['date'].split('T')[0]):
    #         print('Today is holiday!!! But not for me ')
    #         print(f'The reason: {holiday['name']}')
    # app.run(debug=True)




    # city_data = get_city_data('Manizales')
    # print(city_data['results'][0]['geometry'])
    # while True:
    #     clean_terminal()
    #     city = input('Input a City >_ ').lower()
    #     if city == 'q':
    #         break
    #     city_lat_long = get_city_lat_long(city)
    #     print(f'\nlat_long --> {city_lat_long}')
    #     input('\nPress any key to continue >_ ')