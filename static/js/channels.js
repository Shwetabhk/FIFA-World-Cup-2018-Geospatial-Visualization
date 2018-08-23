var apiKey = secretToken;
var mapCenter = [55.715765, 37.551521708]

L.mapbox.accessToken = apiKey;

var map = L.mapbox.map('map', 'mapbox.dark', {
    zoomControl: true
}).setView([mapCenter[0], mapCenter[1]], 2);

map.dragging.disable();
map.touchZoom.disable();

var markers = L.mapbox.featureLayer().addTo(map);
markers.setGeoJSON(data);
markers.on('click', function (e) {
    e.layer.closePopup();

    var feature = e.layer.feature;
    var title = feature.properties.title;
    var content = feature.properties.description;
    var city = feature.properties.address;

    $("#marker_title").text(title);
    $("#marker_content").text(content);
    $("#marker_latlng").text(city);
    $('#exampleModal').modal('show');
});

$('.menu-ui a').on('click', function () {
    var filter = $(this).data('filter');
    $(this).addClass('active').siblings().removeClass('active');
    markers.setFilter(function (f) {
        return (filter === 'all') ? true : f.properties.language === filter;
    });
    return false;
});