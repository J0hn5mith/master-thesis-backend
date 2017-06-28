var path = require('path');
var webpack = require('webpack');
const Dotenv = require('dotenv-webpack');



module.exports = {
  entry: "./src/js/main.js",
  output: {
    path: __dirname,
    filename: "./bundle.js",
  },
  plugins: [
    new webpack.EnvironmentPlugin({
      FRONTEND_SETTINGS: 'local',
      FRONTEND_SETTINGS: 'local',
      //FRONTEND_URL: 'http://localhost:8001/',
      FRONTEND_URL: 'https://staging.jan-meier.me/frontend/',
      STATIC_FILE_PREFIX: 'static/',
      TILE_SET_URL: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      DEBUG: true,
    })
  ],
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        enforce: 'pre',
        loader: 'eslint-loader',
        options: {
          emitWarning: true,
        },
      },
      {
        test: path.join(__dirname, 'src/js/**/*.js'),
        loader: 'babel-loader',
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ],
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.common.js'
    }
  },
  devtool: '#eval-source-map',
};
process.traceDeprecation = true;
