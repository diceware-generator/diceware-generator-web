function copyClipBoard() {
  const pass = document.getElementById('password').value; 
  navigator.clipboard.writeText(pass)
}

function hydePass() {
  formPass = document.getElementById("password");
  if (formPass.type === "text") {
    formPass.type = "password";
  } else {
    formPass.type = "text";
}}

async function getNewPass() {
  const url = "/api/get-diceware";
  await fetch(url)
      .then(
          response => response.text() 
      ).then(
          html => {document.getElementById('password').value = html}
      );
}