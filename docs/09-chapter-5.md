# Capítulo V: Product Implementation, Validation & Deployment

En este capítulo se explica y evidencia el proceso de implementar, comprobar, desplegar y validar la solución de SmartStock, compuesta por el Landing Page, los RESTful Web Services y la Frontend Web Application, todos ellos con diseño web responsive. El Landing Page presenta el modelo de negocio y da acceso a la aplicación web. Los procesos del negocio digital, tanto los procesos core como los de soporte (autenticación y autorización, suscripciones, entre otros), están soportados por la Frontend Web Application y los RESTful Web Services.

## 5.1. Software Configuration Management

En esta sección se establecen las decisiones y convenciones que permiten mantener la consistencia del producto durante todo su ciclo de vida, abarcando la configuración del ambiente de desarrollo, la gestión del código fuente, las convenciones de estilo de código y la configuración del despliegue.

### 5.1.1. Software Development Environment Configuration

A continuación se detallan los productos de software que utilizan los miembros del equipo para colaborar en el ciclo de vida del producto digital, agrupados por tipo de actividad, indicando el propósito de uso en el proyecto y la ruta de referencia o de descarga según corresponda.

**Project Management**

**Tabla 20**

*Herramientas de Project Management*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| Trello | Gestión del Product Backlog y de los Sprint Backlogs mediante tableros por sprint, con el registro de los work-items y su estado. | https://trello.com |
| Microsoft Teams | Realización de las sesiones síncronas del equipo, incluyendo Sprint Planning, Sprint Review y Retrospective. | https://www.microsoft.com/microsoft-teams |
Nota. Elaboración propia

**Requirements Management**

**Tabla 21**

*Herramientas de Requirements Management*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| UXPressia | Elaboración de los User Personas, Empathy Maps, User Journey Maps e Impact Maps de los segmentos objetivo. | https://uxpressia.com |
| Miro | Realización de las sesiones de Big Picture Event Storming y Design-Level Event Storming. | https://miro.com |
Nota. Elaboración propia

**Product UX/UI Design**

**Tabla 22**

*Herramientas de Product UX/UI Design*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| Figma | Elaboración de los wireframes, mock-ups y prototipos del Landing Page y de la Web Application, en sus versiones para Desktop y Mobile Web Browser. | https://www.figma.com |
| FigJam | Elaboración de los Wireflow Diagrams y de los User Flow Diagrams de la Web Application. | https://www.figma.com/figjam |
| LucidChart | Elaboración de los Class Diagrams de UML y de los Database Diagrams de cada bounded context. | https://www.lucidchart.com |
| Structurizr | Elaboración de los diagramas de C4 Model en sus niveles de Context, Container y Component. | https://structurizr.com |
Nota. Elaboración propia

**Software Development**

**Tabla 23**

*Herramientas de Software Development*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| IntelliJ IDEA Ultimate | Entorno de desarrollo integrado para la implementación de los Web Services en Java con Spring Boot. Disponible mediante la JetBrains Educational License. | https://www.jetbrains.com/idea/download |
| WebStorm | Entorno de desarrollo integrado para la implementación de la Frontend Web Application en Angular y del Landing Page. Disponible mediante la JetBrains Educational License. | https://www.jetbrains.com/webstorm/download |
| Java Development Kit (JDK) 21 LTS | Kit de desarrollo del lenguaje Java utilizado para la implementación de los Web Services. | https://adoptium.net/temurin/releases |
| Spring Boot | Framework open source utilizado para la implementación del RESTful API, junto con Spring Data JPA para la persistencia. | https://start.spring.io |
| Node.js y npm | Entorno de ejecución y gestor de paquetes requeridos por Angular CLI. | https://nodejs.org/en/download |
| Angular CLI | Herramienta de línea de comandos para la creación, ejecución y construcción de la Frontend Web Application. | https://angular.dev/tools/cli |
| Angular Material | Biblioteca de componentes de interfaz de usuario basada en Material Design, utilizada en la Web Application. | https://material.angular.io |
| MySQL Community Server | Sistema de gestión de base de datos relacional utilizado para la persistencia de los Web Services. | https://dev.mysql.com/downloads/mysql |
| Postman | Verificación manual de las solicitudes y respuestas de los endpoints del RESTful API durante el desarrollo. | https://www.postman.com/downloads |
Nota. Elaboración propia

**Software Documentation**

**Tabla 24**

*Herramientas de Software Documentation*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| Swagger UI (springdoc-openapi) | Generación y publicación de la documentación del RESTful API bajo la especificación OpenAPI. | https://springdoc.org |
| GitHub | Alojamiento del informe del proyecto en formato Markdown y de la documentación de cada repositorio. | https://github.com/NexoStock |
Nota. Elaboración propia

**Software Deployment**

**Tabla 25**

*Herramientas de Software Deployment*

| Producto | Propósito de uso en el proyecto | Ruta |
|---|---|---|
| GitHub Pages | Publicación del sitio web estático correspondiente al Landing Page. | https://pages.github.com |
| Git | Sistema de control de versiones utilizado localmente por cada miembro del equipo. | https://git-scm.com/downloads |
Nota. Elaboración propia

Pendiente: confirmar el proveedor de despliegue de la Frontend Web Application y de los Web Services antes de la entrega en la que cada producto debe estar desplegado, y agregarlo a este cuadro.

### 5.1.2. Source Code Management

El equipo utiliza GitHub como plataforma de alojamiento y Git como sistema de control de versiones. Los repositorios del proyecto pertenecen a la organización pública InventiaStock y se organizan en un repositorio por producto, además del repositorio de documentación del informe.

**Tabla 26**

*Repositorios del proyecto por producto*

| Producto | Repositorio |
|---|---|
| Project Report | https://github.com/InventiaStock/smartstock-docs.git |
| Landing Page | https://github.com/InventiaStock/smartstock-landing-page.git |
| Frontend Web Application | Pendiente de creación. |
| Web Services | Pendiente de creación. |
Nota. Elaboración propia

**GitFlow como workflow de control de versiones**

El equipo aplica GitFlow, siguiendo el modelo de ramificación descrito por Vincent Driessen. Cada repositorio mantiene las siguientes ramas:

**Tabla 27**

*Ramas de GitFlow y convención de nombres*

| Rama | Propósito | Convención de nombre |
|---|---|---|
| main | Rama principal. Contiene únicamente las versiones entregadas y estables del producto. Cada integración a esta rama corresponde a un release etiquetado. | main |
| develop | Rama de integración. Concentra el avance acumulado de las features completadas que aún no forman parte de un release. | develop |
| Feature branches | Una rama por cada feature o sección en desarrollo. Nace de develop y se integra a develop mediante Pull Request. | feature/\<nombre-en-kebab-case\>, por ejemplo feature/user-stories o feature/sensor-linking |
| Release branches | Rama de preparación de una versión a entregar. Nace de develop y se integra tanto a main como a develop. | release/\<major\>.\<minor\>.\<patch\>, por ejemplo release/1.0.0 |
| Hotfix branches | Rama de corrección urgente sobre una versión ya publicada. Nace de main y se integra tanto a main como a develop. | hotfix/\<nombre-en-kebab-case\>, por ejemplo hotfix/broken-toc-links |
Nota. Elaboración propia

**Semantic Versioning**

Los releases se nombran aplicando Semantic Versioning 2.0.0, bajo el formato MAJOR.MINOR.PATCH. Se incrementa la versión MAJOR ante cambios incompatibles con versiones previas, la versión MINOR ante la incorporación de funcionalidad compatible con versiones previas, y la versión PATCH ante correcciones compatibles con versiones previas. Cada release se registra como un tag de Git sobre main, bajo el formato vMAJOR.MINOR.PATCH.

**Conventional Commits**

Los mensajes de commit siguen la especificación de Conventional Commits, bajo la estructura `<type>(<scope>): <description>`. Los tipos utilizados por el equipo son los siguientes:

**Tabla 28**

*Tipos de commit según Conventional Commits*

| Tipo | Uso |
|---|---|
| feat | Incorporación de una nueva funcionalidad al producto o de una nueva sección al informe. |
| fix | Corrección de un defecto en el producto o de un error en el informe. |
| docs | Cambios que afectan únicamente a la documentación. |
| style | Cambios que no alteran el significado del código, como formato o espaciado. |
| refactor | Cambios en el código que no corrigen defectos ni agregan funcionalidad. |
| test | Incorporación o corrección de pruebas. |
| chore | Cambios en la configuración del proyecto o en las herramientas de soporte. |
Nota. Elaboración propia

La descripción se redacta en inglés, en modo imperativo y en minúsculas, sin punto final. El scope identifica la sección del informe o el módulo del producto afectado.

### 5.1.3. Source Code Style Guide & Conventions

El equipo adopta la nomenclatura en inglés para todos los lenguajes utilizados en la solución, así como las siguientes convenciones estándar de codificación:

**Tabla 29**

*Convenciones de codificación por lenguaje*

| Lenguaje | Convención adoptada |
|---|---|
| HTML | HTML Style Guide and Coding Conventions (W3Schools) / Google HTML/CSS Style Guide |
| CSS | Google HTML/CSS Style Guide |
| JavaScript | Google JavaScript Style Guide / MDN JavaScript Guidelines / Vue Style Guide |
| C# | C# Coding Conventions (Microsoft) / Microsoft ASP.NET Core Coding Guidelines |
| Gherkin (criterios de aceptación) | Gherkin Conventions for Readable Specifications |
Nota. Elaboración propia

### 5.1.4. Software Deployment Configuration

**Landing Page**

El Landing Page se publica como sitio web estático en GitHub Pages, a partir del repositorio correspondiente de la organización InventiaStock. Los pasos de configuración fueron los siguientes:

1. Se integró a la rama main del repositorio del Landing Page la versión a publicar, mediante el flujo GitFlow (ramas feature/, fix/ y chore/ integradas a develop, y develop integrada a main).
2. En la configuración del repositorio, se accedió a la sección **Settings → Pages** y se seleccionó como fuente la rama main y el directorio raíz (/root).
3. Se confirmó la publicación y se verificó el sitio en la URL asignada por GitHub Pages: **https://inventiastock.github.io/smartstock-landing-page/**
4. Se verificó el correcto funcionamiento del selector de idioma, la navegación por anclas y el enlace a los términos y condiciones del footer.

**Figura 154**

*Configuración de GitHub Pages del repositorio smartstock-landing-page*

![Configuración de GitHub Pages para el repositorio smartstock-landing-page](../assets/chapter-5/deploypagesconfig.png)
*Nota: Configuración de GitHub Pages para el repositorio smartstock-landing-page, publicando desde la rama main.*

**Figura 155**

*Landing Page de SmartStock desplegado en GitHub Pages*

![Landing page de SmartStock desplegada y accesible públicamente en GitHub Pages](../assets/chapter-5/deploylandingpublished.png)
*Nota: Landing page de SmartStock desplegada y accesible públicamente en GitHub Pages.*

## 5.2. Landing Page, Services & Applications Implementation

En esta sección se explica y evidencia el proceso de implementación, pruebas, documentación y despliegue del Landing Page, los Web Services y la Frontend Web Application, organizado por sprints.

