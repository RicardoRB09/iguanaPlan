import os
from sqlalchemy.exc import IntegrityError
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv
from forms import SignupForm, SigninForm
from models import User, db
from datetime import datetime
from holidays import get_holidays_by_year
from weather import get_city_lat_long
from send_email import send_email
from pico_placa import scrap_pyphoy_page


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
if not app.config['SECRET_KEY']:
    raise RuntimeError("SECRET_KEY is not set (check your .env file)")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iguanaplan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['DEBUG'] = True

db.init_app(app)

@app.route('/')
def index():
    # return render_template('index.html')
    # return redirect(url_for('signup_form'))
    return redirect(url_for('signin_form'))

@app.route('/signin', methods=["GET", "POST"])
def signin_form():
    
    form = SigninForm()
    action = request.form.get("action")
    
    if action == 'signup':
        return redirect(url_for('signup_form'))
    
    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        print(f'Login data -->{user_email} - {user_password}')
    
    return render_template('signin_form.html', form = form)


@app.route('/signup', methods=["GET", "POST"])
def signup_form():
    
    form = SignupForm()
    action = request.form.get("action")
    
    if action == 'signin':
        return redirect(url_for("signin_form"))
    
    if form.validate_on_submit():
        user_name = form.name.data
        user_email = form.email.data
        user_password = form.password.data
        
        new_user = User(name=user_name, email=user_email, password=user_password)
        db.session.add(new_user)
        try:
            db.session.commit()
            return redirect(url_for('index'))
            
        except IntegrityError as e:
            print(f"🚩 An error occurred: {e.args[0]}")
            form.email.errors.append('Email already exists.')
            db.session.rollback()
        
        
    return render_template('signup_form.html', form = form)


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