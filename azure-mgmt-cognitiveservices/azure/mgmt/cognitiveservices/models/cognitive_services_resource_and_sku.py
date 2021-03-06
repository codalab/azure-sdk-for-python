# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CognitiveServicesResourceAndSku(Model):
    """CognitiveServicesResourceAndSku.

    :param resource_type: Resource Namespace and Type
    :type resource_type: str
    :param sku:
    :type sku: :class:`Sku <azure.mgmt.cognitiveservices.models.Sku>`
    """

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
    }

    def __init__(self, resource_type=None, sku=None):
        self.resource_type = resource_type
        self.sku = sku
