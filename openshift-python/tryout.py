from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config('/Users/nickfreer/.kube/config')

dyn_client = DynamicClient(k8s_client)

v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')

project_list = v1_projects.get()
print(project_list)
# for project in project_list.items:
#     print(project.metadata.name)

