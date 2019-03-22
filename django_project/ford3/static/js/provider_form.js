	var map = new ol.Map({
    target: 'map',
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    view: new ol.View({
        center: ol.proj.fromLonLat([37.41, 8.82]),
        zoom: 4
    })
});

var slider = document.getElementById('campus-count');
var output = document.getElementById('number-of-campuses');
slider.value = 1;
output.value = slider.value; // Display the default slider value
// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {
    output.value = this.value;

    createCampusNameInputs(this.value);
}


function createCampusNameInputs(campus_count) {
    var i;
    var result_html = '';
    var campus_container = document.getElementById('campus-names-input-wrapper');
    campus_container.innerHTML = '';
    for (i = 0; i < campus_count; i++) {
        result_html += `
            <div class="row mt1 campus-name-fade-in">
                <div class="col-4 centerv npl">
                    Name of Campus ${i + 1}:
                </div>
                <div class="col-8">
                    <input name="campus_name_${i + 1}" id="campus_name_${i + 1}" type="text" placeholder="•••••••••••••••••"/>
                </div>
            </div>`
    }
    campus_container.innerHTML = result_html;
}
