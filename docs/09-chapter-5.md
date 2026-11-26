
# Capítulo V: Product Implementation, Validation & Deployment

En este capítulo se explica y evidencia el proceso de implementar,
comprobar, desplegar y validar la solución de SmartStock, compuesta por
el Landing Page, los RESTful Web Services y la Frontend Web Application,
todos ellos con diseño web responsive. El Landing Page presenta el
modelo de negocio y da acceso a la aplicación web. Los procesos del
negocio digital, tanto los procesos core como los de soporte
(autenticación y autorización, suscripciones, entre otros), están
soportados por la Frontend Web Application y los RESTful Web Services.

## 5.1. Software Configuration Management

En esta sección se establecen las decisiones y convenciones que permiten
mantener la consistencia del producto durante todo su ciclo de vida,
abarcando la configuración del ambiente de desarrollo, la gestión del
código fuente, las convenciones de estilo de código y la configuración
del despliegue.

### 5.1.1. Software Development Environment Configuration 

A continuación se detallan los productos de software que utilizan los
miembros del equipo para colaborar en el ciclo de vida del producto
digital, agrupados por tipo de actividad, indicando el propósito de uso
en el proyecto y la ruta de referencia o de descarga según corresponda.

**Project Management**

**Tabla 20**

*Herramientas de Project Management*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>Trello</td>
<td>Gestión del Product Backlog y de los Sprint Backlogs mediante tableros por sprint, con el registro de los work-items y su estado.</td>
<td><a href="https://trello.com/" style="color:#2563eb">https://trello.com/</a></td>
</tr>
<tr>
<td>Microsoft Teams</td>
<td>Realización de las sesiones síncronas del equipo, incluyendo Sprint Planning, Sprint Review y Retrospective.</td>
<td><a href="https://www.microsoft.com/microsoft-teams" style="color:#2563eb">https://www.microsoft.com/microsoft-teams</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Requirements Management**

**Tabla 21**

*Herramientas de Requirements Management*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>UXPressia</td>
<td>Elaboración de los User Personas, Empathy Maps, User Journey Maps e Impact Maps de los segmentos objetivo.</td>
<td><a href="https://uxpressia.com/" style="color:#2563eb">https://uxpressia.com/</a></td>
</tr>
<tr>
<td>Miro</td>
<td>Realización de las sesiones de Big Picture Event Storming y Design-Level Event Storming.</td>
<td><a href="https://miro.com/" style="color:#2563eb">https://miro.com/</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Product UX/UI Design**

**Tabla 22**

*Herramientas de Product UX/UI Design*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>Figma</td>
<td>Elaboración de los wireframes, mock-ups y prototipos del Landing Page y de la Web Application, en sus versiones para Desktop y Mobile Web Browser.</td>
<td><a href="https://www.figma.com/" style="color:#2563eb">https://www.figma.com/</a></td>
</tr>
<tr>
<td>FigJam</td>
<td>Elaboración de los Wireflow Diagrams y de los User Flow Diagrams de la Web Application.</td>
<td><a href="https://www.figma.com/figjam" style="color:#2563eb">https://www.figma.com/figjam</a></td>
</tr>
<tr>
<td>LucidChart</td>
<td>Elaboración de los Class Diagrams de UML y de los Database Diagrams de cada bounded context.</td>
<td><a href="https://www.lucidchart.com/" style="color:#2563eb">https://www.lucidchart.com/</a></td>
</tr>
<tr>
<td>Structurizr</td>
<td>Elaboración de los diagramas de C4 Model en sus niveles de Context, Container y Component.</td>
<td><a href="https://structurizr.com/" style="color:#2563eb">https://structurizr.com/</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Software Development**

**Tabla 23**

*Herramientas de Software Development*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>JetBrains Rider (o Visual Studio 2022)</td>
<td>IDE para implementar los Web Services en C# con ASP.NET Core. Licencia educativa</td>
<td><a href="https://www.jetbrains.com/rider/" style="color:#2563eb">https://www.jetbrains.com/rider/</a></td>
</tr>
<tr>
<td>WebStorm (o Visual Studio Code)</td>
<td>IDE de la Frontend Web Application en Vue y del Landing Page</td>
<td><a href="https://www.jetbrains.com/webstorm/" style="color:#2563eb">https://www.jetbrains.com/webstorm/</a></td>
</tr>
<tr>
<td>.NET 9 SDK</td>
<td>Compilación y ejecución de los Web Services</td>
<td><a href="https://dotnet.microsoft.com/download/dotnet/9.0" style="color:#2563eb">https://dotnet.microsoft.com/download/dotnet/9.0</a></td>
</tr>
<tr>
<td>ASP.NET Core 9 y Entity Framework Core 9</td>
<td>Framework del RESTful API y persistencia de datos</td>
<td><a href="https://learn.microsoft.com/aspnet/core" style="color:#2563eb">https://learn.microsoft.com/aspnet/core</a></td>
</tr>
<tr>
<td>Pomelo.EntityFrameworkCore.MySql</td>
<td>Proveedor de EF Core para MySQL</td>
<td><a href="https://github.com/PomeloFoundation/Pomelo.EntityFrameworkCore.MySql" style="color:#2563eb">https://github.com/PomeloFoundation/Pomelo.EntityFrameworkCore.MySql</a></td>
</tr>
<tr>
<td>MySQL Community Server 8 y MySQL Workbench</td>
<td>Base de datos relacional y diagramas de base de datos</td>
<td><a href="https://dev.mysql.com/downloads/" style="color:#2563eb">https://dev.mysql.com/downloads/</a></td>
</tr>
<tr>
<td>Node.js y npm</td>
<td>Entorno de ejecución del frontend y del simulador IoT</td>
<td><a href="https://nodejs.org/en/download" style="color:#2563eb">https://nodejs.org/en/download</a></td>
</tr>
<tr>
<td>Vue 3 y Vite</td>
<td>Framework y empaquetador de la Frontend Web Application</td>
<td><a href="https://vuejs.org" style="color:#2563eb">https://vuejs.org</a></td>
</tr>
<tr>
<td>PrimeVue</td>
<td>Biblioteca de componentes de interfaz basada en Material Design</td>
<td><a href="https://primevue.org" style="color:#2563eb">https://primevue.org</a></td>
</tr>
<tr>
<td>Postman y archivos .http</td>
<td>Verificación manual de solicitudes y respuestas de los endpoints</td>
<td><a href="https://www.postman.com/downloads" style="color:#2563eb">https://www.postman.com/downloads</a></td>
</tr>
<tr>
<td>xUnit</td>
<td>Pruebas unitarias de las reglas de negocio</td>
<td><a href="https://xunit.net" style="color:#2563eb">https://xunit.net</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Software Documentation**

**Tabla 24**

*Herramientas de Software Documentation*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>OpenAPI (Microsoft.AspNetCore.OpenApi) y Scalar</td>
<td>Generación y publicación de la documentación del RESTful API bajo la especificación OpenAPI, visualizada con Scalar</td>
<td><a href="https://scalar.com/docs-for/dotnet" style="color:#2563eb">https://scalar.com/docs-for/dotnet</a></td>
</tr>
<tr>
<td>GitHub</td>
<td>Alojamiento del informe en Markdown y de la documentación de cada repositorio</td>
<td><a href="https://github.com/InventiaStock" style="color:#2563eb">https://github.com/InventiaStock</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Software Deployment**

**Tabla 25**

*Herramientas de Software Deployment*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Propósito de uso en el proyecto</th>
<th>Ruta</th>
</tr>
<tr>
<td>GitHub Pages y GitHub Actions</td>
<td>Publicación del Landing Page y de la Frontend Web Application</td>
<td><a href="https://pages.github.com" style="color:#2563eb">https://pages.github.com</a></td>
</tr>
<tr>
<td>Render (Docker)</td>
<td>Despliegue de los Web Services</td>
<td><a href="https://render.com" style="color:#2563eb">https://render.com</a></td>
</tr>
<tr>
<td>Aiven for MySQL</td>
<td>Base de datos MySQL gestionada para los Web Services desplegados</td>
<td><a href="https://aiven.io" style="color:#2563eb">https://aiven.io</a></td>
</tr>
<tr>
<td>Docker</td>
<td>Contenedor de los Web Services y entorno local con MySQL</td>
<td><a href="https://www.docker.com" style="color:#2563eb">https://www.docker.com</a></td>
</tr>
<tr>
<td>Git</td>
<td>Sistema de control de versiones de cada integrante</td>
<td><a href="https://git-scm.com/downloads" style="color:#2563eb">https://git-scm.com/downloads</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

### 5.1.2. Source Code Management 

El equipo utiliza GitHub como plataforma de alojamiento y Git como
sistema de control de versiones. Los repositorios del proyecto
pertenecen a la organización pública InventiaStock y se organizan en un
repositorio por producto, además del repositorio de documentación del
informe.

**Tabla 26**

*Repositorios del proyecto por producto*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Repositorio</th>
</tr>
<tr>
<td>Project Report</td>
<td><a href="https://github.com/InventiaStock/smartstock-docs.git" style="color:#2563eb">https://github.com/InventiaStock/smartstock-docs.git</a></td>
</tr>
<tr>
<td>Landing Page</td>
<td><a href="https://github.com/InventiaStock/smartstock-landing-page.git" style="color:#2563eb">https://github.com/InventiaStock/smartstock-landing-page.git</a></td>
</tr>
<tr>
<td>Frontend Web Application</td>
<td><a href="https://github.com/InventiaStock/smartstock-frontend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-frontend</a></td>
</tr>
<tr>
<td>Web Services</td>
<td><a href="https://github.com/InventiaStock/smartstock-backend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-backend</a></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**GitFlow como workflow de control de versiones**

El equipo aplica GitFlow, siguiendo el modelo de ramificación descrito
por Vincent Driessen. Cada repositorio mantiene las siguientes ramas:

**Tabla 27**

*Ramas de GitFlow y convención de nombres*

<table>
<tbody>
<tr>
<th>Rama</th>
<th>Propósito</th>
<th>Convención de nombre</th>
</tr>
<tr>
<td>main</td>
<td>Rama principal. Contiene únicamente las versiones entregadas y estables del producto. Cada integración a esta rama corresponde a un release etiquetado.</td>
<td>main</td>
</tr>
<tr>
<td>develop</td>
<td>Rama de integración. Concentra el avance acumulado de las features completadas que aún no forman parte de un release.</td>
<td>develop</td>
</tr>
<tr>
<td>Feature branches</td>
<td>Una rama por cada feature o sección en desarrollo. Nace de develop y se integra a develop mediante Pull Request.</td>
<td>feature/\<nombre-en-kebab-case\>, por ejemplo feature/user-stories o feature/sensor-linking</td>
</tr>
<tr>
<td>Release branches</td>
<td>Rama de preparación de una versión a entregar. Nace de develop y se integra tanto a main como a develop.</td>
<td>release/\<major\>.\<minor\>.\<patch\>, por ejemplo release/1.0.0</td>
</tr>
<tr>
<td>Hotfix branches</td>
<td>Rama de corrección urgente sobre una versión ya publicada. Nace de main y se integra tanto a main como a develop.</td>
<td>hotfix/\<nombre-en-kebab-case\>, por ejemplo hotfix/broken-toc-links</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Semantic Versioning**

Los releases se nombran aplicando Semantic Versioning 2.0.0, bajo el
formato MAJOR.MINOR.PATCH. Se incrementa la versión MAJOR ante cambios
incompatibles con versiones previas, la versión MINOR ante la
incorporación de funcionalidad compatible con versiones previas, y la
versión PATCH ante correcciones compatibles con versiones previas. Cada
release se registra como un tag de Git sobre main, bajo el formato
vMAJOR.MINOR.PATCH.

**Conventional Commits**

Los mensajes de commit siguen la especificación de Conventional Commits,
bajo la estructura \<type\>(\<scope\>): \<description\>. Los tipos
utilizados por el equipo son los siguientes:

**Tabla 28**

*Tipos de commit según Conventional Commits*

<table>
<tbody>
<tr>
<th>Tipo</th>
<th>Uso</th>
</tr>
<tr>
<td>feat</td>
<td>Incorporación de una nueva funcionalidad al producto o de una nueva sección al informe.</td>
</tr>
<tr>
<td>fix</td>
<td>Corrección de un defecto en el producto o de un error en el informe.</td>
</tr>
<tr>
<td>docs</td>
<td>Cambios que afectan únicamente a la documentación.</td>
</tr>
<tr>
<td>style</td>
<td>Cambios que no alteran el significado del código, como formato o espaciado.</td>
</tr>
<tr>
<td>refactor</td>
<td>Cambios en el código que no corrigen defectos ni agregan funcionalidad.</td>
</tr>
<tr>
<td>test</td>
<td>Incorporación o corrección de pruebas.</td>
</tr>
<tr>
<td>chore</td>
<td>Cambios en la configuración del proyecto o en las herramientas de soporte.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

La descripción se redacta en inglés, en modo imperativo y en minúsculas,
sin punto final. El scope identifica la sección del informe o el módulo
del producto afectado.

### 5.1.3. Source Code Style Guide & Conventions 

El equipo adopta la nomenclatura en inglés para todos los lenguajes
utilizados en la solución, así como las siguientes convenciones estándar
de codificación:

**Tabla 29**

*Convenciones de codificación por lenguaje*

<table>
<tbody>
<tr>
<th>Lenguaje</th>
<th>Convención adoptada</th>
</tr>
<tr>
<td>HTML</td>
<td>HTML Style Guide and Coding Conventions (W3Schools) / Google HTML/CSS Style Guide</td>
</tr>
<tr>
<td>CSS</td>
<td>Google HTML/CSS Style Guide</td>
</tr>
<tr>
<td>JavaScript</td>
<td>Google JavaScript Style Guide / MDN JavaScript Guidelines / Vue Style Guide</td>
</tr>
<tr>
<td>C#</td>
<td>C# Coding Conventions (Microsoft) / Microsoft <a href="http://asp.net" style="color:#2563eb">http://asp.net</a> Core Coding Guidelines</td>
</tr>
<tr>
<td>Gherkin (criterios de aceptación)</td>
<td>Gherkin Conventions for Readable Specifications</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

### 5.1.4. Software Deployment Configuration 

**Landing Page**

El Landing Page se publica como sitio web estático en GitHub Pages, a
partir del repositorio correspondiente de la organización InventiaStock.
Los pasos de configuración fueron los siguientes:

1.  Se integró a la rama main del repositorio del Landing Page la versión a publicar, mediante el flujo GitFlow (ramas feature/, fix/ y chore/ integradas a develop, y develop integrada a main).

2.  En la configuración del repositorio, se accedió a la sección **Settings → Pages** y se seleccionó como fuente la rama main y el directorio raíz (/root).

3.  Se confirmó la publicación y se verificó el sitio en la URL asignada por GitHub Pages: <a href="https://inventiastock.github.io/smartstock-landing-page/" style="color:#2563eb">https://inventiastock.github.io/smartstock-landing-page/</a>

4.  Se verificó el correcto funcionamiento del selector de idioma, la navegación por anclas y el enlace a los términos y condiciones del footer.

**Figura 200**

*Configuración de GitHub Pages del repositorio smartstock-landing-page*

<img src="../assets/chapter-5/figura_200.png" style="max-height:6.6cm">

Nota. Configuración de GitHub Pages para el repositorio smartstock-landing-page, publicando desde la rama main.

**Figura 201**

*Landing Page de SmartStock desplegado en GitHub Pages*

<img src="../assets/chapter-5/figura_201.png" style="max-height:6.6cm">

Nota. Landing page de SmartStock desplegada y accesible públicamente

en GitHub Pages.

## 5.2. Landing Page, Services & Applications Implementation

En esta sección se explica y evidencia el proceso de implementación,
pruebas, documentación y despliegue del Landing Page, los Web Services y
la Frontend Web Application, organizado por sprints.

### 5.2.1. Sprint 1 

#### 5.2.1.1. Sprint Planning 1

**Tabla 30**

*Sprint Planning 1*

<table>
<tbody>
<tr>
<th>Campo</th>
<th>Detalle</th>
</tr>
<tr>
<td><b>Sprint #</b></td>
<td>1</td>
</tr>
<tr>
<td><b>Date</b></td>
<td>2026-09-12</td>
</tr>
<tr>
<td><b>Time</b></td>
<td>4:00 PM</td>
</tr>
<tr>
<td><b>Location</b></td>
<td>Reunión virtual</td>
</tr>
<tr>
<td><b>Prepared By</b></td>
<td>Montañez Salinas, Lorena Ariana</td>
</tr>
<tr>
<td><b>Attendees</b></td>
<td>Lopez Rimachi, Sebastian Leonardo; Montañez Salinas, Lorena Ariana; Sanchez Osorio, Ruth Yanira; Suarez Chinga, Geraldine; Vizcarra Mamani, Candy Milagros</td>
</tr>
<tr>
<td><b>Sprint 0 – Review Summary</b></td>
<td>N/A (Primer Sprint del proyecto. Se establecieron las bases de la arquitectura, infraestructura en la nube y repositorios).</td>
</tr>
<tr>
<td><b>Sprint 0 – Retrospective Summary</b></td>
<td>N/A (Primer Sprint. El equipo acordó usar GitFlow y Conventional Commits rigurosamente desde el primer día).</td>
</tr>
<tr>
<td><b>Sprint 1 Goal</b></td>
<td>Our focus is on delivering a fast, static Landing Page (HTML/CSS/JS) with language support to attract clients and validate our value proposition. We believe it delivers a clear, accessible introduction to our product's value proposition to minimarket and bodega owners exploring inventory solutions. This will be confirmed when the Landing Page is deployed and fully navigable by users, in both supported languages.</td>
</tr>
<tr>
<td><b>Sprint 1 Velocity</b></td>
<td>10 Story Points (Velocidad estimada para el primer ciclo del equipo).</td>
</tr>
<tr>
<td><b>Sum of Story Points</b></td>
<td>10</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.1.2. Aspect Leaders and Collaborators

A continuación, se presenta la matriz de liderazgo y colaboración
(LACX), cuyo objetivo es facilitar una comunicación clara y organizada
entre los integrantes del equipo durante el desarrollo de las tareas
correspondientes a este Sprint.

**Tabla 31**

*Matriz de liderazgo y colaboración (LACX) del Sprint 1*

<table>

<tbody>
<tr>
<th>Team Member</th>
<th><p>GitHub</p>
<p>Username</p></th>
<th><p>Landing Page</p>
<p>Structure</p></th>
<th><p>Landing</p>
<p>Page UI/UX</p></th>
</tr>
<tr>
<td>Lopez Rimachi, Sebastian Leonardo</td>
<td>@leonardoXd1323</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Montañez Salinas, Lorena Ariana</td>
<td>@Lore-MS</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Sanchez Osorio, Ruth Yanira</td>
<td>@Yiya-ciber</td>
<td>L</td>
<td>C</td>
</tr>
<tr>
<td>Suarez Chinga, Geraldine</td>
<td>@geral07-UNIV</td>
<td>C</td>
<td>L</td>
</tr>
<tr>
<td>Vizcarra Mamani, Candy Milagros</td>
<td>@candyvizz</td>
<td>C</td>
<td>C</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.1.3. Sprint Backlog 1

El Sprint Backlog 1 se estructuró en torno a la construcción del sitio
web estático (Landing Page) de SmartStock, encargado de comunicar la
propuesta de valor del producto, los casos de uso diferenciados para
bodegas de barrio y minimarkets, los planes y precios, la comparación
frente a otras soluciones del mercado, y el flujo de contacto y registro
de nuevos usuarios. Cada User Story del Epic EP08 se descompuso en
tareas técnicas concretas, asignadas a los integrantes del subequipo de
Landing Page (Ruth Sánchez y Geraldine Suárez) según su rol de diseño y
desarrollo dentro del proyecto."

Trello link:
<a href="https://trello.com/invite/b/6aa988a0941a5fb8c814af43/ATTI5eecabb28fdc9c85d7ba8336b688a97353B8B08C/trello-web" style="color:#2563eb">https://trello.com/invite/b/6aa988a0941a5fb8c814af43/ATTI5eecabb28fdc9c85d7ba8336b688a97353B8B08C/trello-web</a>

**Figura 202**

*Tablero de Trello del Sprint Backlog 1*

<img src="../assets/chapter-5/figura_202.png" style="max-height:6.6cm">

Nota. Elaboración propia


**Tabla 32**

*Sprint Backlog 1*

<table style="font-size:10pt;">
<tbody>
<tr>
<th>Story Id</th>
<th>Story Title</th>
<th>Task Id</th>
<th>Task Title</th>
<th>Task Description</th>
<th>Estimation (Hours)</th>
<th>Assigned To</th>
<th>Status</th>
</tr>
<tr>
<td>US16</td>
<td>Información general de SmartStock</td>
<td>T01</td>
<td>Construir sección Hero con información general</td>
<td>Maquetar la propuesta de valor y el problema que resuelve SmartStock en la página de inicio, incluyendo los estilos base del sitio (colores y tipografía).</td>
<td>5</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US16</td>
<td>Información general de SmartStock</td>
<td>T02</td>
<td>Rediseñar la sección Hero</td>
<td>Reestructurar el Hero en dos columnas (copy + imagen), agregar el kicker y la imagen del dueño de tienda, junto con los CTA "Start free trial" y "Request a demo".</td>
<td>4</td>
<td>Lorena Montañez Salinas</td>
<td>Done</td>
</tr>
<tr>
<td>US17</td>
<td>Casos de uso para bodegas de barrio</td>
<td>T03</td>
<td>Construir sección de casos de uso — bodegas</td>
<td>Maquetar el contenido dirigido al segmento bodegas de barrio.</td>
<td>3</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US17</td>
<td>Casos de uso para bodegas de barrio</td>
<td>T04</td>
<td>Refinar el copy de casos de uso — bodegas</td>
<td>Ajustar la redacción del contenido de bodegas para mayor claridad.</td>
<td>1</td>
<td>Lorena Montañez Salinas</td>
<td>Done</td>
</tr>
<tr>
<td>US18</td>
<td>Casos de uso para minimarkets</td>
<td>T05</td>
<td>Construir sección de casos de uso — minimarkets</td>
<td>Maquetar el contenido dirigido al segmento minimarkets.</td>
<td>3</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US18</td>
<td>Casos de uso para minimarkets</td>
<td>T06</td>
<td>Refinar el copy de casos de uso — minimarkets</td>
<td>Ajustar la redacción del contenido de minimarkets para mayor claridad.</td>
<td>1</td>
<td>Lorena Montañez Salinas</td>
<td>Done</td>
</tr>
<tr>
<td>US19</td>
<td>Planes y precios</td>
<td>T07</td>
<td>Construir sección de planes y precios</td>
<td>Maquetar los planes disponibles con sus características y costos.</td>
<td>3</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US19</td>
<td>Planes y precios</td>
<td>T08</td>
<td>Agregar botones de selección de plan</td>
<td>Implementar los CTA "Choose Starter" y "Choose Growth" en la sección de planes.</td>
<td>2</td>
<td>Candy Vizcarra Mamani</td>
<td>Done</td>
</tr>
<tr>
<td>US20</td>
<td>Formulario de contacto para solicitar demostración</td>
<td>T09</td>
<td>Construir formulario de contacto y validación</td>
<td>Maquetar el formulario (nombre, negocio, correo) e implementar la validación de campos obligatorios.</td>
<td>4</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US21</td>
<td>Preguntas frecuentes sobre instalación de sensores</td>
<td>T10</td>
<td>Construir sección de preguntas frecuentes</td>
<td>Maquetar el listado de preguntas y respuestas sobre instalación de sensores IoT.</td>
<td>2</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US22</td>
<td>Testimonios de dueños de bodega</td>
<td>T11</td>
<td>Construir sección de testimonios (base)</td>
<td>Maquetar la sección inicial de testimonios de clientes.</td>
<td>2</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US22</td>
<td>Testimonios de dueños de bodega</td>
<td>T12</td>
<td>Rediseñar testimonios como grid de tarjetas</td>
<td>Reestructurar la sección en un grid de tarjetas, con avatares, calificación de 5 estrellas y el rol de cada persona.</td>
<td>4</td>
<td>Geraldine Suarez Chinga</td>
<td>Done</td>
</tr>
<tr>
<td>US22</td>
<td>Testimonios de dueños de bodega</td>
<td>T13</td>
<td>Estilizar el nuevo grid de testimonios</td>
<td>Agregar los estilos CSS del nuevo diseño de testimonios.</td>
<td>2</td>
<td>Geraldine Suarez Chinga</td>
<td>Done</td>
</tr>
<tr>
<td>US23</td>
<td>Comparación frente a otras soluciones</td>
<td>T14</td>
<td>Construir tabla comparativa</td>
<td>Maquetar la tabla comparativa entre SmartStock y otras soluciones del mercado.</td>
<td>3</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US24</td>
<td>Acceso a registro desde el sitio web</td>
<td>T15</td>
<td>Agregar acceso a registro permanente en el header</td>
<td>Incorporar el enlace de registro visible desde cualquier sección del sitio.</td>
<td>2</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>US24</td>
<td>Acceso a registro desde el sitio web</td>
<td>T16</td>
<td>Ajustar logo y etiquetas aria del navbar</td>
<td>Redimensionar el logo (28px→42px) y añadir etiquetas aria descriptivas en la navegación.</td>
<td>2</td>
<td>Candy Vizcarra Mamani</td>
<td>Done</td>
</tr>
<tr>
<td>US24</td>
<td>Acceso a registro desde el sitio web</td>
<td>T17</td>
<td>Dar visibilidad persistente al enlace de registro</td>
<td>Incorporar el enlace "Sign up" visible de forma persistente en el header.</td>
<td>2</td>
<td>Candy Vizcarra Mamani</td>
<td>Done</td>
</tr>
<tr>
<td>US24</td>
<td>Acceso a registro desde el sitio web</td>
<td>T18</td>
<td>Reparar navegación en pantallas angostas</td>
<td>Corregir el comportamiento del menú y el acceso al registro en viewports menores a 720px.</td>
<td>3</td>
<td>Sebastian Lopez Rimachi</td>
<td>Done</td>
</tr>
<tr>
<td>—</td>
<td>Tarea adicional (no ligada a un User Story en particular)</td>
<td>T19</td>
<td>Implementar selector de idioma (inglés/español)</td>
<td>Añadir el switch de idioma con inglés por defecto y diccionario para español (es_419), aplicado a todas las secciones.</td>
<td>4</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>—</td>
<td>Tarea adicional (no ligada a un User Story en particular)</td>
<td>T20</td>
<td>Redactar términos y condiciones</td>
<td>Elaborar la página de términos y condiciones enlazada desde el footer, siguiendo el código de ética ACM/IEEE y del Colegio de Ingenieros del Perú.</td>
<td>3</td>
<td>Ruth Sanchez Osorio</td>
<td>Done</td>
</tr>
<tr>
<td>—</td>
<td>Tarea adicional (no ligada a un User Story en particular)</td>
<td>T21</td>
<td>Eliminar rutas hardcodeadas del script</td>
<td>Quitar la URL y las rutas de la app hardcodeadas en script.js.</td>
<td>2</td>
<td>Sebastian Lopez Rimachi</td>
<td>Done</td>
</tr>
<tr>
<td>—</td>
<td>Tarea adicional (no ligada a un User Story en particular)</td>
<td>T22</td>
<td>Forzar idioma por defecto (inglés)</td>
<td>Configurar inglés como locale por defecto según requisito del curso.</td>
<td>1</td>
<td>Sebastian Lopez Rimachi</td>
<td>Done</td>
</tr>
<tr>
<td>—</td>
<td>Tarea adicional (no ligada a un User Story en particular)</td>
<td>T23</td>
<td>Documentar el proyecto (README)</td>
<td>Redactar el README con el propósito del proyecto, el stack utilizado y la estructura de archivos.</td>
<td>2</td>
<td>Lorena Montañez Salinas</td>
<td>Done</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Resumen de carga por integrante:** Ruth Sanchez Osorio (11 tasks, 34h)
· Lorena Montañez Salinas (4 tasks, 8h) · Candy Vizcarra Mamani (3
tasks, 6h) · Geraldine Suarez Chinga (2 tasks, 6h) · Sebastian Lopez
Rimachi (3 tasks, 6h).

