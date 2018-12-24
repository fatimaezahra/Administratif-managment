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

    $('.insurance_state').change(function () {
        $("#js-insurance-state-form").attr("action", $(this).attr("data-url"));
        var that = $(this);
        state = $(this).prop('checked');
        $("#js-insurance-state-input").val($(this).prop('checked'));
        $("#modal-insurance-state").modal("show");
        $("#btnclose").unbind();
        $("#btnclose").click(function () {
            if (state) {
                that.bootstrapToggle('off');
            } else {
                that.bootstrapToggle('on')
            }
        });
    });


    $("#idsearch").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });

    $('#checkMethod2').hide();
    $('#checkMethod2').prev().hide();
    $('#checkMethod2').prop("disabled", true);

    $('#checkMethod').change(function () {
        var value = $(this).val();
        if (value != null && value.trim() !== "" && value === "check") {
            $('#checkMethod2').show();
            $('#checkMethod2').prev().show();
            $('#checkMethod2').prop("disabled", false);
        } else {
            $('#checkMethod2').prev().hide();
            $('#checkMethod2').hide();
            $('#checkMethod2').prop("disabled", true);
        }

    })

    $("#id_Patient").empty();
    $('#id_collaborator').change(function () {
        var value = $(this).val();
        var name = $("#id_collaborator option:selected").text();;
        $.get("/insurance/collaborator-patient/" + value, function (data, status) {
            var $el = $("#id_Patient");
            $el.empty(); // remove old options
            $.each(data, function (key, value) {
                $el.append($("<option></option>")
                    .attr("value", value.key).text(value.value));
            });
            $("#id_Patient").prepend("<option value='" + value + "' selected='selected'>" + name + "</option>");
        });
    })

});