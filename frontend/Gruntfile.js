module.exports = function (grunt) {
    grunt.initConfig({
        bower: {
            install: {
                options: {
                    targetDir: './bower_components'
                }
            }
        }
    });

    grunt.registerTask('default', ['bower']);
    grunt.loadNpmTasks('grunt-bower-task');
};