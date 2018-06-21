$(document).ready(
    function () {
        // window.setInterval(
        //     function () {
        //         location.reload(true);
        //     },
        //     3000
        // )
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });
        $(document).on('click', 'button.ajaxlike', function(e) {
            e.preventDefault();
            var link = $(this);
            console.log(link.attr('data-url'))
            $.ajax({url: link.attr('data-url'), method: 'POST'}).done(function(data, status, response) {console.log(status, response)});
        });
    }
)