#!/usr/bin/python
# -*- coding: utf-8 -*-

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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision: 421 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 15:16:53 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

WEB_NANGER_RESOURCES_PATH = "web_nanger/nanger/resources"
""" The web mvc manager resources path """

EXTRAS_PATH = WEB_NANGER_RESOURCES_PATH + "/extras"
""" The extras path """

class WebNanger:
    """
    The web nanger class.
    """

    web_nanger_plugin = None
    """ The web nanger plugin """

    def __init__(self, web_nanger_plugin):
        """
        Constructor of the class.

        @type web_nanger_plugin: WebNangerPlugin
        @param web_nanger_plugin: The web nanger plugin.
        """

        self.web_nanger_plugin = web_nanger_plugin

    def load_components(self):
        """
        Loads the main components controller, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the web mvc utils plugin
        web_mvc_utils_plugin = self.web_nanger_plugin.web_mvc_utils_plugin

        # creates the controllers for the web nanger controller modules
        web_mvc_utils_plugin.create_controllers("web_nanger.nanger.web_nanger_controllers", self, self.web_nanger_plugin, "web_nanger")

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the web mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the web mvc service.
        """

        return (
            (r"^web_nanger/?$", self.web_nanger_main_controller.handle_web_nanger_index, "get"),
        )

    def get_communication_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as communication patterns,
        to the web mvc service. The tuple should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as communication patterns,
        to the web mvc service.
        """

        return ()

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the web mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the web mvc service.
        """

        # retrieves the plugin manager
        plugin_manager = self.web_nanger_plugin.manager

        # retrieves the web nanger plugin path
        web_nanger_plugin_path = plugin_manager.get_plugin_path_by_id(self.web_nanger_plugin.id)

        return (
            (r"^web_nanger/resources/.+$", (web_nanger_plugin_path + "/" + EXTRAS_PATH, "web_nanger/resources")),
        )
