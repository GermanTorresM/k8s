# Setup Amazon EKS Clusters

Amazon EKS (Elastic Container Service for Kubernetes) es un servicio de Kubernetes administrado que permite ejecutar Kubernetes en AWS sin la molestia de administrar el Kubernetes control plane. Amazon EKS une estas dos soluciones, lo que permite a los usuarios crear clústeres de Kubernetes en la nube de forma rápida y sencilla.



## Step 1: Before you start

Se deberá tener instalado y configurado los siguientes componentes:

* AWS CLI - Instrucciones de instalación, click aquí [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html]

* kubectl - Se utiliza para comunicarse con el servidor API del clúster. Instrucciones de instalación, click aquí [https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html]

* eksctl - Se utiliza para administrar el clúster Kubernetes en Amazon EKS. Instrucciones de instalación, click aquí [https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html]

* AWS-IAM-Authenticator - 



## Step 2: Create a new IAM role for EKS cluster to use.

1. Abrir la consola de IAM [https://console.aws.amazon.com/iam/].
2. En el panel de navegación de la consola, selecciona **Roles** a la izquierda.
3. Click en el botón **Create Role**.
4. En **Trusted entity type**, seleccione **AWS Service**.
5. En la lista desplegable **Use case**, selecciona **EKS**.
6. Seleccionar **EKS - Cluster** desde el caso de uso, y click en **Next**.
7. En la pestaña **Add permissions**, click en **Next**
8. En **Role name**, ingresa un nombre único para el rol, por ejemplo, ***eksClusterRole***.
9. En **Description**, ingrese texto descriptivo, como ***Amazon EKS - Cluster role***.
10. Click en el botón **Create role**.

Solo se requiere un solo rol para todos los clústeres EKS que se deseen crear.



## Step 3: Create a security group for EKS cluster.

1. Abrir la consola de administración de AWS.
2. Navegar a **Services > Networking & Content Delivery > VPC**.
3. Seleccione **Security groups** en la barra izquierda del panel de navegación.
4. Click en el botón **Create security group**
5. En la página de Create security group, configurar lo siguiente:
* Ingresar un **Security group name** y una **Description** a identificar la politica, por ejemplo, ***acme-eks-cluster-sg***.
* En **VPC**, seleccione la VPC creada.
* Mantener las demás configuraciones por predeterminado.
6. Click en el botón **Create security group**.



## Step 4: Create a EKS Cluster

1. Abrir la consola de administración de AWS.
2. Ir a **Services > Containers > Elastic Kubernetes Service**.
3. Seleccione **Cluster** en el panel de navegación de la izquierda
4. Elija **Add cluster** y, a continuación, elija **Create**
5. En la página de **Configure cluster** setear lo siguiente:
* **Name**: Un nombre único para el clúster, por ejemplo, ***acme-dev-us-east-1-eks-cluster***
* **Kubernetes version**: La versión de Kubernetes que debe utilizarse para el clúster. Seleccione la versión más reciente.
* **Cluster service role**: Elija el rol de IAM del clúster de Amazon EKS que creó para permitir que el control plane de Kubernetes administre los recursos de AWS en su nombre.
* **Tags**: Agregar las etiquetas al clúster.
6. Click en el botón **Next**
7. En la página **Specify networking** configure lo siguiente:
* **VPC**: Elija una VPC existente que cumpla con los Requisitos de Amazon EKS VPC en el que crear el clúster. Para obtener más información, consulte Creación de una VPC para su clúster de Amazon EKS [https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html].
* **Subnets**: De forma predeterminada, se preseleccionan todas las subredes disponibles de la VPC especificada en el campo anterior. Debe seleccionar al menos dos. Seleccione las subnets donde va a implementar los nodos de EKS
* **Security groups**: Especificar uno o varios grupos de seguridad que desea que Amazon EKS asocie a las interfaces de red que crea. (Ej, acme-eks-cluster-sg)
* **Choose cluster IP address family**: Puede elegir IPv4 e IPv6. Seleccionamos IPv4.
* **Cluster endpoint access**: Seleccione una opción. Una vez que se crea el clúster, puede cambiar esta opci+on. Para productivo se recomienda la opción **Private**.
8. Click en el botón **Next**
9. En la página **Configure observability** habilite las opciones de **Control plane logging**.
* _API server_
* _Audit_
* _Authenticator_
* _Controller manager_
* _Scheduler_
10. Click en **Next**
11. En la página de **Select add-ons** seleccione los complementos que desea agregar al clúster.
* _CoreDNS_
* _Amazon VPC CNI_
* _kube-proxy_
* _Amazon EKS Pod Identity Agent_
12. Click en **Next**
13. Click en **Next**
14. En la página **Review and create**, revise la información que ha introducido o seleccionado en las páginas anteriores. 
15. Click en el botón **Create**



## Step 5: Create a new IAM role for EKS node to use.

1. Abrir la consola de IAM [https://console.aws.amazon.com/iam/].
2. En el panel de navegación de la consola, selecciona **Roles** a la izquierda.
3. Click en el botón **Create Role**.
4. En **Trusted entity type**, seleccione **AWS Service**.
5. En la lista desplegable **Use case**, selecciona **EC2**.
6. Seleccionar **EC2** desde el caso de uso, y click en **Next**.
7. En la pestaña **Add permissions**, asociar la politica ***AmazonEKSWorkerNodePolicy***
8. En la pestaña **Add permissions**, asociar la politica ***AmazonEC2ContainerRegistryReadOnly***
9. Click en el botón **Next**
10. En **Role name**, ingresa un nombre único para el rol, por ejemplo, ***AmazonEKSNodeRole***.
11. En **Description**, ingrese texto descriptivo, como ***Amazon EKS - Node role***.
11. Click en el botón **Create role**.



## Step 5: Create a security group for EKS node.

1. Abrir la consola de administración de AWS.
2. Navegar a **Services > Networking & Content Delivery > VPC**.
3. Seleccione **Security groups** en la barra izquierda del panel de navegación.
4. Click en el botón **Create security group**
5. En la página de Create security group, configurar lo siguiente:
* Ingresar un **Security group name** y una **Description** a identificar la politica (por ejemplo, acme-eks-node-sg).
* En **VPC**, seleccione la VPC creada.
* Mantener las demás configuraciones por predeterminado.
6. Click en el botón **Create security group**.














## Step 4: Create an IAM OIDC provider

1. Abrir la consola de EKS [https://console.aws.amazon.com/eks/home#/clusters].
2. 



## Step 5: Configurar La política administrada AmazonEKS_CNI_Policy

1. 





You will probably want to create your own VPC. Don’t create one yourself — EKS is incredibly particular about things. Just use CloudFormation. Use this Amazon S3 template URL. The name for this VPC should be application specific. Name it "uat," "production," or whatever specific name you prefer. Each EKS cluster you create will have its own VPC. 



## Step 3: Install the awscli version 1.16.73 or higher

Even on newer versions of Ubuntu, the awscli is not up-to-date enough in the apt repos. You’ll have to manually install using python’s pip utility, but first you’ll want to make sure that the awscli package is removed. Here, I’m using python3, but you could easily use python2 if you already have it. To do this, replace all instances of “python3” with “python” (not “python2”) and “pip3” with “pip” (not “pip2”). 

 

sudo apt-get remove -y --purge awscli 

sudo apt-get install -y python3 python3-pip 

sudo pip3 install awscli --upgrade 

aws --version 

## Step 4: Create your EKS cluster with the AWS CLI

I recommend not using the AWS console, because it could mess up permissions later. The IAM user who creates the EKS cluster is the only user who will have access to it once created. I created a cluster using root credentials (not realizing it), and then used kubectl with my user’s credentials. To create your cluster, use the following command, but replace the following:

 

1) the role ARN with the role ARN in the first step of this tutorial;

2) the subnet IDs with the subnets created using the CloudFormation template in this tutorial;

3) the security group ID with the security group ID created using the same CloudFormation template; and

