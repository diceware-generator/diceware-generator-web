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
