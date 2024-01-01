from flask import Flask, render_template, url_for, request, redirect

application = Flask(__name__)

urls = {}

@application.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        default_url = request.form["default_link"];
        new_path = request.form["new_path"];
        
        if new_path not in urls.keys():
            urls[new_path] = default_url
            return f"Seu link: {request.url_root}{new_path}"
        
        else:
            return "Caminho Destino não disponível, tente outro"
        
    else:
        return render_template("homepage.html")
    
@application.route("/<new_path>")
def redirect(new_path):
    default_url = urls.get(new_path)
    
    if default_url:
        return redirect(default_url)
    else:
        return "Página não encontrada", 404

if __name__ == '__main__':
    application.run(debug=True) 