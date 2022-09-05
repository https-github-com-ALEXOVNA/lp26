INFO:root:Bot launched
INFO:apscheduler.scheduler:Scheduler started
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:telegram.ext.updater:Received signal 2 (SIGINT), stopping...
INFO:apscheduler.scheduler:Scheduler has been shut down
INFO:root:Bot launched
INFO:apscheduler.scheduler:Scheduler started
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:root:Bot launched
INFO:apscheduler.scheduler:Scheduler started
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:telegram.ext.updater:Received signal 2 (SIGINT), stopping...
INFO:apscheduler.scheduler:Scheduler has been shut down
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:root:Bot launched
INFO:apscheduler.scheduler:Scheduler started
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:telegram.ext.updater:Received signal 2 (SIGINT), stopping...
INFO:apscheduler.scheduler:Scheduler has been shut down
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:root:Bot launched
INFO:apscheduler.scheduler:Scheduler started
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 283, in _request_wrapper
    raise Conflict(message)
telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
INFO:telegram.ext.updater:Received signal 2 (SIGINT), stopping...
INFO:apscheduler.scheduler:Scheduler has been shut down
ERROR:telegram.ext.updater:Error while getting Updates: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=2, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104984c10>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104984e80>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985090>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
ERROR:telegram.ext.updater:Error while getting Updates: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049851e0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 140, in _new_conn
    conn = connection.create_connection(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 360, in _make_request
    self._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 857, in _validate_conn
    super(HTTPSConnectionPool, self)._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 289, in _validate_conn
    conn.connect()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 284, in connect
    conn = self._new_conn()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 149, in _new_conn
    raise NewConnectionError(
telegram.vendor.ptb_urllib3.urllib3.exceptions.NewConnectionError: <telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049851e0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 259, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/retry.py", line 376, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
telegram.vendor.ptb_urllib3.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049851e0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 265, in _request_wrapper
    raise NetworkError(f'urllib3 HTTPError {error}') from error
telegram.error.NetworkError: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049851e0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=2, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104984040>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104984be0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985360>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
ERROR:telegram.ext.updater:Error while getting Updates: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049854b0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 140, in _new_conn
    conn = connection.create_connection(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 360, in _make_request
    self._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 857, in _validate_conn
    super(HTTPSConnectionPool, self)._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 289, in _validate_conn
    conn.connect()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 284, in connect
    conn = self._new_conn()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 149, in _new_conn
    raise NewConnectionError(
telegram.vendor.ptb_urllib3.urllib3.exceptions.NewConnectionError: <telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049854b0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 259, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/retry.py", line 376, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
telegram.vendor.ptb_urllib3.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049854b0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 265, in _request_wrapper
    raise NetworkError(f'urllib3 HTTPError {error}') from error
telegram.error.NetworkError: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049854b0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=2, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104984130>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985660>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x1049857b0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
ERROR:telegram.ext.updater:Error while getting Updates: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985900>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 140, in _new_conn
    conn = connection.create_connection(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 360, in _make_request
    self._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 857, in _validate_conn
    super(HTTPSConnectionPool, self)._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 289, in _validate_conn
    conn.connect()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 284, in connect
    conn = self._new_conn()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 149, in _new_conn
    raise NewConnectionError(
telegram.vendor.ptb_urllib3.urllib3.exceptions.NewConnectionError: <telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985900>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 259, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/retry.py", line 376, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
telegram.vendor.ptb_urllib3.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985900>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 265, in _request_wrapper
    raise NetworkError(f'urllib3 HTTPError {error}') from error
telegram.error.NetworkError: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985900>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=2, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985570>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=1, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985ae0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
WARNING:telegram.vendor.ptb_urllib3.urllib3.connectionpool:Retrying (Retry(total=0, connect=None, read=None, redirect=None)) after connection broken by 'NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985c60>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates
ERROR:telegram.ext.updater:Error while getting Updates: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985de0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
ERROR:telegram.ext.dispatcher:No error handlers are registered, logging exception.
Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 140, in _new_conn
    conn = connection.create_connection(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/socket.py", line 955, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 614, in urlopen
    httplib_response = self._make_request(conn, method, url,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 360, in _make_request
    self._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 857, in _validate_conn
    super(HTTPSConnectionPool, self)._validate_conn(conn)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 289, in _validate_conn
    conn.connect()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 284, in connect
    conn = self._new_conn()
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connection.py", line 149, in _new_conn
    raise NewConnectionError(
telegram.vendor.ptb_urllib3.urllib3.exceptions.NewConnectionError: <telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985de0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 259, in _request_wrapper
    resp = self._con_pool.request(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 68, in request
    return self.request_encode_body(method, url, fields=fields,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/request.py", line 148, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/poolmanager.py", line 244, in urlopen
    response = conn.urlopen(method, u.request_uri, **kw)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 691, in urlopen
    return self.urlopen(method, url, body, headers, retries,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/connectionpool.py", line 665, in urlopen
    retries = retries.increment(method, url, error=e, _pool=self,
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/vendor/ptb_urllib3/urllib3/util/retry.py", line 376, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
telegram.vendor.ptb_urllib3.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985de0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 651, in _network_loop_retry
    if not action_cb():
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/updater.py", line 602, in polling_action_cb
    updates = self.bot.get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/ext/extbot.py", line 226, in get_updates
    updates = super().get_updates(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 133, in decorator
    result = func(*args, **kwargs)
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 3057, in get_updates
    self._post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/bot.py", line 298, in _post
    return self.request.post(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 361, in post
    result = self._request_wrapper(
  File "/Users/alexovna.mac/Documents/lp26_main/venv/lib/python3.10/site-packages/telegram/utils/request.py", line 265, in _request_wrapper
    raise NetworkError(f'urllib3 HTTPError {error}') from error
telegram.error.NetworkError: urllib3 HTTPError HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url: /bot5519145724:AAHT7lixHUTwjBebiejGjr8Ur28doHX9grY/getUpdates (Caused by NewConnectionError('<telegram.vendor.ptb_urllib3.urllib3.connection.VerifiedHTTPSConnection object at 0x104985de0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))
INFO:telegram.ext.updater:Received signal 15 (SIGTERM), stopping...
INFO:apscheduler.scheduler:Scheduler has been shut down
