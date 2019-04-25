def findAMIs() {
    return UUID.randomUUID().toString().split('-').join('\n')
}

node{
    def userInput = input(
        id: 'userInput', message: 'input parameters', parameters: [
            [
                $class: 'ChoiceParameterDefinition',
                name: 'ami',
                choices: findAMIs(),
                description: 'AMI',
            ],
        ]
    )

    echo ("Selected AMI :: "+userInput)
}



pipeline {

    environment {
        AGENT_INFO = ''
    }

    agent {
        docker {
            image 'alpine'
            reuseNode true
        }
    }

    stages {

        stage('Collect agent info'){
            steps {
                echo "Current agent  info: ${env.AGENT_INFO}"
                script {
                    def agentInfo = sh script:'uname -a', returnStdout: true
                    println "Agent info within script: ${agentInfo}"
                    AGENT_INFO = agentInfo.replace("/n", "")
                    env.AGENT_INFO = AGENT_INFO
                }
            }
        }

        stage("Print agent info"){
            steps {
                script {
                    echo "Collected agent info: ${AGENT_INFO}"
                    echo "Environment agent info: ${env.AGENT_INFO}"
                }
            }
        }
    }
}
