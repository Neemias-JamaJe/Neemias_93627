from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "123"  

# ---------------------------- CONEXÃO COM MYSQL ----------------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="loja_nemo"
    )

# ---------------------------- ROTA LOGIN ----------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        db = conectar()
        cursor = db.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND senha=%s",
                       (usuario, senha))
        usuario_db = cursor.fetchone()

        if usuario_db:
            session["usuario"] = usuario
            return redirect("/tabela")
        else:
            return "Usuário ou senha incorretos!"

    return render_template("login.html")

# ---------------------------- ROTA CADASTRAR USUÁRIO ----------------------------
@app.route("/cadastro_usuario", methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]

        db = conectar()
        cursor = db.cursor()

        cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)",
                       (usuario, senha))
        db.commit()

        return redirect("/")

    return render_template("cadastro_usuario.html")

# ---------------------------- ROTA CADASTRAR PRODUTO ----------------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro_produto():
    if "usuario" not in session:
        return redirect("/")

    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        quantidade = request.form["quantidade"]

        db = conectar()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO produtos (nome, preco, quantidade)
            VALUES (%s, %s, %s)
        """, (nome, preco, quantidade))

        db.commit()
        return redirect("/tabela")

    return render_template("cadastrar.html")

# ---------------------------- ROTA TABELA ----------------------------
@app.route("/tabela")
def tabela():
    if "usuario" not in session:
        return redirect("/")

    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    return render_template("tabela.html", produtos=produtos)

# ---------------------------- ROTA SAIR ----------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# ---------------------------- RODAR SERVIDOR ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
