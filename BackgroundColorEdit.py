import sublime
import sublime_plugin

import plistlib
import re
import os.path as path

class EditBackgroundColorCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().show_input_panel("New hex background color", "#", change_background_color, None, None)

class ShowBackgroundColorCommand(sublime_plugin.WindowCommand):
    def run(self):
        currentSchemePath = getCurrentSchemePath()

        if path.isfile(currentSchemePath):
            tree = plistlib.readPlist(currentSchemePath)
            sublime.active_window().status_message(
                "Current background color: " + tree['settings'][0]['settings']['background'])

        else:
            sublime.active_window().status_message("The current color scheme is not supported.")

def change_background_color(userInput):
    match = re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', userInput)

    if match:
        currentSchemePath = getCurrentSchemePath()

        if path.isfile(currentSchemePath):
            tree = plistlib.readPlist(currentSchemePath)
            tree['settings'][0]['settings']['background'] = userInput
            plistlib.writePlist(tree, currentSchemePath)

        else:
            sublime.active_window().status_message("The current color scheme is not supported.")

def getCurrentSchemePath():
    currentSchemeName = str.lstrip(
    sublime.load_settings('Preferences.sublime-settings').get('color_scheme', ''), 'Packages')

    return sublime.packages_path() + currentSchemeName