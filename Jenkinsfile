pipeline {
    agent {
    // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
    dockerfile {
        filename 'Dockerfile'
        }
    }    
    stages {
        stage('Build') {
            steps { 
                sh "python3 /tmp/zip_job.py"
                sh "ls -l"
            }
        }
        stage('Publish') {
            steps {   
               sh 'curl -fL https://getcli.jfrog.io | sh'  
               sh 'jfrog rt c rt-server-1 --url=http://localhost:8081/artifactory/binary-storage --user=super-user --password=Qw12856!'
               sh 'jfrog rt u "(*).zip" binary-storage/{1}/ --recursive=false'
            }
        }
    }
}
