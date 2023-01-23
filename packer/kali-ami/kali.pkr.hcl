source "amazon-ebs" "kali-AMI-test" {
  access_key    = "${var.aws_access_key}"
  secret_key    = "${var.aws_secret_key}"
  region        = var.aws_region
  ami_name      = var.ami_name
  source_ami    = var.source_ami
  instance_type = var.inst_type
  force_deregister = true

  ssh_username   = ""
  user_data_file = "./defaults.cfg"
  associate_public_ip_address  = true
  temporary_key_pair_type = "ed25519"

  subnet_filter {
    filters = {
      "tag:Name" = "test-build"
    }
  }
}

build {
  sources = [
    "source.amazon-ebs.kali-AMI-test"
  ]

  provisioner "file" {
    source = "./defaults.cfg"
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
    playbook_file = "../../ansible/kali_base.yml"
    use_proxy     = false
  }
}
