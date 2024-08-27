terraform {
  required_providers {
    vultr = {
      source  = "vultr/vultr"
      version = "2.10.1"
    }
  }
}

provider "vultr" {
  api_key = terraform.tfvars.vultr_api_key
}

resource "vultr_instance" "example" {
  plan = "vc2-1c-1gb"
  region = "ewr"
  os_id = "387"  # Ubuntu 20.04
}

resource "vultr_database" "example" {
  label = "example-db"
  region = "ewr"
  plan = "db-1c-1gb"
  database_type = "mysql"
  database_version = "8.0"
}

resource "vultr_container_registry" "example" {
  label = "example-registry"
  region = "ewr"
}
