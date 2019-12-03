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

from .proxy_only_resource_py3 import ProxyOnlyResource


class PushSettings(ProxyOnlyResource):
    """Push settings for the App.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param is_push_enabled: Required. Gets or sets a flag indicating whether
     the Push endpoint is enabled.
    :type is_push_enabled: bool
    :param tag_whitelist_json: Gets or sets a JSON string containing a list of
     tags that are whitelisted for use by the push registration endpoint.
    :type tag_whitelist_json: str
    :param tags_requiring_auth: Gets or sets a JSON string containing a list
     of tags that require user authentication to be used in the push
     registration endpoint.
     Tags can consist of alphanumeric characters and the following:
     '_', '@', '#', '.', ':', '-'.
     Validation should be performed at the PushRequestHandler.
    :type tags_requiring_auth: str
    :param dynamic_tags_json: Gets or sets a JSON string containing a list of
     dynamic tags that will be evaluated from user claims in the push
     registration endpoint.
    :type dynamic_tags_json: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'is_push_enabled': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'is_push_enabled': {'key': 'properties.isPushEnabled', 'type': 'bool'},
        'tag_whitelist_json': {'key': 'properties.tagWhitelistJson', 'type': 'str'},
        'tags_requiring_auth': {'key': 'properties.tagsRequiringAuth', 'type': 'str'},
        'dynamic_tags_json': {'key': 'properties.dynamicTagsJson', 'type': 'str'},
    }

    def __init__(self, *, is_push_enabled: bool, kind: str=None, tag_whitelist_json: str=None, tags_requiring_auth: str=None, dynamic_tags_json: str=None, **kwargs) -> None:
        super(PushSettings, self).__init__(kind=kind, **kwargs)
        self.is_push_enabled = is_push_enabled
        self.tag_whitelist_json = tag_whitelist_json
        self.tags_requiring_auth = tags_requiring_auth
        self.dynamic_tags_json = dynamic_tags_json