#### 5.2.1.4. Development Evidence for Sprint Review

Durante el Sprint 1 se implementó la primera versión del sitio web
estático (Landing Page) de SmartStock, cubriendo las secciones de
propuesta de valor, problemática, casos de uso por segmento, comparación
frente a otras soluciones, planes y precios, testimonios, preguntas
frecuentes y formulario de contacto. A continuación se presenta la tabla
de commits relacionados con la implementación, organizados por rama
según GitFlow y redactados bajo la convención de Conventional Commits.

**Tabla 33**

*Commits relacionados con la implementación del Sprint 1*

<table style="font-size:10pt;">
<tbody>
<tr>
<th>Repository</th>
<th>Branch</th>
<th>Commit Id</th>
<th>Commit Message</th>
<th>Commit Message Body</th>
<th>Commited on (Date)</th>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-page</td>
<td>8f8baff</td>
<td>feat(landing): add base styles</td>
<td>White as the dominant background, navy for headings and actions. Only the tokens the page actually uses are declared.</td>
<td>10/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-page</td>
<td>083b61e</td>
<td>feat(landing): add the home page sections</td>
<td>Cover the user stories of the static web site: general information and the problem it solves (US16), use cases for corner stores (US17) and minimarkets (US18), comparison against other solutions (US23), plans and pricing (US19), testimonials (US22), sensor installation FAQ (US21), demonstration request form (US20) and permanent access to sign-up from the header (US24).</td>
<td>10/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-page</td>
<td>a3d57f5</td>
<td>feat(landing): add language switch, menu, faq and form validation</td>
<td>English is the default language and its copy lives in the markup, so the page still reads complete if this script fails to load. Spanish (es_419) comes from a flat dictionary. The call-to-action links to the web application are built from a single URL constant.</td>
<td>11/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-page</td>
<td>f1fd4da</td>
<td>feat(landing): add terms and conditions linked from the footer</td>
<td>Written following the ACM/IEEE Software Engineering Code of Ethics and the code of ethics of the Colegio de Ingenieros del Perú.</td>
<td>11/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>fix/mobile-navbar</td>
<td>519a06f</td>
<td>fix(landing): repair the navigation bar on narrow screens</td>
<td>Below 720px the sign-up button moves into the collapsible menu so the bar keeps only the brand, language switch and menu button. Sign-up stays reachable from every section (US24) and the language switch stays visible.</td>
<td>12/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/header-navbar</td>
<td>5dcbdb0</td>
<td>feat(landing): resize brand logo and improve navbar aria labels</td>
<td>Se ajustó el tamaño del logo (28px→42px) y se añadieron etiquetas aria descriptivas en el selector de idioma y la navegación. Aplica en index.html y terms-of-service.html.</td>
<td>12/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/header-navbar</td>
<td>e08146f</td>
<td>feat(landing): add persistent sign up link in header</td>
<td>Se agregó el enlace "Sign up" visible en el header.</td>
<td>13/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/pricing-cta</td>
<td>4496ea1</td>
<td>feat(landing): add plan selection CTA buttons</td>
<td>Se agregaron los botones "Choose Starter" y "Choose Growth" en la sección de planes.</td>
<td>13/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/usecase-content</td>
<td>bc2072c</td>
<td>content: refine corner store and minimarket copy</td>
<td>Se ajustó la redacción de los casos de uso de bodega y minimarket.</td>
<td>14/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/hero-redesign</td>
<td>9a8b222</td>
<td>feat(landing): redesign hero section with visual and kicker</td>
<td>Se reestructuró el hero en dos columnas (copy + imagen), añadiendo el kicker y la imagen del dueño de tienda.</td>
<td>14/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/hero-redesign</td>
<td>ec752f4</td>
<td>feat(landing): add hero CTAs and supporting copy</td>
<td>Se agregaron los botones "Start free trial" y "Request a demo" junto con el texto de nota.</td>
<td>15/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/testimonials-redesign</td>
<td>3ceb77f</td>
<td>feat(landing): rebuild testimonials as card grid</td>
<td>Se reestructuró la sección de testimonios en un grid de tarjetas.</td>
<td>15/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/testimonials-redesign</td>
<td>21f1118</td>
<td>feat(landing): add avatars, ratings and roles to testimonials</td>
<td>Se añadieron avatares, calificación de 5 estrellas y el rol de cada persona.</td>
<td>16/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/testimonials-redesign</td>
<td>aed1e38</td>
<td>style(landing): add testimonials grid and card styles</td>
<td>Se agregaron los estilos CSS del nuevo diseño de testimonios.</td>
<td>16/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>chore/script-cleanup</td>
<td>871c162</td>
<td>chore(landing): remove hardcoded app routes from script</td>
<td>Se eliminaron la URL y las rutas de la app hardcodeadas en script.js.</td>
<td>16/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>chore/script-cleanup</td>
<td>eb3dc3c</td>
<td>fix(landing): set English as default locale</td>
<td>Se forzó inglés como idioma por defecto según requisito del curso.</td>
<td>16/09/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>develop</td>
<td>bb44d80</td>
<td>docs: add project README</td>
<td>Se documenta el propósito del proyecto, el stack utilizado y la estructura de archivos del landing page.</td>
<td>16/09/2026</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.1.5. Execution Evidence for Sprint Review

Durante el Sprint 1 se implementó y desplegó la primera versión del
Landing Page, que cubre las User Stories del sitio web estático
especificadas en la sección 3.1. El sitio se encuentra accesible en
<a href="https://inventiastock.github.io/smartstock-landing-page/" style="color:#2563eb">https://inventiastock.github.io/smartstock-landing-page/</a>
.

Landing Page Demonstration Video:
<a href="https://upcedupe-my.sharepoint.com/%3Av%3A/g/personal/u20241f205_upc_edu_pe/IQA-Q3weXz9fQKE42Q-KkgoIAadgYrZxWARopglSvgvHunk?e=hNwpTf&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" style="color:#2563eb">https://upcedupe-my.sharepoint.com/&#58;v&#58;/g/personal/u20241f205_upc_edu_pe/IQA-Q3weXz9fQKE42Q-KkgoIAadgYrZxWARopglSvgvHunk?e=hNwpTf&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D</a>

A continuación se presentan las principales vistas implementadas.

**Encabezado principal y propuesta de valor (US16, US24)**

El encabezado principal se organiza en dos columnas: a la izquierda la
propuesta de valor, que presenta qué es SmartStock y qué problema
resuelve, y a la derecha una fotografía de un propietario de tienda
utilizando la plataforma junto a sus estantes abastecidos. La imagen
permite que el visitante reconozca el segmento al que se dirige el
producto antes de leer una sola línea, y cuenta con un texto alternativo
descriptivo que se traduce junto con el resto de la página.

La barra superior mantiene visibles de forma permanente el selector de
idioma y la acción de crear cuenta, en cumplimiento de la regla de
negocio de la US24.

**Figura 203**

*Encabezado principal y propuesta de valor del Landing Page (US16,*

US24)
<img src="../assets/chapter-5/figura_203.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 204**

*Sección de problemática del Landing Page (US16)*

<img src="../assets/chapter-5/figura_204.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Casos de uso por segmento objetivo (US17, US18)**

La sección de casos de uso separa el contenido dirigido a bodegas de
barrio del dirigido a minimarkets. Cada bloque enumera los beneficios
propios del segmento y cierra con un call-to-action que redirige a la
vista de registro de la Web Application transportando el segmento
correspondiente. La captura se presenta con la experiencia conmutada a
español latinoamericano, de modo que evidencie además el alcance de la
traducción sobre el contenido de esta sección.

**Figura 205**

*Sección de casos de uso por segmento objetivo del Landing Page (US17,*

US18)
<img src="../assets/chapter-5/figura_205.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 206**

*Sección comparativa frente a otras soluciones del Landing Page (US23)*

<img src="../assets/chapter-5/figura_206.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Planes y precios (US19)**

Los tres planes se presentan sobre el mismo conjunto de características,
ordenados de menor a mayor capacidad, y el plan intermedio se destaca
mediante un borde de mayor peso. Cada plan conduce al registro con el
plan preseleccionado. Las tarjetas aplican el refresco visual del design
system: radio de esquina de 14 píxeles, elevación tenue en reposo y un
filete de acento que se revela al pasar el cursor.

**Figura 207**

*Sección de planes y precios del Landing Page (US19)*

<img src="../assets/chapter-5/figura_207.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Testimonios de clientes (US22)**

La sección de testimonios presenta las opiniones recogidas durante las
entrevistas, cada una acompañada de una valoración y de un avatar con
las iniciales del entrevistado. La valoración se expone además mediante
aria-label, de modo que un lector de pantalla anuncie la calificación en
lugar de leer una sucesión de símbolos.

**Figura 208**

*Sección de testimonios y preguntas frecuentes del Landing Page (US22)*

<img src="../assets/chapter-5/figura_208.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Formulario de solicitud de demostración (US20)**

El formulario valida los campos obligatorios al abandonar cada campo y
expone los mensajes de error mediante role="alert", de modo que un
lector de pantalla los anuncie. Los campos adoptan el radio de esquina y
el color de borde definidos en la sección 4.1, y el botón de envío
emplea el degradado de marca.

**Figura 209**

*Formulario de solicitud de demostración del Landing Page (US20)*

<img src="../assets/chapter-5/figura_209.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Internacionalización de la experiencia (en_US / es_419)**

El idioma por defecto del sitio es el inglés, conforme a lo establecido
en el enunciado. El sitio no adopta el idioma del navegador en la
primera visita, precisamente para que el idioma por defecto del producto
sea siempre el inglés; a partir de ahí, la preferencia elegida por el
visitante queda registrada en el navegador.

El selector de idioma de la barra superior conmuta toda la experiencia
al español latinoamericano, incluyendo el título del documento, los
textos de la interfaz, los mensajes de validación del formulario y los
atributos aria-label de la navegación, del selector de idioma y de la
imagen del encabezado principal. El atributo lang del documento se
actualiza en cada conmutación, de modo que un lector de pantalla emplee
la pronunciación correcta.

**Figura 210**

*Formulario de demostración y pie de página del Landing Page*

<img src="../assets/chapter-5/figura_210.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Diseño web adaptable (responsive web design)**

La experiencia se adapta a las dimensiones del dispositivo cliente. En
navegador móvil, las rejillas de tarjetas colapsan a una sola columna,
la escala tipográfica de los titulares se reduce y la navegación se
repliega tras un botón de menú.

La barra superior conserva en pantallas estrechas únicamente la marca,
el selector de idioma y el botón de menú. La acción de crear cuenta se
traslada al interior del menú desplegable, de modo que la barra no
compita por el ancho disponible y se mantenga el cumplimiento de la
regla de negocio de la US24, que establece que la opción de registro
está disponible de forma permanente en todas las secciones del sitio web
estático.

**Figura 211**

*Mockup de la pantalla principal del Landing Page en versión móvil*

![Figura 211](../assets/chapter-5/figura_211.png)

Nota. Mockup de la interfaz principal de inicio del landing page de SmartStock adaptada para dispositivos móviles.

#### 5.2.1.6. Services Documentation Evidence for Sprint Review

N/A. Durante el Sprint 1 el esfuerzo de desarrollo se enfocó
exclusivamente en la creación del sitio web estático promocional
(Landing Page), por lo que aún no se han implementado APIs RESTful ni
Endpoints backend que requieran ser documentados a través de
Swagger/OpenAPI. Esta documentación se estructurará a partir del Sprint
2.

#### 5.2.1.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 1, el alcance de despliegue correspondió al Landing
Page. El equipo creó el repositorio smartstock-landing-page dentro de la
organización InventiaStock, aplicó sobre él el flujo de trabajo GitFlow
e integró la versión 1.0.0 a la rama main mediante una release branch. A
continuación, habilitó GitHub Pages tomando como fuente dicha rama y el
directorio raíz del repositorio.

**Tabla 34**

*Evidencia de despliegue del Sprint 1*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Repositorio</th>
<th>URL desplegado</th>
<th>Estado</th>
</tr>
<tr>
<td>Landing Page</td>
<td><a href="https://github.com/InventiaStock/smartstock-landing-page" style="color:#2563eb">https://github.com/InventiaStock/smartstock-landing-page</a></td>
<td><a href="https://inventiastock.github.io/smartstock-landing-page/" style="color:#2563eb">https://inventiastock.github.io/smartstock-landing-page/</a></td>
<td>Desplegado</td>
</tr>
<tr>
<td>Frontend Web Application</td>
<td><a href="https://github.com/InventiaStock/smartstock-frontend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-frontend</a></td>
<td>—</td>
<td>Desplegado</td>
</tr>
<tr>
<td>Web Services</td>
<td>Pendiente de despliegue.</td>
<td>—</td>
<td>Fuera del alcance del Sprint 2</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

La configuración aplicada en el repositorio se muestra a continuación.
La fuente de publicación es la rama main y el directorio raíz, y GitHub
confirma la publicación del sitio. En el selector de ramas se aprecian
además las ramas main y develop, que evidencian la aplicación de GitFlow
sobre el repositorio.

**Figura 212**

*Configuración de GitHub Pages del repositorio smartstock-landing-page*

<img src="../assets/chapter-5/figura_212.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 213**

*Publicación del sitio confirmada en GitHub Pages*

<img src="../assets/chapter-5/figura_213.png" style="max-height:6.6cm">

Nota. Elaboración propia

Se verificó que el sitio publicado responde correctamente tanto en la
página de inicio como en la página de términos y condiciones, y que la
hoja de estilos y el archivo de comportamiento se sirven sin errores.

**Figura 214**

*Landing Page de SmartStock publicado en GitHub Pages*

<img src="../assets/chapter-5/figura_214.png" style="max-height:6.6cm">

Nota. Elaboración propia

#### 5.2.1.8. Team Collaboration Insights during Sprint

Durante el Sprint 1, el equipo organizó la implementación del Landing
Page según los aspectos definidos en la sección 5.2.1.2. Cada integrante
trabajó sobre el aspecto que lideraba y registró su aporte mediante
commits propios en el repositorio smartstock-landing-page, aplicando
GitFlow y Conventional Commits.

El flujo de trabajo seguido fue el siguiente: la rama develop concentró
el avance acumulado, cada conjunto de cambios se desarrolló en una rama
feature/ que se integró a develop sin avance rápido (--no-ff), de modo
que el historial conserve visible el punto de integración de cada
aporte, y la versión entregada se publicó desde main mediante una
release branch.

**Analíticos de colaboración del repositorio del Landing Page**

La vista de contribuyentes evidencia la participación de los cinco
integrantes del equipo, con el detalle de commits y de líneas agregadas
y eliminadas por cada uno.

**Figura 215**

*Contribuyentes del repositorio smartstock-landing-page*

<img src="../assets/chapter-5/figura_215.png" style="max-height:6.6cm">

Nota. Contribuyentes del repositorio smartstock-landing-page, los cinco integrantes del equipo registran commits propios.

**Historial de ramas del repositorio**

El grafo de red muestra la aplicación efectiva de GitFlow: las ramas de
feature nacen de develop, se integran nuevamente a ella y la rama main
recibe únicamente las versiones publicadas.

**Figura 216**

*Historial de commits del repositorio smartstock-landing-page*

<img src="../assets/chapter-5/figura_216.png" style="max-height:6.6cm">

Nota. Comparación de commits entre la primera rama de trabajo y main, mostrando la autoría real de cada commit (autor original y quien lo integró).

### 5.2.2. Sprint 2 

#### 5.2.2.1. Sprint Planning 2

En el Sprint Planning 2 el equipo definió como meta entregar la primera
versión desplegada de la Frontend Web Application de SmartStock, con las
historias de Compras y Ventas como núcleo del producto y el IoT como
verificación del stock físico. El sprint incluye las 23 User Stories del
Product Backlog que no son del Landing Page; las 15 Technical Stories
(endpoints y modelo de datos) pasan al Sprint 3, junto con los Web
Services reales.

**Tabla 35**

*Sprint Planning 2*

<table>
<tbody>
<tr>
<th>Campo</th>
<th>Detalle</th>
</tr>
<tr>
<td><b>Sprint #</b></td>
<td>Sprint 2</td>
</tr>
<tr>
<td><b>Date</b></td>
<td>2026-10-01</td>
</tr>
<tr>
<td><b>Time</b></td>
<td>02:00 PM</td>
</tr>
<tr>
<td><b>Location</b></td>
<td>Reunión virtual</td>
</tr>
<tr>
<td><b>Prepared By</b></td>
<td>Montañez Salinas, Lorena Ariana</td>
</tr>
<tr>
<td><b>Attendees</b></td>
<td>Lopez Rimachi, Sebastian Leonardo / Montañez Salinas, Lorena Ariana / Sanchez Osorio, Ruth Yanira / Suarez Chinga, Geraldine / Vizcarra Mamani, Candy Milagros</td>
</tr>
<tr>
<td><b>Sprint 1 – Review Summary</b></td>
<td>Durante el Sprint 1 se implementó y desplegó la primera versión del Landing Page (versión 1.0.0) en GitHub Pages, cubriendo las User Stories US16 a US24 (20 Story Points). En la revisión del Sprint 1, el docente no indicó correcciones pendientes sobre el Landing Page. Para el Sprint 2 se incorpora una actualización del Landing Page, cuyo botón de registro pasa a redirigir a la aplicación web desplegada.</td>
</tr>
<tr>
<td><b>Sprint 1 – Retrospective Summary</b></td>
<td>Durante el Sprint 1 funcionó bien la aplicación de GitFlow, con ramas de feature integradas a develop y la versión 1.0.0 publicada desde main mediante una release branch, así como el uso de Conventional Commits y la organización del trabajo en Trello. Como aspecto a mejorar, el equipo identificó la necesidad de verificar las URLs antes de cada entrega. Para el Sprint 2, el equipo acordó: (1) construir las pantallas de Compras y Ventas desde las historias ya definidas (US26 a US32); (2) identificar las historias como US y TS y las tareas como T-US## y T-TS##; (3) trabajar cada tarea en una rama corta feature/\<contexto\>-\<tarea\> creada desde develop e integrada mediante pull request con merge commit (--no-ff), sin commits directos en main ni en develop; (4) no modificar archivos compartidos (rutas, stores, estilos y modelos) sin avisar al equipo; (5) usar datos simulados mientras los Web Services estén en desarrollo; y (6) actualizar el Landing Page para que el registro redirija a la Frontend Web Application desplegada, en lugar de apuntar a una dirección local.</td>
</tr>
<tr>
<td><b>Sprint 2 Goal</b></td>
<td>Our focus is on delivering the first deployed version of the SmartStock web application, where owners of minimarkets and bodegas register their sales and purchases and see their stock. We believe it delivers control over what enters and leaves their inventory, verified by IoT sensors, to minimarket and bodega owners. This will be confirmed when a user can sign up, register a product, a purchase and a sale, and then see the updated stock, the low-stock alert and the dashboard in the deployed frontend, without help from the development team.</td>
</tr>
<tr>
<td><b>Sprint 2 Velocity</b></td>
<td>84 Story Points</td>
</tr>
<tr>
<td><b>Sum of Story Points</b></td>
<td>84 (todas de User Stories)</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

Durante el Sprint 1 funcionó bien la aplicación de GitFlow, con ramas de
feature integradas a develop y la versión 1.0.0 publicada desde main
mediante una release branch, así como el uso de Conventional Commits y
la organización del trabajo en Trello. Como aspecto a mejorar, el equipo
identificó la necesidad de verificar las URLs antes de cada entrega.

Para el Sprint 2, el equipo acordó: (1) construir las pantallas de
Compras y Ventas desde las historias ya definidas (US26 a US32); (2)
identificar las historias como US y TS y las tareas como T-US## y
T-TS##; (3) trabajar cada tarea en una rama corta
feature/\<contexto\>-\<tarea\> creada desde develop e integrada mediante
pull request con merge commit (--no-ff), sin commits directos en main ni
en develop; (4) no modificar archivos compartidos (rutas, stores,
estilos y modelos) sin avisar al equipo; (5) usar datos simulados
mientras los Web Services estén en desarrollo; y (6) actualizar el
Landing Page para que el registro redirija a la Frontend Web Application
desplegada, en lugar de apuntar a una dirección local.

#### 5.2.2.2. Aspect Leaders and Collaborators

Los aspectos de este sprint son los seis bounded contexts del frontend:
IAM (registro, inicio de sesión y recuperación de contraseña); IoT
Device (vinculación de sensores y estado de conexión); Alerts &
Restocking (notificaciones de stock bajo, alertas por discrepancia y
compra desde una alerta); Product Catalog (registro y edición de
productos y umbral mínimo); Inventory Monitoring (peso actual, listado
por nivel de stock, comparación físico vs. registrado, y ventas, compras
y proveedores con sus movimientos de stock); y Analytics & Reporting
(dashboard y reportes). Cada integrante lidera el contexto que eligió y
colabora en los demás (L = líder, C = colaborador); esta distribución se
refleja en la selección de tasks de la sección 5.2.2.3 y en la autoría
de los commits. Dentro de Inventory Monitoring, Lorena construye Ventas,
Candy construye Proveedores y Compras, y Leonardo conecta la alerta de
stock bajo con registrar una compra (US32).

**Tabla 36**

*Matriz de liderazgo y colaboración (LACX) del Sprint 2*

<table style="font-size:10pt;">
<tbody>
<tr>
<th>Team Member</th>
<th>GitHub Username</th>
<th>IAM</th>
<th>IoT Device</th>
<th>Alerts & Restocking</th>
<th>Product Catalog</th>
<th>Inventory Monitoring</th>
<th>Analytics & Reporting</th>
</tr>
<tr>
<td>Montañez Salinas, Lorena Ariana</td>
<td>Lore-MS</td>
<td>L</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Sanchez Osorio, Ruth Yanira</td>
<td>Yiya-ciber</td>
<td>C</td>
<td>L</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Lopez Rimachi, Sebastian Leonardo</td>
<td>leonardoXd1323</td>
<td>C</td>
<td>C</td>
<td>L</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Vizcarra Mamani, Candy Milagros</td>
<td>candyvizz</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>L</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Suarez Chinga, Geraldine</td>
<td>geral07-UNIV</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>L</td>
<td>L</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

Geraldine lidera dos aspectos y el resto uno. Ventas y Compras viven
dentro de Inventory Monitoring, pero sus pantallas se reparten: Lorena
construye Ventas, Candy construye Proveedores y Compras, y Leonardo
conecta la alerta de stock bajo con registrar una compra (US32).

#### 5.2.2.3. Sprint Backlog 2

El objetivo del Sprint 2 es entregar la primera versión navegable y
desplegada del frontend de SmartStock, con Compras y Ventas como núcleo.
El sprint contiene las 23 User Stories del Product Backlog que no son
del Landing Page (84 Story Points); las Technical Stories pasan al
Sprint 3 con los Web Services reales, y en este sprint solo se incluyen
sus tareas de simulación (mock), marcadas como "(mock)" y sin Story
Points propios. El tablero del sprint está en Trello y su URL pública es
<a href="https://trello.com/invite/b/6ac4b28dd414f036520b5f47/ATTI194967e117cc1b0e83906e9d86df8680619E986C/sprint-backlog-2-web" style="color:#2563eb">https://trello.com/invite/b/6ac4b28dd414f036520b5f47/ATTI194967e117cc1b0e83906e9d86df8680619E986C/sprint-backlog-2-web</a>

La tabla resume la carga por integrante. Las tareas se identifican como
T-US##.# (historias de usuario), T-TS##.# (contratos simulados, sin
puntos) y T-SH.# (setup compartido, sin historia). Los 84 Story Points
corresponden solo a User Stories.

**Tabla 37**

*Carga de trabajo por integrante en el Sprint 2*

<table>
<tbody>
<tr>
<th>Integrante</th>
<th>Contexto</th>
<th>User Stories</th>
<th>Story Points</th>
</tr>
<tr>
<td>Lorena</td>
<td>IAM y pantallas de Ventas</td>
<td>US01, US02, US03, US26, US27, US28</td>
<td>21</td>
</tr>
<tr>
<td>Ruth</td>
<td>IoT Device</td>
<td>US04, US06</td>
<td>8</td>
</tr>
<tr>
<td>Leonardo</td>
<td>Alerts & Restocking</td>
<td>US09, US10, US12, US32</td>
<td>16</td>
</tr>
<tr>
<td>Candy</td>
<td>Product Catalog, Proveedores y Compras (+ setup y mock server)</td>
<td>US05, US13, US14, US29, US30, US31</td>
<td>18</td>
</tr>
<tr>
<td>Geraldine</td>
<td>Inventory Monitoring y Analytics & Reporting</td>
<td>US07, US08, US11, US15, US25</td>
<td>21</td>
</tr>
<tr>
<td><b>Total</b></td>
<td></td>
<td></td>
<td><b>84</b></td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 38**

*Sprint Backlog 2*

