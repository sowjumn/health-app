docker build -t gcr.io/kubernetes-161617/neighborshamer_web ../.
gcloud docker -- push gcr.io/kubernetes-161617/neighborshamer_web
kubectl delete deployment web-frontend
kubectl delete service web-frontend
kubectl create -f k8-web.yaml
kubectl expose deployment web-frontend --type=NodePort
minikube service web-frontend
