 $('.remove_campus_button').click(function() {
        this_button_parrent_parent = $(this).parent().parent();
        this_button_parrent_parent.remove();
    })

$(document).on("submit", "form", function(e) {
    if (confirm('Submitting data. Continue?')) {
        campus_name_elements = $('.campus_name').elements

       return true;
    }
    else {
       return false;
    }
})

$('#add-campus-name').click(
    function() {addCampusNameInput()}
    )

function addCampusNameInput() {
    var campus_container = document.getElementById('campus-names-input-wrapper');

    var result_html =
            '<div class="row mt1 campus-name-fade-in">' +
                '<div class="col-4 centerv npl">' +
                    'Campus Name ' +
                '</div>' +
                '<div class="col-7">' +
                    '<input required class="campus_name" ' +
                    'type="text" placeholder="•••••••••••••••••"/>' +
                '</div>' +
                '<div class="col-1">' +
                    '<div class="edu-button edu-button-orange remove_campus_button">X</div>' +
                '</div>' +
            '</div>'

    campus_container.innerHTML += result_html
    $('.remove_campus_button').click(function() {
        this_button_parrent_parent = $(this).parent().parent();
        this_button_parrent_parent.remove();
    })
}

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
            '</div>' +
            '<div class="col-1">' +
                '<div class="edu-button edu-button-orange remove_campus_button">X</div>' +
            '</div>'
    }
    campus_container.innerHTML = result_html;
}
