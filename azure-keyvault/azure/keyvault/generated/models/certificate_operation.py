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


class CertificateOperation(Model):
    """A certificate operation is returned in case of asynchronous requests.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The certificate id.
    :vartype id: str
    :param issuer_parameters: Parameters for the issuer of the X509 component
     of a certificate.
    :type issuer_parameters: :class:`IssuerParameters
     <azure.keyvault.generated.models.IssuerParameters>`
    :param csr: The certificate signing request (CSR) that is being used in
     the certificate operation.
    :type csr: bytearray
    :param cancellation_requested: Indicates if cancellation was requested on
     the certificate operation.
    :type cancellation_requested: bool
    :param status: Status of the certificate operation.
    :type status: str
    :param status_details: The status details of the certificate operation.
    :type status_details: str
    :param error: Error encountered, if any, during the certificate operation.
    :type error: :class:`Error <azure.keyvault.generated.models.Error>`
    :param target: Location which contains the result of the certificate
     operation.
    :type target: str
    :param request_id: Identifier for the certificate operation.
    :type request_id: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'issuer_parameters': {'key': 'issuer', 'type': 'IssuerParameters'},
        'csr': {'key': 'csr', 'type': 'bytearray'},
        'cancellation_requested': {'key': 'cancellation_requested', 'type': 'bool'},
        'status': {'key': 'status', 'type': 'str'},
        'status_details': {'key': 'status_details', 'type': 'str'},
        'error': {'key': 'error', 'type': 'Error'},
        'target': {'key': 'target', 'type': 'str'},
        'request_id': {'key': 'request_id', 'type': 'str'},
    }

    def __init__(self, issuer_parameters=None, csr=None, cancellation_requested=None, status=None, status_details=None, error=None, target=None, request_id=None):
        self.id = None
        self.issuer_parameters = issuer_parameters
        self.csr = csr
        self.cancellation_requested = cancellation_requested
        self.status = status
        self.status_details = status_details
        self.error = error
        self.target = target
        self.request_id = request_id
