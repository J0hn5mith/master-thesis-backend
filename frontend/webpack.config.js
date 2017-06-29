var path = require('path');
var webpack = require('webpack');
const DotenvPlugin = require('webpack-dotenv-plugin');

const ENV_FILE = '../' + process.env['ENV_FILE'];



module.exports = {
  entry: "./src/js/main.js",
  output: {
    path: __dirname,
    filename: "./bundle.js",
  },
  plugins: [
        new DotenvPlugin({
            sample: ENV_FILE,
            path: ENV_FILE,
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
