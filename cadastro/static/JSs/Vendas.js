document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-venda");
    const tabela = document.getElementById("tabela-vendas");
    const totalFaturado = document.getElementById("total-faturado");
    const totalLucro = document.getElementById("total-lucro");

    let vendas = JSON.parse(localStorage.getItem("vendas")) || [];

    function atualizarTabela() {
        tabela.innerHTML = "";
        let totalFaturamento = 0;
        let totalLucroGeral = 0;

        vendas.forEach((venda, index) => {
            const lucro = (venda.precoVenda - venda.custo) * venda.quantidade;
            totalFaturamento += venda.precoVenda * venda.quantidade;
            totalLucroGeral += lucro;

            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${venda.produto}</td>
                <td>${venda.quantidade}</td>
                <td>R$ ${venda.precoVenda.toFixed(2)}</td>
                <td>R$ ${venda.custo.toFixed(2)}</td>
                <td>R$ ${lucro.toFixed(2)}</td>
                <td>${venda.data}</td>
                <td>
                    <button onclick="excluirVenda(${index})">Excluir</button>
                </td>
            `;
            tabela.appendChild(row);
        });

        totalFaturado.textContent = totalFaturamento.toFixed(2);
        totalLucro.textContent = totalLucroGeral.toFixed(2);
    }

    window.excluirVenda = function(index) {
        vendas.splice(index, 1);
        localStorage.setItem("vendas", JSON.stringify(vendas));
        atualizarTabela();
    }

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const novaVenda = {
            produto: document.getElementById("produto").value,
            quantidade: parseInt(document.getElementById("quantidade").value),
            precoVenda: parseFloat(document.getElementById("precoVenda").value),
            custo: parseFloat(document.getElementById("custo").value),
            data: document.getElementById("dataVenda").value
        };

        vendas.push(novaVenda);
        localStorage.setItem("vendas", JSON.stringify(vendas));
        form.reset();
        atualizarTabela();
    });

    atualizarTabela();
});