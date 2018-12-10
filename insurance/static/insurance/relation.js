$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-relation").modal("show");
      },
      success: function (data) {
        $("#modal-relation .modal-content").html(data.html_form);
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
          $("#modal-relation ").modal("hide");
        }
        else {
          $("#modal-relation .modal-content").html(data.html_form);
        }
        $("#relation-table tbody").html(data.html_relation_list);
      },
      error: function (dat){
        alert('error')
      }
    });
    return false;
  };


  /* Binding */

  // Create relation
  $(".js-create-relation").click(loadForm);
  $("#modal-relation").on("submit", ".js-relation-create-form", saveForm);

  // Update relation
  $("#relation-table").on("click", ".js-update-relation", loadForm);
  $("#modal-relation").on("submit", ".js-relation-update-form", saveForm);

  // Delete relation
  $("#relation-table").on("click", ".js-delete-relation", loadForm);
  $("#modal-relation").on("submit", ".js-relation-delete-form", saveForm);

});