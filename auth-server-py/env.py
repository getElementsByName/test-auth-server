import os

ENV_JWT_HMAC_SECRET = os.environ.get("JWT_HMAC_SECRET", "")
ENV_ENVOY_RATELIMIT_HTTP_URL = os.environ.get("ENVOY_RATELIMIT_HTTP_URL", "")