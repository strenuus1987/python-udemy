from flask import Flask #import Flask class from flask library
from flask import render_template #import render_template methon wich accesses the html file store in our library and then display it on requested url

app = Flask(__name__) #instatiating this object to Flask class

@app.route('/') #decorator for root page
def home():
    return render_template("home.html")

@app.route('/about/') #decorator for root page
def about():
    return render_template("about.html")

#name of the current script is __main__ when we execute it.
#If we import webapp.py and then execute the name will be __webapp__
if __name__=="__main__":
    app.run(debug=True)
