# Conclusiones

## Sprint 1 – Landing Page y documentación del proyecto

- **Sobre el análisis del problema y la investigación del usuario:** Se concluye que el análisis realizado sobre propietarios y administradores de minimarkets y bodegas de barrio permitió identificar problemas recurrentes relacionados con el control manual del inventario, las diferencias entre el stock registrado y las existencias físicas, la detección tardía de productos con bajo stock y el tiempo invertido en verificaciones manuales. Esta etapa permitió comprender las necesidades de ambos segmentos y orientar la propuesta de SmartStock hacia una gestión de inventario más automatizada mediante tecnologías web e IoT.

- **Sobre la propuesta de valor y validación inicial:** La elaboración e implementación de la Landing Page permitió comunicar de manera clara la propuesta de valor de SmartStock, presentando el problema que busca resolver, los casos de uso para bodegas y minimarkets, los planes y precios, testimonios, preguntas frecuentes, comparación con otras soluciones y el formulario para solicitar una demostración. De esta manera, la Landing Page funciona como un primer medio de presentación y validación de la solución propuesta para los potenciales usuarios.

- **Sobre la documentación y modelado del proyecto:** La elaboración del reporte permitió consolidar los resultados obtenidos mediante herramientas y técnicas como Lean UX, User Personas, User Task Matrix, User Journey Mapping, Empathy Mapping, Big Picture Event Storming y Ubiquitous Language. Asimismo, el modelado realizado permitió estructurar de manera progresiva el dominio de SmartStock y definir una base para el diseño de la arquitectura, la interfaz y las funcionalidades que serán desarrolladas durante los siguientes sprints.

- **Sobre la definición de requerimientos:** La definición de Epics, User Stories, criterios de aceptación y Product Backlog permitió transformar las necesidades identificadas en funcionalidades concretas y organizadas. Asimismo, la priorización de las historias correspondientes al Landing Page permitió establecer un alcance claro para el Sprint 1, concentrando el desarrollo en las User Stories US16 hasta US24.

- **Sobre la gestión y colaboración del equipo:** El uso de Trello, GitHub, GitFlow y Conventional Commits permitió organizar las tareas del Sprint, mantener un control de los cambios realizados y registrar la participación de los integrantes del equipo. La utilización de ramas `feature`, `develop` y `main` permitió mantener un flujo de trabajo estructurado y evidenciar los aportes realizados durante el desarrollo del Landing Page.

## Sprint 2 – Implementación de la aplicación web y funcionalidades principales

- **Sobre la implementación de la Frontend Web Application:** Se concluye que durante el Sprint 2 se logró desarrollar una versión navegable de la aplicación web de SmartStock, incorporando las principales vistas y módulos correspondientes a la gestión de ventas, compras, productos, monitoreo de inventario, alertas, autenticación, dispositivos IoT y analítica. Este avance permitió trasladar los diseños y requerimientos definidos en las etapas anteriores hacia una interfaz funcional y estructurada.

- **Sobre la gestión del catálogo de productos:** La implementación de las funcionalidades de registro, consulta y edición de productos permitió establecer una base para administrar la información del catálogo. Asimismo, la incorporación de validaciones y reglas de negocio contribuyó a mejorar la consistencia de los datos registrados y facilitar la gestión de los productos dentro de la plataforma.

- **Sobre la gestión de proveedores y compras:** Se concluye que la incorporación de las funcionalidades de registro y consulta de proveedores, así como la administración de compras pendientes, recepción, historial y detalle de compras, permitió ampliar las capacidades de SmartStock para gestionar el proceso de abastecimiento. En particular, la recepción de compras permite actualizar el stock y contribuir a la reposición de productos.

- **Sobre el monitoreo y control del inventario:** La implementación de funcionalidades relacionadas con consultas de inventario, movimientos de stock, visualización de detalles y comparación entre existencias permitió establecer una base para mejorar el seguimiento de los productos. Asimismo, la organización de estas funcionalidades en módulos facilita su integración con el catálogo, los dispositivos IoT y el sistema de alertas.

- **Sobre la organización del desarrollo:** El uso de GitFlow, Pull Requests, Conventional Commits y Sprint Backlog permitió organizar el trabajo de los integrantes, mantener un registro de los cambios realizados y facilitar la integración progresiva de los diferentes módulos. Esto contribuyó a mantener una estructura de desarrollo colaborativa y ordenada.

## Sprint 3 – Integración de servicios, funcionalidades y despliegue

- **Sobre la integración de la aplicación web con los servicios backend:** Se concluye que durante el Sprint 3 se avanzó en la integración de la Frontend Web Application con los RESTful Web Services, permitiendo conectar los módulos de la aplicación con servicios encargados de gestionar información del sistema. Esta integración representó un avance importante respecto a la versión navegable desarrollada en el Sprint 2, al incorporar operaciones respaldadas por servicios backend.

