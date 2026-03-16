from flask import Flask,render_template,request
from scraper import scrape_news,summarise_news

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    summary=None
    if request.method=='POST':
        url=request.form.get('url')
        result=scrape_news(url)
        summary=summarise_news(result.markdown)
    return render_template('index.html',summary=summary)



if __name__=='__main__':
    app.run(debug=True)