### 5.2.1. Sprint 1

#### 5.2.1.1. Sprint Planning 1

**Tabla 30**

*Sprint Planning 1*

| Campo | Detalle |
|---|---|
| Sprint # | 1 |
| Date | 2026-09-12 |
| Time | 4:00 PM |
| Location | Reunión virtual |
| Prepared By | Montañez Salinas, Lorena Ariana |
| Attendees | Lopez Rimachi, Sebastian Leonardo; Montañez Salinas, Lorena Ariana; Sanchez Osorio, Ruth Yanira; Suarez Chinga, Geraldine; Vizcarra Mamani, Candy Milagros |
| Sprint 0 – Review Summary | N/A (Primer Sprint del proyecto. Se establecieron las bases de la arquitectura, infraestructura en la nube y repositorios). |
| Sprint 0 – Retrospective Summary | N/A (Primer Sprint. El equipo acordó usar GitFlow y Conventional Commits rigurosamente desde el primer día). |
| Sprint 1 Goal | Our focus is on delivering a fast, static Landing Page (HTML/CSS/JS) with language support to attract clients and validate our value proposition. We believe it delivers a clear, accessible introduction to our product's value proposition to minimarket and bodega owners exploring inventory solutions. This will be confirmed when the Landing Page is deployed and fully navigable by users, in both supported languages. |
| Sprint 1 Velocity | 10 Story Points (Velocidad estimada para el primer ciclo del equipo). |
| Sum of Story Points | 10 |
Nota. Elaboración propia

#### 5.2.1.2. Aspect Leaders and Collaborators

A continuación, se presenta la matriz de liderazgo y colaboración (LACX), cuyo objetivo es facilitar una comunicación clara y organizada entre los integrantes del equipo durante el desarrollo de las tareas correspondientes a este Sprint.

**Tabla 31**

*Matriz de liderazgo y colaboración (LACX) del Sprint 1*

| Team Member | GitHub Username | Landing Page Structure | Landing Page UI/UX |
|---|---|---|---|
| Lopez Rimachi, Sebastian Leonardo | @leonardoXd1323 | C | C |
| Montañez Salinas, Lorena Ariana | @Lore-MS | C | C |
| Sanchez Osorio, Ruth Yanira | @Yiya-ciber | L | C |
| Suarez Chinga, Geraldine | @geral07-UNIV | C | L |
| Vizcarra Mamani, Candy Milagros | @candyvizz | C | C |
Nota. Elaboración propia

#### 5.2.1.3. Sprint Backlog 1

El Sprint Backlog 1 se estructuró en torno a la construcción del sitio web estático (Landing Page) de SmartStock, encargado de comunicar la propuesta de valor del producto, los casos de uso diferenciados para bodegas de barrio y minimarkets, los planes y precios, la comparación frente a otras soluciones del mercado, y el flujo de contacto y registro de nuevos usuarios. Cada User Story del Epic EP08 se descompuso en tareas técnicas concretas, asignadas a los integrantes del subequipo de Landing Page (Ruth Sánchez y Geraldine Suárez) según su rol de diseño y desarrollo dentro del proyecto.

Trello link: https://trello.com/invite/b/6aa988a0941a5fb8c814af43/ATTI5eecabb28fdc9c85d7ba8336b688a97353B8B08C/trello-web

**Figura 156**

*Tablero de Trello del Sprint Backlog 1*

![Tablero de Trello con los Epics y el Sprint Backlog 1](../assets/chapter-5/sprint1trello.png)
Nota. Elaboración propia

**Sprint # Sprint 1**

**Tabla 32**

*Sprint Backlog 1*

| Story Id | Story Title | Task Id | Task Title | Task Description | Estimation (Hours) | Assigned To | Status |
|---|---|---|---|---|---|---|---|
| US16 | Información general de SmartStock | T01 | Construir sección Hero con información general | Maquetar la propuesta de valor y el problema que resuelve SmartStock en la página de inicio, incluyendo los estilos base del sitio (colores y tipografía). | 5 | Ruth Sanchez Osorio | Done |
| US16 | Información general de SmartStock | T02 | Rediseñar la sección Hero | Reestructurar el Hero en dos columnas (copy + imagen), agregar el kicker y la imagen del dueño de tienda, junto con los CTA "Start free trial" y "Request a demo". | 4 | Lorena Montañez Salinas | Done |
| US17 | Casos de uso para bodegas de barrio | T03 | Construir sección de casos de uso — bodegas | Maquetar el contenido dirigido al segmento bodegas de barrio. | 3 | Ruth Sanchez Osorio | Done |
| US17 | Casos de uso para bodegas de barrio | T04 | Refinar el copy de casos de uso — bodegas | Ajustar la redacción del contenido de bodegas para mayor claridad. | 1 | Lorena Montañez Salinas | Done |
| US18 | Casos de uso para minimarkets | T05 | Construir sección de casos de uso — minimarkets | Maquetar el contenido dirigido al segmento minimarkets. | 3 | Ruth Sanchez Osorio | Done |
| US18 | Casos de uso para minimarkets | T06 | Refinar el copy de casos de uso — minimarkets | Ajustar la redacción del contenido de minimarkets para mayor claridad. | 1 | Lorena Montañez Salinas | Done |
| US19 | Planes y precios | T07 | Construir sección de planes y precios | Maquetar los planes disponibles con sus características y costos. | 3 | Ruth Sanchez Osorio | Done |
| US19 | Planes y precios | T08 | Agregar botones de selección de plan | Implementar los CTA "Choose Starter" y "Choose Growth" en la sección de planes. | 2 | Candy Vizcarra Mamani | Done |
| US20 | Formulario de contacto para solicitar demostración | T09 | Construir formulario de contacto y validación | Maquetar el formulario (nombre, negocio, correo) e implementar la validación de campos obligatorios. | 4 | Ruth Sanchez Osorio | Done |
| US21 | Preguntas frecuentes sobre instalación de sensores | T10 | Construir sección de preguntas frecuentes | Maquetar el listado de preguntas y respuestas sobre instalación de sensores IoT. | 2 | Ruth Sanchez Osorio | Done |
| US22 | Testimonios de dueños de bodega | T11 | Construir sección de testimonios (base) | Maquetar la sección inicial de testimonios de clientes. | 2 | Ruth Sanchez Osorio | Done |
| US22 | Testimonios de dueños de bodega | T12 | Rediseñar testimonios como grid de tarjetas | Reestructurar la sección en un grid de tarjetas, con avatares, calificación de 5 estrellas y el rol de cada persona. | 4 | Geraldine Suarez Chinga | Done |
| US22 | Testimonios de dueños de bodega | T13 | Estilizar el nuevo grid de testimonios | Agregar los estilos CSS del nuevo diseño de testimonios. | 2 | Geraldine Suarez Chinga | Done |
| US23 | Comparación frente a otras soluciones | T14 | Construir tabla comparativa | Maquetar la tabla comparativa entre SmartStock y otras soluciones del mercado. | 3 | Ruth Sanchez Osorio | Done |
| US24 | Acceso a registro desde el sitio web | T15 | Agregar acceso a registro permanente en el header | Incorporar el enlace de registro visible desde cualquier sección del sitio. | 2 | Ruth Sanchez Osorio | Done |
| US24 | Acceso a registro desde el sitio web | T16 | Ajustar logo y etiquetas aria del navbar | Redimensionar el logo (28px→42px) y añadir etiquetas aria descriptivas en la navegación. | 2 | Candy Vizcarra Mamani | Done |
| US24 | Acceso a registro desde el sitio web | T17 | Dar visibilidad persistente al enlace de registro | Incorporar el enlace "Sign up" visible de forma persistente en el header. | 2 | Candy Vizcarra Mamani | Done |
| US24 | Acceso a registro desde el sitio web | T18 | Reparar navegación en pantallas angostas | Corregir el comportamiento del menú y el acceso al registro en viewports menores a 720px. | 3 | Sebastian Lopez Rimachi | Done |
| — | Tarea adicional (no ligada a un User Story en particular) | T19 | Implementar selector de idioma (inglés/español) | Añadir el switch de idioma con inglés por defecto y diccionario para español (es_419), aplicado a todas las secciones. | 4 | Ruth Sanchez Osorio | Done |
| — | Tarea adicional (no ligada a un User Story en particular) | T20 | Redactar términos y condiciones | Elaborar la página de términos y condiciones enlazada desde el footer, siguiendo el código de ética ACM/IEEE y del Colegio de Ingenieros del Perú. | 3 | Ruth Sanchez Osorio | Done |
| — | Tarea adicional (no ligada a un User Story en particular) | T21 | Eliminar rutas hardcodeadas del script | Quitar la URL y las rutas de la app hardcodeadas en script.js. | 2 | Sebastian Lopez Rimachi | Done |
| — | Tarea adicional (no ligada a un User Story en particular) | T22 | Forzar idioma por defecto (inglés) | Configurar inglés como locale por defecto según requisito del curso. | 1 | Sebastian Lopez Rimachi | Done |
| — | Tarea adicional (no ligada a un User Story en particular) | T23 | Documentar el proyecto (README) | Redactar el README con el propósito del proyecto, el stack utilizado y la estructura de archivos. | 2 | Lorena Montañez Salinas | Done |
Nota. Elaboración propia

**Resumen de carga por integrante:** Ruth Sanchez Osorio (11 tasks, 34h) · Lorena Montañez Salinas (4 tasks, 8h) · Candy Vizcarra Mamani (3 tasks, 6h) · Geraldine Suarez Chinga (2 tasks, 6h) · Sebastian Lopez Rimachi (3 tasks, 6h).

#### 5.2.1.4. Development Evidence for Sprint Review

Durante el Sprint 1 se implementó la primera versión del sitio web estático (Landing Page) de SmartStock, cubriendo las secciones de propuesta de valor, problemática, casos de uso por segmento, comparación frente a otras soluciones, planes y precios, testimonios, preguntas frecuentes y formulario de contacto. A continuación se presenta la tabla de commits relacionados con la implementación, organizados por rama según GitFlow y redactados bajo la convención de Conventional Commits.

**Tabla 33**

