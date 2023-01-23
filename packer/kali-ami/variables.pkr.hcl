//  variables.pkr.hcl

// This is where the HCL varaibels are declared. You could put these at the top of
// your main .pkr.hcl file, but it is good practice to keep your variables files
// seperate.

// Variable declarations for input variables. Input variables serve as parameters
// for a Packer build, allowing aspects of the build to be customized without
// altering the build's own source code.

// Access Configuration
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
//variable "ami_desc" {
//    type = string
//}
//variable "ami_tag" {
//    type = string
//}

// Run Configuration
variable "inst_type" {
    type = string
}
variable "source_ami" {
    type = string
}
