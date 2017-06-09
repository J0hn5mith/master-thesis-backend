/*
 * A file to collect the code for Vue.js filters which is used multiple times.
 */
import Settings from '../settings.js';

var StaticFile = function(value){
  var url = Settings.STATIC_FILE_URL + value;
  return url;
};

export default StaticFile ;
