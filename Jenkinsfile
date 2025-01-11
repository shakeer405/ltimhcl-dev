pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo Building App on Staging Environment...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo Running tests...on Staging Environment'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo Deploying...on Staging Environment'
            }
        }
    }
}
