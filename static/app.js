document.addEventListener("DOMContentLoaded", () => { // Es una manera de decir que hasta que cargue HTML, se cargue el js

        fetch("http://127.0.0.1:5000/tareas") // "fetch" hace peticion al servidor y a esa direccion
        .then(response => response.json()) // then "espera" con la funcion responde hara que el dato se convierta a json 
        .then(data => { //los datos que llegaron se les asigna el nombre data para usarlos dentro de la función
            const lista = document.getElementById("lista-tareas") // creamos una variable llamada lista que conentra de valor el elemento lista de tareas de html
            data.forEach(tarea => { //data ocupara for each, par recorrer la lista que nos dio el json
                const item = document.createElement("li") //crearemos una variable "item" que sera la creacion de un elemnto "li" en html
                item.textContent = tarea.titulo // El intem le crearemos un tex que ese text su valor sera de "titulo de los diccionarios"
                lista.appendChild(item) // A la lista le agregarmos un elemento hijo que sera el item
            })
        })

    document.getElementById("btn-agregar").addEventListener("click", () => { 
        const input = document.getElementById("input-tarea") 
        const titulo = input.value 

        fetch("http://127.0.0.1:5000/tareas", { //hacemos una peticion a http
            method: "POST", // ocupamos el metodo post para mandar dato
            headers: {"Content-Type": "application/json"}, // atravez de un headers, mandamos la informacion, siendo tipo de contendio, un archvio json
            body: JSON.stringify({titulo: titulo}) // El body es el contenido que mandas. JSON.stringify convierte el objeto JS a texto JSON para enviarlo. 
        })
        .then(response => response.json()) // Aqui espera el mensaje de python cuando nostros mandamos una tarea
        .then(data => { 
            const lista = document.getElementById("lista-tareas")
            const item = document.createElement("li")
            item.textContent = titulo
            lista.appendChild(item)
        })
    })

})

