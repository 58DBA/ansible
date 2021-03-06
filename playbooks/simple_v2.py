#!/usr/bin/env python
# coding=utf-8

#!/usr/bin/env python
# coding=utf-8
import ansible.playbook
from ansible import callbacks
from ansible import utils
import json
stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats,verbose=utils.VERBOSITY)
res=ansible.playbook.PlayBook(
            playbook='replset_test.yml',
            stats=stats,
            callbacks=playbook_cb,
            runner_callbacks=runner_cb
    ).run()
data = json.dumps(res,indent=4)
