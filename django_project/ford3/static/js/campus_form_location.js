
$(document).ready(function () {
    setupMap()
})

const setupMap = () => {
    let hidden_location_x = document.querySelector('#id_campus-location-location_value_x').value
    let hidden_location_y = document.querySelector('#id_campus-location-location_value_y').value
    var current_location = [hidden_location_x, hidden_location_y]
    // This code is adapted from the fiddle demo for: https://github.com/jonataswalker/ol-geocoder
    var olview = new ol.View({center: [0, 0], zoom: 17}),
        baseLayer = new ol.layer.Tile({source: new ol.source.OSM()}),
        map = new ol.Map({
            target: document.getElementById('address_map'),
            view: olview,
            layers: [baseLayer]
        });

    // popup
    var popup = new ol.Overlay.Popup();
    map.addOverlay(popup);

    if (!((hidden_location_x == 0) && (hidden_location_y == 0))) {
        var marker = new ol.Feature({
            geometry: new ol.geom.Point(current_location),
        });
        var vectorSource = new ol.source.Vector({
            features: [marker]
        });
        var markerVectorLayer = new ol.layer.Vector({
            source: vectorSource,
            style: new ol.style.Style({
                image: new ol.style.Circle({
                    radius: 7,
                    fill: new ol.style.Fill({
                        color: '#F99824'
                    })
                })
            })
        });
        map.addLayer(markerVectorLayer);
    }

//Instantiate with some options and add the Control
    var geocoder = new Geocoder('nominatim', {
        provider: 'osm',
        lang: 'en',
        placeholder: 'Search for ...',
        limit: 5,
        debug: true,
        autoComplete: true,
        keepOpen: true
    });
    map.addControl(geocoder);

//Listen when an address is chosen
    geocoder.on('addresschosen', function (evt) {
        setAddress(evt);
        window.setTimeout(function () {
            popup.show(evt.coordinate, evt.address.formatted);
        }, 3000);
    });

}

const setAddress = (evt) => {
    let input_line_1 = document.querySelector('#id_campus-location-physical_address_line_1')
    let input_line_2 = document.querySelector('#id_campus-location-physical_address_line_2')
    let input_city = document.querySelector('#id_campus-location-physical_address_city')
    let input_code = document.querySelector('#id_campus-location-physical_address_postal_code')
    let hidden_location_x = document.querySelector('#id_campus-location-location_value_x')
    let hidden_location_y = document.querySelector('#id_campus-location-location_value_y')
    let address_details = evt['address']['details']
    let original_details = evt['address']['original']['details']

    let city = address_details['city']
    let line1 = address_details['houseNumber'] + ' ' + address_details['road']
    let line2 = original_details['suburb']
    let post_code = address_details['postcode']
    let coord_x = evt['coordinate'][0]
    let coord_y = evt['coordinate'][1]


    input_line_1.value = line1
    input_line_2.value = line2
    input_city.value = city
    input_code.value = post_code
    hidden_location_x.value = coord_x
    hidden_location_y.value = coord_y
}
