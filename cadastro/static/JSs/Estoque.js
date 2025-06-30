// let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

// function salvarProdutos() {
//     localStorage.setItem('produtos', JSON.stringify(produtos));
// }

// function carregarProdutos() {
//     const container = document.getElementById('product-list');
//     if (!container) return;

//     container.innerHTML = ''; // Limpa o conteúdo atual da lista

//     produtos.forEach((produto) => {
//         const card = document.createElement('div');
//         card.className = 'card';

//         // Lógica para definir a cor da bolinha
//         let statusClasse = 'disponivel';
//         if (produto.quantidadeAtual === 0) {
//             statusClasse = 'indisponivel-vermelho'; // Produto em falta (vermelho)
//         } else if (produto.quantidadeAtual <= produto.quantidadeMaxima * 0.5) {
//             statusClasse = 'indisponivel-laranja'; // Produto abaixo de 50% do estoque (laranja)
//         }

//         const statusTexto = produto.quantidadeAtual > 0 ? 'Disponível' : 'Indisponível';

//         card.innerHTML = `
//             <img src="${produto.imagem}" alt="${produto.nome}">
//             <div>
//                 <h1>${produto.nome}</h1>
//                 <div class="status">
//                     <h2>${statusTexto} <span class="status-dot ${statusClasse}"></span></h2>
//                 </div>
//                 <span>${produto.quantidadeAtual}/${produto.quantidadeMaxima}</span>
//             </div>
//         `;

//         container.appendChild(card); // Adiciona o card à lista de produtos
//     });
// }

// function abrirModal() {
//     document.getElementById('modal').style.display = 'flex';
// }

// function fecharModal() {
//     document.getElementById('modal').style.display = 'none';
// }

// window.onclick = function(event) {
//     const modal = document.getElementById('modal');
//     if (event.target === modal) {
//         modal.style.display = 'none';
//     }
// }

// function cadastroProduto() {
//     const nome = document.getElementById('nome-produto').value.trim();
//     const categoria = document.getElementById('categoria-produto').value;
//     const quantidade = parseInt(document.getElementById('quantidade-produto').value);
//     const maximo = parseInt(document.getElementById('estoque-minimo').value);
//     const imagemInput = document.getElementById('imagem-url');

//     if (!nome || !categoria || isNaN(quantidade) || isNaN(maximo) || quantidade < 0 || maximo < 0 || quantidade > maximo) {
//         alert("Preencha os campos corretamente.");
//         return;
//     }

//     const reader = new FileReader();

//     reader.onload = function (e) {
//         const imagemURL = e.target.result;

//         const produto = {
//             nome,
//             categoria,
//             quantidadeAtual: quantidade,
//             quantidadeMaxima: maximo,
//             imagem: imagemURL
//         };

//         produtos.push(produto);
//         salvarProdutos();
//         finalizarCadastro();
//     };

//     if (imagemInput.files && imagemInput.files[0]) {
//         reader.readAsDataURL(imagemInput.files[0]);
//     } else {
//         const produto = {
//             nome,
//             categoria,
//             quantidadeAtual: quantidade,
//             quantidadeMaxima: maximo,
//             imagem: 'https://via.placeholder.com/150'
//         };
//         produtos.push(produto);
//         salvarProdutos();
//         finalizarCadastro();
//     }
// }

// function finalizarCadastro() {
//     carregarProdutos(); // Recarrega os produtos para atualizar a lista
//     document.getElementById('formCadastro').reset(); // Limpa o formulário
//     document.getElementById('imagem-preview').style.display = 'none'; // Esconde a imagem de pré-visualização
//     document.getElementById('modal').style.display = 'none'; // Fecha o modal
//     alert("Produto cadastrado com sucesso!");
// }

// document.addEventListener('DOMContentLoaded', () => {
//     carregarProdutos(); // Carrega os produtos ao carregar a página

//     document.getElementById('formCadastro').addEventListener('submit', function (e) {
//         e.preventDefault(); // Impede o envio do formulário
//         cadastroProduto(); // Chama a função de cadastro do produto
//     });

