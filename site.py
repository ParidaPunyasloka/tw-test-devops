import subprocess

def vmScaleSetdeployment():
    pass
def individualVMdeployment():
    pass
deploymentTypeSelection= {
    '1': vmScaleSetdeployment(),
    '2': individualVMdeployment()
}
def vmScaleSetprovision():
    pass
def individualVMprovision():
    pass
provisionTypeSelection= {
    '1': vmScaleSetprovision(),
    '2': individualVMprovision()
}
def vmScaleSet():
    subprocess.run(["ansible-playbook", 'infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"'])
     
def individualVM():
    subprocess.run(["ansible-playbook", 'infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "dev_scale_set"'])
infraTypeSelection = {
    '1': vmScaleSet(),
    '2': individualVM()
}
def infraCreation():
    infraType = input("What Kind of VM do you want to create ?\n1)VM Scale Set\n2)Individual VM")
    if infraType:
        infraChoiceSelected = infraTypeSelection[infraType]
def provisioning():
    provisionType = input("What kind of VM you would provision to ?\n1)VM Scale Set\n2)Individual VM")
    if provisionType:
        provisionTypeSelected = provisionTypeSelection[provisionType]
def deployment():
    deploymentType = input("What kind of VM you would provision to ?\n1)VM Scale Set\n2)Individual VM")
    if deploymentType:
        deploymentTypeSelected = deploymentTypeSelection[deploymentType]

acitivitySelection = {
    '1': infraCreation(),
    '2': provisioning(),
    '3': deployment()
}
print("Welcome to Ansible Interactive\n")

activityOption = input("Select an activity you want to perform\n\n1)Infrastructure Creation\n2)Provisioning\n3)Deployment\n\nType an option (1,2 or 3) and hit ENTER: ")
if activityOption:
    choiceSelected = acitivitySelection[activityOption]
else:
    print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
    exit(0)
