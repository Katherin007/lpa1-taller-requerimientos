from ..extensions import db
from datetime import datetime, date
from typing import Optional

class Reserva(db.Model):
    """
    Reservation model. Links cliente, habitacion, pago and cancellation policy.
    """
    __tablename__ = "reservas"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    habitacion_id = db.Column(db.Integer, db.ForeignKey("habitaciones.id"), nullable=False)
    politica_id = db.Column(db.Integer, db.ForeignKey("politicas_cancelacion.id"), nullable=True)
    pago = db.relationship("Pago", uselist=False, backref="reserva")
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    estado = db.Column(db.String(50), default="pendiente")  # pendiente, confirmada, cancelada, finalizada
    total = db.Column(db.Float, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    politica = db.relationship("PoliticaCancelacion", backref="reservas")

    def validate_availability(self) -> bool:
        """Check the room's calendar for availability."""
        cal = self.habitacion.calendario
        if not cal:
            # If no calendar exists, assume available
            return True
        return cal.is_available(self.fecha_inicio, self.fecha_fin)

    def confirm(self, payment: "Pago"):
        """
        Confirm reservation: link payment, block calendar and set state to confirmada.
        Payment should already be 'confirmado'.
        """
        if payment.estado != "confirmado":
            raise ValueError("Payment not confirmed")
        # block dates
        cal = self.habitacion.calendario
        if cal:
            if not cal.is_available(self.fecha_inicio, self.fecha_fin):
                raise ValueError("Room not available for requested dates")
            cal.block_dates(self.fecha_inicio, self.fecha_fin)
        self.estado = "confirmada"
        self.pago = payment

    def cancel(self, reason: str = None) -> float:
        """
        Cancel reservation and compute refund based on linked policy.
        Returns refund amount (0 if none). Also sets estado to 'cancelada'.
        """
        refund_amount = 0.0
        if self.politica:
            refund_amount = self.politica.calculate_refund(self.total)
        # release dates from calendar
        cal = self.habitacion.calendario
        if cal:
            cal.release_dates(self.fecha_inicio, self.fecha_fin)
        self.estado = "cancelada"
        # payment marking and actual refund processing should be handled by PaymentService
        return refund_amount

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "habitacion_id": self.habitacion_id,
            "fecha_inicio": self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            "fecha_fin": self.fecha_fin.isoformat() if self.fecha_fin else None,
            "estado": self.estado,
            "total": self.total,
            "fecha_creacion": self.fecha_creacion.isoformat()
        }
