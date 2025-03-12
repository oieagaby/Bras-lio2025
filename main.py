from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulação de banco de dados (usuário e senha fixos)
usuarios = {"admin": "1234", "aluno": "senha123"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario in usuarios and usuarios[usuario] == senha:
            return redirect(url_for("bem_vindo", nome=usuario))
        else:
            return "Login falhou! Tente novamente."

    return render_template("login.html")

@app.route("/bem-vindo/<nome>")
def bem_vindo(nome):
    return f"Bem-vindo, {nome}!"

if __name__ == "__main__":
    app.run(debug=True)