*Commits relacionados con la implementación del Sprint 1*

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Commited on (Date) |
|---|---|---|---|---|---|
| smartstock-landing-page | feature/landing-page | 8f8baff | feat(landing): add base styles | White as the dominant background, navy for headings and actions. Only the tokens the page actually uses are declared. | 10/09/2026 |
| smartstock-landing-page | feature/landing-page | 083b61e | feat(landing): add the home page sections | Cover the user stories of the static web site: general information and the problem it solves (US16), use cases for corner stores (US17) and minimarkets (US18), comparison against other solutions (US23), plans and pricing (US19), testimonials (US22), sensor installation FAQ (US21), demonstration request form (US20) and permanent access to sign-up from the header (US24). | 10/09/2026 |
| smartstock-landing-page | feature/landing-page | a3d57f5 | feat(landing): add language switch, menu, faq and form validation | English is the default language and its copy lives in the markup, so the page still reads complete if this script fails to load. Spanish (es_419) comes from a flat dictionary. The call-to-action links to the web application are built from a single URL constant. | 11/09/2026 |
| smartstock-landing-page | feature/landing-page | f1fd4da | feat(landing): add terms and conditions linked from the footer | Written following the ACM/IEEE Software Engineering Code of Ethics and the code of ethics of the Colegio de Ingenieros del Perú. | 11/09/2026 |
| smartstock-landing-page | fix/mobile-navbar | 519a06f | fix(landing): repair the navigation bar on narrow screens | Below 720px the sign-up button moves into the collapsible menu so the bar keeps only the brand, language switch and menu button. Sign-up stays reachable from every section (US24) and the language switch stays visible. | 12/09/2026 |
| smartstock-landing-page | feature/header-navbar | 5dcbdb0 | feat(landing): resize brand logo and improve navbar aria labels | Se ajustó el tamaño del logo (28px→42px) y se añadieron etiquetas aria descriptivas en el selector de idioma y la navegación. Aplica en index.html y terms-of-service.html. | 12/09/2026 |
| smartstock-landing-page | feature/header-navbar | e08146f | feat(landing): add persistent sign up link in header | Se agregó el enlace "Sign up" visible en el header. | 13/09/2026 |
| smartstock-landing-page | feature/pricing-cta | 4496ea1 | feat(landing): add plan selection CTA buttons | Se agregaron los botones "Choose Starter" y "Choose Growth" en la sección de planes. | 13/09/2026 |
| smartstock-landing-page | feature/usecase-content | bc2072c | content: refine corner store and minimarket copy | Se ajustó la redacción de los casos de uso de bodega y minimarket. | 14/09/2026 |
| smartstock-landing-page | feature/hero-redesign | 9a8b222 | feat(landing): redesign hero section with visual and kicker | Se reestructuró el hero en dos columnas (copy + imagen), añadiendo el kicker y la imagen del dueño de tienda. | 14/09/2026 |
| smartstock-landing-page | feature/hero-redesign | ec752f4 | feat(landing): add hero CTAs and supporting copy | Se agregaron los botones "Start free trial" y "Request a demo" junto con el texto de nota. | 15/09/2026 |
| smartstock-landing-page | feature/testimonials-redesign | 3ceb77f | feat(landing): rebuild testimonials as card grid | Se reestructuró la sección de testimonios en un grid de tarjetas. | 15/09/2026 |
| smartstock-landing-page | feature/testimonials-redesign | 21f1118 | feat(landing): add avatars, ratings and roles to testimonials | Se añadieron avatares, calificación de 5 estrellas y el rol de cada persona. | 16/09/2026 |
| smartstock-landing-page | feature/testimonials-redesign | aed1e38 | style(landing): add testimonials grid and card styles | Se agregaron los estilos CSS del nuevo diseño de testimonios. | 16/09/2026 |
| smartstock-landing-page | chore/script-cleanup | 871c162 | chore(landing): remove hardcoded app routes from script | Se eliminaron la URL y las rutas de la app hardcodeadas en script.js. | 16/09/2026 |
| smartstock-landing-page | chore/script-cleanup | eb3dc3c | fix(landing): set English as default locale | Se forzó inglés como idioma por defecto según requisito del curso. | 16/09/2026 |
| smartstock-landing-page | develop | bb44d80 | docs: add project README | Se documenta el propósito del proyecto, el stack utilizado y la estructura de archivos del landing page. | 16/09/2026 |
Nota. Elaboración propia

#### 5.2.1.5. Execution Evidence for Sprint Review

Durante el Sprint 1 se implementó y desplegó la primera versión del Landing Page, que cubre las User Stories del sitio web estático especificadas en la sección 3.1. El sitio se encuentra accesible en https://inventiastock.github.io/smartstock-landing-page/.

A continuación se presentan las principales vistas implementadas.

**Encabezado principal y propuesta de valor (US16, US24)**

El encabezado principal se organiza en dos columnas: a la izquierda la propuesta de valor, que presenta qué es SmartStock y qué problema resuelve, y a la derecha una fotografía de un propietario de tienda utilizando la plataforma junto a sus estantes abastecidos. La imagen permite que el visitante reconozca el segmento al que se dirige el producto antes de leer una sola línea, y cuenta con un texto alternativo descriptivo que se traduce junto con el resto de la página.

La barra superior mantiene visibles de forma permanente el selector de idioma y la acción de crear cuenta, en cumplimiento de la regla de negocio de la US24.

**Figura 157**

*Encabezado principal y propuesta de valor del Landing Page (US16, US24)*

![Encabezado principal del Landing Page y sección de problemática](../assets/chapter-5/sprint1hero.png)
Nota. Elaboración propia

**Casos de uso por segmento objetivo (US17, US18)**

La sección de casos de uso separa el contenido dirigido a bodegas de barrio del dirigido a minimarkets. Cada bloque enumera los beneficios propios del segmento y cierra con un call-to-action que redirige a la vista de registro de la Web Application transportando el segmento correspondiente. La captura se presenta con la experiencia conmutada a español latinoamericano, de modo que evidencie además el alcance de la traducción sobre el contenido de esta sección.

**Figura 158**

*Sección de casos de uso por segmento objetivo del Landing Page (US17, US18)*

![Sección de casos de uso por segmento y comparación frente a otras soluciones](../assets/chapter-5/sprint1usecases.png)
Nota. Elaboración propia

**Planes y precios (US19)**

Los tres planes se presentan sobre el mismo conjunto de características, ordenados de menor a mayor capacidad, y el plan intermedio se destaca mediante un borde de mayor peso. Cada plan conduce al registro con el plan preseleccionado. Las tarjetas aplican el refresco visual del design system: radio de esquina de 14 píxeles, elevación tenue en reposo y un filete de acento que se revela al pasar el cursor.

**Figura 159**

*Sección comparativa frente a otras soluciones del Landing Page (US23)*

![Comparación frente a otras soluciones del mercado y sección de planes y precios](../assets/chapter-5/sprint1comparison.png)
Nota. Elaboración propia

**Figura 160**

*Sección de planes y precios del Landing Page (US19)*

![Sección de planes y precios con los tres planes disponibles](../assets/chapter-5/sprint1plans.png)
Nota. Elaboración propia

**Testimonios de clientes (US22)**

La sección de testimonios presenta las opiniones recogidas durante las entrevistas, cada una acompañada de una valoración y de un avatar con las iniciales del entrevistado. La valoración se expone además mediante aria-label, de modo que un lector de pantalla anuncie la calificación en lugar de leer una sucesión de símbolos.

**Figura 161**

*Formulario de solicitud de demostración del Landing Page (US20)*

![Sección de testimonios de clientes con calificación por estrellas](../assets/chapter-5/sprint1testimonials.png)
Nota. Elaboración propia

**Formulario de solicitud de demostración (US20)**

El formulario valida los campos obligatorios al abandonar cada campo y expone los mensajes de error mediante `role="alert"`, de modo que un lector de pantalla los anuncie. Los campos adoptan el radio de esquina y el color de borde definidos en la sección 4.1, y el botón de envío emplea el degradado de marca.

**Figura 162**

*Formulario de solicitud de demostración del Landing Page (US20)*

![Formulario de solicitud de demostración](../assets/chapter-5/sprint1demoform.png)
Nota. Elaboración propia

**Internacionalización de la experiencia (en_US / es_419)**

El idioma por defecto del sitio es el inglés, conforme a lo establecido en el enunciado. El sitio no adopta el idioma del navegador en la primera visita, precisamente para que el idioma por defecto del producto sea siempre el inglés; a partir de ahí, la preferencia elegida por el visitante queda registrada en el navegador.

El selector de idioma de la barra superior conmuta toda la experiencia al español latinoamericano, incluyendo el título del documento, los textos de la interfaz, los mensajes de validación del formulario y los atributos aria-label de la navegación, del selector de idioma y de la imagen del encabezado principal. El atributo `lang` del documento se actualiza en cada conmutación, de modo que un lector de pantalla emplee la pronunciación correcta.

**Figura 163**

*Formulario de demostración y pie de página del Landing Page*

![Formulario de solicitud de demostración con la experiencia conmutada a español, y footer del sitio](../assets/chapter-5/sprint1i18n.png)
Nota. Elaboración propia

**Diseño web adaptable (responsive web design)**

La experiencia se adapta a las dimensiones del dispositivo cliente. En navegador móvil, las rejillas de tarjetas colapsan a una sola columna, la escala tipográfica de los titulares se reduce y la navegación se repliega tras un botón de menú.

La barra superior conserva en pantallas estrechas únicamente la marca, el selector de idioma y el botón de menú. La acción de crear cuenta se traslada al interior del menú desplegable, de modo que la barra no compita por el ancho disponible y se mantenga el cumplimiento de la regla de negocio de la US24, que establece que la opción de registro está disponible de forma permanente en todas las secciones del sitio web estático.

**Figura 164**

*Mockup de la interfaz principal de incio del landing*

![Mockup de la interfaz principal de inicio del landing page de SmartStock adaptada para dispositivos móviles](../assets/chapter-5/sprint1mobile.png)
*Nota: Mockup de la interfaz principal de inicio del landing page de SmartStock adaptada para dispositivos móviles.*

**Landing Page Demonstration Video:** SmartStock - Landing Page Review.mp4
<!-- PENDIENTE: reemplazar por el enlace real de alojamiento del video (Microsoft Stream/YouTube/Drive) una vez esté publicado. -->

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

N/A. Durante el Sprint 1 el esfuerzo de desarrollo se enfocó exclusivamente en la creación del sitio web estático promocional (Landing Page), por lo que aún no se han implementado APIs RESTful ni Endpoints backend que requieran ser documentados a través de Swagger/OpenAPI. Esta documentación se estructurará a partir del Sprint 2.

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 1, el alcance de despliegue correspondió al Landing Page. El equipo creó el repositorio `smartstock-landing-page` dentro de la organización InventiaStock, aplicó sobre él el flujo de trabajo GitFlow e integró la versión 1.0.0 a la rama `main` mediante una release branch. A continuación, habilitó GitHub Pages tomando como fuente dicha rama y el directorio raíz del repositorio.

**Tabla 34**

*Evidencia de despliegue del Sprint 1*

| Producto | Repositorio | URL desplegado | Estado |
|---|---|---|---|
| Landing Page | https://github.com/InventiaStock/smartstock-landing-page | https://inventiastock.github.io/smartstock-landing-page/ | Desplegado |
| Frontend Web Application | https://github.com/InventiaStock/smartstock-frontend | — | Desplegado |
| Web Services | Pendiente de despliegue. | — | Fuera del alcance del Sprint 1 |
Nota. Elaboración propia

La configuración aplicada en el repositorio se muestra a continuación. La fuente de publicación es la rama main y el directorio raíz, y GitHub confirma la publicación del sitio. En el selector de ramas se aprecian además las ramas main y develop, que evidencian la aplicación de GitFlow sobre el repositorio.

**Figura 165**

*Configuración de GitHub Pages del repositorio smartstock-landing-page*

