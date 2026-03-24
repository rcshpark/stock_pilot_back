# stock_pilot_back

`pipenv` 기반 Django 백엔드 개발 프로젝트입니다.

`pipenv`가 PATH에 없다면 아래를 먼저 실행하면 됩니다.

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

## 설치

```bash
pipenv install
```

## 실행


```bash
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```

기본 실행은 `config.settings.local`을 사용합니다.

운영 설정으로 실행하려면 다음과 같이 `DJANGO_SETTINGS_MODULE`을 지정합니다.

```bash
pipenv run python manage.py runserver --settings=config.settings.prod
```

## 환경 변수

루트의 `.env` 파일을 사용합니다. 시작할 때는 `.env.example`을 복사해서 쓰면 됩니다.

## 디렉터리 구조

- `apps/`: Django 앱 모음
- `config/`: Django 설정, URL, WSGI/ASGI

## 기본 엔드포인트

- `GET /api/health/`
- `GET /admin/`

## 개발 패키지

- `django`
- `djangorestframework`
- `django-cors-headers`
- `python-dotenv`
