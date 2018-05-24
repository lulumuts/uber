
function our_layers(map.options){
  var datasets = new L.GeoJSON.AJAX("{% url 'driver:map_view' %}"
        )};
      datasets.addTo(map);
      }
