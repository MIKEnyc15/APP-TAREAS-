fetch("http://127.0.0.1:5000/tareas")
    .then(response => response.json())
    .then(data => {
        const lista = document.getElementById("lista-tareas")
        data.forEach(tarea => {
            const item = document.createElement("li")
            item.textContent = tarea.titulo
            lista.appendChild(item)
        })
    })

