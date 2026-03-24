# Sistema de Reservas de Cabañas (Django MVP)

Un sistema web completo de gestión de reservas para un complejo de cabañas o hotel boutique. Este proyecto es un MVP desarrollado para demostrar habilidades de desarrollo Full-Stack con Python, enfocándose en la lógica de negocio sólida y una experiencia de usuario fluida.

## Características Principales

* **Motor de Disponibilidad Inteligente:** El buscador filtra en tiempo real la capacidad de las cabañas y excluye propiedades que ya tienen reservas confirmadas o pendientes que chocan con las fechas seleccionadas por el usuario.
* **Persistencia de Búsqueda sin Sesiones Complejas:** El estado de la búsqueda (fechas, cantidad de personas) viaja de forma limpia a través de la URL mediante parámetros `GET`, garantizando que el usuario nunca pierda su intención de compra al navegar entre las vistas de resultados, detalles y el checkout final.
* **Frontend Moderno e Interactivo:** * Interfaz construida con **Bootstrap 5**.
  * Diseño de buscador con efecto *Glassmorphism*.
  * Galería de imágenes estilo *Bento Grid* integrada con `fslightbox` para una visualización inmersiva.
* **Panel Administrativo Completo:** Panel de control de Django (`/admin`) configurado con `Inlines` para subir múltiples imágenes por cabaña rápidamente y gestionar los estados de las reservas (Pendiente, Confirmada, Cancelada).

## Tecnologías Utilizadas

* **Backend:** Python 3, Django (ORM, Vistas basadas en funciones, Sistema de Plantillas).
* **Base de Datos:** SQLite (escalable fácilmente a PostgreSQL).
* **Frontend:** HTML5, CSS3, Bootstrap 5, FontAwesome.
* **Librerías Extra:** `fslightbox` (Galería modal).
