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

__revision__ = "$LastChangedRevision: 421 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-20 15:16:53 +0000 (Qui, 20 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

WEB_MVC_PANEL_ITEM_MONITOR_RESOURCES_PATH = "web_mvc_panel_item/monitor/resources"
""" The web panel item monitor resources path """

TEMPLATES_PATH = WEB_MVC_PANEL_ITEM_MONITOR_RESOURCES_PATH + "/templates"
""" The templates path """

class WebMvcPanelItemMonitor:
    """
    The web mvc panel item monitor class.
    """

    web_mvc_panel_item_monitor_plugin = None
    """ The web mvc panel item monitor plugin """

    web_mvc_panel_item_monitor_main_controller = None
    """ The web mvc panel item monitor main controller """

    def __init__(self, web_mvc_panel_item_monitor_plugin):
        """
        Constructor of the class.

        @type web_mvc_panel_item_monitor_plugin: WebMvcPanelItemMonitorPlugin
        @param web_mvc_panel_item_monitor_plugin: The web mvc panel item monitor plugin
        """

        self.web_mvc_panel_item_monitor_plugin = web_mvc_panel_item_monitor_plugin

    def load_components(self):
        """
        Loads the main components controller, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the web mvc utils plugin
        web_mvc_utils_plugin = self.web_mvc_panel_item_monitor_plugin.web_mvc_utils_plugin

        # creates the web mvc panel item monitor main controller
        self.web_mvc_panel_item_monitor_main_controller = web_mvc_utils_plugin.create_controller(WebMvcPanelItemDidYouKnowMainController, [self.web_mvc_panel_item_monitor_plugin, self], {})

    def get_patterns(self):
        """
        Retrieves the map of regular expressions to be used as patters,
        to the web mvc service. The map should relate the route with the handler
        method/function.

        @rtype: Dictionary
        @return: The map of regular expressions to be used as patterns,
        to the web mvc service.
        """

        return {}

    def get_communication_patterns(self):
        """
        Retrieves the map of regular expressions to be used as communication patters,
        to the web mvc service. The map should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Dictionary
        @return: The map of regular expressions to be used as communication patterns,
        to the web mvc service.
        """

        return {}

    def get_resource_patterns(self):
        """
        Retrieves the map of regular expressions to be used as resource patters,
        to the web mvc service. The map should relate the route with the base
        file system path to be used.

        @rtype: Dictionary
        @return: The map of regular expressions to be used as resource patterns,
        to the web mvc service.
        """

        return {}

    def get_panel_item(self, parameters):
        return self.web_mvc_panel_item_monitor_main_controller.get_panel_item()

class WebMvcPanelItemDidYouKnowMainController:
    """
    The web mvc panel item did you knwo main controller.
    """

    web_mvc_panel_item_monitor_plugin = None
    """ The web mvc panel item monitor plugin """

    web_mvc_panel_item_monitor = None
    """ The web mvc panel item monitor """

    def __init__(self, web_mvc_panel_item_monitor_plugin, web_mvc_panel_item_monitor):
        """
        Constructor of the class.

        @type web_mvc_panel_item_monitor_plugin: WebMvcPanelItemDidYouKnowPlugin
        @param web_mvc_panel_item_monitor_plugin: The web mvc panel item monitor plugin.
        @type web_mvc_panel_item_monitor: WebMvcPanelItemDidYouKnow
        @param web_mvc_panel_item_monitor: The web mvc panel item monitor.
        """

        self.web_mvc_panel_item_monitor_plugin = web_mvc_panel_item_monitor_plugin
        self.web_mvc_panel_item_monitor = web_mvc_panel_item_monitor

    def start(self):
        """
        Method called upon structure initialization.
        """

        # retrieves the plugin manager
        plugin_manager = self.web_mvc_panel_item_monitor_plugin.manager

        # retrieves the web mvc panel item monitor plugin path
        web_mvc_panel_item_monitor_plugin_path = plugin_manager.get_plugin_path_by_id(self.web_mvc_panel_item_monitor_plugin.id)

        # creates the templates path
        templates_path = web_mvc_panel_item_monitor_plugin_path + "/" + TEMPLATES_PATH

        # sets the templates path
        self.set_templates_path(templates_path)

    def get_panel_item(self):
        # retrieves the template file
        template_file = self.retrieve_template_file("panel_item_monitor.html.tpl")

        # assigns the monitor variables
        self.__assign_monitor_variables(template_file)

        # processes the template file
        processed_template_file = self.process_template_file(template_file)

        # returns the processed template file
        return processed_template_file

    def __assign_monitor_variables(self, template_file):
        # retrieves the plugin manager
        plugin_manager = self.web_mvc_panel_item_monitor_plugin.manager

        # assigns the plugin count to the template
        template_file.assign("plugin_count", len(plugin_manager.get_all_plugins()))

        # assigns the plugin loaded count to the template
        template_file.assign("plugin_loaded_count", len(plugin_manager.get_all_loaded_plugins()))

        # assigns the capabilities count to the template
        template_file.assign("capabilities_count", len(plugin_manager.capabilities_plugins_map))

        import psutil
        import os
        import time

        pid = os.getpid()

        process = psutil.Process(pid)

        # calculates the memory usage in mega bytes
        memory_usage = process.get_memory_info()[0] / 1048576

        cpu_usage = process.get_cpu_percent()

        # assigns the memory usage to the template
        template_file.assign("memory_usage", memory_usage)

        # assigns the cpu usage to the template
        template_file.assign("cpu_usage", cpu_usage)

        # retrieves the current time
        current_time = time.time()

        uptime = current_time - plugin_manager.plugin_manager_timestamp

        uptime_string = str(int(uptime)) + "s"

        # assigns the uptime to the template
        template_file.assign("uptime", uptime_string)
