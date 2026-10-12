# Configuraciones mecánicas de robots móviles

---

## 1. Conceptos básicos

**¿Qué es un robot móvil?**
Es una máquina capaz de desplazarse por su entorno (suelo, agua o aire) con cierto grado de autonomía, usando sensores para percibir el entorno y actuadores para moverse. No está atado a una base fija.

**Diferencia con un robot manipulador fijo.**
Un manipulador (por ejemplo un brazo industrial) está anclado a una base y solo alcanza los puntos dentro de su espacio de trabajo. Un robot móvil cambia de lugar, por lo que su espacio de trabajo es, en principio, todo el entorno por el que puede navegar. Esto lo obliga a resolver problemas que el brazo no tiene, como la localización y la evasión de obstáculos.

**Función del sistema de locomoción.**
Convierte la energía de los motores en desplazamiento del robot completo. Determina hacia dónde puede moverse, con qué rapidez, qué tan preciso es su movimiento y qué terrenos puede atravesar.

**Movilidad omnidireccional.**
Un robot es omnidireccional cuando puede moverse en cualquier dirección del plano (adelante, atrás, a los lados o en diagonal) y además girar, sin necesidad de reorientarse antes. En términos técnicos, tiene tres grados de libertad controlables de forma independiente en el plano: x, y y orientación.

**Relación entre las ruedas y los movimientos posibles.**
Una rueda convencional solo puede generar fuerza útil en la dirección en que apunta, y resiste el deslizamiento hacia los lados. Por eso, *cómo se coloquen y orienten las ruedas* (y de qué tipo sean) define qué movimientos son posibles: un robot con ruedas convencionales no puede moverse de lado, mientras que uno con ruedas especiales (Omni o Mecanum) sí.

**Aplicaciones de robots móviles:**
- Logística en almacenes (transporte de estantes y paquetes).
- Aspiradoras robóticas domésticas.
- Exploración espacial (rovers).
- Vehículos autónomos y de conducción asistida.
- Inspección de instalaciones industriales y agricultura de precisión.
- Educación e investigación.

---

## 2. Robot diferencial con rueda de castor

### Descripción

- **Ruedas motrices:** dos ruedas montadas sobre el mismo eje (una a cada lado del chasis), cada una con su propio motor. Se controlan de forma independiente.
- **Rueda de castor (rueda loca):** una rueda libre (de pivote o esfera) colocada normalmente en la parte frontal o trasera. No tiene motor ni dirección propia: solo sirve de **apoyo** para que el chasis no se incline, y gira libremente para seguir al robot.
- **Línea recta:** ambas ruedas giran a la misma velocidad y en el mismo sentido.
- **Giro a izquierda o derecha:** se hace que la rueda del lado contrario al giro gire más rápido. Si la rueda derecha va más rápido que la izquierda, el robot gira hacia la izquierda, y viceversa.
- **Cuando una rueda gira más rápido que la otra:** el robot describe una curva. Entre mayor sea la diferencia de velocidades, más cerrada será la curva.
- **Giro sobre su propio eje:** las ruedas giran a la misma velocidad pero en sentidos opuestos; el centro de giro queda en el punto medio entre las ruedas.

### Ventajas
- Mecánicamente simple y barata (dos motores).
- Control sencillo de entender.
- Puede girar sobre su propio eje, lo que ayuda en espacios reducidos.

### Limitaciones
- No puede desplazarse de lado (restricción no holonómica).
- La rueda de castor puede introducir un pequeño error al cambiar de dirección.
- Puede patinar si las ruedas pierden tracción, lo que afecta la odometría.

### Aplicaciones
Aspiradoras robóticas, robots educativos, robots seguidores de línea, y plataformas de investigación como TurtleBot.

### Diagrama (vista superior)

```
                 ▲  Sentido de avance (frente)
                 │
        ┌────────┴────────┐
        │                 │
   ┌──┐ │                 │ ┌──┐
   │RI│ │        ⊕        │ │RD│     RI = Rueda izquierda (motriz)
   │  │ │   eje de giro   │ │  │     RD = Rueda derecha (motriz)
   └──┘ │   aproximado    │ └──┘     ⊕  = Punto medio entre ruedas
        │                 │                (eje de giro al girar en sitio)
        │       ( C )     │          C  = Rueda de castor (libre)
        └─────────────────┘
```

> Nota: en el dibujo la rueda de castor va atrás; en otros robots va adelante. El resultado funcional es el mismo.

### Movimiento según el sentido de cada rueda

