import sublime
import sublime_plugin

import plistlib
import re

class EditBackgroundColorCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.active_window().show_input_panel("New hex background color", "#", change_background_color, None, None)

class ShowBackgroundColorCommand(sublime_plugin.WindowCommand):
    def run(self):
        currentThemeName = str.lstrip(
            sublime.load_settings('Preferences.sublime-settings').get('color_scheme', ''), 'Packages')

        currentThemePath = sublime.packages_path() + currentThemeName

        tree = plistlib.readPlist(currentThemePath)
        sublime.active_window().status_message(
            "Current background color: " + tree['settings'][0]['settings']['background'])

def change_background_color(userInput):
    match = re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', userInput)

    if match:
        currentThemeName = str.lstrip(
            sublime.load_settings('Preferences.sublime-settings').get('color_scheme', ''), 'Packages')

        currentThemePath = sublime.packages_path() + currentThemeName

        tree = plistlib.readPlist(currentThemePath)
        tree['settings'][0]['settings']['background'] = userInput
        plistlib.writePlist(tree, currentThemePath)
