from flask import Flask, request, render_template_string
app = Flask(__name__)

@app.route('/echo', methods=['GET','POST'])
def echo():
    q = request.values.get('q','')
    idv = request.values.get('id','')
    
    text_part = f"<div>Search: {q}</div>"
 
    attr_val = f'<input value="{idv}">'

    attr_name = f'<div {q}="1">attribute-name-sim</div>'
    return render_template_string(text_part + attr_val + attr_name)

if __name__ == '__main__':
    app.run(debug=True)
