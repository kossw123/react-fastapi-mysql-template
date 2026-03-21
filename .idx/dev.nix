  { pkgs, ... }: {

    channel = "stable-24.05";

    packages = [
      pkgs.nodejs_22
      pkgs.python311
      pkgs.mysql80
      pkgs.git
    ];
    idx = {

      extensions = [
        "ms-python.python"
        "ms-python.vscode-pylance"
      ];
      workspace = {
        onStart = {
          # 가상환경 없이 설치하려고 했으나, IDX 자체에서 전역 환경은 read-only이기 때문에
          # 설치하지 못하게끔 한다.
          # 그렇기 때문에 가상환경을 생성하여 설치한다.
          server-python-env = ''
            echo "Creating Python virtual environment..."
            cd server
            
            if [ ! -d ".venv" ]; then
              python -m venv .venv
            fi
            
            echo "Activating venv and installing requirements..."
            source .venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
          '';

          client-node-env = ''
            echo "Installing frontend dependencies..."
            cd client
            npm install
            npm install axios
          '';
          run-mysql = ''
            echo "🚀 setup-mysql 시작"

            # MySQL 설치 확인
            if mysql --version >/dev/null 2>&1 || mysqld --version >/dev/null 2>&1; then
            echo "✅ MySQL 설치 확인됨"

            # run-mysql.sh 생성
            mkdir -p $HOME/.idx

            cat << 'EOF' > $HOME/.idx/run-mysql.sh
            #!/usr/bin/env bash

            set -e

            echo "🚀 MySQL 설정 시작"

            DATA_DIR="$HOME/mysql-data"

            # 1. 데이터 디렉토리 생성
            mkdir -p "$DATA_DIR"

            # 2. 초기화 (이미 초기화 되어있으면 스킵)
            if [ ! -d "$DATA_DIR/mysql" ]; then
            echo "📦 MySQL 초기화"
            mysqld --initialize-insecure --datadir="$DATA_DIR"
            else
            echo "📦 이미 초기화됨"
            fi

            # 3. MySQL 서버 실행 (백그라운드)
            echo "🚀 MySQL 서버 실행"
            mysqld \
                --datadir="$DATA_DIR" \
                --socket="$DATA_DIR/mysql.sock" \
                --port=3306 \
                --bind-address=127.0.0.1 &

            sleep 5

            # 4. root 접속 및 DB/유저 생성
            echo "🔐 DB 및 사용자 생성"

            mysql -u root -h 127.0.0.1 <<SQL
            CREATE DATABASE IF NOT EXISTS testdb;
            CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'password';
            GRANT ALL PRIVILEGES ON testdb.* TO 'user'@'localhost';
            FLUSH PRIVILEGES;
            SQL

            # 5. 접속 확인
            echo "🔍 접속 테스트"
            mysql -u root -h 127.0.0.1 testdb -e "SHOW TABLES;"

            echo "🎉 Complete create to user, password, db"
            EOF

            # 권한 부여
            chmod +x $HOME/.idx/run-mysql.sh

            # 실행
            sh $HOME/.idx/run-mysql.sh

            else
            echo "❌ expected to Not installed 'mysql --version' is not messaged"
            fi
          '';
        };
      };


      previews = {
        enable = true;
        previews = {
          web = {
            command = ["bash" "-c" "cd client && npm install && npm run dev -- --port $PORT --host 0.0.0.0"];
            manager = "web";
          };
        };
      };
    };
  }