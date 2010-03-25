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

__revision__ = "$LastChangedRevision: 429 $"
""" The revision number of the module """

__date__ = "$LastChangedDate: 2008-11-21 13:03:27 +0000 (Sex, 21 Nov 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.plugins.plugin_system
import colony.plugins.decorators

class JsonSpecificationGeneratorHandlerPlugin(colony.plugins.plugin_system.Plugin):
    """
    The main class for the Specification Generator plugin.
    """

    id = "pt.hive.colony.plugins.specifications.json_specification_generator_handler"
    name = "Json Specification Generator Handler Plugin"
    short_name = "Json Specification Generator Handler "
    description = "A plugin to generate json specification files"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.plugins.plugin_system.EAGER_LOADING_TYPE
    platforms = [colony.plugins.plugin_system.CPYTHON_ENVIRONMENT]
    capabilities = ["specification_generator_handler"]
    capabilities_allowed = []
    dependencies = []
    events_handled = []
    events_registrable = []
    main_modules = []

    json_specification_generator_handler = None

    def load_plugin(self):
        colony.plugins.plugin_system.Plugin.load_plugin(self)
        global specifications
        import specifications.specification_generator.specification_generator_system
        self.json_specification_generator_handler = specifications.specification_generator.specification_generator_system.SepecificationGenerator()

    def end_load_plugin(self):
        colony.plugins.plugin_system.Plugin.end_load_plugin(self)

    def unload_plugin(self):
        colony.plugins.plugin_system.Plugin.unload_plugin(self)

    def end_unload_plugin(self):
        colony.plugins.plugin_system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.plugins.plugin_system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.plugins.plugin_system.Plugin.unload_allowed(self, plugin, capability)

    def dependency_injected(self, plugin):
        colony.plugins.plugin_system.Plugin.dependency_injected(self, plugin)

    def get_specification_generator_handler_name(self):
        return self.json_specification_generator_handler.get_specification_generator_handler_name()

    def generate_plugin_specification(self, plugin, properties):
        """
        Generates a specification string describing the structure
        and specification of the given plugin.

        @type plugin: Plugin
        @param plugin: The plugin to be used to generate plugin specification.
        @type properties: Dictionary
        @param properties: The properties for plugin specification generation.
        @rtype: String
        @return: The generated plugin specification string.
        """

        self.specification_manager.generate_plugin_specification(plugin, properties)
