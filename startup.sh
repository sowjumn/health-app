heroku ps:scale web=1 -a health-demo-staging
heroku ps:scale web=3 -a health-demo-fr
heroku ps:scale worker=3 -a health-demo-fr
heroku ps:scale web=10 -a health-demo-many-dynos
heroku ps:scale worker=10 -a health-demo-many-dynos
heroku ps:scale web=3 -a health-demo-boot-timeout
heroku ps:scale worker=3 -a health-demo-boot-timeout
heroku ps:scale web=1 -a health-demo-or
heroku ps:scale web=1 -a health-demo-to
heroku ps:scale web=1 -a health-demo-risk-staging
heroku ps:scale web=3 -a health-demo-risk-internal
aws ec2 start-instances --instance-ids i-04dcff2a02c5c1ca5 --region us-west-2
gcloud compute instances start instance-1 --project byrum-heroku-vpn --zone europe-west3-c
echo "Remember to start the docker container on the gcloud instance"
