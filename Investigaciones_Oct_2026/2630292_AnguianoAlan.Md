# Metodologías Ágiles: Scrum, Kanban y Design Thinking


## 1. Resumen ejecutivo

**¿Qué es "ágil"?** Agilidad es la capacidad de un equipo para entregar valor de forma frecuente, aprender rápido de la retroalimentación y adaptarse al cambio sin perder el rumbo. No es una metodología única, sino una **familia de enfoques** (Scrum, Kanban, XP, entre otros) que comparten valores y principios formulados en el *Manifiesto Ágil* (2001).

**¿Por qué surge?** Durante los años 80 y 90, los proyectos de software se gestionaban con enfoques predictivos y secuenciales (cascada). Esos enfoques asumían que los requisitos podían definirse completos al inicio. En la práctica, los requisitos cambian, el cliente aprende mientras ve el producto y la tecnología evoluciona. El resultado eran proyectos tardíos, caros y que entregaban algo que ya no era lo que se necesitaba. En 2001, diecisiete practicantes se reunieron en Utah y publicaron el Manifiesto Ágil como respuesta.

**¿Qué cubre este documento?**

1. Valores y principios ágiles y su impacto en la gestión del trabajo.
2. Panorama comparativo de Scrum, Kanban y Design Thinking.
3. Ventajas, riesgos y trade-offs.
4. Profundización en cada marco: roles, artefactos, eventos, métricas, tableros, fases y un mini-caso.
5. Conclusiones en base a la experiencia y áreas de oportunidad del alumno investigador.

---

## 2. Principios ágiles

### 2.1 Los cuatro valores del Manifiesto

| Se valora más… | …que |
|---|---|
| **Individuos e interacciones** | procesos y herramientas |
| **Software funcionando** | documentación exhaustiva |
| **Colaboración con el cliente** | negociación contractual |
| **Responder al cambio** | seguir un plan |

> Importante: el manifiesto reconoce que lo de la derecha *también tiene valor*; simplemente se prioriza lo de la izquierda.

### 2.2 Los doce principios (resumidos y agrupados)

| Tema | Principios clave | Impacto en la gestión del trabajo |
|---|---|---|
| **Valor y cliente** | Satisfacer al cliente con entregas tempranas y continuas; los cambios son bienvenidos incluso tarde; entregar software funcional con frecuencia (semanas, no meses). | Se planifica en ciclos cortos, se prioriza por valor y se reduce el costo de equivocarse. |
| **Colaboración** | Negocio y desarrollo trabajan juntos a diario; la conversación cara a cara es el medio más eficiente. | Menos traspasos formales; decisiones más rápidas; equipos pequeños y multifuncionales. |
| **Personas** | Proyectos construidos en torno a individuos motivados con confianza y apoyo; equipos auto-organizados. | El gestor pasa de "controlar" a "habilitar" (liderazgo servicial). |
| **Calidad técnica** | Atención continua a la excelencia técnica y al buen diseño; ritmo sostenible. | Se integran pruebas, refactorización e integración continua; se evita el *burnout*. |
| **Simplicidad** | Maximizar la cantidad de trabajo **no** realizado; el software funcionando es la medida principal de progreso. | Se recortan funcionalidades de bajo valor; el avance se mide con producto, no con documentos. |
| **Mejora continua** | Reflexión periódica del equipo para ajustar su forma de trabajar. | Retrospectivas y ajustes regulares del proceso. |

### 2.3 Cambio de mentalidad: predictivo vs. ágil

| Aspecto | Predictivo (cascada) | Ágil |
|---|---|---|
| Requisitos | Cerrados al inicio | Evolutivos |
| Entrega | Una al final | Incrementos frecuentes |
| Cambio | Se evita (control de cambios) | Se acepta y gestiona |
| Planeación | Detallada a largo plazo | Adaptativa, por horizontes |
| Rol del cliente | Al inicio y al final | Colaborador continuo |
| Medida de avance | Cumplimiento del plan | Valor entregado / software funcionando |

---

## 3. Panorama de marcos ágiles

