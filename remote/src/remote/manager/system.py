#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2012 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

class RemoteManager:
    """
    The remote manager class.
    """

    remote_manager_plugin = None
    """ The remote manager plugin """

    def __init__(self, remote_manager_plugin):
        """
        Constructor of the class.

        @type remote_manager_plugin: RemoteManagerPlugin
        @param remote_manager_plugin: The remote manager plugin.
        """

        self.remote_manager_plugin = remote_manager_plugin

    def get_available_rpc_handlers(self):
        """
        Retrieves the available rpc handler.

        @rtype: List
        @return: The list of available rpc handlers.
        """

        # creates the available rpc handlers list
        available_rpc_handlers = []

        # retrieves the rpc handler plugins
        rpc_handler_plugins = self.remote_manager_plugin.rpc_handler_plugins

        # iterates over all the rpc handler plugins
        for rpc_handler_plugin in rpc_handler_plugins:
            if rpc_handler_plugin.is_active():
                available_rpc_handlers.append(rpc_handler_plugin)

        # returns the available rpc handlers list
        return available_rpc_handlers