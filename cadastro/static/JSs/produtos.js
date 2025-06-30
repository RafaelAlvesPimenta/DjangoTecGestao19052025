
/*start modal cadastro*/ 
button_open_modal = document.getElementById('abrirModal')
    button_close_modal = document.getElementById('fecharModal')
    modal_new_product = document.getElementById('modalCadastro')

    security_close_modal = document.querySelectorAll('.security_close_modal')
    button_yes_close = document.getElementById('sim')
    button_no_close = document.getElementById('nao')

    /*função abrir modal de cadastro*/
    button_open_modal.addEventListener("click", function() {
        modal_new_product.style.display = "flex";
        document.body.classList.add('noscroll');
    });

    /*função fechar modal de cadastro*/
    button_close_modal.addEventListener("click", function() {
        security_close_modal.forEach(modal => {
            modal.style.display = 'flex';
          });
        button_yes_close.addEventListener("click", function () {
            document.body.classList.remove('noscroll');
            security_close_modal.forEach(modal => {modal.style.display = 'none';});
            modal_new_product.style.display = "none";
        })
        button_no_close.addEventListener("click", function() {
            security_close_modal[0].style.display = 'none';
        })

    });

    /*função de cadastro nova categoria de produto*/
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
/*end modal cadastro*/

/*strat modal edição*/
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
/*end modal edição*/

// });
