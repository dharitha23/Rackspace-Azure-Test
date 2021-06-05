# Import the needed credential and management objects from the libraries.
import os
import json
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import InteractiveBrowserCredential
from azure.mgmt.resource.resources.models import DeploymentMode
from azure.mgmt.resource.resources.models import Deployment
from azure.mgmt.resource.resources.models import DeploymentProperties


# Acquire a credential object using CLI-based authentication.
credential = InteractiveBrowserCredential(tenant_id="570057f4-73ef-41c8-bcbb-08db2fc15c2b")

# Retrieve subscription ID from environment variable.
# subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
subscription_id = "86fa884d-210e-466a-a164-dddbfb866563"

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential=credential, subscription_id=subscription_id)
resource_group = "HelloWorld-rg"
location = "eastus"

#step1: Create a resource group
rg_result = resource_client.resource_groups.create_or_update(
    resource_group,
    {
        "location": location,
        "tags": { "environment":"test" }
    }
)

#step2: Create VNET with a subnet

template_path = os.path.join(os.path.dirname(__file__), 'templates', 'azuredeploy.json')
with open(template_path, 'r') as template_file_fd:
    template = json.load(template_file_fd)

parameters = {
    'vnetName': "Vnet1",
    'subnetName': "Subnet1",
    'location': location
}

parameters = {k: {'value': v} for k, v in parameters.items()}

deployment_properties = DeploymentProperties(mode=DeploymentMode.incremental, template=template, parameters=parameters)

deployment_async_operation = resource_client.deployments.begin_create_or_update(
    resource_group_name = resource_group,
    deployment_name = 'vnet-and-subnet',
    parameters = Deployment(properties=deployment_properties)
)

deployment_async_operation.wait()