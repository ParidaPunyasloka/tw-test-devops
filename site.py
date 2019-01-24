import subprocess
def staticapp_blue():
    cmd = 'ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set,static_scale"'
    subprocess.call(cmd, shell=True) 
def staticapp_green():
    cmd = 'ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,static_scale"'
    subprocess.call(cmd, shell=True) 
def webapp_blue():
    cmd = 'ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set,web_scale"'
    subprocess.call(cmd, shell=True) 
def webapp_green():
    cmd = 'ansible-playbook deployment/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,web_scale"'
    subprocess.call(cmd, shell=True) 
def webappDeployment(x):
    if(x==1):
        webapp_blue()
    elif(x==2):
        webapp_green()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def staticappDeployment(x):
    if(x==1):
        staticapp_blue()
    elif(x==2):
        staticapp_green()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def webapp_vmset():
    webappdeploymentType = input("\nWhat kind of  Infra do you want this Application to be installed in ?\n\n1)Blue\n2)Green \n\nType an option (1 or 2) and hit ENTER: ")
    if webappdeploymentType:
        webappDeployment(webappdeploymentType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def staticapp_vmset():
    staticappdeploymentType = input("\nWhat kind of  Infra do you want this Application to be installed in ?\n\n1)Blue\n2)Green \n\nType an option (1 or 2) and hit ENTER: ")
    if staticappdeploymentType:
        staticappDeployment(staticappdeploymentType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def webapp():
    cmd = 'ansible-playbook deployment/site.yml -i deployment/inventory/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "web"'
    subprocess.call(cmd, shell=True) 
def staticapp():
    cmd = 'ansible-playbook deployment/site.yml -i deployment/inventory/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "static"'
    subprocess.call(cmd, shell=True) 
def CodeDeployment_vmset(x):
    if(x==1):
        webapp_vmset()
    elif(x==2):
        staticapp_vmset()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def CodeDeployment(x):
    if(x==1):
        webapp()
    elif(x==2):
        staticapp()  
    else:
        print('Invalid Option! Exiting')
        exit(0)

def vmScaleSetdeployment():
    vmScaleSetDeploymentAppType = input("\nWhat do you want to deploy ?\n\n1)WebApp\n2)Static-WebApp(Staic Files) VM\n\nType an option (1 or 2) and hit ENTER: ")
    if vmScaleSetDeploymentAppType:
        CodeDeployment_vmset(vmScaleSetDeploymentAppType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)   
def individualVMdeployment():
    individualVMDeploymentAppType = input("\nWhat do you want to deploy ?\n\n1)WebApp\n2)Static-WebApp(Staic Files) VM\n\nType an option (1 or 2) and hit ENTER: ")
    if individualVMDeploymentAppType:
        CodeDeployment(individualVMDeploymentAppType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)  
def deploymentTypeSelection(x):
    if(x==1):
        vmScaleSetdeployment()
    elif(x==2):
        individualVMdeployment()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def httpd_blue():
    cmd = 'ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set,static_scale"'
    subprocess.call(cmd, shell=True) 
def httpd_green():
    cmd = 'ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,static_scale"'
    subprocess.call(cmd, shell=True) 
def tomcat_blue():
    cmd = 'ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set,web_scale"'
    subprocess.call(cmd, shell=True) 
def tomcat_green():
    cmd = 'ansible-playbook provision/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "scale_set_inv,web_scale"'
    subprocess.call(cmd, shell=True) 
def tomcatDeployment(x):
    if(x==1):
        tomcat_blue()
    elif(x==2):
        tomcat_green()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def httpdDeployment(x):
    if(x==1):
        httpd_blue()
    elif(x==2):
        httpd_green()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def tomcat_vmset():
    tomcatdeploymentType = input("\nWhat kind of  Infra do you want this Application to be installed in ?\n\n1)Blue\n2)Green \n\nType an option (1 or 2) and hit ENTER: ")
    if tomcatdeploymentType:
        tomcatDeployment(tomcatdeploymentType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def httpd_vmset():
    httpddeploymentType = input("\nWhat kind of  Infra do you want this Application to be installed in ?\n\n1)Blue\n2)Green \n\nType an option (1 or 2) and hit ENTER: ")
    if httpddeploymentType:
        httpdDeployment(httpddeploymentType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def tomcat():
    cmd = 'ansible-playbook provision/site.yml -i provision/inventory/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "web"'
    subprocess.call(cmd, shell=True) 
def httpd():
    cmd = 'ansible-playbook provision/site.yml -i provision/inventory/azure_rm.py --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "static"'
    subprocess.call(cmd, shell=True) 
def ApplicationInstallation_vmset(x):
    if(x==1):
        tomcat_vmset()
    elif(x==2):
        httpd_vmset()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def ApplicationInstallation(x):
    if(x==1):
        tomcat()
    elif(x==2):
        httpd()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def vmScaleSetprovision():
    ApplicationType = input("\nWhat Application do you want to provision ?\n\n1)Apache Tomcat\n2)Apache HTTP server VM\n\nType an option (1 or 2) and hit ENTER: ")
    if ApplicationType:
        ApplicationInstallation_vmset(ApplicationType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)   
def individualVMprovision():
    ApplicationType = input("\nWhat Application do you want to provision ?\n\n1)Apache Tomcat\n2)Apache HTTP server VM\n\nType an option (1 or 2) and hit ENTER: ")
    if ApplicationType:
        ApplicationInstallation(ApplicationType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)   
def provisionTypeSelection(x):
    if(x==1):
        vmScaleSetprovision()
    elif(x==2):
        individualVMprovision()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def blueInfra():
    cmd = 'ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.blue.json" --tags "dev_scale_set"'
    subprocess.call(cmd, shell=True)
def greenInfra():
    cmd = 'ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.green.json" --tags "dev_scale_set"'
    subprocess.call(cmd, shell=True)
def blueGreenSelection(x):
    if(x==1):
        blueInfra()
    elif(x==2):
        greenInfra()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def vmScaleSet():
    blueGreenType = input("\nWhich group do you want your Infra to be part of ?\n\n1)Blue\n2)Green \n\nType an option (1 or 2) and hit ENTER: ")
    if blueGreenType:
        blueGreenSelection(blueGreenType)    
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)        
def individualVM():
    cmd = 'ansible-playbook infra/site.yml --vault-id ansible-vault-pass --extra-vars "@extra_vars/infra.json" --tags "dev_vm"'
    subprocess.call(cmd, shell=True)
def infraTypeSelection(x):
    if(x==1):
        vmScaleSet()
    elif(x==2):
        individualVM()  
    else:
        print('Invalid Option! Exiting')
        exit(0)
def infraCreation():
    infraType = input("\nWhat Kind of VM do you want to create ?\n\n1)VM Scale Set\n2)Individual VM\n\nType an option (1 or 2) and hit ENTER: ")
    if infraType:
        infraTypeSelection(infraType)
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def provisioning():
    provisionType = input("What kind of VM you would provision to ?\n1)VM Scale Set\n2)Individual VM\n\nType an option (1 or 2) and hit ENTER: ")
    if provisionType:
        provisionTypeSelection(provisionType)
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)
def deployment():
    deploymentType = input("What kind of VM you would deploy to  ?\n1)VM Scale Set\n2)Individual VM\n\nType an option (1 or 2) and hit ENTER: ")
    if deploymentType:
        deploymentTypeSelection(deploymentType)
    else:
        print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
        exit(0)

def acitivitySelection(x):
    if(x==1):
        infraCreation()
    elif(x==2):
        provisioning()
    elif(x==3):
        deployment()    
    else:
        print('Invalid Option! Exiting')
        exit(0)
print("Welcome to Ansible Interactive\n")
activityOption = input("Select an activity you want to perform\n\n1)Infrastructure Creation\n2)Provisioning\n3)Deployment\n\nType an option (1,2 or 3) and hit ENTER: ")
if activityOption:
    acitivitySelection(activityOption)
else:
    print("\nNo Option Selected. Exiting the Interactive session.GoodBye!") 
    exit(0)