4) the name “devel” with whatever you want to call your EKS cluster.

To get these IDs from CloudFormation, go to the created stack, and click the Outputs tab. 

 

aws eks create-cluster --name devel --role-arn arn:aws:iam::111122223333:role/eks-service-role-AWSServiceRoleForAmazonEKS-EXAMPLEBKZRQR --resources-vpc-config subnetIds=subnet-a9189fe2,subnet-50432629,securityGroupIds=sg-f5c54184 


## Step 5: Install kubectl

This tool (kubectl) is how you manage kubernetes clusters. This step is not specific to AWS, so if you already have kubectl, you are good to go. For Ubuntu, I recommend using the system package manager by running these simple commands: 

 

sudo apt-get update && sudo apt-get install -y apt-transport-https 

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - 

echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list 

sudo apt-get update 

sudo apt-get install -y kubectl 

## Step 6: Install Amazon's authenticator for kubectl and IAM

Amazon EKS uses IAM for user management and access to clusters. Out of the box, kubectl does not support IAM. To bridge the gap, you must install a binary on your system called  aws-iam-authenticator. Run these commands on Ubuntu: 

 

curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.11.5/2018-12-06/bin/linux/amd64/aws-iam-authenticator 

chmod +x aws-iam-authenticator 

sudo mv aws-iam-authenticator /usr/bin/aws-iam-authenticator 