| Rueda izquierda | Rueda derecha | Movimiento del robot |
|---|---|---|
| Avanza | Avanza | Avanza en línea recta hacia adelante |
| Detenida | Avanza | Gira hacia la **izquierda**, pivotando alrededor de la rueda izquierda (curva cerrada) |
| Avanza | Detenida | Gira hacia la **derecha**, pivotando alrededor de la rueda derecha |
| Avanza | Retrocede | Gira sobre su propio eje en sentido **horario** (hacia la derecha) |
| Retrocede | Avanza | Gira sobre su propio eje en sentido **antihorario** (hacia la izquierda) |
| Retrocede | Retrocede | Retrocede en línea recta |

---

## 3. Robots omnidireccionales con ruedas Omni

### La rueda Omni

- **Construcción:** es una rueda cuyo contorno está formado por pequeños **rodillos** montados alrededor de su perímetro, con sus ejes **perpendiculares al eje principal** de la rueda (a 90°).
- **Para qué sirven los rodillos:** permiten que la rueda gire libremente en la dirección lateral (paralela a su eje), mientras el motor la impulsa en la dirección normal de rodadura.
- **Dirección en la que genera fuerza:** el motor impulsa la rueda en la dirección perpendicular a su eje (como una rueda normal). Esa es la dirección *activa*.
- **Por qué se desliza libremente en la otra dirección:** cuando algo empuja a la rueda a lo largo de su eje, los rodillos giran sobre sí mismos en lugar de arrastrarse contra el suelo, así que casi no ofrecen resistencia.
- **Qué permite:** como cada rueda aporta fuerza solo en una dirección y no estorba en la otra, se pueden combinar varias ruedas con orientaciones distintas para generar movimientos que con ruedas convencionales no se podrían, como desplazarse hacia un costado.

### Configuración de tres ruedas

**Distribución:** las ruedas se colocan alrededor del chasis a **120°** una de otra, y cada una está orientada de forma tangencial (su dirección activa es perpendicular al radio que la une con el centro).

```
                 Frente (+y)
                    ▲
              ┌─────┴─────┐
              │    [1]    │       Flecha en cada rueda = dirección activa
              │    ◄──►   │       (tangente al círculo)
              │           │
        [2]   │     ●     │   [3]   ● = centro del robot
        ╲     │           │     ╱
         ╲    └───────────┘    ╱
          ╲                   ╱
    Rueda 1 a 90°, Rueda 2 a 210°, Rueda 3 a 330°
    (separadas 120°)
```

Una forma práctica de entender las velocidades (con signo positivo = giro antihorario de la rueda vista desde arriba, ruedas en 90°, 210° y 330°) es esta, donde `vx` es velocidad lateral, `vy` frontal y `ω` rotación:

```
v1 = -sin(90°)·vx  + cos(90°)·vy  + R·ω
v2 = -sin(210°)·vx + cos(210°)·vy + R·ω
v3 = -sin(330°)·vx + cos(330°)·vy + R·ω
```

| Movimiento | Rueda 1 (frontal) | Rueda 2 (trasera izq.) | Rueda 3 (trasera der.) |
|---|---|---|---|
| Adelante | Detenida | Gira en un sentido | Gira en el sentido contrario (misma magnitud) |
| Atrás | Detenida | Sentido inverso al anterior | Sentido inverso al anterior |
| Lateral | Gira a velocidad completa | Gira en sentido opuesto a 1, a la mitad de velocidad | Igual que 2 |
| Diagonal | Se suman los dos casos anteriores (combinación de lateral y frontal) | | |
| Giro sobre su eje | Las tres giran en el **mismo sentido** a igual velocidad | | |

- **Cuando las tres giran a velocidades distintas:** el movimiento resultante es la combinación (suma vectorial) de los efectos de cada rueda, lo que produce trayectorias curvas con traslación y rotación simultáneas. Es la ventaja principal: se controlan x, y y rotación de forma independiente.

### Configuración de cuatro ruedas

