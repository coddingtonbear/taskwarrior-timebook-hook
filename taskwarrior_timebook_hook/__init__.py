import json
import logging
import os
import sys
import subprocess32 as subprocess
import tempfile


logger = logging.getLogger(__name__)


def execute_command(args, call_type='call', **kwargs):
    method = getattr(subprocess, call_type)
    logger.debug("Executing subprocess: %s (%s).", args, call_type)
    value = method(args, **kwargs)
    if isinstance(value, basestring):
        value = value.strip()
    logger.debug("Subprocess returned with value: %s", value)
    return value


def set_current_task(description=''):
    returncode = execute_command([
        't',
        'change',
        description
    ])
    if returncode != 0:
        logger.warning("Not currently clocked-in; no timebook entry made.")
        print "You are not currently clocked-in"


def main(stdin):
    lines = stdin.split('\n')
    original = json.loads(lines[0])
    modified = json.loads(lines[1])
    logger.debug(
        "Timebook version: %s",
        execute_command(['t', '--version'], call_type='check_output')
    )
    logger.debug(
        "Taskwarrior version: %s",
        execute_command(['task', '--version'], call_type='check_output')
    )
    logger.debug("Original task: %s", original)
    logger.debug("Modified task: %s", modified)

    if 'start' in original and 'start' not in modified:
        # Stop tracking time to this task.
        logger.info(
            "Task %s no longer active; stopping current task.",
            original['uuid'],
        )
        set_current_task()
    elif 'start' in modified and 'start' not in original:
        # Start tracking time to this task.
        logger.info(
            "Task %s started; setting timebook entry as \"%s\".",
            original['uuid'],
            modified['description'],
        )
        set_current_task(modified['description'])

    output = json.dumps(modified, separators=(',', ':'))
    logger.debug(
        "Returning output %s to taskwarrior.",
        output,
    )
    return output


def cmdline(debug=False):
    if debug:
        logging.basicConfig(
            level=logging.DEBUG,
            filename=os.path.join(
                tempfile.gettempdir(),
                'taskwarrior_timebook_hook.log',
            )
        )
    sys.stdout.write(main(sys.stdin.read()))


def cmdline_debug():
    cmdline(debug=True)


if __name__ == '__main__':
    cmdline()
