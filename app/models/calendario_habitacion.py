from ..extensions import db
from datetime import date, datetime
from typing import List

class CalendarioHabitacion(db.Model):
    """
    Calendar for a room. Maintains blocked dates and convenience methods for availability.
    For simplicity we store blocked/occupied date ranges as list of dicts, but in production
    it's preferable to use a dedicated Booking table with start/end dates (we have Reserva).
    """
    __tablename__ = "calendarios"

    id = db.Column(db.Integer, primary_key=True)
    habitacion_id = db.Column(db.Integer, db.ForeignKey("habitaciones.id"), unique=True)
    # We'll store occupancy periods as list of objects: [{"start":"YYYY-MM-DD","end":"YYYY-MM-DD"}, ...]
    ocupaciones = db.Column(db.JSON, default=[])

    def is_available(self, start_date: date, end_date: date) -> bool:
        """Returns True if no ocupacion overlaps the requested range."""
        from ..utils.dates import ranges_overlap
        for occ in self.ocupaciones:
            occ_start = date.fromisoformat(occ["start"])
            occ_end = date.fromisoformat(occ["end"])
            if ranges_overlap(occ_start, occ_end, start_date, end_date):
                return False
        return True

    def block_dates(self, start_date: date, end_date: date):
        """Add an occupied period to the calendar."""
        self.ocupaciones.append({
            "start": start_date.isoformat(),
            "end": end_date.isoformat()
        })

    def release_dates(self, start_date: date, end_date: date):
        """
        Remove a blocked period that exactly matches (or partially matches).
        For demo purposes we'll remove entries that fully match the start/end.
        """
        new_ocup = []
        for occ in self.ocupaciones:
            if not (occ["start"] == start_date.isoformat() and occ["end"] == end_date.isoformat()):
                new_ocup.append(occ)
        self.ocupaciones = new_ocup

    def to_dict(self):
        return {
            "id": self.id,
            "habitacion_id": self.habitacion_id,
            "ocupaciones": self.ocupaciones
        }
