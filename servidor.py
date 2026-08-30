from flask import Flask, render_template

# Variables

app = Flask(__name__)


mis_contactos=[
    {"red": "linkedIn", "link": "https://www.linkedin.com/in/brahiansantiagopirafan"}
]

mi_formacion=[ 

     {"titulo": "ingenieria de sistemas", "fecha":"cursando", "link":"...",},
     {"titulo": "Tecnologo analisis y desarrollo de sistema de informacion", "fecha":"2023", "link":"...",},
     {"titulo": "Tecnico diseño e integracion multimedia", "fecha":"2020", "link":"...",},

]
mis_cursos=[
     
     {"titulo": "master java", "fecha":"2026", "link":"...",},
     {"titulo": "full stack", "fecha":"2026", "link":"...",},
     {"titulo": "serenity web driver con java", "fecha":"2026", "link":"...",},
     {"titulo": "Desarrollo seguro en paginas web", "fecha":"2026", "link":"...",}
     ]

perfil_profesional = """Tecnólogo en Análisis y Desarrollo de Sistemas de Información con experiencia en Aseguramiento de Calidad (QA) y conocimientos en desarrollo de software, pruebas manuales, automatización básica, programación y bases de datos SQL. Mi formación me permite comprender tanto el desarrollo como la validación de aplicaciones, contribuyendo a la entrega de soluciones funcionales y de calidad. Me caracterizo por mi capacidad de aprendizaje continuo, adaptación a nuevas tecnologías y metodologías, pensamiento analítico, atención al detalle y trabajo colaborativo para la resolución de problemas. Uno de los logros más relevantes de mi trayectoria ha sido desempeñar simultáneamente funciones de QA Manual y QA Automation, adaptándome a las necesidades del proyecto y fortaleciendo mi versatilidad para asumir distintos retos dentro del proceso de aseguramiento de calidad. Busco aportar mis conocimientos y continuar creciendo profesionalmente en proyectos de desarrollo de software y calidad."""



@app.route('/')
def inicio():

    return render_template('pasarela.html',

        contactos=mis_contactos,
        formacion=mi_formacion,
        cursos=mis_cursos,
        perfil=perfil_profesional)

if __name__=='__main__':
      app.run(debug=True)


