var output = document.getElementById('number-of-campuses');
// Update the current slider value (each time you drag the slider handle)
output.onchange = function () {
    createCampusNameInputs(output.value);
}

$(document).on("submit", "form", function(e) {
    var oForm = $(this);
    if (confirm('Submitting data. Continue?')) {
       return true;
    }
    else {
       return false;
    }
})

function createCampusNameInputs(campus_count) {
    var i;
    var result_html = '';
    var campus_container = document.getElementById('campus-names-input-wrapper');
    var campus_count_number;
    campus_container.innerHTML = '';
    for (i = 0; i < campus_count; i++) {
        campus_count_number = i + 1;
        result_html +=
            '<div class="row mt1 campus-name-fade-in">' +
                '<div class="col-4 centerv npl">' +
                    'Name of Campus ' + campus_count_number.toString() +
                '</div>' +
                '<div class="col-8">' +
                    '<input required name="campus_name_' + campus_count_number.toString() + '" ' +
                    'id="campus_name_' + campus_count_number.toString() + '" ' +
                    'type="text" placeholder="•••••••••••••••••"/>' +
                '</div>' +
            '</div>'
    }
    campus_container.innerHTML = result_html;
}
