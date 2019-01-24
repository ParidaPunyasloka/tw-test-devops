## INFRASTRUCTRE CREATION, PROVISIONING AND DEPLOYMENT USING ANSIBLE

The playbooks in this repositry are capable of 

* Creating Scale Sets, VMs
* Provisioning VMs
* Deploying Code

Pre-Requisites:

* Linux Host Machine (With Ansible installed along with python 2.7)
* Azure SDKs. You can install by running the command: *pip install 'ansible[azure]'*
* Some Files in this Repository are are encrypted through Ansible-Vault. You need a file with pass key for the Vault in the root directory from where you would be running the scripts. The name of the file should be *ansible-vault-pass*
* The Artifactory is assumed to be a local folder in the Ansible Host machine itself

### Notes: 
* A **Self signed certificate** is created through Java **Keytool** using the provisioning step of ApacheTomcat. The certificate is deployed to tomcat and hence making it available via HTTPS.
* The Deployed site can accessed via https://blue-green-tw.trafficmanager.net/
* The site can also be accessed via the public IP of the load balancer as well. 


The Script **site.py** is a wrapper script to perform all these operations and is self-explainatory. All you need to do is 
*python site.py* in the ansible host machine to get going.

However, I will walkthrough what the various ansible commands that the script executes to performs these operations

### CREATING SCALED VMs BEHIND A LOAD BALANCER AND A TRAFFIC MANAGER

This ansible code base uses roles to modularize various deployment functionalities. Also the runtime configurations are stored inside the folder extra_vars. Any confiugration changes required to the Infrastrucure or the deployment needs to made to the files inside the folder before executing the *site.py* script

A brief description of the config files
**infra.blue.json** Configuration for VM scale sets under the BLUE environment
**infra.green.json** Configuration for VM scale sets under the GREEN environment
**infra.blue.iVM.json** Configuration for individual VMs (Those that don't belong to the VM scale set, especially the static app VMs) sets under the BLUE environment
**infra.green.iVM.json** Configuration for individual VMs (Those that don't belong to the VM scale set, especially the static app VMs) under the GREEN environment


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

## Deploying the StaticApp to BLUE VM Scale Sets
ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "scale_set_inv,static_scale"

## Deploying the StaticApp to GREEN VM Scale Sets
ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,static_scale"

## Deploying the StaticApp to BLUE VM Scale Sets
ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "scale_set_inv,web_scale"

## Deploying the WebApp to GREEN VM Scale Sets
ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,web_scale"

## Deploying the StaticApp to GREEN individual VMs
ansible-playbook deployment/site.yml -i deployment/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.iVM.json" --tags "static"

## Deploying the StaticApp to GREEN individual VMs
ansible-playbook deployment/site.yml -i deployment/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.iVM.json" --tags "static"

## Deploying the WebApp to BLUE individual VMs
ansible-playbook deployment/site.yml -i deployment/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.iVM.json" --tags "web"

## Deploying the WebApp to BLUE individual VMs
ansible-playbook deployment/site.yml -i deployment/inv/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.iVM.json" --tags "web"
