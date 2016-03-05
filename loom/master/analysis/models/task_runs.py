from django.core import exceptions

from analysis.models.base import AnalysisAppInstanceModel, AnalysisAppImmutableModel
from analysis.models.task_definitions import *
from analysis.models.workflows import Step
from analysis.task_manager.dummy import DummyTaskManager
from universalmodels import fields


class TaskRun(AnalysisAppInstanceModel):
    """One instance of executing a TaskDefinition, i.e. executing a Step on a particular set
    of inputs.
    """

    # If multiple steps have the same TaskDefinition, they can share a TaskRun.
    task_definition = fields.ForeignKey('TaskDefinition', related_name='task_runs')
    task_run_inputs = fields.OneToManyField('TaskRunInput', related_name='task_run')
    task_run_outputs = fields.OneToManyField('TaskRunOutput', related_name='task_run')
    active_task_run_location = fields.ForeignKey('TaskRunLocation', null=True, related_name='active_task_run')
    task_run_locations = fields.OneToManyField('TaskRunLocation', related_name='task_run')
    status = fields.CharField(
        max_length=255,
        default='ready_to_run',
        choices=(
            ('ready_to_run', 'Ready to run'),
            ('running', 'Running'),
            ('completed', 'Completed'),
            ('canceled', 'Canceled')
        )
    )

    @classmethod
    def dummy_run_all(cls, finish=True, with_error=False):
        for task_run in TaskRun.objects.filter(status='ready_to_run'):
            task_run.dummy_run(finish=finish, with_error=with_error)

    def dummy_run(self, finish=True, with_error=False):
        task_run_location = TaskRunLocation.create({})
        self.task_run_locations.add(task_run_location)
        self.update({
            'status': 'running',
            'active_task_run_location': task_run_location.to_struct()
        })

        if finish==True:
            DummyTaskManager.run_task(self, task_run_location._id, with_error=with_error)

    def submit_result(self, output_id, data_object, task_run_location_id):
        if not self._is_location_active(task_run_location_id):
            return False # Reject result

        output = self.task_run_outputs.get(_id=output_id)
        output.add_data_object(data_object)
        return True

    def cancel(self):
        if self.active_task_run_location is not None:
            self.active_task_run_location.cancel()
        self.update({
            'status': 'canceled',
            'active_task_run_location': None
        })

    def error(self, task_run_location_id):
        if not self._is_location_active(task_run_location_id):
            return False # Reject error
        self.update({'status': 'error'})

    def _is_location_active(self, task_run_location_id):
        if self.active_task_run_location is None:
            return False
        return self.active_task_run_location._id == task_run_location_id
        
    def update_status(self):
        for output in self.task_run_outputs.all():
            if output.data_object is None:
                return
        self.update({'status': 'completed'})

        
class TaskRunInput(AnalysisAppInstanceModel):

    task_definition_input = fields.ForeignKey('TaskDefinitionInput')


class TaskRunOutput(AnalysisAppInstanceModel):

    task_definition_output = fields.ForeignKey('TaskDefinitionOutput')
    data_object = fields.ForeignKey('DataObject', null=True)

    def has_result(self):
        return self.data_object is not None

    def add_data_object(self, data_object):
        self.update({'data_object': data_object})
        # Send to any channels that are attached
        for step_run_output in self.step_run_outputs.all():
            step_run_output.channel.add_data_object(self.data_object)
    
class TaskRunLocation(AnalysisAppInstanceModel):

    def cancel(self):
        # TODO
        pass