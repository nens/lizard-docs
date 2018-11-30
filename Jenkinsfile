node() {
    stage('Checkout') {
        checkout scm
    }
    stage('Build') {
        sh "docker-compose down --volumes --remove-orphans"
        sh "docker-compose build"
        sh "docker-compose run builder"
    }
    stage('Cleanup') {
        sh "docker-compose down --volumes"
    }
}
