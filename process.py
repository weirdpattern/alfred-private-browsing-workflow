import os
import sys
import subprocess

from library import Workflow


def main(workflow):
    browser = parse_data(' '.join(workflow.args))
    if browser['name'] == 'safari':
        running = subprocess.Popen(['pgrep', '-x', 'Safari'], stdout=subprocess.PIPE).communicate()[0]
        if running:
            command = """
                      osascript -e 'tell application "Safari" to activate
                                    tell application "System Events"
                                        tell process "Safari" to keystroke "N" using {shift down, command down}
                                     end tell'
                      """
        else:
            command = """
                      osascript -e 'tell application "Safari" to activate
                                    tell application "System Events"
                                        tell process "Safari" to keystroke "W" using {command down}
                                        tell process "Safari" to keystroke "N" using {shift down, command down}
                                    end tell'
                      """

        os.system(command)
    else:
        subprocess.call(['open', '-n', '-a',
                         '/Applications/{0}.app'.format(browser['escaped']),
                         '--args', '--{0}'.format(browser['args'])])

    return 0


def parse_data(data):
    switcher = {
        'chromium': 'incognito',
        'google chrome': 'incognito',
        'google chrome canary': 'incognito',
        'firefox': 'private',
        'opera': 'private'
    }

    parts = data.split(':')
    return {
        'name': parts[0].lower(),
        'escaped': parts[1],
        'command': 'P' if parts[0].lower() == 'firefox' else 'N',
        'args': switcher.get(parts[0].lower(), None)
    }


if __name__ == '__main__':
    sys.exit(Workflow.run(main, Workflow()))