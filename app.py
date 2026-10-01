from flask import Flask, render_template, request , send_file
from scrapper import search_incruit, work24
from file import save_to_csv
app = Flask(__name__)

def get_jobs(keyword):
  jobs = []
  for func in (search_incruit, work24):
    try:
      jobs += func(keyword)
    except Exception as e:
      print(f"{func.__name__} 오류: {e}")
  return jobs


@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  jobs = get_jobs(keyword)
  return render_template("search.html", keyword=keyword, jobs=enumerate(jobs))

@app.route("/file")
def file():
  keyword = request.args.get("keyword")
  jobs = get_jobs(keyword)
  save_to_csv(jobs)
  return send_file("downloads.csv", as_attachment=True)
if __name__ == "__main__":
  app.run(debug=True)