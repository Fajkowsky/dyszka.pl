module.exports = function (grunt) {
    grunt.initConfig({
        bower: {
            install: {
                options: {
                    targetDir: './bower_components'
                }
            }
        },
		shell: {
			install_backend: {
				command: 'pip install -r ../backend/requirements.txt'
			},
			run_backend: {
				command: 'python ../backend/manage.py runserver'
			}
		}
    });

    grunt.registerTask('default', ['bower']);

	grunt.registerTask('install_backend', ['shell:install_backend']);
	grunt.registerTask('run_backend', ['shell:run_backend']);

    grunt.loadNpmTasks('grunt-bower-task');
	grunt.loadNpmTasks('grunt-shell');
};