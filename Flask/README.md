# Flask API
Simple Web API using Flask and JWT authentication.

### HOW TO USE [DOCKER]

##### Params
- `name` container name
- `port` application port
- `mode` environment mode
  - (production/development[default])

```bash
# DEPLOY
chmod +x dockerize.sh
./dockerize.sh <name> <port> <optional:mode>

# EXAMPLE
./dockerize.sh webapp01 8080 production
```