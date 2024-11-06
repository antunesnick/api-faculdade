document.getElementById("formulario").addEventListener("submit", async (event) => {
    event.preventDefault();

    const name = document.getElementById("firstname").value;
    const email = document.getElementById("email").value;
    const age = document.getElementById("age").value;
    const nickname = document.getElementById("nickname").value;
    const password = document.getElementById("password").value;
    const game = document.getElementById("game").value;

    try {
        const response = await fetch("http://localhost:5000/api/players", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ name, email, age, nickname, password, game })
        });

        const result = await response.json();
        console.log("Resposta da API: ", result);
    } catch (error) {
        console.error("Erro ao enviar dados: ", error);
    }
});
