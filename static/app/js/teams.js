const targetElement = document.getElementById('flagcards')
const template = UnderscoreTemplate(
    '<button id="filt" class="btn flagcard"  data-filter="<%- properties.title %>"\
        <div class="col-sm-12">\
            <div class="card">\
                <img src="<%- properties.address %>" style="width: 95px; height: 50px">\
                <div class="card-title">\
                    <%- properties.title %>\
                </div>\
            </div>\
        </div>\
    </button>'
);

for (var i = 0; i < data.length; i++) {
    targetElement.innerHTML += template(data[i])
}

var apiKey = secretToken;
var mapCenter = [55.715765, 37.551521708]

L.mapbox.accessToken = apiKey;

var map = L.mapbox.map('map', 'mapbox.dark', {
    zoomControl: true
}).setView([mapCenter[0], mapCenter[1]], 1.5);

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
    $("#marker_city").text(content);
    $("#marker_content").attr('src', city);
    $("#marker_content").attr('style', "width: 500px; height:400px");
});

$('.filt button').on('click', function () {
    var filter = $(this).data('filter');
    $(this).addClass('flagactive').siblings().removeClass('flagactive');
    markers.setFilter(function (f) {
        return (filter === 'all') ? true : f.properties.title === filter;
    });
    return false;
});

