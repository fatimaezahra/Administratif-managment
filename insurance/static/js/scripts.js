$(document).ready(function () {
    $('.datepicker').datepicker({
        format: 'yyyy-mm-dd'
    });

    $(".js-delete-insurance").click(function () {
        $("#js-insurance-delete-form").attr("action", $(this).attr("data-url"));
        $("#modal-insurance").modal("show");
    });


    $(".js-update-pw").click(function () {
        $("#js-update-password").attr("action", $(this).attr("data-url"));
        $("#modal-change-password").modal("show");
    });

    var state = $('#insurance_state').prop('checked');

    $('#insurance_state').change(function () {
        state = $(this).prop('checked');
        $("#js-insurance-state-input").val($(this).prop('checked'));
        $("#modal-insurance-state").modal("show");
    })

    $("#btnclose").on("click", function () {
        if (state) {
            $('#insurance_state').bootstrapToggle('off');
        } else {
            $('#insurance_state').bootstrapToggle('on')
        }
    })
});