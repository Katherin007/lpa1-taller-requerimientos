from ..extensions import db
from datetime import datetime
from typing import List, Optional

class Habitacion(db.Model):
    """
    Room (Habitacion) model.

    Each room belongs to a hotel and has a calendar, bookings and comments.
    """
    __tablename__ = "habitaciones"

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)  # ej. 'doble', 'suite'
    descripcion = db.Column(db.Text)
    precio_base = db.Column(db.Float, nullable=False)
    servicios_incluidos = db.Column(db.Text)
    capacidad_maxima = db.Column(db.Integer, default=1)
    estado = db.Column(db.String(30), default="activo")  # activo / inactivo
    fotos = db.Column(db.JSON, default=[])
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    calendario = db.relationship("CalendarioHabitacion", uselist=False, backref="habitacion")
    reservas = db.relationship("Reserva", backref="habitacion", lazy="dynamic")
    comentarios = db.relationship("Comentario", backref="habitacion", lazy="dynamic")

    def set_inactive(self, reason: str = None):
        """Mark room as inactive; reason is stored in logs or auditoria (outside)."""
        self.estado = "inactivo"

    def set_active(self):
        """Reactivate room."""
        self.estado = "activo"

    def calculate_price(self, start_date, end_date, occupancy: int = 1, ofertas: List = None) -> float:
        """
        Calculate total price for given range and occupancy. 'ofertas' is a list of Oferta objects.
        This is kept simple: price = precio_base * nights, then apply best discount available.
        """
        from ..utils.dates import days_between
        nights = days_between(start_date, end_date)
        base_total = self.precio_base * nights

        # Apply occupancy surcharge if occupancy > capacidad (should be validated elsewhere)
        if occupancy > self.capacidad_maxima:
            raise ValueError("Occupancy exceeds room capacity")

        discount = 0.0
        if ofertas:
            for o in ofertas:
                if o.is_applicable(start_date, end_date):
                    discount = max(discount, o.descuento or 0.0)

        total = base_total * (1 - discount)
        return round(total, 2)

    def to_dict(self) -> dict:
        """Serialize habitacion to dict."""
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "precio_base": self.precio_base,
            "servicios_incluidos": self.servicios_incluidos,
            "capacidad_maxima": self.capacidad_maxima,
            "estado": self.estado,
            "fotos": self.fotos
        }