| | **Scrum** | **Kanban** | **Design Thinking** |
|---|---|---|---|
| **Naturaleza** | Marco de trabajo iterativo con roles, eventos y artefactos | Método para gestionar flujo y mejorar un proceso existente | Enfoque centrado en las personas para descubrir y validar problemas y soluciones |
| **Pregunta que responde** | ¿Cómo construimos un producto complejo de forma incremental? | ¿Cómo hacemos fluir el trabajo y detectamos cuellos de botella? | ¿Estamos resolviendo el problema correcto para el usuario correcto? |
| **Cadencia** | Sprints de duración fija (≤ 1 mes) | Flujo continuo (cadencias opcionales) | Fases iterativas, no lineales |
| **Roles** | Product Owner, Scrum Master, Developers | Ninguno obligatorio | Equipo multidisciplinario, facilitador |
| **Unidad de trabajo** | Ítems del Product Backlog dentro de un Sprint | Tarjeta que fluye por el tablero | Hallazgos, ideas, prototipos |
| **Se enfoca en** | Entregar un Incremento útil cada Sprint | Limitar WIP y reducir tiempos de ciclo | Reducir incertidumbre sobre el valor |

### ¿Cuándo elegir cada uno?

- **Scrum:** desarrollo de producto con objetivos que se descubren sobre la marcha, equipo estable (3–9 personas) y posibilidad de priorizar y entregar en ciclos cortos. Ejemplo: construir una aplicación web nueva.
- **Kanban:** trabajo con demanda impredecible o llegada continua (soporte, mantenimiento, operaciones, tickets), o cuando se quiere mejorar un proceso actual **sin** reorganizar al equipo.
- **Design Thinking:** al inicio de una iniciativa, cuando no se sabe bien qué construir, el usuario no está claro o la solución es innovadora. Se combina con Scrum o Kanban para la construcción.

> Estos marcos **no son excluyentes**: es común usar Design Thinking para descubrir, Scrum para construir y prácticas Kanban (tablero, WIP) dentro del Sprint ("Scrumban").

---

## 4. Ventajas y riesgos

| Categoría | Beneficios | Limitaciones / Riesgos | Trade-off típico |
|---|---|---|---|
| **Adaptación al cambio** | Respuesta rápida a nuevas prioridades | Alcance poco definido puede volverse "scope creep" | Flexibilidad vs. previsibilidad de alcance |
| **Entrega de valor** | Retorno temprano; retroalimentación real | Entregar rápido sin calidad genera deuda técnica | Velocidad vs. calidad sostenida |
| **Colaboración** | Alineación entre negocio y técnico | Requiere disponibilidad constante del cliente/PO | Participación del cliente vs. su tiempo disponible |
| **Equipos** | Autonomía, motivación, responsabilidad compartida | Dependencia de personas clave; conflictos sin liderazgo | Autonomía vs. coordinación entre equipos |
| **Documentación** | Menos desperdicio documental | Pérdida de conocimiento si no se documenta lo esencial | Ligereza vs. trazabilidad (críticas en entornos regulados) |
| **Planeación y costos** | Visibilidad frecuente del avance | Difícil comprometer costo/fecha fijos en contratos tradicionales | Adaptabilidad vs. certeza contractual |
| **Escalabilidad** | Funciona muy bien en equipos pequeños | Escalar a muchos equipos exige marcos adicionales (SAFe, LeSS, etc.) | Simplicidad vs. alineación a gran escala |
| **Cultura** | Mejora continua, transparencia | "Ágil de nombre": ceremonias sin cambio cultural | Adopción superficial vs. transformación real |

**Cuándo NO conviene (o conviene con cautela):** requisitos totalmente estables y bien conocidos, entornos con regulación estricta que exige documentación previa (se puede adaptar, pero con costo), equipos sin acceso al cliente, o cuando la organización no tolera la transparencia ni la autonomía del equipo.

---

# 6. SCRUM

##  Conceptos base

**Propósito.** Scrum es un marco ligero que ayuda a personas, equipos y organizaciones a generar valor mediante soluciones adaptativas para problemas complejos. Se basa en el **empirismo** (el conocimiento viene de la experiencia) y el **pensamiento Lean**.

**Tres pilares del empirismo:**

1. **Transparencia:** el trabajo y el progreso son visibles para quienes lo necesitan.
2. **Inspección:** se revisa frecuentemente el avance y el producto.
3. **Adaptación:** se ajusta el rumbo cuando se detecta una desviación.

**Valores:** compromiso, enfoque, apertura, respeto y coraje.

**Cuándo usarlo:** cuando el problema es complejo, hay incertidumbre sobre el producto o la tecnología, se puede entregar en incrementos y existe un equipo estable.

