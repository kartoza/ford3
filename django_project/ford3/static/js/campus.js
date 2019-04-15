$(document).ready(function () {
    toggleSidebar();
    setPostalAddressEnabled();
})


function setPostalAddressEnabled() {
    let postal_street_element = document.getElementById('id_campus-location-postal_address_street_name');
    let postal_city_element = document.getElementById('id_campus-location-postal_address_city');
    let postal_code_element = document.getElementById('id_campus-location-postal_address_postal_code');
    let postal_address_does_differ = document.getElementById("id_campus-location-postal_address_differs").checked;
    if (postal_address_does_differ) {
        postal_street_element.required = true;
        postal_city_element.required = true;
        postal_code_element.required = true;
        postal_street_element.disabled = false;
        postal_city_element.disabled = false;
        postal_code_element.disabled = false;
    }
    else {
        postal_street_element.required = false;
        postal_city_element.required = false;
        postal_code_element.required = false;
        postal_street_element.disabled = true;
        postal_city_element.disabled = true;
        postal_code_element.disabled = true;
    }
}

$('#id_campus-location-postal_address_differs').click(function(e) {
    setPostalAddressEnabled()
});
