function Sumar(){
    let numero1 = parseInt(document.getElementById("idNum1").value);
    let numero2 = parseInt(document.getElementById("idNum2").value);
    let resultado = numero1 + numero2;

    document.getElementById("idNumResultado").value = resultado
}
function Resta(){
    let numero1 = parseInt(document.getElementById("idNum1").value);
    let numero2 = parseInt(document.getElementById("idNum2").value);
    let resultado = numero1 - numero2;

    document.getElementById("idNumResultado").value = resultado
}