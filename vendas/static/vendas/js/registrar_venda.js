
document.addEventListener("DOMContentLoaded", function () {
    const servicoSelect = document.getElementById("servico-select");
    const valorInput = document.getElementById("valor");
    const servicoValores = JSON.parse(document.getElementById("servico-data").textContent);

    servicoSelect.addEventListener("change", function () {
        const selectedId = this.value;
        const valor = servicoValores[selectedId];
        valorInput.value = valor ? valor.toFixed(2) : "";
    });

    // Preenche valor inicial se o select já tiver valor
    if (servicoSelect.value) {
        valorInput.value = servicoValores[servicoSelect.value].toFixed(2);
    }
});
