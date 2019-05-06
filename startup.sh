heroku ps:scale web=2 -a health-demo-staging
heroku ps:scale web=2 -a health-demo-fr
heroku ps:scale web=2 -a health-demo-or
heroku ps:scale web=2 -a health-demo-to
heroku ps:scale web=2 -a health-demo-risk-staging
heroku ps:scale web=2 -a health-demo-risk-internal
aws ec2 start-instances --instance-ids i-04dcff2a02c5c1ca5 --region us-west-2
gcloud compute instances start instance-1 --project byrum-heroku-vpn --zone europe-west3-c
echo ""
echo "*** Sleeping for 2 minutes to ensure GCP instance is alive ***"
sleep 120

echo ""
echo "*** Starting docker container on GCP instance.  You will have to supply passsword: ***"
gcloud compute ssh jbyrum@instance-1 --command='. docker-start-app.sh' --project byrum-heroku-vpn --zone europe-west3-c

