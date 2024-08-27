output "instance_ip" {
  description = "The IP address of the Ubuntu VM"
  value       = module.instance.instance_ip
}

output "mysql_root_password" {
  description = "The root password of the MySQL database"
  value       = module.mysql.mysql_root_password
}

output "container_registry_url" {
  description = "The URL of the Container Registry"
  value       = module.container_registry.container_registry_url
}