<table style="font-size:10pt;">
<tbody>
<tr>
<th><b>Sprint #</b></th>
<th>Story Id</th>
<th>Story Title</th>
<th>Task Id</th>
<th>Task Title</th>
<th>Task Description</th>
<th>Estimation (Hours)</th>
<th>Assigned To</th>
<th>Status</th>
</tr>
<tr>
<td>2</td>
<td>Soporte</td>
<td>Setup compartido</td>
<td>T-SH.1</td>
<td>Separar traducciones por contexto y ampliar el entorno</td>
<td>Una carpeta de traducciones por bounded context y endpoints del Sprint 2 en el environment.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>Soporte</td>
<td>Setup compartido</td>
<td>T-SH.2</td>
<td>Helpers y componentes compartidos</td>
<td>Helpers de error y rango de fechas; alert banner, summary card y page header; estilos compartidos.</td>
<td>6</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>Soporte</td>
<td>Setup compartido</td>
<td>T-SH.3</td>
<td>Modelo de movimiento de stock</td>
<td>Entidad StockMovement (R17) usada por ventas, compras y reportes.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS14</td>
<td>Registro automático de movimientos (mock)</td>
<td>T-TS14.1</td>
<td>Motor de movimientos y reglas de alerta del mock</td>
<td>Movimientos de stock, reglas de alerta R19–R21 y proyección de producto con estado del sensor.</td>
<td>6</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS01</td>
<td>Recepción de lecturas (mock)</td>
<td>T-TS01.1</td>
<td>Mock POST /sensores/{id}/lecturas</td>
<td>Servidor json-server con token, rutas automáticas y simulador IoT.</td>
<td>5</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS05</td>
<td>Estado de sensor (mock)</td>
<td>T-TS05.1</td>
<td>Mock GET /sensores/{id}/estado</td>
<td>Estado en línea/desconectado (R11) y endpoints de vinculación.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US04</td>
<td>Vinculación de sensor IoT a un producto</td>
<td>T-US04.1</td>
<td>Diseñar vista de vinculación</td>
<td>Sensores disponibles, flujo de vinculación y caso de sensor ya vinculado.</td>
<td>5</td>
<td>Ruth</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US04</td>
<td>Vinculación de sensor IoT a un producto</td>
<td>T-US04.2</td>
<td>Modelo, API y store de dispositivos</td>
<td>Entidades Sensor y LinkableProduct, DevicesApi y store (R9).</td>
<td>6</td>
<td>Ruth</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US04</td>
<td>Vinculación de sensor IoT a un producto</td>
<td>T-US04.3</td>
<td>Validar sensor ya en uso</td>
<td>Rechazar vinculación e indicar que el sensor ya está en uso.</td>
<td>3</td>
<td>Ruth</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US06</td>
<td>Estado de conexión de sensores</td>
<td>T-US06.1</td>
<td>Vista de listado de estado</td>
<td>Lista de sensores con estado en línea o desconectado.</td>
<td>4</td>
<td>Ruth</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US06</td>
<td>Estado de conexión de sensores</td>
<td>T-US06.2</td>
<td>Regla de 5 minutos</td>
<td>Desconectado si no hay lecturas en 5 minutos (R11).</td>
<td>3</td>
<td>Ruth</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US01</td>
<td>Registro de cuenta</td>
<td>T-US01.1</td>
<td>Formulario de registro</td>
<td>Datos del negocio y selector de tipo de negocio.</td>
<td>5</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US01</td>
<td>Registro de cuenta</td>
<td>T-US01.2</td>
<td>Validaciones y correo repetido</td>
<td>Validar campos y mostrar error de correo ya registrado.</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US01</td>
<td>Registro de cuenta</td>
<td>T-US01.3</td>
<td>Estado de registro exitoso</td>
<td>Mensaje de éxito y redirección.</td>
<td>3</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US02</td>
<td>Inicio de sesión</td>
<td>T-US02.1</td>
<td>Vista de login</td>
<td>Formulario con mensaje de error genérico (R3).</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US02</td>
<td>Inicio de sesión</td>
<td>T-US02.2</td>
<td>Modelo, API y store de IAM</td>
<td>UserSession, IamApi y store con signIn y signUp.</td>
<td>6</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS04</td>
<td>Login (mock)</td>
<td>T-TS04.1</td>
<td>Mock POST /auth/login</td>
<td>Endpoints de login, registro y recuperación en el mock.</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US03</td>
<td>Recuperación de contraseña</td>
<td>T-US03.1</td>
<td>Formulario de recuperación</td>
<td>Solicitud con el mismo mensaje neutro para cualquier correo.</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US03</td>
<td>Recuperación de contraseña</td>
<td>T-US03.2</td>
<td>Nueva contraseña y enlace vencido</td>
<td>Confirmación de envío con el aviso de que el enlace vence en 24 horas (R4).</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US26</td>
<td>Registro de venta</td>
<td>T-US26.1</td>
<td>Formulario de nueva venta</td>
<td>Productos, cantidades y total.</td>
<td>6</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US26</td>
<td>Registro de venta</td>
<td>T-US26.2</td>
<td>Modelo y API de ventas</td>
<td>Sale, SaleItem, SaleProductOption y SalesApi.</td>
<td>5</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US26</td>
<td>Registro de venta</td>
<td>T-US26.3</td>
<td>Store y validaciones de stock</td>
<td>Store de ventas; stock suficiente (R13) y producto sin precio (R14).</td>
<td>5</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US27</td>
<td>Historial de ventas</td>
<td>T-US27.1</td>
<td>Listado de ventas</td>
<td>Lista con total del período.</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US27</td>
<td>Historial de ventas</td>
<td>T-US27.2</td>
<td>Filtro por fechas y período vacío</td>
<td>Filtro por rango y estado vacío.</td>
<td>3</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US28</td>
<td>Detalle de una venta</td>
<td>T-US28.1</td>
<td>Vista de detalle de venta</td>
<td>Detalle con los movimientos de stock generados.</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS07</td>
<td>Registro de ventas (mock)</td>
<td>T-TS07.1</td>
<td>Mock POST /ventas</td>
<td>Cada venta crea movimientos de salida (R17).</td>
<td>4</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS08</td>
<td>Consulta de ventas (mock)</td>
<td>T-TS08.1</td>
<td>Mock GET /ventas y /ventas/{id}</td>
<td>Listado y detalle de ventas.</td>
<td>3</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US09</td>
<td>Notificación por correo de stock bajo</td>
<td>T-US09.1</td>
<td>Vista de configuración de notificaciones</td>
<td>Canal correo electrónico y textos en inglés y español.</td>
<td>5</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US09</td>
<td>Notificación por correo de stock bajo</td>
<td>T-US09.2</td>
<td>Store de alertas</td>
<td>Store con alertas y preferencias.</td>
<td>4</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US09</td>
<td>Notificación por correo de stock bajo</td>
<td>T-US09.3</td>
<td>Modelo y API de alertas</td>
<td>Alert, resource, assembler y AlertsApi.</td>
<td>5</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US10</td>
<td>Notificación por WhatsApp de stock bajo</td>
<td>T-US10.1</td>
<td>Canal WhatsApp en configuración</td>
<td>Preferencia de canal y número de WhatsApp.</td>
<td>4</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS03</td>
<td>Notificación de stock bajo (mock)</td>
<td>T-TS03.1</td>
<td>Mock POST /notificaciones/stock-bajo</td>
<td>Endpoint de notificaciones en alerts.js.</td>
<td>4</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS14</td>
<td>Registro automático de movimientos (mock)</td>
<td>T-TS14.2</td>
<td>Mock de alertas con movimientos</td>
<td>Alertas activas ligadas a los movimientos de stock.</td>
<td>3</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS15</td>
<td>Consulta de movimientos (mock)</td>
<td>T-TS15.1</td>
<td>Mock GET /movimientos-stock</td>
<td>Listado de movimientos.</td>
<td>3</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US12</td>
<td>Alerta por discrepancia de inventario</td>
<td>T-US12.2</td>
<td>Lista de alertas activas</td>
<td>Alertas con discrepancia mayor al 10 %.</td>
<td>5</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US32</td>
<td>Registro de compra desde una alerta de stock bajo</td>
<td>T-US32.1</td>
<td>Botón de compra en la alerta</td>
<td>Acción desde la alerta de stock bajo.</td>
<td>3</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US32</td>
<td>Registro de compra desde una alerta de stock bajo</td>
<td>T-US32.2</td>
<td>Precarga de producto y proveedor</td>
<td>Enviar producto y proveedor al formulario de compra.</td>
<td>4</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US32</td>
<td>Registro de compra desde una alerta de stock bajo</td>
<td>T-US32.3</td>
<td>Marcar necesidad atendida</td>
<td>Actualizar el estado de la alerta tras registrar la compra.</td>
<td>3</td>
<td>Leonardo</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US13</td>
<td>Registro de nuevo producto</td>
<td>T-US13.1</td>
<td>Formulario de producto</td>
<td>Validaciones, precio de venta opcional y banner de error.</td>
<td>5</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US13</td>
<td>Registro de nuevo producto</td>
<td>T-US13.2</td>
<td>Modelo, API y store de catálogo</td>
<td>Product, CatalogApi y store (R5, R7).</td>
<td>6</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS13</td>
<td>Modelo de datos: productos (mock)</td>
<td>T-TS13.2</td>
<td>Mock de productos (GET/POST/PUT /productos)</td>
<td>Validaciones R5 y R7 en el mock.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US14</td>
<td>Edición de producto</td>
<td>T-US14.1</td>
<td>Formulario de edición</td>
<td>Precio de venta, costo de compra y proveedor habitual.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US14</td>
<td>Edición de producto</td>
<td>T-US14.2</td>
<td>Stock de solo lectura</td>
<td>El stock solo cambia por movimientos (R17).</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US05</td>
<td>Configuración de umbral mínimo de stock</td>
<td>T-US05.1</td>
<td>Vista de umbral mínimo</td>
<td>Formulario por producto con sensor.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US05</td>
<td>Configuración de umbral mínimo de stock</td>
<td>T-US05.2</td>
<td>Validar capacidad máxima</td>
<td>Rechazar umbral mayor a la capacidad (R7).</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US29</td>
<td>Registro de proveedor</td>
<td>T-US29.1</td>
<td>Formulario y listado de proveedores</td>
<td>Alta y lista de proveedores.</td>
<td>5</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US29</td>
<td>Registro de proveedor</td>
<td>T-US29.2</td>
<td>Proveedor duplicado</td>
<td>Error por proveedor repetido (R8).</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US30</td>
<td>Registro y recepción de compra</td>
<td>T-US30.1</td>
<td>Formulario de nueva compra</td>
<td>Productos, total y precarga desde reposición.</td>
<td>6</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US30</td>
<td>Registro y recepción de compra</td>
<td>T-US30.2</td>
<td>Modelo y API de compras</td>
<td>Purchase, PurchaseItem, Supplier y PurchasesApi.</td>
<td>5</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US30</td>
<td>Registro y recepción de compra</td>
<td>T-US30.3</td>
<td>Detalle y recepción</td>
<td>Recepción de mercadería que crea movimientos de entrada.</td>
<td>6</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US30</td>
<td>Registro y recepción de compra</td>
<td>T-US30.4</td>
<td>Store de compras</td>
<td>Compras, proveedores y recepción (R15, R16).</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US31</td>
<td>Historial de compras</td>
<td>T-US31.1</td>
<td>Listado de compras</td>
<td>Lista con filtro por fechas.</td>
<td>4</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US31</td>
<td>Historial de compras</td>
<td>T-US31.2</td>
<td>Estado vacío</td>
<td>Mensaje cuando no hay compras en el período.</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS09</td>
<td>Proveedores (mock)</td>
<td>T-TS09.1</td>
<td>Mock POST/GET /proveedores</td>
<td>Alta y consulta de proveedores.</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS10</td>
<td>Registro de compras (mock)</td>
<td>T-TS10.1</td>
<td>Mock POST /compras</td>
<td>Alta de compras.</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS11</td>
<td>Recepción de compras (mock)</td>
<td>T-TS11.1</td>
<td>Mock PATCH /compras/{id}/recepcion</td>
<td>Recepción con movimientos de entrada.</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS12</td>
<td>Consulta de compras (mock)</td>
<td>T-TS12.1</td>
<td>Mock GET /compras y /compras/{id}</td>
<td>Listado y detalle.</td>
<td>3</td>
<td>Candy</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US15</td>
<td>Dashboard de inventario</td>
<td>T-US15.1</td>
<td>Vista de dashboard</td>
<td>Tarjetas de resumen y Home de bodega.</td>
<td>6</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US15</td>
<td>Dashboard de inventario</td>
<td>T-US15.2</td>
<td>Tarjetas de ventas y compras del día</td>
<td>Totales del día en el dashboard.</td>
<td>4</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US15</td>
<td>Dashboard de inventario</td>
<td>T-US15.3</td>
<td>Modelo, API y store de analítica</td>
<td>DashboardSummary, Report y AnalyticsApi.</td>
<td>5</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US15</td>
<td>Dashboard de inventario</td>
<td>T-US15.4</td>
<td>Traducciones y estados vacíos</td>
<td>Textos en inglés y español.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US15</td>
<td>Dashboard de inventario</td>
<td>T-US15.5</td>
<td>Mock GET /dashboard y /reportes</td>
<td>Reportes solo para minimarket.</td>
<td>4</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US25</td>
<td>Reportes de consumo y movimientos</td>
<td>T-US25.1</td>
<td>Selector de período</td>
<td>Rango de fechas del reporte.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US25</td>
<td>Reportes de consumo y movimientos</td>
<td>T-US25.2</td>
<td>Reporte de consumo</td>
<td>Consumo por producto.</td>
<td>5</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US25</td>
<td>Reportes de consumo y movimientos</td>
<td>T-US25.3</td>
<td>Movimientos con ventas y compras</td>
<td>Es una tabla de movimientos con ventas y compras.</td>
<td>5</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US25</td>
<td>Reportes de consumo y movimientos</td>
<td>T-US25.4</td>
<td>Reporte sin datos</td>
<td>Estado vacío del período.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US11</td>
<td>Comparación inventario físico vs. registrado</td>
<td>T-US11.1</td>
<td>Vista de comparación</td>
<td>Peso del sensor frente al stock registrado.</td>
<td>6</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US11</td>
<td>Comparación inventario físico vs. registrado</td>
<td>T-US11.3</td>
<td>Resaltar discrepancia</td>
<td>Diferencia mayor al 10 % resaltada.</td>
<td>4</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US11</td>
<td>Comparación inventario físico vs. registrado</td>
<td>T-US11.4</td>
<td>Modelo, API y store de stock</td>
<td>Comparison, SensorReading y StockApi.</td>
<td>5</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS02</td>
<td>Consulta de stock (mock)</td>
<td>T-TS02.1</td>
<td>Mock GET /productos/{id}/stock</td>
<td>Stock y detalle de producto.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>TS06</td>
<td>Comparación de inventario (mock)</td>
<td>T-TS06.1</td>
<td>Mock GET /inventario/comparacion/{productoId}</td>
<td>Comparación con ventas y compras.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US08</td>
<td>Listado de productos por nivel de stock</td>
<td>T-US08.1</td>
<td>Listado con búsqueda</td>
<td>Búsqueda y columna de sensor.</td>
<td>4</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US08</td>
<td>Listado de productos por nivel de stock</td>
<td>T-US08.2</td>
<td>Filtro por nivel de stock</td>
<td>Bajo, normal o sin datos.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US08</td>
<td>Listado de productos por nivel de stock</td>
<td>T-US08.3</td>
<td>Columna de stock registrado</td>
<td>Stock actualizado por movimientos.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US07</td>
<td>Visualización del peso actual de un producto</td>
<td>T-US07.1</td>
<td>Detalle con peso actual</td>
<td>Peso del sensor y unidades equivalentes.</td>
<td>4</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
<tr>
<td>2</td>
<td>US07</td>
<td>Visualización del peso actual de un producto</td>
<td>T-US07.2</td>
<td>Últimas cinco lecturas</td>
<td>Historial corto de lecturas.</td>
<td>3</td>
<td>Geraldine</td>
<td>Done</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.2.4. Development Evidence for Sprint Review

Durante el Sprint 2 se implementó la Frontend Web Application de
SmartStock en Vue 3 en el repositorio InventiaStock/smartstock-frontend,
con las vistas, stores y servicios de IAM, IoT Device, Alerts &
Restocking, Product Catalog, Inventory Monitoring (incluidas ventas,
compras y proveedores) y Analytics & Reporting, consumiendo servicios
simulados. Cada tarea del Sprint Backlog se desarrolló en una rama
feature/\<contexto\>-\<tarea\> creada desde develop e integrada mediante
pull request con merge commit.

La tabla presenta los commits relacionados con la implementación,
organizados por rama según GitFlow y redactados bajo Conventional
Commits, en inglés y en minúsculas, con el identificador de la tarea
(por ejemplo T-US02.1) en el cuerpo del mensaje.  

**Tabla 39**

*Commits relacionados con la implementación del Sprint 2*

<table>
<tbody>
<tr>
<th>Repository</th>
<th>Branch</th>
<th>Commit Id</th>
<th>Commit Message</th>
<th>Commit Message Body</th>
<th>Commited on (Date)</th>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>ab4d22a</td>
<td>chore(shared): split translations per bounded context</td>
<td>One translations folder per context; owners edit only their own. Task: T-SH.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>8c1e4ab</td>
<td>chore(shared): add sprint 2 endpoints to environment</td>
<td>Notifications, comparison, dashboard and reports endpoints. Task: T-SH.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>c787d93</td>
<td>feat(shared): add api error and date range helpers</td>
<td>apiError/apiCode and DateRange helpers. Task: T-SH.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>991c9a7</td>
<td>feat(shared): add alert banner, summary card and page header</td>
<td>Reusable presentation components. Task: T-SH.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>b418324</td>
<td>refactor(shared): extend date range filter and status tag</td>
<td>Initial input, new status tones and shared styles. Task: T-SH.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-sprint2-setup</td>
<td>7a7f92b</td>
<td>feat(inventory): add stock movement model</td>
<td>StockMovement entity (R17). Task: T-SH.3</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-mock-server</td>
<td>f08d04c</td>
<td>chore(shared): add json-server mock backend skeleton</td>
<td>Server, helpers, in-memory db and scripts. Refs: T-TS01.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-mock-server</td>
<td>924cf3c</td>
<td>feat(shared): add stock movement, alert rules and product view for the mock</td>
<td>Movement engine, alert rules R19-R21. Refs: T-TS14.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/shared-mock-server</td>
<td>7ac6ec1</td>
<td>feat(devices): add sensor readings and status mock endpoints</td>
<td>Readings, status and IoT simulator. Refs: T-TS01.1, T-TS05.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-register-product</td>
<td>e1e5428</td>
<td>feat(catalog): add product model and api layer</td>
<td>Task: T-US13.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-register-product</td>
<td>9820b9d</td>
<td>feat(catalog): add catalog store</td>
<td>Task: T-US13.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-register-product</td>
<td>cf0a1f9</td>
<td>feat(catalog): add catalog translations</td>
<td>Task: T-US13.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-register-product</td>
<td>07d8133</td>
<td>feat(catalog): add register product view</td>
<td>Tasks: T-US13.1, T-US13.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-register-product</td>
<td>8e169d6</td>
<td>feat(catalog): add catalog mock endpoints</td>
<td>Refs: T-TS13.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>3732be9</td>
<td>feat(inventory): add purchase and supplier model and api layer</td>
<td>Task: T-US30.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>7708a9f</td>
<td>feat(inventory): add purchases store</td>
<td>Task: T-US30.4</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>647e310</td>
<td>feat(inventory): add purchases translations</td>
<td>Task: T-US29.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>651a94a</td>
<td>feat(inventory): add supplier list view</td>
<td>Tasks: T-US29.1, T-US29.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>0512742</td>
<td>feat(inventory): add purchase list view</td>
<td>Tasks: T-US31.1, T-US31.2</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>1d07274</td>
<td>feat(inventory): add new purchase view</td>
<td>Tasks: T-US30.1, T-US30.2, T-US30.4</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>67767bc</td>
<td>feat(inventory): add purchase details view</td>
<td>Task: T-US30.3</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-purchases</td>
<td>5686709</td>
<td>feat(inventory): add purchases and suppliers mock endpoints</td>
<td>Refs: T-TS09.1, T-TS10.1, T-TS11.1, T-TS12.1</td>
<td>04/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/devices-sensor-linking</td>
<td>0fcfc02</td>
<td>feat(devices): add sensor domain model and api layer</td>
<td>Task: T-US04.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/devices-sensor-linking</td>
<td>cc49da9</td>
<td>feat(devices): add devices store</td>
<td>Task: T-US04.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/devices-sensor-linking</td>
<td>c8fff55</td>
<td>feat(devices): add devices translations</td>
<td>Task: T-US04.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/devices-sensor-linking</td>
<td>6448432</td>
<td>feat(devices): add sensor linking view</td>
<td>Tasks: T-US04.1, T-US04.2, T-US04.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-dashboard</td>
<td>ca31c2a</td>
<td>feat(analytics): add dashboard and report model and api layer</td>
<td>Task: T-US15.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-dashboard</td>
<td>8510857</td>
<td>feat(analytics): add analytics store</td>
<td>Task: T-US15.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-dashboard</td>
<td>de9d94e</td>
<td>feat(analytics): add analytics translations</td>
<td>Task: T-US15.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-dashboard</td>
<td>b947557</td>
<td>feat(analytics): add dashboard view</td>
<td>Tasks: T-US15.1, T-US15.2, T-US15.4</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-dashboard</td>
<td>98a5d9a</td>
<td>feat(analytics): add dashboard and reports mock endpoints</td>
<td>Refs: T-US15.5</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-comparison</td>
<td>de281d6</td>
<td>feat(inventory): add stock comparison model and api layer</td>
<td>Task: T-US11.4</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-comparison</td>
<td>05e9775</td>
<td>feat(inventory): add stock store</td>
<td>Task: T-US11.4</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-comparison</td>
<td>1231e51</td>
<td>feat(inventory): add stock translations</td>
<td>Task: T-US11.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-comparison</td>
<td>0d6b028</td>
<td>feat(inventory): add stock comparison view</td>
<td>Tasks: T-US11.1, T-US11.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-comparison</td>
<td>a8612a5</td>
<td>feat(inventory): add stock and comparison mock endpoints</td>
<td>Refs: T-TS02.1, T-TS06.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/devices-sensor-status</td>
<td>cf52668</td>
<td>feat(devices): add sensor status list view</td>
<td>Tasks: T-US06.1, T-US06.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-edit-product</td>
<td>38a084d</td>
<td>feat(catalog): add edit product view</td>
<td>Tasks: T-US14.1, T-US14.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/catalog-min-threshold</td>
<td>039ef29</td>
<td>feat(catalog): add minimum threshold view</td>
<td>Tasks: T-US05.1, T-US05.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-email</td>
<td>09d74f5</td>
<td>feat(alerts): add alert model and api layer</td>
<td>Task: T-US09.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-email</td>
<td>93adae7</td>
<td>feat(alerts): add alerts store</td>
<td>Task: T-US09.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-email</td>
<td>58411f9</td>
<td>feat(alerts): add alerts translations</td>
<td>Task: T-US09.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-email</td>
<td>3d58c28</td>
<td>feat(alerts): add notification settings view</td>
<td>Tasks: T-US09.1, T-US10.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-email</td>
<td>2707a3d</td>
<td>feat(alerts): add alerts and notifications mock endpoints</td>
<td>Refs: T-TS03.1, T-TS14.2, T-TS15.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/analytics-reports</td>
<td>8c113c5</td>
<td>feat(analytics): add reports view</td>
<td>Tasks: T-US25.1, T-US25.2, T-US25.3, T-US25.4</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-product-list</td>
<td>b43a5e6</td>
<td>feat(inventory): add product list view with stock levels</td>
<td>Tasks: T-US08.1, T-US08.2, T-US08.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-stock-weight</td>
<td>cb46b1f</td>
<td>feat(inventory): add product details view with current weight</td>
<td>Tasks: T-US07.1, T-US07.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/alerts-active-list</td>
<td>0ecbd35</td>
<td>feat(alerts): add active alerts list view</td>
<td>Tasks: T-US12.2, T-US32.1, T-US32.2, T-US32.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-login</td>
<td>dfe5ad4</td>
<td>feat(iam): add user session model and auth api</td>
<td>Task: T-US02.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-login</td>
<td>100a89f</td>
<td>feat(iam): add iam store</td>
<td>Task: T-US02.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-login</td>
<td>dcb278e</td>
<td>feat(iam): add iam translations</td>
<td>Task: T-US02.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-login</td>
<td>067bea8</td>
<td>feat(iam): add login view</td>
<td>Tasks: T-US02.1, T-US02.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-login</td>
<td>3894f21</td>
<td>feat(iam): add auth mock endpoints</td>
<td>Refs: T-TS04.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>ae1ffeb</td>
<td>feat(inventory): add sale model and api layer</td>
<td>Task: T-US26.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>0989723</td>
<td>feat(inventory): add sales store</td>
<td>Task: T-US26.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>75d10bf</td>
<td>feat(inventory): add sales translations</td>
<td>Task: T-US26.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>2ad80c8</td>
<td>feat(inventory): add sales list view</td>
<td>Tasks: T-US27.1, T-US27.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>287e64a</td>
<td>feat(inventory): add new sale view</td>
<td>Tasks: T-US26.1, T-US26.2, T-US26.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>e41b69a</td>
<td>feat(inventory): add sale details view</td>
<td>Task: T-US28.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/inventory-sales</td>
<td>fa72453</td>
<td>feat(inventory): add sales mock endpoints</td>
<td>Refs: T-TS07.1, T-TS08.1</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-register</td>
<td>c9f6cac</td>
<td>feat(iam): add registration view</td>
<td>Tasks: T-US01.1, T-US01.2, T-US01.3</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>feature/iam-password-recovery</td>
<td>438616d</td>
<td>feat(iam): add password recovery view</td>
<td>Tasks: T-US03.1, T-US03.2</td>
<td>05/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>release/1.0.0</td>
<td>77fbb97</td>
<td>chore(release): set github pages base path</td>
<td>Use /smartstock-frontend/ in build and preview. Task: T-SH.1</td>
<td>06/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>release/1.0.0</td>
<td>da7d092</td>
<td>chore(release): add 404 fallback for the vue router</td>
<td>Copy index.html to 404.html after the build. Task: T-SH.1</td>
<td>06/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>release/1.0.0</td>
<td>1e95fc0</td>
<td>chore(release): add github pages deployment workflow</td>
<td>Build and publish dist/ when main changes. Task: T-SH.1</td>
<td>06/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-frontend</td>
<td>release/1.0.0</td>
<td>1cd9852</td>
<td>chore(release): set fake api url for production</td>
<td>The api url is read only from VITE_API_BASE_URL. Task: T-SH.1</td>
<td>06/10/2026</td>
</tr>
<tr>
<td>InventiaStock/smartstock-landing-page</td>
<td>feature/signup-frontend-link</td>
<td>d945662</td>
<td>feat(landing): redirect sign up to deployed frontend</td>
<td>—</td>
<td>07/10/2026</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

La tabla sigue el orden en que las ramas se integraron a develop:
primero las dos ramas compartidas y luego los contextos. En el
repositorio del frontend son 20 ramas (19 de feature y release/1.0.0) y
66 commits.

En el repositorio InventiaStock/smartstock-landing-page se registró
además un commit en la rama feature/signup-frontend-link, que actualiza
el enlace del botón de registro en index.html (menú de navegación y
encabezado) para que redirija a
<a href="https://inventiastock.github.io/smartstock-frontend/sign-up." style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/sign-up.</a>
La rama se integró a develop mediante el PR \#1 y develop se integró a
main mediante el PR \#2, con lo que el Landing Page actualizado quedó
publicado como v1.1.0.

#### 5.2.2.5. Execution Evidence for Sprint Review

