# 📋 Listado de Requerimientos

## 1. Gestión de Hoteles

1. **Registro de hoteles**: El sistema debe permitir registrar un nuevo hotel con la siguiente información mínima: nombre, dirección, teléfono, correo electrónico, ubicación geográfica, descripción de servicios ofrecidos (restaurante, piscina, gimnasio, etc.) y fotos.
   *Criterio de aceptación:* al guardar el registro, los campos obligatorios deben estar completos y almacenarse en la base de datos.

2. **Gestión de estado del hotel**: El sistema debe permitir activar o desactivar un hotel (ej. por reformas), de manera que solo los hoteles activos puedan ser reservados.

3. **Gestión de ofertas especiales**: El sistema debe permitir registrar y asociar promociones a un hotel (ej. descuentos por temporada, paquetes especiales, servicios adicionales como estacionamiento o coworking).

---

## 2. Gestión de Habitaciones

4. **Registro de habitaciones**: El sistema debe permitir registrar habitaciones dentro de un hotel con información como: tipo, descripción, precio, servicios incluidos, capacidad máxima, estado (activo/inactivo) y fotos.

5. **Estados de las habitaciones**: El sistema debe permitir marcar habitaciones como inactivas (ej. por limpieza, mantenimiento, remodelación, desinfección). Mientras estén inactivas, no deben estar disponibles para reservas.

6. **Calendario de disponibilidad**: Cada habitación debe contar con un calendario que muestre fechas reservadas y disponibles para nuevos clientes.

7. **Gestión de precios variables**: El sistema debe permitir modificar el precio de una habitación según temporada, ocupación (cantidad de huéspedes dentro de la capacidad máxima) y políticas del hotel.

---

## 3. Gestión de Reservas y Pagos

8. **Reserva de habitaciones**: El sistema debe permitir que un cliente seleccione una habitación disponible en las fechas deseadas y formalice la reserva mediante el pago correspondiente.

9. **Condiciones de pago**: El sistema debe permitir que cada hotel configure sus condiciones de pago (pago completo por adelantado, pago al llegar, etc.).

10. **Condiciones de cancelación**: El sistema debe permitir configurar políticas de cancelación por hotel y tipo de habitación (reembolso completo, penalidad parcial, no reembolsable).

11. **Gestión de reembolsos**: El sistema debe procesar reembolsos de acuerdo con las políticas de cancelación configuradas por el hotel.

---

## 4. Gestión de Clientes

12. **Registro de clientes**: El sistema debe permitir registrar clientes con los siguientes datos: nombre completo, número de teléfono, correo electrónico y dirección.

13. **Búsqueda de habitaciones**: El sistema debe permitir a los clientes buscar habitaciones aplicando filtros por fecha, ubicación, calificación y precio, con posibilidad de combinarlos.

14. **Detalle de la habitación**: El sistema debe mostrar al cliente la información completa de la habitación seleccionada: descripción, características, servicios incluidos, fotos, calificación y comentarios de huéspedes anteriores.

---

## 5. Opiniones y Calificaciones

15. **Registro de comentarios**: El sistema debe permitir que los clientes, después de su estancia, dejen calificaciones y comentarios asociados a la habitación reservada.

16. **Cálculo de calificación promedio**: El sistema debe calcular y mostrar automáticamente la calificación promedio tanto a nivel de habitación como de hotel.

---

## 6. Requerimientos No Funcionales

17. **Disponibilidad**: El sistema debe estar disponible en línea 24/7 para clientes y administradores.

18. **Seguridad**: El sistema debe garantizar la protección de los datos personales y financieros de los clientes mediante cifrado y control de accesos por roles.

19. **Usabilidad**: La interfaz debe ser intuitiva y permitir que un cliente pueda realizar una reserva en no más de 5 pasos.

20. **Escalabilidad**: El sistema debe soportar el registro de múltiples hoteles, habitaciones y clientes sin necesidad de rediseño de la arquitectura.

21. **Verificabilidad**: Cada requerimiento debe tener asociado un caso de prueba que permita validar su cumplimiento.

