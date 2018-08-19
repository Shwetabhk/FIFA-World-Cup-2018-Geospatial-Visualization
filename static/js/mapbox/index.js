mapboxgl.accessToken = "{{secretToken}}";
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v10',
    center: [37.5515217, 55.715765],
    zoom: 1.5
});
'{%for i in stadiums%}'
var popup = new mapboxgl.Popup().setHTML('{{i.name}}');
var marker = new mapboxgl.Marker()
.setLngLat(['{{i.longitude}}', '{{i.latitude}}'])
.setPopup(popup)
.addTo(map);
'{%endfor%}'