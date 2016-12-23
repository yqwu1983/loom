from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django import db
import multiprocessing
from api import get_setting


@shared_task
def add(x, y):
    return x + y

@shared_task
def _postprocess_workflow(workflow_id):
    from api.serializers.templates import WorkflowSerializer
    WorkflowSerializer.postprocess(workflow_id)

def postprocess_workflow(*args, **kwargs):
    if get_setting('TEST_NO_POSTPROCESS'):
        return

    if get_setting('TEST_DISABLE_TASK_DELAY'):
        _postprocess_workflow(*args, **kwargs)
        return

    # Kill connections so new process will create its own
    db.connections.close_all()
    _postprocess_workflow.delay(*args, **kwargs)

@shared_task
def _postprocess_step(step_id):
    from api.serializers.templates import StepSerializer
    StepSerializer.postprocess(step_id)

def postprocess_step(*args, **kwargs):
    if get_setting('TEST_NO_POSTPROCESS'):
        return

    if get_setting('TEST_DISABLE_TASK_DELAY'):
        _postprocess_step(*args, **kwargs)
        return

    # Kill connections so new process will create its own
    db.connections.close_all()
    _postprocess_step.delay(*args, **kwargs)

@shared_task
def _postprocess_step_run(run_id):
    from api.serializers.runs import StepRun
    StepRun.postprocess(run_id)

def postprocess_step_run(*args, **kwargs):
    if get_setting('TEST_NO_POSTPROCESS'):
        return

    if get_setting('TEST_DISABLE_TASK_DELAY'):
        _postprocess_step_run(*args, **kwargs)
        return

    # Kill connections so new process will create its own
    db.connections.close_all()
    _postprocess_step_run.delay(*args, **kwargs)

@shared_task
def _postprocess_workflow_run(run_id):
    from api.serializers.runs import WorkflowRun
    WorkflowRun.postprocess(run_id)

def postprocess_workflow_run(*args, **kwargs):
    if get_setting('TEST_NO_POSTPROCESS'):
        return

    if get_setting('TEST_DISABLE_TASK_DELAY'):
        _postprocess_workflow_run(*args, **kwargs)
        return

    # Kill connections so new process will create its own
    db.connections.close_all()
    _postprocess_workflow_run.delay(*args, **kwargs)

@shared_task
def _run_step_if_ready(step_run_id):
    from api.models import StepRun
    StepRun.run_if_ready(step_run_id)

def run_step_if_ready(*args, **kwargs):
    if get_setting('TEST_NO_AUTO_START_RUNS'):
        return

    if get_setting('TEST_DISABLE_TASK_DELAY'):
        _run_step_if_ready(*args, **kwargs)
        return

    # Kill connections so new process will create its own
    db.connections.close_all()
    _run_step_if_ready.delay(*args, **kwargs)
