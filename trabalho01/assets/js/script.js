$(function() {
    $("#submit-button").click(function(){
        if (nameValidation()) {
            alert ('ok')
        }

        else {
            alert('erro')
        }
    })
})



function nameValidation() {
    let nome = $("#nome")

    if (nome.val() == '') {
        nome.addClass("is-invalid")
        nome.removeClass("is-valid")
        return false
    }
    
    nome.addClass("is-valid")
    nome.removeClass("is-invalid")      
    return true
}