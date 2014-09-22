import json
import sys
import subprocess


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])

    if 'start' in original and 'start' not in modified:
        # Stop tracking time to this task.
        subprocess.Popen([
            't',
            'change',
        ])
    elif 'start' in modified and 'start' not in original:
        # Start tracking time to this task.
        subprocess.Popen([
            't',
            'change',
            modified['description']
        ])

    return ''


def cmdline():
    sys.stdout.write(main(sys.stdin.read()))


if __name__ == '__main__':
    cmdline()