import env
import requests

# http://localhost:8080/json
# {
#   "domain": "rl",
#   "descriptors": [
#     { "entries": [{ "key": "foo"}, { "key": "bar", "value": "bar" }] }
#   ]
# }

if __name__ == '__main__':
  ratelimit_body = {
    "domain": "rl",
    "descriptors": [
      { "entries": [{ "key": "foo"}, { "key": "bar", "value": "bar" }] }
    ]
  }
response = requests.post(env.ENV_ENVOY_RATELIMIT_HTTP_URL, json=ratelimit_body)
status_code = response.status_code
body = response.text
is_over_limit = (status_code == 429)
print(is_over_limit)
print(status_code)
print(body)