![Configuración de GitHub Pages del repositorio, fuente de publicación desde main](../assets/chapter-5/sprint1pagessaved.png)
Nota. Elaboración propia

**Figura 166**

*Publicación del sitio confirmada en GitHub Pages*

![Confirmación de publicación del sitio en GitHub Pages](../assets/chapter-5/sprint1pageslive.png)
Nota. Elaboración propia

Se verificó que el sitio publicado responde correctamente tanto en la página de inicio como en la página de términos y condiciones, y que la hoja de estilos y el archivo de comportamiento se sirven sin errores.

**Figura 167**

*Landing Page de SmartStock publicado en GitHub Pages*

![Sitio publicado del Landing Page funcionando correctamente](../assets/chapter-5/sprint1sitepublished.png)
Nota. Elaboración propia

#### 5.2.1.8. Team Collaboration Insights during Sprint

Durante el Sprint 1, el equipo organizó la implementación del Landing Page según los aspectos definidos en la sección 5.2.1.2. Cada integrante trabajó sobre el aspecto que lideraba y registró su aporte mediante commits propios en el repositorio smartstock-landing-page, aplicando GitFlow y Conventional Commits.

El flujo de trabajo seguido fue el siguiente: la rama develop concentró el avance acumulado, cada conjunto de cambios se desarrolló en una rama feature/ que se integró a develop sin avance rápido (`--no-ff`), de modo que el historial conserve visible el punto de integración de cada aporte, y la versión entregada se publicó desde main mediante una release branch.

**Analíticos de colaboración del repositorio del Landing Page**

La vista de contribuyentes evidencia la participación de los cinco integrantes del equipo, con el detalle de commits y de líneas agregadas y eliminadas por cada uno.

**Figura 168**

*Contribuyentes del repositorio smartstock-landing-page*

![Contribuyentes del repositorio smartstock-landing-page](../assets/chapter-5/sprint1contributors.png)
*Nota: Contribuyentes del repositorio smartstock-landing-page, los cinco integrantes del equipo registran commits propios.*

**Historial de ramas del repositorio**

El grafo de red muestra la aplicación efectiva de GitFlow: las ramas de feature nacen de develop, se integran nuevamente a ella y la rama main recibe únicamente las versiones publicadas.

**Figura 170**

*Historial de commits del repositorio smartstock-landing-page*

![Historial de commits del repositorio smartstock-landing-page (parte 1)](../assets/chapter-5/sprint1commits1.png)
![Historial de commits del repositorio smartstock-landing-page (parte 2)](../assets/chapter-5/sprint1commits2.png)
![Historial de commits del repositorio smartstock-landing-page (parte 3)](../assets/chapter-5/sprint1commits3.png)

*Nota: Comparación de commits entre la primera rama de trabajo y main, mostrando la autoría real de cada commit (autor original y quien lo integró).*


### 5.2.2. Sprint 2

#### 5.2.2.1. Sprint Planning 2

En el Sprint Planning 2 el equipo definió como meta entregar la primera versión desplegada de la Frontend Web Application de SmartStock, con las historias de Compras y Ventas como núcleo del producto y el IoT como verificación del stock físico. El sprint incluye las 23 User Stories del Product Backlog que no son del Landing Page; las 15 Technical Stories (endpoints y modelo de datos) pasan al Sprint 3, junto con los Web Services reales.

**Tabla 35**

*Sprint Planning 2*

| Campo | Detalle |
|---|---|
| Sprint # | Sprint 2 |
| Date | 2026-10-01 |
| Time | 02:00 PM |
| Location | Reunión virtual |
| Prepared By | Montañez Salinas, Lorena Ariana |
| Attendees (to planning meeting) | Lopez Rimachi, Sebastian Leonardo / Montañez Salinas, Lorena Ariana / Sanchez Osorio, Ruth Yanira / Suarez Chinga, Geraldine / Vizcarra Mamani, Candy Milagros |
| Sprint 1 – Review Summary | Durante el Sprint 1 se implementó y desplegó la primera versión del Landing Page (versión 1.0.0) en GitHub Pages, cubriendo las User Stories US16 a US24 (20 Story Points). En la revisión del Sprint 1, el docente no indicó correcciones pendientes sobre el Landing Page. |
| Sprint 1 – Retrospective Summary | Durante el Sprint 1 funcionó bien la aplicación de GitFlow, con ramas de feature integradas a develop y la versión 1.0.0 publicada desde main mediante una release branch, así como el uso de Conventional Commits y la organización del trabajo en Trello. Como aspecto a mejorar, el equipo identificó la necesidad de verificar las URLs antes de cada entrega. Para el Sprint 2, el equipo acordó: (1) construir las pantallas de Compras y Ventas desde las historias ya definidas (US26 a US32); (2) identificar las historias como US y TS y las tareas como T-US## y T-TS##; (3) trabajar cada tarea en una rama corta `feature/<contexto>-<tarea>` creada desde develop e integrada mediante pull request con merge commit (`--no-ff`), sin commits directos en main ni en develop; (4) no modificar archivos compartidos (rutas, stores, estilos y modelos) sin avisar al equipo; y (5) usar datos simulados mientras los Web Services estén en desarrollo. |
| Sprint 2 Goal | Our focus is on delivering the first deployed version of the SmartStock web application, where owners of minimarkets and bodegas register their sales and purchases and see their stock. We believe it delivers control over what enters and leaves their inventory, verified by IoT sensors, to minimarket and bodega owners. This will be confirmed when a user can sign up, register a product, a purchase and a sale, and then see the updated stock, the low-stock alert and the dashboard in the deployed frontend, without help from the development team. |
| Sprint 2 Velocity | 84 Story Points |
| Sum of Story Points | 84 (todas de User Stories) |

Nota. Elaboración propia

Durante el Sprint 1 funcionó bien la aplicación de GitFlow, con ramas de feature integradas a develop y la versión 1.0.0 publicada desde main mediante una release branch, así como el uso de Conventional Commits y la organización del trabajo en Trello. Como aspecto a mejorar, el equipo identificó la necesidad de verificar las URLs antes de cada entrega.

Para el Sprint 2, el equipo acordó: (1) construir las pantallas de Compras y Ventas desde las historias ya definidas (US26 a US32); (2) identificar las historias como US y TS y las tareas como T-US## y T-TS##; (3) trabajar cada tarea en una rama corta `feature/<contexto>-<tarea>` creada desde develop e integrada mediante pull request con merge commit (`--no-ff`), sin commits directos en main ni en develop; (4) no modificar archivos compartidos (rutas, stores, estilos y modelos) sin avisar al equipo; y (5) usar datos simulados mientras los Web Services estén en desarrollo.

#### 5.2.2.2. Aspect Leaders and Collaborators

Los aspectos de este sprint son los seis bounded contexts del frontend: IAM (registro, inicio de sesión y recuperación de contraseña); IoT Device (vinculación de sensores y estado de conexión); Alerts & Restocking (notificaciones de stock bajo, alertas por discrepancia y compra desde una alerta); Product Catalog (registro y edición de productos y umbral mínimo); Inventory Monitoring (peso actual, listado por nivel de stock, comparación físico vs. registrado, y ventas, compras y proveedores con sus movimientos de stock); y Analytics & Reporting (dashboard y reportes). Cada integrante lidera el contexto que eligió y colabora en los demás (L = líder, C = colaborador); esta distribución se refleja en la selección de tasks de la sección 5.2.2.3 y en la autoría de los commits. Dentro de Inventory Monitoring, Lorena construye Ventas, Candy construye Proveedores y Compras, y Leo conecta la alerta de stock bajo con registrar una compra (US32).

**Tabla 36**

*Matriz de liderazgo y colaboración (LACX) del Sprint 2*

| Team Member | GitHub Username | IAM | IoT Device | Alerts & Restocking | Product Catalog | Inventory Monitoring | Analytics & Reporting |
|---|---|---|---|---|---|---|---|
| Montañez Salinas, Lorena Ariana | Lore-MS | L | C | C | C | C | C |
| Sanchez Osorio, Ruth Yanira | Yiya-ciber | C | L | C | C | C | C |
| Lopez Rimachi, Sebastian Leonardo | leonardoXd1323 | C | C | L | C | C | C |
| Vizcarra Mamani, Candy Milagros | candyvizz | C | C | C | L | C | C |
| Suarez Chinga, Geraldine | geral07-UNIV | C | C | C | C | L | L |

Nota. Elaboración propia

Geraldine lidera dos aspectos y el resto uno. Ventas y Compras viven dentro de Inventory Monitoring, pero sus pantallas se reparten: Lorena construye Ventas, Candy construye Proveedores y Compras, y Leo conecta la alerta de stock bajo con registrar una compra (US32).

#### 5.2.2.3. Sprint Backlog 2

El objetivo del Sprint 2 es entregar la primera versión navegable y desplegada del frontend de SmartStock, con Compras y Ventas como núcleo. El sprint contiene las 23 User Stories del Product Backlog que no son del Landing Page (84 Story Points); las Technical Stories pasan al Sprint 3 con los Web Services reales, y en este sprint solo se incluyen sus tareas de simulación (mock), marcadas como "(mock)" y sin Story Points propios. El tablero del sprint está en Trello y su URL pública es

https://trello.com/invite/b/6ac4b28dd414f036520b5f47/ATTI194967e117cc1b0e83906e9d86df8680619E986C/sprint-backlog-2-web

![Sprint Backlog 2 en Trello](../assets/chapter-5/sprint2trello.png)

La tabla resume la carga por integrante. Las tareas se identifican como T-US##.# (historias de usuario), T-TS##.# (contratos simulados, sin puntos) y T-SH.# (setup compartido, sin historia). Los 84 Story Points corresponden solo a User Stories.

**Tabla 37**

*Carga de trabajo por integrante en el Sprint 2*

| Integrante | Contexto | User Stories | Story Points |
|---|---|---|---:|
| Lorena | IAM y pantallas de Ventas | US01, US02, US03, US26, US27, US28 | 21 |
| Ruth | IoT Device | US04, US06 | 8 |
| Leo | Alerts & Restocking | US09, US10, US12, US32 | 16 |
| Candy | Product Catalog, Proveedores y Compras (+ setup y mock server) | US05, US13, US14, US29, US30, US31 | 18 |
| Geraldine | Inventory Monitoring y Analytics & Reporting | US07, US08, US11, US15, US25 | 21 |
| **Total** | | | **84** |

Nota. Elaboración propia

**Tabla 38**

*Sprint Backlog 2*

