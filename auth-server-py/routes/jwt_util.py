# https://pyjwt.readthedocs.io/en/latest/
import jwt



jwt_algorithm_list = ["HS256", "HS384", "HS512"]
def decode_jwt(encoded_value: str, secret: str):
  jwt_decoded_value = jwt.decode(encoded_value, secret, algorithms=jwt_algorithm_list)
  return jwt_decoded_value


if __name__ == '__main__':
    # encoded = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    encoded_jwt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.5mhBHqs5_DTLdINd9p5m7ZJ6XD0Xc55kIaCRY5r6HRA'
    secret = 'test'
    
    print(decode_jwt(encoded_jwt, secret))