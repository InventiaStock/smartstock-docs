# Conclusiones

**Sprint 1 – Landing Page y documentación del proyecto**

- **Sobre el análisis del problema y la investigación del usuario:** Se concluye que el análisis realizado sobre propietarios y administradores de minimarkets y bodegas de barrio permitió identificar problemas recurrentes relacionados con el control manual del inventario, las diferencias entre el stock registrado y las existencias físicas, la detección tardía de productos con bajo stock y el tiempo invertido en verificaciones manuales. Esta etapa permitió comprender las necesidades de ambos segmentos y orientar la propuesta de SmartStock hacia una gestión de inventario más automatizada mediante tecnologías web e IoT.

- **Sobre la propuesta de valor y validación inicial:** La elaboración e implementación de la Landing Page permitió comunicar de manera clara la propuesta de valor de SmartStock, presentando el problema que busca resolver, los casos de uso para bodegas y minimarkets, los planes y precios, testimonios, preguntas frecuentes, comparación con otras soluciones y el formulario para solicitar una demostración. De esta manera, el Landing Page funciona como un primer medio de presentación y validación de la solución propuesta para los potenciales usuarios.

- **Sobre la documentación y modelado del proyecto:** La elaboración del reporte permitió consolidar los resultados obtenidos mediante herramientas y técnicas como Lean UX, User Personas, User Task Matrix, User Journey Mapping, Empathy Mapping, Big Picture Event Storming y Ubiquitous Language. Asimismo, el modelado realizado permitió estructurar de manera progresiva el dominio de SmartStock y definir una base para el diseño de la arquitectura, la interfaz y las funcionalidades que serán desarrolladas durante los siguientes sprints.

- **Sobre la definición de requerimientos:** La definición de Epics, User Stories, criterios de aceptación y Product Backlog permitió transformar las necesidades identificadas en funcionalidades concretas y organizadas. Asimismo, la priorización de las historias correspondientes al Landing Page permitió establecer un alcance claro para el Sprint 1, concentrando el desarrollo en las User Stories US16 hasta US24.

- **Sobre la gestión y colaboración del equipo:** El uso de Trello, GitHub, GitFlow y Conventional Commits permitió organizar las tareas del Sprint, mantener un control de los cambios realizados y registrar la participación de los integrantes del equipo. La utilización de ramas feature, develop y main permitió mantener un flujo de trabajo estructurado y evidenciar los aportes realizados durante el desarrollo del Landing Page.

**Sprint 2 – Frontend Web Application**

- **Sobre la implementación del frontend y el cumplimiento del objetivo del sprint:** Se concluye que el equipo logró entregar la primera versión navegable y desplegada de la Frontend Web Application de SmartStock, desarrollada en Vue 3 en el repositorio InventiaStock/smartstock-frontend. Las 23 User Stories del Product Backlog que no corresponden al Landing Page (84 Story Points) se implementaron en seis bounded contexts: IAM, IoT Device, Alerts & Restocking, Product Catalog, Inventory Monitoring y Analytics & Reporting. De este modo, un usuario puede registrarse, iniciar sesión, registrar productos, proveedores, compras y ventas, y consultar su stock, sus alertas, el dashboard y los reportes.

- **Sobre el núcleo funcional de Compras y Ventas:** La incorporación de las pantallas de Ventas, Proveedores y Compras permitió que SmartStock controle lo que entra y sale del inventario, que es el registro que luego el sensor IoT verifica. Reglas como el rechazo de una venta cuando la cantidad supera el stock disponible, el aumento del stock solo al marcar una compra como recibida y el registro de cada operación como movimiento de stock permitieron mantener coherente el inventario y sentaron la base para la comparación entre el peso físico y el stock registrado.

- **Sobre el uso de servicios simulados y la documentación de contratos:** Durante el sprint, las pantallas consumieron una Fake API desarrollada con json-server y desplegada en Render, lo que permitió avanzar con el frontend sin esperar a los Web Services reales. Los contratos que esta API implementa se documentaron en OpenAPI 3.0.3 con Swagger Editor y Swagger UI, en 21 operaciones que cubren las Technical Stories TS01 a TS15 y la autenticación. Esta decisión permite que los Web Services del Sprint 3 se construyan sobre el mismo contrato, sin modificar las pantallas ya desarrolladas.

- **Sobre el despliegue y la entrega de la versión 1.0.0:** La publicación de la aplicación en GitHub Pages mediante GitHub Actions, a partir de la rama release/1.0.0 integrada en main y etiquetada como v1.0.0, permitió contar con una versión accesible públicamente. La verificación de la URL pública, de la recarga de páginas mediante 404.html y de las peticiones hacia la Fake API permitió validar el despliegue. Asimismo, el rechazo inicial del job de despliegue por las reglas del entorno github-pages y su posterior corrección dejaron como aprendizaje la importancia de revisar la configuración del entorno antes de cada entrega.

- **Sobre la gestión y colaboración del equipo:** La aplicación de GitFlow y Conventional Commits se consolidó durante el Sprint 2: cada tarea se trabajó en una rama corta feature/\<contexto\>-\<tarea\> creada desde develop, integrada mediante pull request revisado por otro integrante y con merge commit, sin commits directos en main ni en develop. La asignación de un integrante líder por contexto, junto con el uso de Trello, el Sprint Backlog y las vistas Contributors, Pulse y Network graph de GitHub, permitió distribuir la carga de trabajo y evidenciar el aporte de cada miembro. Como aspecto a mejorar, el uso de un correo de git mal configurado impidió que algunos commits se atribuyeran a su autor, situación que ya fue corregida.

