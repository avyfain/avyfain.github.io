---
title: "Code Reviews Efectivos: Alinea a tu equipo y entrega mejor código"
main_image: cdmx2/previews/17.jpeg
layout: post
category: articles
tags: [management, startups, jobs, technology, software engineering, programming]
skip_language: true
---

<small><em>This essay is also available [in English](/articles/2024/07/09/pull-requests/).</em></small>

El ensayo a continuación es una versión ligeramente editada (y traducida) de un documento que escribí para mi equipo en Vouch en el 2021 cuando escalábamos la función de ingeniería de datos. Es una guía de cómo escribir buenos pull requests y cómo revisarlos de manera constructiva. Los patrones son lo suficientemente generales como para encajar en cualquier equipo, no solo en uno enfocado en proyectos de data. El proceso de revisión de pull requests introduce mucha fricción en el ciclo de desarrollo, pero sirve para múltiples propósitos, incluyendo el intercambio de conocimiento, la calidad del código y la alineación de equipos. Vale la pena la inversión.

<hr>

**Primero lo primero - ¿qué es un PR y cuál es el propósito de revisarlos?**

Un PR es un "pull request." Abrir un PR es una forma de pedir (request) a los maintainers de un proyecto que incorporen (pull) un conjunto de cambios de código al repositorio de un proyecto. Los PRs a veces también se llaman "[merge requests](https://stackoverflow.com/a/36666408)."

Cuando un autor abre un PR, uno o varios revisores chequean los cambios propuestos y comparten sus comentarios sobre lo que debe actualizarse antes de que el código pueda ser mergeado al repo. El autor puede entonces responder a la crítica, revisar su trabajo y solicitar otro review. El ciclo se repite varias veces hasta que el revisor se siente cómodo con la propuesta y aprueba el PR. Este proceso de revisión iterativa es cómo nos aseguramos de tener un entendimiento compartido de los sistemas manteniendo un alto estándar en calidad de código.

**¿Qué hace que un PR sea bueno?**

Un buen pull request representa un solo pedazo de lógica. A veces, especialmente en proyectos grandes, quienes revisan PRs pueden tener poco contexto sobre cómo funcionará el cambio propuesto, por lo que es necesario incluir un resumen conciso del efecto previsto. La discusión sobre el problema a resolver debe ocurrir en el sistema de tickets y, idealmente, debería suceder antes de escribir una sola línea de código. La discusión sobre la implementación que resuelve dicho problema debe vivir en el PR. Tus tickets deben contar el "por qué" y el "qué", mientras que tus PRs son el "cómo".

Idelamente, los cambios propuestos son pequeños, y el PR incluye tests que prueban que el cambio propuesto es efectivo, o que la funcionalidad funciona como se espera. Si hay partes de la lógica propuesta de las que no estás seguro como autor, o que no pueden ser probadas fácilmente, asegúrate de señalárselo a los revisores. Esta es una buena oportunidad para que los revisores ayuden a los autores a pensar sobre el problema.

A menudo, los PRs limpian o arreglan otros problemas que estaban presentes en los archivos que tocan. Esto está bien, y de hecho debe ser incentivado, pero si esos cambios van más allá de unas cuantas funciones o actualizaciones de clases adicionales, tiene sentido dividir el PR en dos - uno para la funcionalidad en la que se suponía que estabas trabajando, y otro para la limpieza, especialmente si el alcance del PR se expande.

Revisar el trabajo de otras personas toma tiempo y esfuerzo. Un buen PR hace simple para los revisores entender qué estás cambiando.

**Entonces, cuál es mi rol y cuál el del revisor?**

Como el autor abriendo un PR, eres responsable de pedir code reviews y guiar el PR hasta mergearlo. Los revisores son responsables de la calidad y los estándares del código. El autor es responsable de asegurar que los cambios funcionen como se espera.

Es importante balancear calidad y entrega, asegurando no apuntar a la perfección sino a entregar código "suficientemente bueno." La interacción entre autor y revisores mantiene ese balance. Como autor, debes oponerte a las sugerencias de los revisores cuando tiene sentido. Si los cambios solicitados por el revisor parecen demasiado grandes o no relacionados, abre nuevos tickets en el backlog y evita el scope creep. Si hay desacuerdos sobre la lógica, busca la opinión de un segundo revisor.

Como revisor, es importante enfocarse en los objetivos principales del cambio primero. Evita ser quisquilloso. Si tienes muchos comentarios, sé claro sobre qué cambios son absolutamente necesarios y cuáles son "nice to have." Algunos equipos incluyen listas priorizadas en sus checklists de PRs para guiar este proceso.

Las revisiones normalmente toman un par de ciclos. No esperes mergear tu código tal como estaba en el primer push. Después de que hayas abordado una ronda de comentarios, debes volver a solicitar revisión y pedir explícitamente más sugerencias.

**Está tu código listo para revisión y merge?**

Herramientas como Github o Bitbucket tienen funciones diseñadas para revisar cambios de código, por lo que a menudo los autores abren PRs en borrador para compartir sus ideas antes de que estén listas para ser consolidadas en el repo del equipo. Es importante que cualquier trabajo que está a medias sea marcado como tal, y puedes hacerlo fácilmente al abrir un PR.

De igual forma, si hay cambios adyacentes que deben ocurrir en otros sistemas (piensa en PRs en otros repositorios, o configuración de componentes adicionales) debes mencionarlos para que los revisores entiendan el alcance de tu cambio. A menudo, los equipos usan etiquetas, checklists, u otros mecanismos en su servicio de control de versiones para denotarlo.

La mayoría de repos avanzados tienen algunos checks de integración continua (CI) que corren automáticamente al abrir un PR. El hecho de que los CI checks estén verdes no significa necesariamente que el código es bueno - podrías estar introduciendo cambios que el CI aún no puede detectar. Si el CI se pone rojo podrías haber pegado con un falso negativo - tal vez tienes que actualizar los tests, o potencialmente estés enfrentando un problema no relacionado a tu cambio. Como desarrollador, eres responsable por ambos tipos de errores.

Es posible que te aprueben el PR antes de que el CI esté en verde. En ese caso, usa tu juicio y vuelve a solicitar revisiones si tuviste que hacer cambios grandes para que el CI pase.

Si mergear tu PR lleva al cambio positivo esperado, ¡genial! Si mergear tu PR rompe el build o conlleva problemas inesperados, eres responsable de resolverlos. Si mergeaste algo que no funcionó como esperabas, y las cosas se salen de control, debes trabajar con tu equipo para corregirlo. Generalmente, favorece un _rollforward_ en lugar de retroceder a un estado anterior.

**Algo más?**

Recuerda que los code reviews son buenas oportunidades para aprender de los demás.

La crítica que damos y recibimos en los PR code reviews es sobre el _trabajo_ de las personas, no sobre las personas en si. Todos tenemos opiniones sobre el código y cómo deberían funcionar las cosas. Sé amable y respetuoso.


<hr>
<small><em>Foto: Déjalo Ir, por mí. Anteriormente compartida en [CDMX, Dos](/photos/2022/12/16/cdmx2/).</em></small>
