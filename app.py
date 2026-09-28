from flask import Flask, render_template

app = Flask(__name__)

@app.route("/python")
#http://127.0.0.1:5000/python 로 해야 함
#@app.route("/")
def python():
  return render_template("python.html")
#def hello_world():
  #return "Hello World! flask ㅁㅁ"
  #return render_templates("index.html")

if __name__ == "__main__":
  app.run(debug=True) #개발자모드
  #app.run() #다른컴퓨터에 렌트했을때 이렇게올리세요 