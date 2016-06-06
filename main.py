import os
import sys

from library import Workflow


def main(workflow):
    browsers = {
        'Safari': ['/Applications/Safari.app', 'safari:Safari', 'resources/safari.png'],
        'Opera': ['/Applications/Opera.app', 'opera:Opera', 'resources/opera.png'],
        'Firefox': ['/Applications/Firefox.app', 'firefox:Firefox', 'resources/firefox.png'],
        'Chromium': ['/Applications/Chromium.app', 'chromium:Chromium', 'resources/chromium.png'],
        'Google Chrome': ['/Applications/Google Chrome.app', 'google chrome:Google Chrome', 'resources/chrome.png'],
        'Google Chrome Canary': ['/Applications/Google Chrome Canary.app', 'google chrome canary:Google Chrome Canary',
                                 'resources/canary.png']
    }

    for name, attributes in browsers.items():
        if os.path.exists(attributes[0]):
            workflow.item(name, '', lambda item: customize(item, attributes[1], workflow.resource(attributes[2])))

    workflow.feedback()
    return 0


def customize(item, arg, icon):
    item.valid = 'yes'
    item.icon = icon
    item.arg = arg
    return item

if __name__ == '__main__':
    sys.exit(Workflow.run(main, Workflow()))