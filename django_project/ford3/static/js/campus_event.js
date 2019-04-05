$('#add-campus-event').click(function () {
        addCampusEvent();
    }
);

function addCampusEvent(){
        let name_div = document.getElementById('div_id_2-name');
        let start_date_div = document.getElementById('div_id_2-date_start');
        let end_date_div = document.getElementById('div_id_2-date_end');
        let http_link_div = document.getElementById('div_id_2-http_link');

        let new_name_div = name_div.cloneNode(true);
        let new_start_date_div = start_date_div.cloneNode(true);
        let new_end_date_div = end_date_div.cloneNode(true);
        let new_http_link_div = http_link_div.cloneNode(true);
        clearElement(new_name_div);
        clearElement(new_start_date_div);
        clearElement(new_end_date_div);
        clearElement(new_http_link_div);

        let new_hr = document.createElement('hr')
        let form_group = (
            document.getElementsByClassName('form-group')[0]);
        form_group.appendChild(new_hr);
        form_group.appendChild(new_name_div);
        form_group.appendChild(new_start_date_div);
        form_group.appendChild(new_end_date_div);
        form_group.appendChild(new_http_link_div);
}

function clearElement(elementToClear) {
       $(elementToClear).find('input:text').val('');
};

function updateElementID(elementID) {}
