  { pkgs, ... }: {

    channel = "stable-24.05";

    packages = [
      pkgs.nodejs_22
      pkgs.python311
      pkgs.git
      pkgs.mysql80
      pkgs.direnv
    ];

    idx = {

      extensions = [
        "ms-python.python"
        "ms-python.vscode-pylance"
      ];

      workspace = {
        onCreate = {
          # 가상환경 없이 설치하려고 했으나, IDX 자체에서 전역 환경은 read-only이기 때문에
          # 그렇기 때문에 가상환경을 생성하여 설치한다.
          # 설치하지 못하게끔 한다.
          python-env = ''
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

          node-env = ''
            echo "Installing frontend dependencies..."
            cd client
            npm install
            npm install axios
          '';
        };
      };

    };

  }