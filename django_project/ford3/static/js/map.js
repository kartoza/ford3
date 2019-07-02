const setupMap = (locationX, locationY) => {
  let mapContainer = document.getElementById('address_map')
  mapContainer.innerHTML = ''
  let currentLocation = [locationX, locationY]
  // This code is adapted from the fiddle demo for: https://github.com/jonataswalker/ol-geocoder
  let olsource = new ol.source.OSM()
  let olview = new ol.View({
    center: [0, 0],
    zoom: 5
  })

  if (locationX.length === 0 && locationY.length === 0) {
    olview.setCenter([2753529.9913838077, -3460334.186405535])
  } else {
    olview.setCenter(currentLocation)
  }

  let baseLayer = new ol.layer.Tile({ source: olsource })

  let map = new ol.Map({

    target: mapContainer,
    view: olview,
    layers: [baseLayer]
  })
  // popup
  let popup = new ol.Overlay.Popup()
  map.addOverlay(popup)
  addMarker(map, currentLocation)
  // Instantiate with some options and add the Control
  let geocoder = new Geocoder('nominatim', {
    provider: 'osm',
    lang: 'en',
    placeholder: 'Search for ...',
    limit: 5,
    debug: true,
    autoComplete: true,
    keepOpen: false
  })
  map.addControl(geocoder)
  // Listen when an address is chosen
  geocoder.on('addresschosen', function (evt) {
    setupMap(evt.coordinate[0], evt.coordinate[1])
    setAddress(evt)
  })
  olview.animate({
    center: currentLocation,
    duration: 2000
  })

  map.on('singleclick', function (evt) {
    setLocation(evt)
    addMarker(map, evt.coordinate)
  })
}

// const marker = null
// const markerVectorLayer = null
// const vectorSource = null

const addMarker = (map, currentLocation) => {
  if (this.markerVectorLayer) {
    this.vectorSource.clear()
  }
  // Location 0, 0 indicates no location has been saved
  if (!((currentLocation[0] == 0) && (currentLocation[1] == 0))) {
    this.marker = new ol.Feature({
      geometry: new ol.geom.Point(currentLocation)
    })
    this.vectorSource = new ol.source.Vector({
      features: [this.marker]
    })
    this.markerVectorLayer = new ol.layer.Vector({
      source: this.vectorSource,
      style: new ol.style.Style({
        image: new ol.style.Circle({
          radius: 7,
          fill: new ol.style.Fill({
            color: '#F99824'
          })
        })
      })
    })
    map.addLayer(this.markerVectorLayer)
  }
}
