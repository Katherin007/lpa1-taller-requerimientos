from ..extensions import db
from datetime import datetime

class Cliente(db.Model):
    """
    Customer record.
    """
    __tablename__ = "clientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(150))
    direccion = db.Column(db.String(300))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reservas = db.relationship("Reserva", backref="cliente", lazy="dynamic")
    comentarios = db.relationship("Comentario", backref="cliente", lazy="dynamic")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion
        }
