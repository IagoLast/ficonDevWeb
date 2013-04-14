// $("form").on("submit", function() {
//     $.ajax({ 
//         url: '/groups/dissolve/$org_ID', 
//         type: 'DELETE', 
//         success: function(result) { 
//                 // Do something with the result 
//         } 
//     });  
// });

function setContent(newContent){
    $("#content").html(newContent);
}

function ajaxAdminDishes(){
    $.ajax({
        url:"/admin/dishes",
        success:setContent
    });
}


function ajaxAdminMenus(){
    $.ajax({
        url:"/admin/menus",
        success:setContent
    });
}


function ajaxAdminUsers(){
    $.ajax({
        url:"/admin/users",
        success:setContent
    });
}

$(".admin-dishes-link").click(ajaxAdminDishes);
$(".admin-menus-link").click(ajaxAdminMenus);
$(".admin-users-link").click(ajaxAdminUsers);

var buttons = $(".delete-btn");
var buttonsCount = buttons.length;
if(buttonsCount){
    for (var i = 0; i <= buttonsCount; i++) {
        buttons[i].onclick = function(e) {
            id = this.id
            $.ajax({
                type: "DELETE",
                url: "/admin/dishes/"+id,
            });
            id = "#"+id;
            $(id).parent().hide();
        };
    }
}