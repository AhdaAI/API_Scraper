Write-Host "Starting Cloud Run deployment script..."

gcloud run deploy --source . --region asia-southeast2 --cpu-throttling --max-instances 1 --port 8080