pipeline  {
  agent any

  stages {
    stage('Build'){
      steps{
        git clone https://github.com/baburinsy/sql-pipe.git /tmp/test
        python3 /tmp/test/sql1/sql1.py > /tmp/sql1.log
      }
    }
  }
}
