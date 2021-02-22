$(function () {
  $("#botao-inscricao-newsletter").click(function () {
    let nome_valido = validaNomeFunction();
    let email_valido = validaEmail();

    if (nome_valido && email_valido) {
      alert("Tudo ok!");
    } else {
      alert("Deu erro!");
    }
  });
});

function validaNomeFunction() {
  let nome = $("#nome");

  if (nome.val() == "") {
    nome.addClass("is-invalid");
    nome.removeClass("is-valid");
    return false;
  }

  nome.removeClass("is-invalid");
  nome.addClass("is-valid");
  return true;
}

function validaEmail() {
  let email = $("#email");
  //script padrao de validacao de e-mail utilizando regex
  var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
  if (!regex.test(email.val())) {
    email.addClass("is-invalid")
    email.removeClass("is-valid")
    return false
  }
  email.removeClass("is-invalid")
  email.addClass("is-valid")
  return true
}
