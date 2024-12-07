gcloud builds submit --config cloudbuild.yaml .

gcloud run deploy cloudrunpython --image=us-central1-docker.pkg.dev/ltmhcl-dev/my-docker-repo/cloudrunpython:v1 --allow-unauthenticated --platform managed --region asia-southeast1

gcloud run deploy [SERVICE_NAME] \
    --image [IMAGE_URL] \
    --region [REGION] \
    --platform managed \
    --allow-unauthenticated \
    --cpu 1 \
    --memory 512Mi \
    --port 8080 \
    --timeout 300s


gcloud run services list --region [REGION]


gcloud run services update [SERVICE_NAME] \
    --image [NEW_IMAGE_URL] \
    --region [REGION]


gcloud run services describe [SERVICE_NAME] --region [REGION]

gcloud run services update [SERVICE_NAME] \
    --region [REGION] \
    --split [REVISION_NAME1]=[PERCENTAGE1] \
    --split [REVISION_NAME2]=[PERCENTAGE2]

gcloud run services update [SERVICE_NAME] \
    --no-allow-unauthenticated \
    --region [REGION]


gcloud run services update [SERVICE_NAME] \
    --cpu [CPU_LIMIT] \
    --memory [MEMORY_LIMIT] \
    --region [REGION]


gcloud logs read "resource.type=cloud_run_revision AND resource.labels.service_name=[SERVICE_NAME]" --region [REGION]


gcloud run services delete [SERVICE_NAME] --region [REGION]


gcloud run domain-mappings create \
    --domain [DOMAIN_NAME] \
    --service [SERVICE_NAME] \
    --region [REGION]

gcloud run services update [SERVICE_NAME] \
    --timeout [TIMEOUT_DURATION] \
    --region [REGION]

gcloud run revisions list --service [SERVICE_NAME] --region [REGION]


gcloud run services update [SERVICE_NAME] \
    --port [PORT_NUMBER] \
    --region [REGION]

Action	Command
Deploy a service	gcloud run deploy [SERVICE_NAME] --image [IMAGE_URL] --region [REGION]
List services	gcloud run services list --region [REGION]
Update a service's container image	gcloud run services update [SERVICE_NAME] --image [NEW_IMAGE_URL] --region [REGION]
Enable unauthenticated access	gcloud run services update [SERVICE_NAME] --allow-unauthenticated --region [REGION]
Split traffic between revisions	gcloud run services update [SERVICE_NAME] --region [REGION] --split [REVISION_NAME]=[PERCENTAGE]
Delete a service	gcloud run services delete [SERVICE_NAME] --region [REGION]
Set resource limits	gcloud run services update [SERVICE_NAME] --cpu [CPU_LIMIT] --memory [MEMORY_LIMIT] --region [REGION]
Configure domain mapping	gcloud run domain-mappings create --domain [DOMAIN_NAME] --service [SERVICE_NAME] --region [REGION]
View logs	gcloud logs read "resource.type=cloud_run_revision AND resource.labels.service_name=[SERVICE_NAME]" --region [REGION]
