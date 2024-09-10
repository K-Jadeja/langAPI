import requests

data = {"target_language":"fr","text": """Here are some events available for booking:

Government Museum Chennai

Type: Museum
History: Established in 1851, the second oldest museum in India with a rich collection of artifacts.
Ticket Price: ₹50
Event Start: 12th September 2024, 09:00
Event End: 12th September 2024, 17:00
CHILDREN'S MUSEUM

Type: Museum
History: Founded in 1997 to educate children through interactive exhibits.
Ticket Price: ₹30
Event Start: 13th September 2024, 10:00
Event End: 13th September 2024, 16:00
DR. ARUN'S PHOTOGRAPHY AND VINTAGE CAMERA MUSEUM

Type: Museum
History: Showcases the evolution of photography with over 1,500 antique cameras.
Ticket Price: ₹40
Event Start: 14th September 2024, 09:30
Chennai Rail Museum

Type: Museum
History: Showcases the rich heritage of Indian Railways with vintage locomotives and artifacts.
Ticket Price: ₹50
Event Start: 15th September 2024, 10:00
Event End: 15th September 2024, 18:00
Vivekananda House

Type: Museum
History: Dedicated to the life and teachings of Swami Vivekananda.
Ticket Price: ₹60
Event Start: 16th September 2024, 09:00
Event End: 16th September 2024, 17:00
Fort St. George Museum

Type: Museum
History: Houses artifacts from the colonial period within the first British fortress in India.
Ticket Price: ₹60
Event Start: 17th September 2024, 09:00
Event End: 17th September 2024, 17:00
National Art Gallery Chennai

Type: Museum
History: Showcases paintings from various Indian art schools in a Victorian-style building.
Ticket Price: ₹20
Event Start: 18th September 2024, 10:00
Event End: 18th September 2024, 16:00
Art Through Time

Type: Exhibition
History: Walk through history with famous paintings from different time periods.
Ticket Price: ₹250
Event Start: 20th September 2024, 11:00
Event End: 20th September 2024, 17:00
Science Wonders

Type: Exhibition
History: Fun science adventure with experiments and interactive displays.
Ticket Price: ₹300
Event Start: 21st September 2024, 10:00
Event End: 21st September 2024, 16:00
Ancient Treasures

Type: Exhibition
History: Discover amazing objects from long-ago civilizations.
Ticket Price: ₹200
Event Start: 22nd September 2024, 09:30
Event End: 22nd September 2024, 17:30
Please let me know which event Krishna would like to attend and how many tickets are needed."""}
# try:
#     response = requests.post('http://localhost:5000/translate', json=data)
#     with open('response.txt', 'w', encoding='utf-8') as f:
#         f.write(response.text)
# except Exception as e:
#     print(f"An error occurred: {e}")
import requests
import textwrap

