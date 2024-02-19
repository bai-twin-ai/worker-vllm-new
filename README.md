# runpod vllm worker


### Optional - build base image locally
```shell
docker build -t ehartford/runpod-worker-vllm:latest .
```

### Bake model into image

```shell
docker build -t ehartford/runpod-worker-vllm:ondemand --build-arg MODEL_NAME="cognitivecomputations/dolphin-2.6-mixtral-8x7b" --build-arg MODEL_BASE_PATH="/model/" -f Dockerfile-ondemand .
docker push ehartford/runpod-worker-vllm:ondemand
```
### Venus

```
docker build -t runpod-worker-vllm:ondemand -f Dockerfile-ondemand .
docker tag runpod-worker-vllm:ondemand europe-west6-docker.pkg.dev/aitesting-405910/ai-registry/runpod-worker-vllm:ondemand
docker push europe-west6-docker.pkg.dev/aitesting-405910/ai-registry/runpod-worker-vllm:ondemand
```
