import subprocess

def vmScaleSetdeployment():
    pass
def individualVMdeployment():
    pass
def deploymentTypeSelection(x):
    return {
    '1': vmScaleSetdeployment(),
    '2': individualVMdeployment()
}[x]
def vmScaleSetprovision():
    pass
def individualVMprovision():
    pass
def provisionTypeSelection(x):
    return {
    '1': vmScaleSetprovision(),
    '2': individualVMprovision()
}[x]
def vmScaleSet():
    subprocess.call(["ansible-playbook", "infra/site.yml", "--vault-id", "ansible-vault-pass", "--extra-vars", '"@extra_vars/infra.blue.json"', "--tags", '"dev_scale_set"'])
     
def individualVM():
    subprocess.call(["ansible-playbook", "infra/site.yml", "--vault-id", "ansible-vault-pass", "--extra-vars", '"@extra_vars/infra.blue.json"', "--tags", '"dev_vm"'])
def infraTypeSelection(x):
    return {
    '1': vmScaleSet(),
    '2': individualVM()
}[x]
def infraCreation():
    infraType = input("What Kind of VM do you want to create ?\n1)VM Scale Set\n2)Individual VM")
    if infraType:
        infraChoiceSelected = infraTypeSelection(infraType)
def provisioning():
    provisionType = input("What kind of VM you would provision to ?\n1)VM Scale Set\n2)Individual VM")
    if provisionType:
        provisionTypeSelected = provisionTypeSelection(provisionType)
def deployment():
    deploymentType = input("What kind of VM you would provision to ?\n1)VM Scale Set\n2)Individual VM")
    if deploymentType:
        deploymentTypeSelected = deploymentTypeSelection(deploymentType)

def acitivitySelection(x):
    return {
    '1': infraCreation(),
    '2': provisioning(),
    '3': deployment()
}[x]
print("Welcome to Ansible Interactive\n")
activityOption = input("Select an activity you want to perform\n\n1)Infrastructure Creation\n2)Provisioning\n3)Deployment\n\nType an option (1,2 or 3) and hit ENTER: ")
if activityOption:
    choiceSelected = acitivitySelection(activityOption)
else:
    print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
    exit(0)
