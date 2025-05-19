let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

function salvarProdutos() {
    localStorage.setItem('produtos', JSON.stringify(produtos));
}

function carregarProdutos() {
    const container = document.getElementById('product-list');
    if (!container) return;

    container.innerHTML = ''; // Limpa o conteúdo atual da lista

    produtos.forEach((produto) => {
        const card = document.createElement('div');
        card.className = 'card';

        // Lógica para definir a cor da bolinha
        let statusClasse = 'disponivel';
        if (produto.quantidadeAtual === 0) {
            statusClasse = 'indisponivel-vermelho'; // Produto em falta (vermelho)
        } else if (produto.quantidadeAtual <= produto.quantidadeMaxima * 0.5) {
            statusClasse = 'indisponivel-laranja'; // Produto abaixo de 50% do estoque (laranja)
        }

        const statusTexto = produto.quantidadeAtual > 0 ? 'Disponível' : 'Indisponível';

        card.innerHTML = `
            <img src="${produto.imagem}" alt="${produto.nome}">
            <div>
                <h1>${produto.nome}</h1>
                <div class="status">
                    <h2>${statusTexto} <span class="status-dot ${statusClasse}"></span></h2>
                </div>
                <span>${produto.quantidadeAtual}/${produto.quantidadeMaxima}</span>
            </div>
        `;

        container.appendChild(card); // Adiciona o card à lista de produtos
    });
}

function abrirModal() {
    document.getElementById('modal').style.display = 'flex';
}

function fecharModal() {
    document.getElementById('modal').style.display = 'none';
}

window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}

function cadastroProduto() {
    const nome = document.getElementById('nome-produto').value.trim();
    const categoria = document.getElementById('categoria-produto').value;
    const quantidade = parseInt(document.getElementById('quantidade-produto').value);
    const maximo = parseInt(document.getElementById('estoque-minimo').value);
    const imagemInput = document.getElementById('imagem-url');

    if (!nome || !categoria || isNaN(quantidade) || isNaN(maximo) || quantidade < 0 || maximo < 0 || quantidade > maximo) {
        alert("Preencha os campos corretamente.");
        return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
        const imagemURL = e.target.result;

        const produto = {
            nome,
            categoria,
            quantidadeAtual: quantidade,
            quantidadeMaxima: maximo,
            imagem: imagemURL
        };

        produtos.push(produto);
        salvarProdutos();
        finalizarCadastro();
    };

    if (imagemInput.files && imagemInput.files[0]) {
        reader.readAsDataURL(imagemInput.files[0]);
    } else {
        const produto = {
            nome,
            categoria,
            quantidadeAtual: quantidade,
            quantidadeMaxima: maximo,
            imagem: 'https://via.placeholder.com/150'
        };
        produtos.push(produto);
        salvarProdutos();
        finalizarCadastro();
    }
}

function finalizarCadastro() {
    carregarProdutos(); // Recarrega os produtos para atualizar a lista
    document.getElementById('formCadastro').reset(); // Limpa o formulário
    document.getElementById('imagem-preview').style.display = 'none'; // Esconde a imagem de pré-visualização
    document.getElementById('modal').style.display = 'none'; // Fecha o modal
    alert("Produto cadastrado com sucesso!");
}

document.addEventListener('DOMContentLoaded', () => {
    carregarProdutos(); // Carrega os produtos ao carregar a página

    document.getElementById('formCadastro').addEventListener('submit', function (e) {
        e.preventDefault(); // Impede o envio do formulário
        cadastroProduto(); // Chama a função de cadastro do produto
    });

    document.getElementById('fecharModal').addEventListener('click', fecharModal); // Fecha o modal ao clicar no botão

    document.getElementById('imagem-url').addEventListener('change', function () {
        const preview = document.getElementById('imagem-preview');
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        } else {
            preview.src = '';
            preview.style.display = 'none';
        }
    });
});
