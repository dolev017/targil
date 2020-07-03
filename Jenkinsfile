pipeline {
    agent {
        docker {
            image 'zip:1'
            args '-v /home/dolev/.m2:/root/.m2'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python zip_job.py'
            }
        }
    }
}
