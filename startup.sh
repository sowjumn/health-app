heroku ps:scale web=1 -a health-demo-staging
heroku ps:scale web=1 -a health-demo-fr
heroku ps:scale web=1 -a health-demo-or
heroku ps:scale web=1 -a health-demo-to
heroku ps:scale web=1 -a health-demo-ms-public
heroku ps:scale worker=1 -a health-demo-ms-private
aws ec2 start-instances --instance-ids i-04dcff2a02c5c1ca5 --region us-west-2
