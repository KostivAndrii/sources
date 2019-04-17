import groovy.json.JsonSlurper
    def response = httpRequest customHeaders: [[name: 'X-JFrog-Art-Api', value: 'AKCp5ccGXKgp571DUjg7FfjTru6n8DyEygjrGCkV5JHgjwBYYnzsyRPFuu8g5v244TdnoXbS4'],[name: 'content-type', value: 'text/plain']], httpMode: 'POST', requestBody: 'items.find({"repo":{"$match":"libs-*-local"},"path":{"$match":"com/geekcap/vmturbo/hello-world-servlet-example/*"},"name":{"$match":"*.war"}}).include("repo","name","path")', responseHandle: 'LEAVE_OPEN', url: 'http://artifactory:8081/artifactory/api/search/aql'
    def json = new JsonSlurper().parseText(response.content).results.name

pipeline {
    agent any
    parameters {
        choice(choices: json, description: 'Choise artifact', name: 'release')
    }
    stages {
        stage ('Examle') {
            steps {
                echo 'Hello, AWS'
                echo "Trying: ${params.release}"
                sh 'pwd'
                sh 'printenv | sort'
                sh 'sh ./get_target.sh ${release}'
             }
        }
    }
}
