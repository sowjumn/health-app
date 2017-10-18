read -p "Enter docker image tag: " text
docker build -t gcr.io/kubernetes-161617/neighborshamer_web:$text ../.
gcloud docker -- push gcr.io/kubernetes-161617/neighborshamer_web:$text
kubectl set image --filename=k8-web.yaml ns-web=gcr.io/kubernetes-161617/neighborshamer_web:$text
minikube service web-frontend
