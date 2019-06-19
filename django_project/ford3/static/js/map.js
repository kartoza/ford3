
const setupMap = (location_x, location_y) => {
    var current_location = [location_x, location_y]
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

    addMarker(map, current_location);
    //Instantiate with some options and add the Control
    var geocoder = new Geocoder('nominatim', {
        provider: 'osm',
        lang: 'en',
        placeholder: 'Search for ...',
        limit: 5,
        debug: false,
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

    olview.animate({
          center: current_location,
          duration: 2000
        });
}

const addMarker = (map, current_location) => {
    // Location 0, 0 indicates no location has been saved
    if (!((current_location[0] == 0) && (current_location[1] == 0))) {
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
}
