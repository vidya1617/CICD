provider "aws" {
  region = "ap-southeast-1"  
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-039454f12c36e7620" 
  instance_type = "t2.micro"
  key_name      = "vidya"

  tags = {
    Name = "MyTerraformEC2"
  }
}
