# fastapi-playground
FastAPI를 사용한 API 서비스 개발을 위한 Playground입니다.
## 환경 설정

### 1. install [rye](https://github.com/mitsuhiko/rye)

[install documentation](https://rye-up.com/guide/installation/#installing-rye)

Linux
```bash
curl -sSf https://rye-up.com/get | bash
echo 'source "$HOME/.rye/env"' >> ~/.bashrc
source ~/.bashrc
```

Windows  
see [install documentation](https://rye-up.com/guide/installation/)


### 2. Create virtual environment

First, Please match the index url to the environment at hand to use torch.

```toml
# pyproject.toml
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn>=0.31.1",
    "requests>=2.32.3",
    ...
]
```

Second, create virtual environment.
```bash
rye sync
```

## Run code

(예시)API 서버는 다음과 같이 실행합니다.
```sh
rye run uvicorn app.server:app --host=127.0.0.1 --port=8000 --reload
```
