$env:GEMINI_API_KEY = ""
echo $env:GEMINI_API_KEY

#for jwt.io
{
  "sub": "arnab",
  "name": "Arnab",
  "iat": 1516239022
}

#curl commands
curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Tell me about persian cats"
}'

curl -X POST \
  'http://127.0.0.1:8000/chat' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhcm5hYiIsIm5hbWUiOiJBcm5hYiIsImlhdCI6MTUxNjIzOTAyMn0.Z_QQdjVfjfZ3cu5VaOkKxcnm0uYEskmNgjykJx7QPu0' \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "Why are cats cute?"}'