- **Colocación:** cuatro ruedas Omni, normalmente separadas 90° (en forma de "+" o de "X"), con la dirección activa tangente al chasis. En la disposición en "+", las ruedas opuestas trabajan por pares: un par genera el movimiento en x y el otro en y.
- **Combinación de velocidades:** para ir hacia adelante se mueve el par de ruedas que está alineado con esa dirección (en sentidos que sumen), y el otro par queda libre rodando en su dirección lateral. Para movimientos diagonales se mueven ambos pares. Para girar, las cuatro giran en el mismo sentido.
- **Diferencias frente a tres ruedas:** el sistema de cuatro tiene **una rueda extra**, lo que da más tracción y capacidad de carga, pero el sistema queda *sobredeterminado*: tres ruedas bastan para tres grados de libertad. Con cuatro, las velocidades deben coordinarse con más cuidado.
- **Ventajas:** mejor soporte y estabilidad, mayor capacidad de carga y mayor tracción total.
- **Limitaciones:** más costo y complejidad; con cuatro puntos de apoyo, si el suelo es irregular una rueda puede perder contacto, y entonces hay deslizamiento y pérdida de precisión.

---

## 4. Robot omnidireccional con ruedas Mecanum

### Características

- **Construcción:** es una rueda con rodillos montados en su perímetro, pero con sus ejes inclinados **45°** respecto al eje de la rueda (en la Omni están a 90°). Los rodillos suelen ser de caucho para dar agarre. La rueda Mecanum fue inventada por Bengt Ilon, ingeniero de la empresa sueca Mecanum AB, que patentó el diseño en 1975.
- **Diferencia con la rueda Omni:** en la Omni, la fuerza de la rueda se genera en una sola dirección (la de rodadura). En la Mecanum, al estar inclinados los rodillos, la fuerza que el suelo devuelve a la rueda queda **a 45°** de la dirección de rodadura, es decir, tiene una componente frontal y una lateral.
- **Por qué cuatro ruedas:** con cuatro ruedas colocadas en esquinas, se pueden **cancelar** las componentes laterales (para ir recto) o **sumarlas** (para ir de lado). Cuatro ruedas también ofrecen una base de apoyo estable y rectangular.
- **Orientación respecto al chasis:** las ruedas se instalan en pares con orientación de rodillos **opuesta** (imagen en espejo). Vistas desde arriba, los rodillos en contacto con el suelo forman una **"X"**.

### Diagrama (vista superior, configuración en X)

```
                    Frente  ▲

       ┌───────┐                  ┌───────┐
       │ \ \ \ │                  │ / / / │
       │  \ \  │  Delantera       │  / /  │  Delantera
       │ \ \ \ │  izquierda (DI)  │ / / / │  derecha (DD)
       └───────┘                  └───────┘
                       CHASIS

       ┌───────┐                  ┌───────┐
       │ / / / │                  │ \ \ \ │
       │  / /  │  Trasera         │  \ \  │  Trasera
       │ / / / │  izquierda (TI)  │ \ \ \ │  derecha (TD)
       └───────┘                  └───────┘

   Los rodillos en contacto con el suelo forman una X:
   DI y TD con rodillos "\" ;  DD y TI con rodillos "/"
```

### Combinación de movimientos

- **Avance:** las cuatro ruedas giran hacia adelante; las componentes laterales de cada par se cancelan y queda solo movimiento frontal.
- **Retroceso:** las cuatro giran hacia atrás.
- **Movimiento a un lado:** las ruedas de una misma diagonal giran en el mismo sentido, y las de la otra diagonal en el contrario. Así las componentes frontales se cancelan y las laterales se suman.
- **Diagonal:** se hace girar solo una diagonal (dos ruedas) y la otra queda detenida.
- **Giro sobre el propio eje:** las ruedas del lado izquierdo giran en un sentido y las del derecho en el contrario.

### Tabla de sentido de giro de cada rueda

(↑ = gira hacia adelante, ↓ = gira hacia atrás, ● = detenida. Se asume la configuración en X del diagrama.)

| Movimiento | Delantera izquierda | Delantera derecha | Trasera izquierda | Trasera derecha |
|---|---|---|---|---|
| Avanzar | ↑ | ↑ | ↑ | ↑ |
| Retroceder | ↓ | ↓ | ↓ | ↓ |
| Desplazarse a la izquierda | ↓ | ↑ | ↑ | ↓ |
| Desplazarse a la derecha | ↑ | ↓ | ↓ | ↑ |
| Girar a la izquierda | ↓ | ↑ | ↓ | ↑ |
| Girar a la derecha | ↑ | ↓ | ↑ | ↓ |
| Diagonal adelante-derecha | ↑ | ● | ● | ↑ |
| Diagonal adelante-izquierda | ● | ↑ | ↑ | ● |

> Estos sentidos dependen de cómo se montaron los rodillos. Si un fabricante invierte la orientación de los rodillos, hay que invertir la lógica lateral. Lo mejor es verificarlo con pruebas para evitar errores.

---

## 5. Robot con dirección Ackermann

