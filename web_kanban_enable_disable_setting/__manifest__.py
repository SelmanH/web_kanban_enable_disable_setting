# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo support
#    Copyright (C) HICHRI Selman.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Web Kanban enable/disable settings",

    'summary': """
        Kanban view grouped enable/disable setting""",

    'description': """
Add an attribute to the Kanban view group 
to enable or disable the setting displayed in the header view on hover on the title""",

    'author': "Hichri Selman",
    'category': 'Extra Tools',
    'version': '0.1',
    'depends': ['base','web_kanban'],
    'data': [
        'views/assets.xml'
    ],
    'qweb': [
        'static/src/xml/web_kanban.xml'
    ],
}