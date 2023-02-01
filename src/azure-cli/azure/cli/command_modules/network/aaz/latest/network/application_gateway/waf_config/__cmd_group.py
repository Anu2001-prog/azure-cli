# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network application-gateway waf-config",
)
class __CMDGroup(AAZCommandGroup):
    """Configure the settings of a web application firewall.

    These commands are only applicable to application gateways with an SKU type of WAF. To learn more, visit https://learn.microsoft.com/en-us/azure/web-application-firewall/ag/tutorial-restrict-web-traffic-cli.
    """
    pass


__all__ = ["__CMDGroup"]