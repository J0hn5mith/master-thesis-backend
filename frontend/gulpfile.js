//https://www.sitepoint.com/simple-gulpy-workflow-sass/

var gulp = require('gulp');
var sass = require('gulp-sass');
var webpack = require('webpack');
var gulpWebpack = require('webpack-stream');
var useref = require('gulp-useref');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;
var child_process = require('child_process');
var jscs = require('gulp-jscs');

var uglify = require('gulp-uglify');
var usemin = require('gulp-usemin');
var minifyCss = require('gulp-minify-css');
var rimraf = require('gulp-rimraf');
var clean = require('gulp-clean');
var runSequence = require('run-sequence');
var serve = require('gulp-serve');

var input_css = './src/css/**/*.scss';
var output_css = './static/css';

var input_js = './src/js/main.js';
var input_folder_js = './src/**/*.+(js|vue|html)';
var output_js = './static/js/';

var input_img = './src/img/**/*';
var output_img = './static/img/';

var input_html = '**/templates/**/*.html';

var input_libs = './src/libs/*.html';
var libs_output = './static/';
var fonts_input = './node_modules/bootstrap/fonts/*';
var fonts_output = './static/fonts/';
var img_input = ['./node_modules/leaflet/dist/images/*',];
var img_output = './static/img/';



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
        }));
});

gulp.task('html', function() {
    gulp.src(input_html).pipe(browserSync.reload({
        stream: true
    }));
});

gulp.task('img', function() {
    return gulp.src(input_img)
        .pipe(gulp.dest(output_img))
        .pipe(browserSync.reload({
            stream: true
        }));
});

gulp.task('libs',  function(callback){
    runSequence('libs-compile',  'copy-fonts', 'copy-img', 'libs-clean', callback);
});

gulp.task('libs-compile', function() {
    return gulp.src('src/libs/css.html')
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
        .pipe(browserSync.reload({ stream: true }));
});

gulp.task('watch', ['browserSync', 'serve'], function() {
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
    gulp.watch(input_img, ['img'])
        .on('change', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
        });
    gulp.watch(input_libs, ['libs'])
        .on('change', function(event) {
            console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
        });
});

gulp.task('build', function(callback) {
    return runSequence('img',  'webpack', 'sass', 'libs');
});

gulp.task('browserSync', [], function() {
    return browserSync.init({
        notify: true,
        port: 8000,
        proxy: 'localhost:8000',
    });
});

gulp.task('clean',['libs-clean'], function() {
    var generated = ['static/js/libs.js', 'static/css/libs.css'];
    return gulp.src(generated)
        .pipe(rimraf());
});


gulp.task('serve', serve({
    root: ['static', ],
    port: 8001,
}));