En este sprint el frontend alcanzó las vistas de los seis contextos
funcionando con datos simulados: registro e inicio de sesión, ventas,
productos, proveedores y compras, sensores, alertas, stock, dashboard y
reportes. Cada captura se rotula con la historia que cubre. El video que
muestra la visualización y la navegación logradas en el sprint está en
<a href="https://upcedupe-my.sharepoint.com/%3Av%3A/g/personal/u202421125_upc_edu_pe/IQA0X9BfccMdRJeE63zaQfNvARW9W4pA0re8x3wlKPuZiqU?e=fPJy8k&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" style="color:#2563eb">https://upcedupe-my.sharepoint.com/&#58;v&#58;/g/personal/u202421125_upc_edu_pe/IQA0X9BfccMdRJeE63zaQfNvARW9W4pA0re8x3wlKPuZiqU?e=fPJy8k&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D</a>


**Tabla 40**
*Evidencia de ejecución por contexto e historia de usuario del Sprint 2*

<table>
<tbody>
<tr>
<th>Contexto</th>
<th>Historia</th>
<th>Ruta</th>
<th>La captura debe mostrar</th>
<th>Figura</th>
</tr>
<tr>
<td>IAM</td>
<td>US01 Registro de cuenta</td>
<td>/sign-up</td>
<td>Formulario con tipo de negocio y el error de correo en uso</td>
<td>161</td>
</tr>
<tr>
<td>IAM</td>
<td>US02 Inicio de sesión</td>
<td>/sign-in</td>
<td>Login y el mensaje de credenciales incorrectas</td>
<td>162</td>
</tr>
<tr>
<td>IAM</td>
<td>US03 Recuperación de contraseña</td>
<td>/forgot-password</td>
<td>Solicitud del enlace y restablecimiento</td>
<td>163</td>
</tr>
<tr>
<td>Ventas</td>
<td>US26, US27 y US28</td>
<td>/sales, /sales/new, /sales/:id</td>
<td>Venta registrada, rechazo por stock insuficiente, historial por fechas y detalle</td>
<td>164</td>
</tr>
<tr>
<td>IoT Device</td>
<td>US04 Vinculación de sensor</td>
<td>/sensors/link</td>
<td>Selección de sensor y producto, y error de sensor en uso</td>
<td>165</td>
</tr>
<tr>
<td>IoT Device</td>
<td>US06 y US07 Estado y peso actual</td>
<td>/sensors</td>
<td>Sensores en línea y desconectados, y peso con su equivalente en unidades</td>
<td>166</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>US09 y US10 Notificaciones</td>
<td>/settings</td>
<td>Canales de correo y WhatsApp configurados</td>
<td>167</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>US12 y US32 Alertas y compra desde alerta</td>
<td>/alerts</td>
<td>Alerta de stock bajo o discrepancia y el botón que abre el registro de compra</td>
<td>168</td>
</tr>
<tr>
<td>Product Catalog</td>
<td>US13, US14 y US05 Productos</td>
<td>/products</td>
<td>Registro, edición y umbral mínimo con su error de validación</td>
<td>169</td>
</tr>
<tr>
<td>Proveedores y Compras</td>
<td>US29, US30 y US31</td>
<td>/purchases, /purchases/new, /purchases/suppliers</td>
<td>Proveedor creado, compra pendiente, compra recibida e historial por fechas</td>
<td>170</td>
</tr>
<tr>
<td>Inventory Monitoring</td>
<td>US08 y US11</td>
<td>/products, /comparison</td>
<td>Niveles de stock y comparación físico vs. registrado (solo minimarket)</td>
<td>171</td>
</tr>
<tr>
<td>Analytics & Reporting</td>
<td>US15 y US25</td>
<td>/dashboard, /reports</td>
<td>Tarjetas del día con ventas y compras, y reporte por periodo</td>
<td>172</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Figura 217**

*Registro de cuenta con selección de tipo de negocio (US01)*

<img src="../assets/chapter-5/figura_217.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 218**

*Inicio de sesión con mensaje de credenciales incorrectas (US02)*

<img src="../assets/chapter-5/figura_218.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 219**

*Recuperación de contraseña: solicitud del enlace y confirmación de*

envío (US03)
<img src="../assets/chapter-5/figura_219.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 220**

*Ventas: (a) venta registrada, (b) rechazo por stock insuficiente,*

(c) historial por fechas y (d) detalle con movimiento de salida (US26,
US27, US28)
<img src="../assets/chapter-5/figura_220.png" style="max-height:6.6cm">  
  

Nota. Elaboración propia

**Figura 221**

*Vinculación de sensor a un producto y error de sensor en uso*

(US04)
<img src="../assets/chapter-5/figura_221.png" style="max-height:6.6cm">

  
Nota. Elaboración propia

**Figura 222**

*Estado de conexión de sensores en línea y desconectados (US06)*

<img src="../assets/chapter-5/figura_222.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 223**

*Configuración de notificaciones por correo y WhatsApp (US09, US10)*

<img src="../assets/chapter-5/figura_223.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 224**

*Alertas activas y botón de compra desde una alerta de stock bajo*

(US12, US32)
<img src="../assets/chapter-5/figura_224.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 225**

*Catálogo: (a) registro de producto, (b) edición con stock de solo*

lectura (US13, US14)

<img src="../assets/chapter-5/figura_225.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 226**

*Proveedores y compras: (a) proveedor creado, (b) compra pendiente,*

(c) compra recibida y (d) historial por fechas (US29, US30, US31)
<img src="../assets/chapter-5/figura_226.png" style="max-height:6.6cm">

  
Nota. Elaboración propia

**Figura 227**

*Monitoreo de inventario: (a) productos por nivel de stock, (b)*

detalle con peso actual y (c) comparación físico vs. registrado (US07,
US08, US11)
<img src="../assets/chapter-5/figura_227.png" style="max-height:6.6cm">Nota. Elaboración propia  

**Figura 228**

*Dashboard con ventas y compras del día, y reporte por período (US15,*

US25)
<img src="../assets/chapter-5/figura_228.png" style="max-height:6.6cm">

  
Nota. Elaboración propia

**Figura 229**

*Menú lateral según tipo de negocio: (a) bodega y (b) minimarket*

(US01)
<img src="../assets/chapter-5/figura_229.png" style="max-height:6.6cm">

  
Nota. Elaboración propia

#### 5.2.2.6. Services Documentation Evidence for Sprint Review

En el Sprint 2 el equipo documentó con OpenAPI los contratos de los
endpoints que las pantallas consumen a través de la Fake API: los de las
Technical Stories TS01 a TS15 y los de autenticación que usan las
pantallas de registro y recuperación (21 operaciones). Los Web Services
reales (ASP.NET Core) se implementarán en el Sprint 3 con el mismo
contrato; por eso aún no existe el repositorio de Web Services ni hay
commits de documentación en este sprint. La especificación de los Web
Services se redactó en formato OpenAPI 3.0.3 utilizando Swagger Editor y
se visualiza mediante Swagger UI (Figuras 174 y 175). Los endpoints
documentados corresponden a los contratos que el frontend consume
actualmente a través de la Fake API; su implementación real en el
backend se realizará en el Sprint 3. . Los contratos se documentan con
el prefijo /api del backend real; la Fake API desplegada los expone en
la raíz, sin ese prefijo (por ejemplo, POST /auth/login).

**Tabla 41**

*Documentación de los endpoints de los Web Services del Sprint 2*

<table style="font-size:8pt; word-break:break-word; table-layout:fixed; width:100%;">
<tbody>
<tr>
<th>Endpoint</th>
<th>Método</th>
<th>Acción</th>
<th>Parámetros</th>
<th>Ejemplo de request</th>
<th>Response y explicación</th>
<th>TS</th>
</tr>
<tr>
<td>/api/auth/register</td>
<td>POST</td>
<td>Registra una cuenta</td>
<td>—</td>
<td>{ "businessName": "Bodega Luna", "email": "ana@bodega.pe", "password": "•••", "businessType": "bodega" }</td>
<td>201 con la sesión { token, email, businessName, businessType }; 400 si faltan datos; 409 si el correo ya está registrado</td>
<td>TS04</td>
</tr>
<tr>
<td>/api/auth/forgot-password</td>
<td>POST</td>
<td>Solicita el enlace de recuperación</td>
<td>—</td>
<td>{ "email": "ana@bodega.pe" }</td>
<td>200 con { sent: true, email, expiresInHours: 24 }; la respuesta es la misma si el correo no existe (R4)</td>
<td>TS04</td>
</tr>
<tr>
<td>/api/auth/login</td>
<td>POST</td>
<td>Valida credenciales</td>
<td>—</td>
<td>{ "email": "ana@bodega.pe", "password": "•••" }</td>
<td>200 con la sesión { token, email, businessName, businessType }; 401 INVALID_CREDENTIALS si las credenciales son incorrectas, sin indicar cuál falló (R3)</td>
<td>TS04</td>
</tr>
<tr>
<td>/api/ventas</td>
<td>POST</td>
<td>Registra una venta</td>
<td>—</td>
<td>{ "items": [{ "productoId": 3, "cantidad": 2, "precioUnitario": 4.5 }] }. Sin precioUnitario el mock responde 422</td>
<td>201 con { id } del comprobante (ej. R-00042); 400 si no hay ítems o la cantidad es inválida; 422 si la cantidad supera el stock (indica producto y stock disponible) o si el producto no tiene precio de venta (R14)</td>
<td>TS07</td>
</tr>
<tr>
<td>/api/ventas</td>
<td>GET</td>
<td>Lista las ventas</td>
<td>desde, hasta (fecha)</td>
<td>—</td>
<td>200 con la lista de ventas del rango</td>
<td>TS08</td>
</tr>
<tr>
<td>/api/ventas/{id}</td>
<td>GET</td>
<td>Detalle de una venta</td>
<td>id (ruta)</td>
<td>—</td>
<td>200 con ítems, precios y total; 404 si no existe</td>
<td>TS08</td>
</tr>
<tr>
<td>/api/proveedores</td>
<td>POST</td>
<td>Registra un proveedor</td>
<td>—</td>
<td>{ "nombre": "Distribuidora Sol", "telefono": "987654321" }</td>
<td>201 con el proveedor; 409 si ya existe el mismo nombre y teléfono</td>
<td>TS09</td>
</tr>
<tr>
<td>/api/proveedores</td>
<td>GET</td>
<td>Lista los proveedores</td>
<td>—</td>
<td>—</td>
<td>200 con la lista de proveedores</td>
<td>TS09</td>
</tr>
<tr>
<td>/api/compras</td>
<td>POST</td>
<td>Registra una compra pendiente</td>
<td>—</td>
<td>{ "proveedorId": 1, "items": [{ "productoId": 3, "cantidad": 24, "costoUnitario": 2.5 }] }</td>
<td>201 con la orden (PO-00031) en estado pendiente, sin cambiar el stock; 422 si no tiene ítems</td>
<td>TS10</td>
</tr>
<tr>
<td>/api/compras</td>
<td>GET</td>
<td>Lista las compras</td>
<td>desde, hasta (fecha)</td>
<td>—</td>
<td>200 con la lista de compras del rango</td>
<td>TS12</td>
</tr>
<tr>
<td>/api/productos</td>
<td>GET</td>
<td>Lista los productos</td>
<td>—</td>
<td>—</td>
<td>200 con la lista de productos, con su stock registrado y su sensor vinculado (si lo tienen)</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/productos</td>
<td>POST</td>
<td>Registra un producto</td>
<td>—</td>
<td>{ "nombre": "Rice 1 kg", "categoria": "Grocery", "pesoUnitario": 1, "precioVenta": 4.5, "costoCompra": 3.2, "umbralMinimo": 5, "capacidadMaxima": 100 }</td>
<td>201 con el producto creado (el stock arranca en 0 y sin sensor); 400 INVALID_PRODUCT con el detalle de errores por campo si incumple R5 o R7</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/compras/{id}</td>
<td>GET</td>
<td>Detalle de una compra</td>
<td>id (ruta)</td>
<td>—</td>
<td>200 con ítems y estado; 404 si no existe</td>
<td>TS12</td>
</tr>
<tr>
<td>/api/compras/{id}/recepcion</td>
<td>PATCH</td>
<td>Recibe la compra</td>
<td>id (ruta)</td>
<td>—</td>
<td>200 con la compra recibida y el stock sumado; 409 si ya fue recibida</td>
<td>TS11</td>
</tr>
<tr>
<td>/api/sensores/{id}/lecturas</td>
<td>POST</td>
<td>Recibe una lectura de peso</td>
<td>id (ruta)</td>
<td>{ "pesoKg": 12.4, "fecha": "2026-10-04T10:15:00" }</td>
<td>201 con el id de la lectura; 404 si el sensor no existe</td>
<td>TS01</td>
</tr>
<tr>
<td>/api/sensores/{id}/estado</td>
<td>GET</td>
<td>Estado del sensor</td>
<td>id (ruta)</td>
<td>—</td>
<td>200 con estado (en línea o desconectado) y última lectura</td>
<td>TS05</td>
</tr>
<tr>
<td>/api/productos/{id}</td>
<td>PUT</td>
<td>Edita un producto</td>
<td>id (ruta)</td>
<td>{ "precioVenta": 5.2, "costoCompra": 3.5, "proveedorHabitual": "Distribuidora Sol" }</td>
<td>200 con el producto actualizado; 400 INVALID_PRODUCT; 404 si no existe. Nunca cambia el stock ni el sensor: el stock solo se mueve por movimientos (R17)</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/productos/{id}/stock</td>
<td>GET</td>
<td>Stock registrado</td>
<td>id (ruta)</td>
<td>—</td>
<td>200 con el stock y su nivel</td>
<td>TS02</td>
</tr>
<tr>
<td>/api/inventario/comparacion/{productoId}</td>
<td>GET</td>
<td>Compara peso físico y registrado</td>
<td>productoId (ruta)</td>
<td>—</td>
<td>200 con ambos valores y la diferencia porcentual</td>
<td>TS06</td>
</tr>
<tr>
<td>/api/notificaciones/stock-bajo</td>
<td>POST</td>
<td>Notifica stock bajo</td>
<td>—</td>
<td>{ "productoId": 3, "canal": "email" }</td>
<td>200 con la notificación enviada por los canales activos</td>
<td>TS03</td>
</tr>
<tr>
<td>/api/movimientos-stock</td>
<td>GET</td>
<td>Lista los movimientos de stock</td>
<td>desde, hasta (fecha)</td>
<td>—</td>
<td>200 con entradas, salidas y ajustes del periodo</td>
<td>TS15</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 42**

*Relación de endpoints*

<table>
<tbody>
<tr>
<th>Contexto</th>
<th>Recurso</th>
<th>Acciones</th>
<th>TS</th>
</tr>
<tr>
<td>IAM</td>
<td>/api/auth/login, /register, /forgot-password</td>
<td>POST</td>
<td>TS04</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores/{id}/lecturas</td>
<td>POST</td>
<td>TS01</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores/{id}/estado</td>
<td>GET</td>
<td>TS05</td>
</tr>
<tr>
<td>Product Catalog</td>
<td>/api/productos, /api/productos/{id}</td>
<td>GET, POST, PUT</td>
<td>TS13</td>
</tr>
<tr>
<td>Inventory Monitoring</td>
<td>/api/productos/{id}/stock</td>
<td>GET</td>
<td>TS02</td>
</tr>
<tr>
<td>Inventory Monitoring</td>
<td>/api/inventario/comparacion/{productoId}</td>
<td>GET</td>
<td>TS06</td>
</tr>
<tr>
<td>Inventory – Ventas</td>
<td>/api/ventas, /api/ventas/{id}</td>
<td>GET, POST / GET</td>
<td>TS07, TS08</td>
</tr>
<tr>
<td>Inventory – Compras</td>
<td>/api/proveedores</td>
<td>GET, POST</td>
<td>TS09</td>
</tr>
<tr>
<td>Inventory – Compras</td>
<td>/api/compras, /api/compras/{id}</td>
<td>GET, POST / GET</td>
<td>TS10, TS12</td>
</tr>
<tr>
<td>Inventory – Compras</td>
<td>/api/compras/{id}/recepcion</td>
<td>PATCH</td>
<td>TS11</td>
</tr>
<tr>
<td>Inventory – Movimientos</td>
<td>/api/movimientos-stock</td>
<td>GET</td>
<td>TS15</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>/api/notificaciones/stock-bajo</td>
<td>POST</td>
<td>TS03</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Figura 230**

*Documentación OpenAPI de los endpoints del Sprint 2 en Swagger*

Editor
<img src="../assets/chapter-5/figura_230.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 231**

*Detalle del endpoint POST /api/ventas con ejemplo de solicitud y*

respuestas documentadas
<img src="../assets/chapter-5/figura_231.png" style="max-height:6.6cm">  

Nota. Elaboración propia

#### 5.2.2.7. Software Deployment Evidence for Sprint Review

