$(document).ready(function(){
    //initialize modal element on page
    $('.modal-trigger').leanModal();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
            return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $('#upload_photo').submit(function(e){
        e.preventDefault();
        var csrftoken = getCookie('csrftoken');

        var data = new FormData($(this)[0]);
        data.append('csrfmiddlewaretoken', csrftoken);
        //data.append('comment', $(this).find('div.input-field').find('textarea').val());
        //data.append('photo', $(this).find('div.file-field').find('input:file')[0]);
        $.ajax({
            url: "/photo/upload",
            type: "POST",
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: data,
            processData: false,
            contentType: false,
            success: function(data) {
                if(data['code']== 1) {
                    location.reload();
                }
                else {
                    alert(data);
                }
            },
            error: function (xhr, ajaxOptions, thrownError) {
                alert(xhr.status);
                alert(thrownError);
            }
        });
    });
});
