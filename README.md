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

<p align="center"> Automating resilient, reusable, and disposable offensive infrastructure utilizing packer, ansible, and terraform. 
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Acknowledgments](#acknowledgement)

## About <a name = "about"></a>
Eris utilizes a set of modules and third-party terraform providers to create resilient, reusable, and disposable offensive infrastructure.

## Getting Started <a name = "getting_started"></a>
### Prerequisites
- AWS Account - [Create AWS Account](https://www.aws.amazon.com/free)
- [AWS CLI](https://aws.amazon.com/cli/) **
- [Terraform](https://www.terraform.io/)
- [Ansible](https://www.ansible.com/)

### Setup
Instructions on how to get Eris configured locally.

Clone the repository
```bash
#Download Repo and Navigate to Directory
git clone https://github.com/hackedbyagirl/Eris.git
cd Eris
```

Setup required Environmental Variables
```bash
# Export Required Keys
export AWS_ACCESS_KEY_ID="accesskey"
export AWS_SECRET_ACCESS_KEY="secretkey"
export AWS_DEFAULT_REGION="default region"
```

## Usage <a name="usage"></a>
```bash
sudo poetry install
sudo poetry run python3 eris.py
```

## Acknowledgements <a name = "acknowledgement"></a>
Inspiration
- [Red Baron](https://github.com/byt3bl33d3r/Red-Baron)
- [CISAGOV](https://github.com/cisagov/kali-packer)

 