Durante el Sprint 2 el alcance de despliegue correspondió a la primera
versión de la Frontend Web Application, publicada en GitHub Pages desde
la rama main, a la que se integró mediante la rama release/1.0.0 (PR
\#20) y quedó etiquetada como v1.0.0. El Landing Page, publicado en el
Sprint 1, se actualizó para que su botón de registro redirija a la
aplicación desplegada (PR \#1 y PR \#2 del repositorio del Landing Page)
y quedó etiquetado como v1.1.0. Los Web Services no forman parte de este
sprint.

**Tabla 43**

*Evidencia de despliegue del Sprint 2*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Repositorio</th>
<th>URL desplegada</th>
<th>Versión</th>
<th>Estado</th>
</tr>
<tr>
<td>Landing Page</td>
<td><a href="https://github.com/InventiaStock/smartstock-landing-page" style="color:#2563eb">https://github.com/InventiaStock/smartstock-landing-page</a></td>
<td><a href="https://inventiastock.github.io/smartstock-landing-page/" style="color:#2563eb">https://inventiastock.github.io/smartstock-landing-page/</a></td>
<td>v1.1.0</td>
<td>Desplegado en el Sprint 1; actualizado en el Sprint 2 (registro hacia el frontend)</td>
</tr>
<tr>
<td>Frontend Web Application</td>
<td><a href="https://github.com/InventiaStock/smartstock-frontend.git" style="color:#2563eb">https://github.com/InventiaStock/smartstock-frontend.git</a></td>
<td><a href="https://inventiastock.github.io/smartstock-frontend/" style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/</a></td>
<td>v1.0.0</td>
<td>Primera versión desplegada</td>
</tr>
<tr>
<td>Fake API (json-server)</td>
<td><a href="https://github.com/InventiaStock/smartstock-frontend/tree/main/server" style="color:#2563eb">https://github.com/InventiaStock/smartstock-frontend/tree/main/server</a></td>
<td><a href="https://smartstock-fake-api.onrender.com" style="color:#2563eb">https://smartstock-fake-api.onrender.com</a></td>
<td>v1.0.0</td>
<td>Desplegada</td>
</tr>
<tr>
<td>Web Services</td>
<td>[aún no creado; ASP.NET Core]</td>
<td>—</td>
<td>—</td>
<td>Previsto para el Sprint 3</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

Las actividades de despliegue fueron: (1) habilitar GitHub Pages con
*Source: GitHub Actions*; (2) crear el workflow deploy.yml («Deploy
frontend to GitHub Pages»), que al integrar en main ejecuta un job
*build* (Node 22, npm install, npm run build) y un job *deploy*; (3)
preparar release/1.0.0 con cuatro commits de la tarea T-SH.1: ruta base
/smartstock-frontend/ en vite.config.js y el router, copia de index.html
como 404.html mediante el script postbuild, el workflow, y la URL de la
Fake API en .env.production; (4) actualizar el Landing Page: en el
repositorio del Landing Page se cambió el enlace del botón de registro,
que apuntaba a una dirección local, a
<a href="https://inventiastock.github.io/smartstock-frontend/sign-up," style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/sign-up,</a>
y se integró a main mediante los PR \#1 y \#2; y (5) verificar la URL
pública.

Como json-server no corre en GitHub Pages, la Fake API se publicó como
Web Service de Node en Render (plan gratuito): repositorio
InventiaStock/smartstock-frontend, rama main, build npm install
--include=dev, inicio node server/server.js y variables NODE_VERSION=22
y SIMULATE=1. Implementa los contratos documentados en 5.2.2.6 y, al ser
plan gratuito, se suspende tras unos 15 minutos sin uso: la primera
petición tarda cerca de un minuto y sus datos en memoria se reinician.
Cuando exista el backend, solo cambia VITE_API_BASE_URL en
.env.production.

El despliegue se verificó abriendo el Landing Page y comprobando que el
botón de registro abre la pantalla /sign-up del frontend desplegado, y
luego abriendo la URL pública del frontend, iniciando sesión, navegando
a Ventas y recargando la página (lo que prueba el 404.html), registrando
una venta de prueba y confirmando en la pestaña Network que las
peticiones van a la Fake API.

**Figura 232**

*Configuración de GitHub Pages con GitHub Actions como fuente.*

<img src="../assets/chapter-5/figura_232.png" style="max-height:6.6cm">

Nota. Pages del repositorio InventiaStock/smartstock-frontend; la aplicación se publica con el workflow deploy.yml al integrar en main.  

Figura 233  
Ejecución del workflow «Deploy frontend to GitHub Pages» con los jobs
build y deploy exitosos.
<img src="../assets/chapter-5/figura_233.png" style="max-height:6.6cm">

Nota. Ejecución disparada por el merge del PR \#20 en main. En la primera corrida, deploy fue rechazado por las reglas del entorno github-pages (no permitían main); tras permitirla, la reejecución terminó con éxito en 19 s.  

**Figura 234**

*Fake API desplegada en Render (Live, rama main).*

<img src="../assets/chapter-5/figura_234.png" style="max-height:6.6cm">

Nota. Web Service de Node, plan Free, repositorio

InventiaStock/smartstock-frontend, rama main, URL
<a href="https://smartstock-fake-api.onrender.com" style="color:#2563eb">https://smartstock-fake-api.onrender.com</a>  

**Figura 235**

*Verificación de la Fake API desplegada.*

<img src="../assets/chapter-5/figura_235.png" style="max-height:6.6cm">

Nota. POST /auth/forgot-password responde sent: True y

expiresInHours: 24.
Figura 236  
Frontend Web Application funcionando en su URL pública.
<img src="../assets/chapter-5/figura_236.png" style="max-height:6.6cm">

Nota. (a) Dashboard en

inventiastock.github.io/smartstock-frontend/dashboard con datos de la
Fake API; (b) recarga con F5 en /sales, que funciona gracias a
404.html.

#### 5.2.2.8. Team Collaboration Insights during Sprint

Durante el Sprint 2, el equipo organizó la implementación según los
aspectos definidos en la sección 5.2.2.2. Cada integrante trabajó sobre
el contexto que lideraba y registró su aporte mediante commits propios
en el repositorio InventiaStock/smartstock-frontend, aplicando GitFlow y
Conventional Commits.

El flujo de trabajo seguido se resume en la siguiente tabla:

**Tabla 44**

*Flujo de ramas de GitFlow seguido en el Sprint 2*

<table>
<tbody>
<tr>
<th>Rama</th>
<th>Nace de</th>
<th>Se integra en</th>
<th>Regla</th>
</tr>
<tr>
<td>main</td>
<td>—</td>
<td>—</td>
<td>Recibe únicamente las versiones publicadas; protegida, solo se modifica mediante pull request.</td>
</tr>
<tr>
<td>develop</td>
<td>—</td>
<td>—</td>
<td>Concentra el avance acumulado del sprint; protegida, solo se modifica mediante pull request.</td>
</tr>
<tr>
<td>feature/\<contexto\>-\<tarea\></td>
<td>develop</td>
<td>develop</td>
<td>Una rama corta por tarea del Sprint Backlog; se integra mediante pull request revisado por otro integrante, con merge commit (--no-ff).</td>
</tr>
<tr>
<td>release/\<x.y.z\></td>
<td>develop</td>
<td>main y de vuelta a develop</td>
<td>Prepara la versión a entregar; al integrarse en main se etiqueta con versionado semántico (vX.Y.Z).</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

Los mensajes de commit siguen Conventional Commits (feat, fix, docs,
refactor, test, chore), en inglés, con el contexto como alcance, por
ejemplo feat(iam): add login view.

**Analíticos de colaboración de los repositorios**

La vista de contribuyentes de GitHub muestra a cuatro de los cinco
integrantes. Los seis commits de @leonardoXd1323 (ramas
feature/alerts-email y feature/alerts-active-list) no se atribuyen a su
cuenta porque se realizaron con un correo de git mal configurado; su
participación se evidencia en la vista Pulse (cinco autores), en los
pull requests \#12 y \#17 y en la tabla 39. El correo ya fue corregido
para los siguientes sprints.

**Figura 237**

*Contributors del repositorio InventiaStock/smartstock-frontend*

<img src="../assets/chapter-5/figura_237.png" style="max-height:6.6cm">  

Nota. Elaboración propia  

**Figura 238**

*Pulse del repositorio InventiaStock/smartstock-frontend: cinco autores y*

67 commits

<img src="../assets/chapter-5/figura_238.png" style="max-height:6.6cm">

Nota. Elaboración propia  

**Historial de ramas de los repositorios**

El grafo de red muestra la aplicación efectiva de GitFlow: las ramas de
feature nacen de develop, se integran nuevamente a ella mediante merge
commits, y la rama main recibe únicamente las versiones publicadas.

**Figura 239**

*Network graph del repositorio InventiaStock/smartstock-frontend*

<img src="../assets/chapter-5/figura_239.png" style="max-height:6.6cm">

Nota. Elaboración propia

### 5.2.3. Sprint 3

#### 5.2.3.1.Sprint Planning 3

En el Sprint Planning 3 el equipo definió como meta entregar la primera
versión desplegada de los Web Services de SmartStock (ASP.NET Core 9,
Entity Framework Core y MySQL), para que la Frontend Web Application
funcione con datos reales y persistentes en lugar de la Fake API. El
sprint incluye las 15 Technical Stories (TS01 a TS15) y las 30
operaciones de la API. Por indicación del docente, la autenticación
(inicio de sesión y token JWT) pasó al Sprint 4: por ahora los endpoints
van abiertos y trabajan con un negocio fijo (id 1). El documento se
elaboró el 2026-11-05 y el equipo lo revisó de forma asíncrona, sin
reunión.

**Tabla 45**

*Sprint Planning 3*

<table>
<tbody>
<tr>
<th>Campo</th>
<th>Detalle</th>
</tr>
<tr>
<td><b>Sprint #</b></td>
<td>Sprint 3</td>
</tr>
<tr>
<td><b>Date</b></td>
<td>2026-11-02</td>
</tr>
<tr>
<td><b>Time</b></td>
<td>2:00 PM</td>
</tr>
<tr>
<td><b>Location</b></td>
<td>Reunión virtual</td>
</tr>
<tr>
<td><b>Prepared By</b></td>
<td>Montañez Salinas, Lorena Ariana</td>
</tr>
<tr>
<td><b>Attendees</b></td>
<td>Lopez Rimachi, Sebastian Leonardo / Montañez Salinas, Lorena Ariana / Sanchez Osorio, Ruth Yanira / Suarez Chinga, Geraldine / Vizcarra Mamani, Candy Milagros</td>
</tr>
<tr>
<td><b>Sprint 2 – Review Summary</b></td>
<td>El frontend de SmartStock quedó desplegado (v1.0.0) en GitHub Pages con Compras y Ventas como núcleo, consumiendo una Fake API publicada en Render; el Landing Page se actualizó (v1.1.0) para redirigir el registro a la aplicación. En la revisión de TB1 el docente calificó 18/20 y observó que el informe debe estar ligado al README, que los escenarios deben seguir Given-When-Then y que faltaba el precio de nuestro producto en la comparación de competidores. Mejora continua obtuvo 1 de 3 por falta de autocrítica.</td>
</tr>
<tr>
<td><b>Sprint 2 – Retrospective Summary</b></td>
<td>Funcionó bien: GitFlow con pull request y merge commit, ramas cortas por tarea y datos simulados para avanzar en paralelo. A mejorar: revisar el contenido copiado de otro curso (stack y enlaces), cerrar los textos "pendiente" antes de entregar y dejar evidencia de cada corrección. Para el Sprint 3 el equipo acordó: (1) cada integrante construye el backend del contexto que ya construyó en el frontend; (2) los contextos se comunican solo por fachadas; (3) la base de datos se crea en Aiven con migraciones; y (4) cada corrección queda registrada con su evidencia.</td>
</tr>
<tr>
<td><b>Sprint 3 Goal</b></td>
<td>Our focus is on delivering the first deployed version of the SmartStock Web Services, so the Vue application works on real and persistent data instead of the Fake API. We believe it delivers reliable control of sales, purchases and stock, verified by IoT sensors, to minimarket and bodega owners. This will be confirmed when a user can create a product, record a purchase and a sale in the deployed web application, see the stock change with its movements, receive a low stock alert by email, and the 30 operations are documented in Scalar.</td>
</tr>
<tr>
<td><b>Sprint 3 Velocity</b></td>
<td>45 Story Points</td>
</tr>
<tr>
<td><b>Sum of Story Points</b></td>
<td>45 (TS01 a TS15)</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

La suma de 45 Story Points incluye los 3 puntos de TS04, aunque en este
sprint solo se implementan sus tablas de IAM; el inicio de sesión y el
token JWT se completan en el Sprint 4.

Como el Sprint 2 recibió 1 de 3 en Mejora continua por falta de
autocrítica, el equipo registra a continuación las observaciones
recibidas y los hallazgos propios, con la mejora acordada y el lugar del
informe donde se evidencia.

**Tabla 46**

*Autocrítica y mejoras acordadas para AV2*

<table>
<tbody>
<tr>
<th>Id</th>
<th>Entrega</th>
<th>Autocrítica</th>
<th>Mejora acordada</th>
<th>Evidencia</th>
</tr>
<tr>
<td>M01</td>
<td>TB1</td>
<td>El README solo tenía un resumen y el informe vivía aparte.</td>
<td>El README contiene el informe completo, generado desde los capítulos del repositorio.</td>
<td>README del repositorio de documentación</td>
</tr>
<tr>
<td>M02</td>
<td>TB1</td>
<td>Los criterios de aceptación no seguían el orden Given-When-Then.</td>
<td>Reescribir las User Stories y Technical Stories con Given / When / Then / And en inglés y el resto en español.</td>
<td>Sección 3.1</td>
</tr>
<tr>
<td>M03</td>
<td>TB1</td>
<td>La comparación de precios no incluía el precio de SmartStock.</td>
<td>Agregar los planes Starter (S/ 49), Growth (S/ 129) y Business (S/ 279) y analizarlos frente a la competencia.</td>
<td>Secciones 2.1.1 y 2.1.2</td>
</tr>
<tr>
<td>M04 a M06</td>
<td>TB1</td>
<td>La tabla de herramientas conservaba el stack de otro curso (Java, Spring Boot, Angular), el enlace apuntaba a otra organización y quedaban textos "pendiente".</td>
<td>Reemplazar por C#, ASP.NET Core, EF Core, MySQL, Vue y PrimeVue; apuntar a InventiaStock; completar repositorios y despliegue.</td>
<td>Secciones 5.1.1, 5.1.2 y 5.1.4</td>
</tr>
<tr>
<td>M07, M08 y M17</td>
<td>TB1</td>
<td>Los diagramas C4 hablaban de módulos "previstos", faltaba el diagrama de componentes de Alerts & Restocking y el diagrama de base de datos no coincidía con las 16 tablas implementadas.</td>
<td>Actualizar los textos, dibujar el diagrama faltante y regenerar el diagrama de base de datos desde MySQL.</td>
<td>Secciones 4.6.4 y 4.8.1</td>
</tr>
<tr>
<td>M19</td>
<td>AV1</td>
<td>La evidencia colaborativa por persona estaba incompleta, persistieron errores y hubo observaciones de ortografía y estructura.</td>
<td>Capturas de commits, Scalar y Trello por integrante; revisión de ortografía antes de entregar.</td>
<td>Secciones 5.2.3.4 a 5.2.3.8</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.3.2. Aspect Leaders and Collaborators

Los aspectos de este sprint son cinco grupos de trabajo que agrupan los
seis bounded contexts del backend y el trabajo compartido: Data Model &
Sales (tablas de IAM y de los demás contextos, shared kernel y Ventas);
Catalog & Procurement (productos, proveedores y compras); IoT, Analytics
& Deployment (sensores, lecturas, dashboard, reportes y despliegue en
Render y Aiven); Stock Movements (motor de movimientos, consulta de
stock y comparación de inventario); y Alerts & Frontend (alertas,
notificaciones por correo y WhatsApp, y conexión de la aplicación Vue
con la API real). Cada integrante lidera un aspecto y colabora en los
demás (L = líder, C = colaborador), revisando pull requests y probando
sus pantallas contra la API; esta distribución se refleja en la
selección de tasks de la sección 5.2.3.3 y en la autoría de los commits.

**Tabla 47**

*Matriz de liderazgo y colaboración (LACX) del Sprint 3*

<table style="font-size:10pt;">
<tbody>
<tr>
<th>Team Member</th>
<th>GitHub Username</th>
<th>Data Model & Sales</th>
<th>Catalog & Procurement</th>
<th>IoT, Analytics & Deployment</th>
<th>Stock Movements</th>
<th>Alerts & Frontend</th>
</tr>
<tr>
<td>Montañez Salinas, Lorena Ariana</td>
<td>Lore-MS</td>
<td>L</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Vizcarra Mamani, Candy Milagros</td>
<td>candyvizz</td>
<td>C</td>
<td>L</td>
<td>C</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Sanchez Osorio, Ruth Yanira</td>
<td>Yiya-ciber</td>
<td>C</td>
<td>C</td>
<td>L</td>
<td>C</td>
<td>C</td>
</tr>
<tr>
<td>Suarez Chinga, Geraldine</td>
<td>geral07-UNIV</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>L</td>
<td>C</td>
</tr>
<tr>
<td>Lopez Rimachi, Sebastian Leonardo</td>
<td>leonardoXd1323</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>C</td>
<td>L</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.3.3.Sprint Backlog 3

El objetivo del Sprint 3 es entregar la primera versión desplegada de
los Web Services de SmartStock, para que la aplicación Vue funcione con
datos reales y persistentes. El sprint contiene las 15 Technical Stories
(TS01 a TS15), que suman 45 Story Points, y 50 tareas con 286 horas en
total. Las tareas de autenticación T-TS04.2 (servicios de registro,
inicio de sesión y recuperación) y T-TS04.3 (controlador y
documentación) pasan al Sprint 4 por indicación del docente. De TS04
solo se implementan las tablas de IAM (T-TS04.1). El tablero del sprint
está en Trello (figura 194) y su URL pública es:

URL pública del tablero:
<a href="https://trello.com/b/KSPnNOWF/sprint-backlog-3-web" style="color:#2563eb">https://trello.com/b/KSPnNOWF/sprint-backlog-3-web</a>

**Figura 240**

*Tablero de Trello del Sprint Backlog 3*

<img src="../assets/chapter-5/figura_240.png" style="max-height:6.6cm">

Nota. Elaboración propia

Las tareas se identifican como T-TS##.# (Technical Stories), T-US##.#
(endpoints de apoyo a pantallas existentes), T-SH3.# (setup compartido),
T-DOC3.# (documentación OpenAPI) y T-QA3.# (pruebas de aceptación).
Estas dos últimas familias y las de setup no tienen Story Points propios
y se agrupan como "Soporte técnico del sprint".

**Tabla 48**

**Sprint Backlog 3**

<table style="font-size:10pt;">
<tbody>
<tr>
<th><b>Sprint #</b></th>
<th>Story Id</th>
<th>Story Title</th>
<th>Task Id</th>
<th>Task Title</th>
<th>Task Description</th>
<th>Estimation (Hours)</th>
<th>Assigned To</th>
<th>Status</th>
</tr>
<tr>
<td>3</td>
<td>TS01</td>
<td>Endpoint de recepción de lecturas de sensores</td>
<td>T-TS01.1</td>
<td>Sensor and reading persistence</td>
<td>Sensor and SensorReading entities, tables sensors and sensor_readings, repository and demo sensors.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS01</td>
<td>Endpoint de recepción de lecturas de sensores</td>
<td>T-TS01.2</td>
<td>ReceiveReading service and endpoint</td>
<td>Public endpoint for the devices with optional X-Device-Key, 404 and 400 rules, triggers rule R20.</td>
<td>8</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS02</td>
<td>Endpoint de consulta de stock de un producto</td>
<td>T-TS02.1</td>
<td>Stock level query</td>
<td>GET /api/productos/{id}/stock with registered stock, reference stock and level.</td>
<td>4</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS02</td>
<td>Endpoint de consulta de stock de un producto</td>
<td>T-TS02.2</td>
<td>Product detail with sensor</td>
<td>GET /api/productos/{id}/detalle with the sensor and its last 5 readings.</td>
<td>5</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.1</td>
<td>Alert domain and persistence</td>
<td>Alert, RestockingNeed, NotificationChannel and SentNotification entities, tables and demo alerts.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.2</td>
<td>Alert rules R19, R20 and R21</td>
<td>AlertsFacade creates and resolves alerts after movements, readings and purchases.</td>
<td>8</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.3</td>
<td>Notification service and controller</td>
<td>POST /api/notificaciones/stock-bajo and GET/PUT of channels (at least one active).</td>
<td>6</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.4</td>
<td>Email through SMTP</td>
<td>SmtpEmailSender with MailKit; credentials from secrets, never in the repository.</td>
<td>6</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.5</td>
<td>WhatsApp through Twilio</td>
<td>TwilioWhatsAppSender with the sandbox; credentials from secrets.</td>
<td>6</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS03</td>
<td>Endpoint de envío de notificaciones de stock bajo</td>
<td>T-TS03.6</td>
<td>Alerts list query</td>
<td>GET /api/alertas with product name, threshold and sensor data.</td>
<td>4</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS04</td>
<td>Endpoint de autenticación</td>
<td>T-TS04.1</td>
<td>IAM domain and persistence</td>
<td>IAM tables: Business and User entities, EF Core configuration, repositories and demo business seed.</td>
<td>6</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>3</td>
<td>TS05</td>
<td>Endpoint de estado de conexión de un sensor</td>
<td>T-TS05.1</td>
<td>Sensor status and list</td>
<td>GET /api/sensores, /{id} and /{id}/estado with the 5-minute rule (R11).</td>
<td>6</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS06</td>
<td>Endpoint de comparación de inventario físico y registrado</td>
<td>T-TS06.1</td>
<td>Inventory comparison</td>
<td>List and per-product comparison (R20) with 409 NO_REGISTERED_QUANTITY.</td>
<td>8</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS07</td>
<td>Endpoint de registro de ventas</td>
<td>T-TS07.1</td>
<td>Sale domain and persistence</td>
<td>Sale and SaleItem entities, tables sales and sale_items, repository and demo sale R-00041.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS07</td>
<td>Endpoint de registro de ventas</td>
<td>T-TS07.2</td>
<td>RegisterSale service</td>
<td>Validates items, price and stock (R13, R14) and creates one OUT movement per item (R17).</td>
<td>8</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS08</td>
<td>Endpoints de consulta de ventas</td>
<td>T-TS08.1</td>
<td>Sales history and detail</td>
<td>GET /api/ventas by date range with total, and GET /api/ventas/{code} with its movements.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS09</td>
<td>Endpoints de proveedores</td>
<td>T-TS09.1</td>
<td>Suppliers service and controller</td>
<td>POST and GET /api/proveedores with duplicate detection (R8).</td>
<td>6</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS10</td>
<td>Endpoint de registro de compras</td>
<td>T-TS10.1</td>
<td>Purchase domain and persistence</td>
<td>Supplier, Purchase and PurchaseItem entities, tables suppliers, purchases and purchase_items, demo purchase PO-00031.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS10</td>
<td>Endpoint de registro de compras</td>
<td>T-TS10.2</td>
<td>RegisterPurchase service</td>
<td>PENDING purchase that does not change the stock (R15); it can come from an alert (R21).</td>
<td>6</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS11</td>
<td>Endpoint de recepción de compras</td>
<td>T-TS11.1</td>
<td>ReceivePurchase service</td>
<td>PATCH /api/compras/{code}/recepcion adds stock with IN movements (R16); 409 if repeated.</td>
<td>6</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS12</td>
<td>Endpoints de consulta de compras</td>
<td>T-TS12.1</td>
<td>Purchases history and detail</td>
<td>GET /api/compras by date range with total, and GET /api/compras/{code}.</td>
<td>6</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS13</td>
<td>Modelo de datos y migraciones de ventas y compras</td>
<td>T-TS13.1</td>
<td>Product entity and persistence</td>
<td>Product entity with sale_price and purchase_cost, EF configuration, repository and 5 demo products.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS13</td>
<td>Modelo de datos y migraciones de ventas y compras</td>
<td>T-TS13.2</td>
<td>Product services and validation</td>
<td>Create and edit product with rules R5 and R7, INVALID_PRODUCT errors by field, initial stock as movement.</td>
<td>8</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS13</td>
<td>Modelo de datos y migraciones de ventas y compras</td>
<td>T-TS13.3</td>
<td>Products controller and threshold</td>
<td>GET, POST and PUT /api/productos and PUT /api/sensores/{id}/umbral (US05).</td>
<td>6</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS13</td>
<td>Modelo de datos y migraciones de ventas y compras</td>
<td>T-TS13.4</td>
<td>InitialCreate migration, schema.sql and 16-table diagram</td>
<td>dotnet ef migration, schema.sql and the ERD exported from MySQL Workbench; shown to the professor on Wed 4 (Leonardo reuses the ERD image for section 4.8.1).</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS14</td>
<td>Registro automático de movimientos de stock</td>
<td>T-TS14.1</td>
<td>StockMovement entity and persistence</td>
<td>StockMovement entity, table stock_movements, repository and demo movements.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS14</td>
<td>Registro automático de movimientos de stock</td>
<td>T-TS14.2</td>
<td>Stock movement engine</td>
<td>IStockMovementFacade changes the stock through the catalog, saves the movement and asks Alerts to evaluate R19 (R17).</td>
<td>8</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>TS15</td>
<td>Endpoint de movimientos de stock</td>
<td>T-TS15.1</td>
<td>Movements query endpoint</td>
<td>GET /api/movimientos-stock with date filter; empty list when there are no movements.</td>
<td>4</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.1</td>
<td>OpenAPI evidence of Sales</td>
<td>Scalar screenshots and endpoint table for sales (section 5.2.3.6).</td>
<td>4</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.2</td>
<td>OpenAPI evidence of Catalog and Procurement</td>
<td>Scalar screenshots and endpoint table (section 5.2.3.6).</td>
<td>4</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.3</td>
<td>OpenAPI evidence of Stock and section 5.2.3.6</td>
<td>Scalar screenshots of Stock and the endpoint table of Stock (Lorena compiles the whole section 5.2.3.6).</td>
<td>6</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.4</td>
<td>OpenAPI evidence of IoT and Analytics</td>
<td>Scalar screenshots and endpoint table (section 5.2.3.6).</td>
<td>4</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.5</td>
<td>OpenAPI evidence of Alerts</td>
<td>Scalar screenshots and endpoint table (section 5.2.3.6).</td>
<td>4</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-DOC3.6</td>
<td>Sprint Backlog 3 table and Trello board</td>
<td>Task table of the report, public Trello board and final states (section 5.2.3.3).</td>
<td>4</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-QA3.1</td>
<td>Acceptance test of sales screens</td>
<td>Run the Vue screens against the real API and register defects.</td>
<td>4</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-QA3.2</td>
<td>Acceptance test of catalog, suppliers and purchases screens</td>
<td>Run the Vue screens against the real API and register defects.</td>
<td>4</td>
<td>Candy</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-QA3.3</td>
<td>Acceptance test of stock and comparison screens</td>
<td>Run the Vue screens against the real API and register defects.</td>
<td>4</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-QA3.4</td>
<td>Acceptance test of sensors, dashboard and reports screens</td>
<td>Run the Vue screens against the real API and register defects.</td>
<td>4</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-QA3.5</td>
<td>Acceptance test of alerts and notification screens</td>
<td>Run the Vue screens against the real API and register defects.</td>
<td>4</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.1</td>
<td>Backend repository and skeleton</td>
<td>Repository smartstock-backend, protected main and develop, skeleton, README.</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.2</td>
<td>Shared kernel</td>
<td>AppDbContext with tenant filter, error middleware, JSON names, open endpoints with fixed business 1 and contracts between contexts.</td>
<td>8</td>
<td>Lorena</td>
<td>Done</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.3</td>
<td>Local environment and CI</td>
<td>docker-compose, Dockerfile and GitHub Actions build and tests.</td>
<td>5</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.4</td>
<td>Cross-context foreign keys and integration build</td>
<td>CrossContextRelations.cs: foreign keys from sale_items, purchase_items, stock_movements, sensors and alerts to products (done together with the 16 tables).</td>
<td>6</td>
<td>Lorena</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.5</td>
<td>Deploy Web Services and MySQL</td>
<td>Render (Docker) and Aiven MySQL, environment variables, CORS and health check.</td>
<td>8</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.6</td>
<td>Connect the Vue app to the real API</td>
<td>Change VITE_API_BASE_URL, regression of the main flows and release v1.1.0 of the frontend.</td>
<td>8</td>
<td>Leonardo</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.7</td>
<td>Unit tests of business rules</td>
<td>xUnit project with tests for R8, R11, R12, R13, R15, R16, R17, R20 and JSON names.</td>
<td>6</td>
<td>Geraldine</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-SH3.8</td>
<td>IoT simulator and HTTP collection</td>
<td>iot-simulator.mjs and the .http files of sensors and analytics.</td>
<td>4</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-US04.3</td>
<td>Link sensor to product endpoint</td>
<td>POST /api/sensores/vincular with the conflicts of rule R9.</td>
<td>5</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-US15.3</td>
<td>Dashboard endpoint</td>
<td>GET /api/dashboard aggregating sales, purchases, alerts and stock level.</td>
<td>6</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
<tr>
<td>3</td>
<td>Soporte</td>
<td>Soporte técnico del sprint</td>
<td>T-US25.3</td>
<td>Reports endpoint</td>
<td>GET /api/reportes with totals and movements of a period.</td>
<td>5</td>
<td>Ruth</td>
<td>To Do</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

#### 5.2.3.4.Development Evidence for Sprint Review

Durante el Sprint 3 se implementaron los Web Services de SmartStock en
ASP.NET Core 9 en el repositorio InventiaStock/smartstock-backend,
organizados como un monolito modular con seis bounded contexts (IAM,
Product Catalog, IoT Device, Inventory Monitoring, Alerts & Restocking y
Analytics & Reporting) y persistencia en MySQL mediante Entity Framework
Core. Cada tarea del Sprint Backlog se desarrolló en una rama
feature/\<nombre-descriptivo\> creada desde develop e integrada mediante
pull request con merge commit.

Además, en el repositorio InventiaStock/smartstock-landing-page se
incorporó la sección de video del producto y del equipo.

La tabla presenta los commits relacionados con la implementación,
organizados por rama según GitFlow y redactados bajo Conventional
Commits, en inglés y en minúsculas, con el identificador de la tarea
(por ejemplo T-TS07.2) en el cuerpo del mensaje. Se exceptúan los merge
commits generados por GitHub y los commits del landing page, que no
incluyen el identificador de tarea.

De los commits listados, 34 pertenecen al repositorio smartstock-backend
y 3 al repositorio smartstock-landing-page.

**Tabla 49**

*Commits relacionados con la implementación del Sprint 3*

<table>
<tbody>
<tr>
<th>Repository</th>
<th>Branch</th>
<th>Commit Id</th>
<th>Commit Message</th>
<th>Commit Message Body</th>
<th>Committed on (Date)</th>
</tr>
<tr>
<td>smartstock-backend</td>
<td>main</td>
<td>74c0df8</td>
<td>Initial commit</td>
<td>—</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/shared-skeleton</td>
<td>02f4b75</td>
<td>chore(repo): add gitignore, readme and docker compose</td>
<td>Task: T-SH3.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/shared-skeleton</td>
<td>ecd53b5</td>
<td>feat(shared): add business rules and contracts between contexts</td>
<td>Task: T-SH3.2</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/shared-skeleton</td>
<td>ed4482a</td>
<td>feat(shared): add database context, tenant filter, errors, json names and security</td>
<td>Task: T-SH3.2</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/shared-skeleton</td>
<td>01db8e1</td>
<td>chore(api): add project file, entry point, settings and module stubs</td>
<td>Task: T-SH3.1, T-SH3.2</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/shared-skeleton</td>
<td>61a22c9</td>
<td>chore(repo): add solution file</td>
<td>Task: T-SH3.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/data-16-tables</td>
<td>4ed3bb7</td>
<td>feat(iam): add business, user and password reset persistence</td>
<td>Task: T-TS04.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/data-16-tables</td>
<td>5b88ff3</td>
<td>feat(data): add catalog and iot tables</td>
<td>Task: T-TS13.1, T-TS01.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/data-16-tables</td>
<td>cec1a47</td>
<td>feat(data): add stock, sales and procurement tables</td>
<td>Task: T-TS14.1, T-TS07.1, T-TS10.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/data-16-tables</td>
<td>b3115e4</td>
<td>feat(data): add alerts and restocking tables</td>
<td>Task: T-TS03.1</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/data-16-tables</td>
<td>2f2e369</td>
<td>feat(shared): add cross-context foreign keys</td>
<td>Task: T-SH3.4</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/db-migration</td>
<td>52b9c34</td>
<td>feat(db): add initial migration, schema script and database diagram</td>
<td>Task: T-TS13.4</td>
<td>03/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/iam-auth</td>
<td>ba89296</td>
<td>refactor(shared): open endpoints with a fixed business and apply migrations</td>
<td>Task: T-SH3.2</td>
<td>04/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/iam-auth</td>
<td>9f520ac</td>
<td>feat(iam): register iam module without authentication</td>
<td>Task: T-TS04.1</td>
<td>04/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/sales-register</td>
<td>fd4d070</td>
<td>feat(sales): register sales with stock rules and movements</td>
<td>Task: T-TS07.2, T-TS08.1</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/sales-register</td>
<td>cc1eb2f</td>
<td>feat(sales): add sales controller with history and detail</td>
<td>Task: T-TS08.1</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/sales-register</td>
<td>a3ee520</td>
<td>fix(sales): skip the demo sale until the demo products exist</td>
<td>Task: T-TS07.1</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/iot-sensors</td>
<td>f0a2483</td>
<td>feat(iot): add reading reception, status and sensor linking services</td>
<td>Task: T-TS01.2, T-TS05.1, T-US04.3</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/iot-sensors</td>
<td>bf83ce6</td>
<td>feat(iot): add sensors controller with openapi documentation</td>
<td>Task: T-TS05.1</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/analytics-dashboard</td>
<td>bd2c4d1</td>
<td>feat(analytics): add dashboard and reports queries</td>
<td>Task: T-US15.3, T-US25.3</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/analytics-dashboard</td>
<td>fd34d7c</td>
<td>feat(analytics): add analytics controller</td>
<td>Task: T-US25.3</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/tools-local-ci</td>
<td>f0d7cee</td>
<td>feat(tools): add iot sensor simulator</td>
<td>Task: T-SH3.8</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/tools-local-ci</td>
<td>b95708e</td>
<td>ci(actions): build and test on every push and pull request</td>
<td>Task: T-SH3.3</td>
<td>05/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/catalog-products</td>
<td>4548995</td>
<td>feat(catalog): add product services with validation rules</td>
<td>Task: T-TS13.2</td>
<td>06/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/catalog-products</td>
<td>0537c1c</td>
<td>feat(catalog): add products controller and threshold endpoint</td>
<td>Task: T-TS13.3</td>
<td>06/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/procurement-suppliers-purchases</td>
<td>7c90966</td>
<td>feat(procurement): add supplier, purchase and reception services</td>
<td>Task: T-TS09.1, T-TS10.2, T-TS11.1</td>
<td>06/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/procurement-suppliers-purchases</td>
<td>4337dca</td>
<td>feat(procurement): add suppliers and purchases controllers</td>
<td>Task: T-TS12.1</td>
<td>06/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/alerts-rules</td>
<td>a160c91</td>
<td>feat(alerts): add alert rules and list endpoints</td>
<td>Task: T-TS03.2, T-TS03.6, T-TS03.3</td>
<td>07/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/alerts-rules</td>
<td>827c7f1</td>
<td>test(alerts): add wave 1 http requests</td>
<td>Task: T-TS03.6, T-TS03.3</td>
<td>07/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/stock-movements</td>
<td>3b6222d</td>
<td>feat(stock): add movement engine, stock query and comparison</td>
<td>Task: T-TS14.2, T-TS02.1, T-TS02.2, T-TS06.1</td>
<td>08/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/stock-movements</td>
<td>d69d951</td>
<td>feat(stock): add stock controller with movements endpoint</td>
<td>Task: T-TS15.1</td>
<td>08/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/unit-tests</td>
<td>40274fb</td>
<td>test(rules): add unit tests for the business rules</td>
<td>Task: T-SH3.7</td>
<td>08/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>feature/external-services</td>
<td>fcf8c55</td>
<td>feat(alerts): add notification endpoints and SMTP Twilio services</td>
<td>Task: T-TS03.4, T-TS03.5</td>
<td>09/11/2026</td>
</tr>
<tr>
<td>smartstock-backend</td>
<td>hotfix/twilio-content-template</td>
<td>1aa8eb4</td>
<td>fix(alerts): send WhatsApp messages with a Twilio ContentSid</td>
<td>Task: T-TS03.5</td>
<td>10/11/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-videos</td>
<td>02611c5</td>
<td>feat(landing): add product and team video section</td>
<td>—</td>
<td>09/11/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-videos</td>
<td>2e5a1a3</td>
<td>feat(landing): add bilingual video translations</td>
<td>—</td>
<td>09/11/2026</td>
</tr>
<tr>
<td>smartstock-landing-page</td>
<td>feature/landing-videos</td>
<td>fbfbe4c</td>
<td>fix(landing): correct youtube embed URLs</td>
<td>—</td>
<td>09/11/2026</td>
</tr>
<tr>
<td>smartstock-frontend</td>
<td>feature/real-api</td>
<td>b6625de</td>
<td>feat(frontend): connect real API and add temporary demo access</td>
<td>Task: T-SH3.6</td>
<td>11/11/2026</td>
</tr>
</tbody>
</table>

Nota. Los 34 commits de smartstock-backend coinciden con la actividad

del repositorio mostrada en la figura 240 (sin contar merges). Los 3
commits de smartstock-landing-page pertenecen a otro repositorio.
Elaboración propia.

#### 5.2.3.5.Execution Evidence for Sprint Review

En este sprint la Frontend Web Application (v1.1.0) quedó conectada a
los Web Services reales: las vistas de IoT Device, Alerts & Restocking,
Product Catalog, Inventory Monitoring (incluidas ventas, compras y
proveedores) y Analytics & Reporting funcionan con datos persistentes en
MySQL en lugar de la Fake API, sin cambios en la interfaz (solo cambió
la variable VITE_API_BASE_URL). La autenticación real (login y JWT) está
planificada para el Sprint 4; en esta entrega los endpoints son
abiertos, la aplicación opera con un negocio fijo y el frontend usa un
acceso de demostración. Cada captura se rotula con la historia que
cubre. El video que muestra la visualización y la navegación logradas en
el sprint está en
upc-pre-202620-1asi0730-8168-inventiastock-product-navigation-sprint-3.mp4

Link en Microsoft Stream:
<a href="https://upcedupe-my.sharepoint.com/%3Av%3A/g/personal/u20241f946_upc_edu_pe/IQBdzCqqjN2bRZw1igPd50NKAcr_uPD4Xa5YEMWKscZGjGA?e=OLh1PM&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" style="color:#2563eb">https://upcedupe-my.sharepoint.com/&#58;v&#58;/g/personal/u20241f946_upc_edu_pe/IQBdzCqqjN2bRZw1igPd50NKAcr_uPD4Xa5YEMWKscZGjGA?e=OLh1PM&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D</a>

**Tabla 50**

*Evidencia de ejecución por contexto e historia de usuario del Sprint 3*

<table style="font-size:10pt;">
<tbody>
<tr>
<th>Contexto</th>
<th>Historia</th>
<th>Ruta</th>
<th>La captura debe mostrar</th>
<th>Figura</th>
</tr>
<tr>
<td>Ventas</td>
<td>US26, US27 y US28</td>
<td>/sales, /sales/new, /sales/:id</td>
<td>Venta registrada, rechazo por stock insuficiente, historial por fechas y detalle</td>
<td>185</td>
</tr>
<tr>
<td>IoT Device</td>
<td>US04 Vinculación de sensor</td>
<td>/sensors/link</td>
<td>Selección de sensor y producto, y error de sensor en uso</td>
<td>186</td>
</tr>
<tr>
<td>IoT Device</td>
<td>US06 y US07 Estado y peso actual</td>
<td>/sensors</td>
<td>Sensores en línea y desconectados, y peso con su equivalente en unidades</td>
<td>187</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>US09 y US10 Notificaciones</td>
<td>/settings</td>
<td>Canales de correo y WhatsApp configurados</td>
<td>188</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>US12 y US32 Alertas y compra desde alerta</td>
<td>/alerts</td>
<td>Alerta de stock bajo o discrepancia y el botón que abre el registro de compra</td>
<td>189</td>
</tr>
<tr>
<td>Product Catalog</td>
<td>US13, US14 y US05 Productos</td>
<td>/products</td>
<td>Registro, edición y umbral mínimo con su error de validación</td>
<td>190</td>
</tr>
<tr>
<td>Proveedores y Compras</td>
<td>US29, US30 y US31</td>
<td>/purchases, /purchases/new, /purchases/suppliers</td>
<td>Proveedor creado, compra pendiente, compra recibida e historial por fechas</td>
<td>191</td>
</tr>
<tr>
<td>Inventory Monitoring</td>
<td>US08 y US11</td>
<td>/products, /comparison</td>
<td>Niveles de stock y comparación físico vs. registrado (solo minimarket)</td>
<td>192</td>
</tr>
<tr>
<td>Analytics & Reporting</td>
<td>US15 y US25</td>
<td>/dashboard, /reports</td>
<td>Tarjetas del día con ventas y compras, y reporte por periodo</td>
<td>193</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Figura 241**

**Pantalla de Ventas: registro, historial y detalle de ventas (US26,**

US27, US28)  
<img src="../assets/chapter-5/figura_241.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 242**

*Vinculación de sensor a un producto y error de sensor en uso (US04)*

<img src="../assets/chapter-5/figura_242.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 243**

*Estado de conexión de sensores en línea y desconectados, y peso actual*

(US06, US07)  
<img src="../assets/chapter-5/figura_243.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 244**

*Configuración de notificaciones por correo y WhatsApp (US09, US10)*

<img src="../assets/chapter-5/figura_244.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 245**

*Alertas activas y botón de compra desde una alerta de stock bajo (US12,*

US32)  
<img src="../assets/chapter-5/figura_245.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 246**

*Catálogo: lista de productos con su nivel de stock (US13)*

<img src="../assets/chapter-5/figura_246.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 247**

*Proveedores y compras: (a) proveedor creado, (b) formulario de nueva*

compra, (c) compra recibida y (d)
historia<img src="../assets/chapter-5/figura_247.png" style="max-height:6.6cm">l por fechas con una compra
pendiente (US29, US30, US31)  

Nota. Elaboración propia

**Figura 248**

*Prueba T-QA3.3-4: lectura de 2.0 kg en el sensor 2, estado online y*

discrepancia del -50 % (R20) en Scalar y en la Web App, 12/11/2026
<img src="../assets/chapter-5/figura_248.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 249**

*Dashboard con ventas y compras del día, y reporte por período (US15,*

US25)  
<img src="../assets/chapter-5/figura_249.png" style="max-height:6.6cm">

Nota. Elaboración propia

#### 5.2.3.6.Services Documentation Evidence for Sprint Review

En el Sprint 3 el equipo implementó y documentó con OpenAPI las 30
operaciones de los Web Services de SmartStock, que se visualizan
mediante Scalar. Por indicación del docente, los endpoints van abiertos
con un negocio fijo (id 1); el inicio de sesión y el token JWT se
incorporan en el Sprint 4. Los errores se devuelven con un código (code)
y un mensaje en inglés o en español, según el encabezado
Accept-Language, sin mostrar el stack trace.

- Repositorio de Web Services: <a href="https://github.com/InventiaStock/smartstock-backend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-backend</a>
- Documentación desplegada (Scalar): <a href="https://smartstock-backend-kj6m.onrender.com/scalar/v1" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com/scalar/v1</a>
- Documentación local (referencia): <a href="http://localhost:5000/scalar" style="color:#2563eb">http://localhost:5000/scalar</a>
- Contrato OpenAPI (JSON, 30 endpoints): <a href="https://smartstock-backend-kj6m.onrender.com/openapi/v1.json" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com/openapi/v1.json</a>
- Commits de documentación: ver tabla 49 (sección 5.2.3.4)

**Tabla 51**

*Documentación de los endpoints de los Web Services del Sprint 3*

<table style="font-size:8pt; word-break:break-word; table-layout:fixed; width:100%;">
<tbody>
<tr>
<th>Endpoint</th>
<th>Método</th>
<th>Acción</th>
<th>Parámetros</th>
<th>Ejemplo de request</th>
<th>Response y explicación</th>
<th>Historia</th>
</tr>
<tr>
<td>/api/ventas</td>
<td>POST</td>
<td>Registra una venta. Valida los ítems y crea un movimiento de stock de salida (OUT) por cada ítem; el stock solo cambia por ese movimiento.</td>
<td>Cuerpo JSON: items (lista obligatoria). Cada ítem: productoId (entero), cantidad (entero mayor que 0) y precioUnitario (número mayor que 0). Sin parámetros de ruta ni de consulta.</td>
<td>{ "items": [ { "productoId": 1, "cantidad": 1, "precioUnitario": 8.2 } ] }</td>
<td>201 Created: { "id": "R-00042" }, el código correlativo de la venta. 400 NO_ITEMS si no hay ítems o INVALID_QUANTITY si la cantidad no es válida. 404 PRODUCT_NOT_FOUND si el producto no existe. 422 NO_SALE_PRICE si el producto no tiene precio de venta (R14) o INSUFFICIENT_STOCK si la cantidad supera el stock registrado (R13). Si hay un error no se cambia nada.</td>
<td>TS07</td>
</tr>
<tr>
<td>/api/ventas</td>
<td>GET</td>
<td>Lista las ventas de un periodo y calcula el total acumulado de las ventas completadas.</td>
<td>Consulta opcional: desde y hasta, con formato yyyy-MM-dd. Sin filtros devuelve todas las ventas.</td>
<td>GET /api/ventas?desde=2026-11-01&hasta=2026-11-30</td>
<td>200 OK: { "ventas": [ { "id": "R-00042", "fecha": "2026-11-09", "estado": "COMPLETED", "total": 8.20, "items": [ { "productoId": 1, "cantidad": 1, "precioUnitario": 8.20, "productoNombre": "Rice 1 kg", "subtotal": 8.20 } ] } ], "total": 60.30 }. El ejemplo muestra una venta; la lista incluye también R-00041 (52.10). total suma solo las ventas completadas. Sin ventas devuelve { "ventas": [], "total": 0 }.</td>
<td>TS08</td>
</tr>
<tr>
<td>/api/ventas/{code}</td>
<td>GET</td>
<td>Consulta el detalle de una venta con sus ítems y los movimientos de stock que generó.</td>
<td>Ruta: code, el código de la venta, por ejemplo R-00042.</td>
<td>GET /api/ventas/R-00042</td>
<td>200 OK: { "id": "R-00042", "fecha": "2026-11-09", "estado": "COMPLETED", "total": 8.20, "items": [ { "productoId": 1, "cantidad": 1, "precioUnitario": 8.20, "productoNombre": "Rice 1 kg", "subtotal": 8.20 } ], "movimientos": [ { "id": 4, "productoId": 1, "tipo": "OUT", "origen": "SALE", "origenId": "R-00042", "cantidad": 1, "fecha": "2026-11-09", "productoNombre": "Rice 1 kg" } ] }. 404 NOT_FOUND si el código no existe, por ejemplo R-99999.</td>
<td>TS08</td>
</tr>
<tr>
<td>/api/productos</td>
<td>GET</td>
<td>Lista los productos del negocio con el estado de su sensor y su stock de referencia.</td>
<td>Consulta opcional: sensorId (entero) para filtrar por el sensor vinculado.</td>
<td>GET /api/productos?sensorId=1</td>
<td>200 OK: lista de productos, cada uno con id, nombre, sku, categoria, pesoUnitario, precioVenta, costoCompra, proveedorHabitual, stockRegistrado, umbralMinimo, capacidadMaxima, sensorId, estadoSensor, unidadesSensor, stockReferencia y nivelStock. Sin productos devuelve [].</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/productos/{id}</td>
<td>GET</td>
<td>Consulta un producto por su identificador.</td>
<td>Ruta: id, identificador del producto (entero).</td>
<td>GET /api/productos/1</td>
<td>200 OK: el producto, con los mismos campos que la lista (id, nombre, sku, categoria, precioVenta, stockRegistrado, umbralMinimo, estadoSensor, nivelStock, etc.). 404 NOT_FOUND si el producto no existe.</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/productos</td>
<td>POST</td>
<td>Registra un producto. El stock inicial se registra mediante un movimiento de stock (R17).</td>
<td>Cuerpo JSON: nombre, sku, categoria, pesoUnitario, precioVenta, costoCompra, proveedorHabitual, umbralMinimo, capacidadMaxima y, opcionalmente, stockRegistrado (stock inicial).</td>
<td>{ "nombre": "Lentils 500 g", "sku": "LENT-500G", "categoria": "Grocery", "pesoUnitario": 0.5, "precioVenta": 6.5, "costoCompra": 4.9, "proveedorHabitual": "Fresh Foods Co.", "umbralMinimo": 5, "capacidadMaxima": 60 }</td>
<td>201 Created: el producto creado, con su id y los campos de la lista de productos. 400 INVALID_PRODUCT con el detalle de los campos inválidos (por ejemplo nombre vacío, peso unitario 0 o umbral mayor que la capacidad máxima).</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/productos/{id}</td>
<td>PUT</td>
<td>Edita los datos de un producto sin modificar su stock registrado (R17).</td>
<td>Ruta: id del producto. Cuerpo JSON con los campos a cambiar (por ejemplo precioVenta y costoCompra).</td>
<td>PUT /api/productos/1 con { "precioVenta": 8.5, "costoCompra": 6.8 }</td>
<td>200 OK: el producto actualizado. 400 INVALID_PRODUCT si algún dato no es válido. 404 NOT_FOUND si el producto no existe.</td>
<td>TS13</td>
</tr>
<tr>
<td>/api/sensores/{id}/umbral</td>
<td>PUT</td>
<td>Cambia el umbral mínimo del producto vinculado a un sensor.</td>
<td>Ruta: id del sensor. Cuerpo JSON: umbralMinimo (entero).</td>
<td>PUT /api/sensores/1/umbral con { "umbralMinimo": 6 }</td>
<td>200 OK: el producto con el nuevo umbralMinimo. 404 NOT_FOUND si el sensor no existe. 422 THRESHOLD_INVALID si el umbral no es válido o THRESHOLD_EXCEEDS_CAPACITY si supera la capacidad máxima del producto.</td>
<td>US05</td>
</tr>
<tr>
<td>/api/proveedores</td>
<td>POST</td>
<td>Registra un proveedor.</td>
<td>Cuerpo JSON: nombre y telefono (obligatorios) y correo (opcional).</td>
<td>{ "nombre": "Distribuidora Sol", "telefono": "987654321", "correo": "ventas@sol.pe" }</td>
<td>201 Created: el proveedor creado, con su id numérico asignado por el sistema, nombre, correo y telefono. 400 INCOMPLETE si falta el nombre o el teléfono. 409 DUPLICATE_SUPPLIER si ya existe un proveedor con el mismo nombre y teléfono (R8).</td>
<td>TS09</td>
</tr>
<tr>
<td>/api/proveedores</td>
<td>GET</td>
<td>Lista los proveedores del negocio.</td>
<td>No usa parámetros.</td>
<td>GET /api/proveedores</td>
<td>200 OK: lista de proveedores, cada uno con id, nombre, correo y telefono. Sin proveedores devuelve [].</td>
<td>TS09</td>
</tr>
<tr>
<td>/api/compras</td>
<td>POST</td>
<td>Registra una compra a un proveedor. La compra nace en estado PENDING y no modifica el stock (R15); puede originarse en una alerta de stock bajo (R21).</td>
<td>Cuerpo JSON: proveedorId, items (lista con productoId, cantidad y costoUnitario), y opcionalmente restockingNeedId (necesidad de reposición de la alerta) y fecha.</td>
<td>{ "proveedorId": 1, "items": [ { "productoId": 1, "cantidad": 24, "costoUnitario": 2.5 } ] }</td>
<td>201 Created: { "id": "PO-00032" }, el código correlativo de la compra. 400 si faltan datos o hay una cantidad inválida. 404 SUPPLIER_NOT_FOUND si el proveedor no existe.</td>
<td>TS10</td>
</tr>
<tr>
<td>/api/compras/{code}/recepcion</td>
<td>PATCH</td>
<td>Recibe una compra: suma las cantidades al stock mediante movimientos de entrada (IN) y cierra la reposición asociada (R16, R21).</td>
<td>Ruta: code, código de la compra, por ejemplo PO-00031. Sin cuerpo.</td>
<td>PATCH /api/compras/PO-00031/recepcion</td>
<td>200 OK: la compra con estado RECEIVED, sus ítems y su total. 404 NOT_FOUND si el código no existe. 409 ALREADY_RECEIVED si la compra ya fue recibida, para no recibirla dos veces.</td>
<td>TS11</td>
</tr>
<tr>
<td>/api/compras</td>
<td>GET</td>
<td>Lista las compras de un periodo y calcula el total acumulado.</td>
<td>Consulta opcional: desde y hasta, con formato yyyy-MM-dd.</td>
<td>GET /api/compras?desde=2026-11-01&hasta=2026-11-30</td>
<td>200 OK: objeto con producto (los datos del producto), sensor (id, codigo, estado, pesoKg, unidades y ultimaLecturaAt) y lecturas (las últimas 5). Ejemplo de lectura: { "id": 9, "sensorId": 3, "pesoKg": 12.360, "fecha": "2026-11-09T20:11:37.871Z", "unidades": 12 }. 404 NOT_FOUND si el producto no existe.</td>
<td>TS12</td>
</tr>
<tr>
<td>/api/compras/{code}</td>
<td>GET</td>
<td>Consulta el detalle de una compra con sus ítems y los movimientos de stock que generó.</td>
<td>Ruta: code, código de la compra, por ejemplo PO-00031.</td>
<td>GET /api/compras/PO-00031</td>
<td>200 OK: la compra con id, proveedorId, proveedorNombre, fecha, estado, total, restockingNeedId, items y movimientos. 404 NOT_FOUND si el código no existe.</td>
<td>TS12</td>
</tr>
<tr>
<td>/api/productos/{id}/stock</td>
<td>GET</td>
<td>Consulta el nivel de stock de un producto: stock registrado, stock de referencia (físico si el sensor está en línea) y nivel.</td>
<td>Ruta: id del producto.</td>
<td>GET /api/productos/1/stock</td>
<td>200 OK: { "productoId": 1, "stockRegistrado": 2, "stockReferencia": 2, "nivelStock": "lowStock", "estadoSensor": "disconnected", "unidadesSensor": null }. nivelStock es lowStock o healthy. 404 NOT_FOUND si el producto no existe.</td>
<td>TS02</td>
</tr>
<tr>
<td>/api/movimientos-stock</td>
<td>GET</td>
<td>Lista los movimientos de stock de un periodo.</td>
<td>Consulta opcional: desde y hasta, con formato yyyy-MM-dd.</td>
<td>GET /api/movimientos-stock?desde=2026-11-01&hasta=2026-11-30</td>
<td>200 OK: lista de movimientos, por ejemplo { "id": 4, "productoId": 1, "tipo": "OUT", "origen": "SALE", "origenId": "R-00042", "cantidad": 1, "fecha": "2026-11-09", "productoNombre": "Rice 1 kg" }. Un periodo sin movimientos devuelve [] con 200.</td>
<td>TS15</td>
</tr>
<tr>
<td>/api/productos/{id}/detalle</td>
<td>GET</td>
<td>Consulta un producto con su sensor y sus últimas 5 lecturas.</td>
<td>Ruta: id del producto.</td>
<td>GET /api/productos/3/detalle</td>
<td>200 OK: el producto con id, nombre, sku, categoria, pesoUnitario, precioVenta, costoCompra, proveedorHabitual, stockRegistrado, umbralMinimo, capacidadMaxima, sensorId, estadoSensor, unidadesSensor, stockReferencia y nivelStock. 404 NOT_FOUND si el producto no existe.</td>
<td>TS02</td>
</tr>
<tr>
<td>/api/inventario/comparacion</td>
<td>GET</td>
<td>Compara el stock físico (sensor) con el stock registrado de todos los productos.</td>
<td>No usa parámetros.</td>
<td>GET /api/inventario/comparacion</td>
<td>200 OK: { "items": [ { "productoId": 3, "productoNombre": "Milk 1 L", "stockRegistrado": 14, "pesoKg": 12.360, "unidadesFisicas": 12, "diferenciaPct": -14.3, "resultado": "DISCREPANCY" } ], "discrepancias": 1, "alertaId": 1 }. items trae un elemento por producto. resultado es MATCH, DISCREPANCY (diferencia mayor a 10 %, R20) o REGISTERED_ONLY (sin sensor en línea).</td>
<td>TS06</td>
</tr>
<tr>
<td>/api/inventario/comparacion/{productoId}</td>
<td>GET</td>
<td>Compara el stock físico con el registrado de un producto.</td>
<td>Ruta: productoId, identificador del producto.</td>
<td>GET /api/inventario/comparacion/3</td>
<td>200 OK: { "productoId": 3, "productoNombre": "Milk 1 L", "stockRegistrado": 14, "pesoKg": 12.360, "unidadesFisicas": 12, "diferenciaPct": -14.3, "resultado": "DISCREPANCY" }. 404 NOT_FOUND si el producto no existe. 409 NO_REGISTERED_QUANTITY si el producto no tiene cantidad registrada.</td>
<td>TS06</td>
</tr>
<tr>
<td>/api/sensores</td>
<td>GET</td>
<td>Lista los sensores con su estado de conexión.</td>
<td>No usa parámetros.</td>
<td>GET /api/sensores</td>
<td>200 OK: lista de sensores, cada uno con id, codigo, productoId, pesoKg, ultimaLecturaAt, pesoReferenciaKg, estado, productoNombre y unidades. estado es online (última lectura de hace 5 minutos o menos, R11), disconnected o available (sin producto).</td>
<td>US06</td>
</tr>
<tr>
<td>/api/sensores/{id}/lecturas</td>
<td>POST</td>
<td>Recibe una lectura de peso enviada por el microcontrolador. Es un endpoint público para los dispositivos.</td>
<td>Ruta: id del sensor. Cuerpo JSON: peso (kg, mayor o igual que 0) y opcionalmente fecha. Cabecera X-Device-Key solo si el servidor la tiene configurada.</td>
<td>{ "peso": 2.0 }</td>
<td>201 Created: { "id": 8 }, el identificador de la lectura. 400 INVALID_WEIGHT si el peso es negativo. 404 SENSOR_NOT_FOUND si el sensor no existe. 401 UNAUTHORIZED si falta la clave del dispositivo cuando está configurada. Una lectura con más de 10 % de diferencia respecto al stock registrado crea una alerta de discrepancia (R20).</td>
<td>TS01</td>
</tr>
<tr>
<td>/api/sensores/{id}</td>
<td>GET</td>
<td>Consulta un sensor con su estado.</td>
<td>Ruta: id del sensor.</td>
<td>GET /api/sensores/1</td>
<td>200 OK: el sensor con id, codigo, productoId, pesoKg, ultimaLecturaAt, pesoReferenciaKg, estado, productoNombre y unidades. 404 NOT_FOUND si el sensor no existe.</td>
<td>US06</td>
</tr>
<tr>
<td>/api/sensores/{id}/estado</td>
<td>GET</td>
<td>Consulta el estado de conexión de un sensor (en línea si su última lectura tiene 5 minutos o menos, R11).</td>
<td>Ruta: id del sensor.</td>
<td>GET /api/sensores/1/estado</td>
<td>200 OK: objeto con estado (online si la última lectura tiene 5 minutos o menos, R11; si no, disconnected), ultimaLecturaAt (fecha y hora de la última lectura) y pesoKg (último peso recibido). 404 NOT_FOUND si el sensor no existe.</td>
<td>TS05</td>
</tr>
<tr>
<td>/api/sensores/vincular</td>
<td>POST</td>
<td>Vincula un sensor libre con un producto (un sensor por producto, R9).</td>
<td>Cuerpo JSON: sensorId y productoId (enteros).</td>
<td>{ "sensorId": 4, "productoId": 4 }</td>
<td>200 OK: el sensor vinculado, con su productoId y productoNombre. 404 NOT_FOUND si el sensor o el producto no existe. 409 SENSOR_IN_USE si el sensor ya tiene un producto o PRODUCT_HAS_SENSOR si el producto ya tiene un sensor.</td>
<td>US04</td>
</tr>
<tr>
<td>/api/dashboard</td>
<td>GET</td>
<td>Obtiene el resumen del día: ventas y compras de hoy, alertas de stock bajo activas, las 5 operaciones recientes y el nivel de stock de cada producto.</td>
<td>No usa parámetros.</td>
<td>GET /api/dashboard</td>
<td>200 OK: objeto con ventasHoy y comprasHoy (cada uno con total y cantidad), alertasStockBajo (número de alertas activas), actividadReciente (las 5 operaciones más recientes, cada una con tipo, id, total y fecha) y resumenStock (por producto: productoId, nombre, unidades, nivel y sensor).</td>
<td>US15</td>
</tr>
<tr>
<td>/api/reportes</td>
<td>GET</td>
<td>Obtiene el reporte de un periodo: totales de ventas y compras, movimientos de stock y compras pendientes.</td>
<td>Consulta opcional: desde y hasta, con formato yyyy-MM-dd.</td>
<td>GET /api/reportes?desde=2026-11-01&hasta=2026-11-30</td>
<td>200 OK: objeto con desde y hasta (el periodo), ventasTotal, comprasTotal, movimientos (los movimientos de stock del periodo) y comprasPendientes (códigos de las compras PENDING). Una compra PENDING no genera movimiento de entrada.</td>
<td>US25</td>
</tr>
<tr>
<td>/api/alertas</td>
<td>GET</td>
<td>Lista las alertas activas y las resueltas en las últimas 24 horas.</td>
<td>No usa parámetros.</td>
<td>GET /api/alertas</td>
<td>200 OK: lista de alertas con id, tipo (LOW_STOCK por R19 o DISCREPANCY por R20), productoId, productoNombre, stockReferencia, fuente (sensor o registered), estado, creadaEn, resueltaEn, necesidadId (para comprar desde la alerta, R21), umbralMinimo y stockActual. Las de discrepancia añaden stockRegistrado, stockFisico y diferenciaPct.</td>
<td>US09</td>
</tr>
<tr>
<td>/api/canales-notificacion</td>
<td>GET</td>
<td>Lista los canales de notificación del negocio (correo y WhatsApp).</td>
<td>No usa parámetros.</td>
<td>GET /api/canales-notificacion</td>
<td>200 OK: lista de canales; cada uno con id, canal (email o whatsapp), destino (correo o número configurado) y activo (true o false). La primera vez se crean los dos canales.</td>
<td>US10</td>
</tr>
<tr>
<td>/api/canales-notificacion</td>
<td>PUT</td>
<td>Activa o desactiva los canales de notificación.</td>
<td>Cuerpo JSON: lista de cambios con id y activo (booleano).</td>
<td>[ { "id": 2, "activo": false } ]</td>
<td>200 OK: la lista de canales actualizada. 422 AT_LEAST_ONE_CHANNEL si el cambio dejaría todos los canales inactivos.</td>
<td>US10</td>
</tr>
<tr>
<td>/api/notificaciones/stock-bajo</td>
<td>POST</td>
<td>Envía la notificación de la alerta activa de un producto por todos los canales activos (correo y WhatsApp).</td>
<td>Cuerpo JSON: productoId (entero).</td>
<td>{ "productoId": 1 }</td>
<td>202 Accepted: { "sent": true, "at": fecha y hora del envío }. 404 ALERT_NOT_FOUND si el producto no tiene una alerta activa. Si un canal falla, el error se guarda en las notificaciones enviadas y la operación no se rompe.</td>
<td>TS03</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 52**

*Relación de endpoints*

<table>
<tbody>
<tr>
<th>Contexto</th>
<th>Recurso</th>
<th>Acciones</th>
<th>Historia</th>
</tr>
<tr>
<td>Inventory Monitoring – Ventas</td>
<td>/api/ventas, /api/ventas/{code}</td>
<td>POST, GET</td>
<td>TS07, TS08</td>
</tr>
<tr>
<td>Product Catalog</td>
<td>/api/productos, /api/productos/{id}</td>
<td>GET, POST, PUT</td>
<td>TS13</td>
</tr>
<tr>
<td>Product Catalog</td>
<td>/api/sensores/{id}/umbral</td>
<td>PUT</td>
<td>US05</td>
</tr>
<tr>
<td>Inventory Monitoring – Proveedores</td>
<td>/api/proveedores</td>
<td>GET, POST</td>
<td>TS09</td>
</tr>
<tr>
<td>Inventory Monitoring – Compras</td>
<td>/api/compras, /api/compras/{code}</td>
<td>POST, GET</td>
<td>TS10, TS12</td>
</tr>
<tr>
<td>Inventory Monitoring – Compras</td>
<td>/api/compras/{code}/recepcion</td>
<td>PATCH</td>
<td>TS11</td>
</tr>
<tr>
<td>Inventory Monitoring – Stock</td>
<td>/api/productos/{id}/stock, /api/productos/{id}/detalle</td>
<td>GET</td>
<td>TS02</td>
</tr>
<tr>
<td>Inventory Monitoring – Movimientos</td>
<td>/api/movimientos-stock</td>
<td>GET</td>
<td>TS15</td>
</tr>
<tr>
<td>Inventory Monitoring – Comparación</td>
<td>/api/inventario/comparacion, /api/inventario/comparacion/{productoId}</td>
<td>GET</td>
<td>TS06</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores, /api/sensores/{id}</td>
<td>GET</td>
<td>US06</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores/{id}/lecturas</td>
<td>POST</td>
<td>TS01</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores/{id}/estado</td>
<td>GET</td>
<td>TS05</td>
</tr>
<tr>
<td>IoT Device</td>
<td>/api/sensores/vincular</td>
<td>POST</td>
<td>US04</td>
</tr>
<tr>
<td>Analytics & Reporting</td>
<td>/api/dashboard, /api/reportes</td>
<td>GET</td>
<td>US15, US25</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>/api/alertas</td>
<td>GET</td>
<td>US09</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>/api/canales-notificacion</td>
<td>GET, PUT</td>
<td>US10</td>
</tr>
<tr>
<td>Alerts & Restocking</td>
<td>/api/notificaciones/stock-bajo</td>
<td>POST</td>
<td>TS03</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Figura 250**

*POST /api/ventas en Scalar (TS07)*

<img src="../assets/chapter-5/figura_250.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 251**

*GET /api/ventas en Scalar (TS08)*

<img src="../assets/chapter-5/figura_251.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 252**

*GET /api/ventas/{code} en Scalar (TS08)*

<img src="../assets/chapter-5/figura_252.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 253**

*GET /api/productos en Scalar (TS13)*

<img src="../assets/chapter-5/figura_253.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 254**

*GET /api/productos/{id} en Scalar (TS13)*

<img src="../assets/chapter-5/figura_254.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 255**

*POST /api/productos en Scalar (TS13)*

<img src="../assets/chapter-5/figura_255.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 256**

*PUT /api/productos/{id} en Scalar (TS13)*

<img src="../assets/chapter-5/figura_256.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 257**

*PUT /api/sensores/{id}/umbral en Scalar (US05)*

<img src="../assets/chapter-5/figura_257.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 258**

*POST /api/proveedores en Scalar (TS09)*

<img src="../assets/chapter-5/figura_258.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 259**

*GET /api/proveedores en Scalar (TS09)*

<img src="../assets/chapter-5/figura_259.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 260**

*POST /api/compras en Scalar (TS10)*

<img src="../assets/chapter-5/figura_260.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 261**

*PATCH /api/compras/{code}/recepcion en Scalar (TS11)*

<img src="../assets/chapter-5/figura_261.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 262**

*GET /api/compras en Scalar (TS12)*

<img src="../assets/chapter-5/figura_262.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 263**

*GET /api/compras/{code} en Scalar (TS12)*

<img src="../assets/chapter-5/figura_263.png" style="max-height:6.6cm">  

Nota. Elaboración propia

**Figura 264**

*GET /api/productos/{id}/stock en Scalar (TS02)*

<img src="../assets/chapter-5/figura_264.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 265**

*GET /api/movimientos-stock en Scalar (TS15)*

<img src="../assets/chapter-5/figura_265.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 266**

*GET /api/productos/{id}/detalle en Scalar (TS02)*

<img src="../assets/chapter-5/figura_266.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 267**

*GET /api/inventario/comparacion en Scalar (TS06)*

<img src="../assets/chapter-5/figura_267.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 268**

*GET /api/inventario/comparacion/{productoId} en Scalar (TS06)*

<img src="../assets/chapter-5/figura_268.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 269**

*GET /api/sensores en Scalar (US06)*

<img src="../assets/chapter-5/figura_269.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 270**

*POST /api/sensores/{id}/lecturas en Scalar (TS01)*

<img src="../assets/chapter-5/figura_270.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 271**

*GET /api/sensores/{id} en Scalar (US06)*

<img src="../assets/chapter-5/figura_271.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 272**

*GET /api/sensores/{id}/estado en Scalar (TS05)*

<img src="../assets/chapter-5/figura_272.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 273**

*POST /api/sensores/vincular en Scalar (US04)*

<img src="../assets/chapter-5/figura_273.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 274**

*GET /api/dashboard en Scalar (US15)*

<img src="../assets/chapter-5/figura_274.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 275**

*GET /api/reportes en Scalar (US25)*

<img src="../assets/chapter-5/figura_275.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 276**

*GET /api/alertas en Scalar (US09)*

<img src="../assets/chapter-5/figura_276.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 277**

*GET /api/canales-notificacion en Scalar (US10)*

<img src="../assets/chapter-5/figura_277.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 278**

*PUT /api/canales-notificacion en Scalar (US10)*

<img src="../assets/chapter-5/figura_278.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 279**

*POST /api/notificaciones/stock-bajo en Scalar (TS03)*

<img src="../assets/chapter-5/figura_279.png" style="max-height:6.6cm">

Nota. Elaboración propia

#### 5.2.3.7.Software Deployment Evidence for Sprint Review

Durante el Sprint 3 el alcance de despliegue incluyó los Web Services,
la base de datos y la nueva versión de la Frontend Web Application. Los
Web Services se empaquetaron con Docker y se desplegaron en Render; la
base de datos MySQL se alojó en Aiven y sus tablas se crearon por
comando mediante las migraciones de Entity Framework Core (dotnet ef
database update). La Frontend Web Application y el Landing Page
continúan publicados en GitHub Pages; el frontend se actualizó para
consumir la API desplegada cambiando la variable VITE_API_BASE_URL. Las
actividades de despliegue fueron:  
1. Empaquetar los Web Services con Docker y publicarlos en Render,
disponibles en
<a href="https://smartstock-backend-kj6m.onrender.com" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com</a>
con la documentación en Scalar en
<a href="https://smartstock-backend-kj6m.onrender.com/scalar/v1" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com/scalar/v1</a>  
2. Elojar la base de datos MySQL en Aiven y crear sus 16 tablas por
comando mediante las migraciones de Entity Framework Core (dotnet ef
database update)  
3. Actualizar la Frontend Web Application cambiando la variable
VITE_API_BASE_URL para que consuma la API desplegada y publicarla en
GitHub Pages, disponible en
<a href="https://inventiastock.github.io/smartstock-frontend/" style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/</a>

**Tabla 53**

*Evidencia de despliegue del Sprint 3*

<table>
<tbody>
<tr>
<th>Producto</th>
<th>Repositorio</th>
<th>URL desplegada</th>
<th>Versión</th>
<th>Estado</th>
</tr>
<tr>
<td>Web Services (ASP.NET Core)</td>
<td><a href="https://github.com/InventiaStock/smartstock-backend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-backend</a></td>
<td><a href="https://smartstock-backend-kj6m.onrender.com" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com</a> (documentación: <a href="https://smartstock-backend-kj6m.onrender.com/scalar" style="color:#2563eb">https://smartstock-backend-kj6m.onrender.com/scalar</a>)</td>
<td>v1.0.0 (+ hotfix PR \#16)</td>
<td>Desplegado (Live en Render)</td>
</tr>
<tr>
<td>Base de datos MySQL (Aiven)</td>
<td><a href="https://github.com/InventiaStock/smartstock-backend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-backend</a></td>
<td>MySQL en Aiven: <a href="http://smartstock-db-sanchezosorioruth4-3d9d.i.aivencloud.com:22200" style="color:#2563eb">http://smartstock-db-sanchezosorioruth4-3d9d.i.aivencloud.com:22200</a> (servicio smartstock-db, DigitalOcean nyc, conexión con SSL)</td>
<td>MySQL 8 · migración InitialCreate</td>
<td>Running</td>
</tr>
<tr>
<td>Frontend Web Application</td>
<td><a href="https://github.com/InventiaStock/smartstock-frontend" style="color:#2563eb">https://github.com/InventiaStock/smartstock-frontend</a></td>
<td><a href="https://inventiastock.github.io/smartstock-frontend/" style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/</a></td>
<td>v1.1.0</td>
<td>Desplegado (GitHub Pages)</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Figura 280**

*Backend API de SmartStock desplegado en Render*

<img src="../assets/chapter-5/figura_280.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 281**

*Base de datos MySQL creada en Aiven*

<img src="../assets/chapter-5/figura_281.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 282**

*Visualización de tablas creadas en Aiven mediante la migración de Entity*

Framework Core  
<img src="../assets/chapter-5/figura_282.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 283**

*Verificación del despliegue: /health y documentación en /scalar*

<img src="../assets/chapter-5/figura_283.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Figura 284**

*Ejecución del workflow de integración continua en GitHub Actions*

<img src="../assets/chapter-5/figura_284.png" style="max-height:6.6cm">

Nota. Elaboración propia

#### 5.2.3.8.Team Collaboration Insights during Sprint

Durante el Sprint 3, el equipo organizó la implementación según los
aspectos definidos en la sección 5.2.3.2. Cada integrante trabajó sobre
el contexto que lideraba y registró su aporte mediante commits propios
en el repositorio InventiaStock/smartstock-backend, aplicando GitFlow y
Conventional Commits.

El flujo de trabajo seguido se resume en la siguiente tabla:

**Tabla 54**

*Flujo de ramas de GitFlow seguido en el Sprint 3*

<table>
<tbody>
<tr>
<th>Rama</th>
<th>Nace de</th>
<th>Se integra en</th>
<th>Regla</th>
</tr>
<tr>
<td>main</td>
<td>—</td>
<td>—</td>
<td>Recibe únicamente las versiones publicadas; protegida, solo se modifica mediante pull request.</td>
</tr>
<tr>
<td>develop</td>
<td>—</td>
<td>—</td>
<td>Concentra el avance acumulado del sprint; protegida, solo se modifica mediante pull request.</td>
</tr>
<tr>
<td>feature/\<nombre-descriptivo\></td>
<td>develop</td>
<td>develop</td>
<td>Una rama corta por grupo de tareas del Sprint Backlog; se integra mediante pull request revisado por otro integrante, con merge commit.</td>
</tr>
<tr>
<td>release/\<x.y.z\></td>
<td>develop</td>
<td>main y de vuelta a develop</td>
<td>Prepara la versión a entregar; al integrarse en main se etiqueta con versionado semántico (vX.Y.Z).</td>
</tr>
<tr>
<td>hotfix/\<nombre\></td>
<td>main</td>
<td>main y de vuelta a develop</td>
<td>Corrige un error detectado en la versión publicada.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia.

Los mensajes de commit siguen Conventional Commits (feat, fix, docs,
refactor, test, chore, ci), en inglés y en minúsculas, con el contexto
como alcance y el identificador de la tarea en el cuerpo, por ejemplo
feat(sales): register sales with stock rules and movements.

**Analíticos de colaboración de los repositorios**

La vista de contribuyentes de GitHub atribuye commits a los cinco
integrantes del equipo: @Lore-MS (17), @Yiya-ciber (6), @candyvizz (4),
@leonardoXd1323 (4) y @geral07-UNIV (3), con un total de 34 commits en
la rama develop, sin contar los merge commits. A diferencia del Sprint
2, todos los commits se atribuyen a la cuenta de su autor, porque se
corrigió el correo de Git configurado en cada equipo.

**Figura 285**

*Contributors del repositorio InventiaStock/smartstock-backend*

<img src="../assets/chapter-5/figura_285.png" style="max-height:6.6cm">

Nota. Elaboración propia.

**Figura 286**

**Resumen de actividad (Pulse) del repositorio smartstock-backend, del**

11 de octubre al 11 de noviembre de 2026

<img src="../assets/chapter-5/figura_286.png" style="max-height:6.6cm">

Nota. Elaboración propia.

**Historial de ramas de los repositorios**

El grafo de red muestra la aplicación efectiva de GitFlow: las 14 ramas
de feature nacen de develop y se integran nuevamente a ella mediante
merge commits (pull requests \#1 a \#14), la rama release/1.0.0 prepara
la versión v1.0.0 y se integra en main (#15), y una rama hotfix corrige
el envío de mensajes de WhatsApp con Twilio (#16).

**Figura 287**

*Network graph del repositorio InventiaStock/smartstock-backend*

<img src="../assets/chapter-5/figura_287.png" style="max-height:6.6cm">

Nota. Elaboración propia.

### 5.2.4. Sprint 4

#### 5.2.4.1. Sprint Planning 4

#### 5.2.4.2. Aspect Leaders and Collaborators

#### 5.2.4.3. Sprint Backlog 4

#### 5.2.4.4. Development Evidence for Sprint Review

#### 5.2.4.5. Execution Evidence for Sprint Review

#### 5.2.4.6. Services Documentation Evidence for Sprint Review

#### 5.2.4.7. Software Deployment Evidence for Sprint Review

#### 5.2.4.8. Team Collaboration Insights during Sprint

## 5.3. Validation Interviews

### 5.3.1. Diseño de Entrevistas

Las entrevistas de validación evaluarán la comprensión y la facilidad de
uso del Landing Page y de la Web Application de SmartStock con
propietarios y administradores de minimarkets y bodegas de barrio. El
equipo realizará entre tres y cinco entrevistas por segmento, buscando
contactar nuevamente a los participantes de TB1. A diferencia de las
entrevistas iniciales (2.2.1), que buscaban conocer al usuario y su
problema, estas sesiones buscan observar cómo el usuario reacciona ante
el producto y qué partes no comprende.

Para agilizar las sesiones, se aplicará una demostración guiada e
interactiva: la persona entrevistadora presenta y opera el Landing Page
y la Web Application, y el participante interactúa indicando qué opción
elegiría, qué dato ingresaría y qué espera que ocurra en cada pantalla.
Si el participante desea manejar la aplicación, se le cede el control.
Las preguntas de opinión se realizan al final. Cada sesión dura
aproximadamente 5 a 6 minutos y se edita en un fragmento de 3 a 5
minutos por entrevista, que se integra en el video único de entrevistas
de validación.

Elementos de la sesión de validación

<table>
<tbody>
<tr>
<th>Elemento</th>
<th>Qué se evalúa</th>
<th>Enlace</th>
</tr>
<tr>
<td>Landing Page</td>
<td>Comprensión de la propuesta de valor, planes, preguntas frecuentes y acceso al registro o contacto.</td>
<td><a href="https://inventiastock.github.io/smartstock-landing-page/" style="color:#2563eb">https://inventiastock.github.io/smartstock-landing-page/</a></td>
</tr>
<tr>
<td>Web Application</td>
<td>Los cuatro user flows de cada segmento (ver tablas más abajo).</td>
<td><a href="https://inventiastock.github.io/smartstock-frontend/" style="color:#2563eb">https://inventiastock.github.io/smartstock-frontend/</a></td>
</tr>
</tbody>
</table>

**Preparación de la sesión**

Antes de cada entrevista, la persona entrevistadora comprobará el
funcionamiento del Landing Page y de la Web Application. Se prepararán
los datos de prueba necesarios: una cuenta ya registrada, un producto de
ejemplo, un sensor disponible y una alerta de stock bajo. Se utilizarán
datos ficticios para evitar registrar información sensible. Se aplicará
únicamente la guía correspondiente al segmento del participante.

**Estructura de la sesión**
<table>
<tbody>
<tr>
<th>Fase</th>
<th>Qué ocurre</th>
<th>Tiempo aproximado</th>
</tr>
<tr>
<td>1\. Inicio y datos del participante</td>
<td>Bienvenida, autorización para grabar, nombre y apellido, edad, distrito y función en el negocio.</td>
<td>1 minuto</td>
</tr>
<tr>
<td>2\. Demostración del Landing Page</td>
<td>La persona entrevistadora presenta tres secciones y el participante indica su reacción.</td>
<td>1 minuto</td>
</tr>
<tr>
<td>3\. Demostración de la Web Application</td>
<td>La persona entrevistadora presenta cuatro user flows y el participante indica qué opción elegiría y qué espera que ocurra.</td>
<td>3 minutos</td>
</tr>
<tr>
<td>4\. Preguntas finales y cierre</td>
<td>Cuatro preguntas sobre la experiencia, comentario final y agradecimiento.</td>
<td>1 a 2 minutos</td>
</tr>
</tbody>
</table>

El texto exacto de las fases de inicio y cierre es común para ambos
segmentos y se encuentra en el guion de presentación del equipo, para
que todas las personas entrevistadoras usen las mismas palabras.

**Primer Segmento Objetivo (Propietarios y administradores de**

minimarkets)

**Demostración del Landing Page**

Se mostrará primero el Landing Page y se indicará: «Le voy a mostrar
nuestra página como si estuviera buscando una herramienta para su
minimarket. Cuénteme qué le llama la atención o qué no entiende.»

<table>
<tbody>
<tr>
<th>Sección del Landing Page</th>
<th>Qué presenta la persona entrevistadora</th>
<th>Qué indica el participante</th>
</tr>
<tr>
<td>Propuesta de valor</td>
<td>Muestra el inicio de la página y los beneficios.</td>
<td>Qué entiende que ofrece SmartStock.</td>
</tr>
<tr>
<td>Planes</td>
<td>Muestra los planes Crecimiento y Business.</td>
<td>Qué diferencia ve entre ambos y cuál elegiría.</td>
</tr>
<tr>
<td>Acceso al registro</td>
<td>Muestra la parte superior de la página.</td>
<td>Dónde cree que debería ingresar para comenzar.</td>
</tr>
</tbody>
</table>

**User flows de la Web Application**

Se indicará: «Ahora le mostraré la aplicación. Iré presentando una
pantalla a la vez y le pediré que me diga qué opción elegiría y qué
espera que pase. Si prefiere manejarla usted, con gusto.»

<table>
<tbody>
<tr>
<th>N.°</th>
<th>User flow</th>
<th>Qué presenta la persona entrevistadora</th>
<th>Qué indica el participante</th>
<th>Qué se observa</th>
</tr>
<tr>
<td>1</td>
<td>Registro de productos</td>
<td>Muestra el formulario de un producto de prueba.</td>
<td>Qué nivel de existencias fijaría para recibir una alerta de stock bajo (la persona entrevistadora lo ingresa).</td>
<td>Si entiende el campo del umbral de stock.</td>
</tr>
<tr>
<td>2</td>
<td>Consulta y vinculación de sensores</td>
<td>Muestra la lista de sensores y el estado de uno disponible.</td>
<td>Qué entiende del estado del sensor y cuál vincularía al producto.</td>
<td>Si interpreta el estado y reconoce cómo vincularlo.</td>
</tr>
<tr>
<td>3</td>
<td>Registro de ventas</td>
<td>Muestra la pantalla de ventas.</td>
<td>Qué opción tocaría para registrar la venta de un producto y qué espera que ocurra con las existencias (la persona entrevistadora la registra).</td>
<td>Si identifica la opción correcta y comprende el cambio en las existencias.</td>
</tr>
<tr>
<td>4</td>
<td>Reposición desde una alerta</td>
<td>Muestra una alerta de stock bajo.</td>
<td>Qué significa la alerta y qué opción elegiría para reponer el producto (la persona entrevistadora inicia la compra).</td>
<td>Si entiende la alerta y encuentra cómo iniciar la compra.</td>
</tr>
</tbody>
</table>

**Preguntas finales**

Al terminar la demostración, se indicará: «Gracias. Ahora quisiéramos
conocer su opinión sobre la experiencia.»

1\. ¿Qué entiende que ofrece SmartStock y qué información le resultó confusa o considera que falta?

2\. ¿Qué parte de la aplicación le resultó más clara y cuál le generó más dudas?

3\. ¿Confiaría en las alertas para decidir cuándo reponer un producto? ¿Por qué?

4\. ¿Qué precio mensual consideraría razonable por esta solución y por qué?

**Segundo Segmento Objetivo (Propietarios y administradores de bodegas**

de barrio)

**Demostración del Landing Page**

Se mostrará primero el Landing Page y se indicará: «Le voy a mostrar
nuestra página como si estuviera buscando una herramienta para su
bodega. Cuénteme qué le llama la atención o qué no entiende.»

<table>
<tbody>
<tr>
<th>Sección del Landing Page</th>
<th>Qué presenta la persona entrevistadora</th>
<th>Qué indica el participante</th>
</tr>
<tr>
<td>Propuesta de valor y casos de uso para bodegas</td>
<td>Muestra el inicio de la página y los casos de uso.</td>
<td>Para qué cree que podría utilizar SmartStock en su bodega.</td>
</tr>
<tr>
<td>Plan Inicial y preguntas frecuentes sobre sensores</td>
<td>Muestra el plan Inicial y las preguntas frecuentes sobre la instalación de sensores.</td>
<td>Qué entiende que incluye el plan y qué dudas tiene sobre los sensores.</td>
</tr>
<tr>
<td>Acceso al registro</td>
<td>Muestra la parte superior de la página.</td>
<td>Dónde cree que debería ingresar para comenzar.</td>
</tr>
</tbody>
</table>

**User flows de la Web Application**

Se indicará: «Ahora le mostraré la aplicación. Iré presentando una
pantalla a la vez y le pediré que me diga qué opción elegiría y qué
espera que pase. Si prefiere manejarla usted, con gusto.»

<table>
<tbody>
<tr>
<th>N.°</th>
<th>User flow</th>
<th>Qué presenta la persona entrevistadora</th>
<th>Qué indica el participante</th>
<th>Qué se observa</th>
</tr>
<tr>
<td>1</td>
<td>Registro de productos</td>
<td>Muestra el formulario de un producto de prueba.</td>
<td>Qué nivel de existencias fijaría para recibir una alerta de stock bajo (la persona entrevistadora lo ingresa).</td>
<td>Si entiende el campo del umbral de stock.</td>
</tr>
<tr>
<td>2</td>
<td>Consulta y vinculación de sensores</td>
<td>Muestra la lista de sensores y el estado de uno disponible.</td>
<td>Qué entiende del estado del sensor y cuál vincularía al producto.</td>
<td>Si interpreta el estado y reconoce cómo vincularlo.</td>
</tr>
<tr>
<td>3</td>
<td>Registro de una venta simple</td>
<td>Muestra la pantalla de ventas.</td>
<td>Qué opción tocaría para registrar una venta y cuántas unidades espera que queden (la persona entrevistadora la registra).</td>
<td>Si identifica la opción con pocos pasos y entiende las unidades restantes.</td>
</tr>
<tr>
<td>4</td>
<td>Consulta de alertas y reposición</td>
<td>Muestra una alerta de stock bajo.</td>
<td>Qué haría al recibirla y qué opción elegiría para reponer el producto (la persona entrevistadora inicia la compra).</td>
<td>Qué decisión toma ante la alerta y si encuentra cómo iniciar la compra.</td>
</tr>
</tbody>
</table>

**Preguntas finales**

Al terminar la demostración, se indicará: «Gracias. Ahora quisiéramos
conocer su opinión sobre la experiencia.»

1\. ¿Qué entiende que ofrece SmartStock en su bodega y qué dudas le quedan sobre los sensores?

2\. ¿Qué parte de la aplicación le resultó más clara y cuál le generó más dudas?

3\. ¿Qué entendió de la alerta de stock bajo y qué decisión tomaría al verla?

4\. Viendo el plan Inicial, ¿qué precio mensual consideraría razonable por esta solución y por qué?

**Indicaciones de observación (comunes para ambos segmentos)**

Antes de ejecutar cada acción en la aplicación, la persona
entrevistadora esperará a que el participante indique qué opción
elegiría, sin señalar botones. Si el participante no sabe cómo
continuar, se le ayudará y se registrará. Si desea manejar la
aplicación, se le cederá el control y se dejará constancia de esta
modalidad. Para el video, de cada entrevista se conservará un fragmento
de 3 a 5 minutos con el título del entrevistado, su segmento y la fecha.
Las reacciones, las dificultades y la ayuda brindada serán la base de la
evaluación según heurísticas (5.3.3).

### 5.3.2. Registro de Entrevistas.

**Needfinding Interviews Link:**

<a href="https://upcedupe-my.sharepoint.com/%3Av%3A/g/personal/u20241f205_upc_edu_pe/IQCD31owQgSgTZFdrCyY4KOZAU7JcAG4oKshYrSLWzAkljE?e=TSODlh&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" style="color:#2563eb">https://upcedupe-my.sharepoint.com/&#58;v&#58;/g/personal/u20241f205_upc_edu_pe/IQCD31owQgSgTZFdrCyY4KOZAU7JcAG4oKshYrSLWzAkljE?e=TSODlh&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D</a>

Entrevista 01: 00:05 - 07:42

Entrevista 02: 07:47 - 14:23

Entrevista 03: 14:28 - 20:36

Entrevista 04: 20:41 - 27:08

Entrevista 05: 27:13 - 39:48

**Figura 288**

*Video de entrevistas de validación a propietarios y administradores de minimarkets y bodegas de barrio*
<img src="../assets/chapter-5/figura_288.png" style="max-height:6.6cm">

Nota. Elaboración propia

**Primer Segmento Objetivo (Propietarios y administradores de**

minimarkets)

**Tabla 55**

*Registro de la entrevista 1 a propietarios y administradores de*

minimarkets
<table>
<tbody>
<tr>
<th>Screenshot:</th>
<th><img src="../assets/chapter-5/figura_288_a.png" style="max-height:6.6cm"></th>
</tr>
<tr>
<td>Inicia:</td>
<td>00:05</td>
</tr>
<tr>
<td>Duración:</td>
<td>07:37</td>
</tr>
<tr>
<td>Nombre completo:</td>
<td>José Martín Montañez</td>
</tr>
<tr>
<td>Edad:</td>
<td>51 años</td>
</tr>
<tr>
<td>Distrito:</td>
<td>Pueblo Libre</td>
</tr>
<tr>
<td>Resumen:</td>
<td>José identificó SmartStock como una solución para controlar el inventario, gestionar reposiciones y recibir alertas. Eligió el plan Business y propuso recibir avisos desde diez unidades, considerando la rotación de cada producto. Reconoció las opciones para crear una cuenta, registrar ventas y nuevas compras, pero manifestó dificultad para comprender los estados de los sensores. Consideró útiles las alertas para contactar a sus proveedores y señaló que las revisaría al iniciar y terminar el día. Como mejora principal, sugirió incorporar la lectura de códigos de barras en ventas y compras para evitar digitar numerosos productos. No precisó una tarifa mensual concreta.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 56**

*Registro de la entrevista 2 a propietarios y administradores de*

minimarkets
<table>
<tbody>
<tr>
<th>Screenshot:</th>
<th><img src="../assets/chapter-5/figura_288_b.png" style="max-height:6.6cm"></th>
</tr>
<tr>
<td>Inicia:</td>
<td>07:47</td>
</tr>
<tr>
<td>Duración:</td>
<td>06:36</td>
</tr>
<tr>
<td>Nombre completo:</td>
<td>Cristopher Benavides</td>
</tr>
<tr>
<td>Edad:</td>
<td>23 años</td>
</tr>
<tr>
<td>Distrito:</td>
<td>Jesus Maria</td>
</tr>
<tr>
<td>Resumen:</td>
<td>Cristopher identificó SmartStock como una herramienta para actualizar el stock mediante las entradas y salidas de productos. Eligió el plan Crecimiento y propuso recibir alertas desde cuatro unidades. Consideró el panel la pantalla más clara y destacó el cambio de idioma y las notificaciones. Inicialmente tuvo dificultad para seguir la demostración de compras y, al preguntarle cómo registrar una venta, señaló la opción Comprobante, lo que sugiere revisar la claridad de esa acción. Indicó que confiaría en las alertas para decidir cuándo reponer y consideró razonable un precio mensual cercano a S/100.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 57**

*Registro de la entrevista 3 a propietarios y administradores de*

minimarkets
<table>
<tbody>
<tr>
<th>Screenshot:</th>
<th><img src="../assets/chapter-5/figura_288_c.png" style="max-height:6.6cm"></th>
</tr>
<tr>
<td>Inicia:</td>
<td>14:28</td>
</tr>
<tr>
<td>Duración:</td>
<td>06:08</td>
</tr>
<tr>
<td>Nombre completo:</td>
<td>Yngrid Ruiz</td>
</tr>
<tr>
<td>Edad:</td>
<td>23 años</td>
</tr>
<tr>
<td>Distrito:</td>
<td>Pueblo Libre</td>
</tr>
<tr>
<td>Resumen:</td>
<td>Yngrid identificó SmartStock como una solución para registrar y controlar el inventario de su minimarket. Tras la demostración guiada, consideró que la aplicación era completa y señaló el registro de inventario como la función más clara. No manifestó dudas sobre las secciones presentadas y afirmó que confiaría en las alertas para decidir cuándo reponer, porque los productos estarían registrados en la aplicación. Consideró razonable un precio mensual de S/50 y no añadió otras observaciones.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Segundo Segmento Objetivo (Propietarios y administradores de bodegas**

de barrio)

**Tabla 58**

*Registro de la entrevista 1 a propietarios y administradores de bodegas*

de barrio
<table>
<tbody>
<tr>
<th>Screenshot:</th>
<th><img src="../assets/chapter-5/figura_288_d.png" style="max-height:6.6cm"></th>
</tr>
<tr>
<td>Inicia:</td>
<td>20:41</td>
</tr>
<tr>
<td>Duración:</td>
<td>06:27</td>
</tr>
<tr>
<td>Nombre completo:</td>
<td>Lincoln Bruno</td>
</tr>
<tr>
<td>Edad:</td>
<td>49 años</td>
</tr>
<tr>
<td>Distrito:</td>
<td>Comas</td>
</tr>
<tr>
<td>Resumen:</td>
<td>Lincoln identificó SmartStock como una herramienta para controlar el stock de su tienda y almacén. Eligió el plan Inicial para conocer su funcionamiento y evaluar posteriormente otros planes según el movimiento del negocio. Propuso recibir alertas desde cinco unidades y señaló que estas le permitirían realizar pedidos para reponer productos. Esperaba acceder directamente desde una alerta al registro de compras. Aunque consideró que la aplicación era clara en general, solicitó una mejor explicación sobre el funcionamiento de los sensores. Al preguntarle cómo registrar una venta, señaló la opción Comprobante, por lo que conviene revisar la claridad de esa acción.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Tabla 59**

*Registro de la entrevista 2 a propietarios y administradores de bodegas*

de barrio
<table>
<tbody>
<tr>
<th>Screenshot:</th>
<th><img src="../assets/chapter-5/figura_288_e.png" style="max-height:6.6cm"></th>
</tr>
<tr>
<td>Inicia:</td>
<td>27:13</td>
</tr>
<tr>
<td>Duración:</td>
<td>12:35</td>
</tr>
<tr>
<td>Nombre completo:</td>
<td>Ruth Osorio</td>
</tr>
<tr>
<td>Edad:</td>
<td>42 años</td>
</tr>
<tr>
<td>Distrito:</td>
<td>San Juan de Lurigancho</td>
</tr>
<tr>
<td>Resumen:</td>
<td>Ruth identificó SmartStock como una solución para detectar productos próximos a agotarse, controlar el almacén y realizar pedidos a tiempo. Destacó la posibilidad de controlar sus productos sin revisarlos manualmente. Entendió que el plan Inicial incluía el registro de entradas y salidas y las alertas de stock bajo. Solicitó información sobre cómo se colocan los sensores debajo de los productos, cómo funcionan y cuánto costaría implementarlos en su bodega.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Análisis de entrevistas de validación**

Se analizaron las respuestas de cinco participantes: tres del segmento
de propietarios y administradores de minimarkets y dos del segmento de
propietarios y administradores de bodegas de barrio. Las sesiones
permitieron recoger opiniones sobre la comprensión de SmartStock, la
navegación de la aplicación, las alertas y las mejoras esperadas.

Se dispone de la transcripción completa de cuatro entrevistas y de una
transcripción parcial de la entrevista de Ruth Osorio. Por ello, los
resultados de esta última se limitan a las respuestas disponibles. Los
porcentajes describen únicamente a los participantes analizados y no
representan a la totalidad de negocios de cada segmento.

**Primer segmento objetivo: propietarios y administradores de**

minimarkets
Participaron José Montañez, Cristopher Benavides y Yngrid Ruiz, con
edades declaradas de 51, 23 y 23 años, respectivamente. El 66,7 % de los
participantes tiene 23 años. José y Cristopher señalaron residir en
Jesús María, mientras que el distrito de Yngrid no se especificó en la
entrevista disponible.

Los tres participantes relacionaron SmartStock con el control del
inventario. José destacó su utilidad para gestionar las existencias, las
reposiciones y las alertas; Cristopher reconoció el registro de entradas
y salidas de productos; y Yngrid identificó la solución como una
herramienta para registrar y administrar el inventario. Asimismo, los
tres expresaron confianza en las alertas para decidir cuándo reponer
productos.

Se identificaron dificultades específicas durante la demostración. José
manifestó que no comprendía el significado de los estados de los
sensores y propuso incorporar la lectura de códigos de barras para
agilizar las ventas y compras. Cristopher indicó que necesitaba mayor
claridad en el recorrido de compras porque no había observado con
precisión dónde se hacía clic. Además, al preguntarle cómo registrar una
venta, señaló la opción «Comprobante», lo que sugiere revisar la
claridad de esa acción. Yngrid consideró claro el registro de inventario
y no manifestó dudas al finalizar la sesión.

**Hallazgos identificados en las entrevistas de validación de**

minimarkets

**Tabla 60**

*Hallazgos de las entrevistas de validación a propietarios y*

administradores de minimarkets
<table>

<tbody>
<tr>
<th>
<p><strong>Aspecto evaluado</strong></p>
</th>
<th>
<p><strong>Hallazgo identificado</strong></p>
</th>
<th>
<p><strong>Frecuencia</strong></p>
</th>
</tr>
<tr>
<td>
<p>Comprensión de la propuesta</p>
</td>
<td>
<p>Relacionaron SmartStock con el registro o control del inventario.</p>
</td>
<td>
<p>3 de 3 (100 %)</p>
</td>
</tr>
<tr>
<td>
<p>Confianza en las alertas</p>
</td>
<td>
<p>Expresaron que confiarían en las alertas para decidir cuándo reponer
productos.</p>
</td>
<td>
<p>3 de 3 (100 %)</p>
</td>
</tr>
<tr>
<td>
<p>Comprensión de los sensores</p>
</td>
<td>
<p>José manifestó explícitamente que no comprendía los estados
mostrados.</p>
</td>
<td>
<p>1 de 3 (33,3 %)</p>
</td>
</tr>
<tr>
<td>
<p>Claridad del recorrido de compras</p>
</td>
<td>
<p>Cristopher solicitó mayor claridad sobre los pasos mostrados durante
la demostración.</p>
</td>
<td>
<p>1 de 3 (33,3 %)</p>
</td>
</tr>
<tr>
<td>
<p>Agilidad del registro</p>
</td>
<td>
<p>José propuso incorporar códigos de barras para reducir la digitación
de productos.</p>
</td>
<td>
<p>1 de 3 (33,3 %)</p>
</td>
</tr>
<tr>
<td>
<p>Ausencia de dudas declaradas</p>
</td>
<td>
<p>Yngrid manifestó que no tenía dudas al finalizar la sesión.</p>
</td>
<td>
<p>1 de 3 (33,3 %)</p>
</td>
</tr>
<tr>
<td>
<p>Referencia de precio mensual</p>
</td>
<td>
<p>Cristopher propuso aproximadamente S/ 100 y Yngrid, S/ 50.</p>
</td>
<td>
<p>2 de 3 (66,7 %)</p>
</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia a partir de las respuestas de validación. Las

frecuencias registran menciones explícitas; la ausencia de una mención
no implica una opinión contraria. La respuesta de José sobre el precio
no permitió identificar con claridad una tarifa mensual comparable.

En conclusión, los resultados de este segmento muestran una comprensión
compartida de la finalidad de SmartStock y una valoración favorable de
las alertas de reposición. No obstante, la aceptación general no elimina
las dificultades específicas encontradas. Se recomienda explicar los
estados de los sensores con lenguaje sencillo, mostrar de forma más
clara la secuencia de compras y evaluar la incorporación de códigos de
barras. Las referencias de precio presentan diferencias, por lo que no
permiten establecer una tarifa única aceptada por el segmento.

**Segundo segmento objetivo: propietarios y administradores de bodegas**

de barrio
Se analizaron las entrevistas de Lincoln Bruno, de 49 años y residente
en Comas, e Ian Kimi San Martin Cauti, de 20 años y residente en
Santiago de Surco. La entrevista de Lincoln cuenta con transcripción
completa y la de Ian dispone de una transcripción parcial.

Ambos participantes identificaron beneficios relacionados con el control
de productos y la reposición. Lincoln vinculó la solución con la gestión
del almacén y del stock de su tienda. Ian destacó la posibilidad de
organizar el inventario, reconocer qué productos se están agotando y
saber cuándo reponer mercadería. Explicó que, durante los periodos de
numerosas ventas, resulta difícil revisar manualmente las existencias.

Los dos participantes solicitaron información adicional sobre los
sensores. Lincoln expresó que necesitaba comprender mejor su
funcionamiento y cómo apoyarían el control de estantes con numerosos
productos. Ian planteó dudas sobre su funcionamiento, los posibles
costos adicionales y los requisitos necesarios para implementarlos.
Estas respuestas muestran la necesidad de explicar tanto el uso de los
dispositivos como las condiciones para incorporarlos al negocio.

Respecto a la adopción, Lincoln prefirió comenzar con el plan Inicial
para aprender a utilizar la herramienta y evaluar posteriormente otros
planes. Ian también consideró que el plan Inicial podía ser adecuado
para una bodega pequeña. Lincoln, además, manifestó que esperaba pasar
desde las alertas hacia la compra de los productos faltantes.

Hallazgos identificados en las entrevistas de validación de bodegas de
barrio

**Tabla 61**

*Hallazgos de las entrevistas de validación a propietarios y*

administradores de bodegas de barrio
<table>

<tbody>
<tr>
<th>
<p>Aspecto evaluado</p>
</th>
<th>
<p>Hallazgo identificado</p>
</th>
<th>
<p>Alcance de la evidencia</p>
</th>
</tr>
<tr>
<td>
<p>Comprensión de la propuesta</p>
</td>
<td>
<p>Ambos relacionaron SmartStock con el control de productos, almacén o
stock.</p>
</td>
<td>
<p>2 de 2 (100 %)</p>
</td>
</tr>
<tr>
<td>
<p>Comprensión de los sensores</p>
</td>
<td>
<p>Ambos solicitaron explicaciones adicionales sobre su funcionamiento o
implementación.</p>
</td>
<td>
<p>2 de 2 (100 %)</p>
</td>
</tr>
<tr>
<td>
<p>Reposición de productos</p>
</td>
<td>
<p>Lincoln indicó que realizaría pedidos al recibir una alerta de stock
bajo.</p>
</td>
<td>
<p>Respuesta verificada en Lincoln; sin respuesta disponible de Ruth a
esa pregunta.</p>
</td>
</tr>
<tr>
<td>
<p>Continuidad entre alertas y compras</p>
</td>
<td>
<p>Lincoln manifestó que esperaba pasar desde las alertas hacia la
compra de los productos faltantes.</p>
</td>
<td>
<p>Hallazgo individual de Lincoln.</p>
</td>
</tr>
<tr>
<td>
<p>Adopción gradual</p>
</td>
<td>
<p>Lincoln prefirió comenzar con el plan inicial para aprender y evaluar
posteriormente otros planes.</p>
</td>
<td>
<p>Hallazgo individual de Lincoln.</p>
</td>
</tr>
<tr>
<td>
<p>Reducción del trabajo manual</p>
</td>
<td>
<p>Ruth destacó el beneficio de controlar productos sin revisar todo
manualmente.</p>
</td>
<td>
<p>Hallazgo individual de Ruth.</p>
</td>
</tr>
<tr>
<td>
<p>Instalación y costo de sensores</p>
</td>
<td>
<p>Ruth solicitó información sobre su colocación y costo de
implementación.</p>
</td>
<td>
<p>Hallazgo individual de Ruth.</p>
</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia. Los porcentajes se utilizan únicamente en

aspectos con respuestas disponibles de ambos participantes. No se
atribuyen a Ruth opiniones sobre pantallas o preguntas que no aparecen
en su transcripción parcial.

En conclusión, los participantes de este segmento reconocieron la
utilidad de SmartStock para controlar existencias y apoyar la
reposición. La principal necesidad compartida fue comprender el
funcionamiento de los sensores, mencionada por el 100 % de los
participantes analizados. Se recomienda incorporar explicaciones
visuales sobre su instalación, ejemplos de uso y una presentación clara
de sus costos. Asimismo, conviene facilitar el paso desde una alerta
hacia el registro de una compra y acompañar a los usuarios durante su
aprendizaje inicial.

**Conclusión general**

Las entrevistas muestran que los cinco participantes comprendieron la
finalidad de SmartStock como herramienta para controlar el inventario.
En los minimarkets destacó la confianza declarada en las alertas de
reposición, mientras que en las bodegas se identificó una necesidad
compartida de información adicional sobre los sensores y su
implementación.

Las mejoras prioritarias son explicar los estados y el funcionamiento de
los dispositivos, hacer más comprensible el recorrido de compras y
facilitar la identificación del registro de ventas. La propuesta de
incorporar códigos de barras constituye una oportunidad adicional para
reducir la digitación de productos.

Estos hallazgos sirven como insumo para la evaluación de usabilidad y
las propuestas de mejora de la interfaz. Las opiniones favorables
expresadas durante una demostración guiada no permiten afirmar, por sí
solas, que todos los participantes puedan completar las tareas sin
ayuda.

### 5.3.3. Evaluaciones según heurísticas

**Site o app a evaluar**

SmartStock: Landing Page y Aplicación Web, en la versión mostrada
durante las sesiones de validación.

**Tareas a evaluar**

El alcance de esta evaluación incluye la revisión de la usabilidad de
las siguientes tareas, tomadas de las sesiones de validación (5.3.2):

1.  Identificar qué ofrece SmartStock y elegir un plan en la Landing Page.

2.  Crear una cuenta.

3.  Registrar productos y definir desde cuántas unidades se desea recibir una alerta.

4.  Registrar una venta.

5.  Registrar una compra a un proveedor.

6.  Interpretar el estado de los sensores de peso.

7.  Atender una alerta de stock bajo e iniciar la reposición.

8.  Consultar reportes y la comparación entre lo registrado y lo que pesan los sensores.

No están incluidas en esta versión de la evaluación las siguientes
tareas:

1.  Inicio de sesión con credenciales propias y control de acceso (Sprint 4).

2.  Recepción de alertas por correo y WhatsApp.

3.  Instalación física de los sensores de peso en el negocio.

4.  Lectura de códigos de barras (función aún no implementada).

5.  Pago de un plan de suscripción.

**Escala de severidad**

Los errores serán puntuados tomando en cuenta la siguiente escala de
severidad:

**Tabla 62**

*Escala de severidad de los problemas de usabilidad*

<table>
<tbody>
<tr>
<th>Nivel</th>
<th>Descripción</th>
</tr>
<tr>
<td>1</td>
<td>Problema superficial: puede ser fácilmente superado por el usuario o se da con muy poca frecuencia. No necesita ser arreglado a menos que exista disponibilidad de tiempo.</td>
</tr>
<tr>
<td>2</td>
<td>Problema menor: puede ocurrir con un poco más de frecuencia o es algo más difícil de superar para el usuario. Se le debe asignar una prioridad baja de cara al siguiente release.</td>
</tr>
<tr>
<td>3</td>
<td>Problema mayor: ocurre con frecuencia o los usuarios no logran resolverlo. Es importante corregirlo y se le debe asignar una prioridad alta.</td>
</tr>
<tr>
<td>4</td>
<td>Problema muy grave: un error de gran impacto que impide al usuario continuar con el uso de la herramienta. Es imperativo corregirlo antes del lanzamiento.</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Resumen en una tabla**

**Tabla 63**

*Resumen de los problemas de usabilidad identificados*

<table>
<tbody>
<tr>
<th>\#</th>
<th>Problema</th>
<th>Escala de severidad</th>
<th>Heurística o principio violado</th>
</tr>
<tr>
<td>1</td>
<td>El estado de los sensores (En línea, Desconectado, Disponible) no se entiende o se interpreta de formas distintas</td>
<td>3</td>
<td>Usability: Correspondencia entre el sistema y el mundo real</td>
</tr>
<tr>
<td>2</td>
<td>La opción Comprobante se confunde con la acción de registrar una venta</td>
<td>3</td>
<td>Usability: Reconocer antes que recordar</td>
</tr>
<tr>
<td>3</td>
<td>No hay explicación accesible de cómo se colocan, funcionan y cuánto cuestan los sensores</td>
<td>2</td>
<td>Information Architecture: Is it findable?</td>
</tr>
<tr>
<td>4</td>
<td>Registrar ventas y compras exige digitar cada producto; no hay lectura de código de barras</td>
<td>2</td>
<td>Usability: Flexibilidad y eficiencia de uso</td>
</tr>
<tr>
<td>5</td>
<td>El usuario espera pasar de la alerta de stock bajo directamente a registrar la compra</td>
<td>1</td>
<td>Usability: Reconocer antes que recordar</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

**Descripción de problemas**

**PROBLEMA \#1: El estado de los sensores no se entiende o se interpreta**

de formas distintas
**Severidad:** 3

**Heurística violada:** Usability – Correspondencia entre el sistema y
el mundo real

**Problema:**

La columna de estado de la pantalla de sensores muestra los valores En
línea, Desconectado y Disponible sin explicar qué significan ni qué
acción corresponde. José Martín Montañez pudo leer los estados, pero
indicó que no los entendía. Cristopher Benavides los interpretó como si
el producto estaba siendo contabilizado o si no había datos suficientes.
Lincoln Bruno entendió que los sensores estaban "activados". Los tres
participantes a quienes se les preguntó por esta columna dieron una
lectura distinta o ninguna, lo que muestra que los términos no se
corresponden con el lenguaje del usuario. Además, al cierre de su
entrevista Lincoln pidió que se explique cómo funciona el sensor.

**Figura 289**

*Pantalla de Sensores con la columna de estado (En línea, Desconectado*

y Disponible)

<img src="../assets/chapter-5/figura_289.png" style="max-height:6.6cm">

Nota. Captura de la entrevista a José Martín Montañez (inicio 00:05). Elaboración propia.

**Recomendación:**

Agregar una breve leyenda junto a la columna de estado que explique cada
valor, por ejemplo "En línea: envió una lectura en los últimos 5
minutos". Usar un texto de ayuda o un ícono de información con la acción
que corresponde cuando un sensor aparece desconectado.

**PROBLEMA \#2: La opción Comprobante se confunde con la acción de**

registrar una venta
**Severidad:** 3

**Heurística violada:** Usability – Reconocer antes que recordar

**Problema:**

Al pedirles que indicaran cómo registrar una venta, Cristopher Benavides
y Lincoln Bruno señalaron la opción Comprobante. Cristopher la entendió
como el lugar para ver los productos vendidos; Lincoln, como la acción
para emitir el comprobante. En cambio, José Martín Montañez encontró el
botón Nueva venta. Dos de tres participantes que realizaron esta tarea
no encontraron la acción principal de la pantalla, por lo que la acción
de registrar y la de consultar una venta no se diferencian con claridad.

**Figura 290**

***Pantalla de Ventas con las opciones Nueva venta y Comprobante***

<img src="../assets/chapter-5/figura_290.png" style="max-height:6.6cm">

Nota. Captura de la entrevista a Cristopher Benavides (inicio 07:47). Elaboración propia.

**Recomendación:**

Destacar el botón Nueva venta como acción principal, con mayor tamaño y
color, y renombrar la opción Comprobante por un texto que indique que es
una consulta, por ejemplo "Ver detalle de la venta".

**PROBLEMA \#3: No hay una explicación accesible de los sensores**

(instalación, funcionamiento y costo)
**Severidad**: 2

**Heurística violada**: Information Architecture – Is it findable?

**Problema:**

Lincoln Bruno pidió que se explicara mejor cómo funciona el sensor y
Ruth Osorio preguntó cómo se colocan debajo de los productos, cómo
funcionan y cuánto costaría implementarlos en su bodega. Estas dudas
surgieron en ambos segmentos y corresponden a la función que diferencia
a SmartStock, por lo que la información de ayuda no resulta fácil de
encontrar para el usuario.

**Figura 291**

***Landing Page, sección donde se mencionan los sensores de peso***

<img src="../assets/chapter-5/figura_291.png" style="max-height:6.6cm">

Nota. Captura de la entrevista a Ruth Osorio (inicio 27:13). Elaboración propia.

**Recomendación:**

Incluir en la Landing Page y en la aplicación una sección breve "Cómo
funcionan los sensores" con la instalación, el funcionamiento y una
referencia del costo, enlazada desde la pantalla de sensores.

**PROBLEMA \#4: Registrar ventas y compras exige digitar cada producto**

**Severidad**: 2

**Heurística violada**: Usability – Flexibilidad y eficiencia de uso

**Problema:**

José Martín Montañez indicó que lo más importante que faltaba era la
lectura del código de barras en ventas y compras, porque las facturas de
sus proveedores llegan con 15, 20, 30 y hasta 40 ítems y digitarlos uno
por uno toma mucho tiempo. El problema fue señalado por un solo
participante, pero afecta a una tarea que el negocio repite a diario.

**Figura 292**

***Formulario Nueva compra de la aplicación web***

<img src="../assets/chapter-5/figura_292.png" style="max-height:6.6cm">

Nota. Captura de la entrevista a José Martín Montañez (inicio 00:05). Elaboración propia.

**Recomendación:**

Incorporar la lectura de códigos de barras en los formularios de venta y
compra, y, mientras tanto, permitir buscar y seleccionar productos desde
una lista con búsqueda por nombre.

**PROBLEMA \#5: El usuario espera pasar de la alerta de stock bajo**

directamente a registrar la compra
**Severidad**: 1

**Heurística violada**: Usability – Reconocer antes que recordar

**Problema:**

Lincoln Bruno esperaba ir de la alerta directamente a la compra, y
Cristopher Benavides dijo que la usaría para registrar una nueva compra.
Los participantes entendieron bien qué hacer ante la alerta (contactar
al proveedor o hacer el pedido), por lo que el problema es leve: el
atajo hacia la compra no fue evidente durante la demostración.

**Figura 293**

***Pantalla de Alertas de stock bajo***

<img src="../assets/chapter-5/figura_293.png" style="max-height:6.6cm">

Nota. Captura de la entrevista a Lincoln Bruno (inicio 20:41). Elaboración propia.

**Recomendación:**

Mantener visible, junto a cada alerta, el botón "Registrar compra" que
lleva al formulario con el producto ya seleccionado.

**Observaciones de diseño inclusivo**

Cristopher Benavides valoró positivamente el cambio de idioma entre
español e inglés, las notificaciones y las opciones de sesión. Durante
las sesiones no se probó la aplicación con lectores de pantalla ni con
navegación por teclado, por lo que no se registraron problemas de este
tipo. La Landing Page y la aplicación incorporan atributos ARIA como
parte de la mejora continua M11, y se recomienda validarlos con un
lector de pantalla en el siguiente sprint.

## 5.4. Video About-the-Product

En esta sección se presenta el video About-the-Product de SmartStock,
dirigido a los visitantes de la Landing Page y a los usuarios de la
aplicación: propietarios y administradores de minimarkets y bodegas de
barrio. El video resume la propuesta de valor del sistema, que permite
controlar el inventario comparando el stock registrado con el stock
físico medido por sensores IoT, y muestra escenas de interacción con la
Web App, como el panel, el registro de compras y ventas, la comparación
de inventario y las alertas de stock bajo. Además, incluye la opinión de
usuarios de ambos segmentos que participaron en las entrevistas de
validación.

**Figura 294**

*Captura del video About-the-Product de SmartStock (2:56)*

<img src="../assets/chapter-5/figura_294.png" style="max-height:6.6cm">

Nota. Elaboración propia.

**Nombre del archivo:**

upc-pre-202620-1asi0730-8168-inventiastock-about-the-product-sprint-3.mp4

**Duración:** 2:56

**Video About-the-Product (Microsoft Stream):**

<a href="https://upcedupe-my.sharepoint.com/%3Av%3A/g/personal/u20241f205_upc_edu_pe/IQDt74urtMRpQq5e6TGbpgsGAXq2FqEG-uEW2QSq1XAW85Y?e=U39l7V&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" style="color:#2563eb">https://upcedupe-my.sharepoint.com/&#58;v&#58;/g/personal/u20241f205_upc_edu_pe/IQDt74urtMRpQq5e6TGbpgsGAXq2FqEG-uEW2QSq1XAW85Y?e=U39l7V&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D</a>

**Video About-the-Product (YouTube):**

<a href="https://youtu.be/SkEUuXnyouY" style="color:#2563eb">https://youtu.be/SkEUuXnyouY</a>
