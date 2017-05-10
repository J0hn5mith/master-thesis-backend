//process.env.FRONTEND_SETTINGS
var Settings = {
  STATIC_FILE_URL: process.env.FRONTEND_URL,
  IMAGE_URL: process.env.FRONTEND_URL + 'img/',
  TILE_SET_URL: process.env.TILE_SET_URL,
};

export default Settings;
