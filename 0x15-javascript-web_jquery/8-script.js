const url = "https://swapi-api.hbtn.io/api/films/?format=json"
$.get(url,
    function (data, textStatus, jqXHR){
        $.each( data.results, function( key, value ){
            $("ul#list_movies").append("<li>"+value['title']+"</li>")
        });
    });
