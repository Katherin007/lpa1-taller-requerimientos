from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import Hotel, Habitacion, Cliente, Reserva
from ..services.payment_service import PaymentService

bp = Blueprint("example", __name__)

@bp.route("/hotels", methods=["GET"])
def list_hotels():
    hotels = Hotel.query.all()
    return jsonify([h.to_dict() for h in hotels]), 200

@bp.route("/reserva", methods=["POST"])
def create_reserva():
    """
    Very simplified endpoint to create reservation and process payment.
    Expected JSON:
    {
        "cliente_id": 1,
        "habitacion_id": 2,
        "fecha_inicio": "2025-10-01",
        "fecha_fin": "2025-10-05",
        "metodo_pago": "tarjeta"
    }
    """
    payload = request.json
    cliente = Cliente.query.get(payload["cliente_id"])
    habitacion = Habitacion.query.get(payload["habitacion_id"])
    if not cliente or not habitacion:
        return jsonify({"error": "cliente or habitacion not found"}), 404

    # calculate price example
    from datetime import date
    start = date.fromisoformat(payload["fecha_inicio"])
    end = date.fromisoformat(payload["fecha_fin"])
    total = habitacion.calculate_price(start, end)

    reserva = Reserva(
        cliente_id=cliente.id,
        habitacion_id=habitacion.id,
        fecha_inicio=start,
        fecha_fin=end,
        total=total
    )

    # Validate availability
    if not reserva.validate_availability():
        return jsonify({"error": "room not available"}), 409

    db.session.add(reserva)
    db.session.flush()  # get reserva.id

    # Process payment (simulated)
    pago = PaymentService.process_payment(reserva.id, total, payload.get("metodo_pago", "tarjeta"))
    reserva.confirm(pago)

    db.session.add(reserva)
    db.session.commit()

    return jsonify({"reserva": reserva.to_dict(), "pago": pago.to_dict()}), 201
