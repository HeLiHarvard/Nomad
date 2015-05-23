$(document).ready(function() {
  var max_locations = 10,
          locations = 2,
         date_field = $(".datepicker"),
         inputs_div = $("#home-dest-inputs"),
         add_button = $("#new-location-button");
         //bg_pics    = ['island_boat.jpg', 'korcula.jpg', 'paris.jpg', 'rome.jpg', 'shanghai.jpg', 'skye.jpg'],
         //bg_pic_chosen  = bg_pics[Math.floor(Math.random()*5)];

  $(".datepicker").datepicker();
  //$(".full-bg-image").css("background", "../img/"+bg_pic_chosen);
  //alert($(".full-bg-image").css("background"));

  $("#new-location-button").click(function(e) {
    e.preventDefault();
    if(locations < max_locations) {
      locations++;

      var date_name = "dates-"+(locations-2),
      new_date = '<td class="home-search-cell">Departure date:<br><input id='+date_name+' name='+date_name+' size="25" type="text" value class="datepicker"></td>';
      $(".row-"+(locations-2)).append(new_date);
      $(".datepicker").datepicker();

      var place_name = "places-"+(locations-1),
      new_dest = '<tr class="row-'+(locations-1)+'"><td class="home-search-cell">Next destination:<br><input id='+place_name+' name='+place_name+' size="45" type="text" value></td></tr>';
      $(inputs_div).append(new_dest);
    }
  });
});
