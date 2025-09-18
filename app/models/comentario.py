from ..extensions import db
from datetime import datetime

class Comentario(db.Model):
    """
    Customer review/comment. Can be associated to a hotel and/or a specific room.
    """
    __tablename__ = "comentarios"

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotels.id"), nullable=True)
    habitacion_id = db.Column(db.Integer, db.ForeignKey("habitaciones.id"), nullable=True)
    texto = db.Column(db.Text)
    calificacion = db.Column(db.Integer)  # 1..5
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "cliente_id": self.cliente_id,
            "hotel_id": self.hotel_id,
            "habitacion_id": self.habitacion_id,
            "texto": self.texto,
            "calificacion": self.calificacion,
            "fecha": self.fecha.isoformat()
        }
