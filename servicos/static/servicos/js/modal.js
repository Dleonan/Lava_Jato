document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('modal');
    const btn = document.getElementById('btnAbrirModal');
    const span = document.querySelector('.fechar');

    btn.onclick = () => modal.style.display = 'block';
    span.onclick = () => modal.style.display = 'none';
    window.onclick = (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };
});
