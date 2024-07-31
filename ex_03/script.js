document.body.innerHTML += `
    <h1 id="titulo">Título do Site</h1>
    <div id="produto">
        <h2>Nome do Produto</h2>
        <p>Descrição do Produto</p>
        <p>Preço: R$ 100,00</p>
    </div>
`;

const titulo = document.createElement('h1');
titulo.id = 'titulo';
titulo.innerText = 'Título do Site';

const produto = document.createElement('div');
produto.id = 'produto';

const nome = document.createElement('h2');
nome.innerText = 'Nome do Produto';

const descricao = document.createElement('p');
descricao.innerText = 'Descrição do Produto';

const preco = document.createElement('p');
preco.innerText = 'Preço: R$ 100,00';

produto.appendChild(nome);
produto.appendChild(descricao);
produto.appendChild(preco);

document.body.appendChild(titulo);
document.body.appendChild(produto);
