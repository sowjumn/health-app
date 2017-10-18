kubectl delete deployment redis
kubectl delete service redis-service
kubectl create -f k8-redis.yaml
minikube service web-frontend