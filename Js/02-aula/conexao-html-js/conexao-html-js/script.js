const post_02 = document.getElementById('post02');


const form = document.getElementById('formulario');


const texto = document.querySelector('.post-texto');

const TextoDosPosts = document.querySelectorAll('.post-texto');

texto.innerText = "Eu sou alberico"
texto.id = "IDnovo"


// console.log(post_02);
// console.log(form);
// console.log(texto);
// console.log(TextoDosPosts);


const link = document.querySelector('#post01 .post-texto a');
console.log(link);

const negrito = document.querySelector('#post02 .post-texto strong');
console.log(negrito);


const InputNome = document.querySelector('input[type="name"]');
console.log(InputNome);

const redes = document.querySelectorAll(".lista_redes");
console.log(redes);

const linksNav = document.querySelectorAll('.lista_redes a');
// console.log(linksNav);

const todosNegritos = document.querySelectorAll("strong");
console.log(todosNegritos);


let titulos = document.querySelectorAll("footer .lista_redes a");
function imprimirTodos(lista){
  for(let i = 0; i < lista.length; i++){
    console.log(lista[i].innerHTML);
  }
}

imprimirTodos(lista);