## 📌 Entidades identificadas

1. **Hotel**

   * idHotel, nombre, dirección, teléfono, correo, ubicación, descripciónServicios, estado, fotos

2. **Habitación**

   * idHabitación, tipo, descripción, precio, serviciosIncluidos, capacidadMáxima, estado, fotos

3. **CalendarioHabitación**

   * idCalendario, fechasDisponibles, fechasOcupadas

4. **Oferta**

   * idOferta, descripción, tipo, descuento, vigencia

5. **Reserva**

   * idReserva, fechaInicio, fechaFin, estado, total, fechaCreación

6. **Cliente**

   * idCliente, nombre, teléfono, correo, dirección

7. **Pago**

   * idPago, monto, fecha, método, estado

8. **PolíticaCancelación**

   * idPolítica, condiciones, penalidad, reembolsoPermitido

9. **Comentario**

   * idComentario, texto, calificación, fecha

---

## 📊 Relaciones principales

* Un **Hotel** tiene muchas **Habitaciones**.
* Un **Hotel** puede tener muchas **Ofertas**.
* Una **Habitación** pertenece a un **Hotel**.
* Una **Habitación** tiene un **CalendarioHabitación**.
* Una **Habitación** puede estar asociada a muchas **Reservas**.
* Una **Reserva** pertenece a un **Cliente** y a una **Habitación**.
* Una **Reserva** genera un **Pago** y puede estar sujeta a una **PolíticaCancelación**.
* Un **Cliente** puede hacer muchas **Reservas**.
* Un **Cliente** puede dejar muchos **Comentarios** asociados a una **Habitación** o un **Hotel**.

---

## 🎨 Diagrama de clases en Mermaid

```mermaid
classDiagram
    class Hotel {
        +idHotel: int
        +nombre: string
        +direccion: string
        +telefono: string
        +correo: string
        +ubicacion: string
        +descripcionServicios: string
        +estado: string
        +fotos: string[]
    }

    class Habitacion {
        +idHabitacion: int
        +tipo: string
        +descripcion: string
        +precio: float
        +serviciosIncluidos: string
        +capacidadMaxima: int
        +estado: string
        +fotos: string[]
    }

    class CalendarioHabitacion {
        +idCalendario: int
        +fechasDisponibles: date[]
        +fechasOcupadas: date[]
    }

    class Oferta {
        +idOferta: int
        +descripcion: string
        +tipo: string
        +descuento: float
        +vigencia: date
    }

    class Reserva {
        +idReserva: int
        +fechaInicio: date
        +fechaFin: date
        +estado: string
        +total: float
        +fechaCreacion: date
    }

    class Cliente {
        +idCliente: int
        +nombre: string
        +telefono: string
        +correo: string
        +direccion: string
    }

    class Pago {
        +idPago: int
        +monto: float
        +fecha: date
        +metodo: string
        +estado: string
    }

    class PoliticaCancelacion {
        +idPolitica: int
        +condiciones: string
        +penalidad: float
        +reembolsoPermitido: boolean
    }

    class Comentario {
        +idComentario: int
        +texto: string
        +calificacion: int
        +fecha: date
    }

    %% Relaciones
    Hotel "1" --> "many" Habitacion
    Hotel "1" --> "many" Oferta
    Habitacion "1" --> "1" CalendarioHabitacion
    Habitacion "1" --> "many" Reserva
    Reserva "1" --> "1" Cliente
    Reserva "1" --> "1" Pago
    Reserva "1" --> "1" PoliticaCancelacion
    Cliente "1" --> "many" Comentario
    Habitacion "1" --> "many" Comentario
    Hotel "1" --> "many" Comentario
```
