var path = require('path');
module.exports = {
  entry: "./frontend/js/src/main.js",
  output: {
    path: __dirname,
    //filename: "./static/js/bundle.js"
    filename: "./bundle.js"
  },
  module: {
    loaders: [
      {
        test: path.join(__dirname, 'frontend/js/src'),
        loader: 'babel-loader',
      }
    ]
  }
};