```
        ┌────────────────────── SPRINT (1–4 semanas) ──────────────────────┐
        │                                                                  │
Product │  Sprint     Trabajo diario      Sprint        Sprint             │ Incremento
Backlog ─▶ Planning ─▶ (Daily Scrum) ───▶ Review ────▶ Retrospective ─────▶ utilizable
        │                                                                  │
        └──────────────────────────────────────────────────────────────────┘
```

##  Roles

> Nota: la Guía de Scrum 2020 agrupa los roles en un único **Scrum Team** (Product Owner, Scrum Master y Developers) y sustituye el término "Development Team" por "Developers". Aquí se usa "Development Team" en el sentido tradicional, equivalente a Developers.

###  Product Owner (PO)

- **Responsabilidades:** maximizar el valor del producto; definir y comunicar el Product Goal; crear, ordenar y comunicar los ítems del Product Backlog; ser una sola persona (no un comité).
- **Errores frecuentes:**
  - Actuar como "pasamanos" sin autoridad para decidir.
  - No estar disponible para resolver dudas.
  - Dictar *cómo* se desarrolla en lugar de *qué* y *por qué*.
  - Backlog desordenado o con ítems demasiado grandes.

### Scrum Master (SM)

- **Responsabilidades:** ser responsable de que Scrum se entienda y se aplique; remover impedimentos; facilitar eventos; coachear al equipo y a la organización. Es un **líder servicial**, no un jefe.
- **Errores frecuentes:**
  - Comportarse como gerente de proyecto que asigna tareas.
  - Resolver todos los problemas en lugar de enseñar al equipo a hacerlo.
  - Limitarse a agendar reuniones.
  - No proteger al equipo de interrupciones externas.

###  Development Team (Developers)

- **Responsabilidades:** crear cualquier aspecto de un Incremento utilizable cada Sprint; planear el Sprint Backlog; adherirse a la Definition of Done; auto-organizarse. Es multifuncional (diseño, desarrollo, pruebas, etc.).
- **Errores frecuentes:**
  - Esperar a que "alguien" les diga qué hacer.
  - Especialización rígida ("eso no me toca").
  - Dejar las pruebas para el final.
  - Comprometerse con más trabajo del que pueden terminar.

## 7. Artefactos

Cada artefacto tiene un **compromiso** que aporta transparencia.

| Artefacto | Compromiso | Definición |
|---|---|---|
| **Product Backlog** | Product Goal | Lista ordenada y emergente de lo necesario para mejorar el producto. Fuente única de trabajo. |
| **Sprint Backlog** | Sprint Goal | Ítems elegidos para el Sprint + plan para entregarlos. Pertenece a los Developers. |
| **Increment** | Definition of Done | Peldaño concreto hacia el Product Goal; debe ser utilizable y cumplir la DoD. |

### Criterios de calidad por artefacto

- **Product Backlog:** ordenado por valor y riesgo; los ítems de arriba están **refinados** (pequeños, claros, estimables); visible para todos; vivo (se actualiza).
- **Sprint Backlog:** alineado al Sprint Goal; realista según la capacidad del equipo; actualizado diariamente.
- **Increment:** integrado, probado, cumple la DoD y está en condición de ser liberado (aunque el PO decida no hacerlo aún).

### Definition of Done (DoD) vs. Criterios de aceptación

| | **Definition of Done** | **Criterios de aceptación** |
|---|---|---|
| **Alcance** | Aplica a **todos** los ítems | Específicos de **cada** historia de usuario |
| **Responde** | ¿Está el trabajo terminado con calidad? | ¿Hace lo que el usuario/negocio necesita? |
| **Quién lo define** | El equipo (con la organización) | El PO con el equipo |
| **Naturaleza** | Calidad técnica y de proceso | Comportamiento funcional |
| **Ejemplos** | Código revisado por pares; pruebas unitarias en verde; sin vulnerabilidades críticas; documentación actualizada; desplegado en entorno de pruebas | "Dado que estoy autenticado, cuando selecciono un producto, entonces se agrega al carrito y el total se actualiza" |

Un ítem se considera terminado solo si cumple **ambos**: sus criterios de aceptación **y** la DoD.

## 8. Eventos

Los tiempos son máximos sugeridos por la Guía de Scrum para un Sprint de **un mes**; en Sprints más cortos, el tiempo suele ser proporcionalmente menor.

