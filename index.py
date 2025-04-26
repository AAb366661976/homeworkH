from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def final():
    return render_template("final.html")  # 首頁直接渲染 final.html，並且可以套用 CSS

@app.route("/me")
def me():
    return render_template("my.html")     # 關於我

@app.route("/work")
def work():
    return render_template("work.html")   # 我的履歷

@app.route("/futuer")
def futuer():
    return render_template("futuer.html") # 關於資訊顧問

if __name__ == "__main__":
    app.run(debug=True)


