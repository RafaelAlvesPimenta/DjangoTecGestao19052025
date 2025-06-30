function saveSpreadsheet() {
    const title = document.querySelector('.inputs-wspreadsheet').value;
    const fileInput = document.getElementById('fileInput').files[0];

    if (!fileInput || !title) {
        alert("Preencha o título e selecione o arquivo.");
        return;
    }

    const fileURL = URL.createObjectURL(fileInput);
    const planilha = { title, fileURL };

    let planilhas = JSON.parse(localStorage.getItem('planilhas')) || [];
    planilhas.push(planilha);
    localStorage.setItem('planilhas', JSON.stringify(planilhas));

    loadPlanilhas();
}

function loadPlanilhas() {
    const planilhas = JSON.parse(localStorage.getItem('planilhas')) || [];
    const listaPlanilhas = document.getElementById('lista-planilhas');
    listaPlanilhas.innerHTML = '';

    planilhas.forEach((planilha, index) => {
        const planilhaElement = document.createElement('div');
        planilhaElement.classList.add('planilha');

        planilhaElement.innerHTML = `
            <img src="https://cdn-icons-png.flaticon.com/512/732/732220.png" alt="Excel">
            <span>${planilha.title}</span>
            <button class="botao-excluir" onclick="deletePlanilha(${index}); event.stopPropagation();">X</button>
        `;

        planilhaElement.addEventListener('click', () => {
            window.open(planilha.fileURL, '_blank');
        });

        listaPlanilhas.appendChild(planilhaElement);
    });
}

function deletePlanilha(index) {
    let planilhas = JSON.parse(localStorage.getItem('planilhas')) || [];
    planilhas.splice(index, 1);
    localStorage.setItem('planilhas', JSON.stringify(planilhas));
    loadPlanilhas();
}

document.getElementById('save-nspreadsheet').addEventListener('click', (event) => {
    event.preventDefault();
    saveSpreadsheet();
    document.getElementById('window-new-spreadsheet').style.display = 'none';
});

document.getElementById('cancel-nspreadsheet').addEventListener('click', (event) => {
    event.preventDefault();
    document.getElementById('window-new-spreadsheet').style.display = 'none';
});

document.getElementById('ad-planilha').addEventListener('click', () => {
    document.getElementById('window-new-spreadsheet').style.display = 'flex';
});

window.onload = loadPlanilhas;
