provider "vultr" {
  api_key = var.vultr_api_key
}

module "ssh_key" {
  source = "vultr/ssh-key/vultr"
  version = "1.0.0"

  name       = "terraform-key"
}

module "instance" {
  source = "vultr/instance/vultr"
  version = "1.0.0"

  region      = var.region
  plan        = "vc2-1c-1gb"
  os_slug     = "ubuntu_20_04"
  ssh_key_id  = module.ssh_key.ssh_key_id

  enable_ip_v6 = false
}

module "mysql" {
  source = "vultr/database/vultr"
  version = "1.0.0"

  region = var.region
  name   = var.mysql_database_name
  user   = var.mysql_database_user
  password = var.mysql_database_password
  plan   = "db-small"
}

module "container_registry" {
  source = "vultr/container-registry/vultr"
  version = "1.0.0"

  region = var.region
  plan = "registry-free"
}