La **geometría Ackermann** es un esquema de dirección usado en automóviles y en muchos vehículos autónomos, que permite tomar curvas sin que las ruedas se arrastren de lado.

- **Distribución de las ruedas:** cuatro ruedas, dos delanteras y dos traseras, como un auto.
- **Ruedas de dirección:** normalmente las delanteras, que pueden orientarse (girar sobre un eje vertical).
- **Ruedas de tracción:** pueden ser las traseras (tracción trasera), las delanteras o las cuatro.
- **Por qué los ángulos son distintos:** en una curva, todas las ruedas deben seguir círculos con **el mismo centro**. La rueda interior recorre un círculo más pequeño que la exterior, por lo que necesita **un mayor ángulo de giro**. Si ambas ruedas giraran lo mismo, una de ellas tendría que patinar. La geometría Ackermann resuelve esto con un mecanismo (trapecio de dirección) que hace que la rueda interior gire más.
- **Radio de giro:** es la distancia entre el centro de la curva y el centro del vehículo. Cuanto más se gira la dirección, menor es el radio. Existe un **radio mínimo** que depende de la distancia entre ejes y del ángulo máximo de dirección.
- **Por qué no se mueve de lado:** las ruedas traseras (y las delanteras cuando están rectas) solo pueden rodar hacia adelante o hacia atrás; resisten el deslizamiento lateral. Por eso el vehículo no puede trasladarse directamente hacia un costado.
- **Semejanzas con un automóvil:** es *la misma geometría*. Un auto convencional es un vehículo Ackermann.

### Diagrama (vehículo tomando una curva a la izquierda)

```
                       Dirección de desplazamiento
                              ↑
              ┌──┐                    ┌──┐
              │\ │  Rueda interior     │ \│  Rueda exterior
              │ \│  (ángulo mayor)     │  │  (ángulo menor)
              └──┘                    └──┘
               ╲        EJE DELANTERO    ╲
                ╲   ┌──────────────┐      ╲
                 ╲  │   CHASIS     │       ╲
                  ╲ └──────────────┘        ╲
              ┌──┐                    ┌──┐   ╲
              │  │  Rueda trasera     │  │    ╲
              │  │  interior          │  │     ╲  Rueda trasera exterior
              └──┘                    └──┘      ╲
               ╲_____________ línea del eje trasero (prolongada)
                              ╲
    ●  Centro aproximado de giro (a la izquierda del vehículo, sobre el
       eje trasero prolongado; todas las ruedas giran alrededor de él)
```

**Ejemplos de vehículos que usan esta configuración:** automóviles autónomos como los de Waymo, vehículos de la competencia F1TENTH (autos a escala 1:10), carritos de golf autónomos y la mayoría de los vehículos de campo con dirección tipo automóvil.

---

## 6. Comparación de configuraciones

| Configuración | N.º típico de ruedas | Movimiento lateral | Giro sobre su eje | Complejidad mecánica | Complejidad de control | Aplicaciones |
|---|---|---|---|---|---|---|
| Diferencial + castor | 2 motrices + 1 loca | No | Sí | Baja | Baja | Robots educativos, aspiradoras |
| Omni de 3 ruedas | 3 | Sí | Sí | Media | Media | Robots de competencia, plataformas de investigación |
| Omni de 4 ruedas | 4 | Sí | Sí | Media-alta | Media-alta | Robots ligeros que requieren mejor tracción |
| Mecanum | 4 | Sí | Sí | Alta | Media-alta | Montacargas y plataformas industriales, robots de competencia |
| Ackermann | 4 (2 de dirección y 2 de tracción) | No | No | Media-alta | Media | Autos autónomos, vehículos de exterior |

### ¿Qué configuración elegiría en cada caso?

- **Robot pequeño para aprender programación y control:** *diferencial con castor*. Con solo dos motores se aprenden conceptos básicos (odometría, PID, seguimiento de trayectoria) sin que la mecánica complique el aprendizaje.
- **Robot en un almacén con espacios reducidos:** *Mecanum* (o diferencial si basta con girar en sitio). La capacidad de moverse de lado y girar en el lugar permite maniobrar entre pasillos estrechos.
- **Plataforma que debe moverse lateralmente sin cambiar su orientación:** *Mecanum u Omni*. Ambas permiten desplazamiento lateral conservando la orientación; Mecanum soporta más carga y es más común en plataformas grandes.
- **Vehículo autónomo que circula como un automóvil:** *Ackermann*, porque es la geometría de los vehículos de carretera y ofrece estabilidad a velocidad.
- **Robot de competencia con cambios rápidos de dirección:** *Omni de 3 ruedas* (o Mecanum). Cambian de dirección sin reorientar el chasis y son ligeros.
- **Robot sencillo con solo dos motores:** *diferencial con castor*, que es precisamente la configuración que se hace con dos motores.

