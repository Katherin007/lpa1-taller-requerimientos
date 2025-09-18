from ..extensions import db
from datetime import datetime
from typing import Optional

class Hotel(db.Model):
    """
    Hotel model.

    A hotel contains many rooms (Habitacion) and offers. It stores general
    information used to list the property.
    """
    __tablename__ = "hotels"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    direccion = db.Column(db.String(300), nullable=False)
    telefono = db.Column(db.String(50))
    correo = db.Column(db.String(150))
    ubicacion = db.Column(db.String(200))
    descripcion_servicios = db.Column(db.Text)
    estado = db.Column(db.String(30), default="activo")  # activo/inactivo
    fotos = db.Column(db.JSON, default=[])  # lista de URLs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    habitaciones = db.relationship("Habitacion", backref="hotel", lazy="dynamic")
    ofertas = db.relationship("Oferta", backref="hotel", lazy="dynamic")
    comentarios = db.relationship("Comentario", backref="hotel", lazy="dynamic")

    def activate(self):
        """Activate the hotel so it can accept reservations."""
        self.estado = "activo"

    def deactivate(self):
        """Deactivate the hotel (e.g., for renovations)."""
        self.estado = "inactivo"

    def average_rating(self) -> Optional[float]:
        """Return average rating across hotel's comments; None if no comments."""
        comments = self.comentarios.all()
        if not comments:
            return None
        total = sum([c.calificacion for c in comments if c.calificacion is not None])
        return total / len(comments)

    def to_dict(self) -> dict:
        """Serialize hotel to dictionary."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "correo": self.correo,
            "ubicacion": self.ubicacion,
            "descripcion_servicios": self.descripcion_servicios,
            "estado": self.estado,
            "fotos": self.fotos,
            "average_rating": self.average_rating(),
        }
