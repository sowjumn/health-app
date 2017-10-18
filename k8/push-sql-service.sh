docker build -t gcr.io/kubernetes-161617/neighborshamer_sql ../sql/.
gcloud docker -- push gcr.io/kubernetes-161617/neighborshamer_sql
kubectl delete deployment postgres
kubectl delete service postgres-service
kubectl create -f k8-sql.yaml
minikube service web-frontend