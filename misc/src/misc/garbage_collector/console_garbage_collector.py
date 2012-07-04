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

__author__ = "João Magalhães <joamag@hive.pt> & Tiago Silva <tsilva@hive.pt>"
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

CONSOLE_EXTENSION_NAME = "garbage_collector"
""" The console extension name """

class ConsoleGarbageCollector:
    """
    The console garbage collector class.
    """

    garbage_collector_plugin = None
    """ The garbage collector plugin """

    commands_map = {}
    """ The map containing the commands information """

    def __init__(self, garbage_collector_plugin):
        """
        Constructor of the class.

        @type garbage_collector_plugin: GarbageCollectorPlugin
        @param garbage_collector_plugin: The garbage collector plugin.
        """

        self.garbage_collector_plugin = garbage_collector_plugin

        # initializes the commands map
        self.commands_map = self.__generate_commands_map()

    def get_console_extension_name(self):
        return CONSOLE_EXTENSION_NAME

    def get_commands_map(self):
        return self.commands_map

    def process_run_garbage_collector(self, arguments, arguments_map, output_method, console_context):
        """
        Processes the run garbage collector command, with the given
        arguments and output method.

        @type arguments: List
        @param arguments: The arguments for the processing.
        @type arguments_map: Dictionary
        @param arguments_map: The map of arguments for the processing.
        @type output_method: Method
        @param output_method: The output method to be used in the processing.
        @type console_context: ConsoleContext
        @param console_context: The console context for the processing.
        """

        # retrieves the garbage collector instance
        garbage_collector = self.garbage_collector_plugin.garbage_collector

        # outputs a message stating that the garbage collector has started running
        output_method("running garbage collector")

        # runs the garbage collector
        garbage_collector.run_garbage_collector()

    def __generate_commands_map(self):
        # creates the commands map
        commands_map = {
            "run_garbage_collector" : {
                "handler" : self.process_run_garbage_collector,
                "description" : "runs the python garbage collector"
            }
        }

        # returns the commands map
        return commands_map