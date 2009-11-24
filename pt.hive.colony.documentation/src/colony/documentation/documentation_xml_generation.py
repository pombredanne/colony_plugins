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

import cStringIO

import documentation_ast
import documentation_visitor

XML_HEADER_VALUE = "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
""" The xml header value """

class XmlGenerationVisitor(documentation_visitor.Visitor):
    """
    The xml generation visitor class.
    """

    file_buffer = None
    """ The file buffer """

    def __init__(self):
        documentation_visitor.Visitor.__init__(self)

        self.file_buffer = cStringIO.StringIO()

    def get_file_buffer(self):
        return self.file_buffer

    def set_file_buffer(self, file_buffer):
        self.file_buffer = file_buffer

    def _write_buffer(self, string_value):
        self.file_buffer.write(string_value)

    def _write_line_buffer(self, string_value):
        self._write_buffer(string_value + "\n")

    @documentation_visitor._visit(documentation_ast.AstNode)
    def visit_ast_node(self, node):
        pass

    @documentation_visitor._visit(documentation_ast.ProjectNode)
    def visit_project_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer(XML_HEADER_VALUE);
            self._write_line_buffer("<project>");
            self._write_line_buffer("<name>tobias</name>");
            self._write_line_buffer("<author>tobias</author>");
            self._write_line_buffer("<description>tobias</description>");
            self._write_line_buffer("<license>tobias</license>");
        elif self.visit_index == 1:
            self._write_line_buffer("</project>");

    @documentation_visitor._visit(documentation_ast.DocumentationElementNode)
    def visit_documentation_element_node(self, node):
        pass

    @documentation_visitor._visit(documentation_ast.NamespaceNode)
    def visit_namespace_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer("<namespace>");
        elif self.visit_index == 1:
            self._write_line_buffer("</namespace>");

    @documentation_visitor._visit(documentation_ast.ClassNode)
    def visit_class_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer("<class>");
        elif self.visit_index == 1:
            self._write_line_buffer("</class>");

    @documentation_visitor._visit(documentation_ast.FunctionNode)
    def visit_function_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer("<class>");
        elif self.visit_index == 1:
            self._write_line_buffer("</class>");

    @documentation_visitor._visit(documentation_ast.VariableNode)
    def visit_variable_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer("<variable>");
        elif self.visit_index == 1:
            self._write_line_buffer("</variable>");

    @documentation_visitor._visit(documentation_ast.ConstantNode)
    def visit_constant_node(self, node):
        if self.visit_index == 0:
            self._write_line_buffer("<constant>");
        elif self.visit_index == 1:
            self._write_line_buffer("</constant>");
