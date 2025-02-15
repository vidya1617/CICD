resource "aws_s3_bucket" "my_s3_bucket"{
    bucket = "bucket-for-csvdata"

    tags = {
    Name = "My bucket"
    Enviroment ="Dev"
}
}
