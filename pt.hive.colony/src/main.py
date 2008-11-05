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

import getopt
import sys

import colony.plugins.plugin_system
import colony.plugins.util

USAGE = "Help:\n\
--help[-h] - prints this message\n\
--verbose[-v] - starts the program in verbose mode\n\
--debug[-d] - starts the program in debug mode\n\
--plugin-dir[-p]=(PLUGIN_DIR_1;PLUGIN_DIR_2;...) - sets the series of plugin directories to use"
""" The usage string for the command line arguments """

def usage():
    """
    Prints the usage for the command line
    """

    print USAGE

def run(plugin_path, verbose = False, debug = False, noloop = False):
    """
    Starts the loading of the plugin manager
    
    @type plugin_path: String
    @param plugin_path: The set of paths to the various plugin locations separated by a semi-column
    @type verbose: bool
    @param verbose: If the log is going to be of type verbose
    @type debug: bool
    @param debug: If the log is going to be of type debug
    @type noloop: bool
    @param noloop: If the plugin manager is going to run in a loop
    """

    # checks if the path is not empty
    if plugin_path != None:
        plugin_paths = plugin_path.split(";")
    else:
        plugin_paths = []

    # sets the plugin manager as a global variable
    global plugin_manager

    # retrieves the current executing platform
    platform = colony.plugins.util.get_environment()

    # creates the plugin manager with the given plugin paths
    plugin_manager = colony.plugins.plugin_system.PluginManager(plugin_paths, platform, [], not noloop)

    # conditional logging import (depending on the current environment)
    if platform == colony.plugins.util.CPYTHON_ENVIRONMENT:
        import logging
    elif platform == colony.plugins.util.JYTHON_ENVIRONMENT:
        import colony.plugins.dummy_logging as logging
    elif platform == colony.plugins.util.IRON_PYTHON_ENVIRONMENT:
        import colony.plugins.dummy_logging as logging

    # sets the logging level for the plugin manager logger
    if debug:
        plugin_manager.start_logger(logging.DEBUG)
    elif verbose:
        plugin_manager.start_logger(logging.INFO)
    else:
        plugin_manager.start_logger(logging.WARN)

    # starts and loads the plugin system
    plugin_manager.load_system()

def main():
    """
    The main entry point of the application
    """

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvdnm:p:", ["help", "verbose", "debug", "noloop", "manager_dir=", "plugin_dir="])
    except getopt.GetoptError, err:
        # prints help information and exit
        # will print something like "option -a not recognized"
        print str(err)
        usage()
        sys.exit(2)
    verbose = False
    debug = False
    noloop = False
    manager_path = None
    plugin_path = None
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ("-v", "--verbose"):
            verbose = True
        elif option in ("-d", "--debug"):
            debug = True
        elif option in ("-n", "--noloop"):
            noloop = True
        elif option in ("-m", "--manager_dir"):
            manager_path = value
        elif option in ("-p", "--plugin_dir"):
            plugin_path = value
        else:
            assert False, "unhandled option"

    # sets the prefix path for the plugins
    if manager_path:
        prefix_path = manager_path + "/../../"
    else:
        prefix_path = "../../"

    # creates the plugin path
    plugin_path = prefix_path + "pt.hive.colony.plugins.adapters.input/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.adapters.input.handlers/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.adapters.output/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.adapters.output.handlers/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.build.automation/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.build.automation.extensions/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.build.automation.items/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.business/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.document/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.configuration.startup/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.dummy/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.gui.diamante/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.io/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.javascript.file_handler/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.javascript.handlers/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.javascript.manager/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.access/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.console/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.gui/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.log/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.logic/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.mod_python/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.remote/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.remote.jsonrpc/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.remote.soap/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.remote.xmlrpc/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.restricted/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.test/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.tasks/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.main.threads/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.messaging/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.misc/src/colony/plugins;"  +\
    prefix_path + "pt.hive.colony.plugins.misc.gui/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.prototype.business/src/colony/plugins;" +\
    prefix_path + "pt.hive.colony.plugins.system.updater/src/colony/plugins;" +\
    prefix_path + "pt.hive.omni.plugins.eureka/src/omni/plugins;" +\
    prefix_path + "pt.hive.omni.plugins.eureka.mocks/src/omni/plugins"

    # starts the running process
    run(plugin_path, verbose, debug, noloop)

if __name__ == "__main__":
    main()
