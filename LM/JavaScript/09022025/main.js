function llamarAlerta(boton) {
    boton.classList.toggle("blackgroundBlue")
    boton.classList.toggle("blackgroundRed")

    ///boton NM
    let idReverse = boton.id.split("").reverse()
    let fila = parseInt(idReverse[1])+1
    let columna = parseInt(idReverse[0])+1

    document.querySelector("#boton" +  fila + columna).classList.toggle("blackgroundRed")
    document.querySelector("#boton" +  fila + columna).classList.toggle("blackgroundBlue")
}