"""
Simple payment service for demonstration. In production integrate with a real gateway.
"""
from ..models.pago import Pago
from ..extensions import db

class PaymentService:
    @staticmethod
    def process_payment(reserva_id: int, amount: float, metodo: str, reference: str = None) -> Pago:
        """
        Simulate processing a payment. Create a Pago record and mark as confirmed.
        """
        pago = Pago(reserva_id=reserva_id, monto=amount, metodo=metodo)
        pago.mark_confirmed(reference or f"REF-{reserva_id}-{int(pago.monto*100)}")
        db.session.add(pago)
        db.session.flush()  # persist temporarily to get id if needed
        return pago

    @staticmethod
    def refund_payment(pago: Pago, reason: str = None) -> Pago:
        """
        Simulate refunding a payment. Marks pago as 'reembolsado'.
        """
        pago.mark_refunded(reference=f"REFUND-{pago.id}")
        db.session.add(pago)
        db.session.flush()
        return pago
