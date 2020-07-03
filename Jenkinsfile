pipeline {
    agent {
        docker { image 'zip:1' }
    }
    stages {
        stage('Test') {
            steps {
                sh './zip_job.py'
            }
        }
    }
}


