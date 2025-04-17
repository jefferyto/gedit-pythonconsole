# Python Console, a plugin for gedit, Pluma, and xed

Interactive Python console standing in the bottom panel  
<https://github.com/jefferyto/gedit-pythonconsole>  
48.2-dev

This is a fork of gedit’s Python Console plugin (from [5002633235c6]).

All bug reports, feature requests, and miscellaneous comments are
welcome at the [project issue tracker].

Be sure to watch the project on GitHub to receive notifications for new
releases.

[5002633235c6]: https://gitlab.gnome.org/World/gedit/gedit/-/tree/5002633235c6a389df1a2ae9733f5bfaefe838f9
[project issue tracker]: https://github.com/jefferyto/gedit-pythonconsole/issues

## Requirements

This plugin requires one of these text editors:

*   gedit 3.12 to 48.1
*   Pluma 1.26.0 or later
*   xed 1.4.0 or later

## Installation

1.  Download the [latest release] and extract.
2.  Copy the `pythonconsole` folder and the `pythonconsole.plugin` file
    into one of these paths (create if it does not exist):
    * gedit: `~/.local/share/gedit/plugins`
    * Pluma: `~/.local/share/pluma/plugins`
    * xed: `~/.local/share/xed/plugins`
3.  Restart the text editor, then activate the plugin in the **Plugins**
    tab of the text editor’s **Preferences** window.

[latest release]: https://github.com/jefferyto/gedit-pythonconsole/releases/latest

## Usage

See [help].

[help]: help/README.md

## License

Copyright © 2006 Steve Frécinaux  
Copyright © 2008 B. Clausius  
Copyright © 2024 Jeffery To <jeffery.to@gmail.com>

Parts from “Interactive Python-GTK Console” (stolen from epiphany’s console.py)  
    Copyright ©, 1998 James Henstridge <james@daa.com.au>  
    Copyright ©, 2005 Adam Hooper <adamh@densi.com>

Bits from gedit Python Console Plugin  
    Copyright ©, 2005 Raphaël Slinckx

Available under GNU General Public License version 2 or later

## Other plugins you may like

*   [Control Your Tabs]  
    Switch between document tabs using Ctrl+Tab and other common keyboard shortcuts

*   [Ex-Mortis] (gedit only)  
    Reopen closed windows and optionally restore windows between sessions

*   [Tab Group Salute] (gedit only)  
    Switch between tab groups using Ctrl+\<key above Tab\>

[Control Your Tabs]: https://github.com/jefferyto/gedit-control-your-tabs
[Ex-Mortis]: https://github.com/jefferyto/gedit-ex-mortis
[Tab Group Salute]: https://github.com/jefferyto/gedit-tab-group-salute
