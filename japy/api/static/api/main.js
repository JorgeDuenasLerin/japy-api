async function obtenerListado(token){
    var listado = await fetch(
        '/api/actores/',
        {
            headers:{
                'Authorization': 'Token ' + token,
            },
        }
    ).then(
        response => response.json()
    ).then(data => {
        debugger
        return data
    })
    return listado
}

var f = document.getElementById('autentificacion')
f.addEventListener('submit', (e)=>{
    var u = document.getElementById('username').value
    var p = document.getElementById('password').value
    e.preventDefault()
    var datos = []
    csrf = document.cookie.split("=")[1]
    fetch(
        '/api-token-auth/',
        {
            method:'POST',
            headers:{
                'Content-Type':'application/x-www-form-urlencoded',
                'X-CSRFToken': csrf
            },
            body:`username=${u}&password=${p}`,
        }
    )
    .then(
        response => response.json()
    )
    .then(data => {
        if(data['token'] != undefined){
            datos = obtenerListado(data['token'])
        } else {
            // mostrar error UI
        }
    })
})