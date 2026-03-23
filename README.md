# stock_pilot_back

`pipenv` 기반 Django 백엔드 개발 프로젝트입니다.

`pipenv`가 PATH에 없다면 아래를 먼저 실행하면 됩니다.

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

## 실행

```bash
cd stock_pilot_back
PIPENV_VENV_IN_PROJECT=1 pipenv install
PIPENV_VENV_IN_PROJECT=1 pipenv run python manage.py migrate
PIPENV_VENV_IN_PROJECT=1 pipenv run python manage.py runserver
```

## 기본 엔드포인트

- `GET /api/health/`
- `GET /admin/`

## 개발 패키지

- `django`
- `djangorestframework`
- `django-cors-headers`
- `python-dotenv`
