document.addEventListener("DOMContentLoaded", function() {
    $("input#btn_translate").on("click", function (event){
        const language = $("input#language_code").val();
        url = 'https://fourtonfish.com/hellosalut/?lang=' + language;
        $.get(url, 
            function(data, textStatus, jqXHR){
                $("div#hello").text(data['hello']);
            });
    });
});
