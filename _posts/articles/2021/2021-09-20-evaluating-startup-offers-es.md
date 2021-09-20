---
title: Cómo evaluar ofertas de trabajo en startups - una guía para principiantes
layout: post
tags: [startups, jobs, tech, san francisco]
main_image: vaxd-travel/previews/2.jpeg
category: articles
skip_language: true
description: Si planeas unirte a un startup por la plata, lo estás haciendo por la razón incorrecta, pero eso no implica que la plata no debe ser un factor en tu decisión. Podemos construir modelos financieros de salario y capital, y acá demostraré cómo hacerlo.
---


<small>TL;DR, [ésta](https://docs.google.com/spreadsheets/d/1AW0WVzsaEQOan_oHHIFHO0lAfpjtATsywe18hvh1H3Q/edit) es una hoja de calculo que puedes duplicar para evaluar tus ofertas de trabajo.</small>

<small><em>This essay is also available [in English](/articles/2021/09/20/evaluating-startup-offers/).</em></small>

Hace poco decidí [dejar mi trabajo en Apple](/2021/04/16/heres-to-the-crazy-ones-es), donde estuve por 6 años, para entrar a un startup llamado [Vouch](vouch.us) (estamos [contratando](vouch.us/careers)!). Al considerar el cambio, mucha gente me dijo que estaba haciendo un gran error, perdiendo en estabilidad laboral y compensación. Esa gente no tenía idea de lo que estaban hablando. Si planeas unirte a un startup por la plata, lo estás haciendo por la razón incorrecta, pero eso no implica que la plata no debe ser un factor en tu decisión.

Podemos construir modelos financieros de salario y capital, y acá demostraré cómo hacerlo, pero recuerda que tu experiencia laboral te va a dar conocimiento [intangible](https://economipedia.com/definiciones/activo-intangible.html) que no puedes representar en una hoja de cálculo. Una oferta de FAANG siempre va a ganar en números. Si tienes la flexibilidad, escoje tu próximo trabajo basándote en cómo te va a ayudar a llegar donde quieres llegar. La gente con la que trabajarás y los contactos que puedes hacer importan mucho. Solo uno puede saber si un nombre de marca o el aprendizaje de cómo navegar burocracias serán más o menos valiosas para su futuro que ver un nuevo negocio nacer desde cero o vivir la experiencia del hiper-crecimiento. Asegurate de tener un objetivo claro, o escoger entre tus opciones será mucho más dificil. Por ejemplo, cuando [decidí entrar a Vouch](/articles/2021/04/26/new-beginnings/), intenté maximizar cuánto aprendería sobre el sistema de capital de riesgo y como operan las startups.

Si estás considerando tomar un rol en un startup, la estructura que presento a continuación te dará las herramientas básicas para comparar ofertas, pero no pretende dar respuestas exactas.

### 1. Cómo funciona el capital de riesgo

Cuando uno lee que un startup levantó una ronda de capital con una valuación ridícula, simplemente significa que un fondo de capital de riesgo (en inglés _venture capital_ o VC) estaba dispuesto a comprar una porción del negocio en efectivo, y que el startup aceptó su propuesta. Los términos del convenio implican la nueva valoración de la compañía. Los startups usan diferentes instrumentos financieros para levantar capital, pero el camino más común es simplemente ese: un flujo de dólares hacia la compañía emparejado por la emisión de **acciones preferentes**, creando valor casi que de la nada.

Para ilustrar el mecanismo, imaginemos[^1] una compañía que levanta una ronda semilla de un solo fondo:

* Antes del trato, el startup tiene 10M de acciones en circulación
* Un VC valora la compañía en $5M _pre-financiamiento_ y accede a invertir $1M a ese precio. Esto efectivamente le da a la compañía una valoración _post-financiamento_ de $6M.
* La valuación implica el precio de las acciones en circulación. Si _pre-financiamiento_ los 10M de acciones valen $5M, el precio es $5M / 10M acciones = $0.50 / acción
* A cambio de $1M, la compañía emite nuevas acciones y se las da al VC. El número de acciones emitidas es una cuestión de aritmética: ($1M) / ($0.50/acción) = 2M nuevas acciones. Ahora la empresa tiene 10M + 2M = 12M acciones en circulación
* Normalmente, un bloque adicional de **acciones ordinarias** es emitido con cada ronda para provisionar el [employee option pool](https://carta.com/blog/how-to-size-employee-option-pool/) (acciones designadas para atraer talento). Estas acciones también afectan la valoración, pero las ignoraremos para mantener el análisis sencillo.

Para los accionistas, la ronda es una buena noticia. Sin embargo, ahora son dueños de una tajada más pequeña de un pastel más grande. El proceso que disminuye el porcentaje de propiedad al emitir nuevas acciones se llama **dilución**. Si eras un dichoso accionista con 100,000 acciones, solías ser el dueño de 1% de la empresa. Después de eta ronda, solo posees 0.83%, y las próximas rondas de capital diluirán tu participación aún más.

El proceso de financiamento es complejo y detallado[^2], pero los conceptos básicos descritos anteriormente sobre como se llega al precio de una acción y cómo su valor cambia a través de la vida de una empresa resuelven una gran parte del rompecabezas. [La mayoría de los startups fracasan](https://www.failory.com/blog/startup-failure-rate) pero si tienes suerte, entrarás a uno de los pocos que no valen $0 a largo plazo.


### 2. Estructura de paquetes de compensación y opciones

Además del salario y tal vez un bono inicial, los startups ofrecen propiedad (en inglés _equity_) como parte de su compensación. La propiedad compartida es parte de la mentalidad de los startups a propósito. Recibir parte del pago en acciones alinea incentivos, traduciendo el duro trabajo de los empleados en el potencial de ganancias compartidas. Al mismo tiempo, permite a las empresas ofrecer el prospecto de un gran pago en el futuro a cambio de un sueldo más bajo a corto plazo.

Aunque compañías más grandes pueden ofrecer acciones en forma de RSUs, que son funcionalmente similares a las acciones de empresas públicas que uno puede comprar en la bolsa de valores, los startups suelen pagar con [opciones](https://www.investopedia.com/terms/o/option.asp). Estos activos vienen en muchos sabores, más que todo se diferencian por su tratamiento fiscal, pero para mantener las cosas simples asumiremos que estamos hablndo de opciones de incentivo ([_incentive stock options_ o ISOs](https://carta.com/blog/what-are-incentive-stock-options/)). Un ISO le da al titular el derecho de comprar una acción ordinaria en el futuro, a un precio preestablecido. Esto se llama el **precio de ejercicio** (_strike price_) y porviene de una evaluación independiente del valor justo de mercado de las acciones (_fair market value, o FMV_). Este precio también se conoce como la **valoración 409a**, por la [sección](https://en.wikipedia.org/wiki/Internal_Revenue_Code_section_409A) del código del gobierno de Estados Unidos que lo regula. El precio de ejercicio siempre es una fracción del precio preferencial pagado por los inversionistas en la última ronda, configurado de tal forma que el valor de las acciones ordinarias tengan un valor nominal de $0, asegurando que no haya un evento fiscal al momento de concederle las acciones al empleado.

Usando el ejemplo anterior, el precio de $0.50 por accion preferencial pagado por los inversionistas puede traducirse a un precio de ejercicio de $0.15[^3]. A este prcio, si un posible empleado recibe $50k en acciones, estaría recibiendo una oferta de 100,000 opciones. Si a la compañía le va mal, las opciones pueden quedar sin valor o [bajo el agua](https://www.investopedia.com/terms/u/underwater.asp),pero asumamos que la compañía prospera, y que en unos años sus acciones valen $50 cada una (un incremento de 100x!). Este empleado suertudo tiene el derecho de **ejercer** sus opciones, canjeándolas por acciones pagando $15,000 ($0.15 * 100,000 opciones) para obtener $5 millones en acciones ($50 * 100,000 acciones). 

Pero nos estamos adelantando. Antes de que el capital se pueda apreciar, tiene que ser **adjudicado** (en inglés, **vest**). Los números grandes suenan emocionantes para el hipotético nuevo miembro del equipo, pero recibir una concesión de acciones al firmar una oferta no significa que el capital será transferido inmediatamente. Una vez más, esto es una cuestión de incentivos. Si la empleada recibiera sus acciones inmediatamente, podría renunciar al día sguiente. Para garantizar que las personas están comprometidas a largo plazo, el estándar en la industria es un programa de adjudicación que extiende la distribución a lo largo de cuatro años, con un periodo de pausa inicial (en inglés, **cliff**) de un año. Durante el primer año de su labor, el empleado no recibe capital del todo. Al terminar ese periodo inicial, se le adjudica 25% de su concesión, y cada mes después de eso se le entregarán otros 2.0833% (75% a través de 36 meses).

Los términos discutidos anteriormente varían de empresa a empresa, y algunas serán más abiertas que otras al compartir esta infromación durante la negociación. Dos condiciones sobre las cuales vale la pena preguntar son el [ejercicio temprano](https://www.cooleygo.com/early-exercisable-stock-options-what-you-need-to-know/) y las ventanas de ejercicio[^4]. En resumen, al dejar la empresa, los empleados tienen un tiempo limitado para comprar sus acciones. El estándar en la industria solía ser [90 días después de la partida](https://zachholman.com/posts/fuck-your-90-day-exercise-window/), pero algunas compañías han empezado a cambiar sus prácticas para favorecer más a los empleados. Éstos terminos tienen un gran impacto en el valor de tu compensación.

La transparencia al hablar de condiciones y valoración es una señal de una operación bien gestionada, una cultura abierta, y un negocio saludable. Si la compañía no comparte estos datos eso puede significar que no le está yendo tan bien. El valor en dólares de un paquete de capital no significa mucho sin un contexto más amplio. Siempre debes recibir números específicos de:

* Número de acciones emitidas
* El último precio preferencial
* Valoración 409a/precio de ejercicio
* Número exacto de opciones en tu concesión

Con éstos números a nuestro alcance, y dejando de lado la complejidad de los impuestos, podemos seguir con el cálculo que nos permitirá comparar ofertas.


### 3. Valor Esperado
Si has llevado una clase básica de probabilidad, considera saltar está sección.

El valor esperado es exactamente lo que parece: una forma de medir el potencial de algo que actualmente tiene un valor desconocido, como la valoración de un startup en 5, 10 o 20 años.

Usemos el juego de cara o escudo como ejemplo. Si sale cara, recibes $100. Si sale escudo, recibes $0. El valor esperado (indicado como E[x]) se define como la suma de los resultados ponderados por la probabilidad de que cada uno ocurra:

    E[x] = (½ * $0) + (½ * $100) = $50

Cierto, con estas reglas, en ningún caso nos recompensará con $50, pero el valor que anticipamos igualmente está dado por esta suma ponderada. Si uno repite el ejercicio y tira la moneda mil veces, el promedio terminará en $50, como nos dice [la ley de los grandes números](https://es.wikipedia.org/wiki/Ley_de_los_grandes_n%C3%BAmeros). Eventos más complejos pueden ser modelados de la misma forma. Si tiramos un dado común de 6 lados, el valor esperado es 3.5, sin importar que nunca haya un lanzamiento donde el resultado quede suspendido entre 3 y 4:

    (⅙ * 1) + (⅙ * 2) + (⅙ * 3) + (⅙ * 4) + (⅙ * 5) + (⅙ * 6) = 3.5

Aplicando esta idea, podemos estimar el valor futuro de cualquier cosa: el premio por jugar en una máquina tragamonedas, el retorno al comprar una casa, el precio de las acciones de Apple mañana, o el posible pago cuando tu startup se haga pública. Un detalle importante es que a diferencia de el lanzamiento de una moneda donde las proabilidades son conocidas y discretas (la mitad del tiempo vemos cara, la mitad vemos escudo) y los pagos están bien definidos ($0 o $100) los problemas más interesantes siempre involucran más incertidumbre. Con una máquina tragamonedas, el jugador no sabe la estructure de los premios, ni la distribución de las propiedades, sin embargo ambas fueron diseñadas por el fabricante. En los mercados de bienes raices, la bolsa de valores, y el capital de riesgo, no solo desconocemos los pagos y la distribuciones de probabilidad, sino que éstos no han sido definidos por nadie. Son fenómenos emergentes.

La incertidumbre sobre la incertidumbre es la razón por la que existe toda una industria dedicada a analizar patrones en el ruido. Al igual que existe un valor esperado, también se puede medir el [riesgo esperado](https://www.investopedia.com/terms/r/risk.asp), pero lo dejaré para otro ensayo.

### 4. Análisis de flujo de fondos descontado

Si has llevado una clase básica de finanzas, considera saltar está sección.

Evaluar cualquier proyecto financiero require tomar en cuenta el [valor del dinero en el tiempo](https://www.investopedia.com/terms/t/timevalueofmoney.asp). Además de los aspectos inciertos discutidos anteriormente, el pago en los startups es asimétrico: Uno acepta menos compesación hoy por la promesa de una gran retribución mañana. Dejando de lado restricciones de liquidez (por ejemplo, el deseo de ahorrar $X/año para pagar una prima, o necesitar $Y/mes para pagar un préstamo o alquiler), necesitamos una forma de incluir el costo del tiempo para calcular el valor real de las ofertas que tenemos en la mesa.

En resumen, el problema que queremos resolver es que $1 hoy vale más que $1 mañnana. Con $1 hoy, podemos pagar $1 de nuestra deuda y evitar acumular intereses; o podemos poner ese $1 en el banco y ganarnos el interés. Este proceso de trazar proyectos uno al lado del otro para comparar sus rendimientos se llama análisis de flujo de fondos descontado, o [DCF](https://www.investopedia.com/terms/d/dcf.asp) por sus siglas en inglés.

Por ejemplo, asumiendo que hay un banco que está dispuesto a darnos una tasa de r = 1% anual sobre nuestro efectivo, sabemos que depositar $100 hoy implica tener $101 en un año. La matemática también funciona de forma inversa, y podemos ver que si:

    ($100 hoy) * (1 + 1%) = $101 el próximo año

entonces

    $100 hoy =  ($101 el próximo año) / (1 + 1%)

Abstractamente,

    $X hoy = $X el próximo año/(1+r)

Dividir por ese factor se llama _descontar_. Podemos usar esta misma lógica para descontar pagos más adelante en el futuro, dividiendo cada flujo de caja por (1+r) cada periodo.

    $X el próximo año/(1+r) = ($X en dos años/(1+r))/(1+r) = $X en dos años/(1+r)^2

Entre más nos alejamos del presente, mas se reduce el valor de esos futuros flujos de caja. Escoger el [valor correcto de r](https://twitter.com/avyfain/status/1372198641910288386) es una ciencia por si sola, pero de cierta forma representa el uso alternativo que le podríamos dar a esos fondos si los tuvieramos a la mano hoy.

Por ejemplo, imaginemos dos startups. Uno nos ofrece un salario inicial mayor, con aumentos salariales anuales, mientras que el otro nos anuncia de una vez que no tendremos un aumento el primer año a cambio de más fondos en el futuro.

<table>
  <tr>
   <td></td>
   <td>Año 1</td>
   <td>Año 2</td>
   <td>Año 3</td>
   <td>Año 4</td>
  </tr>
  <tr>
   <td>Oferta A
   </td>
   <td>$110</td>
   <td>$115</td>
   <td>$120</td>
   <td>$125</td>
  </tr>
  <tr>
   <td>Oferta B
   </td>
   <td>$100</td>
   <td>$100</td>
   <td>$120</td>
   <td>$150</td>
  </tr>
</table>

Si escogemos r = 5%, por ejemplo, podemos descontar esos flujos de caja para llegar al [valor actual neto](https://es.wikipedia.org/wiki/Valor_actual_neto) (NPV por sus siglas en inglés):

    NPV(A) = $110 + $115/(1+r) + $120/(1+r)^2 + $125/(1+r)^3 = $415.57
    NPV(B) = $100 + $100/(1+r) + $120/(1+r)^2 + $150/(1+r)^3 = $413.01

Si sumamos los flujos de caja ingenuamente, ambos llegan a $470, pero la estructura de pagos es muy diferente y (solo financieramente) sería mejor aceptar la oferta de A que la de B. El NPV que obtenemos depende completamente del valor que elejimos para r.

### Evaluar nuestra oferta


Ahora pongámoslo todo junto, entrando en anális de [escenarios](https://www.investopedia.com/terms/s/scenario_analysis.asp) y [sensibilidad](https://www.investopedia.com/terms/s/sensitivityanalysis.asp).

Volvamos a las empresas hipotéticas, pero ahora, en lugar de asumir salidas seguras, modelemos estos pagos basados en valores esperados, incluyendo los costos de dilución y ejercicio de nuestras acciones. Aquí es donde entra en juego el análisis de escenarios. Podemos estimar las probabilidades de los resultados basándonos en sabemos sobre el mercado; asegurándonos de errar siempre siendo demasiado negativos y no demasiado optimistas.

Pueden encontrar una hoja de cálculo que pueden copiar y editar para poner sus propios valores [acá](https://docs.google.com/spreadsheets/d/1AW0WVzsaEQOan_oHHIFHO0lAfpjtATsywe18hvh1H3Q/edit?usp=sharing).

![Equity Spreadsheet]({{ site.image_path }}evaluating_startup_offers/equity_tool.png
 "Equity Spreadsheet")

Los valores en celeste representan los términos que nos daría el reclutador de la empresa con quien negociaremos (por eso es que la transparencia importa). Los valores en rojo pueden ser llenados en base a lo que aprendemos en nuestras entrevistas y nuestra propia investigación sobre el mercado. Qué tan grande puede llegar a ser esta empresa? Finalmente, los valores en amarillo son aproximaciones estándar que dependen de cuánto capital ha recibido la compañía, y el sentimiento del mercado en general.

Podemos construir tablas como esta para modelar cada escenario de las ofertas que tenemos. Para

You can build a table like this one to model scenarios for the offers you have at hand. Para hacer las cosas sencillas, la hoja de cálculo hace suposiciones para todas las ofertas que no necesariamente se tienen que mantener. Por ejemplo, todas estas startups ficticias tienen una venta después de 4 años, pero podríamos modelar incertidumbre en ese aspecto también. Toma la hoja como una plantilla y actualízala para ajustarla a tus necesidades. Podríamos ampliar los cálculos para incluir la dilución de rondas de financiaciamiento adicionales, ventas secundarias, o [concesiones futuras](https://review.firstround.com/The-Right-Way-to-Grant-Equity-to-Your-Employees), etc. Al final, lo que estamos tratando de hacer es reducir cada oferta a una lista de flujos de caja, los cuales podemos descontar a diferentes tasas.

En el ejemplo en la hoja de cálculo, por exemplo, Foo Inc ofrece un buen salario y un bueno bono de entrada, pero un bajo potencial de venta, mientras que Bar.ly y Baz.io reciben más valor de la venta después de cuatro años. Al menos en papel, parece que Bar.ly no ofrece tanto en términos de dinero.

![NPV Sensitivity Analysis]({{ site.image_path }}evaluating_startup_offers/equity_tool.png
 "NPV Sensitivity Analysis")

Solo tu instinto puede decirte cómo seguir desde acá. Los inversionistas de riesgo pueden hacer muchas apuestas pequeñas con su fondo. Eso les da mucho más margen de error para equivocarse varias veces y aún así recibir ganancias. Al elegir un nuevo trabajo, uno está poniendo todos sus huevos en la misma canasta, por lo que es mejor elejir una donde parezca poco probable que se rompa el fondo. Justo por eso es que elegir un startup solo por la posibilidad financieras es una mala idea. Si tienes un par de opciones que marcan todas las casillas de lo que estás buscando y estás igualmente entusiasmado con ambas, solo entonces se reduce todo a las finanzas. Si las acciones valen $0, vas a aprender las cosas que quieres aprender? Vas a hacer los contactos adecuados? Vas a trabajar lo suficientemente cerca con los líderes de la empresa? Estos detalles no aparecen en ningún modelo financiero, pero probablemente importan mucho más a lo largo de tu carrera.

### Un pequeño comentario sobre negociación

La mayoría de los startups están dispuestos a canjear acciones por efectivo. Si tienes préstamos que pagar, o tienes algún otro tipo de límite de liquidez, siempre puedes pedir más efectivo y menos acciones. Si puedes vivir con un sueldo más bajo y realmente crees en la visión, puedes tomar el riesgo y pedir más acciones. Si sientes que tienes poder en la negociación, pedir dos ofertas, una con muchas acciones y pero poco sueldo y vice versa, eso te puede dar una pista a cómo la empresa evalúa su propio valor. Pedir más acciones siempre es más fácil que más efectivo, pero tener dos ofertas te dará una idea de cómo se ve una oferta completamente en efectivo, lo cual es un dato útil por si solo.

Voy a dejar el resto de mis consejos sobre negociación para el próximo post, pero si estás buscando más ayuda de ese lado mi recomendación es leer la [guía de Patrick McKenzie](https://www.kalzumeus.com/2012/01/23/salary-negotiation/).

Tienes sugerencias de negociación, ideas sobre como mejorar el modelo, consejos sobre startups o comentarios generales/ Me encantaría [escúcharlos](/contact/page/).

<small>_This is the third in a series I’m writing about my recent career transition out of Apple. See part one, on [things I learned in my time at Apple](/2021/04/16/heres-to-the-crazy-ones/), and part two, on [how I picked my role at Vouch](/articles/2021/04/26/new-beginnings/). Make sure to check back in a few weeks for upcoming pieces on **things to ask in interviews with startups**, and **tips on how to make your job transition as smooth as possible**, etc._<small>

<small>_Este es el tercer artículo en una serie que estoy escribiendo sobre mi transición al salir de Apple. Puedes ver la parte uno sobre [cosas que aprendí en Apple](/2021/04/16/heres-to-the-crazy-ones), la parte dos sobre [cómo escogí mi próximo rol en Vouch](/articles/2021/04/26/new-beginnings/) o volver en unas semanas para leer otros sobre **preguntas para hacer en entrevistas con startups**, **tips sobre cómo hacer que la transición entre trabajos sea lo mejor posible**, etc._</small>

Gracias a Hannah Doherty, Max Faingezicht, Moi Stern, y Sandeep Paruchuri por sus comentarios en borradores de este post.

<hr>
<small><em>Foto: Big Wheel, Las Vegas, propia. Anteriormente compartida en [Vax'd Travel](/photos/2021/07/10/vaxd-travel/).</em></small>
<hr>


[^1]:
    Sacado de la [guía de cómo levantar fondos](https://www.ycombinator.com/library/4A-a-guide-to-seed-fundraising) de Y Combinator.

[^2]:
     Si quieres entender esto más a fondo el libro [Venture Deals de Brad Feld](https://bookshop.org/books/venture-deals-be-smarter-than-your-lawyer-and-venture-capitalist/9781119594826) es el lugar correcto para empezar.

[^3]:
     Esto implica un FMV de 30% de la valoración de la última ronda. Aunque le evaluación en si es un proceso muy complejo, dependiendo del mercado y la ronda ⅕ a ⅓ del precio preferencial es una buena regla a seguir.

[^4]:
     Ambos están fuera de lo que quiero cubrir en este post, pero el primero puede tener un gran impacto en tus impuestos, mientras que el segundo puede hacer que tus opciones valgan incluso menos de lo que pensabas si tu situación financiera no te permite adquirir las acciones.