| Sprint # | Story Id | Story Title | Task Id | Task Title | Task Description | Estimation (Hours) | Assigned To | Status |
|---:|---|---|---|---|---|---:|---|---|
| 2 | Soporte | Setup compartido | T-SH.1 | Separar traducciones por contexto y ampliar el entorno | Una carpeta de traducciones por bounded context y endpoints del Sprint 2 en el environment. | 4 | Candy | Done |
| 2 | Soporte | Setup compartido | T-SH.2 | Helpers y componentes compartidos | Helpers de error y rango de fechas; alert banner, summary card y page header; estilos compartidos. | 6 | Candy | Done |
| 2 | Soporte | Setup compartido | T-SH.3 | Modelo de movimiento de stock | Entidad StockMovement (R17) usada por ventas, compras y reportes. | 4 | Candy | Done |
| 2 | TS14 | Registro automático de movimientos (mock) | T-TS14.1 | Motor de movimientos y reglas de alerta del mock | Movimientos de stock, reglas de alerta R19–R21 y proyección de producto con estado del sensor. | 6 | Candy | Done |
| 2 | TS01 | Recepción de lecturas (mock) | T-TS01.1 | Mock POST /sensores/{id}/lecturas | Servidor json-server con token, rutas automáticas y simulador IoT. | 5 | Candy | Done |
| 2 | TS05 | Estado de sensor (mock) | T-TS05.1 | Mock GET /sensores/{id}/estado | Estado en línea/desconectado (R11) y endpoints de vinculación. | 4 | Candy | Done |
| 2 | US04 | Vinculación de sensor IoT a un producto | T-US04.1 | Diseñar vista de vinculación | Sensores disponibles, flujo de vinculación y caso de sensor ya vinculado. | 5 | Ruth | Done |
| 2 | US04 | Vinculación de sensor IoT a un producto | T-US04.2 | Modelo, API y store de dispositivos | Entidades Sensor y LinkableProduct, DevicesApi y store (R9). | 6 | Ruth | Done |
| 2 | US04 | Vinculación de sensor IoT a un producto | T-US04.3 | Validar sensor ya en uso | Rechazar vinculación e indicar que el sensor ya está en uso. | 3 | Ruth | Done |
| 2 | US06 | Estado de conexión de sensores | T-US06.1 | Vista de listado de estado | Lista de sensores con estado en línea o desconectado. | 4 | Ruth | Done |
| 2 | US06 | Estado de conexión de sensores | T-US06.2 | Regla de 5 minutos | Desconectado si no hay lecturas en 5 minutos (R11). | 3 | Ruth | Done |
| 2 | US01 | Registro de cuenta | T-US01.1 | Formulario de registro | Datos del negocio y selector de tipo de negocio. | 5 | Lorena | Done |
| 2 | US01 | Registro de cuenta | T-US01.2 | Validaciones y correo repetido | Validar campos y mostrar error de correo ya registrado. | 4 | Lorena | Done |
| 2 | US01 | Registro de cuenta | T-US01.3 | Estado de registro exitoso | Mensaje de éxito y redirección. | 3 | Lorena | Done |
| 2 | US02 | Inicio de sesión | T-US02.1 | Vista de login | Formulario con mensaje de error genérico (R3). | 4 | Lorena | Done |
| 2 | US02 | Inicio de sesión | T-US02.2 | Modelo, API y store de IAM | UserSession, IamApi y store con signIn y signUp. | 6 | Lorena | Done |
| 2 | TS04 | Login (mock) | T-TS04.1 | Mock POST /auth/login | Endpoints de login, registro y recuperación en el mock. | 4 | Lorena | Done |
| 2 | US03 | Recuperación de contraseña | T-US03.1 | Formulario de recuperación | Solicitud con el mismo mensaje neutro para cualquier correo. | 4 | Lorena | Done |
| 2 | US03 | Recuperación de contraseña | T-US03.2 | Nueva contraseña y enlace vencido | Confirmación de envío con el aviso de que el enlace vence en 24 horas (R4). | 4 | Lorena | Done |
| 2 | US26 | Registro de venta | T-US26.1 | Formulario de nueva venta | Productos, cantidades y total. | 6 | Lorena | Done |
| 2 | US26 | Registro de venta | T-US26.2 | Modelo y API de ventas | Sale, SaleItem, SaleProductOption y SalesApi. | 5 | Lorena | Done |
| 2 | US26 | Registro de venta | T-US26.3 | Store y validaciones de stock | Store de ventas; stock suficiente (R13) y producto sin precio (R14). | 5 | Lorena | Done |
| 2 | US27 | Historial de ventas | T-US27.1 | Listado de ventas | Lista con total del período. | 4 | Lorena | Done |
| 2 | US27 | Historial de ventas | T-US27.2 | Filtro por fechas y período vacío | Filtro por rango y estado vacío. | 3 | Lorena | Done |
| 2 | US28 | Detalle de una venta | T-US28.1 | Vista de detalle de venta | Detalle con los movimientos de stock generados. | 4 | Lorena | Done |
| 2 | TS07 | Registro de ventas (mock) | T-TS07.1 | Mock POST /ventas | Cada venta crea movimientos de salida (R17). | 4 | Lorena | Done |
| 2 | TS08 | Consulta de ventas (mock) | T-TS08.1 | Mock GET /ventas y /ventas/{id} | Listado y detalle de ventas. | 3 | Lorena | Done |
| 2 | US09 | Notificación por correo de stock bajo | T-US09.1 | Vista de configuración de notificaciones | Canal correo electrónico y textos en inglés y español. | 5 | Leo | Done |
| 2 | US09 | Notificación por correo de stock bajo | T-US09.2 | Store de alertas | Store con alertas y preferencias. | 4 | Leo | Done |
| 2 | US09 | Notificación por correo de stock bajo | T-US09.3 | Modelo y API de alertas | Alert, resource, assembler y AlertsApi. | 5 | Leo | Done |
| 2 | US10 | Notificación por WhatsApp de stock bajo | T-US10.1 | Canal WhatsApp en configuración | Preferencia de canal y número de WhatsApp. | 4 | Leo | Done |
| 2 | TS03 | Notificación de stock bajo (mock) | T-TS03.1 | Mock POST /notificaciones/stock-bajo | Endpoint de notificaciones en alerts.js. | 4 | Leo | Done |
| 2 | TS14 | Registro automático de movimientos (mock) | T-TS14.2 | Mock de alertas con movimientos | Alertas activas ligadas a los movimientos de stock. | 3 | Leo | Done |
| 2 | TS15 | Consulta de movimientos (mock) | T-TS15.1 | Mock GET /movimientos-stock | Listado de movimientos. | 3 | Leo | Done |
| 2 | US12 | Alerta por discrepancia de inventario | T-US12.2 | Lista de alertas activas | Alertas con discrepancia mayor al 10 %. | 5 | Leo | Done |
| 2 | US32 | Registro de compra desde una alerta de stock bajo | T-US32.1 | Botón de compra en la alerta | Acción desde la alerta de stock bajo. | 3 | Leo | Done |
| 2 | US32 | Registro de compra desde una alerta de stock bajo | T-US32.2 | Precarga de producto y proveedor | Enviar producto y proveedor al formulario de compra. | 4 | Leo | Done |
| 2 | US32 | Registro de compra desde una alerta de stock bajo | T-US32.3 | Marcar necesidad atendida | Actualizar el estado de la alerta tras registrar la compra. | 3 | Leo | Done |
| 2 | US13 | Registro de nuevo producto | T-US13.1 | Formulario de producto | Validaciones, precio de venta opcional y banner de error. | 5 | Candy | Done |
| 2 | US13 | Registro de nuevo producto | T-US13.2 | Modelo, API y store de catálogo | Product, CatalogApi y store (R5, R7). | 6 | Candy | Done |
| 2 | TS13 | Modelo de datos: productos (mock) | T-TS13.2 | Mock de productos (GET/POST/PUT /productos) | Validaciones R5 y R7 en el mock. | 4 | Candy | Done |
| 2 | US14 | Edición de producto | T-US14.1 | Formulario de edición | Precio de venta, costo de compra y proveedor habitual. | 4 | Candy | Done |
| 2 | US14 | Edición de producto | T-US14.2 | Stock de solo lectura | El stock solo cambia por movimientos (R17). | 3 | Candy | Done |
| 2 | US05 | Configuración de umbral mínimo de stock | T-US05.1 | Vista de umbral mínimo | Formulario por producto con sensor. | 4 | Candy | Done |
| 2 | US05 | Configuración de umbral mínimo de stock | T-US05.2 | Validar capacidad máxima | Rechazar umbral mayor a la capacidad (R7). | 3 | Candy | Done |
| 2 | US29 | Registro de proveedor | T-US29.1 | Formulario y listado de proveedores | Alta y lista de proveedores. | 5 | Candy | Done |
| 2 | US29 | Registro de proveedor | T-US29.2 | Proveedor duplicado | Error por proveedor repetido (R8). | 3 | Candy | Done |
| 2 | US30 | Registro y recepción de compra | T-US30.1 | Formulario de nueva compra | Productos, total y precarga desde reposición. | 6 | Candy | Done |
| 2 | US30 | Registro y recepción de compra | T-US30.2 | Modelo y API de compras | Purchase, PurchaseItem, Supplier y PurchasesApi. | 5 | Candy | Done |
| 2 | US30 | Registro y recepción de compra | T-US30.3 | Detalle y recepción | Recepción de mercadería que crea movimientos de entrada. | 6 | Candy | Done |
| 2 | US30 | Registro y recepción de compra | T-US30.4 | Store de compras | Compras, proveedores y recepción (R15, R16). | 4 | Candy | Done |
| 2 | US31 | Historial de compras | T-US31.1 | Listado de compras | Lista con filtro por fechas. | 4 | Candy | Done |
| 2 | US31 | Historial de compras | T-US31.2 | Estado vacío | Mensaje cuando no hay compras en el período. | 3 | Candy | Done |
| 2 | TS09 | Proveedores (mock) | T-TS09.1 | Mock POST/GET /proveedores | Alta y consulta de proveedores. | 3 | Candy | Done |
| 2 | TS10 | Registro de compras (mock) | T-TS10.1 | Mock POST /compras | Alta de compras. | 3 | Candy | Done |
| 2 | TS11 | Recepción de compras (mock) | T-TS11.1 | Mock PATCH /compras/{id}/recepcion | Recepción con movimientos de entrada. | 3 | Candy | Done |
| 2 | TS12 | Consulta de compras (mock) | T-TS12.1 | Mock GET /compras y /compras/{id} | Listado y detalle. | 3 | Candy | Done |
| 2 | US15 | Dashboard de inventario | T-US15.1 | Vista de dashboard | Tarjetas de resumen y Home de bodega. | 6 | Geraldine | Done |
| 2 | US15 | Dashboard de inventario | T-US15.2 | Tarjetas de ventas y compras del día | Totales del día en el dashboard. | 4 | Geraldine | Done |
| 2 | US15 | Dashboard de inventario | T-US15.3 | Modelo, API y store de analítica | DashboardSummary, Report y AnalyticsApi. | 5 | Geraldine | Done |
| 2 | US15 | Dashboard de inventario | T-US15.4 | Traducciones y estados vacíos | Textos en inglés y español. | 3 | Geraldine | Done |
| 2 | US15 | Dashboard de inventario | T-US15.5 | Mock GET /dashboard y /reportes | Reportes solo para minimarket. | 4 | Geraldine | Done |
| 2 | US25 | Reportes de consumo y movimientos | T-US25.1 | Selector de período | Rango de fechas del reporte. | 3 | Geraldine | Done |
| 2 | US25 | Reportes de consumo y movimientos | T-US25.2 | Reporte de consumo | Consumo por producto. | 5 | Geraldine | Done |
| 2 | US25 | Reportes de consumo y movimientos | T-US25.3 | Movimientos con ventas y compras | Tabla de movimientos con ventas y compras. | 5 | Geraldine | Done |
| 2 | US25 | Reportes de consumo y movimientos | T-US25.4 | Reporte sin datos | Estado vacío del período. | 3 | Geraldine | Done |
| 2 | US11 | Comparación inventario físico vs. registrado | T-US11.1 | Vista de comparación | Peso del sensor frente al stock registrado. | 6 | Geraldine | Done |
| 2 | US11 | Comparación inventario físico vs. registrado | T-US11.3 | Resaltar discrepancia | Diferencia mayor al 10 % resaltada. | 4 | Geraldine | Done |
| 2 | US11 | Comparación inventario físico vs. registrado | T-US11.4 | Modelo, API y store de stock | Comparison, SensorReading y StockApi. | 5 | Geraldine | Done |
| 2 | TS02 | Consulta de stock (mock) | T-TS02.1 | Mock GET /productos/{id}/stock | Stock y detalle de producto. | 3 | Geraldine | Done |
| 2 | TS06 | Comparación de inventario (mock) | T-TS06.1 | Mock GET /inventario/comparacion/{productoId} | Comparación con ventas y compras. | 3 | Geraldine | Done |
| 2 | US08 | Listado de productos por nivel de stock | T-US08.1 | Listado con búsqueda | Búsqueda y columna de sensor. | 4 | Geraldine | Done |
| 2 | US08 | Listado de productos por nivel de stock | T-US08.2 | Filtro por nivel de stock | Bajo, normal o sin datos. | 3 | Geraldine | Done |
| 2 | US08 | Listado de productos por nivel de stock | T-US08.3 | Columna de stock registrado | Stock actualizado por movimientos. | 3 | Geraldine | Done |
| 2 | US07 | Visualización del peso actual de un producto | T-US07.1 | Detalle con peso actual | Peso del sensor y unidades equivalentes. | 4 | Geraldine | Done |
| 2 | US07 | Visualización del peso actual de un producto | T-US07.2 | Últimas cinco lecturas | Historial corto de lecturas. | 3 | Geraldine | Done |

