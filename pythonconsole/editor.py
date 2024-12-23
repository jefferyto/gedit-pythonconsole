# -*- coding: utf-8 -*-
#
# editor.py -- editor-related data
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

try:
    gi.require_version('Gedit', '3.0')
except ValueError:
    Editor = None
else:
    from gi.repository import Gedit as Editor
    name = 'gedit'
    CONSOLE_KEY_BASE = 'org.gnome.gedit.plugins.pythonconsole'
    INTERFACE_KEY_BASE = 'org.gnome.desktop.interface'

    def add_console(plugin, title):
        name = "GeditPythonConsolePanel"
        whole_bottom = plugin.window.get_template_child(Editor.Window, 'bottom_panel')
        bottom = plugin.window.get_bottom_panel()
        if bottom is not whole_bottom:
            from gi.repository import Tepl
            plugin.panel_item = Tepl.PanelItem.new(plugin._console, name, title, None, 0)
            bottom.add(plugin.panel_item)
        else: # gedit 47
            bottom.add_titled(plugin._console, name, title)

    def remove_console(plugin):
        whole_bottom = plugin.window.get_template_child(Editor.Window, 'bottom_panel')
        bottom = plugin.window.get_bottom_panel()
        if bottom is not whole_bottom:
            bottom.remove(plugin.panel_item)
            plugin.panel_item = None
        else: # gedit 47
            bottom.remove(plugin._console)

if not Editor:
    try:
        gi.require_version('Xed', '1.0')
    except ValueError:
        Editor = None
    else:
        from gi.repository import Xed as Editor
        name = 'xed'
        CONSOLE_KEY_BASE = 'org.x.editor.plugins.pythonconsole'
        INTERFACE_KEY_BASE = 'org.gnome.desktop.interface'

        def add_console(plugin, title):
            bottom = plugin.window.get_bottom_panel()
            bottom.add_item(plugin._console, title, 'text-x-script')

        def remove_console(plugin):
            bottom = plugin.window.get_bottom_panel()
            bottom.remove_item(plugin._console)

if not Editor:
    try:
        # needs to be last because Pluma is a non-private namespace
        gi.require_version('Pluma', '1.0')
    except ValueError:
        Editor = None
    else:
        from gi.repository import Pluma as Editor
        name = 'Pluma'
        CONSOLE_KEY_BASE = 'org.mate.pluma.plugins.pythonconsole'
        INTERFACE_KEY_BASE = 'org.mate.interface'

        def add_console(plugin, title):
            from gi.repository import Gtk
            bottom = plugin.window.get_bottom_panel()
            image = Gtk.Image()
            image.set_from_icon_name('text-x-script', Gtk.IconSize.MENU)
            bottom.add_item(plugin._console, title, image)

        def remove_console(plugin):
            bottom = plugin.window.get_bottom_panel()
            bottom.remove_item(plugin._console)

# ex:et:ts=4:
