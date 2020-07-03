pipeline {
    agent {
        docker { image 'zip:1' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python zip_job.py'
            }
        }
    }
}
