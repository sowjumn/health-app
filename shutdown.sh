heroku ps:scale web=0 -a health-demo-staging
heroku ps:scale web=0 -a health-demo-fr
heroku ps:scale web=0 -a health-demo-or
heroku ps:scale web=0 -a health-demo-to
heroku ps:scale web=0 -a health-demo-risk-staging
heroku ps:scale web=0 -a health-demo-risk-internal
aws ec2 stop-instances --instance-ids i-04dcff2a02c5c1ca5 --region us-west-2
gcloud compute instances stop instance-1 --project byrum-heroku-vpn --zone europe-west3-c
