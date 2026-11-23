let numero = 1;
let custoUp1 = 60;
let porClick = 1
let custoUp2 = 140
let dinheiroPassivo = 0
let upgrades = 0

const imagen = document.getElementById("imagem")
const dinheiro = document.getElementById("dinheiro")
const botaoMais = document.getElementById("botao+")
const upgrade1 = document.getElementById("upgrade1")
const custo1 = document.getElementById("custo1")
const upgrade2 = document.getElementById("upgrade2")
const custo2 = document.getElementById("custo2")

const PORCLICK = document.getElementById("porClick")

botaoMais.addEventListener("click", function(){
    numero = numero + porClick
    dinheiro.textContent = numero
})
upgrade1.addEventListener("click", function(){
    if (numero >= custoUp1){
        numero = numero - custoUp1
        porClick = porClick + 1
        custoUp1 = custoUp1 * 2
        dinheiro.textContent = numero
        PORCLICK.textContent = porClick
        custo1.textContent = custoUp1
        upgrades = upgrades +1
        if (upgrades >= 5 && upgrades < 10){
            imagen.src="img/OIP.webp"
        }
                if (upgrades >= 10 && upgrades < 15){
            imagen.src="img/OIP (1).webp"
        }
        if (upgrades >= 15 && upgrades < 20){
            imagen.src="img/OIP (3).webp"
        }
        if (upgrades >= 20 && upgrades < 30){
            imagen.src="img/OIP.jpg"
        }
        if (upgrades >= 30 && upgrades < 35){
            imagen.src="img/Ocarina Dourada do Herói.png"
        }
        if (upgrades >= 35 && upgrades < 40){
            imagen.src="img/Ocarina Dourada no Estilo Meme.png"
        }
        if (upgrades >= 40 && upgrades < 50){
            imagen.src="img/Ocarina Suprema_ Explosão de Memes Neon.png"
        }
        

    }
    
})
upgrade2.addEventListener("click", function(){
    if (numero >= custoUp2){
        numero = numero - custoUp2
        dinheiroPassivo = dinheiroPassivo + 1
        custoUp2 = custoUp2 * 2
        dinheiro.textContent = numero
        custo2.textContent = custoUp2
        upgrades = upgrades +1
        if (upgrades >= 5 && upgrades < 10){
            imagen.src="img/OIP.webp"
                    if (upgrades >= 10 && upgrades < 15){
            imagen.src="img/OIP(1).webp"
        }
        if (upgrades >= 15 && upgrades < 20){
            imagen.src="img/OIP(3).webp"
        }
        if (upgrades >= 20 && upgrades < 30){
            imagen.src="img/OIP.jpg"
        }
        if (upgrades >= 30 && upgrades < 35){
            imagen.src="img/Ocarina dourada do heroi.png"
        }
        if (upgrades >= 35 && upgrades < 40){
            imagen.src="img/Ocarina Dourada no Estilo Meme.png"
        }
        if (upgrades >= 40 && upgrades < 50){
            imagen.src="img/Ocarina Suprema_ Explosão de Memes Neon.png"
        }

        }
    }
    
})
setInterval(function(){
    numero = numero + dinheiroPassivo
    dinheiro.textContent = numero
},5000)
