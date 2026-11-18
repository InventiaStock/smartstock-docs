
# Capítulo IV: Product Design
## 4.1. Style Guidelines 

En este apartado estableceremos los criterios visuales y de comunicación
que se utilizarán en el diseño del Landing Page y de la Web
Application,. El diseño estará centrado en transmitir una imagen simple,
moderna y confiable, utilizando colores, tipografías, botones e iconos
que permitan entender fácilmente la información. Como SmartStock está
dirigido a propietarios y administradores de minimarkets y bodegas de
barrio, se evitará un diseño demasiado complejo y se priorizará una
interfaz sencilla y fácil de usar para los usuarios

### 4.1.1. General Style Guidelines

**Branding**

SmartStock es operado por InventiaStock. El logo se usa como ícono de 42
x 42px junto al nombre de marca en la cabecera (reducido a 34 x 34px en
pantallas móviles menores a 720px), manteniendo consistencia en todas
las vistas.

**Typography.**

Para la identidad visual del producto, se seleccionó una tipografía que
combine claridad, accesibilidad y un estilo tecnológico.

- **Tipografía:** Manrope, disponible en Google Fonts.
- **Peso 400 (Regular):** utilizado para el texto de cuerpo.
- **Peso 600 (Semibold):** aplicado en labels, botones y elementos de navegación.
- **Peso 700 (Bold):** utilizado en los títulos principales.
- **Estilo:** sans-serif geométrica, elegida para transmitir un tono técnico pero accesible.
- **Enfoque:** busca adaptarse a un producto de monitoreo IoT dirigido a dueños de bodegas, quienes no necesariamente cuentan con conocimientos técnicos.

**Colors**

La paleta se construyó sobre un azul marino como color de marca, con dos
acentos adicionales (cian y verde menta) incorporados para reforzar
puntos de interés visual en etiquetas, testimonios y elementos
decorativos:

**Tabla 19**

*Paleta de colores y tokens de diseño de SmartStock*

<table>
<tbody>
<tr>
<th>Token</th>
<th>Valor</th>
<th>Uso</th>
</tr>
<tr>
<td>--navy</td>
<td>#082b4c</td>
<td>Titulares, marca, botón primario, foco de navegación</td>
</tr>
<tr>
<td>--blue</td>
<td>#1266d4</td>
<td>Enlaces, acentos, estado hover de botones</td>
</tr>
<tr>
<td>--cyan</td>
<td>#0ea5a8</td>
<td>Etiquetas destacadas (eyebrow) y acentos secundarios</td>
</tr>
<tr>
<td>--mint</td>
<td>#2fcf78</td>
<td>Detalles decorativos (blobs de fondo, indicador de tarjeta al hover)</td>
</tr>
<tr>
<td>--ink</td>
<td>#172033</td>
<td>Texto de cuerpo</td>
</tr>
<tr>
<td>--muted</td>
<td>#667085</td>
<td>Texto secundario / descripciones</td>
</tr>
<tr>
<td>--border</td>
<td>#dce6ef</td>
<td>Bordes y separadores</td>
</tr>
<tr>
<td>--soft</td>
<td>#f5f9fd</td>
<td>Fondos alternos de sección</td>
</tr>
</tbody>
</table>

Nota. Elaboración propia

