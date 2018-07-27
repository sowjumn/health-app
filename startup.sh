heroku ps:scale web=1 -a health-demo-staging
heroku ps:scale web=1 -a health-demo-fr
heroku ps:scale web=1 -a health-demo-or
heroku ps:scale web=1 -a health-demo-to
heroku ps:scale web=1 -a health-demo-ms-public
heroku ps:scale worker=1 -a health-demo-ms-private

