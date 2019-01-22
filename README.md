## Run Playbook to create a Scale set behind a Load Balancer
ansible-playbook infra/site.yml --ask-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"
ansible-playbook infra/site.yml --ask-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "dev_vm"