| Evento | Objetivo | Duración sugerida | Antipatrón típico |
|---|---|---|---|
| **Sprint** | Contenedor de todos los eventos; produce un Incremento. | 1–4 semanas (fija) | Extender o acortar el Sprint a mitad por no terminar; cambiar el alcance sin consulta. |
| **Sprint Planning** | Definir *por qué* es valioso el Sprint (Sprint Goal), *qué* se puede hacer y *cómo* se hará. | Hasta 8 h (Sprint de 1 mes) | El PO o el SM asignan tareas; no hay Sprint Goal, solo una lista de ítems. |
| **Daily Scrum** | Inspeccionar el progreso hacia el Sprint Goal y adaptar el plan. | 15 min | Reunión de reporte al jefe, ronda "ayer/hoy/mañana" mecánica, que se alarga en discusión técnica. |
| **Sprint Review** | Inspeccionar el resultado con los interesados y adaptar el Product Backlog. | Hasta 4 h | Demo unilateral sin retroalimentación; presentar "casi terminado"; usarla solo como aprobación formal. |
| **Sprint Retrospective** | Planear mejoras de calidad y efectividad del equipo. | Hasta 3 h | Quejas sin acciones; mismos temas cada Sprint; asistir sin participar; no dar seguimiento a las acciones acordadas. |

*Refinamiento del Product Backlog* no es un evento formal, pero es una actividad continua (típicamente ≤ 10 % de la capacidad).

## 9. Métricas

| Métrica | ¿Qué es? | Cómo interpretarla | Cómo **no** usarla |
|---|---|---|---|
| **Velocity** | Cantidad de trabajo (p. ej., puntos de historia) completado por Sprint. | Ayuda a **pronosticar** cuánto podría completar el equipo en próximos Sprints; observar tendencia (promedio de varios Sprints). | Compararla entre equipos; usarla para evaluar desempeño individual; fijarla como meta (se infla la estimación, Ley de Goodhart). |
| **Burndown** | Trabajo restante en el Sprint (o release) vs. tiempo. | Si la línea real queda por encima de la ideal, hay riesgo de no alcanzar el Sprint Goal; escalones bruscos indican ítems demasiado grandes. | Interpretarla como "culpa" del equipo; usarla como único indicador de salud. Ignora la calidad y el valor. |
| **WIP (Work in Progress)** | Cantidad de ítems en curso simultáneamente. | Un WIP alto suele indicar multitarea, menor foco y tiempos de entrega más largos. | Verlo solo como número sin considerar el contexto del Sprint Goal. |

**Principios para usar métricas:** servir al aprendizaje del equipo, no a la vigilancia; combinar varias; acompañar con preguntas ("¿por qué?"); y recordar que la mejor medida de progreso es un **Incremento funcionando que aporta valor**.

---

# 10. KANBAN

##  Fundamentos

Kanban ("tarjeta visual" en japonés) tiene origen en el sistema de producción de Toyota. Aplicado al conocimiento (David J. Anderson), es un método para **gestionar el flujo de trabajo** y mejorar de forma evolutiva, partiendo de **lo que ya se hace**.

### Principios

1. **Comenzar con lo que haces ahora:** no requiere reorganizar roles de inicio.
2. **Acordar buscar cambio evolutivo:** cambios pequeños e incrementales.
3. **Respetar el proceso actual, roles y responsabilidades.**
4. **Fomentar el liderazgo en todos los niveles.**

### Las seis prácticas

| Práctica | Qué significa | Ejemplo |
|---|---|---|
| **Visualizar el trabajo** | Hacer visible cada ítem y su estado. | Tablero con columnas por etapa. |
| **Limitar el WIP** | Restringir cuánto trabajo está en curso. | Máximo 3 tarjetas en "Desarrollo". |
| **Gestionar el flujo** | Medir y optimizar el movimiento del trabajo. | Revisar cuellos de botella cada semana. |
| **Hacer explícitas las políticas** | Reglas claras y visibles de cómo se trabaja. | "Una tarjeta pasa a Pruebas solo con revisión de código aprobada". |
| **Implementar bucles de retroalimentación** | Revisiones regulares para aprender. | Reunión diaria de tablero, revisión de entrega, retrospectiva operativa. |
| **Mejorar colaborativamente, evolucionar experimentalmente** | Usar hipótesis y datos para cambiar. | "Si reducimos el WIP de 4 a 3, el cycle time bajará". |

## Tablero Kanban para un equipo de desarrollo

**Contexto supuesto:** equipo de 5 personas (3 desarrolladores, 1 QA, 1 analista/UX).

