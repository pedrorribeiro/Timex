import asyncio
import sys
import time
import os
import fcntl


async def timex(prompt: str, timeout: int):
    timer = 0
    response = 0
    var = 0
    start = time.time()
    fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)
    await asyncio.get_event_loop().run_in_executor(
        None, lambda s=prompt: sys.stdout.write(s + '\n'))
    while timer < timeout:
        try:
            stdin = sys.stdin.read()
            response = int(stdin)
            break
        except TypeError:
            timer = time.time() - start
            pass

    if timer >= timeout:
        print('Time is up!')
        var = 5985
        return var
    else:
        return response
