const raster = new ol.layer.Tile({
  source: new ol.source.OSM(),
});

const source = new ol.source.Vector({wrapX: false});

const vector = new ol.layer.Vector({
  source: source,
});

const map = new ol.Map({
  layers: [raster, vector],
  target: 'map',
  view: new ol.View({
    center: [-11000000, 4600000],
    zoom: 4,
  }),
});

const typeSelect = "Polygon";

let draw; // global so we can remove it later
function addInteraction() {
    draw = new ol.interaction.Draw({
      source: source,
      type: typeSelect,
    });
    map.addInteraction(draw);
}

document.getElementById('undo').addEventListener('click', function () {
  draw.removeLastPoint();
});

addInteraction();