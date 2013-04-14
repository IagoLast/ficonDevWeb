var buttons = $(".delete-btn");
var buttonsCount = buttons.length;
if(buttonsCount){
    for (var i = 0; i <= buttonsCount; i++) {
        buttons[i].onclick = function(e) {
            id = this.id
            $.ajax({
                type: "DELETE",
                url: "/admin/menus/"+id,
            });
            id = "#"+id;
            $(id).parent().hide();
        };
    }
}