El blanco (#ffffff) es el fondo dominante, reforzando una identidad
limpia y confiable, apropiada para un producto que maneja datos de
inventario de un negocio.

Estas decisiones se sustentan en los principios de claridad, confianza y
accesibilidad: el azul marino como color dominante transmite seriedad y
profesionalismo sin resultar frío; los acentos cian y verde menta se
reservan para elementos puntuales de refuerzo visual (etiquetas,
indicadores de interacción), evitando sobrecargar la interfaz; y el uso
del blanco como fondo dominante prioriza la legibilidad de los datos de
inventario que el producto presenta al usuario.

**Figura 20**

*Paleta de colores de SmartStock*

<img src="../assets/chapter-4/figura_020.png" style="max-height:12.9cm">
Nota. Elección y elaboración propia

**Spacing**

Para mantener una interfaz consistente y facilitar la lectura, se
establecieron criterios de espaciado y dimensiones para los componentes.

- **Border-radius:** escala de 12px como base (inputs y contenedores generales), 10px en botones y 14px en tarjetas y tablas, dando mayor presencia visual a los elementos interactivos y a los contenedores de datos.
- **Ancho máximo de contenido:** 1040px.
- **Propósito:** mantener líneas de lectura cómodas y evitar que el contenido se extienda demasiado en pantallas grandes.

**Tono de comunicación**

El tono de comunicación definido es cercano, práctico y directo,
priorizando la confianza y la facilidad de comprensión sobre el lenguaje
técnico.

- **Testimonios:** se utilizan testimonios en primera persona para generar identificación con los usuarios.
  - "Antes me enteraba de que el arroz se había acabado cuando un cliente lo pedía…"
- **Llamadas a la acción:** son directas y orientadas a la acción.
  - "Empezar prueba gratuita"
  - "Sin tarjeta · Instalación en menos de un día"
- **Enfoque:** en las cuatro dimensiones de tono definidas para el producto:
  - **Divertido – Serio:** más cerca de Serio, priorizando la confianza sobre el humor, dado que se maneja información de inventario y ventas del negocio.
  - **Formal – Casual:** más cerca de Casual, evitando lenguaje corporativo rígido para conectar con dueños de bodegas y minimarkets.
  - **Respetuoso – Irreverente:** más cerca de Respetuoso, reconociendo que el usuario no necesariamente cuenta con conocimientos técnicos y evitando minimizar sus dudas.
  - **Entusiasta – Sereno:** más cerca de Entusiasta, transmitiendo confianza y motivación para adoptar la solución.
- **Objetivo:** facilitar la comprensión del producto y conectar con los usuarios sin recurrir a tecnicismos innecesarios.

### 4.1.2. Web Style Guidelines 

- **Botones:** se definieron tres variantes: .btn como botón primario, con relleno en degradado de navy y estado hover con elevación (desplazamiento sutil hacia arriba) y sombra reforzada; .btn.ghost como botón secundario, con borde y sin relleno; y .btn.block como botón de ancho completo, utilizado en las tarjetas de planes. Las tres variantes cuentan con un estado hover definido.

**Figura 21**

*Botones del Landing Page: primario, secundario y de selección de plan*

![Figura 21](../assets/chapter-4/figura_021.png) style="width:5.05729in;height:0.56766in" /> style="width:5.01563in;height:0.39646in" />

Nota. Elaboración propia

- **Formularios:** los campos de entrada utilizan un borde de 1px y un radio de 8px. El estado de error se identifica mediante aria-invalid="true", acompañado de un borde rojo \#c0392b y un mensaje de error asociado mediante aria-describedby. La validación se ejecuta en el evento blur, en lugar de realizarse mientras el usuario escribe, evitando marcar como inválido un campo que aún se encuentra en proceso de completarse.

**Figura 22**

*Estado de error de validación en el formulario de demostración del
Landing Page*

<img src="../assets/chapter-4/figura_022.png" style="max-height:12.9cm">
Nota. Elaboración propia

- **Foco visible:** se define :focus-visible con un outline azul de 2px en toda la interfaz, facilitando la navegación mediante teclado como parte de los criterios de accesibilidad.
- **Avatares de testimonios:** cada testimonio incorpora un avatar circular con las iniciales de la persona sobre un fondo en degradado (rosa, azul o verde según el caso), reforzando la identificación visual de cada historia sin depender de fotografías reales.
- **Responsive breakpoints:** se establecen dos puntos de quiebre principales: 900px, donde las grillas de 3 o 2 columnas se reducen a una sola columna; y 720px, donde la barra de navegación se transforma en un menú hamburguesa y el botón "Crear cuenta" se incorpora dentro del menú móvil. Adicionalmente, se definieron puntos de quiebre intermedios (850px, 980px y 1180px) para ajustar con mayor precisión el espaciado y la disposición de secciones específicas como testimonios y tarjetas.
- **Reduced motion:** se respeta la configuración prefers-reduced-motion: reduce, desactivando las transiciones y animaciones para los usuarios que tienen activada esta preferencia en su sistema, como parte del compromiso de accesibilidad e inclusión declarado en el propio sitio (sección 6 de Términos y Condiciones).

## 4.2. Information Architecture 

La arquitectura de información de SmartStock integra tanto el Landing
Page como la Web Application dentro de una misma estructura, debido a
que ambos productos comparten una lógica de navegación coherente, una
misma preferencia de idioma almacenada en el navegador y un lenguaje
visual y de interacción consistente.

Ambos productos utilizan la misma preferencia de idioma mediante
localStorage, utilizando la clave smartstock.lang, lo cual permite
mantener el idioma seleccionado por el usuario al navegar entre ambos
sistemas.

**Mapa de Arquitectura de Información**

**Figura 23**

*Mapa de arquitectura de información de SmartStock*

<img src="../assets/chapter-4/figura_023.png" style="max-height:12.9cm">
Nota. Elaboración propia

El mapa de arquitectura de información representa la organización de
ambos productos y muestra también las conexiones existentes entre ellos.
Asimismo, permite identificar visualmente la navegación que ya se
encuentra implementada y aquella integración que todavía se encuentra
pendiente.

### 4.2.1. Organization Systems 

Para la organización visual del contenido, SmartStock utiliza diferentes
esquemas dependiendo del tipo de información y del flujo que realiza el
usuario.

**Organización jerárquica**

La organización jerárquica se utiliza principalmente en la Web
Application.

El Dashboard funciona como el punto central de navegación y, desde ahí,
el usuario puede acceder a las principales funcionalidades del sistema.

Dentro de la sección de productos existe una jerarquía más profunda:

**Dashboard → Productos → Detalle de producto → Vincular sensor**

Esto permite que el usuario avance desde una sección general hacia
información cada vez más específica.

Además, dentro del sidebar, las funcionalidades principales se muestran
primero, mientras que opciones secundarias como Configuración y Cerrar
sesión se encuentran ubicadas al final del menú.

**Figura 24**

*Dashboard con barra lateral de la Web Application para minimarkets*

<img src="../assets/chapter-4/figura_024.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 25**

*Pantalla de inicio de la Web Application para bodegas de barrio*

<img src="../assets/chapter-4/figura_025.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Organización secuencial**

La organización secuencial se utiliza en los procesos que requieren que
el usuario complete una serie de pasos en un orden determinado.

Por ejemplo, durante el proceso de incorporación del usuario se sigue el
siguiente flujo:

**Registro → Elección de segmento → Inicio de sesión → Registro del
primer producto**

De esta manera, el usuario es guiado paso a paso hasta comenzar a
utilizar el sistema.

Este mismo principio también se aplica en el Landing Page, cuya
información está organizada para ser recorrida de arriba hacia abajo:

**Hero → Casos de uso → Comparación → Planes → FAQ → Contacto**

**Organización matricial**

La organización matricial se utiliza principalmente en las tablas de
Productos y Comparación.

En la sección **Productos**, cada producto se relaciona con diferentes
atributos como:

- Categoría.
- Estado.
- Stock.
- Umbral.
- Sensor.

En la sección **Comparación**, cada producto se relaciona principalmente
con:

- Stock físico.
- Stock registrado.
- Diferencia entre ambos valores.

Este tipo de organización permite visualizar diferentes atributos de un
mismo producto dentro de una sola fila y aplicar filtros sin perder el
contexto de la información.

**Organización por audiencia**

La organización por audiencia representa una de las decisiones más
importantes dentro de SmartStock.

**Figura 26**

*Pantalla de creación de cuenta con selección de segmento*

<img src="../assets/chapter-4/figura_026.png" style="max-height:12.9cm">
Nota. Elaboración propia

Las funcionalidades disponibles se organizan dependiendo del segmento
seleccionado por el usuario durante el registro.

Los segmentos utilizados son:

- Bodega de barrio.
- Minimarket.

Esta diferenciación se aplica tanto en el menú lateral como en las rutas
disponibles dentro de la aplicación.

De esta manera, cada tipo de usuario visualiza únicamente las
funcionalidades correspondientes a las necesidades de su negocio.

**Organización por tópicos**

El Landing Page utiliza una organización por tópicos.

Cada sección presenta un tema específico dentro de la página, por
ejemplo:

- Casos de uso.
- Comparación.
- Planes.
- FAQ.

Estas secciones pueden ser accedidas directamente desde el menú mediante
enlaces internos.

**Organización cronológica**

La organización cronológica se utiliza en la sección de Alertas.

Los eventos más recientes aparecen primero mediante referencias de
tiempo como:

- Hace 4 min.
- Hace 12 min.
- Hace 30 min.

Esto permite que el usuario pueda identificar primero los eventos más
recientes y atender rápidamente las situaciones que puedan requerir su
atención.

**Organización alfabética**

Actualmente no se utiliza una organización alfabética dentro del
producto.

Debido a que los catálogos manejados durante el alcance actual del
proyecto son relativamente pequeños, se priorizó la organización basada
en el estado de los productos.

Por ejemplo, los productos con stock bajo pueden mostrarse antes que los
productos con niveles normales, ya que esta información resulta más
relevante para la gestión del inventario.

**Limitación actual de integración**

Actualmente existe una limitación de integración entre el Landing Page y
la Web Application.

Desde la Web Application, el usuario puede regresar hacia el Landing
Page utilizando el logo de SmartStock o mediante el enlace:

**“← Volver al sitio SmartStock”**

Sin embargo, actualmente el Landing Page todavía no redirige hacia la
Web Application.

Los siguientes botones continúan utilizando enlaces temporales href="#":

- Regístrate.
- Prueba gratis.
- Crear mi cuenta de bodega.
- Crear mi cuenta de minimarket.
- Elegir Starter.
- Elegir Growth.

Por este motivo, esta funcionalidad se considera una limitación conocida
del alcance actual del proyecto y no una integración completamente
implementada.

### 4.2.2. Labeling Systems 

Las etiquetas utilizadas en SmartStock fueron diseñadas buscando
mantener textos simples, cortos y fáciles de comprender.

**Landing Page**

En el Landing Page, las etiquetas del menú corresponden directamente con
los títulos de las diferentes secciones.

Por ejemplo:

- Casos de uso.
- Comparación.
- Planes.
- FAQ.

Estas etiquetas utilizan una o dos palabras y funcionan al mismo tiempo
como enlaces internos hacia las secciones correspondientes.

Esto evita inconsistencias entre el nombre mostrado en el menú y el
contenido al cual dirige cada opción.

**Web Application**

En la Web Application, los elementos del sidebar combinan un ícono con
una etiqueta corta.

Entre las principales etiquetas se encuentran:

- Dashboard.
- Productos.
- Sensores.
- Alertas.
- Comparación.
- Reportes.

Los íconos ayudan a complementar visualmente el significado de cada
opción, permitiendo mantener textos cortos sin perder claridad.

**Figura 27**

*Pantalla de registro de producto de la Web Application*

<img src="../assets/chapter-4/figura_027.png" style="max-height:12.9cm">
Nota. Elaboración propia

Además, tanto el Landing Page como la Web Application se encuentran
disponibles en inglés y español.

Ambos productos comparten la misma preferencia de idioma mediante:

localStorage

Clave utilizada:

smartstock.lang

Esto permite que el idioma seleccionado por el usuario permanezca activo
al desplazarse entre ambos productos.

**Diferencia de etiquetado según el segmento**

Existe una diferencia intencional en la etiqueta utilizada para la ruta
interna \#dashboard.

Para usuarios del segmento **Bodega de barrio**, esta sección se
denomina:

**Inicio**

Mientras que para los usuarios del segmento **Minimarket**, la misma
sección se denomina:

**Dashboard**

Esta diferencia fue implementada de manera intencional para utilizar una
terminología más sencilla en el segmento de negocio más pequeño.

### 4.2.3. SEO Tags and Meta Tags 

**Landing Page**

El Landing Page incluye las principales etiquetas SEO y Meta Tags
solicitadas.

Tanto index.html como terms-of-service.html cuentan con:

- \<title\>
- \<meta name="description"\>
- \<meta name="keywords"\>
- \<meta name="author"\>

La etiqueta \<title\> contiene un título descriptivo de la página.

La etiqueta \<meta name="description"\> contiene una descripción del
contenido y puede mostrarse de acuerdo con el idioma seleccionado.

La etiqueta \<meta name="keywords"\> contiene términos relacionados con
el proyecto como:

- minimarket.
- corner store.
- SmartStock.
- InventiaStock.

Finalmente, la etiqueta de autor utiliza:

\<meta name="author" content="InventiaStock"\>

**Web Application**

ctualmente, la Web Application cuenta únicamente con la etiqueta
\<title\>. Por ello, se identificó la necesidad de incorporar las
etiquetas de descripción, palabras clave y autor para completar la
configuración de SEO y Meta Tags.

Se propone agregar las siguientes etiquetas:

\<meta name="description" content="SmartStock Web Application — gestiona
tu inventario monitoreado por sensores IoT, alertas y comparaciones de
stock."\>

\<meta name="keywords" content="SmartStock, Inventia, gestión de
inventario, sensores IoT, monitoreo de stock"\>

\<meta name="author" content="Inventia"\>

De manera opcional, también puede utilizarse:

\<meta name="robots" content="noindex"\>

Esta etiqueta puede emplearse para indicar que la Web Application, al
tratarse de un sistema protegido o autenticado, no está destinada a ser
indexada por los motores de búsqueda.

### 4.2.4. Searching Systems 

El sistema de búsqueda de SmartStock se encuentra implementado
principalmente dentro de la Web Application, mientras que el Landing
Page no requiere un mecanismo de búsqueda debido a su estructura de
navegación por secciones.

**Landing Page**

El Landing Page no incorpora un sistema de búsqueda, debido a que
presenta una estructura de una sola página con secciones claramente
diferenciadas y un menú superior que permite acceder directamente a cada
una de ellas.

**Web Application**

La Web Application incorpora sistemas de búsqueda y filtrado en las
secciones de Productos, Comparación y Alertas, permitiendo al usuario
localizar información específica de manera más rápida.

**Productos**

La sección Productos dispone de un campo de búsqueda que filtra los
resultados en tiempo real.

La búsqueda puede realizarse utilizando:

- Nombre del producto.
- Categoría.

Además, el buscador puede combinarse con un filtro de estado que
contiene las siguientes opciones:

- Todos los estados.
- Stock bajo.
- Normal.
- Sin sensor.

**Figura 28**

*Sección Productos con búsqueda y filtro por estado*

<img src="../assets/chapter-4/figura_028.png" style="max-height:12.9cm">
Nota. Elaboración propia

Después de realizar una búsqueda, las filas que no coinciden con los
criterios ingresados se ocultan.

Las filas que sí coinciden continúan mostrando toda su información
correspondiente, como:

- Imagen.
- Categoría.
- Stock.
- Umbral.
- Sensor.
- Estado.

De esta manera, el usuario puede encontrar rápidamente un producto sin
perder información relevante de los resultados encontrados.

**Comparación**

La sección Comparación incorpora un sistema de búsqueda por prefijo y
filtros que permiten organizar los productos según su situación.

Los filtros disponibles son:

- Todos.
- Con discrepancia.
- Sin discrepancia.

Después de realizar una búsqueda o aplicar un filtro, el sistema
recalcula automáticamente:

- El número de productos visibles.
- El número de productos que superan el 10 % de diferencia entre el stock registrado y el stock físico.

Esto permite que los indicadores mostrados se mantengan consistentes con
los resultados actualmente visibles.

**Figura 29**

*Sección Comparación con búsqueda y filtro de discrepancias*

<img src="../assets/chapter-4/figura_029.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Alertas**

La sección Alertas utiliza pestañas que funcionan como filtros por
categoría.

Las opciones disponibles son:

- Todas.
- Stock bajo.
- Discrepancias.
- Sensores.

Los contadores de cada categoría se actualizan según las alertas
disponibles. Cada alerta conserva información relevante como:

- Icono.
- Mensaje.
- Tiempo relativo desde su generación

**Figura 30**

*Sección Alertas con pestañas por categoría*

<img src="../assets/chapter-4/figura_030.png" style="max-height:12.9cm">
Nota. Elaboración propia

### 4.2.5. Navigation Systems 

SmartStock utiliza diferentes sistemas de navegación para facilitar el
desplazamiento del usuario tanto dentro del Landing Page como dentro de
la Web Application.

**Landing Page**

El Landing Page utiliza un menú superior persistente como sistema de
navegación global. Este menú permite acceder directamente a las
diferentes secciones de la página mediante enlaces internos.

También se cuenta con un pie de página que incorpora navegación
contextual mediante enlaces legales, información secundaria y enlaces a
redes sociales.

La navegación mediante anclas permite acceder directamente a secciones
como:

- Casos de uso.
- Comparación.
- Planes.
- FAQ.
- Contacto.

**Web Application**

La Web Application utiliza un sidebar persistente como sistema de
navegación global.

Las opciones disponibles dentro del sidebar cambian dependiendo del
segmento del usuario.

Para pantallas pequeñas se utiliza un menú hamburguesa que contiene las
mismas opciones disponibles en el menú lateral.

La barra superior también incorpora diferentes elementos de navegación y
orientación, entre ellos:

- Selector de idioma.
- Campana de notificaciones.
- Contador de notificaciones no leídas.
- Nombre del negocio.
- Tipo de negocio.
- Avatar con las iniciales del usuario.

La campana de notificaciones permite acceder directamente hacia la
sección de Alertas.

El bloque que contiene la información del negocio funciona además como
un indicador de identidad, ayudando al usuario a reconocer qué cuenta y
qué tipo de negocio está utilizando.

Dentro del Detalle de producto también se proporciona contexto adicional
mediante una navegación similar a un breadcrumb:

**Figura 31**

*Sección Sensores IoT de la Web Application*

<img src="../assets/chapter-4/figura_031.png" style="max-height:12.9cm">
Nota. Elaboración propia

Esto permite identificar la ubicación actual dentro de la aplicación y
regresar hacia niveles anteriores.

**Navegación entre el Landing Page y la Web Application**

Actualmente, la Web Application permite regresar al Landing Page
mediante:

- El logotipo de SmartStock.
- La opción ← Volver al sitio SmartStock.

**Figura 32**

*Pantalla de inicio de sesión de la Web Application*

<img src="../assets/chapter-4/figura_032.png" style="max-height:12.9cm">
Nota. Elaboración propia

Sin embargo, desde el Landing Page todavía no existe una conexión
funcional hacia la Web Application, debido a que los principales botones
Call to Action continúan utilizando enlaces temporales.

Esta situación se considera una limitación conocida correspondiente al
estado actual del proyecto.

## 4.3. Landing Page UI Design 

El diseño de la interfaz de usuario (UI) de la página de inicio de
SmartStock es clave para captar la atención de los administradores y
propietarios de bodegas y minimarkets, ya que los guía hacia una acción
clara: comprender y adoptar una solución inteligente de gestión de
inventarios. Se ha priorizado una experiencia continua, de modo que cada
elemento de la página sea accesible, interactivo y fácil de usar,
transmitiendo confianza, mientras refleja el compromiso de SmartStock
con la innovación tecnológica y la claridad en la comunicación.

### 4.3.1. Landing Page Wireframe 

El wireframe de SmartStock organiza de forma clara la página de inicio,
mostrando la secuencia lógica de secciones: desde el problema de la
gestión del inventario, pasando por las funcionalidades principales,
hasta los beneficios que ofrece la plataforma.

- **Desktop:**

**Figura 33**

*Interfaz principal de bienvenida del landing page de SmartStock*

<img src="../assets/chapter-4/figura_033.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura principal de inicio del landing page de
SmartStock en versión de escritorio.

**Figura 34**

*Interfaz sección de problemas y beneficios de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_034.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura de la sección de problemas y beneficios
de SmartStock en versión de escritorio.

**Figura 35**

*Interfaz de la sección de casos de uso de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_035.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura de la sección de casos de uso de
SmartStock en versión de escritorio.

**Figura 36**

*Interfaz de la sección comparativa de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_036.png" style="max-height:12.9cm">
Nota. Estructura de la sección comparativa de SmartStock en versión de
escritorio.

**Figura 37**

*Interfaz de la sección de planes de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_037.png" style="max-height:12.9cm">
Nota. Estructura de la sección de planes de SmartStock en versión de
escritorio.

**Figura 38**

*Interfaz de la sección de testimonios de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_038.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura de la sección de testimonios de
SmartStock en versión de escritorio.

**Figura 39**

*Interfaz de la sección de preguntas frecuentes de SmartStock en versión
de escritorio*

<img src="../assets/chapter-4/figura_039.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura de la sección de preguntas frecuentes
de SmartStock en versión de escritorio.

**Figura 40**

*Interfaz del formulario de demostración de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_040.png" style="max-height:12.9cm">
Nota. Wireframe de la estructura del formulario de demostración de
SmartStock en versión de escritorio.

**Figura 41**

*Pie de página del landing page de SmartStock*

![Figura 41](../assets/chapter-4/figura_041.png)

Nota. Wireframe del pie de página del landing page de SmartStock

- **Mobile:**

**Figura 42**

*Interfaz de la interfaz principal de inicio de SmartStock en versión
móvil*

![Figura 42](../assets/chapter-4/figura_042.png)

Nota. Wireframe de la estructura principal de inicio del landing page de
SmartStock adaptada para dispositivos móviles.

**Figura 43**

*Interfaz de la sección de problemas y beneficios de SmartStock en
versión móvil*

![Figura 43](../assets/chapter-4/figura_043.png)

Nota. Wireframe de la estructura de la sección de problemas y beneficios
de SmartStock adaptada para dispositivos móviles.

**Figura 44**

*Interfaz de la sección de casos de uso de SmartStock en versión móvil*

![Figura 44](../assets/chapter-4/figura_044.png)

Nota. Wireframe de la estructura de la sección de casos de uso de
SmartStock adaptada para dispositivos móviles.

**Figura 45**

*Interfazde la sección comparativa de SmartStock en versión móvil*

![Figura 45](../assets/chapter-4/figura_045.png)

Nota. Estructura de la sección comparativa de SmartStock adaptada para
dispositivos móviles.

**Figura 46**

*Interfaz de la sección de planes de SmartStock en versión móvil*

![Figura 46](../assets/chapter-4/figura_046.png)

Nota. Estructura de la sección de planes de SmartStock adaptada para
dispositivos móviles.

**Figura 47**

*Interfazde la sección de testimonios de SmartStock en versión móvil*

![Figura 47](../assets/chapter-4/figura_047.png)

Nota. Wireframe de la estructura de la sección de testimonios de
SmartStock adaptada para dispositivos móviles.

**Figura 48**

*Interfaz de la sección de preguntas frecuentes de SmartStock en versión
móvil*

![Figura 48](../assets/chapter-4/figura_048.png)

Nota. Estructura de la sección de preguntas frecuentes adaptada para
dispositivos móviles.

**Figura 49**

*Interfaz del formulario de demostración de SmartStock en versión móvil*

![Figura 49](../assets/chapter-4/figura_049.png)

Nota. Estructura del formulario de demostración de SmartStock adaptada
para celulares

**Figura 50**

*Interfaz del menú de navegación de SmartStock en versión móvil*

![Figura 50](../assets/chapter-4/figura_050.png)

Nota.Wireframe de la estructura del menú de navegación de SmartStock
adaptado para dispositivos móviles.

### 4.3.2. Landing Page Mock-up 

El mock-up de la página de inicio de SmartStock actúa como un mapa
visual que organiza la estructura y el flujo de la información, mientras
cada sección conduce al usuario desde la identificación del problema
hasta la presentación de las funcionalidades y beneficios de la
plataforma.

- **Desktop:**

**Figura 51**

*Interfaz principal de inicio del landing page de SmartStock en versión
de escritorio*

<img src="../assets/chapter-4/figura_051.png" style="max-height:12.9cm">
Nota. Interfaz principal de inicio del landing page de SmartStock en
versión de escritorio.

**Figura 52**

*Interfaz de problemas y beneficios de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_052.png" style="max-height:12.9cm">
Nota. Interfaz de problemas y beneficios de SmartStock en versión de
escritorio.

**Figura 53**

*Interfaz de casos de uso de SmartStock en versión de escritorio*

<img src="../assets/chapter-4/figura_053.png" style="max-height:12.9cm">
Nota. Mockup de la interfaz de casos de uso de SmartStock en versión de
escritorio.

**Figura 54**

*Interfaz de planes de SmartStock en versión de escritorio*

<img src="../assets/chapter-4/figura_054.png" style="max-height:12.9cm">
Nota. Mockup de la interfaz de planes de SmartStock en versión de
escritorio.

**Figura 55**

*Interfaz principal de bienvenida del landing page de SmartStock*

<img src="../assets/chapter-4/figura_055.png" style="max-height:12.9cm">
Nota. Imagen de la interfaz principal de bienvenida del landing page de
SmartStock

**Figura 56**

*Interfaz de testimonios de SmartStock en versión de escritorio*

<img src="../assets/chapter-4/figura_056.png" style="max-height:12.9cm">
Nota. Mockup de la interfaz de testimonios de SmartStock en versión de
escritorio.

**Figura 57**

*Interfaz de preguntas frecuentes de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_057.png" style="max-height:12.9cm">
Nota. Mockup de la interfaz de preguntas frecuentes de SmartStock en
versión de escritorio.

**Figura 58**

*Interfaz del formulario de demostración de SmartStock en versión de
escritorio*

<img src="../assets/chapter-4/figura_058.png" style="max-height:12.9cm">
Nota. Interfaz del formulario de demostración de SmartStock en versión
de escritorio.

**Figura 59**

*Pie de página de la verizon de escritorio de SmartStock*

![Figura 59](../assets/chapter-4/figura_059.png)

*Nota*. Mockup del pie de página de SmartStock

- **Mobile:**

**Figura 60**

*Interfaz principal de inicio del landing page de SmartStock en versión
móvil*

![Figura 60](../assets/chapter-4/figura_060.png)

*Nota*. Mockup de la interfaz principal de inicio del landing page de
SmartStock adaptada para dispositivos móviles.

**Figura 61**

*Interfaz de problemas y beneficios de SmartStock en versión de móvil*

![Figura 61](../assets/chapter-4/figura_061.png)

*Nota*. Mockup de la interfaz de problemas y beneficios de SmartStock
adaptada para dispositivos móviles.

**Figura 62**

*Interfaz de casos de uso de SmartStock en versión móvil*

![Figura 62](../assets/chapter-4/figura_062.png)

*Nota*. Mockup de la interfaz de casos de uso de SmartStock para
dispositivos móviles.

**Figura 63**

*Interfaz comparativa de SmartStock en versión móvil*

![Figura 63](../assets/chapter-4/figura_063.png)

*Nota*. Mockup de la interfaz comparativa de SmartStock adaptada para
dispositivos móviles.

**Figura 64**

*Interfaz de planes de SmartStock en versión móvil*

![Figura 64](../assets/chapter-4/figura_064.png)

*Nota*. Mockup de la interfaz de planes de SmartStock adaptada para
dispositivos móviles.

**Figura 65**

*Interfaz de testimonios de SmartStock en versión de escritorio*

![Figura 65](../assets/chapter-4/figura_065.png)

*Nota*. Mockup de la interfaz de testimonios de SmartStock para
dispositivos móviles.

**Figura 66**

*Interfaz de preguntas frecuentes de SmartStock en versión de
escritorio*

![Figura 66](../assets/chapter-4/figura_066.png)

*Nota*. Mockup de la interfaz de preguntas frecuentes de SmartStock
adaptada para dispositivos móviles.

**Figura 67**

*Interfaz del formulario de demostración de SmartStock en versión de
escritorio*

![Figura 67](../assets/chapter-4/figura_067.png)

*Nota*. Mockup de la interfaz del formulario de demostración de
SmartStock adaptada para dispositivos móviles.

**Figura 68**

*Interfaz del menú de navegación de SmartStock en versión móvil*

![Figura 68](../assets/chapter-4/figura_068.png)

Nota. Mockup del menú de navegación del landing page de SmartStock
adaptado para dispositivos móviles.

## 4.4. Web Applications UX/UI Design 

En esta sección se presentan los wireframes, wireflows, mock-ups y
diagramas de flujo de usuario desarrollados para los dos segmentos
objetivo de SmartStock: propietarios y administradores de minimarkets, y
propietarios y administradores de bodegas de barrio. A través de estos
artefactos visuales, se detalla la arquitectura de la información y la
experiencia de interacción diseñada para optimizar la gestión diaria del
inventario. Asimismo, se evidencia cómo cada interfaz ha sido adaptada a
las necesidades operativas y al nivel de digitalización particular de
cada tipo de negocio, garantizando una navegación intuitiva y eficiente.

### 4.4.1. Web Applications Wireframes 

- **Dueños y administradores de Minimarkets**

**Figura 69**

*Wireframe 1 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_069.png" style="max-height:12.9cm">
*Nota*. Elaboración propia.

**Figura 70**

*Wireframe 2 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_070.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 71**

*Wireframe 3 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_071.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 72**

*Wireframe 4 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_072.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 73**

*Wireframe 5 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_073.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 74**

*Wireframe 6 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_074.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 75**

*Wireframe 7 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_075.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 76**

*Wireframe 8 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_076.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 77**

*Wireframe 9 de la aplicación web para propietarios y administradores de
minimarkets*

<img src="../assets/chapter-4/figura_077.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 78**

*Wireframe 10 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_078.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 79**

*Wireframe 11 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_079.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 80**

*Wireframe 12 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_080.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 81**

*Wireframe 13 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_081.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 82**

*Wireframe 14 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_082.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 83**

*Wireframe 15 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_083.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 84**

*Wireframe 16 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_084.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 85**

*Wireframe 17 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_085.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 86**

*Wireframe 18 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_086.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 87**

*Wireframe 19 de la aplicación web para propietarios y administradores
de minimarkets*

<img src="../assets/chapter-4/figura_087.png" style="max-height:12.9cm">
Nota. Elaboración propia.

- **Dueños y administradores de Bodegas**

**Figura 88**

*Wireframe 1 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_088.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 89**

*Wireframe 2 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_089.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 90**

*Wireframe 3 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_090.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 91**

*Wireframe 4 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_091.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 92**

*Wireframe 5 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_092.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 93**

*Wireframe 6 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_093.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 94**

*Wireframe 7 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_094.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 95**

*Wireframe 8 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_095.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 96**

*Wireframe 9 de la aplicación web para propietarios y administradores de
bodegas de barrio*

<img src="../assets/chapter-4/figura_096.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 97**

*Wireframe 10 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_097.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 98**

*Wireframe 11 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_098.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 99**

*Wireframe 12 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_099.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 100**

*Wireframe 13 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_100.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 101**

*Wireframe 14 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_101.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 102**

*Wireframe 15 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_102.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 103**

*Wireframe 16 de la aplicación web para propietarios y administradores
de bodegas de barrio*

<img src="../assets/chapter-4/figura_103.png" style="max-height:12.9cm">
Nota. Elaboración propia.

### 4.4.2. Web Applications Wireflow Diagrams 

Los wireflows ilustran las rutas de navegación entre pantallas según
cada segmento. Cada diagrama parte de un objetivo del usuario (User
Goal), identifica las pantallas con su código e indica la ruta esperada
en azul y las alternativas o de error en rojo discontinuo, acompañándose
de una breve explicación y su condición principal.

Se elaboraron wireflows para los dos segmentos objetivo de SmartStock:
propietarios y administradores de minimarkets, y de bodegas de barrio.
Por extensión, este informe incluye únicamente los flujos centrales del
producto (acceso, catálogo, monitoreo de stock con sensores IoT,
compras, ventas y alertas de reposición). El conjunto completo puede
consultarse en el siguiente enlace.

Link:<a href="https://www.figma.com/board/Tdon4igryTEOc1wl7f5I15/Wireflow-diagrams-SmartStock?node-id=0-1&t=ik1xWHtOIA29fNXh-1" style="color:#2563eb">https://www.figma.com/board/Tdon4igryTEOc1wl7f5I15/Wireflow-diagrams-SmartStock?node-id=0-1&t=ik1xWHtOIA29fNXh-1</a>

- **Dueños y administradores de Minimarkets**

Para este segmento se presentan 11 wireflows, que cubren el acceso a la
cuenta, la gestión del catálogo, el monitoreo del stock con sensores
IoT, el registro de compras, ventas y proveedores, y la reposición desde
una alerta de stock bajo. Las pantallas se adaptan al tipo de negocio,
de modo que el menú y las funciones disponibles corresponden al segmento
de bodegas.

**Figura 104**

*Wireflow 1 de la aplicación web para propietarios y administradores de
minimarkets: iniciar sesión (US02)*

<img src="../assets/chapter-4/figura_104.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 105**

*Wireflow 2 de la aplicación web para propietarios y administradores de
minimarkets: registrar una cuenta (US01)*

<img src="../assets/chapter-4/figura_105.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 106**  
*Wireflow 3 de la aplicación web para propietarios y administradores de
minimarkets: consultar el resumen del negocio y navegar a sus módulos
(US15)*

<img src="../assets/chapter-4/figura_106.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 107**

*Wireflow 4 de la aplicación web para propietarios y administradores de
minimarkets: registrar un producto en el catálogo (US13)*

<img src="../assets/chapter-4/figura_107.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 108**

*Wireflow 5 de la aplicación web para propietarios y administradores de
minimarkets: consultar el stock de un producto y su peso en el sensor
(US07, US08, US06)*

<img src="../assets/chapter-4/figura_108.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 109**

*Wireflow 6 de la aplicación web para propietarios y administradores de
minimarkets: vincular un sensor IoT a un producto (US04)*

<img src="../assets/chapter-4/figura_109.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 110**

*Wireflow 7 de la aplicación web para propietarios y administradores de
minimarkets: configurar el umbral mínimo de stock (US05)*

<img src="../assets/chapter-4/figura_110.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 111**

*Wireflow 8 de la aplicación web para propietarios y administradores de
minimarkets: registrar una compra (US30)*

<img src="../assets/chapter-4/figura_111.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 112**

*Wireflow 9 de la aplicación web para propietarios y administradores de
minimarkets: registrar una venta (US26)*

<img src="../assets/chapter-4/figura_112.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 113**

*Wireflow 10 de la aplicación web para propietarios y administradores de
minimarkets: registrar un proveedor (US211)*

<img src="../assets/chapter-4/figura_113.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 114**

*Wireflow 11 de la aplicación web para propietarios y administradores de
minimarkets: reponer un producto desde una alerta de stock bajo (US32)*

<img src="../assets/chapter-4/figura_114.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 115**

*Wireflow 12 de la aplicación web para propietarios y administradores de
minimarkets: comparar el inventario físico con el registrado (US11,
US12)*

<img src="../assets/chapter-4/figura_115.png" style="max-height:12.9cm">
Nota. Elaboración propia.

- **Dueños y administradores de Bodegas**

Para este segmento se presentan 11 wireflows. Son los mismos flujos que
en minimarkets, salvo la comparación entre inventario físico y
registrado, que no forma parte del recorrido de este segmento. Las
pantallas se adaptan al tipo de negocio, de modo que cambian el menú y
las funciones disponibles.

**Figura 116**

*Wireflow 1 de la aplicación web para propietarios y administradores de
bodegas de barrio: iniciar sesión (US02)*

<img src="../assets/chapter-4/figura_116.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 117**

*Wireflow 2 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una cuenta (US01)*

<img src="../assets/chapter-4/figura_117.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 118**

*Wireflow 3 de la aplicación web para propietarios y administradores de
bodegas de barrio: consultar el resumen del negocio y navegar a sus
módulos (US15)*

<img src="../assets/chapter-4/figura_118.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 119**

*Wireflow 4 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar un producto en el catálogo (US13)*

<img src="../assets/chapter-4/figura_119.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 120**

*Wireflow 5 de la aplicación web para propietarios y administradores de
bodegas de barrio: consultar el stock de un producto y su peso en el
sensor (US07, US08, US06)*

<img src="../assets/chapter-4/figura_120.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 121**

*Wireflow 6 de la aplicación web para propietarios y administradores de
bodegas de barrio: vincular un sensor IoT a un producto (US04)*

<img src="../assets/chapter-4/figura_121.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 122**

*Wireflow 7 de la aplicación web para propietarios y administradores de
bodegas de barrio: configurar el umbral mínimo de stock (US05)*

<img src="../assets/chapter-4/figura_122.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 123**

*Wireflow 8 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una compra (US30)*

<img src="../assets/chapter-4/figura_123.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 124**

*Wireflow 9 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una venta (US26)*

<img src="../assets/chapter-4/figura_124.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 125**

*Wireflow 10 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar un proveedor (US29)*

<img src="../assets/chapter-4/figura_125.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 126**

*Wireflow 11 de la aplicación web para propietarios y administradores de
bodegas de barrio: reponer un producto desde una alerta de stock bajo
(US32)*

<img src="../assets/chapter-4/figura_126.png" style="max-height:12.9cm">
Nota. Elaboración propia.

### 4.4.3. Web Applications Mock-ups 

- **Dueños y administradores de minimarkets**

**Figura 127**

*Mock-up 1 de la aplicación web para propietarios y administradores
de minimarkets: registro de cuenta (US01)*
<img src="../assets/chapter-4/figura_127.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 128**

*Mock-up 2 de la aplicación web para propietarios y administradores
de minimarkets: inicio de sesión (US02)*
<img src="../assets/chapter-4/figura_128.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 129**

*Mock-up 3 de la aplicación web para propietarios y administradores
de minimarkets: inicio de sesión con credenciales incorrectas (US02)*
<img src="../assets/chapter-4/figura_129.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 130**

*Mock-up 4 de la aplicación web para propietarios y administradores
de minimarkets: dashboard inicial del negocio (US15)*
<img src="../assets/chapter-4/figura_130.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 131**

*Mock-up 5 de la aplicación web para propietarios y administradores
de minimarkets: catálogo de productos sin registros (US07)*
<img src="../assets/chapter-4/figura_131.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 132**

*Mock-up 6 de la aplicación web para propietarios y administradores
de minimarkets: formulario para registrar un producto (US13)*
<img src="../assets/chapter-4/figura_132.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 133**

*Mock-up 7 de la aplicación web para propietarios y administradores
de minimarkets: catálogo con el producto registrado (US07)*
<img src="../assets/chapter-4/figura_133.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 134**

*Mock-up 8 de la aplicación web para propietarios y administradores
de minimarkets: detalle de un producto y nivel de stock (US08)*
<img src="../assets/chapter-4/figura_134.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 135**

*Mock-up 9 de la aplicación web para propietarios y administradores
de minimarkets: listado de sensores IoT (US06)*
<img src="../assets/chapter-4/figura_135.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 136**

*Mock-up 10 de la aplicación web para propietarios y administradores
de minimarkets: vincular un sensor a un producto (US04)*
<img src="../assets/chapter-4/figura_136.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 137**

*Mock-up 11 de la aplicación web para propietarios y administradores
de minimarkets: confirmación de sensor vinculado (US04)*
<img src="../assets/chapter-4/figura_137.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 138**

*Mock-up 12 de la aplicación web para propietarios y administradores
de minimarkets: alertas, vista de todas*
<img src="../assets/chapter-4/figura_138.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 139**

*Mock-up 13 de la aplicación web para propietarios y administradores
de minimarkets: alertas de stock bajo*
<img src="../assets/chapter-4/figura_139.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 140**

*Mock-up 14 de la aplicación web para propietarios y administradores
de minimarkets: alertas de discrepancias de inventario*
<img src="../assets/chapter-4/figura_140.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 141**

*Mock-up 15 de la aplicación web para propietarios y administradores
de minimarkets: alertas de sensores*
<img src="../assets/chapter-4/figura_141.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 142**

*Mock-up 16 de la aplicación web para propietarios y administradores
de minimarkets: comparación del inventario físico con el registrado
(US11, US12)  

<img src="../assets/chapter-4/figura_142.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 143**

*Mock-up 17 de la aplicación web para propietarios y administradores
de minimarkets: reportes de consumo (US25)*
<img src="../assets/chapter-4/figura_143.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 144**

*Mock-up 18 de la aplicación web para propietarios y administradores
de minimarkets: configuración del negocio*
<img src="../assets/chapter-4/figura_144.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 145**

*Mock-up 19 de la aplicación web para propietarios y administradores
de minimarkets: confirmación de cambios en la configuración*
<img src="../assets/chapter-4/figura_145.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

- **Dueños y administradores de Bodegas**

**Figura 146**

*Mock-up 1 de la aplicación web para propietarios y administradores
de bodegas de barrio: registro de cuenta (US01)  

<img src="../assets/chapter-4/figura_146.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 147**

*Mock-up 2 de la aplicación web para propietarios y administradores
de bodegas de barrio: inicio de sesión (US02)  

<img src="../assets/chapter-4/figura_147.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 148**

*Mock-up 3 de la aplicación web para propietarios y administradores
de bodegas de barrio: pantalla de inicio “Mi inventario” (US15)  

<img src="../assets/chapter-4/figura_148.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 149**

*Mock-up 4 de la aplicación web para propietarios y administradores
de bodegas de barrio: catálogo de productos sin registros (US07)  

<img src="../assets/chapter-4/figura_149.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 150**

*Mock-up 5 de la aplicación web para propietarios y administradores
de bodegas de barrio: formulario para registrar un producto (US13)  

<img src="../assets/chapter-4/figura_150.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 151**

*Mock-up 6 de la aplicación web para propietarios y administradores
de bodegas de barrio: catálogo con el producto registrado (US07)  

<img src="../assets/chapter-4/figura_151.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 152**

*Mock-up 7 de la aplicación web para propietarios y administradores
de bodegas de barrio: detalle de un producto y nivel de stock (US08)  

<img src="../assets/chapter-4/figura_152.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 153**

*Mock-up 8 de la aplicación web para propietarios y administradores
de bodegas de barrio: alertas, vista de todas  

<img src="../assets/chapter-4/figura_153.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 154**

*Mock-up 9 de la aplicación web para propietarios y administradores
de bodegas de barrio: alertas de stock bajo  

<img src="../assets/chapter-4/figura_154.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 155**

*Mock-up 10 de la aplicación web para propietarios y administradores
de bodegas de barrio: alertas de sensores  

<img src="../assets/chapter-4/figura_155.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 156**

*Mock-up 11 de la aplicación web para propietarios y administradores
de bodegas de barrio: listado de sensores IoT (US06)  

<img src="../assets/chapter-4/figura_156.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 157**

*Mock-up 12 de la aplicación web para propietarios y administradores
de bodegas de barrio: vincular un sensor a un producto (US04)  

<img src="../assets/chapter-4/figura_157.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 158**

*Mock-up 13 de la aplicación web para propietarios y administradores
de bodegas de barrio: confirmación de sensor vinculado (US04)  

<img src="../assets/chapter-4/figura_158.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 159**

*Mock-up 14 de la aplicación web para propietarios y administradores
de bodegas de barrio: configuración del negocio  

<img src="../assets/chapter-4/figura_159.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

**Figura 160**

*Mock-up 15 de la aplicación web para propietarios y administradores
de bodegas de barrio: confirmación de cambios en la configuración  

<img src="../assets/chapter-4/figura_160.png" style="max-height:12.9cm">
*Nota.* Elaboración propia.

### 4.4.4. Web Applications User Flow Diagrams 

Los user flows muestran el recorrido que sigue el usuario para lograr un
objetivo concreto dentro de la aplicación según su segmento. Cada
diagrama parte de un User Goal, identifica las pantallas por código y
diferencia la ruta esperada (línea azul) de las alternativas o de error
(línea roja discontinua), acompañándose de una explicación y su
condición principal.

Se diseñaron flujos para los dos segmentos de SmartStock: propietarios y
administradores de minimarkets, y de bodegas de barrio. Por extensión,
este informe presenta únicamente los que cubren las funciones centrales
(acceso, catálogo, monitoreo de stock con sensores IoT, compras, ventas
y alertas de reposición). El conjunto completo puede consultarse en el
siguiente enlace.

Link:<a href="https://www.figma.com/board/Q4SExEhBOi9wb1iWULW9ce/User-Flow-diagrams-SmartStock?node-id=0-1&t=GD9ioBq6MAOymx5J-1" style="color:#2563eb">https://www.figma.com/board/Q4SExEhBOi9wb1iWULW9ce/User-Flow-diagrams-SmartStock?node-id=0-1&t=GD9ioBq6MAOymx5J-1</a>

- **Dueños y administradores de Minimarkets**

Para este segmento se presentan 12 user flows. Los de acceso
corresponden al inicio de sesión y al registro de la cuenta; los de
gestión, al registro de productos, la consulta del stock, la vinculación
de sensores y la configuración del umbral mínimo; y los de operación, al
registro de compras, ventas y proveedores, la reposición desde una
alerta y la comparación entre el inventario físico y el registrado.

**Figura 161**

*User Flow 1 de la web para propietarios de minimarkets: iniciar sesión
(US02)*

<img src="../assets/chapter-4/figura_161.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 162**

*User Flow 2 de la aplicación web para propietarios y administradores de
minimarkets: registrar una cuenta (US01)*

<img src="../assets/chapter-4/figura_162.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 163**

*User Flow 3 de la aplicación web para propietarios y administradores de
minimarkets: consultar el resumen del negocio y navegar a sus módulos
(US15)*

<img src="../assets/chapter-4/figura_163.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 164**

*User Flow 4 de la aplicación web para propietarios y administradores de
minimarkets: registrar un producto en el catálogo (US13)*

<img src="../assets/chapter-4/figura_164.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 165**

*User Flow 5 de la aplicación web para propietarios y administradores de
minimarkets: consultar el stock de un producto y su peso en el sensor
(US07, US08, US06)*

<img src="../assets/chapter-4/figura_165.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 166**

*User Flow 6 de la aplicación web para propietarios y administradores de
minimarkets: vincular un sensor IoT a un producto (US04)*

<img src="../assets/chapter-4/figura_166.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 167**

*User Flow 7 de la aplicación web para propietarios y administradores de
minimarkets: configurar el umbral mínimo de stock (US05)*

<img src="../assets/chapter-4/figura_167.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 168**

*User Flow 8 de la aplicación web para propietarios y administradores de
minimarkets: registrar una compra (US30)*

<img src="../assets/chapter-4/figura_168.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 169**

*User Flow 9 de la aplicación web para propietarios y administradores de
minimarkets: registrar una venta (US26)*

<img src="../assets/chapter-4/figura_169.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 170**

*User Flow 10 de la aplicación web para propietarios y administradores
de minimarkets: registrar un proveedor (US29)*

<img src="../assets/chapter-4/figura_170.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 171**

*User Flow 11 de la aplicación web para propietarios y administradores
de minimarkets: reponer un producto desde una alerta de stock bajo
(US32)*

<img src="../assets/chapter-4/figura_171.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 172**

*User Flow 12 de la aplicación web para propietarios y administradores
de minimarkets: comparar el inventario físico con el registrado (US11,
US12)*

<img src="../assets/chapter-4/figura_172.png" style="max-height:12.9cm">
Nota. Elaboración propia.

- **Dueños y administradores de Bodegas**

Para este segmento se presentan 11 user flows, que cubren el acceso a la
cuenta, la gestión del catálogo, el monitoreo del stock con sensores
IoT, el registro de compras, ventas y proveedores, y la reposición desde
una alerta de stock bajo. Las pantallas se adaptan al tipo de negocio,
de modo que el menú y las funciones disponibles corresponden al segmento
de bodegas.

**Figura 173**

*User Flow 1 de la aplicación web para propietarios y administradores de
bodegas de barrio: iniciar sesión (US02)*

<img src="../assets/chapter-4/figura_173.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 174**

*User Flow 2 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una cuenta (US01)*

<img src="../assets/chapter-4/figura_174.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 175**

*User Flow 3 de la aplicación web para propietarios y administradores de
bodegas de barrio: consultar el resumen del negocio y navegar a sus
módulos (US15)*

<img src="../assets/chapter-4/figura_175.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 176**

*User Flow 4 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar un producto en el catálogo (US13)*

<img src="../assets/chapter-4/figura_176.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 177**

*User Flow 5 de la aplicación web para propietarios y administradores de
bodegas de barrio: consultar el stock de un producto y su peso en el
sensor (US07, US08, US06)*

<img src="../assets/chapter-4/figura_177.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 178**

*User Flow 6 de la aplicación web para propietarios y administradores de
bodegas de barrio: vincular un sensor IoT a un producto (US04)*

<img src="../assets/chapter-4/figura_178.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 179**

*User Flow 7 de la aplicación web para propietarios y administradores de
bodegas de barrio: configurar el umbral mínimo de stock (US05)*

<img src="../assets/chapter-4/figura_179.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 180**

*User Flow 8 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una compra (US30)*

<img src="../assets/chapter-4/figura_180.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 181**

*User Flow 9 de la aplicación web para propietarios y administradores de
bodegas de barrio: registrar una venta (US26)*

<img src="../assets/chapter-4/figura_181.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 182**

*User Flow 10 de la aplicación web para propietarios y administradores
de bodegas de barrio: registrar un proveedor (US29)*

<img src="../assets/chapter-4/figura_182.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Figura 183**

*User Flow 11 de la aplicación web para propietarios y administradores
de bodegas de barrio: reponer un producto desde una alerta de stock bajo
(US32)*

<img src="../assets/chapter-4/figura_183.png" style="max-height:12.9cm">
Nota. Elaboración propia.

## 4.5. Web Applications Prototyping 

**Prototipo Desktop**

- **Segmento 1 - Propietarios y administradores de minimarkets**

Link:<a href="https://www.figma.com/proto/2LwKTN6fwKJFIL49MOMgnh/Untitled?node-id=77-7527&t=GDY486wi86Ivvvax-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=77%3A6562&show-proto-sidebar=1" style="color:#2563eb">https://www.figma.com/proto/2LwKTN6fwKJFIL49MOMgnh/Untitled?node-id=77-7527&t=GDY486wi86Ivvvax-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=77%3A6562&show-proto-sidebar=1</a>

- **Segmento 2 - Propietarios y administradores de bodegas de barrio**

Link:<a href="https://www.figma.com/proto/2LwKTN6fwKJFIL49MOMgnh/Untitled?node-id=77-11053&p=f&t=sKhI7uDZF4sUaseH-1&scaling=min-zoom&content-scaling=fixed&page-id=77%3A3&starting-point-node-id=77%3A10208&show-proto-sidebar=1" style="color:#2563eb">https://www.figma.com/proto/2LwKTN6fwKJFIL49MOMgnh/Untitled?node-id=77-11053&p=f&t=sKhI7uDZF4sUaseH-1&scaling=min-zoom&content-scaling=fixed&page-id=77%3A3&starting-point-node-id=77%3A10208&show-proto-sidebar=1</a>

**Prototipo Mobile**

Link:<a href="https://www.figma.com/design/ZXJ7Yk6gBQYIItE5B7hcvj/Wireframes-y-mockup-Mobile?node-id=0-1&t=gTdd0STYXGH6kUgr-1" style="color:#2563eb">https://www.figma.com/design/ZXJ7Yk6gBQYIItE5B7hcvj/Wireframes-y-mockup-Mobile?node-id=0-1&t=gTdd0STYXGH6kUgr-1</a>

## 4.6. Domain-Driven Software Architecture 

### 4.6.1. Design-Level Event Storming 

Se utilizó la guía de Philippe Bourgau, proporcionada en la rúbrica del
Final Problem Statement, para llevar a cabo el proceso de Design-Level
EventStorming, con el objetivo de identificar los Bounded Contexts,
siguiendo sus etapas:

- Unstructured Exploration
- Timelines
- Pain Points
- Pivotal Points
- Commands
- Policies
- Read Models
- External Systems
- Aggregates
- Bounded Contexts

**Miro Board Link:**

<a href="https://miro.com/welcomeonboard/WXlEQy9hRngvZnRPQkVlR3pJMDN5M25TTmpLSUY1Rk1kckJOVU15UnczNVNWQURZN3dUVFAxcitFSFJsUXJFaU5ET1JCc2VweWsrNytLZFliMGRLeEU2Y0VkT2ZMMEZSQmZXeXFHL3dBZ1VuR1Y3emdReUdaZHV1WFFLd3BrWDVNakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=815705743217" style="color:#2563eb">https://miro.com/welcomeonboard/WXlEQy9hRngvZnRPQkVlR3pJMDN5M25TTmpLSUY1Rk1kckJOVU15UnczNVNWQURZN3dUVFAxcitFSFJsUXJFaU5ET1JCc2VweWsrNytLZFliMGRLeEU2Y0VkT2ZMMEZSQmZXeXFHL3dBZ1VuR1Y3emdReUdaZHV1WFFLd3BrWDVNakdSWkpBejJWRjJhRnhhb1UwcS9BPT0hdjE=?share_link_id=815705743217</a>

**Figura 184**

*Design-Level EventStorming de SmartStock con los seis Bounded
Contexts*

<img src="../assets/chapter-4/figura_184.png" style="max-height:12.9cm">
Nota. Elaboración propia.

### 4.6.2. Software Architecture Context Diagram 

**Figura 185**

*Diagrama de contexto C4 de SmartStock*

<img src="../assets/chapter-4/figura_185.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** El diagrama de contexto muestra a SmartStock como un
único sistema de software que utiliza el propietario de un minimarket o
bodega para registrar ventas y compras, gestionar su inventario,
vincular sensores IoT y consultar su estado. El microcontrolador con
balanza IoT envía lecturas de peso para verificar el stock físico frente
al registrado, sin modificarlo. SmartStock se comunica con dos sistemas
externos: un servicio de notificaciones que envía alertas por correo o
WhatsApp, y un servicio de correo para la confirmación de cuenta y la
recuperación de contraseña.

### 4.6.3. Software Architecture Container Diagrams 

**Figura 186**

*Diagrama de contenedores C4 de SmartStock*

<img src="../assets/chapter-4/figura_186.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** SmartStock se compone de tres contenedores. La interfaz
web, implementada en Vue 3 con PrimeVue, es utilizada por el propietario
del negocio y consume el Backend API mediante solicitudes HTTP. El
Backend API, implementado en ASP.NET Core, es un monolito modular que
integra los seis contextos delimitados (IAM, Product Catalog, Inventory
Monitoring, IoT Device, Alerts & Restocking y Analytics & Reporting) y
expone sus servicios documentados con OpenAPI. La base de datos MySQL,
desplegada en Aiven, almacena usuarios, productos, ventas, compras,
proveedores, movimientos de inventario, sensores y alertas. Los sensores
IoT envían sus lecturas de peso al Backend API y no modifican el stock
registrado. El Backend API envía las alertas por correo (SMTP) y por
WhatsApp (Twilio).

### 4.6.4. Software Architecture Components Diagrams 

**Figura 187**

*Diagrama de componentes C4 de SmartStock, parte 1*

<img src="../assets/chapter-4/figura_187.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** IAM es un módulo del Backend API implementado en
ASP.NET Core en el Sprint 3, con la persistencia de negocios, usuarios y
recuperación de contraseña. El registro y la autenticación se completan
en el Sprint 4. Gestiona el registro, la autenticación y la recuperación
de contraseña desde Vue, con persistencia en MySQL y un servicio externo
de correo. BusinessType determina el menú según el negocio. En el Sprint
2 se utiliza una Fake API.

**Leyenda:** Azul oscuro: frontend; azul claro: componentes IAM; verde:
base de datos; amarillo: servicio externo. Los recuadros delimitan el
sistema, contenedor y módulo; las flechas indican sus relaciones.

**Figura 188**

*Diagrama de componentes C4 de SmartStock, parte 2*

<img src="../assets/chapter-4/figura_188.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** Product Catalog es un módulo del Backend API
implementado en ASP.NET Core en el Sprint 3. Gestiona los productos, sus
precios de venta, costos de compra, referencias al proveedor habitual y
umbrales mínimos, con persistencia en MySQL. Proporciona información a
Inventory Monitoring para Compras y Ventas, y a IoT Device para vincular
y monitorear sensores. Los proveedores se gestionan en Inventory
Monitoring.

**Leyenda:** Azul oscuro: frontend Vue; azul claro: componentes del
catálogo; morado: módulos relacionados; verde: base de datos MySQL. Los
recuadros delimitan el sistema, el contenedor y los módulos; las flechas
indican solicitudes y dependencias.

**Figura 189**

*Diagrama de componentes C4 de SmartStock, parte 3*

<img src="../assets/chapter-4/figura_189.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** IoT Device es un módulo del Backend API implementado en
ASP.NET Core en el Sprint 3. Gestiona la vinculación de sensores con
productos, registra sus lecturas y considera desconectado un sensor tras
cinco minutos sin recibir datos. Consulta el peso unitario en Product
Catalog y comunica las lecturas a Inventory Monitoring para comparar el
stock físico con el registrado, sin modificar este último. Los datos se
almacenan en MySQL.

**Leyenda:** Azul oscuro: frontend Vue; azul claro: componentes IoT;
morado: módulos relacionados; amarillo: sensores externos; verde: base
de datos MySQL. Los recuadros delimitan el sistema, el contenedor y los
módulos; las flechas indican solicitudes, lecturas y eventos internos.

**Figura 190**

*Diagrama de componentes C4 de SmartStock, parte 4*

<img src="../assets/chapter-4/figura_190.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** Inventory Monitoring es un módulo del Backend API
implementado en ASP.NET Core en el Sprint 3. Gestiona Compras, Ventas,
Proveedores y movimientos de inventario, con persistencia en MySQL. Las
ventas generan salidas de stock y las compras generan entradas al
confirmar su recepción. Recibe lecturas de IoT Device para comparar el
stock físico con el registrado, sin modificar este último, y comunica
los cambios y discrepancias a Alerts & Restocking.

**Leyenda:** Azul oscuro: frontend Vue; azul claro: componentes de
inventario; morado: módulos relacionados; verde: base de datos MySQL.
Los recuadros delimitan el sistema, el contenedor y los módulos; las
flechas indican solicitudes y eventos internos.

**Figura 191**

*Diagrama de componentes C4 de SmartStock, parte 5*

<img src="../assets/chapter-4/figura_191.png" style="max-height:12.9cm">
Nota. Elaboración propia.

**Descripción:** Alerts & Restocking es un módulo del Backend API
implementado en ASP.NET Core en el Sprint 3. Evalúa los umbrales del
catálogo usando el stock físico cuando el sensor está en línea y el
registrado cuando no hay sensor o está desconectado. Gestiona alertas,
notificaciones por correo y WhatsApp y necesidades de reposición
vinculadas con Compras en Inventory Monitoring. El usuario confirma la
compra; su registro y recepción permiten actualizar la reposición y
resolver la alerta asociada. Los datos se almacenan en MySQL.

**Leyenda:** Azul oscuro: frontend Vue; azul claro: componentes de
alertas y reposición; morado: módulos relacionados; amarillo: servicio
externo de notificaciones; verde: base de datos MySQL. Los recuadros
delimitan el sistema, el contenedor y los módulos; las flechas indican
solicitudes y eventos internos.

**Figura 192**

*Diagrama de componentes C4 de SmartStock, parte 6*

<img src="../assets/chapter-4/figura_192_00.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_01.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_02.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_03.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_04.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_05.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_06.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">
<img src="../assets/chapter-4/figura_192_07.png" style="width:11cm;max-height:none;display:block;margin:0 auto;break-before:auto">

Nota. Elaboración propia.

**Analytics** & Reporting es un módulo de consulta del Backend API
implementado en ASP.NET Core en el Sprint 3. Construye el dashboard y
los reportes por periodo con información de stock, Compras, Ventas y
movimientos de Inventory Monitoring, y alertas activas de Alerts &
Restocking. Consulta los datos mediante estos módulos, sin modificar el
inventario ni mantener agregados propios.

**Leyenda:** Azul oscuro: frontend Vue; azul claro: componentes de
análisis y reportes; morado: módulos consultados; verde: base de datos
MySQL. Los recuadros delimitan el sistema, el contenedor y los módulos;
las flechas indican solicitudes y consultas.

## 4.7. Software Object-Oriented Design 

### 4.7.1. Class Diagrams 

**Figura 193**

*Diagrama de clases del Bounded Context 1*

<img src="../assets/chapter-4/figura_193.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 194**

*Diagrama de clases del Bounded Context 2*

<img src="../assets/chapter-4/figura_194.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 195**

*Diagrama de clases del Bounded Context 3*

<img src="../assets/chapter-4/figura_195.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 196**

*Diagrama de clases del Bounded Context 4*

<img src="../assets/chapter-4/figura_196.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 197**

*Diagrama de clases del Bounded Context 5*

<img src="../assets/chapter-4/figura_197.png" style="max-height:12.9cm">
Nota. Elaboración propia

**Figura 198**

*Diagrama de clases del Bounded Context 6*

<img src="../assets/chapter-4/figura_198.png" style="max-height:12.9cm">
Nota. Elaboración propia

En la implementación del Sprint 3 el diseño de dominio se simplificó sin
cambiar las reglas de negocio: por indicación del docente, la
autenticación (login y token JWT) pasa al Sprint 4 y por ahora los
endpoints van abiertos con un negocio fijo (sin entidad AuthSession), la
categoría del producto se guarda como texto, y el umbral mínimo y el
stock registrado viven en el producto. Los diagramas muestran el modelo
de dominio; las tablas reales están en la sección 4.8.

## 4.8. Database Design 

### 4.8.1. Database Diagrams 

**Figura 199**

*Diagrama de base de datos de SmartStock*

<img src="../assets/chapter-4/figura_199.png" style="max-height:12.9cm">
Nota. Elaboración propia

El diseño de la base de datos organiza las tablas por bounded context.
Los negocios se relacionan con usuarios, productos, proveedores y
operaciones de inventario. Cada venta y compra contiene sus ítems, que
conservan el precio o costo de la operación: las ventas generan
movimientos de salida y las compras generan entradas al confirmar su
recepción. Los sensores registran lecturas para verificar el stock
físico, sin modificar el registrado. Las alertas se vinculan con
necesidades de reposición y compras asociadas, mientras que las
preferencias y notificaciones permiten gestionar los canales de aviso.
Analytics & Reporting consulta estos datos para construir el dashboard y
los reportes.