## Step 7: Wait until the EKS cluster status is "ACTIVE"

It should take about 10 minutes from when you ran the AWS CLI command to create it. 

## Step 8: Update your ~/.kube/config using AWS CLI

If you’ve followed the tutorial exactly to this point, all you need to do is run this command. It will update your kubectl configuration file with the context, user, and authentication commands. You will need to replace the name “devel” with the name of your cluster used in the “aws eks create-cluster” command above. Then, you can test your connection using the kubectl command listed next. 

 

aws eks update-kubeconfig --name devel 

kubectl get svc  

## Step 9: Launch worker nodes into EKS cluster

There are a lot of options here, so I’ll just defer to the AWS docs link I posted. This step will help you create EC2 instances, place them in the right subnets, and help them connect to the EKS cluster. As such, it’s important to follow the directions exactly. 

## Step 10: Download, edit, and apply the AWS authenticator configuration map

This is a continuation of the previous step (even in the AWS docs), but worthy of note, since your nodes will not show up in the EKS cluster otherwise. To watch your nodes show up, run this kubectl command: 

 

kubectl get nodes --watch 

## Step 11: Use kubectl like you would with any other kubernetes cluster

At this point, you have a fully functioning EKS cluster. Congratulations!. 


## Step 12:

## Step 13:

## Step 14:

## Step 15:



Open the IAM console at https://console.aws.amazon.com/iam/.

In the left navigation pane, choose **Roles**.

On the **Roles** page, choose **Create role**.

On the **Select trusted entity** page, do the following:

In the **Trusted entity type** section, choose **AWS service**.

Under **Use case**, choose **EC2**.

Choose **Next**.

On the **Add permissions** page, attach a custom policy or do the following:

In the **Filter policies** box, enter ***AmazonEKSWorkerNodePolicy***.

Select the check box to the left of **AmazonEKSWorkerNodePolicy** in the search results.

Choose **Clear filters**.

In the **Filter policies** box, enter ***AmazonEC2ContainerRegistryReadOnly***.

Select the check box to the left of **AmazonEC2ContainerRegistryReadOnly** in the search results.

Either the **AmazonEKS_CNI_Policy** managed policy, or an IPv6 policy that you create must also be attached to either this role or to a different role that's mapped to the aws-node Kubernetes service account. We recommend assigning the policy to the role associated to the Kubernetes service account instead of assigning it to this role. For more information, see Configuring the Amazon VPC CNI plugin for Kubernetes to use IAM roles for service accounts.

Choose **Next**.

On the **Name, review, and create** page, do the following:

For **Role name**, enter a unique name for your role, such as ***AmazonEKSNodeRole***.

For **Description**, replace the current text with descriptive text such as ***Amazon EKS - Node role***.

Under **Add tags (Optional)**, add metadata to the role by attaching tags as key–value pairs. For more information about using tags in IAM, see Tagging IAM Entities in the IAM User Guide.

Choose **Create role**.