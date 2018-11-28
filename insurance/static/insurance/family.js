$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-family").modal("show");
      },
      success: function (data) {
        $("#modal-family .modal-content").html(data.html_form);
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
          $("#modal-family ").modal("hide");
        }
        else {
          $("#modal-family .modal-content").html(data.html_form);
        }
        $("#family-table tbody").html(data.html_family_list);
      },
      error: function (dat){
        alert('error')
      }
    });
    return false;
  };


  /* Binding */

  // Create family
  $(".js-create-family").click(loadForm);
  $("#modal-family").on("submit", ".js-family-create-form", saveForm);

  // Update family
  $("#family-table").on("click", ".js-update-family", loadForm);
  $("#modal-family").on("submit", ".js-family-update-form", saveForm);

  // Delete family
  $("#family-table").on("click", ".js-delete-family", loadForm);
  $("#modal-family").on("submit", ".js-family-delete-form", saveForm);

});