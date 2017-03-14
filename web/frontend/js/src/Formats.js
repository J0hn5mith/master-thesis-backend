var formater = {
  date: function(date){
    var d = new Date(date);
    var curr_date = d.getDate();
    var curr_month = d.getMonth() + 1; //Months are zero based
    var curr_year = d.getFullYear();
    var curr_hour = d.getUTCHours();
    var curr_min = d.getUTCMinutes();
    var curr_sec = d.getUTCSeconds();
    return(curr_hour + ":" + curr_min + ":" + curr_sec + " " + curr_date + "." + curr_month + "." + curr_year);
  },
  coordinates: function(coordinates){
    return coordinates.lat.toFixed(5)+ " | " + coordinates.lng.toFixed(5);
  },
}

export default formater;
