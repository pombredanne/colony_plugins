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

import colony.base.system

class SslSocketUpgraderPlugin(colony.base.system.Plugin):
    """
    The main class for the Ssl Socket Upgrader plugin.
    """

    id = "pt.hive.colony.plugins.service.ssl_socket_upgrader"
    name = "Ssl Socket Upgrader"
    description = "The plugin that offers the ssl socket upgrader"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    capabilities = [
        "socket_upgrader"
    ]
    dependencies = [
        colony.base.system.PackageDependency("Python 2.6", "ssl", "2.6.x", "http://python.org")
    ]
    main_modules = [
        "service.ssl_socket_upgrader.system"
    ]

    ssl_socket_upgrader = None
    """ The ssl socket upgrader """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import service.ssl_socket_upgrader.system
        self.ssl_socket_upgrader = service.ssl_socket_upgrader.system.SslSocketUpgrader(self)

    def get_upgrader_name(self):
        """
        Retrieves the socket upgrader name.

        @rtype: String
        @return: The socket upgrader name.
        """

        return self.ssl_socket_upgrader.get_upgrader_name()

    def upgrade_socket(self, socket):
        """
        Upgrades the given socket, configured with
        the default parameters.

        @type socket: Socket
        @param socket: The socket to be upgraded.
        @rtype: Socket
        @return: The upgraded socket.
        """

        return self.ssl_socket_upgrader.upgrade_socket(socket)

    def upgrade_socket_parameters(self, socket, parameters):
        """
        Upgrades the given socket, configured with
        the given parameters.

        @type socket: Socket
        @param socket: The socket to be upgraded.
        @type parameters: Dictionary
        @param parameters: The parameters for socket configuration.
        @rtype: Socket
        @return: The upgraded socket.
        """

        return self.ssl_socket_upgrader.upgrade_socket_parameters(socket, parameters)
