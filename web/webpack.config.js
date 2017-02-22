module = {
  loaders: [
    {
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel-loader',
      babelrc: false,
      query: {
        presets: ['es2015']
      }
    }
  ],
  exports: {
    context: __dirname + "/frontend/js/src/",
    entry: "./main.js",
    output: {
      path: __dirname + "/frontend/js/",
      filename: "./bundle.js"
    }
  }
}

//module.loaders = [
//{
//test: /\.js$/,
//exclude: /(node_modules|bower_components)/,
//loader: 'babel-loader',
//query: {
//presets: ['es2015']
//}
//}
//]
//module.exports = {
//context: __dirname + "/frontend/js/src/",
//entry: "./main.js",
//output: {
//path: __dirname + "/frontend/js/",
//filename: "./bundle.js"
//}
//}
