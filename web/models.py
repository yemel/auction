# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

ITEMS = [
    {'id': 1, 'price': 500, 'url': 'img/1.jpg', 'name': 'Camiseta Pumas', 'desc': 'Camistea firmada por el plantel de Los Pumas, mayo 2019.'},
    {'id': 2, 'price': 500, 'url': 'img/2.png', 'name': 'Camiseta Boca', 'desc': 'Camiseta firmada por el plantel de Club Atlético Boca Jrs., julio 2019.'},
    {'id': 3, 'price': 500, 'url': 'img/3.png', 'name': 'Camiseta Racing', 'desc': 'Camiseta firmada por el plantel de Racing Club de Avellaneda, agosto 2019.'},
    {'id': 4, 'price': 500, 'url': 'img/4.png', 'name': 'Camistea River', 'desc': 'Camiseta firmada por el plantel de Club Atlético River Plate, agosto 2019.'},
    {'id': 5, 'price': 500, 'url': 'img/5.jpg', 'name': 'Gorra Angel Cabrera', 'desc': 'Gorra de golf del torneo Augusta, firmada por Angel Cabrera en 2008 tras firmar la tarjeta ganadora. '},
    {'id': 6, 'price': 500, 'url': 'img/6.jpg', 'name': 'Gorra Alvaro Quiroz', 'desc': 'Gorra de golf del torneo Valderrama, firmada por Alvaro Quiroz en 2019.'},
    {'id': 7, 'price': 500, 'url': 'img/7.jpg', 'name': 'Gorra JM Olazabal', 'desc': 'Gorra de golf del torneo Valderrama, firmada por José María Olazabal en 2019.'},
    {'id': 8, 'price': 500, 'url': 'img/8.png', 'name': 'Banderín Golf', 'desc': 'Banderín firmado por los jugadores del toreo Valderrama, para los amigos de Educar y Crecer, en 2019.'},
    {'id': 9, 'price': 500, 'url': 'img/9.jpeg', 'name': 'Degustación vinos Sophenia', 'desc': 'Degustación a domicilio para 4 personas. Vinos de alta gama de producciones limitadas de la bodega Finca Sophenia y State Winery, a cargo de su embajadora de marca, Eugenia Luka.'},
    {'id': 10, 'price': 500, 'url': 'img/10.jpeg', 'name': 'Sesión de fotos de Julia Cabrera', 'desc': 'Sesión de fotos Baby o Kids a cargo de Julia Cabrera.'},
    {'id': 11, 'price': 500, 'url': 'img/11.jpg', 'name': 'Una Noche con JFK', 'desc': '2 entradas para el taller "Una noche con JFK" para el 18/9 o 25/9. Un repaso de la historia a través de la literatura y las artes; con experiencias culinarias especialmente diseñadas y una degustación de vinos. Viajá al pasado para conocerlo con todos los sentidos en acción.'},
    {'id': 12, 'price': 500, 'url': 'img/12.png', 'name': 'Tratamiento Dermatólogico Blessa', 'desc': '4 sesiones de láser Lumiia + 4 meso francesa + 4 mascarillas + 1 sesión de limpieza profunda de cutis.'},
    {'id': 13, 'price': 500, 'url': 'img/13.jpg', 'name': 'Cochecito Yoyo', 'desc': 'El carrito YOYO+ puede plegarse, desplegarse, llevarse como un bolso, conducirlo con una mano, cabe en cualquier sitio, puede guardarse cómodamente y subirlo a la cabina como equipaje de mano.'},
    {'id': 14, 'price': 500, 'url': 'img/14.jpg', 'name': 'Silla de comer Babydan', 'desc': 'Silla de bebé de diseño danés. Incluye barra protectora, correa (de quita y pon) y arnés de seguridad. fácil de montar y desmontar. Pies extra largos para mayor estabilidad. Asiento y reposapiés ajustables.'},
    {'id': 15, 'price': 500, 'url': 'img/15.jpg', 'name': 'Obra Alexei Serrano con los chicos de La Carcova', 'desc': 'Artista: Alexei Serrano con los chicos de La Cárcova (2010). El Perro, Técnica Mixta, 50x50. // La Jirafa. Técnica Mixta, 50x50.'},
    {'id': 16, 'price': 500, 'url': 'img/16.jpeg', 'name': 'Obra Catalina White', 'desc': 'Artista: Catalina White. Orquídea. Óleo sobre tela, 100 x 100 cm.'},
    {'id': 17, 'price': 500, 'url': 'img/17.jpg', 'name': 'Obra Teresa Liberati', 'desc': 'Artista: Teresa Liberati. Libre y Vida, de la serie Infancia VI. Técnica Mixta. 50x60 '},
    {'id': 18, 'price': 500, 'url': 'img/18.jpg', 'name': 'Obra Marie France Soulas', 'desc': 'Artista: Marie France Soulas (2018). Achira amarirra. Acrílico sobre tela. 60x50'},
    {'id': 19, 'price': 500, 'url': 'img/19.jpeg', 'name': 'Obra de Rafael Gonzalez Moreno', 'desc': 'Artista: Rafael Gonzalez Moreno. Sin Titulo. Fotografía sobre PVC. 70x90'},
    {'id': 20, 'price': 500, 'url': 'img/20.jpeg', 'name': 'Obra Susana Puchetta', 'desc': 'Artista: Susana Puchetta. Flor. Técnica Mixta. 1,50x1,15'},
    {'id': 21, 'price': 500, 'url': 'img/21.jpg', 'name': 'Obra de Fabiola Benvenuto', 'desc': 'Artista: Fabiola Benvenuto. Sin Titulo. Técnica Mixta. 90x70'},
    {'id': 22, 'price': 500, 'url': 'img/22.jpg', 'name': 'Obra de Belén Sanmartino', 'desc': 'Artista: Belén Sanmartino. Día de la madre. Acrílico sobre tela. 120x70'},
    {'id': 23, 'price': 500, 'url': 'img/23.jpg', 'name': 'Obra de Graciela Bello', 'desc': 'Artista: Graciela Bello. Terrenal, Celestial. Acrilico sobre tela. 100 x 150 cm.'},
    {'id': 24, 'price': 500, 'url': 'img/24.jpeg', 'name': 'Obra de Daniela Militelio', 'desc': 'Artista: Daniela Militelo. Ayre. Técnica mixta, acrílico sobre papel. 60 x 30 cm.'},
    {'id': 25, 'price': 500, 'url': 'img/25.jpeg', 'name': '25. Obra de Mapi de Aubeyzon', 'desc': 'Artista: Mapi de Aubeyzon. Foresta (2019). Serigrafía intervenida. 55 x 45 cm.'},
]
