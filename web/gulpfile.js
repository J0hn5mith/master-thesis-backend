//https://www.sitepoint.com/simple-gulpy-workflow-sass/
var gulp = require('gulp');
var sass = require('gulp-sass');
var webpack = require('webpack-stream');
var useref = require('gulp-useref');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;

var uglify = require('gulp-uglify');
var usemin = require('gulp-usemin');
var minifyCss = require('gulp-minify-css');
var rimraf = require('gulp-rimraf');
var clean = require('gulp-clean');
var runSequence = require('run-sequence');

var input_css = './frontend/css/**/*.scss';
var output_css = './static/css';

var input_js = './frontend/js/main.js';
var input_folder_js = './frontend/js/*';
var output_js = './static/js/';

var input_html = '**/templates/**/*.html';

var input_libs = './templates/partials/*.html';
var libs_output = './static/';
var fonts_input = './node_modules/bootstrap/fonts/*'
var fonts_output = './static/fonts/'


function swallowError(error) {

    console.log(error.toString())

    this.emit('end')
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
    runSequence('libs-compile',  'coppy-fonts' ,'libs-clean', callback);
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

gulp.task('coppy-fonts', function() {
    return gulp.src(fonts_input).pipe(gulp.dest(fonts_output));
});

gulp.task('libs-clean', function() {
    var generated = ['./static/*.html'];
    return gulp.src(generated)
        .pipe(clean());
});

gulp.task('webpack', function() {
    return gulp.src(input_js)
        .pipe(webpack( require('./webpack.config.js')))
        .pipe(webpack({
            output: {
                filename: "main.js"
            }
        }))
    //.on('error', swallowError)
        .pipe(gulp.dest(output_js))
        .pipe(browserSync.reload({
            stream: true
        }))
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

gulp.task('browserSync', ['runserver'], function() {
    return browserSync.init({
        notify: false,
        port: 8000,
        proxy: 'localhost:8000'
    })
});

gulp.task('runserver', function() {
    var proc = exec('python manage.py runserver');
});

gulp.task('clean',['libs-clean'], function() {
    var generated = ['static/js/libs.js', 'static/css/libs.css'];
    return gulp.src(generated)
        .pipe(rimraf());
});
