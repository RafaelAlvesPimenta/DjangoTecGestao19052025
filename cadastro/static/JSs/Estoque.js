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
// });
