Run it with Uvicorn:

```bash
uvicorn backend.asgi:application --reload --host 0.0.0.0 --port 8000 
```

```sh
# To run in docker
bash scripts/docker_deploy.sh
```