# Cloud Run Deployment Script (`cloud_run.ps1`)

The `cloud_run.ps1` script automates the deployment of your API to [Google Cloud Run](https://cloud.google.com/run) using PowerShell. It reads configuration from a `.env` file, sets up the required Google Cloud project, enables necessary services, and deploys your application.

---

## How It Works

1. **Reads Environment Variables**  
   The script loads deployment settings (like `PROJECT_ID`, `SERVICE_NAME`, and `REGION`) from a `production.env` file. If any required variable is missing, it prompts you to enter it.

2. **Sets Google Cloud Project**  
   It sets the active Google Cloud project using the provided `PROJECT_ID`.

3. **Enables Required Services**  
   The script enables the Cloud Run and Cloud Build APIs for your project.

4. **Deploys to Cloud Run**  
   It constructs and runs the `gcloud run deploy` command, deploying your API source code to Cloud Run with the specified configuration.

---

## Usage

1. **Configure `production.env`**  
   Make sure your `production.env` file contains:

   ```env
   PROJECT_ID=your-gcp-project-id
   SERVICE_NAME=your-cloud-run-service-name
   REGION=your-gcp-region
   ```

2. **Run the Script**  
   Open PowerShell in your project directory and execute:

   ```powershell
   ./cloud_run.ps1
   ```

3. **Follow Prompts**  
   If any required variable is missing, the script will prompt you to enter it.

---

## Notes

- The script defaults the region to `asia-southeast2` if not specified.
- You must have the [Google Cloud SDK](https://cloud.google.com/sdk) installed and authenticated.
- Optional environment variables can be added to `production.env` and passed to Cloud Run by uncommenting and adjusting the relevant section in the script.

---

## Example `production.env`

```env
PROJECT_ID=required
SERVICE_NAME=api
REGION=asia-southeast2
```

---

This script simplifies and standardizes your Cloud Run deployment process, making it easy to deploy updates with a single command.
