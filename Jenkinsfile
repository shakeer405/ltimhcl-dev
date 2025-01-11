pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo Building App on QA Environment...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo Running tests...on QA Environment'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo Deploying...on QA Environment'
            }
        }
    }
}
