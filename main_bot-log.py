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
