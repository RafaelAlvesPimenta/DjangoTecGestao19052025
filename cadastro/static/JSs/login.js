document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("forgotModal");
  const openModalBtn = document.getElementById("openModal");
  const closeModalBtn = document.getElementById("closeModal");
  const enviarBtn = document.getElementById("enviarCodigo");
  const inputContato = document.getElementById("contatoRecuperacao");

  openModalBtn.addEventListener("click", function (event) {
    event.preventDefault();
    modal.style.display = "block";
  });

  closeModalBtn.addEventListener("click", function () {
    modal.style.display = "none";
  });

  window.addEventListener("click", function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });

  enviarBtn.addEventListener("click", function (e) {
    e.preventDefault();
    const metodo = document.querySelector('input[name="recuperacao"]:checked').value;
    const contato = inputContato.value.trim();

    if (!contato) {
      alert("Por favor, insira seu e-mail ou número de telefone.");
      return;
    }

    if (metodo === "email" && !contato.includes("@")) {
      alert("Por favor, insira um e-mail válido.");
      return;
    }

    if (metodo === "telefone" && !/^\d{10,11}$/.test(contato)) {
      alert("Por favor, insira um telefone válido (somente números).");
      return;
    }

    alert(`Um código de recuperação será enviado para o seu ${metodo === "email" ? "e-mail" : "telefone"}: ${contato}`);
    modal.style.display = "none";

    setTimeout(() => {
     document.getElementById("form_resetpassword").submit();
     }, 100);
  });
});