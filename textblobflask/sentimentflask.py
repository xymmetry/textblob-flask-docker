from flask import Flask, render_template, request
import textblobanalysis


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = textblobanalysis.get_sentiment(text, rnge=0.1)
        return render_template('sentiment.html', text=text, sentiment=sentiment)
    return render_template('sentiment.html')

if __name__ == "__main__" :
    app.run(debug=True)