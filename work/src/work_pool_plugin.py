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
import colony.base.decorators

class WorkPoolPlugin(colony.base.system.Plugin):
    """
    The main class for the Work Pool plugin
    """

    id = "pt.hive.colony.plugins.work.pool"
    name = "Work Pool"
    description = "Work Pool Plugin"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT,
        colony.base.system.JYTHON_ENVIRONMENT,
        colony.base.system.IRON_PYTHON_ENVIRONMENT
    ]
    capabilities = [
        "work_pool",
        "system_information"
    ]
    dependencies = [
        colony.base.system.PluginDependency("pt.hive.colony.plugins.threads.pool", "1.x.x")
    ]
    main_modules = [
        "work.pool.algorithms",
        "work.pool.exceptions",
        "work.pool.system"
    ]

    work_pool = None
    """ The work pool """

    thread_pool_plugin = None
    """ The thread pool plugin """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import work.pool.system
        self.work_pool = work.pool.system.WorkPool(self)

    def unload_plugin(self):
        colony.base.system.Plugin.unload_plugin(self)
        self.work_pool.unload()

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.system.Plugin.dependency_injected(self, plugin)

    def create_new_work_pool(self, name, description, work_processing_task_class, work_processing_task_arguments, number_threads, scheduling_algorithm, maximum_number_threads, maximum_number_works_thread, work_scheduling_algorithm):
        return self.work_pool.create_new_work_pool(
            name,
            description,
            work_processing_task_class,
            work_processing_task_arguments,
            number_threads,
            scheduling_algorithm,
            maximum_number_threads,
            maximum_number_works_thread,
            work_scheduling_algorithm
        )

    def get_system_information(self):
        """
        Retrieves the system information map, containing structured
        information to be visible using presentation viewers.

        @rtype: Dictionary
        @return: The system information map.
        """

        return self.work_pool.get_system_information()

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.threads.pool")
    def set_thread_pool_plugin(self, thread_pool_plugin):
        self.thread_pool_plugin = thread_pool_plugin
