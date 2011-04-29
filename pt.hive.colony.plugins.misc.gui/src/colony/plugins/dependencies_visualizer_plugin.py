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

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.base.plugin_system
import colony.base.decorators

class DependenciesVisualizerPlugin(colony.base.plugin_system.Plugin):
    """
    The main class for the Dependencies Visualizer plugin
    """

    id = "pt.hive.colony.plugins.misc.gui.dependencies_visualizer"
    name = "Dependencies Visualizer Plugin"
    short_name = "Dependencies Visualizer"
    description = "Dependencies Visualizer Plugin"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.plugin_system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.plugin_system.CPYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/misc_gui/dependencies_visualizer/resources/baf.xml"
    }
    capabilities = [
        "gui_panel",
        "build_automation_item"
    ]
    dependencies = [
        colony.base.plugin_system.PluginDependency("pt.hive.colony.plugins.misc.dependencies_calculator", "1.0.0"),
        colony.base.plugin_system.PackageDependency("Wx Python", "wx", "2.8.7.x", "http://wxpython.org")
    ]
    main_modules = [
        "misc_gui.dependencies_visualizer.dependencies_visualizer_system"
    ]

    dependencies_visualizer = None
    """ The dependencies visualizer """

    dependencies_calculator_plugin = None
    """ The dependencies calculator plugin """

    def load_plugin(self):
        colony.base.plugin_system.Plugin.load_plugin(self)
        global misc_gui
        import misc_gui.dependencies_visualizer.dependencies_visualizer_system
        self.dependencies_visualizer = misc_gui.dependencies_visualizer.dependencies_visualizer_system.DependenciesVisualizer(self)

    def end_load_plugin(self):
        colony.base.plugin_system.Plugin.end_load_plugin(self)

    def unload_plugin(self):
        colony.base.plugin_system.Plugin.unload_plugin(self)

    def end_unload_plugin(self):
        colony.base.plugin_system.Plugin.end_unload_plugin(self)

    def load_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.load_allowed(self, plugin, capability)

    def unload_allowed(self, plugin, capability):
        colony.base.plugin_system.Plugin.unload_allowed(self, plugin, capability)

    @colony.base.decorators.inject_dependencies("pt.hive.colony.plugins.misc.gui.dependencies_visualizer", "1.0.0")
    def dependency_injected(self, plugin):
        colony.base.plugin_system.Plugin.dependency_injected(self, plugin)

    def do_panel(self, parent):
        return self.dependencies_visualizer.do_panel(parent)

    def get_dependencies_calculator_plugin(self):
        return self.dependencies_calculator_plugin

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.misc.dependencies_calculator")
    def set_dependencies_calculator_plugin(self, dependencies_calculator_plugin):
        self.dependencies_calculator_plugin = dependencies_calculator_plugin
