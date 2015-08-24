import hashlib
import logging
import os
import requests
import subprocess

from django.conf import settings

from analysis.models import StepResult


logger = logging.getLogger('xppf')

# Location of Python in virtualenv on worker node
PYTHON_EXECUTABLE = os.path.abspath(
    os.path.join(
        settings.BASE_DIR,
        '../../../env/bin/python',
        ))

# Location of step runner on worker node
STEP_RUNNER_EXECUTABLE = os.path.abspath(
    os.path.join(
        settings.BASE_DIR,
        '../../worker/step_runner.py',
        ))

class ClusterWorkerManager:

    @classmethod
    def run(cls, step_run):
        cmd = '%s %s --run_id %s --master_url %s' % (
            PYTHON_EXECUTABLE,
            STEP_RUNNER_EXECUTABLE,
            step_run._id,
            settings.MASTER_URL,
            )
        # Retrieve resource requirements 
        if step_run.step_set.count() < 1:
            raise Exception('No step found for a step run')
        if step_run.step_set.count() > 1:
            raise Exception('More than one step found for a step run')
        step = step_run.step_set.get()
        resources = step.resources

        # Use Slurm to call the step runner on a worker node
        cmd = "echo -e '#!/bin/bash\n%s' | sbatch -n %s --mem %s" % (
            cmd,
            resources.cores,
            resources.memory
            )

        logger.debug(cmd)

        proc = subprocess.Popen(cmd, shell=True)

        #TODO save proc.pid for follow-up
