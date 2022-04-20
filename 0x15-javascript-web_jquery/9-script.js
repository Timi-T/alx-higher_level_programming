const url = "https://fourtonfish.com/hellosalut/?lang=fr"
$.get(url,
    function (data, textStatus, jqXHR){
        $("div#hello").append(data['hello'])
    });
