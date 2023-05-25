// ami.auto.pkrvars.hcl

// Variables that are loaded automatically and are the same for every build. This
// is where the AMI build variables will be stored. File is not needed to be passed
// at the command line.

// AWS Configuration
aws_region    = "us-west-1"

// AMI Configuration
ami_name      = "Kali-Base-Eris"
source_ami    = "ami-08e895caaf450b4f9"
inst_type     = "t2.medium"
ssh_user      = "bnastee"
defaults_file = "./defaults.cfg"
tmp_key_pair  = "ed25519"

// Tags
vpc_tag       = "AMI Build"
subnet_tag    = "AMI Build"

