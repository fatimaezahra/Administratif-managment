
$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-status").modal("show");
      },
      success: function (data) {
        $("#modal-status .modal-content").html(data.html_form_status);
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
          $("#status-table tbody").html(data.html_status_list);
          $("#modal-status").modal("hide");
        }
        else {
          $("#modal-status .modal-content").html(data.html_form_status);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create book
  $(".js-create-status").click(loadForm);
  $("#modal-status").on("submit", ".js-status-create-form", saveForm);

  // Update book
  $("#status-table").on("click", ".js-update-status", loadForm);
  $("#modal-status").on("submit", ".js-status-update-form", saveForm);

  $("#status-table").on("click", ".js-delete-status", loadForm);
  $("#modal-status").on("submit", ".js-status-delete-form", saveForm);

});