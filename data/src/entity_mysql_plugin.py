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

class EntityMysqlPlugin(colony.base.system.Plugin):
    """
    The main class for the Entity Mysql plugin.
    """

    id = "pt.hive.colony.plugins.data.entity.mysql"
    name = "Entity Mysql"
    description = "The plugin that manages the mysql adaptation structures for the entity manager"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    capabilities = [
        "entity_engine"
    ]
    dependencies = [
        colony.base.system.PackageDependency("MySQL-Python extension module", "MySQLdb", "1.x.x", "http://mysql-python.sourceforge.net")
    ]
    main_modules = [
        "data.entity_mysql.system"
    ]

    entity_mysql = None
    """ The entity mysql """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import data.entity_mysql.system
        self.entity_mysql = data.entity_mysql.system.EntityMysql(self)

    def get_engine_name(self):
        return self.entity_mysql.get_engine_name()

    def get_internal_version(self):
        return self.entity_mysql.get_internal_version()

    def create_engine(self, entity_manager):
        return self.entity_mysql.create_engine(entity_manager)
