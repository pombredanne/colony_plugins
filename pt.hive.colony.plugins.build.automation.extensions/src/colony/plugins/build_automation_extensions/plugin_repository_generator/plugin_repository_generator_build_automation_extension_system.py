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

__date__ = "$LastChangedDate: 2008-10-21 23:29:54 +0100 (Ter, 21 Out 2008) $"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os

import colony.libs.path_util

TARGET_DIRECTORY_VALUE = "target_directory"
""" The target directory value """

BUNDLES_DIRECTORY_VALUE = "bundles_directory"
""" The bundles directory value """

PLUGINS_DIRECTORY_VALUE = "plugins_directory"
""" The plugins directory value """

LIBRARIES_DIRECTORY_VALUE = "libraries_directory"
""" The libraries directory value """

TARGET_VALUE = "target"
""" The target value """

REPOSITORY_NAME_VALUE= "repository_name"
""" The repository name value """

REPOSITORY_DESCRIPTION = "repository_description"
""" The repository description value """

REPOSITORY_LAYOUT = "repository_layout"
""" The repository layout value """

PACKED_BUNDLES_VALUE = "packed_bundles"
""" The packed bundles value """

PACKED_PLUGINS_VALUE = "packed_plugins"
""" The packed plugins value """

PACKED_LIBRARIES_VALUE = "packed_libraries"
""" The packed libraries value """

BUNDLE_EXTENSION_VALUE = ".cbx"
""" The bundle extension value """

PLUGIN_EXTENSION_VALUE = ".cpx"
""" The plugin extension value """

LIBRARY_EXTENSION_VALUE = ".clx"
""" The library extension value """

class PluginRepositoryGeneratorBuildAutomationExtension:
    """
    The plugin repository generator build automation extension class.
    """

    plugin_repository_generator_build_automation_extension_plugin = None
    """ The plugin repository generator build automation extension plugin """

    def __init__(self, plugin_repository_generator_build_automation_extension_plugin):
        """
        Constructor of the class.

        @type plugin_repository_generator_build_automation_extension_plugin: PluginRepositoryGeneratorBuildAutomationExtensionPlugin
        @param plugin_repository_generator_build_automation_extension_plugin: The plugin repository generator build automation extension plugin.
        """

        self.plugin_repository_generator_build_automation_extension_plugin = plugin_repository_generator_build_automation_extension_plugin

    def run_automation(self, plugin, stage, parameters, build_automation_structure, logger):
        # retrieves the repository descriptor generator plugin
        repository_descriptor_generator_plugin = self.plugin_repository_generator_build_automation_extension_plugin.repository_descriptor_generator_plugin

        # retrieves the build automation structure runtime
        build_automation_structure_runtime = build_automation_structure.runtime

        # retrieves the build properties
        build_properties = build_automation_structure.get_all_build_properties()

        # retrieves the target directory
        target_directory = build_properties[TARGET_DIRECTORY_VALUE]

        # retrieves the bundles directory
        bundles_directory = build_properties[BUNDLES_DIRECTORY_VALUE]

        # retrieves the plugins directory
        plugins_directory = build_properties[PLUGINS_DIRECTORY_VALUE]

        # retrieves the libraries directory
        libraries_directory = build_properties[LIBRARIES_DIRECTORY_VALUE]

        # retrieves the repository name
        repository_name = parameters[REPOSITORY_NAME_VALUE]

        # retrieves the repository description
        repository_description = parameters[REPOSITORY_DESCRIPTION]

        # retrieves the repository layout
        repository_layout = parameters[REPOSITORY_LAYOUT]

        # retrieves the packed bundles, plugins and libraries from
        # the build automation structure runtime
        packed_bundles = build_automation_structure_runtime.properties.get(PACKED_BUNDLES_VALUE, [])
        packed_plugins = build_automation_structure_runtime.properties.get(PACKED_PLUGINS_VALUE, [])
        packed_libraries = build_automation_structure_runtime.properties.get(PACKED_LIBRARIES_VALUE, [])

        # retrieves the target
        target = parameters.get(TARGET_VALUE, target_directory)

        # creates the full target directory appending the colony plugins
        # suffix value
        full_target_directory = target + "/colony"

        # in case the full target directory does not exist
        if not os.path.exists(full_target_directory):
            # cretes the full target directory
            os.makedirs(full_target_directory)

        # creates the repository descriptor file path
        repository_descriptor_file_path = full_target_directory + "/repository_descriptor.xml"

        # generates the repository descriptor file
        repository_descriptor_generator_plugin.generate_repository_descriptor_file(repository_descriptor_file_path, repository_name, repository_description, repository_layout)

        # processes the bundles copying them to the repository directory
        self._process_bundles(packed_bundles, bundles_directory, full_target_directory)

        # processes the plugins copying them to the repository directory
        self._process_plugins(packed_plugins, plugins_directory, full_target_directory)

        # processes the libraries copying them to the repository directory
        self._process_libraries(packed_libraries, libraries_directory, full_target_directory)

        # returns true (success)
        return True

    def _process_bundles(self, packed_bundles, bundles_directory, full_target_directory):
        # creates the full bundles directory
        full_bundles_directory = full_target_directory + "/bundles"

        # in case the full bundles directory does not exist
        if not os.path.exists(full_bundles_directory):
            # creates the full bundles directory
            os.makedirs(full_bundles_directory)

        # iterates over all the packed bundles to copy the files
        for packed_bundle in packed_bundles:
            # installs (deploy) the bundle to the target path
            self._deploy_packed_item(packed_bundle, BUNDLE_EXTENSION_VALUE, bundles_directory, full_target_directory)

    def _process_plugins(self, packed_plugins, plugins_directory, full_target_directory):
        # creates the full plugins directory
        full_plugins_directory = full_target_directory + "/plugins"

        # in case the full plugins directory does not exist
        if not os.path.exists(full_plugins_directory):
            # creates the full plugins directory
            os.makedirs(full_plugins_directory)

        # iterates over all the packed plugins to copy the files
        for packed_plugin in packed_plugins:
            # installs (deploy) the plugin to the target path
            self._deploy_packed_item(packed_plugin, PLUGIN_EXTENSION_VALUE, plugins_directory, full_target_directory)

    def _process_libraries(self, packed_libraries, libraries_directory, full_target_directory):
        # creates the full libraries directory
        full_libraries_directory = full_target_directory + "/libraries"

        # in case the full libraries directory does not exist
        if not os.path.exists(full_libraries_directory):
            # creates the full libraries directory
            os.makedirs(full_libraries_directory)

        # iterates over all the packed libraries to copy the files
        for packed_library in packed_libraries:
            # installs (deploy) the library to the target path
            self._deploy_packed_item(packed_library, LIBRARY_EXTENSION_VALUE, libraries_directory, full_target_directory)

    def _deploy_packed_item(self, packed_item, packed_item_extension, packed_item_directoy, full_packed_item_directory):
        # retrieves the packed item id and version
        packed_item_id = packed_item["id"]
        packed_item_version = packed_item["version"]

        # creates the packed item file name from the packed item id and version
        packed_item_file_name = packed_item_id + "_" + packed_item_version + packed_item_extension

        # creates the packed item file paths
        packed_item_file_path = packed_item_directoy + "/" + packed_item_file_name
        packed_item_target_file_path = full_packed_item_directory + "/" + packed_item_file_name

        # in case the source packed item path does not exists
        if not os.path.exists(packed_item_file_path):
            # continues the loop
            continue

        # copies the packed item file from the packed item directory to the repository directory
        colony.libs.path_util.copy_file(packed_item_file_path, packed_item_target_file_path)
