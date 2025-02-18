pipeline {
    agent any
    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch to build and deploy')
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: 'Select environment to deploy to')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests before deployment')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'echo Building...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'echo Deploying...'
            }
        }
    }
}
