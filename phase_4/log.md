# Enlaces

* https://en.wiktionary.org/wiki/Wiktionary:Main_Page
* https://es.wikiquote.org/wiki/Portada
* [How to calibrate the Magnetometer](https://rpf.io/ap-mag): Enlace interesante sobre el magnetómetro comentado en webinar, aunque en el proyecto de este año no lo vayamos a utilizar.
* [Ground sampling distance calculator](https://www.3dflow.net/ground-sampling-distance-calculator/)
* [Computer vision and machine learning](https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/7)
* [Calculate the speed of the ISS](https://projects.raspberrypi.org/en/projects/astropi-iss-speed)
* [Math and equations in Juputer Notebooks](https://jupyterbook.org/en/stable/content/math.html)
* [LaTeX:Symbols](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols)
* [Coordinate Systems Worldwide](https://epsg.io/)
* [Conversor coordenadas](https://www.earthpoint.us/Convert.aspx)
* [RadioGlobe - Spin to Search Over 15000 Web Radio Stations!](https://www.instructables.com/RadioGlobe-Spin-to-Search-Over-Web-Radio-2000-Stat/)
* [GeoPy’s documentation](https://geopy.readthedocs.io/en/latest/)
* [Populated Places](https://datacore-gn.unepgrid.ch/geonetwork//srv/spa/catalog.search#/metadata/4a64faed-8674-4bb2-baad-fb6446ee3a6d)

# Propuesta

What is your experiment idea?

Nuestro proyecto de este año se titula "El lenguaje de la tierra". Utilizando los datos de los sensores y las fotografías geolocalizadas tomadas por la ISS realizaremos una interface que señale los núcleos urbanos más importantes sobrevolados por la estación, y reproduzca diferentes audios en los distintos idiomas empleados en esos lugares. El experimento consiste en recopilar los datos capturados en la IIS, contrastarlos con otras bases de datos, y construir una interfaz de AR (Augmented Reality) para mostrar sobre las fotografías originales, nuevos datos de la imagen junto a sonidos autóctonos, significando el valor de un proyecto internacional como la ISS y poniendo voz a las diversas culturas que comparten nuestro planeta.

How will you use the Astro Pi computers to perform your experiment?

Aunque para el proyecto de este año seguramente sería suficiente con hacer fotografías, queremos recopilar todos los datos posibles de los sensores de AstroPi, para tener datos reales que podamos emplear para testear posibles futuras participaciones en el proyecto AstroPi. Queremos hacer uso del theme "Life on Earth" con la "VIS Camera", ya que queremos que el vídeo final resulte lo más bonito posible.

# Enviado el 2022-10-27 17:30

Describe your team’s experiment and the hypothesis they will investigate

Our project this year is entitled "The language of the Earth". Using sensor data and geolocated photographs taken by the ISS, we will create an interface that points out the most important urban centres overflown by the station, and plays different audios in the different languages used in those places. The experiment consists of compiling the data captured by the ISS, contrasting them with other databases, and building an AR (Augmented Reality) interface to display new image data on the original photographs, together with indigenous sounds, signifying the value of an international project such as the ISS and giving voice to the different cultures that share our planet.

What type of data does your team plan to gather? How will this data help test your hypothesis?

Although for this year's project it would probably be enough to take pictures, we want to collect as much data as possible from the AstroPi sensors, in order to have real data that we can use for testing possible future participations in the AstroPi project. We want to use the theme "Life on Earth" with the "VIS Camera", because we want the final AR video to be as beautiful as possible.



# Logro 1: Señalar ciudades de más de 100.000 habitantes sobre las fotos

## Datos cámara:

https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/4

### Mark I

* Focal length (mm): 3.04
* Sensor width (mm): 3.68 x 2.76

### Mark II

* Focal length (mm): 5
* Sensor width (mm): 6.287 x 4.712

## Ejemplos:

* Sobrevuelo Tokio (Mark I):     2020-2021; Fotos: 620-628
* Sobrevuelo Pamplona (Mark II): 2021-2022; Fotos: 493-495
* Sobrevuelo Zaragoza (Mark II): 2021-2022; Fotos: 494-496

## Sobrevuelo Pamplona

* 493: 2022-04-26 10:14:03,314	atlantes_493.jpg	43,097612303689	-2,3949488058073	420980,867804757
* 494: 2022-04-26 10:14:18,314	atlantes_494.jpg	42,5769655132425	-1,34409030873256	420935,392917282
* 495: 2022-04-26 10:14:33,314	atlantes_495.jpg	42,0456549998534	-0,311780686364562	420888,465009558

Calcular anchura/altura de foto en m


Calcular latitud/longitud esquinas foto.


[(1664.064208984375, 1325.3760986328125), (1665.10107421875, 1325.0306396484375), (1418.3427734375, 1260.0855712890625)]
[(2278.080078125, 1388.1600341796875), (2278.88671875, 1387.2386474609375), (2005.2000732421875, 393.6000061035156)]


3280/2 = 1640
2464/2 = 1232

## Foto 492
43.607322,-3.464841
alpha: -33.34; beta: -5.89; gamma: 152.55; delta: 118.35

## Foto 493
43.097612,-2.394949 -> 43.517345,-2.684443
alpha: -34.16; beta: -5.89; gamma: 151.73; delta: 117.53

## Foto 557
-1.388801,42.051250 -> -0.921566,41.995050
alpha: -54.83; beta: -5.89; gamma: 131.06; delta: 95,08

