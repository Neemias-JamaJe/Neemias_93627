document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formLogin");

    if (!form) return;

    form.addEventListener("submit", function (e) {
        const usuario = document.getElementById("usuario").value.trim();
        const senha = document.getElementById("senha").value.trim();

        if (usuario.length < 3) {
            alert("O usuário deve ter pelo menos 3 caracteres.");
            e.preventDefault();
            return;
        }

        if (senha.length < 3) {
            alert("A senha deve ter pelo menos 3 caracteres.");
            e.preventDefault();
            return;
        }
    });
});
