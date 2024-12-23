# -*- coding: utf-8 -*-
#
# settings.py -- settings object
#
# Copyright (C) 2024 - Jeffery To
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

# Parts from "Interactive Python-GTK Console" (stolen from epiphany's console.py)
#     Copyright (C), 1998 James Henstridge <james@daa.com.au>
#     Copyright (C), 2005 Adam Hooper <adamh@densi.com>
# Bits from gedit Python Console Plugin
#     Copyright (C), 2005 Raphaël Slinckx

import gi
gi.require_version('Gio', '2.0')

import os.path
from gi.repository import Gio
from .editor import CONSOLE_KEY_BASE
from .plugin import data_dir

def get_settings():
    schemas_directory = os.path.join(data_dir, 'schemas')
    default_schema_source = Gio.SettingsSchemaSource.get_default()

    schema_source = Gio.SettingsSchemaSource.new_from_directory(schemas_directory,
                                                                default_schema_source,
                                                                False)
    schema = schema_source.lookup(CONSOLE_KEY_BASE, True)
    return Gio.Settings.new_full(schema, None, None)

# ex:et:ts=4:
