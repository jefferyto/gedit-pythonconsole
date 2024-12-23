# -*- coding: utf-8 -*-

# plugin.py -- plugin-related data
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
gi.require_version('GLib', '2.0')
gi.require_version('Peas', '1.0')

import os.path
from gi.repository import GLib, Peas

data_dir = Peas.Engine.get_default().get_plugin_info('pythonconsole').get_data_dir()

try:
    import locale
    locale.bindtextdomain('gedit-pythonconsole', os.path.join(data_dir, 'locale'))
    locale.bind_textdomain_codeset('gedit-pythonconsole', 'UTF-8')
except:
    pass

_ = lambda s: GLib.dgettext('gedit-pythonconsole', s)

# ex:et:ts=4:
