pipeline {
    dockerNode(dockerHost: 'tcp://127.0.0.1:2376', image: 'zip:1', remoteFs: '/home/dolev/workspace') {
    stages {
        stage('build') {
            steps {
                sh 'python /tmp/zip_job.py'
            }
        }
        stage('Push') {
            steps {
		def version = sh(script: 'echo $VERSION', returnStdout: true)
                rtUpload (
                	serverId: 'Artifactory',
       			spec: '''{
                		"files": [
            				{	
              					"pattern": "*.zip",
              					"target": "binary-storage/${version}"
            				}
         			]
    			}''',
		)
            }
        }
	stage('Send Mail') {
	  steps {
		mail bcc: '' , body: '' , cc: '' , from: '' , replyTo: '' , subject: 'test', to: 'dolevm017@gmail.com'
	  }
	}
        stage('Clean') {
            steps {
                sh 'rm -rf /home/dolev/workspace/*'
            }
        }
    }
  }
}
