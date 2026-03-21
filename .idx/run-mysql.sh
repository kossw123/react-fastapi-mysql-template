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