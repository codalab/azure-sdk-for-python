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


class InputPort(Model):
    """Asset input port.

    :param type: Port data type. Possible values include: 'Dataset'. Default
     value: "Dataset" .
    :type type: str or :class:`InputPortType
     <azure.mgmt.machinelearning.models.InputPortType>`
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, type="Dataset"):
        self.type = type