```
┌──────────┬─────────┬───────────┬────────────┬──────────┬─────────┬────────────┬────────┐
│ Backlog  │  Listo  │ Análisis  │ Desarrollo │ Revisión │ Pruebas │  Listo p/  │ Hecho  │
│          │ (Ready) │  WIP: 2   │   WIP: 3   │  WIP: 2  │ WIP: 2  │ desplegar  │        │
│          │ WIP: 5  │           │            │          │         │  WIP: 3    │        │
├──────────┼─────────┼───────────┼────────────┼──────────┼─────────┼────────────┼────────┤
│ [Idea A] │ [US-12] │  [US-10]  │  [US-07]   │ [US-05]  │ [US-03] │  [US-02]   │ [US-01]│
│ [Idea B] │ [US-11] │           │  [US-08]   │          │         │            │        │
│ [Idea C] │         │           │  [US-09]   │          │         │            │        │
└──────────┴─────────┴───────────┴────────────┴──────────┴─────────┴────────────┴────────┘
        ◀─── Se extrae trabajo de derecha a izquierda (sistema pull) ───
```

### Razonamiento de los límites WIP

| Columna | Límite | Justificación |
|---|---|---|
| Backlog | Sin límite | Es una lista de opciones, no trabajo comprometido. |
| Listo (Ready) | 5 | Mantiene a los desarrolladores abastecidos sin acumular requisitos que envejecen y se vuelven obsoletos. |
| Análisis | 2 | Un analista; permite una historia en curso y otra en espera/validación. |
| Desarrollo | 3 | Un ítem por desarrollador (3 devs): evita multitarea y favorece terminar antes de empezar. |
| Revisión | 2 | La revisión de código es rápida; un límite bajo obliga a revisar antes de iniciar nuevo trabajo. |
| Pruebas | 2 | Un QA; dos ítems permiten alternar si uno está bloqueado. |
| Listo p/ desplegar | 3 | Evita acumular trabajo terminado sin liberar; es una señal de alerta si se llena. |

**Reglas de ajuste:** como punto de partida, WIP total ≈ tamaño del equipo (o ligeramente menor); si una columna se llena constantemente, es candidata a cuello de botella; si siempre está vacía, el límite puede ser demasiado bajo o el flujo está subutilizado. Se ajusta experimentando.

##  Métricas de flujo

| Métrica | Definición | Para qué sirve |
|---|---|---|
| **Lead time** | Tiempo desde que se solicita un ítem hasta que se entrega. | Es lo que percibe el cliente. |
| **Cycle time** | Tiempo desde que se comienza a trabajar en el ítem hasta que se termina. | Mide la eficiencia del proceso interno. |
| **Throughput** | Cantidad de ítems terminados por unidad de tiempo (p. ej., por semana). | Capacidad y pronósticos. |
| **Work Item Age** | Antigüedad de un ítem en curso (desde que inició). | Detecta ítems atascados antes de que terminen. |
| **WIP** | Ítems en proceso. | Se relaciona con las demás mediante la Ley de Little. |

**Ley de Little:** `Cycle time promedio = WIP promedio / Throughput promedio`. Si se baja el WIP y el throughput se mantiene, el cycle time disminuye.

```
Lead time  ├──────────────────────────────────────────────┤
           Solicitud     Inicio de trabajo       Entrega
Cycle time                ├─────────────────────┤
```

### Diagrama de Flujo Acumulado (CFD) y su lectura

El CFD apila, por día, el número acumulado de ítems en cada estado.

```
Ítems
acumulados
  │                                          ╱ Hecho
  │                                     ╱╱╱╱
  │                              ╱╱╱╱╱╱  ╱ En pruebas
  │                         ╱╱╱╱╱     ╱╱
  │                    ╱╱╱╱╱     ╱╱╱╱╱  En desarrollo
  │               ╱╱╱╱╱     ╱╱╱╱╱
  │          ╱╱╱╱╱     ╱╱╱╱╱            Backlog
  └───────────────────────────────────────── Tiempo
```

**Cómo leerlo:**

- **Distancia vertical** entre dos bandas = cantidad de ítems en esa etapa (WIP).
- **Distancia horizontal** = tiempo aproximado que tarda un ítem en recorrer las etapas (cycle/lead time).
- **Bandas paralelas y estables:** flujo saludable.
- **Una banda que se ensancha:** hay acumulación; posible cuello de botella en esa etapa.
- **Línea de "Hecho" plana:** no se está entregando (bloqueo o trabajo atascado).
- **Escalones:** entregas por lotes en lugar de flujo continuo.

