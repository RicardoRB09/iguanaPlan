
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



# # # @app.route('/')
# # # def home():
# # #     return render_template('index.html')


# # # @app.route('/myportfolio')
# # # def myPortfolio():
# # #     return redirect("https://www.ricardoracines.com")


# # # if __name__ == '__main__':
# # #     Movie.delete_movie_database()
# # #     Movie.init_movies_database()
# # #     Book.delete_book_database()
# # #     Book.init_books_database()
# # #     app.run(debug=True)





import os
from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
from holidays import get_holidays_by_year
from weather import get_city_lat_long
from send_email import send_email
from pico_placa import scrap_pyphoy_page


app = Flask(__name__)
app.config['ENV'] = "development"
app.config['DEBUG'] = True


@app.route('/')
def index():
    # return render_template('index')
    # return redirect(url_for('signup_form'))
    return redirect(url_for('signin_form'))


@app.route('/signin', methods=["GET", "POST"])
def signin_form():
    if request.method == 'POST':
        button_value = request.form.get('signup-btn')   
        print('😄😄😄')
        if button_value == 'signup':           
            return redirect(url_for('signup_form'))
    
    return render_template('signin_form.html')


@app.route('/signup', methods=["GET", "POST"])
def signup_form():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        user_password = request.form['password']
            
        button_value = request.form.get('signup-btn')
        
        if button_value == 'Create an account':
            print(f'{user_name} - {user_email} - {user_password}')
            
        elif button_value == 'signin':
            print(f'sign in')
            return redirect(url_for('signin_form'))    
            
        next = request.args.get('next', None)
        if next:
            print('😂😂😂')
            return redirect(next)
        return redirect(url_for('index'))
        
    return render_template('signup_form.html')


@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")


def clean_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    
    app.run(debug=True)
    
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