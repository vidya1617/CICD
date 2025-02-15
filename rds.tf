
resource "aws_db_instance" "my_rds" {
  allocated_storage    = 20
  engine              = "mysql"
  engine_version      = "8.0"  
  instance_class      = "db.t3.micro"  
  db_name             = "rdsdb"
  username           = "admin"
  password           = "Vidya2004" 
  parameter_group_name = "default.mysql8.0"
  publicly_accessible = false
  skip_final_snapshot = true
}
