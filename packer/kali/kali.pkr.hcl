source "amazon-ebs" "kali" {
  // AWS Configuration
  access_key                   = "${var.aws_access_key}"
  secret_key                   = "${var.aws_secret_key}"
  region                       = var.aws_region
  
  // AMI Configuration
  ami_name                     = var.ami_name
  source_ami                   = var.source_ami
  instance_type                = var.inst_type
  associate_public_ip_address  = true
  force_deregister             = true
  ssh_username                 = var.ssh_user
  user_data_file               = var.defaults_file
  temporary_key_pair_type      = var.tmp_key_pair

  // Filters to populate the `vpc_id` field and `subnet_id` field
  vpc_filter {
    filters = {
      "tag:Name" = var.vpc_tag
    }
  }    
  subnet_filter {
    filters = {
      "tag:Name" = var.subnet_tag
    }
  }

  // AMI Build Tags
  tags = {
    Application        = "Kali-OffsecOps"
    OS_Version         = "Kali Linux"
    Team               = "Offensive Security Team"
    Deployment         = "Eris"
  }
}

// Build AMI Resource
build {
  sources = [
    "source.amazon-ebs.kali"
  ]

  provisioner "file" {
    source = var.defaults_file
    destination = "/tmp/defaults.cfg"
  }

  provisioner "shell" {
    inline = ["sudo mv /tmp/defaults.cfg /etc/cloud/cloud.cfg.d/deafults.cfg"]
  }

  provisioner "shell" {
    execute_command = "sudo env {{ .Vars }} {{ .Path }}"
    inline 	    = ["rm --force /root/.ssh/authorized_keys", "rm --force /etc/cloud/cloud.cfg.d/20_kali.cfg"]
    skip_clean      = true
  }
  
  provisioner "ansible" {
    user = ""
    playbook_file = "../../data/playbooks/kali-playbook/kali_base.yml"
    use_proxy     = false
  }
}