##  Políticas y clases de servicio

### Políticas explícitas (ejemplos)

| Área | Política |
|---|---|
| Entrada a "Listo" | La historia tiene criterios de aceptación y está estimada como pequeña (≤ 3 días). |
| Entrada a "Revisión" | Pruebas unitarias en verde y pipeline de CI aprobado. |
| WIP | Si una columna está al límite, nadie inicia trabajo nuevo; se ayuda a desbloquear. |
| Bloqueos | Un ítem bloqueado se marca visiblemente y se atiende en la reunión diaria. |
| Definition of Done | Ítem desplegado en producción con monitoreo activo. |

### Clases de servicio

| Clase | Descripción | Política típica | Cuándo aplicarla |
|---|---|---|---|
| **Expedite (urgente)** | Impacto inmediato y alto costo por demora. | Máximo 1 a la vez; puede exceder el WIP; se deja todo lo demás. | Caídas en producción, vulnerabilidad crítica. |
| **Fecha fija** | Tiene una fecha límite con penalización. | Se inicia con tiempo suficiente según el cycle time histórico (p. ej., percentil 85). | Cumplimiento legal, lanzamiento comprometido. |
| **Estándar** | Valor normal, sin fecha crítica. | Se atiende por orden de prioridad/FIFO. | La mayor parte del trabajo. |
| **Intangible** | Valor a futuro, sin costo inmediato por demora. | Se atiende con una capacidad reservada (p. ej., 10–20 %). | Deuda técnica, refactorización, capacitación. |

##  Cuándo usar Kanban vs. otros enfoques

| Situación | Recomendación |
|---|---|
| Trabajo por **tickets** o soporte con demanda continua e impredecible | **Kanban** (no tiene sentido planear un Sprint cerrado) |
| **Alta variabilidad** en tamaño y prioridad de tareas | **Kanban**, con clases de servicio |
| Mejorar un proceso existente sin cambios drásticos | **Kanban** |
| Desarrollo de un producto con objetivos por iteración y fuerte necesidad de cadencia y compromiso de equipo | **Scrum** |
| Alta incertidumbre sobre qué construir | **Design Thinking** + Scrum/Kanban |
| Mantenimiento + nuevas funcionalidades en el mismo equipo | **Scrumban** (Scrum con tablero Kanban y WIP) |

**Límites de Kanban:** al no imponer cadencia ni roles, puede degenerar en un "tablero de tareas" sin disciplina de WIP ni mejora; requiere madurez para usar datos.

---

# 15. DESIGN THINKING

##  Visión general

**Design Thinking (DT)** es un enfoque **centrado en las personas** para resolver problemas complejos y mal definidos. Combina empatía con el usuario, creatividad y experimentación rápida. Popularizado por IDEO y la d.school de Stanford.

### Principios

1. **Centrado en el humano:** el punto de partida son las necesidades reales del usuario.
2. **Colaboración multidisciplinaria:** perspectivas diversas.
3. **Divergir y converger:** primero muchas opciones, luego elegir.
4. **Aprender haciendo:** prototipos rápidos y baratos.
5. **Iteración:** el proceso no es lineal; se vuelve atrás cuando se aprende algo nuevo.
6. **Tolerar el error temprano:** fallar rápido para fallar barato.

### Encaje con el desarrollo de software

Muchos proyectos fracasan no por mala ejecución, sino por **construir lo incorrecto**. DT actúa **antes y alrededor** del desarrollo para validar la necesidad, el usuario y la propuesta de valor, produciendo hipótesis y requisitos con evidencia.

##  Fases

```
  EMPATIZAR ──▶ DEFINIR ──▶ IDEAR ──▶ PROTOTIPAR ──▶ PROBAR
      ▲                                                  │
      └──────────── iteración y aprendizaje ◀────────────┘
```

| Fase | Objetivo | Técnicas sugeridas | Entregables mínimos |
|---|---|---|---|
| **1. Empatizar** | Comprender al usuario, su contexto, necesidades y frustraciones. | Entrevistas, observación, *shadowing*, encuestas, mapa de empatía, *journey map* inicial. | Notas/insights de investigación, mapa de empatía, lista de hallazgos. |
| **2. Definir** | Sintetizar los hallazgos en un problema claro y accionable. | Persona, *Point of View* (POV), preguntas "¿Cómo podríamos…?" (HMW), agrupación por afinidad. | Persona(s), declaración del problema, 3–5 preguntas HMW. |
| **3. Idear** | Generar muchas soluciones posibles y elegir las más prometedoras. | Lluvia de ideas, *Crazy 8s*, SCAMPER, matriz impacto/esfuerzo, votación por puntos. | Conjunto de ideas, ideas priorizadas, hipótesis a validar. |
| **4. Prototipar** | Hacer tangible la idea de forma barata y rápida. | Bocetos, *wireframes* de baja fidelidad, *storyboards*, prototipos de papel, maquetas clicables, "Mago de Oz". | Prototipo de baja fidelidad con los flujos clave. |
| **5. Probar** | Validar con usuarios reales y aprender. | Pruebas de usabilidad, observación, entrevistas post-prueba, matriz de retroalimentación (agrada / critica / preguntas / ideas). | Resultados de pruebas, lista de ajustes, decisión: iterar, pivotar o avanzar. |

##  Mini-caso: "Cola Cero" (cafetería universitaria)

**Problema hipotético:** en una universidad, los estudiantes pierden entre 15 y 25 minutos en la fila de la cafetería durante el receso y muchos terminan sin comer o llegan tarde a clase.

### Actividades por fase

| Fase | Actividades realizadas | Resultado |
|---|---|---|
| **Empatizar** | Observar la fila en horas pico; entrevistar a 8 estudiantes, 2 docentes y 2 trabajadores de la cafetería; cronometrar tiempos. | Los estudiantes no saben cuánto tardarán; el personal pierde tiempo cobrando en efectivo; el pico es de 10:00 a 10:30; muchos pedirían algo rápido si supieran que está listo. |
| **Definir** | Crear la persona "Ana, 20 años, estudiante con 30 min de receso". Redactar el POV. | *"Ana necesita obtener su comida de forma rápida y predecible durante un receso de 30 min porque no puede arriesgarse a llegar tarde a clase."* HMW: ¿Cómo podríamos reducir la incertidumbre del tiempo de espera? ¿Cómo podríamos separar el pedido del pago en el mostrador? |
| **Idear** | Sesión de lluvia de ideas con estudiantes y personal; *Crazy 8s*; votación. | Ideas: pedido previo por app, casilleros de recogida, combos "rápidos" preparados, pantalla con tiempo estimado. Priorizada: **pedido previo con hora de recogida**. |
| **Prototipar** | Boceto en papel de 3 pantallas y flujo de recogida. | Prototipo de baja fidelidad (ver abajo). |
| **Probar** | Probar con 6 estudiantes en la cafetería; medir si completan un pedido y qué les confunde. | Aprendizajes: querían ver el tiempo estimado antes de pagar; el código de recogida debía ser más visible. Se itera el prototipo. |

### Prototipo de baja fidelidad (texto)

```
┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
│ COLA CERO          │   │ TU PEDIDO          │   │ ✔ PEDIDO LISTO     │
│                    │   │                    │   │                    │
│ Menú rápido        │   │ 1x Torta de pollo  │   │ Pasa por tu pedido │
│ ┌────────────────┐ │   │ 1x Agua 600 ml     │   │ Mostrador B        │
│ │ Torta   $45  + │ │   │                    │   │                    │
│ │ Ensalada $50 + │ │   │ Total: $60         │   │   CÓDIGO: 4 7 2    │
│ │ Agua    $15  + │ │   │ Recoger a las:     │   │                    │
│ └────────────────┘ │   │ [ 10:20 ▼ ]        │   │ Tiempo ahorrado:   │
│                    │   │ Espera estimada:   │   │ ~15 min            │
│ [ Ver pedido (2) ] │   │ 4 min              │   │                    │
│                    │   │ [ Pagar y confirmar]│  │                    │
└────────────────────┘   └────────────────────┘   └────────────────────┘
     Pantalla 1               Pantalla 2               Pantalla 3
```

**Hipótesis a validar con métricas:** reducir el tiempo promedio de espera a menos de 5 minutos para pedidos anticipados.

##  Relación de DT con SDLC y Ágil

### Cómo reduce el riesgo de construir lo incorrecto

