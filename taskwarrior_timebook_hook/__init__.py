import json
import sys
import subprocess


def set_current_task(description=''):
    returncode = subprocess.call([
        't',
        'change',
        description
    ])
    if returncode != 0:
        print "You are not currently clocked-in"


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])

    if 'start' in original and 'start' not in modified:
        # Stop tracking time to this task.
        set_current_task()
    elif 'start' in modified and 'start' not in original:
        # Start tracking time to this task.
        set_current_task(modified['description'])

    return json.dumps(modified)


def cmdline():
    sys.stdout.write(main(sys.stdin.read()))


if __name__ == '__main__':
    cmdline()