Nota. Elaboración propia

#### 5.2.2.4. Development Evidence for Sprint Review

Durante el Sprint 2 se implementó la Frontend Web Application de SmartStock en Vue 3 en el repositorio InventiaStock/smartstock-frontend, con las vistas, stores y servicios de IAM, IoT Device, Alerts & Restocking, Product Catalog, Inventory Monitoring (incluidas ventas, compras y proveedores) y Analytics & Reporting, consumiendo servicios simulados. Cada tarea del Sprint Backlog se desarrolló en una rama `feature/<contexto>-<tarea>` creada desde develop e integrada mediante pull request con merge commit.

La tabla presenta los commits relacionados con la implementación, organizados por rama según GitFlow y redactados bajo Conventional Commits, en inglés y en minúsculas, con el identificador de la tarea (por ejemplo T-US02.1) en el cuerpo del mensaje.

**Tabla 39**

*Commits relacionados con la implementación del Sprint 2*

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on (Date) |
|---|---|---|---|---|---|
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | ab4d22a | chore(shared): split translations per bounded context | One translations folder per context; owners edit only their own. Task: T-SH.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | 8c1e4ab | chore(shared): add sprint 2 endpoints to environment | Notifications, comparison, dashboard and reports endpoints. Task: T-SH.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | c787d93 | feat(shared): add api error and date range helpers | apiError/apiCode and DateRange helpers. Task: T-SH.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | 991c9a7 | feat(shared): add alert banner, summary card and page header | Reusable presentation components. Task: T-SH.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | b418324 | refactor(shared): extend date range filter and status tag | Initial input, new status tones and shared styles. Task: T-SH.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-sprint2-setup | 7a7f92b | feat(inventory): add stock movement model | StockMovement entity (R17). Task: T-SH.3 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-mock-server | f08d04c | chore(shared): add json-server mock backend skeleton | Server, helpers, in-memory db and scripts. Refs: T-TS01.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-mock-server | 924cf3c | feat(shared): add stock movement, alert rules and product view for the mock | Movement engine, alert rules R19-R21. Refs: T-TS14.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/shared-mock-server | 7ac6ec1 | feat(devices): add sensor readings and status mock endpoints | Readings, status and IoT simulator. Refs: T-TS01.1, T-TS05.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-register-product | e1e5428 | feat(catalog): add product model and api layer | Task: T-US13.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-register-product | 9820b9d | feat(catalog): add catalog store | Task: T-US13.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-register-product | cf0a1f9 | feat(catalog): add catalog translations | Task: T-US13.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-register-product | 07d8133 | feat(catalog): add register product view | Tasks: T-US13.1, T-US13.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-register-product | 8e169d6 | feat(catalog): add catalog mock endpoints | Refs: T-TS13.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 3732be9 | feat(inventory): add purchase and supplier model and api layer | Task: T-US30.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 7708a9f | feat(inventory): add purchases store | Task: T-US30.4 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 647e310 | feat(inventory): add purchases translations | Task: T-US29.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 651a94a | feat(inventory): add supplier list view | Tasks: T-US29.1, T-US29.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 0512742 | feat(inventory): add purchase list view | Tasks: T-US31.1, T-US31.2 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 1d07274 | feat(inventory): add new purchase view | Tasks: T-US30.1, T-US30.2, T-US30.4 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 67767bc | feat(inventory): add purchase details view | Task: T-US30.3 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-purchases | 5686709 | feat(inventory): add purchases and suppliers mock endpoints | Refs: T-TS09.1, T-TS10.1, T-TS11.1, T-TS12.1 | 04/10/2026 |
| InventiaStock/smartstock-frontend | feature/devices-sensor-linking | 0fcfc02 | feat(devices): add sensor domain model and api layer | Task: T-US04.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/devices-sensor-linking | cc49da9 | feat(devices): add devices store | Task: T-US04.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/devices-sensor-linking | c8fff55 | feat(devices): add devices translations | Task: T-US04.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/devices-sensor-linking | 6448432 | feat(devices): add sensor linking view | Tasks: T-US04.1, T-US04.2, T-US04.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-dashboard | ca31c2a | feat(analytics): add dashboard and report model and api layer | Task: T-US15.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-dashboard | 8510857 | feat(analytics): add analytics store | Task: T-US15.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-dashboard | de9d94e | feat(analytics): add analytics translations | Task: T-US15.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-dashboard | b947557 | feat(analytics): add dashboard view | Tasks: T-US15.1, T-US15.2, T-US15.4 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-dashboard | 98a5d9a | feat(analytics): add dashboard and reports mock endpoints | Refs: T-US15.5 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-comparison | de281d6 | feat(inventory): add stock comparison model and api layer | Task: T-US11.4 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-comparison | 05e9775 | feat(inventory): add stock store | Task: T-US11.4 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-comparison | 1231e51 | feat(inventory): add stock translations | Task: T-US11.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-comparison | 0d6b028 | feat(inventory): add stock comparison view | Tasks: T-US11.1, T-US11.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-comparison | a8612a5 | feat(inventory): add stock and comparison mock endpoints | Refs: T-TS02.1, T-TS06.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/devices-sensor-status | cf52668 | feat(devices): add sensor status list view | Tasks: T-US06.1, T-US06.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-edit-product | 38a084d | feat(catalog): add edit product view | Tasks: T-US14.1, T-US14.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/catalog-min-threshold | 039ef29 | feat(catalog): add minimum threshold view | Tasks: T-US05.1, T-US05.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-email | 09d74f5 | feat(alerts): add alert model and api layer | Task: T-US09.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-email | 93adae7 | feat(alerts): add alerts store | Task: T-US09.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-email | 58411f9 | feat(alerts): add alerts translations | Task: T-US09.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-email | 3d58c28 | feat(alerts): add notification settings view | Tasks: T-US09.1, T-US10.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-email | 2707a3d | feat(alerts): add alerts and notifications mock endpoints | Refs: T-TS03.1, T-TS14.2, T-TS15.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/analytics-reports | 8c113c5 | feat(analytics): add reports view | Tasks: T-US25.1, T-US25.2, T-US25.3, T-US25.4 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-product-list | b43a5e6 | feat(inventory): add product list view with stock levels | Tasks: T-US08.1, T-US08.2, T-US08.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-stock-weight | cb46b1f | feat(inventory): add product details view with current weight | Tasks: T-US07.1, T-US07.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/alerts-active-list | 0ecbd35 | feat(alerts): add active alerts list view | Tasks: T-US12.2, T-US32.1, T-US32.2, T-US32.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-login | dfe5ad4 | feat(iam): add user session model and auth api | Task: T-US02.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-login | 100a89f | feat(iam): add iam store | Task: T-US02.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-login | dcb278e | feat(iam): add iam translations | Task: T-US02.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-login | 067bea8 | feat(iam): add login view | Tasks: T-US02.1, T-US02.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-login | 3894f21 | feat(iam): add auth mock endpoints | Refs: T-TS04.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | ae1ffeb | feat(inventory): add sale model and api layer | Task: T-US26.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | 0989723 | feat(inventory): add sales store | Task: T-US26.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | 75d10bf | feat(inventory): add sales translations | Task: T-US26.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | 2ad80c8 | feat(inventory): add sales list view | Tasks: T-US27.1, T-US27.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | 287e64a | feat(inventory): add new sale view | Tasks: T-US26.1, T-US26.2, T-US26.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | e41b69a | feat(inventory): add sale details view | Task: T-US28.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/inventory-sales | fa72453 | feat(inventory): add sales mock endpoints | Refs: T-TS07.1, T-TS08.1 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-register | c9f6cac | feat(iam): add registration view | Tasks: T-US01.1, T-US01.2, T-US01.3 | 05/10/2026 |
| InventiaStock/smartstock-frontend | feature/iam-password-recovery | 438616d | feat(iam): add password recovery view | Tasks: T-US03.1, T-US03.2 | 05/10/2026 |
| InventiaStock/smartstock-frontend | release/1.0.0 | 77fbb97 | chore(release): set github pages base path | Use /smartstock-frontend/ in build and preview. Task: T-SH.1 | 06/10/2026 |
| InventiaStock/smartstock-frontend | release/1.0.0 | da7d092 | chore(release): add 404 fallback for the vue router | Copy index.html to 404.html after the build. Task: T-SH.1 | 06/10/2026 |
| InventiaStock/smartstock-frontend | release/1.0.0 | 1e95fc0 | chore(release): add github pages deployment workflow | Build and publish dist/ when main changes. Task: T-SH.1 | 06/10/2026 |
| InventiaStock/smartstock-frontend | release/1.0.0 | 1cd9852 | chore(release): set fake api url for production | The api url is read only from VITE_API_BASE_URL. Task: T-SH.1 | 06/10/2026 |

Nota. Elaboración propia

La tabla sigue el orden en que las ramas se integraron a develop: primero las dos ramas compartidas y luego los contextos. Son 20 ramas (19 de feature y `release/1.0.0`) y 66 commits.