**Sprint 3 – Frontend Web Application**

- **Sobre la arquitectura del backend:** Se concluye que el backend de SmartStock, desarrollado en ASP.NET Core 9 como monolito modular con 6 bounded contexts, permitió organizar de forma clara las responsabilidades del sistema (catálogo, stock, compras, ventas, sensores IoT, alertas y reportes), y facilitó su mantenimiento y evolución en los siguientes sprints.

- **Sobre los Web Services y su documentación:** Se implementaron y documentaron en Scalar 30 operaciones (17 de Nivel 1 y 13 de Nivel 2), que permiten probar el funcionamiento de la API de manera directa y sirven como contrato para la integración con la Web App.

- **Sobre la persistencia de datos:** El uso de EF Core con MySQL (Aiven, 16 tablas) permitió almacenar y consultar de forma consistente productos, movimientos de stock, compras, proveedores, lecturas de sensores y alertas.

- **Sobre las reglas de negocio:** Se verificaron con pruebas sobre la API real reglas clave como la recepción de compras que suma stock y registra el movimiento de entrada (R16), la imposibilidad de recibir dos veces una misma compra y la detección de discrepancias de más del 10 % entre el stock físico y el registrado (R20).

- **Sobre el despliegue y la integración:** La publicación del backend en Render y la conexión de la Web App v1.1.0 con la API real permitieron validar el flujo completo entre la interfaz y los servicios, aunque el acceso de demostración temporal se mantiene hasta implementar la autenticación.

- **Sobre el trabajo en equipo y el control de versiones:** El uso de GitFlow, Conventional Commits, pull requests e integración continua permitió mantener un historial ordenado y trazable del desarrollo.

**Recomendaciones**

- **Sobre la continuidad de la integración frontend y backend:** Se recomienda continuar verificando la integración entre la aplicación web y los RESTful Web Services, asegurando que las operaciones de consulta, registro, edición y actualización funcionen correctamente. También es importante comprobar el manejo de errores, las respuestas HTTP y la consistencia de los datos intercambiados entre ambos componentes.

- **Sobre la autenticación y seguridad:** Se recomienda fortalecer los mecanismos de autenticación y autorización, verificando el manejo de sesiones, la protección de rutas y el acceso a las funcionalidades según los permisos de cada usuario. Asimismo, es importante validar los procesos de recuperación de contraseñas y registro para garantizar una experiencia segura.

- **Sobre la integración de sensores IoT:** Se recomienda continuar desarrollando y validando la comunicación entre los sensores de peso y la plataforma SmartStock, asegurando que las lecturas obtenidas puedan utilizarse para conocer las existencias físicas de los productos. También será importante evaluar la estabilidad de la conexión y el comportamiento del sistema ante sensores desconectados, lecturas incorrectas o datos no disponibles.

- **Sobre las alertas y la gestión preventiva del inventario:** Se recomienda continuar validando las condiciones que generan alertas de bajo stock y diferencias entre las existencias físicas y las registradas. Asimismo, se debe comprobar la entrega de las notificaciones mediante los canales configurados, considerando posibles fallos de comunicación y mecanismos de reintento.

- **Sobre la gestión de compras y proveedores:** Se recomienda fortalecer las validaciones del proceso de abastecimiento, verificando que la recepción de compras actualice correctamente las existencias y que el historial permita consultar las operaciones realizadas. También es conveniente mantener la integridad de la información relacionada con proveedores, productos y cantidades recibidas.

- **Sobre los reportes y la toma de decisiones:** Se recomienda continuar mejorando las funcionalidades de analítica y generación de reportes, incorporando información sobre ventas, movimientos, rotación e historial del inventario. Estos datos permitirán brindar información útil para planificar las compras, identificar productos de mayor demanda y mejorar las decisiones de reposición.

- **Sobre las pruebas y la validación con usuarios:** Se recomienda continuar ejecutando pruebas funcionales y técnicas sobre los diferentes módulos de SmartStock, complementándolas con entrevistas y evaluaciones de usabilidad con representantes de los segmentos objetivo. Los resultados permitirán identificar oportunidades de mejora en la navegación, comprensión de las funcionalidades y facilidad de uso de la plataforma.

- **Sobre la experiencia de usuario (UX/UI):** Se recomienda mantener una interfaz sencilla, clara y accesible, considerando las características de los propietarios y administradores de minimarkets y bodegas de barrio. Es importante que las operaciones frecuentes, como consultar productos, registrar ventas, revisar alertas y gestionar compras, puedan realizarse de manera intuitiva.

- **Sobre la escalabilidad y mantenimiento del proyecto:** Finalmente, se recomienda mantener la arquitectura modular y las convenciones de desarrollo utilizadas durante los sprints, documentando las modificaciones realizadas y manteniendo actualizados los servicios web. Esto permitirá incorporar nuevas funcionalidades, mejorar los módulos existentes y facilitar el mantenimiento de SmartStock sin afectar los componentes previamente implementados.