---

## 7. Análisis del movimiento

**Diferencial: ¿qué debe hacer cada rueda para que el robot gire sobre su propio eje?**
Cada rueda debe girar en sentido contrario y a la misma velocidad. Cada rueda genera una fuerza hacia adelante en un lado y hacia atrás en el otro, a la misma distancia del centro. Las fuerzas netas de traslación se cancelan (una empuja hacia adelante y la otra hacia atrás con la misma magnitud), pero los momentos (fuerza por distancia) respecto al centro **se suman en el mismo sentido**, lo que produce un par neto que hace girar al robot sin trasladarlo.

**Omni: ¿por qué los rodillos permiten generar movimiento lateral?**
Porque los rodillos eliminan la resistencia en la dirección lateral de cada rueda. Una rueda normal se opone al deslizamiento lateral por la fricción de su neumático, pero en la Omni los rodillos giran libremente cuando algo empuja a la rueda a lo largo de su eje. Así, mientras otras ruedas con distinta orientación empujan al robot hacia el lado, la rueda que *no* tiene fuerza en esa dirección simplemente rueda sobre sus rodillos sin frenarlo. El movimiento lateral resulta de la **suma vectorial** de las fuerzas de las ruedas activas, sin que las demás se opongan.

**Mecanum: ¿por qué se puede mover de lado aunque ninguna rueda apunte hacia el costado?**
Porque, al estar los rodillos a 45°, cada rueda empuja al robot en una dirección inclinada (con componente frontal y lateral). En el movimiento lateral, las ruedas se accionan de forma que las **componentes frontales se cancelen** entre las ruedas (unas empujan adelante y otras atrás) y las **componentes laterales se sumen**, todas hacia el mismo lado. La dirección lateral surge de la combinación de fuerzas diagonales, no de una sola rueda apuntando a un costado.

**Ackermann: ¿por qué el vehículo necesita avanzar o retroceder para cambiar de posición lateral?**
Porque sus ruedas solo pueden rodar en la dirección en que apuntan y resisten el deslizamiento lateral (restricción no holonómica). Para moverse hacia un lado, el vehículo debe trazar una curva (por ejemplo, avanzando con las ruedas giradas y luego retrocediendo con ellas giradas en sentido contrario). El desplazamiento lateral solo puede lograrse como una **secuencia de movimientos hacia adelante y atrás**, como al estacionarse en paralelo.

---

## 8. Aplicación en un robot real

**Robot seleccionado: Robotino (Festo Didactic).**