- **Sobre la implementación de los servicios de ventas:** El desarrollo de los servicios relacionados con ventas permitió incorporar operaciones para registrar ventas, validar la disponibilidad de productos y consultar el historial y detalle de las transacciones. Estas funcionalidades contribuyen a mantener un mejor control de las operaciones comerciales y su relación con el inventario disponible.

- **Sobre el sistema de alertas y reposición:** La implementación de las funcionalidades relacionadas con las alertas permitió avanzar en la gestión preventiva del inventario mediante la consulta de alertas y la configuración de canales de notificación. Estas funcionalidades contribuyen a que los propietarios y administradores puedan identificar oportunamente situaciones que requieren atención y mejorar el seguimiento de las condiciones del inventario.

- **Sobre la documentación de los servicios web:** La documentación de los endpoints mediante Scalar permitió organizar y presentar las operaciones disponibles en los servicios backend. Esto facilita la comprensión de las rutas, los métodos HTTP y las funcionalidades expuestas por la API, además de servir como referencia para las actividades de integración y mantenimiento.

- **Sobre la arquitectura e integración de los módulos:** La coordinación entre los diferentes contextos del sistema permitió avanzar hacia una solución modular, en la que las funcionalidades de catálogo, inventario, ventas, alertas, autenticación y analítica se organizan de acuerdo con sus responsabilidades. Esta separación favorece la mantenibilidad y permite continuar ampliando las capacidades de SmartStock de manera progresiva.

- **Sobre la gestión del desarrollo y el trabajo colaborativo:** La utilización de ramas de trabajo, Pull Requests, revisiones de código y convenciones de commits permitió integrar los avances realizados por los diferentes integrantes. Asimismo, el seguimiento del Sprint Backlog facilitó la organización de las actividades y la identificación de los entregables correspondientes a cada etapa del proyecto.

# Recomendaciones

- **Sobre la continuidad de la integración frontend y backend:** Se recomienda continuar verificando la integración entre la aplicación web y los RESTful Web Services, asegurando que las operaciones de consulta, registro, edición y actualización funcionen correctamente. También es importante comprobar el manejo de errores, las respuestas HTTP y la consistencia de los datos intercambiados entre ambos componentes.

- **Sobre la autenticación y seguridad:** Se recomienda fortalecer los mecanismos de autenticación y autorización, verificando el manejo de sesiones, la protección de rutas y el acceso a las funcionalidades según los permisos de cada usuario. Asimismo, es importante validar los procesos de recuperación de contraseñas y registro para garantizar una experiencia segura.

- **Sobre la integración de sensores IoT:** Se recomienda continuar desarrollando y validando la comunicación entre los sensores de peso y la plataforma SmartStock, asegurando que las lecturas obtenidas puedan utilizarse para conocer las existencias físicas de los productos. También será importante evaluar la estabilidad de la conexión y el comportamiento del sistema ante sensores desconectados, lecturas incorrectas o datos no disponibles.

- **Sobre las alertas y la gestión preventiva del inventario:** Se recomienda continuar validando las condiciones que generan alertas de bajo stock y diferencias entre las existencias físicas y las registradas. Asimismo, se debe comprobar la entrega de las notificaciones mediante los canales configurados, considerando posibles fallos de comunicación y mecanismos de reintento.

- **Sobre la gestión de compras y proveedores:** Se recomienda fortalecer las validaciones del proceso de abastecimiento, verificando que la recepción de compras actualice correctamente las existencias y que el historial permita consultar las operaciones realizadas. También es conveniente mantener la integridad de la información relacionada con proveedores, productos y cantidades recibidas.

- **Sobre los reportes y la toma de decisiones:** Se recomienda continuar mejorando las funcionalidades de analítica y generación de reportes, incorporando información sobre ventas, movimientos, rotación e historial del inventario. Estos datos permitirán brindar información útil para planificar las compras, identificar productos de mayor demanda y mejorar las decisiones de reposición.

- **Sobre las pruebas y la validación con usuarios:** Se recomienda continuar ejecutando pruebas funcionales y técnicas sobre los diferentes módulos de SmartStock, complementándolas con entrevistas y evaluaciones de usabilidad con representantes de los segmentos objetivo. Los resultados permitirán identificar oportunidades de mejora en la navegación, comprensión de las funcionalidades y facilidad de uso de la plataforma.

- **Sobre la experiencia de usuario (UX/UI):** Se recomienda mantener una interfaz sencilla, clara y accesible, considerando las características de los propietarios y administradores de minimarkets y bodegas de barrio. Es importante que las operaciones frecuentes, como consultar productos, registrar ventas, revisar alertas y gestionar compras, puedan realizarse de manera intuitiva.

- **Sobre la escalabilidad y mantenimiento del proyecto:** Finalmente, se recomienda mantener la arquitectura modular y las convenciones de desarrollo utilizadas durante los sprints, documentando las modificaciones realizadas y manteniendo actualizados los servicios web. Esto permitirá incorporar nuevas funcionalidades, mejorar los módulos existentes y facilitar el mantenimiento de SmartStock sin afectar los componentes previamente implementados.