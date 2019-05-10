let campus_event_counter = 1
function addCampusEvent(){
    campus_event_counter += 1
    let name_div = document.getElementById(
        'div_id_campus-dates-event_name');
    let start_date_div = document.getElementById(
        'div_id_campus-dates-date_start');
    let end_date_div = document.getElementById(
        'div_id_campus-dates-date_end');
    let http_link_div = document.getElementById(
        'div_id_campus-dates-http_link');
    let new_name_div = name_div.cloneNode(true);
    let new_start_date_div = start_date_div.cloneNode(true);
    let new_end_date_div = end_date_div.cloneNode(true);
    let new_http_link_div = http_link_div.cloneNode(true);
    clearElement(new_name_div);
    clearElement(new_start_date_div);
    clearElement(new_end_date_div);
    clearElement(new_http_link_div);
    // let new_hr = document.createElement('hr');
    let new_remove_button_row = document.createElement('div');
    new_remove_button_row.innerHTML = getRemoveGroupRow();
    let form_group = (
        document.getElementsByClassName('form-group')[0]);
    new_remove_button_row.classlist += 'row';
    let new_start_date_input = new_start_date_div.getElementsByTagName('input')[0];
    let new_end_date_input = new_end_date_div.getElementsByTagName('input')[0];
    let new_events_group_div = document.createElement("div");

    new_events_group_div.appendChild(new_remove_button_row)
    new_events_group_div.appendChild(new_name_div);
    new_events_group_div.appendChild(new_start_date_div);
    new_events_group_div.appendChild(new_end_date_div);
    new_events_group_div.appendChild(new_http_link_div);

    form_group.append(new_events_group_div);
    
    $(new_start_date_input).removeClass('hasDatepicker');
    updateElementID(new_start_date_input, campus_event_counter);
    $(new_start_date_input).datepicker();
    $(new_end_date_input).removeClass('hasDatepicker');
    updateElementID(new_end_date_input, campus_event_counter);
    $(new_end_date_input).datepicker();
    
    innitiateRemoveCampusEventButtons();
    onNameEditMakeOtherFieldsRequired();
    clearElement(new_name_div)

}

function updateElementID(e, counter){
     $(e).attr('id', $(e).attr('id') + '_' + counter.toString());
}

function clearElement(elementToClear) {
       $(elementToClear).find('input:text').val('');
};

function innitiateRemoveCampusEventButtons() {
    $('.remove-campus-event-button').click(function() {
        var parent_div = this.parentElement.parentElement.parentElement.parentElement;
        parent_div.remove();
    })
 }

function innitiateRemoveFirstEventButton() {
    $('.remove-first-campus-event-button').click(function (e) {
        let target = e.target.parentNode.parentNode.parentNode;
        let newTarget = $(target).prev();
        for (let i = 0; i < 4; i++) {

            $(newTarget).find("input").val("");
            newTarget = $(newTarget).prev();
        }
        markAllFieldsRequiredOrNot();
    })
 }

function getRemoveGroupRow() {
    let button_html = '<div class="remove-campus-event-button">' +
        '<div class="remove-campus-button-inner ">X</div></div>'
    let result = (  '<div class="row">' +
                    '<div class="col-11"><hr/></div><div class="col-1">' +
        button_html + '</div>')
    return result
}

function getRemoveFirstGroupRow() {
    let button_html = '<div class="remove-first-campus-event-button">' +
        '<div class="remove-campus-button-inner ">X</div></div>'
    let result = (  '<div class="row">' +
                    '<div class="col-11"><hr/></div><div class="col-1">' +
        button_html + '</div>')
    return result
}

function markAllFieldsRequiredOrNot(){
    $('[name=campus-dates-event_name]').each(function (index, nextElement) {
        // Check if my next element is empty
        if ($(nextElement).val().length == 0) {
            let nextInputParent = $(nextElement).parent().parent()
            for (let i = 0; i < 3; i++) {
                let nextInput = nextInputParent.next().find('input')
                nextInput.prop('required', false);
                let nextLabel = nextInputParent.find('label');
                nextLabel.text(nextLabel.text().toString().replace('*', ''));
                nextInputParent = $(nextInput).parent().parent()
            }

        } else {
            let nextInputParent = $(nextElement).parent().parent()
            for (let i = 0; i < 3; i++) {
                let nextInput = nextInputParent.next().find('input')
                let nextLabel = nextInputParent.find('label');
                nextLabel.text(nextLabel.text().toString().replace('*', ''));
                nextLabel.text(nextLabel.text().toString() + '*');

                // nextLabel.html(nextLabel.html + '*');
                nextInput.prop('required', true);
                nextInputParent = $(nextInput).parent().parent()
            }
        }
    });
}

function onNameEditMakeOtherFieldsRequired()
{
    $('[name=campus-dates-event_name]').each(function(index, nextElement) {
        $(nextElement).change(function() {
            // Check if my next element is empty
            if ($(nextElement).val().length == 0) {
                let nextInputParent = $(nextElement).parent().parent()
                for (let i = 0; i < 3; i ++) {
                    let nextInput = nextInputParent.next().find('input')
                    nextInput.prop('required', false);
                    let nextLabel = nextInputParent.find('label');
                    nextLabel.text(nextLabel.text().toString().replace('*', ''));
                    nextInputParent = $(nextInput).parent().parent()
                }

            }
            else {
                let nextInputParent = $(nextElement).parent().parent()
                for (let i = 0; i < 3; i ++) {
                    let nextInput =nextInputParent.next().find('input')
                    let nextLabel = nextInputParent.find('label');
                    nextLabel.text(nextLabel.text().toString().replace('*', ''));
                    nextLabel.text(nextLabel.text().toString() + '*');

                    // nextLabel.html(nextLabel.html + '*');
                    nextInput.prop('required', true);
                    nextInputParent = $(nextInput).parent().parent()
                }
            }
        })
    });
}

$(document).ready(function () {
    onNameEditMakeOtherFieldsRequired();
    $('#add-campus-event').click(function () {
            addCampusEvent();
        }
    );
    let event_counter = 0;
    innitiateRemoveCampusEventButtons();
    let dateInputlist = $('.dateinput');
    dateInputlist.each(function (key, each_datepicker) {
        $(each_datepicker).removeClass("hasDatepicker");
        updateElementID(each_datepicker, event_counter);
        $(each_datepicker).datepicker();
        event_counter += 1;
    });
    addRemoveButtonToFirstGroup();

})

function addRemoveButtonToFirstGroup(){
    $('#div_id_campus-dates-http_link').parent().append(getRemoveFirstGroupRow());
    innitiateRemoveFirstEventButton();

    // Check if my next element is empty
}