#### 5.2.2.5. Execution Evidence for Sprint Review

En este sprint el frontend alcanzó las vistas de los seis contextos funcionando con datos simulados: registro e inicio de sesión, ventas, productos, proveedores y compras, sensores, alertas, stock, dashboard y reportes. Cada captura se rotula con la historia que cubre. El video que muestra la visualización y la navegación logradas en el sprint está en upc-pre-202620-1asi0730-8168-inventiastock-product-navigation-sprint-2.mp4

**Tabla 40**

*Evidencia de ejecución por contexto e historia de usuario del Sprint 2*

| Contexto | Historia | Ruta | La captura debe mostrar | Figura |
|---|---|---|---|---:|
| IAM | US01 Registro de cuenta | `/sign-up` | Formulario con tipo de negocio y el error de correo en uso | 161 |
| IAM | US02 Inicio de sesión | `/sign-in` | Login y el mensaje de credenciales incorrectas | 162 |
| IAM | US03 Recuperación de contraseña | `/forgot-password` | Solicitud del enlace y restablecimiento | 163 |
| Ventas | US26, US27 y US28 | `/sales`, `/sales/new`, `/sales/:id` | Venta registrada, rechazo por stock insuficiente, historial por fechas y detalle | 164 |
| IoT Device | US04 Vinculación de sensor | `/sensors/link` | Selección de sensor y producto, y error de sensor en uso | 165 |
| IoT Device | US06 y US07 Estado y peso actual | `/sensors` | Sensores en línea y desconectados, y peso con su equivalente en unidades | 166 |
| Alerts & Restocking | US09 y US10 Notificaciones | `/settings` | Canales de correo y WhatsApp configurados | 167 |
| Alerts & Restocking | US12 y US32 Alertas y compra desde alerta | `/alerts` | Alerta de stock bajo o discrepancia y el botón que abre el registro de compra | 168 |
| Product Catalog | US13, US14 y US05 Productos | `/products` | Registro, edición y umbral mínimo con su error de validación | 169 |
| Proveedores y Compras | US29, US30 y US31 | `/purchases`, `/purchases/new`, `/purchases/suppliers` | Proveedor creado, compra pendiente, compra recibida e historial por fechas | 170 |
| Inventory Monitoring | US08 y US11 | `/products`, `/comparison` | Niveles de stock y comparación físico vs. registrado (solo minimarket) | 171 |
| Analytics & Reporting | US15 y US25 | `/dashboard`, `/reports` | Tarjetas del día con ventas y compras, y reporte por período | 172 |

Nota. Elaboración propia

**Figura 161**

*Registro de cuenta con selección de tipo de negocio (US01)*

![Registro de cuenta con selección de tipo de negocio](../assets/chapter-5/sprint2signup.png)

Nota. Elaboración propia

**Figura 162**

*Inicio de sesión con mensaje de credenciales incorrectas (US02)*

![Inicio de sesión con mensaje de credenciales incorrectas](../assets/chapter-5/sprint2signin.png)

Nota. Elaboración propia

**Figura 163**

*Recuperación de contraseña: solicitud del enlace y confirmación de envío (US03)*

![Recuperación de contraseña](../assets/chapter-5/sprint2forgotpassword.png)

Nota. Elaboración propia

**Figura 164**

*Ventas: (a) venta registrada, (b) rechazo por stock insuficiente, (c) historial por fechas y (d) detalle con movimiento de salida (US26, US27, US28)*

![Ventas: historial de ventas](../assets/chapter-5/sprint2sales1.png)

![Ventas: rechazo por stock insuficiente](../assets/chapter-5/sprint2sales2.png)

![Ventas: historial por fechas](../assets/chapter-5/sprint2sales3.png)

![Ventas: detalle de la venta](../assets/chapter-5/sprint2sales4.png)

Nota. Elaboración propia

**Figura 165**

*Vinculación de sensor a un producto y error de sensor en uso (US04)*

![Vinculación de sensor a un producto](../assets/chapter-5/sprint2linksensor1.png)

![Error de sensor en uso](../assets/chapter-5/sprint2linksensor2.png)

Nota. Elaboración propia

**Figura 166**

*Estado de conexión de sensores en línea y desconectados (US06)*

![Estado de conexión de sensores](../assets/chapter-5/sprint2sensors.png)

Nota. Elaboración propia

**Figura 167**

*Configuración de notificaciones por correo y WhatsApp (US09, US10)*

![Configuración de notificaciones](../assets/chapter-5/sprint2settings.png)

Nota. Elaboración propia

**Figura 168**

*Alertas activas y botón de compra desde una alerta de stock bajo (US12, US32)*

![Alertas activas](../assets/chapter-5/sprint2alerts.png)

Nota. Elaboración propia

**Figura 169**

*Catálogo: (a) registro de producto, (b) edición con stock de solo lectura (US13, US14)*

![Registro de producto](../assets/chapter-5/sprint2productnew.png)

![Edición de producto con stock de solo lectura](../assets/chapter-5/sprint2productedit.png)

Nota. Elaboración propia

**Figura 170**

*Proveedores y compras: (a) proveedor creado, (b) compra pendiente, (c) compra recibida y (d) historial por fechas (US29, US30, US31)*

![Proveedores y compras: proveedor creado](../assets/chapter-5/sprint2purchases1.png)

![Proveedores y compras: compra pendiente](../assets/chapter-5/sprint2purchases2.png)

![Proveedores y compras: compra recibida](../assets/chapter-5/sprint2purchases3.png)

![Proveedores y compras: historial por fechas](../assets/chapter-5/sprint2purchases4.png)

Nota. Elaboración propia

**Figura 171**

*Monitoreo de inventario: (a) productos por nivel de stock, (b) detalle con peso actual y (c) comparación físico vs. registrado (US07, US08, US11)*

![Monitoreo de inventario: productos por nivel de stock](../assets/chapter-5/sprint2inventory1.png)

![Monitoreo de inventario: detalle con peso actual](../assets/chapter-5/sprint2inventory2.png)

![Monitoreo de inventario: comparación físico vs. registrado](../assets/chapter-5/sprint2inventory3.png)

Nota. Elaboración propia

**Figura 172**

*Dashboard con ventas y compras del día, y reporte por período (US15, US25)*

![Dashboard con ventas y compras del día](../assets/chapter-5/sprint2dashboard.png)

![Reporte por período](../assets/chapter-5/sprint2reports.png)

Nota. Elaboración propia

**Figura 173**

*Menú lateral según tipo de negocio: (a) bodega y (b) minimarket (US01)*

![Menú lateral de bodega](../assets/chapter-5/sprint2menubodega.png)

![Menú lateral de minimarket](../assets/chapter-5/sprint2menuminimarket.png)

Nota. Elaboración propia

#### 5.2.2.6. Services Documentation Evidence for Sprint Review

En el Sprint 2 el equipo documentó con OpenAPI los contratos de los endpoints que las pantallas consumen a través de la Fake API: los de las Technical Stories TS01 a TS15 y los de autenticación que usan las pantallas de registro y recuperación (21 operaciones). Los Web Services reales (ASP.NET Core) se implementarán en el Sprint 3 con el mismo contrato; por eso aún no existe el repositorio de Web Services ni hay commits de documentación en este sprint. La especificación de los Web Services se redactó en formato OpenAPI 3.0.3 utilizando Swagger Editor y se visualiza mediante Swagger UI (Figuras 174 y 175). Los endpoints documentados corresponden a los contratos que el frontend consume actualmente a través de la Fake API; su implementación real en el backend se realizará en el Sprint 3. Los contratos se documentan con el prefijo `/api` del backend real; la Fake API desplegada los expone en la raíz, sin ese prefijo (por ejemplo, `POST /auth/login`).

**Tabla 41**

*Documentación de los endpoints de los Web Services del Sprint 2*

| Endpoint | Método | Acción | Parámetros | Ejemplo de request | Response y explicación | TS |
|---|---|---|---|---|---|---|
| `/api/auth/register` | POST | Registra una cuenta | — | `{ "businessName": "Bodega Luna", "email": "ana@bodega.pe", "password": "•••", "businessType": "bodega" }` | 201 con la sesión { token, email, businessName, businessType }; 400 si faltan datos; 409 si el correo ya está registrado | TS04 |
| `/api/auth/forgot-password` | POST | Solicita el enlace de recuperación | — | `{ "email": "ana@bodega.pe" }` | 200 con { sent: true, email, expiresInHours: 24 }; la respuesta es la misma si el correo no existe (R4) | TS04 |
| `/api/auth/login` | POST | Valida credenciales | — | `{ "email": "ana@bodega.pe", "password": "•••" }` | 200 con la sesión { token, email, businessName, businessType }; 401 INVALID_CREDENTIALS si las credenciales son incorrectas, sin indicar cuál falló (R3) | TS04 |
| `/api/ventas` | POST | Registra una venta | — | `{ "items": [{ "productoId": 3, "cantidad": 2, "precioUnitario": 4.5 }] }`. Sin precioUnitario el mock responde 422 | 201 con { id } del comprobante (ej. R-00042); 400 si no hay ítems o la cantidad es inválida; 422 si la cantidad supera el stock (indica producto y stock disponible) o si el producto no tiene precio de venta (R14) | TS07 |
| `/api/ventas` | GET | Lista las ventas | desde, hasta (fecha) | — | 200 con la lista de ventas del rango | TS08 |
| `/api/ventas/{id}` | GET | Detalle de una venta | id (ruta) | — | 200 con ítems, precios y total; 404 si no existe | TS08 |
| `/api/proveedores` | POST | Registra un proveedor | — | `{ "nombre": "Distribuidora Sol", "telefono": "987654321" }` | 201 con el proveedor; 409 si ya existe el mismo nombre y teléfono | TS09 |
| `/api/proveedores` | GET | Lista los proveedores | — | — | 200 con la lista de proveedores | TS09 |
| `/api/compras` | POST | Registra una compra pendiente | — | `{ "proveedorId": 1, "items": [{ "productoId": 3, "cantidad": 24, "costoUnitario": 2.5 }] }` | 201 con la orden (PO-00031) en estado pendiente, sin cambiar el stock; 422 si no tiene ítems | TS10 |
| `/api/compras` | GET | Lista las compras | desde, hasta (fecha) | — | 200 con la lista de compras del rango | TS12 |
| `/api/productos` | GET | Lista los productos | — | — | 200 con la lista de productos, con su stock registrado y su sensor vinculado (si lo tienen) | TS13 |
| `/api/productos` | POST | Registra un producto | — | `{ "nombre": "Rice 1 kg", "categoria": "Grocery", "pesoUnitario": 1, "precioVenta": 4.5, "costoCompra": 3.2, "umbralMinimo": 5, "capacidadMaxima": 100 }` | 201 con el producto creado (el stock arranca en 0 y sin sensor); 400 INVALID_PRODUCT con el detalle de errores por campo si incumple R5 o R7 | TS13 |
| `/api/compras/{id}` | GET | Detalle de una compra | id (ruta) | — | 200 con ítems y estado; 404 si no existe | TS12 |
| `/api/compras/{id}/recepcion` | PATCH | Recibe la compra | id (ruta) | — | 200 con la compra recibida y el stock sumado; 409 si ya fue recibida | TS11 |
| `/api/sensores/{id}/lecturas` | POST | Recibe una lectura de peso | id (ruta) | `{ "pesoKg": 12.4, "fecha": "2026-10-04T10:15:00" }` | 201 con el id de la lectura; 404 si el sensor no existe | TS01 |
| `/api/sensores/{id}/estado` | GET | Estado del sensor | id (ruta) | — | 200 con estado (en línea o desconectado) y última lectura | TS05 |
| `/api/productos/{id}` | PUT | Edita un producto | id (ruta) | `{ "precioVenta": 5.2, "costoCompra": 3.5, "proveedorHabitual": "Distribuidora Sol" }` | 200 con el producto actualizado; 400 INVALID_PRODUCT; 404 si no existe. Nunca cambia el stock ni el sensor: el stock solo se mueve por movimientos (R17) | TS13 |
| `/api/productos/{id}/stock` | GET | Stock registrado | id (ruta) | — | 200 con el stock y su nivel | TS02 |
| `/api/inventario/comparacion/{productoId}` | GET | Compara peso físico y registrado | productoId (ruta) | — | 200 con ambos valores y la diferencia porcentual | TS06 |
| `/api/notificaciones/stock-bajo` | POST | Notifica stock bajo | — | `{ "productoId": 3, "canal": "email" }` | 200 con la notificación enviada por los canales activos | TS03 |
| `/api/movimientos-stock` | GET | Lista los movimientos de stock | desde, hasta (fecha) | — | 200 con entradas, salidas y ajustes del periodo | TS15 |