//     document.getElementById('fecharModal').addEventListener('click', fecharModal); // Fecha o modal ao clicar no botão

//     document.getElementById('imagem-url').addEventListener('change', function () {
//         const preview = document.getElementById('imagem-preview');
//         const file = this.files[0];

//         if (file) {
//             const reader = new FileReader();
//             reader.onload = function (e) {
//                 preview.src = e.target.result;
//                 preview.style.display = 'block';
//             };
//             reader.readAsDataURL(file);
//         } else {
//             preview.src = '';
//             preview.style.display = 'none';
//         }
//     });
// });


    button_open_modal = document.getElementById('abrirModal')
    button_close_modal = document.getElementById('fecharModal')
    modal_new_product = document.getElementById('modalCadastro')

    security_close_modal = document.querySelectorAll('.security_close_modal')
    button_yes_close = document.getElementById('sim')
    button_no_close = document.getElementById('nao')

    button_open_modal.addEventListener("click", function() {
        modal_new_product.style.display ="flex";
    });

    button_close_modal.addEventListener("click", function() {
        security_close_modal.forEach(modal => {
            modal.style.display = 'flex';
          });
        button_yes_close.addEventListener("click", function() {
            security_close_modal.forEach(modal => {modal.style.display = 'none';});
            modal_new_product.style.display = "none";
        })
        button_no_close.addEventListener("click", function() {
            security_close_modal[0].style.display = 'none';
        })

    });

    button_new_category = document.getElementById('button_new_category')
    form_new_category = document.getElementById('backend_form_new_category')
    button_new_category.addEventListener("click", function(){
        document.getElementById('new_category').value = "";
        form_new_category.style.display = 'flex'
    })
    button_close_modal_new_category = document.getElementById('fecharModal_new_category')
    button_close_modal_new_category.addEventListener('click', function() {
        form_new_category.style.display = 'none'
    });


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

    // Função para abrir o modal de edição
function abrirModalEditar(botao) {
    document.body.classList.add('noscroll');
    // Obter todos os dados do produto dos atributos data-*
    const produto = {
        id: botao.getAttribute('data-id'),
        nome: botao.getAttribute('data-nome'),
        quantidade: botao.getAttribute('data-quantidade'),
        min: botao.getAttribute('data-min'),
        max: botao.getAttribute('data-max'),
        descricao: botao.getAttribute('data-descricao'),
        custo: botao.getAttribute('data-custo'),
        valor: botao.getAttribute('data-valor'),
        categoria: botao.getAttribute('data-categoria'),
        imagem: botao.getAttribute('data-imagem')
    };

    // Preencher o formulário de edição com os dados
    document.getElementById('editar-produto-id').value = produto.id;
    document.getElementById('editar-nome-produto').value = produto.nome;
    document.getElementById('editar-quantidade').value = produto.quantidade;
    document.getElementById('editar-quantidade-min').value = produto.min;
    document.getElementById('editar-quantidade-max').value = produto.max;
    document.getElementById('editar-descricao').value = produto.descricao;
    document.getElementById('editar-custo-producao').value = produto.custo;
    document.getElementById('editar-valor').value = produto.valor;
    
    // Definir a categoria selecionada
    const selectCategoria = document.getElementById('editar-categoria');
    selectCategoria.value = produto.categoria;
    
    // Exibir a imagem atual
    const imgPreview = document.getElementById('editar-imagem-preview');
    imgPreview.src = produto.imagem;
    imgPreview.style.display = 'block';

    // Mostrar o modal
    document.getElementById('modalEditar').style.display = 'flex';
}

// Função para fechar o modal de edição
function fecharModalEditar() {
    document.body.classList.remove('noscroll');
    security_close_modal.forEach(modal => {
        modal.style.display = 'flex';
      });
      button_yes_close.addEventListener("click", function() {
        security_close_modal.forEach(modal => {modal.style.display = 'none';});
        document.getElementById('modalEditar').style.display = 'none';
    })
    button_no_close.addEventListener("click", function() {
        security_close_modal[0].style.display = 'none';
    })
    // document.getElementById('modalEditar').style.display = 'none';
}


// });
