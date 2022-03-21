const finish_button = document.getElementById("complete");
finish_button.disabled = true;
const area_span = document.getElementById("the_area");

const source = new ol.source.Vector({wrapX: false});

const raster = new ol.layer.Tile({
    source: new ol.source.OSM(),
});

const vector = new ol.layer.Vector({
    source: source,
});

let current_projection = raster.getSource().getProjection();
let new_projection = new ol.proj.Projection({code: "EPSG:4326"});

const map = new ol.Map({
    layers: [raster, vector],
    target: 'map',
    view: new ol.View({
        center: [-11000000, 4600000],
        zoom: 4,
    }),
});

let draw = new ol.interaction.Draw({
    source: source,
    type: "Polygon",
});
map.addInteraction(draw);

document.getElementById('undo').addEventListener('click', function () {
    draw.removeLastPoint();
});

document.getElementById('clear').addEventListener('click', function () {
    let features = vector.getSource().getFeatures();
    features.forEach((feature) => {
        vector.getSource().removeFeature(feature);
    });
    finish_button.classList.remove("btn-success");
    finish_button.classList.add("btn-outline-success");
    finish_button.disabled = true;

    area_span.textContent = "-";
});

let coordinates;
let area;

document.getElementById('complete').addEventListener('click', function () {
    finish_button.classList.remove("btn-success");
    finish_button.classList.add("btn-outline-success");
    finish_button.disabled = true;

    $.post("/api/pin_field", {
        field_coordinates: JSON.stringify(coordinates),
        field_area: area
    });
});

source.on('addfeature', function(evt) {
    let this_feature = evt.feature;
    let features = vector.getSource().getFeatures();

    const raw_coordinates = this_feature.getGeometry().getCoordinates();
    const this_polygon = new ol.geom.Polygon(raw_coordinates);

    area = Math.round(this_polygon.getArea() * 10) / 10;
    coordinates = this_polygon.transform(current_projection, new_projection).getCoordinates();

    finish_button.classList.remove("btn-outline-success");
    finish_button.classList.add("btn-success");
    finish_button.disabled = false;
    area_span.textContent = area.toString();

    features.forEach((feature) => {
        if (feature !== this_feature) {
            vector.getSource().removeFeature(feature);
        }
    });
});
