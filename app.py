from flask import Flask, render_template, request, redirect, url_for, flash
from connector import PostgresConnector

app = Flask(__name__)
app.secret_key = "Ale_dem"
manager = PostgresConnector()


@app.route('/', methods=['GET', 'POST'])
def get_index():
    books = manager.get_data()
    return render_template('index.html', books=books)


@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        Author = request.form['author']
        Title = request.form['title']
        Publication_date = request.form['publication_date']
        Language = request.form['language']
        Programming_language = request.form['programming_language']
        manager.insert_data(Author=Author,
                            Title=Title,
                            Publication_date=Publication_date,
                            Language=Language,
                            Programming_language=Programming_language)
    return redirect(url_for('get_index'))


@app.route('/edit/<id_>', methods=['POST', 'GET'])
def edit_book(id_):
    books = manager.edit_data(id_)
    return render_template('edit.html', books=books[0])


@app.route('/update/<id_>', methods=['POST'])
def update_book(id_):
    if request.method == 'POST':
        Author = request.form['author']
        Title = request.form['title']
        Publication_date = request.form['publication_date']
        Language = request.form['language']
        Programming_language = request.form['programming_language']
        manager.update_data(Author=Author,
                            Title=Title,
                            Publication_date=Publication_date,
                            Language=Language,
                            Programming_language=Programming_language,
                            id_=id_)
        flash('Book updated successfully')
        return redirect(url_for('get_index'))


@app.route('/delete/<string:id_>', methods=['POST', 'GET'])
def delete_data(id_):
    manager.delete_data(id_)
    flash('Book was successfully removed')
    return redirect(url_for('get_index'))


if __name__ == '__main__':
    app.run(debug=True)
