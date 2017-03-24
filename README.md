# BackgroundColorEdit

Allows you to quickly and easily change only the background color of the currently active color scheme in Sublime Text 3.

Currenntly only works with color schemes installed via [Colorsublime](colorsublime.com/).

## Requirements

 - Sublime Text 3
 - Colorsublime

## Installation

### Manual

Clone this repo to your Sublime Text 'Packages' directory, which can be found via `Preferences > Browse Packages`.

### Via Package Control

*Note: Proper PackageControl support is pending approval. Here's how to add this package in the meantime.*

1. Open the command palette (`ctrl+shift+p` or `cmd+shift+p` by default)
2. Search for `Package Control: Add Repository`
3. Paste in the URL to this github repo, press enter

## Usage

1. Open the command palette (`ctrl+shift+p` or `cmd+shift+p` by default)
2. Search for `BackgroundColorEdit: Set Background Color`
3. Type a hex color code in the prompt provided and press enter to apply.
4. Alternately, search for `BackgroundColorEdit: Show Background Color` to print out the active color scheme's current background color to the status bar.

## Resetting the background color

Simply reinstall the color scheme in Colorsublime.