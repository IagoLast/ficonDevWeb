function setContent(newContent){
   $("#content").html(newContent);
}

function ajaxDishes(){
  $.ajax({
    url:"/dishes",
    success:setContent
  });
}

function ajaxAppetizers(){
    $.ajax({
        url:"/dishes/appetizer",
        success:setContent
    });
}

function ajaxMeats(){
    $.ajax({
        url:"/dishes/meat",
        success:setContent
    });
}

function ajaxFish(){
    $.ajax({
        url:"/dishes/fish",
        success:setContent
    });
}

function ajaxDesserts(){
    $.ajax({
        url:"/dishes/dessert",
        success:setContent
    });
}

function ajaxMenu(){
    $.ajax({
        url:"/menus",
        success:setContent
    });
}

function ajaxLoadPicks(){
    $.ajax({
        url:"/instafood",
        success:setContent
    })

}

// $('#hidebutton').click(myHide);
$(".dishes-link").click(ajaxDishes);
$(".appetizers-link").click(ajaxAppetizers);
$(".meat-link").click(ajaxMeats);
$(".fish-link").click(ajaxFish);
$(".desserts-link").click(ajaxDesserts);
$(".menu-link").click(ajaxMenu);
$(".food-link").click(ajaxLoadPicks);