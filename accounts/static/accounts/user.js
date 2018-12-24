$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-user").modal("show");
      },
      success: function (data) {
        $("#modal-user .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-user ").modal("hide");
        }
        else {
          $("#modal-user .modal-content").html(data.html_form);
        }
        $("#user-table tbody").html(data.html_user_list);
      },
      error: function (dat){
        alert('error')
      }
    });
    return false;
  };


  //$("#user-table").on("click", ".js-update-pw", loadForm);
  //$("#modal-user").on("submit", ".js-update-password", saveForm);

  // Delete user
  $("#user-table").on("click", ".js-delete-user", loadForm);
  $("#modal-user").on("submit", ".js-user-delete-form", saveForm);

});