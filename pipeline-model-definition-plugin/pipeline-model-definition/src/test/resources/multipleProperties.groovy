/*
 * The MIT License
 *
 * Copyright (c) 2016, CloudBees, Inc.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

pipeline {
    agent any
    parameters {
        booleanParam(defaultValue: true, description: '', name: 'flag')
        // TODO: Be prepared to change this to "stringParam" once we're on a new enough core.
        string(defaultValue: '', description: '', name: 'SOME_STRING')
    }
    triggers {
        // TODO: Add a second trigger. Needs to be one with a symbol, and "upstream" has issues due to Result.
        cron('@daily')
    }
    options {
        buildDiscarder(logRotator(numToKeepStr:'1'))
        disableConcurrentBuilds()
        skipDefaultCheckout()
        timeout(time: 5, unit: 'MINUTES')
    }
    stages {
        stage("foo") {
            steps {
                echo "hello"
                sh "test -f Jenkinsfile"
            }
        }
    }
}


