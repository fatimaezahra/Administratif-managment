$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-employee").modal("show");
      },
      success: function (data) {
        $("#modal-employee .modal-content").html(data.html_form);
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
          $("#modal-employee ").modal("hide");
        }
        else {
          $("#modal-employee .modal-content").html(data.html_form);
        }
        $("#employee-table tbody").html(data.html_employee_list);
      },
      error: function (dat){
        alert('error')
      }
    });
    return false;
  };




  // Delete employee
  $("#employee-table").on("click", ".js-delete-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-delete-form", saveForm);

});