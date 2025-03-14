resource "null_resource" "delete_old_gcr_images" {
  provisioner "local-exec" {
    command = <<EOT
      #!/bin/bash
      # Authenticate with gcloud (ensure authentication is already set up)
      PROJECT_ID="your-project-id"
      REPOSITORY_NAME="your-repository-name"
      DATE_THRESHOLD=$(date -d "-85 days" +%Y-%m-%dT%H:%M:%SZ)

      # List all images in the repository
      IMAGES=$(gcloud container images list-tags gcr.io/${PROJECT_ID}/${REPOSITORY_NAME} \
        --format="get(digest, timestamp.datetime)" \
        --filter="timestamp.datetime<'${DATE_THRESHOLD}'")

      # Loop through and delete old images
      while IFS= read -r IMAGE; do
        DIGEST=$(echo $IMAGE | awk '{print $1}')
        echo "Deleting image: $DIGEST"
        gcloud container images delete gcr.io/${PROJECT_ID}/${REPOSITORY_NAME}@${DIGEST} --quiet
      done <<< "$IMAGES"
    EOT
  }
}
