
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

from flask import Flask, redirect, render_template


app = Flask(__name__)
app.config['ENV'] = "development"
app.config['DEBUG'] = True


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/myportfolio')
def myPortfolio():
    return redirect("https://www.ricardoracines.com")


if __name__ == '__main__':
    app.run(debug=True)
        
        

    
    
