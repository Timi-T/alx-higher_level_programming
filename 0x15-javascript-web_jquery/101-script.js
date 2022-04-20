document.addEventListener("DOMContentLoaded", function() {
    $("div#add_item").on("click", function ( event ){
        $("ul.my_list").append("<li>Item</li>");
    });
    $("div#remove_item").on("click", function ( event ){
        $("ul.my_list > :last-child").remove();
    })
    $("div#clear_list").on("click", function ( event ){
        $("ul.my_list li").each(function (){
            $(this).remove();
        })
    })
  });
