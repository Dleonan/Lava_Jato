
document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("modal");
    const btnAbrirModal = document.getElementById("btnAbrirModal");
    const btnFechar = document.querySelector(".fechar");

    if (btnAbrirModal) {
        btnAbrirModal.addEventListener("click", function () {
            modal.style.display = "block";
        });
    }

    if (btnFechar) {
        btnFechar.addEventListener("click", function () {
            modal.style.display = "none";
        });
    }

    window.addEventListener("click", function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
});
