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

__author__ = "Jo�o Magalh�es <joamag@hive.pt> & Tiago Silva <tsilva@hive.pt>"
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

class PythonConsoleInterfacePlugin(colony.base.plugin_system.Plugin):
    """
    The main class for the Python Console Interface plugin.
    """

    id = "pt.hive.colony.plugins.misc.gui.python_console_interface"
    name = "Python Console Interface Plugin"
    short_name = "Python Console Interface"
    description = "Python Console Interface Plugin"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.plugin_system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.plugin_system.CPYTHON_ENVIRONMENT
    ]
    attributes = {
        "build_automation_file_path" : "$base{plugin_directory}/misc_gui/python_console_interface/resources/baf.xml"
    }
    capabilities = [
        "gui_panel",
        "build_automation_item"
    ]
    dependencies = [
        colony.base.plugin_system.PackageDependency("Wx Python", "wx", "2.8.7.x", "http://wxpython.org")
    ]
    main_modules = [
        "misc_gui.python_console_interface.python_console_interface_system"
    ]

    python_console_interface = None
    """ The python console interface """

    def load_plugin(self):
        colony.base.plugin_system.Plugin.load_plugin(self)
        import misc_gui.python_console_interface.python_console_interface_system
        self.python_console_interface = misc_gui.python_console_interface.python_console_interface_system.PythonConsoleInterface(self)

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

    def dependency_injected(self, plugin):
        colony.base.plugin_system.Plugin.dependency_injected(self, plugin)

    def create_panel(self, parent):
        return self.python_console_interface.create_panel(parent)

    def get_icon_path(self):
        return self.python_console_interface.get_icon_path()