#!/usr/bin/python
# -*- coding: Cp1252 -*-

# Hive Colony Framework
# Copyright (C) 2008 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "Jo�o Magalh�es <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 72 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-10-21 23:29:54 +0100 (Tue, 21 Oct 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

HELPER_NAME = "xmlrpc"
""" The helper name """

HTTP_PROTOCOL_PREFIX = "HTTP://"
""" The httpd protocol prefix """

class DistributionXmlrpcHelper:
    """
    The distribution xmlrpc helper class.
    """

    distribution_xmlrpc_helper_plugin = None
    """ The distribution xmlrpc helper plugin """

    def __init__(self, distribution_xmlrpc_helper_plugin):
        """
        Constructor of the class.
        
        @type distribution_xmlrpc_helper_plugin: DistributionXmlrpcHelperPlugin
        @param distribution_xmlrpc_helper_plugin: The distribution xmlrpc helper plugin.
        """

        self.distribution_xmlrpc_helper_plugin = distribution_xmlrpc_helper_plugin

    def get_helper_name(self):
        return HELPER_NAME

    def create_client(self, remote_reference):
        """
        Creates a xmlrpc remote client from a remote reference.
        
        @type remote_reference: RemoteReference
        @param remote_reference: The remote reference to retrieve the xmlrpc remote client.
        @rtype: XmlrpcRemoteClient
        @return: The xmlrpc remote client retrieved from a remote reference.
        """

        # retrieves the main xmlrpc client plugin
        main_xmlrpc_client_plugin = self.distribution_xmlrpc_helper_plugin.main_xmlrpc_client_plugin

        # retrieves the remote reference hostname
        hostname = remote_reference.hostname

        # retrieves the remote reference port
        port = remote_reference.port

        # retrieves the remote reference properties list
        properties_list = remote_reference.properties_list

        # retrieves the xmlrpc handler base filename
        xmlrpc_handler_base_filename = properties_list[0]

        # retrieves the xmlrpc handler extension
        xmlrpc_handler_extension = properties_list[1]

        # creates the xmlrpc server address
        xmlrpc_server_address = HTTP_PROTOCOL_PREFIX + hostname + ":" + str(port) + "/" + xmlrpc_handler_base_filename + "." + xmlrpc_handler_extension

        # creates the xmlrpc remote client
        xmlrpc_remote_client = main_xmlrpc_client_plugin.create_remote_client({"xmlrpc_server_address" : xmlrpc_server_address})

        # creates the xmlrpc remote client proxy
        xmlrpc_remote_client_proxy = XmlrpcClientProxy(xmlrpc_remote_client, remote_reference)

        # returns the xmlrpc remote client proxy
        return xmlrpc_remote_client_proxy

class XmlrpcClientProxy:
    """
    The xmlrpc client proxy class.
    """

    xmlrpc_client = None
    """ The xmlrpc client """

    remote_reference = None
    """ The remote reference """

    def __init__(self, xmlrpc_client = None, remote_reference = None):
        """
        Constructor of the class.
        
        @type xmlrpc_client: XmlrpcClient
        @param xmlrpc_client: The xmlrpc client.
        @type remote_reference: RemoteReference
        @param remote_reference: The xmlrpc remote reference.
        """

        self.xmlrpc_client = xmlrpc_client
        self.remote_reference = remote_reference

    def __nonzero__(self):
        return True

    def __getattr__(self, name):
        if hasattr(self.xmlrpc_client, name):
            return getattr(self.xmlrpc_client, name)

        raise AttributeError()
