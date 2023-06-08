from flask import Flask, render_template, request, redirect, session

# Creating the flask application
app = Flask(__name__)

# Secret is used to sign or encrypt data in session storage
app.secret_key = "skdjfhnal;e3iadslkfhji3f3few20"

# Creating a route for '/'
@app.route('/')
def home():
    # render/display the index.html file
    return render_template("index.html")

# ++ specifying the HTTP method used as POST
@app.route('/submit_data', methods=['POST'])
def submit_info():
    
    # Checking if a key of 'list_of_entries' exists in session storage
    if not 'list_of_entries' in session:
        session['list_of_entries'] = []
    
    # Copying data from session storage to a variable called list
    list = session['list_of_entries']
    
    # Appending data to the variable
    list.append(request.form)
    
    # Updating the session storage with the list
    session['list_of_entries'] = list
    
    print(list)

    # Redirecting to the another route
    return redirect(f'/display_info')

@app.route('/display_info')
def display_info():
    return render_template("display_info.html", list = session['list_of_entries'])

@app.route('/clear_session')
def clear():
    
    # Clearing session storage (ALL OF IT)
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
