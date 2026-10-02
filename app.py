from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Base de datos SQLite para la prueba
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///prueba.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Tabla de prueba
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(50), nullable=False)

def crear_datos_prueba():
    if Pedido.query.count() == 0:
        pedidos = [
            Pedido(estado="Pendiente"),
            Pedido(estado="Pendiente"),
            Pedido(estado="Pendiente"),
            Pedido(estado="En preparación"),
            Pedido(estado="En preparación"),
            Pedido(estado="Listo"),
            Pedido(estado="Listo"),
            Pedido(estado="Listo"),
            Pedido(estado="Listo"),
            Pedido(estado="Entregado"),
            Pedido(estado="Entregado")
        ]

        db.session.add_all(pedidos)
        db.session.commit()

@app.route("/")
def dashboard():

    pedidos = Pedido.query.all()

    estados = [
        "Pendiente",
        "En preparación",
        "Listo",
        "Entregado"
    ]

    cantidades = [
        sum(1 for pedido in pedidos if pedido.estado == "Pendiente"),
        sum(1 for pedido in pedidos if pedido.estado == "En preparación"),
        sum(1 for pedido in pedidos if pedido.estado == "Listo"),
        sum(1 for pedido in pedidos if pedido.estado == "Entregado")
    ]

    return render_template(
        "dashboard.html",
        estados=estados,
        cantidades=cantidades
    )


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
        crear_datos_prueba()

    app.run(debug=True)