import Settings from '../settings.js';

var StaticFile = function(value){
  var url = Settings.STATIC_FILE_URL + value;
  return url;
};

export default StaticFile ;
