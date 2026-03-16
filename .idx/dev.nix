{ pkgs, ... }: {
  # 최신 패키지를 지원하는 채널 선택
  channel = "stable-24.05";

  packages = [
    # Node.js 설정 (Vite용)
    pkgs.nodejs_22

    # Python 설정 (FastAPI용)
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.virtualenv # 가상환경 권장
  ];

  # 환경 변수 설정 (필요 시)
  env = {};

    idx = {
    # 1. 확장 프로그램 설정
    extensions = [
      "ms-python.python"
      "ms-ceintl.vscode-language-pack-ko"
    ];

    workspace = {
      # 처음 생성될 때 (신규 생성 시에만 작동)
      onCreate = {
        npm-install = "cd client && npm install";
      };
      
      # 워크스페이스가 열릴 때마다 실행 (현재 환경 복구 및 자동화 핵심)
      onStart = {
        setup-python = ''
          cd server
          # 1. .venv 폴더가 없으면 생성
          if [ ! -d ".venv" ]; then
            python -m venv .venv
          fi
          # 2. 가상환경 활성화 및 패키지 설치
          source .venv/bin/activate
          pip install -r requirements.txt
        '';
      };
    };



    # 3. 프리뷰 설정 (쉼표 없이 공백으로 구분)
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "npm" "run" "dev" "--" "--port" "$PORT" "--host" "0.0.0.0" ];
          manager = "web";
        };
      };
    };
  };
}
