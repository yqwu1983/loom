from analysis.models import *
from django.conf import settings
from django.test import TestCase
import os
import sys
from loom.common import fixtures
from loom.common.fixtures.workflows import hello_world
from .common import UniversalModelTestMixin


class TestWorkflowRunModels(TestCase, UniversalModelTestMixin):
    """
    def testWorkflowRun(self):
        o = WorkflowRun.create(fixtures.workflow_run_struct)
        self.assertEqual(o.inputs.first().input_name, fixtures.workflow_run_struct['inputs'][0]['input_name'])
        self.roundTripJson(o)
        self.roundTripStruct(o)
        
class TestWorkflowRunMethods(TestCase):

    def testWorkflowRunsReverseSorted(self):
        count = 5
        for i in range(count):
            WorkflowRun.create(fixtures.workflow_run_struct)
        wf_list = WorkflowRun.order_by_most_recent()
        for i in range(1, count):
            self.assertTrue(wf_list[i-1].datetime_created > wf_list[i].datetime_created)

    def testWorkflowRunNoCount(self):
        count = 5
        for i in range(count):
            WorkflowRun.create(fixtures.workflow_run_struct)
        wf_list = WorkflowRun.order_by_most_recent()
        self.assertEqual(len(wf_list), count)

    def testWorkRunRequestflowWithCount(self):
        count = 5
        for i in range(count):
            WorkflowRun.create(fixtures.workflow_run_struct)

        wf_list_full = WorkflowRun.order_by_most_recent()
        wf_list_truncated = WorkflowRun.order_by_most_recent(count-1)
        wf_list_untruncated = WorkflowRun.order_by_most_recent(count+1)

        # Truncated list should start with the newest record
        self.assertEqual(wf_list_full[0].datetime_created, wf_list_truncated[0].datetime_created)

        # Length should match count
        self.assertEqual(len(wf_list_truncated), count-1)

        # If count is greater than available elements, all elements should be present
        self.assertEqual(len(wf_list_untruncated), count)
    """
    
class TestWorkflowRunInitChannels(TestCase):

    def testInitializeWorkflow(self):
        wfrun = WorkflowRun.create(fixtures.hello_world_workflow_run_struct)
        self.assertTrue(True)