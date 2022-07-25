from flask import Flask, render_template, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
import random
#############################
# APP FLASK CONFIGURATION
app = Flask(__name__)
app.secret_key = ".."
# DATABASE CONFIGURATION
uri = os.environ.get('MONGO_DB_URI', "mongodb://127.0.0.1")
client = MongoClient(uri)
db = client.meli
#############################


@app.route("/")
def meli_view():
    productos = list(db.productos.find())
    servicios = list(db.servicios.find())
    beneficios = list(db.beneficios.find())
    tiendas = list(db.tiendas.find())
    extras = list(db.extras.find())
    supermercado = list(db.supermercado.find())
    categorias = list(db.categorias.find())
    avisoPrincipal = db.avisoPrincipal.find()
    productos = db.productoNuevo.find()

    if not session.get('id'):
        session['id'] = random.randint(12345, 99999)
    return render_template("meli.html",
                           titulo="Mercado Libre 2.0 | by: Sr.Cthulhu ©",
                           productos=productos,
                           servicios=servicios,
                           beneficios=beneficios,
                           tiendas=tiendas,
                           extras=extras,
                           supermercado=supermercado,
                           categorias=categorias,
                           avisoPrincipal=avisoPrincipal,
                           id=session.get('id')
                           )


@app.route("/meli/aviso/<id>")
def meli_aviso_view(id):
    aviso = db.avisoPrincipal.find_one({'_id': ObjectId(id)})
    return render_template("meli_detalle.html", aviso=aviso)


@app.route("/meli/linkdecompra/<id>")
def meli_linkdecompra_view(id):

    linkdecompra = db.productoNuevo.find_one({'_id': ObjectId(id)})
    return render_template("meli_detalle.html", linkdecompra=linkdecompra)
