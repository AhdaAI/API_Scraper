# Define the path to your .env file
$envFilePath = ".\production.env"

# Initialize a hashtable to store environment variables
$envVars = @{}

# Load environment variables from the .env file if it exists
if (Test-Path $envFilePath) {
    Get-Content $envFilePath | ForEach-Object {
        # Skip empty lines and comments
        if ($_ -and -not $_.StartsWith("#")) {
            # Split the line into key and value
            $parts = $_ -split '=', 2
            if ($parts.Count -eq 2) {
                $key = $parts[0].Trim()
                $value = $parts[1].Trim()
                $envVars[$key] = $value
            }
        }
    }
} else {
    Write-Warning "The .env file was not found at path: $envFilePath"
}

# Define required parameters
$requiredParams = @("PROJECT_ID", "SERVICE_NAME")

# Prompt for missing required parameters
foreach ($param in $requiredParams) {
    if (-not $envVars.ContainsKey($param) -or [string]::IsNullOrWhiteSpace($envVars[$param])) {
        $inputValue = Read-Host "Enter value for $param"
        if ([string]::IsNullOrWhiteSpace($inputValue)) {
            Write-Error "$param is required. Exiting script."
            exit 1
        }
        $envVars[$param] = $inputValue
    }
}

# Set default values for optional parameters if not provided
if (-not $envVars.ContainsKey("REGION") -or [string]::IsNullOrWhiteSpace($envVars["REGION"])) {
    write-host "No REGION provided, defaulting to asia-southeast2"
    $envVars["REGION"] = "asia-southeast2"
}

# Set the active project
write-host "Setting active project to $($envVars["PROJECT_ID"])"
gcloud config set project $envVars["PROJECT_ID"]

# Enable required services
write-host "Enabling required services..."
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Deploy to Cloud Run
$deployCommand = @(
    "gcloud run deploy $($envVars["SERVICE_NAME"])",
    "--source .",
    "--region $($envVars["REGION"])",
    "--cpu-throttling",
    "--max-instances 1",
    "--allow-unauthenticated"
)

# Prepare environment variables string for deployment
# $deploymentEnvVars = $envVars.GetEnumerator() | Where-Object {
#     $_.Key -notin $requiredParams -and $_.Key -ne "REGION" -and $_.Key -ne "IMAGE_TAG"
# } | ForEach-Object {
#     "$($_.Key)=$($_.Value)"
# }

# $envVarsString = if ($deploymentEnvVars.Count -gt 0) {
#     "--set-env-vars " + ($deploymentEnvVars -join ",")
# } else {
#     ""
# }

# if ($envVarsString -ne "") {
#     $deployCommand += $envVarsString
# }

# Join the array elements into a single string with spaces
$fullCommand = $deployCommand -join " "
write-host "Executing: $fullCommand"
Invoke-Expression $fullCommand