//obs I.: não será necessário validar o radio, visto que esse já terá, por padrão, 1 opção checked
//obs II: apenas será necessário validar a 2 checkbox, visto que a primeira é opcional para o usuário

$(function () {
  $("#botao-form-newsletter").click(function() {
    let nome_valido = validaNome();
    let email_valido = validaEmail();
    let freq_valida = validaFrequenciaNewsletter()
    let genero_valido = validaGenero()
    let termos_valido = validaCheckTermos()

    if (nome_valido && email_valido && freq_valida && genero_valido && termos_valido) {
      alert("Tudo ok!")
    } else {
      alert("Erro!")
    }
  })

  $("#botao-form-contato").click(function() {
    let nome_valido = validaNome()
    let email_valido = validaEmail()
    let assunto_valido = validaAssunto()
    let msg_valida = validaMsg()
    if (nome_valido && email_valido && assunto_valido && msg_valida) {
      alert("Tudo ok!")
    }
    else {
      alert("Erro!")
    }
  })


});

function validaNome() {
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

function validaFrequenciaNewsletter() {
  let frequencia = $("#frequencia-newsletter")

  if(frequencia.val() === '') {
     frequencia.addClass("is-invalid")
     frequencia.removeClass("is-valid")
     return false
  }
  else {
     frequencia.removeClass("is-invalid")
     frequencia.addClass("is-valid")
     return true
  }
}

function validaGenero() {

  let gen_m = $("#genero-m")
  let gen_f = $("#genero-f")
  let gen_x = $("#genero-x")
  let genero_feedback = $("#genero-feedback")
  let botoes = $("input[name='genero']:checked")

  if (botoes.length === 0) {
     gen_m.addClass("is-invalid")
     gen_m.removeClass("is-valid")
     gen_f.addClass("is-invalid")
     gen_f.removeClass("is-valid")
     gen_x.addClass("is-invalid")
     gen_x.removeClass("is-valid")
     genero_feedback.addClass("d-block")
     return false
  }
  else {
     gen_m.removeClass("is-invalid")
     gen_m.addClass("is-valid")
     gen_f.removeClass("is-invalid")
     gen_f.addClass("is-valid")
     gen_x.removeClass("is-invalid")
     gen_x.addClass("is-valid")
     genero_feedback.removeClass("d-block")
     return true
  }
}

function validaCheckTermos() {
  let check_termos = $("#permissao-2")
  let termos_feedback = $("#termos-feedback")

  console.log(check_termos.is(":checked"))

  if (!check_termos.is(":checked")) {
    check_termos.addClass("is-invalid")
    check_termos.removeClass("is-valid")
    termos_feedback.addClass("d-block")
    return false
  }

  check_termos.addClass("is-valid")
  check_termos.removeClass("is-invalid")
  termos_feedback.removeClass("d-block")
  return true

}

function validaAssunto() {
  let assunto = $("#assunto")

  if (assunto.val()=='') {
    assunto.addClass("is-invalid")
    assunto.removeClass("is-valid")
    return false
  }

  assunto.addClass("is-valid")
  assunto.removeClass("is-invalid")
  return true
}

function validaMsg() {
  let msg = $("#msg")
  if (msg.val()=='') {
    msg.addClass("is-invalid")
    msg.removeClass("is-valid")
    return false
  }

  msg.addClass("is-valid")
  msg.removeClass("is-invalid")
  return true
}