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

__author__ = "Tiago Silva <tsilva@hive.pt>"
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

RELATIVE_PATH_VALUE = "relative_path"
""" The relative path value """

RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE = "relative_destination_file_path_format"
""" The relative destination file path format """

UNIX_DIRECTORY_SEPARATOR = "/"
""" The unix directory separator """

SCAFFOLDER_TYPE = "base"
""" The scaffolder type """

TEMPLATES_PATH = "base_scaffolder/scaffolder/resources/templates"
""" The templates path """

TEMPLATES_MAP = {
    "backend/console.py.tpl" : {
        RELATIVE_PATH_VALUE : TEMPLATES_PATH,
        RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE : "${relative_backend_path}/console_${variable_name}.py"
    },
    "backend/exceptions.py.tpl" : {
        RELATIVE_PATH_VALUE : TEMPLATES_PATH,
        RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE : "${relative_backend_path}/${variable_name}_exceptions.py",
    },
    "backend/system.py.tpl" : {
       RELATIVE_PATH_VALUE : TEMPLATES_PATH,
       RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE : "${relative_backend_path}/${variable_name}_system.py",
    },
    "backend/test.py.tpl" : {
        RELATIVE_PATH_VALUE : TEMPLATES_PATH,
        RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE : "${relative_backend_path}/${variable_name}_test.py",
    },
    "plugin.py.tpl" : {
        RELATIVE_PATH_VALUE : TEMPLATES_PATH,
        RELATIVE_DESTINATION_FILE_PATH_FORMAT_VALUE : "${variable_name}_plugin.py"
    }
}
""" The templates map """

class BaseScaffolder:
    """
    The base scaffolder.
    """

    base_scaffolder_plugin = None
    """ The base scaffolder plugin """

    def __init__(self, base_scaffolder_plugin):
        """
        Constructor of the class.

        @type base_scaffolder_plugin: BaseScaffolderPlugin
        @param base_scaffolder_plugin: The base scaffolder plugin.
        """

        self.base_scaffolder_plugin = base_scaffolder_plugin

    def get_scaffolder_type(self):
        return SCAFFOLDER_TYPE

    def get_templates(self, scaffold_attributes_map):
        return TEMPLATES_MAP

    def process_scaffold_attributes(self, scaffold_attributes_map):
        pass

    def process_template(self, template_file_name, template, scaffold_attributes_map):
        return template

    def generate_scaffold(self, scaffold_path, scaffold_attributes_map):
        pass