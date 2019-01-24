## Run Playbook to create a Scale set behind a Load Balancer
The playbooks in this repositry are capable of 

* Creating Scale Sets, VMs
* Provisioning VMs
* Deploying Code

The Script **site.py** is a wrapper script to perform all these operations and is self-explainatory. I will walkthrough what the various ansible commands that the script executes to performs these operations

### CREATING SCALED VMs BEHIND A LOAD BALANCER AND A TRAFFIC MANAGER

##
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"
## 
ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "dev_scale_set"
   

ansible-playbook infra/site.yml --ask-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"
ansible-playbook infra/site.yml --ask-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "dev_vm"
