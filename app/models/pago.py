from ..extensions import db
from datetime import datetime
from typing import Optional

class Pago(db.Model):
    """
    Payment model. In production a Payment gateway integration would be used.
    This model stores the payment record and status.
    """
    __tablename__ = "pagos"

    id = db.Column(db.Integer, primary_key=True)
    reserva_id = db.Column(db.Integer, db.ForeignKey("reservas.id"), nullable=True)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    metodo = db.Column(db.String(100))  # 'tarjeta', 'transferencia', 'payu', etc.
    estado = db.Column(db.String(50), default="pendiente")  # pendiente, confirmado, reembolsado, fallido
    referencia = db.Column(db.String(200))  # gateway reference id

    def mark_confirmed(self, reference: Optional[str] = None):
        """Mark payment as confirmed."""
        self.estado = "confirmado"
        if reference:
            self.referencia = reference

    def mark_failed(self, reason: str = None):
        """Mark payment as failed."""
        self.estado = "fallido"

    def mark_refunded(self, reference: Optional[str] = None):
        """Mark payment as refunded."""
        self.estado = "reembolsado"
        if reference:
            self.referencia = reference

    def to_dict(self):
        return {
            "id": self.id,
            "reserva_id": self.reserva_id,
            "monto": self.monto,
            "fecha": self.fecha.isoformat(),
            "metodo": self.metodo,
            "estado": self.estado,
            "referencia": self.referencia
        }
