from flask import Flask, request
app = Flask(__name__)

@app.route("/test", methods=["GET", "POST"])
def test():
    q = request.args.get("q", "") or request.form.get("q","")
    search = request.args.get("search", "") or request.form.get("search","")
    idp = request.args.get("id", "") or request.form.get("id","")

    html = f"""
    <html>
    <body>
        <p>You searched: {q}</p>
        <input value="{search}">
        <div {idp}>Test attribute-name</div>
    </body>
    </html>
    """
    return html

app.run(port=5000)
