const template = UnderscoreTemplate(
    '<a href="#" data-filter="<%-properties.name%>" style="color:#93a647;"><span class="fa fa-check-circle fa-lg"></span> Plot Match</a>\
     <li class="game game-top winner"><%-properties.home_team%> <span><%-properties.home_result%></span></li>\
     <li class="game game-spacer">&nbsp;</li>\
     <li class="game game-bottom "><%-properties.away_team%> <span><%-properties.away_result%></span></li>\
     <li class="spacer">&nbsp;</li>'
);

var round_16 = data.filter((data) => data.properties.round === 'round_16');
const targetElement_16 = document.getElementById('round-16');
for (var i = 0; i < round_16.length; i++) {
    targetElement_16.innerHTML += template(round_16[i]);
}


var round_8 = data.filter((data) => data.properties.round === 'round_8');
const targetElement_8 = document.getElementById('round-8');
for (var i = 0; i < round_8.length; i++) {
    targetElement_8.innerHTML += template(round_8[i]);
}


var round_4 = data.filter((data) => data.properties.round === 'round_4');
const targetElement_4 = document.getElementById('round-4');
for (var i = 0; i < round_4.length; i++) {
    targetElement_4.innerHTML += template(round_4[i]);
}

var round_2 = data.filter((data) => data.properties.round === 'round_2');
const targetElement_2 = document.getElementById('round-2');
for (var i = 0; i < round_2.length; i++) {
    targetElement_2.innerHTML += template(round_2[i]);
}

const winner_template = UnderscoreTemplate(
    '<li class="game game-top winner"><%-properties.winner%> <span class="fa fa-trophy fa-lg">winner</span></li>\
     <li class="spacer">&nbsp;</li>'
);
const targetElement_winner = document.getElementById('winner')
targetElement_winner.innerHTML += winner_template(round_2[0])

var apiKey = secretToken;
var mapCenter = [55.715765, 37.551521708]

L.mapbox.accessToken = apiKey;

var map = L.mapbox.map('map', 'mapbox.dark', {
    zoomControl: true
}).setView([mapCenter[0], mapCenter[1]], 4);


var match_id = ""
var markers = L.mapbox.featureLayer().addTo(map);
markers.setGeoJSON(data);

var commentTemplate = UnderscoreTemplate(
    '<div class="col-sm-12 mt-4 comments">\
        <p><%-info%></p>\
        ---<%-user_name%>&nbsp;&nbsp;<%-date%>\
    </div>'
)


markers.on('click', function (e) {
    e.layer.closePopup();

    var feature = e.layer.feature;
    var match = feature.properties.name;
    var teams = feature.properties.home_team + " vs " + feature.properties.away_team + "( match no. " + match + ")";
    var home_flag = feature.properties.home_flag;
    var away_flag = feature.properties.away_flag;
    var home_score = feature.properties.home_result;
    var away_score = feature.properties.away_result;
    var channels = feature.properties.channels;
    var stadium = feature.properties.stadium;
    var round = feature.properties.round;


    var targetDiv = document.getElementById("comments");
    targetDiv.innerHTML = "";
    $.get('/comments?', { match: match }, function (data) {
        for (var i = 0; i < data.length; i++) {
            data[i].date = new Date(data[i].date).toLocaleString();
            targetDiv.innerHTML = commentTemplate(data[i]) + targetDiv.innerHTML;
        }
    });
    match_id = parseInt(match);

    if (round === "round_16") {
        round = "Round of 16";
    }
    else if (round === "round_8") {
        round = "Quarter-Final";
    }
    else if (round === "round_4") {
        round = "Semi-Final";
    }
    else if (round === "round_2" || round === "round_2_loser") {
        round = "Final";
    }
    else {
        round = "Group Stage "
    }

    $("#marker_title").text(teams);
    $("#round").text(round)
    $("#home_flag").attr("src", home_flag);
    $("#away_flag").attr("src", away_flag);
    $("#stadium").text(stadium)
    $("#score").text(feature.properties.home_team + " - " + home_score + "    |    " + feature.properties.away_team + " - " + away_score);
    const card_template = UnderscoreTemplate(
        '<div class="col-sm-3 center" style="margin:15px">\
            <div class="card">\
                <img src="<%- icon %>" style="width: 95px; height: 50px">\
                <div class="card-title">\
                  <h4 class="mt-2">  <%- name %></h4>\
                </div>\
            </div>\
        </div>'
    );
    var target = document.getElementById("channelcards");
    target.innerHTML = "";
    for (var i = 0; i < channels.length; i++) {
        channel = {
            name: channels[i][0],
            icon: channels[i][1]
        }
        target.innerHTML += card_template(channel);
    }
    $('#exampleModal').modal('show');
});

$('.filt button').on('click', function () {
    var filter = $(this).data('filter');
    $(this).addClass('active').siblings().removeClass('active');
    markers.setFilter(function (f) {
        return (filter === 'all') ? true : f.properties.round === filter;
    });
    return false;
});

$('.tournament a').on('click', function () {
    var filter = $(this).data('filter');
    markers.setFilter(function (f) {
        return (filter === 'all') ? true : f.properties.name === filter;
    });
    return false;
});


$('#form').submit(function (e) {
    var targetDiv = document.getElementById("comments");
    $.post('/matches/', $(this).serialize() + "&match=" + match_id, function (data) {
        data.date = new Date(data.date).toLocaleString();
        targetDiv.innerHTML = commentTemplate(data) + targetDiv.innerHTML;
    });
    document.getElementById("form").reset();
    e.preventDefault();
});