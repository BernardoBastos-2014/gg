let cliques = 0
let contador = document.getElementById("contador")
let botão = document.getElementById("botão")
let botão2 = document.getElementById("botão2")
botão.onclick = function(){
    cliques += 1
    contador.innerHTML = cliques
}
botão2.onclick = function(){
    cliques =0
    contador.innerHTML = cliques
}