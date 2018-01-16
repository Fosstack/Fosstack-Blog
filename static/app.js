$(document).ready(function(){
    $(".post_detail img").each(function(){
        $(this).addClass("img-fluid");
    });
});




// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    var $myForm = $('#subscription_ajax')
    $myForm.submit(function(event){
        event.preventDefault()
        var $formData = $(this).serialize()
        $.ajax({
            method: "POST",
            url: '/subscribe',
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    });

    function handleFormSuccess(response){
        if(response.message == 'alreadyExists') {
            alert('Email already registered !','warning');
        }
        else if( response.message == 'successful'){
            alert('Your email is successfully subscribed','success');
        }
        else if( response.message == 'invalid'){
            alert('Enter a valid email address','error');s
        }
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)

        alert('Error occurred !','error');
    }



