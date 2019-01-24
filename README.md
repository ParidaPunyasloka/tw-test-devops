## Run Playbook to create a Scale set behind a Load Balancer
The playbooks in this repositry are capable of 

* Creating Scale Sets, VMs
* Provisioning VMs
* Deploying Code

The Script **site.py** is a wrapper script to perform all these operations and is self-explainatory. All you need to do is *python site.py* in the ansible host machine to get going.

However, I will walkthrough what the various ansible commands that the script executes to performs these operations

### CREATING SCALED VMs BEHIND A LOAD BALANCER AND A TRAFFIC MANAGER

## Creating the Blue Infrastructre for the webApp deployment
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"
## Creating the Green Infrastructre for the webApp deployment
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "dev_scale_set"

## Creating the VM for static App deployment in the BLUE Infrastructre
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.iVM.json" --tags "dev_vm"
## Creating the VM for static App deployment in the GREEN Infrastructre
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.iVM.json" --tags "dev_vm"

## Provisioning the BLUE VM scalesets that require Apache HTTP server
ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "scale_set_inv,static_scale"


## Provisioning the GREEN VM scalesets that require Apache HTTP server
ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,static_scale"

## Provisioning the BLUE VM scalesets that require Apache Tomcat
ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "scale_set_inv,web_scale"

## Provisioning the GREEN VM scalesets that require Apache Tomcat
ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,web_scale"

## Provisioning the BLUE Individual VMs that require Apache HTTP Server
ansible-playbook provision/site.yml -i provision/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.iVM.json" --tags "static"

## Provisioning the GREEN Individual VMs that require Apache HTTP Server
ansible-playbook provision/site.yml -i provision/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.iVM.json" --tags "static"

## Provisioning the BLUE Individual VMs that require Apache Tomcat
ansible-playbook provision/site.yml -i provision/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.iVM.json" --tags "web"

## Provisioning the GREEN Individual VMs that require Apache Tomcat
ansible-playbook provision/site.yml -i provision/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.iVM.json" --tags "web"'

