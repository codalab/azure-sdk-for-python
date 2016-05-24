# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class ContainerService(Resource):
    """
    Container service

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: String
    :ivar name: Resource name
    :vartype name: String
    :ivar type: Resource type
    :vartype type: String
    :param location: Resource location
    :type location: String
    :param tags: Resource tags
    :type tags: dict
    :ivar provisioning_state: Gets the provisioning state, which only appears
     in the response.
    :vartype provisioning_state: str
    :param orchestrator_profile: Properties of orchestrator
    :type orchestrator_profile: :class:`ContainerServiceOrchestratorProfile
     <azure.mgmt.compute.models.ContainerServiceOrchestratorProfile>`
    :param master_profile: Properties of master agents
    :type master_profile: :class:`ContainerServiceMasterProfile
     <azure.mgmt.compute.models.ContainerServiceMasterProfile>`
    :param agent_pool_profiles: Properties of agent pools
    :type agent_pool_profiles: list of
     :class:`ContainerServiceAgentPoolProfile
     <azure.mgmt.compute.models.ContainerServiceAgentPoolProfile>`
    :param windows_profile: Properties of Windows VMs
    :type windows_profile: :class:`ContainerServiceWindowsProfile
     <azure.mgmt.compute.models.ContainerServiceWindowsProfile>`
    :param linux_profile: Properties for Linux VMs
    :type linux_profile: :class:`ContainerServiceLinuxProfile
     <azure.mgmt.compute.models.ContainerServiceLinuxProfile>`
    :param diagnostics_profile: Properties for Diagnostic Agent
    :type diagnostics_profile: :class:`ContainerServiceDiagnosticsProfile
     <azure.mgmt.compute.models.ContainerServiceDiagnosticsProfile>`
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'master_profile': {'required': True},
        'agent_pool_profiles': {'required': True},
        'linux_profile': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'String'},
        'name': {'key': 'name', 'type': 'String'},
        'type': {'key': 'type', 'type': 'String'},
        'location': {'key': 'location', 'type': 'String'},
        'tags': {'key': 'tags', 'type': '{String}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'orchestrator_profile': {'key': 'properties.orchestratorProfile', 'type': 'ContainerServiceOrchestratorProfile'},
        'master_profile': {'key': 'properties.masterProfile', 'type': 'ContainerServiceMasterProfile'},
        'agent_pool_profiles': {'key': 'properties.agentPoolProfiles', 'type': '[ContainerServiceAgentPoolProfile]'},
        'windows_profile': {'key': 'properties.windowsProfile', 'type': 'ContainerServiceWindowsProfile'},
        'linux_profile': {'key': 'properties.linuxProfile', 'type': 'ContainerServiceLinuxProfile'},
        'diagnostics_profile': {'key': 'properties.diagnosticsProfile', 'type': 'ContainerServiceDiagnosticsProfile'},
    }

    def __init__(self, location, master_profile, agent_pool_profiles, linux_profile, tags=None, orchestrator_profile=None, windows_profile=None, diagnostics_profile=None):
        super(ContainerService, self).__init__(location=location, tags=tags)
        self.provisioning_state = None
        self.orchestrator_profile = orchestrator_profile
        self.master_profile = master_profile
        self.agent_pool_profiles = agent_pool_profiles
        self.windows_profile = windows_profile
        self.linux_profile = linux_profile
        self.diagnostics_profile = diagnostics_profile