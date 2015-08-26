#!/usr/bin/env python

from datetime import datetime
import json
import os
import requests
import subprocess
import time
import unittest
import logging

from django.conf import settings
from xppf.master.analysis.test import fixtures
from xppf.utils.testserver import TestServer
from xppf.master.analysis.worker_manager.factory import WorkerManagerFactory
from xppf.master.analysis.worker_manager.cluster import ClusterWorkerManager
from xppf.master.analysis.worker_manager.local import LocalWorkerManager
from analysis.models.work_in_progress import WorkInProgress

logger = logging.getLogger('xppf')

class TestWorkerManagers(unittest.TestCase):

    def setUp(self):
        self.test_server = TestServer()
        self.test_server.start()
	self.WORKER_TYPE_BEFORE = settings.WORKER_TYPE
	self.MASTER_URL_BEFORE = settings.MASTER_URL

    def tearDown(self):
	# Give tests some time to finish before shutting down the server. 
	time.sleep(5)

        self.test_server.stop()
	settings.WORKER_TYPE = self.WORKER_TYPE_BEFORE
	settings.MASTER_URL = self.MASTER_URL_BEFORE

    def test_local_worker_manager(self):
	settings.WORKER_TYPE = settings.LOCAL_WORKER_TYPE
	settings.MASTER_URL = settings.LOCAL_MASTER_URL
	self._run_helloworld()

    def test_cluster_worker_manager(self):
	settings.WORKER_TYPE = settings.CLUSTER_WORKER_TYPE
	settings.MASTER_URL = settings.CLUSTER_MASTER_URL
	self._run_helloworld()

    def _run_helloworld(self):
	work = WorkInProgress._get_queue_singleton()
	work.submit_new_request(fixtures.helloworld_json)
	WorkInProgress.update_and_run()

if __name__=='__main__':
    unittest.main()
