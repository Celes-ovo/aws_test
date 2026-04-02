from base import *

# EC2 초반 테스트를 위해 True로 설정
DEBUG = True

# EC2의 public ip
ALLOWED_HOSTS = [
    '44.203.17.126',
]

STATIC_URL = 'static/'

# EC2에서는 static 파일을 따로 관리함
# 따라서 본래는 STATIC_ROOT를 써야 하지만 마찬가지로 테스트를 위해 STATICFILES_DIRS 사용
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [BASE_DIR / 'static',]