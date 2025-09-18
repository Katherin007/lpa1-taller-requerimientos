from ..extensions import db
from datetime import datetime

class PoliticaCancelacion(db.Model):
    """
    Cancellation policy model. Policies are associated to hotels or room types.
    """
    __tablename__ = "politicas_cancelacion"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150))
    condiciones = db.Column(db.Text)  # textual description
    penalidad = db.Column(db.Float, default=0.0)  # fraction to retain on cancel (0.1 => 10%)
    reembolso_permitido = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_refund(self, amount: float, now=None) -> float:
        """
        Return refund amount based on policy. For simplicity we ignore time-based rules here.
        """
        if not self.reembolso_permitido:
            return 0.0
        # retain penalidad fraction
        return round(amount * (1 - self.penalidad), 2)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "condiciones": self.condiciones,
            "penalidad": self.penalidad,
            "reembolso_permitido": self.reembolso_permitido
        }
