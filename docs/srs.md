# 📄 Documento de Especificación de Requerimientos de Software (SRS)

**Sistema de Gestión de Reservas Hoteleras**

---

## 1. Introducción

### 1.1 Propósito

El propósito de este documento es definir de manera clara, completa y verificable los requerimientos funcionales y no funcionales del **Sistema de Gestión de Reservas Hoteleras (SGRH)**. Este sistema permitirá a hoteles registrar sus servicios, administrar habitaciones y reservas, gestionar pagos y políticas de cancelación, así como ofrecer a los clientes una plataforma confiable para realizar reservas en línea.

### 1.2 Alcance

El sistema proporcionará funcionalidades para:

* Administradores de hoteles: gestión de hoteles, habitaciones, precios, disponibilidad, políticas de pago y cancelación.
* Clientes: búsqueda, consulta y reserva de habitaciones, registro de datos personales, consulta de disponibilidad, calificaciones y comentarios.
* Gestión de procesos asociados: manejo de reembolsos, promociones y control de estados de hoteles y habitaciones.

El sistema será accesible vía web y deberá integrarse con pasarelas de pago seguras.

### 1.3 Definiciones, Acrónimos y Abreviaturas

* **SGRH**: Sistema de Gestión de Reservas Hoteleras.
* **Administrador**: Personal autorizado de un hotel para gestionar información y operaciones en el sistema.
* **Cliente**: Usuario que busca, consulta y realiza reservas en el sistema.
* **Reserva activa**: Reserva confirmada con pago procesado.
* **Política de cancelación**: Condiciones que determinan reembolsos o penalidades en caso de cancelación de reservas.

### 1.4 Referencias

* Entrevista con administradora turística y asistente del hotel (documento fuente: *entrevista.pdf*).
* Estándar IEEE 830 para especificación de requerimientos.

### 1.5 Visión General

El sistema será modular, incluyendo:

* Módulo de gestión de hoteles.
* Módulo de gestión de habitaciones.
* Módulo de reservas y pagos.
* Módulo de clientes.
* Módulo de opiniones y calificaciones.

---

## 2. Descripción General

### 2.1 Perspectiva del Producto

El sistema reemplazará los procesos manuales actuales de reservas por una plataforma digital centralizada, accesible en línea, integrando información de disponibilidad, pagos y políticas de los hoteles.

### 2.2 Funciones del Producto

* Registro y administración de hoteles y habitaciones.
* Gestión de precios, disponibilidad y ofertas.
* Proceso completo de reservas y pagos.
* Gestión de clientes y su historial.
* Recolección y visualización de calificaciones y comentarios.

### 2.3 Características de los Usuarios

* **Administrador del hotel**: Perfil con permisos para gestionar la información de hoteles, habitaciones, precios y políticas.
* **Cliente**: Usuario final que consulta, selecciona y paga por reservas de habitaciones.

### 2.4 Restricciones

* El sistema debe cumplir con la normativa de protección de datos vigente (ej. GDPR/Ley de Habeas Data).
* Las reservas deben formalizarse únicamente con pago confirmado.
* Solo hoteles y habitaciones en estado activo estarán disponibles para reservas.

### 2.5 Suposiciones y Dependencias

* Se asume que los hoteles proporcionarán información actualizada y veraz.
* El sistema dependerá de la disponibilidad de pasarelas de pago externas.

---

## 3. Requerimientos Específicos

### 3.1 Requerimientos Funcionales

**RF01 - Registro de hoteles**
El sistema debe permitir registrar hoteles con datos: nombre, dirección, teléfono, correo, ubicación geográfica, descripción de servicios y fotos.
*Criterio de aceptación:* los campos obligatorios deben completarse antes de guardar.

**RF02 - Estado del hotel**
El sistema debe permitir activar/inactivar hoteles, de forma que solo los activos estén disponibles para reservas.

**RF03 - Ofertas especiales**
El sistema debe permitir registrar promociones por temporada o paquetes especiales asociados a cada hotel.

**RF04 - Registro de habitaciones**
El sistema debe permitir registrar habitaciones con: tipo, descripción, precio, servicios incluidos, capacidad máxima, estado (activo/inactivo) y fotos.

**RF05 - Estados de habitaciones**
El sistema debe permitir marcar habitaciones como inactivas (mantenimiento, remodelación, limpieza). Habitaciones inactivas no deben poder reservarse.

**RF06 - Calendario de disponibilidad**
El sistema debe mostrar un calendario de cada habitación con fechas ocupadas y disponibles.

**RF07 - Gestión de precios variables**
El sistema debe permitir modificar precios por temporada, ocupación y políticas definidas por el hotel.

**RF08 - Reserva de habitaciones**
El sistema debe permitir que un cliente seleccione fechas y habitación disponible, confirmando la reserva mediante pago.

**RF09 - Condiciones de pago**
El sistema debe permitir configurar modalidades de pago (adelantado, pago al llegar, parcial).

**RF10 - Políticas de cancelación**
El sistema debe permitir configurar condiciones de cancelación y reembolso por hotel y tipo de habitación.

**RF11 - Gestión de reembolsos**
El sistema debe procesar automáticamente reembolsos según la política configurada.

**RF12 - Registro de clientes**
El sistema debe registrar clientes con: nombre, teléfono, correo electrónico y dirección.

**RF13 - Búsqueda de habitaciones**
El sistema debe permitir búsqueda por filtros combinables: fecha, ubicación, calificación y precio.

**RF14 - Detalle de habitación**
El sistema debe mostrar descripción, características, servicios, fotos, calificación y comentarios de cada habitación.

**RF15 - Registro de comentarios**
El sistema debe permitir que clientes registren calificaciones y comentarios al finalizar su estancia.

**RF16 - Calificación promedio**
El sistema debe calcular y mostrar la calificación promedio por habitación y por hotel.

---

### 3.2 Requerimientos No Funcionales

**RNF01 - Disponibilidad**
El sistema debe estar disponible en línea 24/7.

**RNF02 - Seguridad**
El sistema debe proteger datos personales y financieros mediante cifrado y control de accesos por roles.

**RNF03 - Usabilidad**
La interfaz debe ser intuitiva y permitir completar una reserva en máximo 5 pasos.

**RNF04 - Escalabilidad**
El sistema debe soportar múltiples hoteles, habitaciones y usuarios sin pérdida de rendimiento.

**RNF05 - Rendimiento**
Las búsquedas de habitaciones deben mostrar resultados en menos de 3 segundos.

**RNF06 - Verificabilidad**
Cada requerimiento debe contar con un caso de prueba asociado para validar su implementación.

---

## 4. Apéndices

* Fuente principal: entrevista con administradora turística y asistente del hotel (*entrevista.pdf*).
* Glosario de términos del sector turístico (opcional, para futuras versiones).


