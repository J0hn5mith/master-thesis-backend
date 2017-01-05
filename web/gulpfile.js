//https://www.sitepoint.com/simple-gulpy-workflow-sass/
var gulp = require('gulp');
var sass = require('gulp-sass');
var webpack = require('webpack-stream');
var useref = require('gulp-useref');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;

var input_css = './frontend/css/**/*.scss';
var output_css = './static/css';

var input_js = './frontend/js/main.js';
var input_folder_js = './frontend/js/*';
var output_js = './static/js/';

var input_html = '**/templates/**/*.html';


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
    return gulp.src(input_html).pipe(browserSync.reload({
        stream: true
    }))
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
});

gulp.task('useref', function(){
    return gulp.src('templates/*.html')
        .pipe(useref())
        .pipe(gulp.dest('static/'))
});

gulp.task('browserSync', ['runserver'], function() {
    browserSync.init({
        notify: false,
        port: 8000,
        proxy: 'localhost:8000'
    })
});

gulp.task('runserver', function() {
    var proc = exec('python manage.py runserver');
});
