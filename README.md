<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=400px src="https://github.com/hackedbyagirl/Eris/blob/main/imgs/eris-goddess.png" alt="Eris Avatar"></a>
</p>

<h2 align="center">Eris</h2>

<div align="center">

  [![Status](https://img.shields.io/badge/status-in%20development-yellowgreen)](https://github.com/hackedbyagirl/Eris) 
  [![GitHub Issues](https://img.shields.io/github/issues/hackedbyagirl/kali-packer-ami)](https://github.com/hackedbyagirl/Eris/issues)

</div>

---

<p align="center"> Automating resilient, reusable, and disposable offensive infrastructure utilizing packer and ansible to create Offensive AMIs that can be deployed to AWS EC2.
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Deployment](#deploy)
- [Built Using](#built_using)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>
Eris is a tool designed for creating Offensive Amazon Machine Images (AMIs) by utilizing `packer`, `amazon-ebs`, and `ansible` to create a offensive AMIs. Eris launches EC2 instance from a source AMI, provisioning the running machine, and then creates an AMI from that machine. 

The builder will create temporary keypairs, security group rules, etc. that provide it temporary access to the instance while the image is being created. This simplifies configuration quite a bit.

> *Note*: The builder does *not* manage AMIs. Once it creates an AMI and stores it in your account, it is up to you to use, delete, etc. the AMI. (Ex: Terraform)

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running for development and testing purposes.

### Prerequisites
- AWS Account - [Create AWS Account](https://www.aws.amazon.com/free)
- [AWS CLI](https://aws.amazon.com/cli/) **
- [Packer](https://www.packer.io/)
- [Ansible](https://www.ansible.com/)
- [Terraform](https://www.terraform.io/)

### Setup
Instructions on how to get Eris configured locally.

Clone the repository
```bash
#Download Repo and Navigate to Directory
git clone https://github.com/hackedbyagirl/Eris.git
cd Eris
```
Before building the image, it is important that you have the correct environmental variables set. 
Setup required Environmental Variables

Linux or MacOS
```bash
# Packer Variables
export PKR_VAR_aws_access_key=<YOUR_ACCESSKEY>
export PKR_VAR_aws_secret_key=<YOUR_SECRETKEY>

# AWS CLI Integration
export AWS_ACCESS_KEY_ID=<YOUR_ACCESSKEY>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRETKEY>
export AWS_DEFAULT_REGION=<region>
```

Windows

```bash 
# AWS CLI Integration
setx AWS_ACCESS_KEY_ID <AKIAIOSFODNN7EXAMPLE>
setx AWS_SECRET_ACCESS_KEY <wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY>
setx AWS_DEFAULT_REGION us-west-1

# Packer Variable
setx PKR_VAR_aws_access_key YOURKEY
setx PKR_VAR_aws_secret_key YOURKEY
```

## Usage <a name="usage"></a>
```bash
sudo poetry install
sudo poetry run python3 eris.py
```
Sit back, relax, and enjoy because this can take awhile :-)

***Important:** Note down the AMI-ID as this will be used for provisioning and deployment using terraform*
> Bug: You may get an error the first time you run this and it says you need to accept terms and conditions. Navigate to the link it provides. 
> I am still Trying to figure this out on the backend

## Acknowledgements <a name = "acknowledgement"></a>
Inspiration
- [hackedbyagirl kali ami](https://github.com/hackedbyagirl/kali-packer-ami)
- [Red Baron](https://github.com/byt3bl33d3r/Red-Baron)
- [CISAGOV](https://github.com/cisagov/kali-packer)

 
