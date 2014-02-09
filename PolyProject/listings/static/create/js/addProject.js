$(document).on("click", "#addImage", function(e) {
   var box = $("#description");
   box.val(box.val() + "\n <img src='IMAGE_URL_GOES_HERE' width=100% />");
});