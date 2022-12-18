// Initialize and add the map
function initMap() {
  // The location of the service
  const galaTech = { lat: 43.208555, lng: 27.968086 };
  // The map, centered at GalaTech
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: galaTech,
  });

  const marker = new google.maps.Marker({
    position: galaTech,
    map: map,
  });
}

window.initMap = initMap;