Nota. Elaboración propia

**Tabla 42**

*Tabla Relación de endpoints*

| Contexto | Recurso | Acciones | TS |
|---|---|---|---|
| IAM | `/api/auth/login`, `/register`, `/forgot-password` | POST | TS04 |
| IoT Device | `/api/sensores/{id}/lecturas` | POST | TS01 |
| IoT Device | `/api/sensores/{id}/estado` | GET | TS05 |
| Product Catalog | `/api/productos`, `/api/productos/{id}` | GET, POST, PUT | TS13 |
| Inventory Monitoring | `/api/productos/{id}/stock` | GET | TS02 |
| Inventory Monitoring | `/api/inventario/comparacion/{productoId}` | GET | TS06 |
| Inventory – Ventas | `/api/ventas`, `/api/ventas/{id}` | GET, POST / GET | TS07, TS08 |
| Inventory – Compras | `/api/proveedores` | GET, POST | TS09 |
| Inventory – Compras | `/api/compras`, `/api/compras/{id}` | GET, POST / GET | TS10, TS12 |
| Inventory – Compras | `/api/compras/{id}/recepcion` | PATCH | TS11 |
| Inventory – Movimientos | `/api/movimientos-stock` | GET | TS15 |
| Alerts & Restocking | `/api/notificaciones/stock-bajo` | POST | TS03 |

Nota. Elaboración propia

**Figura 174**

*Documentación OpenAPI de los endpoints del Sprint 2 en Swagger Editor*

![Documentación OpenAPI en Swagger Editor](../assets/chapter-5/sprint2swagger1.png)

Nota. Elaboración propia

**Figura 175**

*Detalle del endpoint POST /api/ventas con ejemplo de solicitud y respuestas documentadas*

![Detalle del endpoint POST /api/ventas](../assets/chapter-5/sprint2swagger2.png)

Nota. Elaboración propia

#### 5.2.2.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 2 el alcance de despliegue correspondió a la primera versión de la Frontend Web Application, publicada en GitHub Pages desde la rama main, a la que se integró mediante la rama `release/1.0.0` (PR #20) y quedó etiquetada como v1.0.0. El Landing Page se mantiene en la versión 1.0.0 del Sprint 1 y los Web Services no forman parte de este sprint.

**Tabla 43**

*Evidencia de despliegue del Sprint 2*

| Producto | Repositorio | URL desplegada | Versión | Estado |
|---|---|---|---|---|
| Landing Page | https://github.com/InventiaStock/smartstock-landing-page | https://inventiastock.github.io/smartstock-landing-page/ | v1.0.0 | Desplegado en el Sprint 1, sin cambios |
| Frontend Web Application | https://github.com/InventiaStock/smartstock-frontend | https://inventiastock.github.io/smartstock-frontend/ | v1.0.0 | Primera versión desplegada |
| Fake API (json-server) | https://github.com/InventiaStock/smartstock-frontend/tree/main/server | https://smartstock-fake-api.onrender.com | v1.0.0 | Desplegada |
| Web Services | [aún no creado; ASP.NET Core] | — | — | Previsto para el Sprint 3 |

Nota. Elaboración propia

Las actividades de despliegue fueron: (1) habilitar GitHub Pages con *Source: GitHub Actions*; (2) crear el workflow `deploy.yml` («Deploy frontend to GitHub Pages»), que al integrar en main ejecuta un job *build* (Node 22, `npm install`, `npm run build`) y un job *deploy*; (3) preparar `release/1.0.0` con cuatro commits de la tarea T-SH.1: ruta base `/smartstock-frontend/` en `vite.config.js` y el router, copia de `index.html` como `404.html` mediante el script `postbuild`, el workflow, y la URL de la Fake API en `.env.production`; y (4) verificar la URL pública. En la primera ejecución el job *deploy* fue rechazado por las reglas de protección del entorno `github-pages`, que no permitían la rama main; se agregó main a las ramas permitidas y la reejecución del workflow terminó con éxito.

Como json-server no corre en GitHub Pages, la Fake API se publicó como Web Service de Node en Render (plan gratuito): repositorio InventiaStock/smartstock-frontend, rama main, build `npm install --include=dev`, inicio `node server/server.js` y variables `NODE_VERSION=22` y `SIMULATE=1`. Implementa los contratos documentados en 5.2.2.6 y, al ser plan gratuito, se suspende tras unos 15 minutos sin uso: la primera petición tarda cerca de un minuto y sus datos en memoria se reinician. Cuando exista el backend, solo cambia `VITE_API_BASE_URL` en `.env.production`.

El despliegue se verificó abriendo la URL pública, iniciando sesión, navegando a Ventas y recargando la página (lo que prueba el `404.html`), registrando una venta de prueba y confirmando en la pestaña Network que las peticiones van a la Fake API.

**Figura 176**

*Configuración de GitHub Pages con GitHub Actions como fuente*

![Configuración de GitHub Pages con GitHub Actions como fuente](../assets/chapter-5/sprint2pagesconfig.png)

*Nota.* Pages del repositorio InventiaStock/smartstock-frontend; la aplicación se publica con el workflow `deploy.yml` al integrar en main.

**Figura 177**

*Ejecución del workflow «Deploy frontend to GitHub Pages» con los jobs build y deploy exitosos*

![Ejecución del workflow Deploy frontend to GitHub Pages](../assets/chapter-5/sprint2deployworkflow.png)

*Nota.* Ejecución disparada por el merge del PR #20 en main. En la primera corrida, deploy fue rechazado por las reglas del entorno github-pages (no permitían main); tras permitirla, la reejecución terminó con éxito en 19 s.

**Figura 178**

*Fake API desplegada en Render (Live, rama main)*

![Fake API desplegada en Render](../assets/chapter-5/sprint2render.png)

*Nota.* Web Service de Node, plan Free, repositorio InventiaStock/smartstock-frontend, rama main, URL https://smartstock-fake-api.onrender.com.

**Figura 179**

*Verificación de la Fake API desplegada*

![Verificación de la Fake API desplegada](../assets/chapter-5/sprint2fakeapi.png)

*Nota.* `POST /auth/forgot-password` responde `sent: True` y `expiresInHours: 24`.

**Figura 180**

*Frontend Web Application funcionando en su URL pública*

![Dashboard del frontend en su URL pública](../assets/chapter-5/sprint2dashboardlive.png)

![Recarga con F5 en /sales](../assets/chapter-5/sprint2saleslive.png)

*Nota.* (a) Dashboard en inventiastock.github.io/smartstock-frontend/dashboard con datos de la Fake API; (b) recarga con F5 en /sales, que funciona gracias a `404.html`.

#### 5.2.2.8. Team Collaboration Insights during Sprint

Durante el Sprint 2, el equipo organizó la implementación según los aspectos definidos en la sección 5.2.2.2. Cada integrante trabajó sobre el contexto que lideraba y registró su aporte mediante commits propios en el repositorio InventiaStock/smartstock-frontend, aplicando GitFlow y Conventional Commits.

El flujo de trabajo seguido se resume en la siguiente tabla:

**Tabla 44**

*Flujo de ramas de GitFlow seguido en el Sprint 2*

| Rama | Nace de | Se integra en | Regla |
|---|---|---|---|
| `main` | — | — | Recibe únicamente las versiones publicadas; protegida, solo se modifica mediante pull request. |
| `develop` | — | — | Concentra el avance acumulado del sprint; protegida, solo se modifica mediante pull request. |
| `feature/<contexto>-<tarea>` | `develop` | `develop` | Una rama corta por tarea del Sprint Backlog; se integra mediante pull request revisado por otro integrante, con merge commit (`--no-ff`). |
| `release/<x.y.z>` | `develop` | `main` y de vuelta a `develop` | Prepara la versión a entregar; al integrarse en main se etiqueta con versionado semántico (`vX.Y.Z`). |

Nota. Elaboración propia

Los mensajes de commit siguen Conventional Commits (`feat`, `fix`, `docs`, `refactor`, `test`, `chore`), en inglés, con el contexto como alcance, por ejemplo `feat(iam): add login view`.

**Analíticos de colaboración de los repositorios**

La vista de contribuyentes de GitHub muestra a cuatro de los cinco integrantes. Los seis commits de @leonardoXd1323 (ramas feature/alerts-email y feature/alerts-active-list) no se atribuyen a su cuenta porque se realizaron con un correo de git mal configurado; su participación se evidencia en la vista Pulse (cinco autores), en los pull requests #12 y #17 y en la tabla 39. El correo ya fue corregido para los siguientes sprints.

**Figura 181**

*Contributors del repositorio InventiaStock/smartstock-frontend*

![Contributors del repositorio smartstock-frontend](../assets/chapter-5/sprint2contributors.png)

*Nota.* Elaboración propia

**Figura 183**

*Pulse del repositorio InventiaStock/smartstock-frontend: cinco autores y 67 commits*

![Pulse del repositorio smartstock-frontend](../assets/chapter-5/sprint2pulse.png)

*Nota.* Elaboración propia

**Historial de ramas de los repositorios**

El grafo de red muestra la aplicación efectiva de GitFlow: las ramas de feature nacen de develop, se integran nuevamente a ella mediante merge commits, y la rama main recibe únicamente las versiones publicadas.

**Figura 184**

*Network graph del repositorio InventiaStock/smartstock-frontend*

![Network graph del repositorio smartstock-frontend](../assets/chapter-5/sprint2network.png)

*Nota.* Elaboración propia