| Característica | Descripción |
|---|---|
| **Nombre** | Robotino |
| **Fabricante** | Festo Didactic (Alemania) |
| **Tipo de locomoción** | Omnidireccional |
| **Número y tipo de ruedas** | 3 ruedas Omni, separadas 120° |
| **Sensores principales** | Sensores infrarrojos de distancia, sensor inductivo, sensor óptico, parachoques (bumper) con detección de contacto, cámara y encoders en los motores |
| **Actuadores para el movimiento** | 3 motores de corriente directa con reductor y encoder, uno por cada rueda Omni |
| **Aplicación** | Plataforma educativa y de investigación en robótica móvil y logística, usada en universidades y centros de formación |
### ESTA IMAGEN OCUPA UN MONTON DE ESPACIO EN EL EDITOR
![Robotino de Festo Didactic](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAgYCTgMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABQECAwQGBwj/xABWEAABAwIDBAUHCQQGBggGAwABAAIDBBEFEiEGMUFREyIyYXEHFFKBkaGxFSMzQmJygsHRQ1OS4RYkNGNzsiUmNaLC8ERUdJPT4uPxNlZklNLyF0WE/8QAFwEBAQEBAAAAAAAAAAAAAAAAAAECA//EACIRAQEAAgICAgIDAAAAAAAAAAABAhEhMQNBEpEyURNCof/aAAwDAQACEQMRAD8A9xREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERARY3SxN7T2rE6shb6R9SDZRaD6/0W/xLC6sk9MN+61BKq0va3tOUM6WR3bc73q26CYdPG3e5YzWQ/a9iikugkjXx+i5WGv9Fg9ZP6LQRFbnn0votVDWSLTS6DZ88l/e/wC6FXzif958Fq5lQuQbLp5vSkagqp/3vwWuJHN+sheg2hWz+k3+FXsxB31ox6tFo5kzoJQV8X1rtV/nsHpH+EqIzJdBLefQekf4Sq+ewekf4Som6XREv55B+8/3Sq+dwfvWqHul0EyKiD9632q7pY/3rfaFC3VEE7mb6SsmljhjMkr2sYBq5ygn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) 

**¿Por qué esta configuración es adecuada?**
Robotino se usa para enseñar y para investigación, donde se requiere probar distintos algoritmos de navegación. La configuración de tres ruedas Omni lo hace holonómico: puede moverse en cualquier dirección sin reorientarse, lo que simplifica el seguimiento de trayectorias y permite maniobrar en espacios limitados. Además, es mecánicamente más simple que una plataforma de cuatro ruedas Mecanum (tres motores en lugar de cuatro) y sirve bien para estudiar cinemática omnidireccional.

---

## Reflexión final

**¿Qué configuración te pareció más sencilla de comprender?**
La diferencial con rueda de castor, porque la relación entre lo que hacen las ruedas y el movimiento del robot es muy directa: si una rueda va más rápido, el robot gira hacia el otro lado. Las configuraciones con ruedas Omni y Mecanum requieren pensar en componentes de fuerza y en cómo se cancelan o se suman, lo cual cuesta más al principio.

**¿Cuál ofrece mayor libertad de movimiento?**
Las omnidireccionales (Omni y Mecanum), porque pueden trasladarse en cualquier dirección y girar de forma independiente, es decir, controlan los tres grados de libertad del plano. El diferencial y el Ackermann tienen restricciones que les impiden moverse de lado.

**¿Qué configuración utilizarías para construir tu primer robot móvil?**
La diferencial con castor, ya que usa solo dos motores, es barata, fácil de armar y de programar, y permite aprender conceptos básicos como control de velocidad, odometría y seguimiento de trayectorias antes de pasar a configuraciones más complejas.

**¿Por qué no existe una sola configuración de ruedas adecuada para todos los robots?**
Porque cada una resuelve un compromiso distinto entre maniobrabilidad, costo, estabilidad, capacidad de carga y simplicidad. Un vehículo autónomo en carretera necesita estabilidad a alta velocidad (Ackermann), mientras que un robot de almacén necesita moverse en espacios cerrados (Mecanum u Omni), y uno educativo necesita ser simple y barato (diferencial). Según el entorno, el terreno, la carga y el presupuesto, cambia la configuración más conveniente.

---

## Referencias

1. Siegwart, R., Nourbakhsh, I. R., & Scaramuzza, D. (2011). *Introduction to Autonomous Mobile Robots* (2.ª ed.). MIT Press. https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/
2. Dudek, G., & Jenkin, M. (2010). *Computational Principles of Mobile Robotics* (2.ª ed.). Cambridge University Press. https://doi.org/10.1017/CBO9780511780929
3. Siciliano, B., & Khatib, O. (Eds.). (2016). *Springer Handbook of Robotics* (2.ª ed.). Springer. https://doi.org/10.1007/978-3-319-32552-1
4. Campion, G., Bastin, G., & D'Andréa-Novel, B. (1996). Structural properties and classification of kinematic and dynamic models of wheeled mobile robots. *IEEE Transactions on Robotics and Automation, 12*(1), 47–62. https://doi.org/10.1109/70.481750
5. Taheri, H., & Zhao, C. X. (2020). Omnidirectional mobile robots, mechanisms and navigation approaches. *Mechanism and Machine Theory, 153*, 103958. https://doi.org/10.1016/j.mechmachtheory.2020.103958
6. Ilon, B. E. (1975). *Wheels for a course stable selfpropelling vehicle movable in any desired direction on the ground or some other base* (U.S. Patent No. 3,876,255). U.S. Patent and Trademark Office. https://patents.google.com/patent/US3876255A/en
7. Rajamani, R. (2012). *Vehicle Dynamics and Control* (2.ª ed.). Springer. https://doi.org/10.1007/978-1-4614-1433-9
8. ROBOTIS. (s. f.). *TurtleBot3: Overview* [Documentación del fabricante]. https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/
9. Festo Didactic. (s. f.). *Robotino: plataforma robótica móvil educativa* [Sitio oficial del fabricante]. https://www.festo-didactic.com
10. F1TENTH Foundation. (s. f.). *F1TENTH: Autonomous racing platform*. https://f1tenth.org
