//https://www.sitepoint.com/simple-gulpy-workflow-sass/

var gulp = require('gulp');
var sass = require('gulp-sass');
var webpack = require('webpack');
var gulpWebpack = require('webpack-stream');
var useref = require('gulp-useref');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;
var child_process = require('child_process');

var uglify = require('gulp-uglify');
var usemin = require('gulp-usemin');
var minifyCss = require('gulp-minify-css');
var rimraf = require('gulp-rimraf');
var clean = require('gulp-clean');
var runSequence = require('run-sequence');
//var notify = require("gulp-notify");

var input_css = './frontend/css/**/*.scss';
var output_css = './static/css';

var input_js = './frontend/js/main.js';
var input_folder_js = './frontend/**/*.+(js|vue|html)';
var output_js = './static/js/';

var input_html = '**/templates/**/*.html';

var input_libs = './templates/partials/*.html';
var libs_output = './static/';
var fonts_input = './node_modules/bootstrap/fonts/*'
var fonts_output = './static/fonts/'
var img_input = ['./node_modules/leaflet/dist/images/*',]
var img_output = './static/img/'



function swallowError(error) {
  console.log(error.toString());
  this.emit('end');
}

gulp.task('sass', function() {
  return gulp
    .src(input_css)
    .pipe(sass())
    .on('error', swallowError)
    .pipe(gulp.dest(output_css))
    .pipe(browserSync.reload({
      stream: true
    }))
});

gulp.task('html', function() {
  gulp.src(input_html).pipe(browserSync.reload({
    stream: true
  }))
});

gulp.task('libs',  function(callback){
  runSequence('libs-compile',  'copy-fonts', 'copy-img', 'libs-clean', callback);
});

gulp.task('libs-compile', function() {
  return gulp.src('templates/partials/*.html')
    .pipe(usemin({
      assetsDir: './',
      js: [uglify(), 'concat'],
      css: [minifyCss(), 'concat'],
    }))
    .pipe(gulp.dest(libs_output))
    .pipe(browserSync.reload({
      stream: true
    }));
});

gulp.task('copy-fonts', function() {
  return gulp.src(fonts_input).pipe(gulp.dest(fonts_output));
});

gulp.task('copy-img', function() {
  return gulp.src(img_input).pipe(gulp.dest(img_output));
});

gulp.task('libs-clean', function() {
  var generated = ['./static/*.html'];
  return gulp.src(generated)
    .pipe(clean());
});

gulp.task('webpack', function() {
  return gulp.src(input_js)
    .pipe(gulpWebpack(require('./webpack.config.js'), webpack))
    .on('error', swallowError)
    .pipe(gulp.dest(output_js))
    .pipe(browserSync.reload({ stream: true }))
});

gulp.task('watch', ['browserSync'], function() {
  gulp.watch(input_folder_js, ['webpack'])
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
  gulp.watch(input_css, ['sass'])
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
  gulp.watch(input_html, ['html'])
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
  gulp.watch(input_libs, ['libs'])
    .on('change', function(event) {
      console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
    });
});

gulp.task('browserSync', [], function() {
  return browserSync.init({
    notify: true,
    port: 8000,
    proxy: 'localhost:8000'
  })
});

gulp.task('runserver', function(cb) {
  var cons = console;
  ls = child_process.exec('./manage.py runserver -v 3 --no-color', function (error, stdout, stderr) {
    if (error) {
      console.log(error.stack);
      console.log('Error code: '+error.code);
      console.log('Signal received: '+error.signal);
    }
    console.log('Child Process STDOUT: '+stdout);
    console.log('Child Process STDERR: '+stderr);
  });
});

gulp.task('clean',['libs-clean'], function() {
  var generated = ['static/js/libs.js', 'static/css/libs.css'];
  return gulp.src(generated)
    .pipe(rimraf());
});

