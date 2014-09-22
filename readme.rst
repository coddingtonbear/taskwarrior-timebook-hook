Taskwarrior Timebook Hook
=========================


Install using pip::

    pip install taskwarrior-timebook-hook

And add it to your Taskwarrior hooks::

    mkdir -p ~/.task/hooks
    ln -s `which taskwarrior_timebook_hook` ~/.task/hooks/on-modify.timebook

Use ``task <TASK ID> start`` and ``task <TASK ID> stop`` to record when you have
started and stopped working on tasks.

Tasks will appear in your `Timebook <https://github.com/coddingtonbear/timebook>`_
automatically.
