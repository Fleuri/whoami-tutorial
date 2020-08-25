resource "google_cloud_run_service" "whoami" {
  name     = var.service_name
  location = var.region
  project  = var.project

  template {
    spec {
      containers {
        image = "gcr.io/${var.project}/whoami:latest"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location = google_cloud_run_service.whoami.location
  project  = google_cloud_run_service.whoami.project
  service  = google_cloud_run_service.whoami.name

  policy_data = data.google_iam_policy.noauth.policy_data
}
