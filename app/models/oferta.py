from ..extensions import db
from datetime import date, datetime
from typing import Optional

class Oferta(db.Model):
    """
    Promotional offer associated with a hotel. Offers can be percentage discounts.
    """
    __tablename__ = "ofertas"

    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=False)
    descripcion = db.Column(db.String(300))
    tipo = db.Column(db.String(50))  # ej. 'temporada', 'paquete'
    descuento = db.Column(db.Float, default=0.0)  # fraction: 0.1 == 10%
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_applicable(self, start_date: date, end_date: date) -> bool:
        """Return True if offer overlaps the booking dates."""
        # If dates are None, consider not applicable
        if not self.fecha_inicio or not self.fecha_fin:
            return False
        # overlap check
        return not (end_date < self.fecha_inicio or start_date > self.fecha_fin)

    def to_dict(self):
        return {
            "id": self.id,
            "hotel_id": self.hotel_id,
            "descripcion": self.descripcion,
            "tipo": self.tipo,
            "descuento": self.descuento,
            "fecha_inicio": self.fecha_inicio.isoformat() if self.fecha_inicio else None,
            "fecha_fin": self.fecha_fin.isoformat() if self.fecha_fin else None,
        }
