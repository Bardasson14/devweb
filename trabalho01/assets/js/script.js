$(function() {
    $("#submit-button").click(function(){

        let valid = nameValidation()
        let erro_1 = document.querySelector("#erro-1")

        if (valid) {
            erro_1.classList.remove("d-block")
        }

        else {
            erro_1.classList.add("d-block")
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