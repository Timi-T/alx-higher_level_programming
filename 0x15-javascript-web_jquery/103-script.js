document.addEventListener("DOMContentLoaded", function() {
    $("input#language_code").keyup(function (event){
        const key_pressed = event.which;
        if (key_pressed === 13){
            const language = $("input#language_code").val();
            url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
            $.get(url, 
                function(data, textStatus, jqXHR){
                    $("div#hello").text(data['hello']);
                });
        }
    });

    $("input#btn_translate").on("click", function (event){
        const language = $("input#language_code").val();
        url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
        $.get(url, 
            function(data, textStatus, jqXHR){
                $("div#hello").text(data['hello']);
            });
    });
});
