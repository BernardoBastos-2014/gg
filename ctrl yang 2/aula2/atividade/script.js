let imagem = document.getElementById("botão")
let texto = document.getElementById("texto")
let pokemon1 = "The flame on its tail shows the strength of its life-force. If Charmander is weak, the flame also burns weakly."
let pokemon2 = "For some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow."
let pokemon3 = "After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth."
let botão = document.getElementById("botão")
let botão2 = document.getElementById("botão2")
let botão3 = document.getElementById("botão3")

botão.onclick = function(){
    pokemon.src = "imagens/pokemon1.png"
    texto.innerHTML = pokemon1
}

botão2.onclick = function(){
    pokemon.src = "imagens/pokemon2.png"
    texto.innerHTML = pokemon2
}
botão3.onclick = function(){
    pokemon.src = "imagens/pokemon3.png"
    texto.innerHTML = pokemon3
}