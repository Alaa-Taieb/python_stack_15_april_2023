from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    items = ['Item 1','Item 2', 'Item 3', 'Item 4']
    return render_template('home.html', title="Neighbor Home", list=items)

@app.route('/about')
def about():
    return "This is the about page!"

@app.route('/contact')
def contact():
    return "This is the contact page!"

@app.route('/user/<username>')
def user_profile(username):
    return f"Hello {username} to our page!"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Showing Post: {post_id}"

@app.route('/post/<string:post_id>')
def show_error(post_id):
    return f"{post_id} is not an integer!"

if __name__ == "__main__":
    app.run(debug=True)