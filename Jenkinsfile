pipeline  {
  agent any

  stages {
    stage('Build'){
      steps{
        sh "git clone https://github.com/baburinsy/sql-pipe.git /tmp/test"
        sh "python3 /tmp/test/sql1/sql1.py > /tmp/sql2.log"
      }
    }
  }
}