data = {
    "text":"""
A continuación, se muestran algunos eventos disponibles para reservar:

Museo del Gobierno de Chennai

Tipo: Museo
Historia: Fundado en 1851, es el segundo museo más antiguo de la India y cuenta con una rica colección de artefactos.
Precio de la entrada: ₹50
Inicio del evento: 12 de septiembre de 2024, 09:00
Fin del evento: 12 de septiembre de 2024, 17:00
MUSEO INFANTIL

Tipo: Museo
Historia: Fundado en 1997 para educar a los niños a través de exhibiciones interactivas.
Precio de la entrada: ₹30
Inicio del evento: 13 de septiembre de 2024, 10:00
Fin del evento: 13 de septiembre de 2024, 16:00
MUSEO DE FOTOGRAFÍA Y CÁMARAS ANTIGUAS DEL DR. ARUN

Tipo: Museo
Historia: Muestra la evolución de la fotografía con más de 1500 cámaras antiguas.
Precio de la entrada: ₹40
Inicio del evento: 14 de septiembre de 2024, 09:30
Museo del Ferrocarril de Chennai

Tipo: Museo
Historia: Muestra la rica herencia de los ferrocarriles indios con locomotoras y artefactos antiguos.
Precio de la entrada: ₹50
Inicio del evento: 15 de septiembre de 2024, 10:00
Fin del evento: 15 de septiembre de 2024, 18:00
Casa Vivekananda

Tipo: Museo
Historia: Dedicado a la vida y las enseñanzas de Swami Vivekananda.
Precio de la entrada: ₹60
Inicio del evento: 16 de septiembre de 2024, 09:00
Fin del evento: 16 de septiembre de 2024, 17:00
Museo del Fuerte St. George

Tipo: Museo
Historia: Alberga artefactos del período colonial dentro de la primera fortaleza británica en la India.
Precio de la entrada: ₹60
Inicio del evento: 17 de septiembre de 2024, 09:00
Fin del evento: 17 de septiembre de 2024, 17:00
Galería Nacional de Arte de Chennai

Tipo: Museo
Historia: Muestra pinturas de varias escuelas de arte de la India en un edificio de estilo victoriano.
Precio de la entrada: ₹20
Inicio del evento: 18 de septiembre de 2024, 10:00
Fin del evento: 18 de septiembre de 2024, 16:00
El arte a través del tiempo

Tipo: Exposición
Historia: Recorre la historia con pinturas famosas de diferentes períodos de tiempo.
Precio de la entrada: 250 ₹
Inicio del evento: 20 de septiembre de 2024, 11:00
Fin del evento: 20 de septiembre de 2024, 17:00
Maravillas de la ciencia

Tipo: Exposición
Historia: Divertida aventura científica con experimentos y exhibiciones interactivas.
Precio de la entrada: 300 ₹
Inicio del evento: 21 de septiembre de 2024, 10:00
Fin del evento: 21 de septiembre de 2024, 16:00
Tesoros antiguos

Tipo: Exposición
Historia: Descubra objetos asombrosos de civilizaciones antiguas.
Precio de la entrada: 200 ₹
Inicio del evento: 22 de septiembre de 2024, 09:30
Fin del evento: 22 de septiembre de 2024, 17:30
Por favor, háganme saber a qué evento le gustaría asistir Krishna y cuántas entradas se necesitan.    
Fin del evento: 18 de septiembre de 2024, 16:00
El arte a través del tiempo

Tipo: Exposición
Historia: Recorre la historia con pinturas famosas de diferentes períodos de tiempo.
Precio de la entrada: 250 ₹
Inicio del evento: 20 de septiembre de 2024, 11:00
Fin del evento: 20 de septiembre de 2024, 17:00
Maravillas de la ciencia

Tipo: Exposición
Historia: Divertida aventura científica con experimentos y exhibiciones interactivas.
Precio de la entrada: 300 ₹
Inicio del evento: 21 de septiembre de 2024, 10:00
Fin del evento: 21 de septiembre de 2024, 16:00
Tesoros antiguos

Tipo: Exposición
Historia: Descubra objetos asombrosos de civilizaciones antiguas.
Precio de la entrada: 200 ₹
Inicio del evento: 22 de septiembre de 2024, 09:30
Fin del evento: 22 de septiembre de 2024, 17:30
Por favor, háganme saber a qué evento le gustaría asistir Krishna y cuántas entradas se necesitan.
Fin del evento: 18 de septiembre de 2024, 16:00
El arte a través del tiempo

Tipo: Exposición
Historia: Recorre la historia con pinturas famosas de diferentes períodos de tiempo.
Precio de la entrada: 250 ₹
Inicio del evento: 20 de septiembre de 2024, 11:00
Fin del evento: 20 de septiembre de 2024, 17:00
Maravillas de la ciencia

Tipo: Exposición
Historia: Divertida aventura científica con experimentos y exhibiciones interactivas.
Precio de la entrada: 300 ₹
Inicio del evento: 21 de septiembre de 2024, 10:00
Fin del evento: 21 de septiembre de 2024, 16:00
Tesoros antiguos

Tipo: Exposición
Historia: Descubra objetos asombrosos de civilizaciones antiguas.
Precio de la entrada: 200 ₹
Inicio del evento: 22 de septiembre de 2024, 09:30
Fin del evento: 22 de septiembre de 2024, 17:30
Por favor, háganme saber a qué evento le gustaría asistir Krishna y cuántas entradas se necesitan.

"""        

}

try:
    response = requests.post('http://localhost:5000/detect-and-translate', json=data)
    with open('response.txt', 'w', encoding='utf-8') as f:
        f.write(response.text)
except Exception as e:
    print(f"An error occurred: {e}")