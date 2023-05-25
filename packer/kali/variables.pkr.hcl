//  variables.pkr.hcl

// Variable declarations for input variables. Input variables serve as parameters
// for a Packer build, allowing aspects of the build to be customized without
// altering the build's own source code.

// AWS Configuration
variable "aws_access_key" {
    type    = string
    default = "${env("aws_access_key")}"
}
variable "aws_secret_key" {
    type    = string 
    default = "${env("aws_secret_key")}"   
}
variable "aws_region" {
    type = string
    default = ""  
}

// AMI Configuration
variable "ami_name" {
    type = string
}
variable "source_ami" {
    type = string
    default = "ami-08e895caaf450b4f9"
    description = "Kali Base 64-bit (x86) AMI from AWS Marketplace"
}
variable "inst_type" {
    type = string
    default = "t2.medium"
}
variable "ssh_user" {
    type = string
}
variable "defaults_file" {
    type = string
}
variable "tmp_key_pair" {
    type = string
}

// Tags
variable "vpc_tag" {
    type = string
}
variable "subnet_tag" {
    type = string
}
