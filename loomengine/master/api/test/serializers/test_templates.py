from rest_framework.test import RequestsClient
import datetime
from django.test import TestCase, TransactionTestCase, override_settings
import loomengine.utils.helper

from . import fixtures
import fixtures.run_fixtures.many_steps.generator
from api.serializers.templates import *


def wait_for_template_postprocessing(template):
    TIMEOUT = 120 # seconds
    INTERVAL = 1 # seconds
    loomengine.utils.helper.wait_for_true(
        lambda: Template.objects.get(id=template.id).saving_status=='ready',
        timeout_seconds=TIMEOUT,
        sleep_interval=INTERVAL)
    loomengine.utils.helper.wait_for_true(
        lambda: all([step.saving_status=='ready' for step in Template.objects.get(id=template.id).workflow.steps.all()]),
        timeout_seconds=TIMEOUT,
        sleep_interval=INTERVAL)
    return Template.objects.get(id=template.id)

@override_settings(TEST_DISABLE_TASK_DELAY=True)
class TestFixedStepInputSerializer(TestCase):

    def testCreate(self):
        step = Step(command='test command')
        step.save()

        s = FixedStepInputSerializer(
            data=fixtures.templates.fixed_step_input,
            context={'parent_field': 'step',
                     'parent_instance': step})
        s.is_valid(raise_exception=True)
        fixed_input = s.save()

        self.assertEqual(
            fixed_input.data_root.data_object.substitution_value,
            fixtures.templates.fixed_step_input['data']['contents'])


    def testRender(self):
        step = Step(command='test command')
        step.save()

        s = FixedStepInputSerializer(
            data=fixtures.templates.fixed_step_input,
            context={'parent_field': 'step',
                     'parent_instance': step})
        s.is_valid(raise_exception=True)
        fixed_input = s.save()

        s2 = FixedStepInputSerializer(fixed_input)
        self.assertEqual(s2.data['data'].keys(),
                         ['uuid'])
        

@override_settings(TEST_DISABLE_TASK_DELAY=True)
class TestStepSerializer(TransactionTestCase):

    def testCreate(self):
        with self.settings(TEST_DISABLE_TASK_DELAY=True,
                           WORKER_TYPE='MOCK'):
            s = StepSerializer(data=fixtures.templates.step_a)
            s.is_valid()
            m = s.save()

        self.assertEqual(m.command, fixtures.templates.step_a['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.step_a['fixed_inputs'][0]['data']['contents'])

    def testRender(self):
        with self.settings(TEST_DISABLE_TASK_DELAY=True,
                           WORKER_TYPE='MOCK'):
            s = StepSerializer(data=fixtures.templates.step_a)
            s.is_valid()
            m = s.save()

        self.assertEqual(m.command, s.data['command'])


@override_settings(TEST_DISABLE_TASK_DELAY=True)
class TestWorkflowSerializer(TransactionTestCase):

    @classmethod
    def isWorkflowReady(cls, workflow_id):
        return Workflow.objects.get(id=workflow_id).saving_status == 'ready'

    def testCreateFlatWorkflow(self):
        s = WorkflowSerializer(data=fixtures.templates.flat_workflow)
        s.is_valid()
        m = s.save()

        self.assertEqual(
            m.steps.first().step.command,
            fixtures.templates.flat_workflow['steps'][0]['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.flat_workflow['fixed_inputs'][0]['data']['contents'])

    def testCreateNestedWorkflow(self):
        s = WorkflowSerializer(data=fixtures.templates.nested_workflow)
        s.is_valid()
        m = s.save()

        self.assertEqual(
            m.steps.first().workflow.steps.first().step.command,
            fixtures.templates.nested_workflow[
                'steps'][0]['steps'][0]['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.nested_workflow['fixed_inputs'][0]['data']['contents'])

    def testRender(self):
        s = WorkflowSerializer(data=fixtures.templates.nested_workflow)
        s.is_valid()
        m = s.save()

        self.assertEqual(s.data['name'], 'nested')

@override_settings(TEST_DISABLE_TASK_DELAY=True)
class TestTemplateSerializer(TransactionTestCase):

    def testCreateStep(self):
        with self.settings(TEST_DISABLE_TASK_DELAY=True,
                           WORKER_TYPE='MOCK'):
            s = TemplateSerializer(data=fixtures.templates.step_a)
            s.is_valid()
            m = s.save()

        self.assertEqual(m.step.command, fixtures.templates.step_a['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.step_a['fixed_inputs'][0]['data']['contents'])

    def testCreateFlatWorkflow(self):
        with self.settings(TEST_DISABLE_TASK_DELAY=True,
                           WORKER_TYPE='MOCK'):
            s = TemplateSerializer(data=fixtures.templates.flat_workflow)
            s.is_valid()
            m = s.save()

        self.assertEqual(
            m.steps.first().step.command, 
            fixtures.templates.flat_workflow['steps'][0]['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.flat_workflow['fixed_inputs'][0]['data']['contents'])

    def testCreateNestedWorkflow(self):
        with self.settings(TEST_DISABLE_TASK_DELAY=True,
                           WORKER_TYPE='MOCK'):
            s = TemplateSerializer(data=fixtures.templates.nested_workflow)
            s.is_valid()
            m = s.save()

        self.assertEqual(
            m.steps.first().workflow.steps.first().step.command,
            fixtures.templates.nested_workflow[
                'steps'][0]['steps'][0]['command'])
        self.assertEqual(
            m.fixed_inputs.first().data_root.data_object.substitution_value,
            fixtures.templates.nested_workflow['fixed_inputs'][0]['data']['contents'])

    def testRender(self):
        s = TemplateSerializer(data=fixtures.templates.nested_workflow)
        s.is_valid()
        m = s.save()

        s2 = TemplateSerializer(m)
        self.assertEqual(s2.data['name'], 'nested')

    def testCreationPostprocessing(self):

        STEP_COUNT=2
        
        data = fixtures.run_fixtures.many_steps\
                                    .generator.make_many_steps(STEP_COUNT)

        s = TemplateSerializer(data=data)
        s.is_valid(raise_exception=True)
        m = s.save()

        wait_for_template_postprocessing(m)
        self.assertTrue(m.workflow.steps.count() == STEP_COUNT+1)