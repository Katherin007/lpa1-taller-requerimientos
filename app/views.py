from flask import Blueprint, render_template
from app.models import Hotel, Habitacion, Cliente, Reserva

bp = Blueprint("web", __name__)

@bp.route("/")
def index():
    """
    Página de inicio con enlaces a las secciones principales.
    """
    return render_template("index.html")

@bp.route("/hoteles")
def listar_hoteles():
    """
    Lista todos los hoteles registrados.
    """
    hoteles = Hotel.query.all()
    return render_template("hotels.html", hoteles=hoteles)

@bp.route("/hotel/<int:hotel_id>")
def detalle_hotel(hotel_id):
    """
    Muestra detalles de un hotel específico y sus habitaciones.
    """
    hotel = Hotel.query.get_or_404(hotel_id)
    habitaciones = hotel.habitaciones.all()
    return render_template("hotel_detail.html", hotel=hotel, habitaciones=habitaciones)

@bp.route("/reservas")
def listar_reservas():
    """
    Lista todas las reservas registradas.
    """
    reservas = Reserva.query.all()
    return render_template("reservas.html", reservas=reservas)

@bp.route("/cliente")
def listar_cliente():
    """
    Lista todos los clientes registrados.
    """
    cliente = Cliente.query.all()
    return render_template("cliente.html", cliente=cliente)
