
## Deploy to Cloud Run

See the [Cloud Run documentation](https://cloud.google.com/sql/docs/mysql/connect-run)
for more details on connecting a Cloud Run service to Cloud SQL.

1. Build the container image:

```sh
gcloud builds submit --tag gcr.io/<YOUR_PROJECT_ID>/run-mysql
```

eg.
```sh
gcloud builds submit --tag gcr.io/webhook1030/run-myapp2 ./src
```

2. Deploy the service to Cloud Run:

```sh
gcloud run deploy run-mysql --image gcr.io/<YOUR_PROJECT_ID>/run-mysql \
  --add-cloudsql-instances '<PROJECT-ID>:<INSTANCE-REGION>:<INSTANCE-NAME>' \
  --set-env-vars INSTANCE_UNIX_SOCKET='/cloudsql/<PROJECT-ID>:<INSTANCE-REGION>:<INSTANCE-NAME>' \
  --set-env-vars DB_USER='<YOUR_DB_USER_NAME>' \
  --set-env-vars DB_PASS='<YOUR_DB_PASSWORD>' \
  --set-env-vars DB_NAME='<YOUR_DB_NAME>'
```
eg.
```sh
gcloud run deploy run-myapp2 --image gcr.io/webhook1030/run-myapp2 \
  --add-cloudsql-instances webhook1030:us-central1:myinstance \
  --set-env-vars INSTANCE_UNIX_SOCKET='/cloudsql/webhook1030:us-central1:myinstance' \
  --set-env-vars DB_NAME="mydb" \
  --set-env-vars DB_USER="myuser" \
  --set-env-vars DB_PASS="Hangzhou123"
```

Take note of the URL output at the end of the deployment process.

Replace environment variables with the correct values for your Cloud SQL
instance configuration.

It is recommended to use the [Secret Manager integration](https://cloud.google.com/run/docs/configuring/secrets) for Cloud Run instead
of using environment variables for the SQL configuration. The service injects the SQL credentials from
Secret Manager at runtime via an environment variable.

Create secrets via the command line:
```sh
echo -n $INSTANCE_UNIX_SOCKET | \
    gcloud secrets create [INSTANCE_UNIX_SOCKET_SECRET] --data-file=-
```

Deploy the service to Cloud Run specifying the env var name and secret name:
```sh
gcloud beta run deploy SERVICE --image gcr.io/<YOUR_PROJECT_ID>/run-sql \
    --add-cloudsql-instances <PROJECT-ID>:<INSTANCE-REGION>:<INSTANCE-NAME> \
    --update-secrets INSTANCE_UNIX_SOCKET=[INSTANCE_UNIX_SOCKET_SECRET]:latest,\
      DB_USER=[DB_USER_SECRET]:latest, \
      DB_PASS=[DB_PASS_SECRET]:latest, \
      DB_NAME=[DB_NAME_SECRET]:latest
```
