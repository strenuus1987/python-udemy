from flask import Flask #import Flask class from flask library
from flask import render_template #import render_template methon wich accesses the html file store in our library and then display it on requested url

app = Flask(__name__) #instatiating this object to Flask class

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2017,1,1)
    end = datetime.datetime(2017,12,31)
    df = data.DataReader(name="AAPL", data_source="google", start=start, end=end)

    def inc_def(c, o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value

    df["Status"] = [inc_def(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open+df.Close)/2
    df["Height"] = abs(df.Open - df.Close)

    p = figure(x_axis_type='datetime', width=1200, height=800)
    p.title.text = "Apple stocks 2017 by Google"
    p.grid.grid_line_alpha = 0.5

    hours_12 = 12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low)
    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"], hours_12, df.Height[df.Status == "Increase"],
           fill_color="#C6FFB3", line_color="black")
    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"], hours_12, df.Height[df.Status == "Decrease"],
           fill_color="#FF3333", line_color="black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files
    cdn_css = CDN.css_files

    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js[0],
    cdn_css=cdn_css[0])

@app.route('/') #decorator for root page
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

#name of the current script is __main__ when we execute it.
#If we import webapp.py and then execute the name will be __webapp__
if __name__=="__main__":
    app.run(debug=True)