| Riesgo | Cómo lo mitiga DT |
|---|---|
| Resolver un problema que no existe | La fase de Empatizar valida el problema con usuarios reales. |
| Requisitos basados en suposiciones | Las hipótesis se prueban con prototipos antes de programar. |
| Alto costo de corregir tarde | Prototipos de baja fidelidad cuestan horas, no meses. |
| Soluciones que nadie quiere usar | Pruebas de usabilidad tempranas y repetidas. |

### Articulación con el ciclo de vida

| Etapa | Rol de DT | Cómo se conecta |
|---|---|---|
| **Descubrimiento** (antes del desarrollo) | Empatizar, Definir, Idear | Genera Product Backlog inicial, personas y Product Goal. |
| **Validación** | Prototipar y Probar | Reduce la incertidumbre; decide qué construir y qué descartar. |
| **Construcción** (con Scrum/Kanban) | Retroalimentación continua | Historias de usuario con insights reales; pruebas de usabilidad en cada Sprint Review. |
| **Evolución** | Observación del uso | Nuevas necesidades alimentan el backlog. |

**Con Scrum:** el *Dual-Track Agile* ejecuta dos pistas en paralelo: **descubrimiento** (DT, validar) y **entrega** (Scrum, construir). Los resultados del descubrimiento se convierten en ítems del Product Backlog.
**Con Kanban:** se puede tener un tablero de descubrimiento (Investigar → Sintetizar → Idear → Prototipar → Validar) que alimenta el tablero de desarrollo.

---

## 19. Conclusiones y aplicaciones

**Ágil es una forma de pensar antes que un conjunto de ceremonias.** Los marcos son herramientas; el valor está en entregar pronto, aprender y adaptarse. Aplicar Scrum "por la forma" sin transparencia ni mejora continua produce los mismos problemas que se querían evitar.

 **Cada marco resuelve un problema distinto.** Design Thinking reduce el riesgo de construir lo incorrecto; Scrum organiza la construcción incremental de un producto complejo; Kanban optimiza el flujo y es ideal cuando la demanda es continua y variable. La combinación (Dual-Track, Scrumban) suele ser más realista que la adopción "pura".

 **Las métricas deben servir al aprendizaje, no al control.** Velocity, burndown o cycle time aportan información, pero se vuelven dañinas al convertirse en metas o en comparaciones entre personas.

 **Aplicaciones:**
   - **Académico:** en proyectos de materia o integradores, usar Scrum con Sprints de 1–2 semanas, un Product Backlog compartido y una retrospectiva breve ayuda a distribuir el trabajo, evitar la entrega "de último minuto" y mejorar la coordinación del equipo. Un tablero Kanban en herramientas como Trello, GitHub Projects o Jira hace visible quién hace qué. Design Thinking es útil al inicio de proyectos de tesis o emprendimiento para validar la necesidad con usuarios reales.
   - **Profesional:** en prácticas, servicio social o primeros empleos, es probable que encuentre equipos que usan Scrum o Kanban; entender roles, artefactos y métricas permite integrarse más rápido y proponer mejoras con criterio. Para soporte y mantenimiento, Kanban con clases de servicio es especialmente pertinente.

**Retos personales de adopción:** trabajar en equipos pequeños con disponibilidad limitada, definir una Definition of Done desde el inicio y practicar la comunicación transparente de impedimentos.

---

## 20. Referencias

1. Beck, K., Beedle, M., van Bennekum, A., et al. (2001). *Manifesto for Agile Software Development* y *Principles behind the Agile Manifesto*. https://agilemanifesto.org
2. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide: The Definitive Guide to Scrum: The Rules of the Game*. https://scrumguides.org
3. Anderson, D. J. (2010). *Kanban: Successful Evolutionary Change for Your Technology Business*. Blue Hole Press.
4. Kanban University / Scrum.org (2021). *The Kanban Guide for Scrum Teams*. https://kanbanguides.org
5. Brown, T. (2008). Design Thinking. *Harvard Business Review*, 86(6), 84–92.
6. Hasso Plattner Institute of Design at Stanford (d.school). *An Introduction to Design Thinking: Process Guide* y *Bootcamp Bootleg*. https://dschool.stanford.edu
7. Vacanti, D. S. (2015). *Actionable Agile Metrics for Predictability: An Introduction*. Actionable Agile Press.
8. Cohn, M. (2010). *Succeeding with Agile: Software Development Using Scrum*. Addison-Wesley.
9. Cagan, M. (2017). *Inspired: How to Create Tech Products Customers Love* (2.ª ed.). Wiley. *(Referencia para Dual-Track Agile y descubrimiento de producto.)*
