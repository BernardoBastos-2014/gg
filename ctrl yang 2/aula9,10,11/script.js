const CLASSE = document.getElementById("classe");
const RACA = document.getElementById("raca");
const IMAGEM = document.getElementById("imagen-personagen");

const nomesRaca = {
    huggy: "HuggyWuggy"
};

const nomeClasses = {
    guerreiro: "Guerreiro",
    chef: "Chef",
    paladino: "Paladino",
    necromante: "Necromante",
    arqueiro: "arqueiro" // Faltava o arqueiro (com 'a' minúsculo, igual ao nome do arquivo)
};

// A pasta se chama "imagens" e o arquivo padrão original era .webp
const imagenPadrao = "imagens/OIP.webp"; 
const extensoes = [".jpg", ".png"];
let tentativaAtual = 0; // Corrigido de "tentetivaAtual" para "tentativaAtual"

function atualizarImagen(){
    const raca = RACA.value; // Corrigido de "vaule" para "value"
    const classe = CLASSE.value; // Corrigido de "vaule" para "value"
    
    if (!raca || !classe){
        IMAGEM.src = imagenPadrao;
        return;
    }
    
    // Removida a chave { no início e o espaço sobrando no final
    const caminhoBase = `imagens/${nomeClasses[classe]} ${nomesRaca[raca]}`;
    
    tentativaAtual++; 
    tentarCarregar(caminhoBase, 0, tentativaAtual);
}

function tentarCarregar(caminhoBase, indice, tentativa){
    if (tentativa !== tentativaAtual){
        return;
    }

    if (indice >= extensoes.length){
        IMAGEM.src = imagenPadrao;
        return;
    }

    const teste = new Image();
    teste.onload = () => {
        if (tentativa === tentativaAtual){
            IMAGEM.src = teste.src; // Corrigido: deve ser IMAGEM.src, e não tentar reatribuir a const IMAGEM
        }
    };
    teste.onerror = () => tentarCarregar(caminhoBase, indice + 1, tentativa);
    teste.src = encodeURI(caminhoBase + extensoes[indice]);
}

CLASSE.addEventListener("change", atualizarImagen);
RACA.addEventListener("change", atualizarImagen);