# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractFileImport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractWorkflow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractWorkflowRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CancelRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_hard_stop', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('is_closed_to_new_data', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChannelOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.ForeignKey(related_name='outputs', to='analysis.Channel', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataObject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DataObjectContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FailureNotice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_hard_stop', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FileLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000)),
                ('status', models.CharField(default=b'incomplete', max_length=256, choices=[(b'incomplete', b'Incomplete'), (b'complete', b'Complete'), (b'failed', b'Failed')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FixedStepInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('channel', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.fixedstepinput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FixedWorkflowInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('channel', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.fixedworkflowinput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InputOutputNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestedEnvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestedResourceSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memory', models.CharField(max_length=255)),
                ('disk_space', models.CharField(max_length=255)),
                ('cores', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestartRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RunRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_running', models.BooleanField(default=True)),
                ('is_stopping', models.BooleanField(default=False)),
                ('is_hard_stop', models.BooleanField(default=False)),
                ('is_failed', models.BooleanField(default=False)),
                ('is_canceled', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('channel', models.CharField(max_length=255)),
                ('hint', models.CharField(max_length=255, null=True)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.stepinput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StepOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('filename', models.CharField(max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.stepoutput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('command', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskDefinitionEnvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskDefinitionInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskDefinitionOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('task_definition', models.ForeignKey(related_name='outputs', to='analysis.TaskDefinition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRun',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resources', models.OneToOneField(to='analysis.RequestedResourceSet')),
                ('task_definition', models.OneToOneField(related_name='task_run', on_delete=django.db.models.deletion.PROTECT, to='analysis.TaskDefinition')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRunAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRunAttemptLogFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('log_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRunAttemptOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRunInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaskRunOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnnamedFileContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash_value', models.CharField(max_length=255)),
                ('hash_function', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('channel', models.CharField(max_length=255)),
                ('hint', models.CharField(max_length=255, null=True)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.workflowinput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkflowOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channel', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, choices=[(b'file', b'File'), (b'boolean', b'Boolean'), (b'string', b'String'), (b'integer', b'Integer')])),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_analysis.workflowoutput_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractStepRunInput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='BooleanContent',
            fields=[
                ('dataobjectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObjectContent')),
                ('boolean_value', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobjectcontent',),
        ),
        migrations.CreateModel(
            name='BooleanDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObject')),
                ('boolean_content', models.OneToOneField(related_name='data_object', on_delete=django.db.models.deletion.PROTECT, to='analysis.BooleanContent')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobject',),
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('dataobjectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObjectContent')),
                ('filename', models.CharField(max_length=255)),
                ('unnamed_file_content', models.ForeignKey(related_name='file_contents', on_delete=django.db.models.deletion.PROTECT, to='analysis.UnnamedFileContent')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobjectcontent',),
        ),
        migrations.CreateModel(
            name='FileDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObject')),
                ('file_content', models.ForeignKey(related_name='data_object', on_delete=django.db.models.deletion.PROTECT, to='analysis.FileContent', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobject',),
        ),
        migrations.CreateModel(
            name='FileImport',
            fields=[
                ('abstractfileimport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractFileImport')),
                ('note', models.TextField(max_length=10000, null=True)),
                ('source_url', models.TextField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractfileimport',),
        ),
        migrations.CreateModel(
            name='FixedWorkflowRunInput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='GoogleCloudTaskRunAttempt',
            fields=[
                ('taskrunattempt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.TaskRunAttempt')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.taskrunattempt',),
        ),
        migrations.CreateModel(
            name='IntegerContent',
            fields=[
                ('dataobjectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObjectContent')),
                ('integer_value', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobjectcontent',),
        ),
        migrations.CreateModel(
            name='IntegerDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObject')),
                ('integer_content', models.OneToOneField(related_name='data_object', on_delete=django.db.models.deletion.PROTECT, to='analysis.IntegerContent')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobject',),
        ),
        migrations.CreateModel(
            name='LocalTaskRunAttempt',
            fields=[
                ('taskrunattempt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.TaskRunAttempt')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.taskrunattempt',),
        ),
        migrations.CreateModel(
            name='MockTaskRunAttempt',
            fields=[
                ('taskrunattempt_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.TaskRunAttempt')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.taskrunattempt',),
        ),
        migrations.CreateModel(
            name='RequestedDockerEnvironment',
            fields=[
                ('requestedenvironment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.RequestedEnvironment')),
                ('docker_image', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.requestedenvironment',),
        ),
        migrations.CreateModel(
            name='RunRequestInput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='RunRequestOutput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('abstractworkflow_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractWorkflow')),
                ('command', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractworkflow',),
        ),
        migrations.CreateModel(
            name='StepRun',
            fields=[
                ('abstractworkflowrun_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractWorkflowRun')),
                ('template', models.ForeignKey(related_name='step_runs', to='analysis.Step')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractworkflowrun',),
        ),
        migrations.CreateModel(
            name='StepRunOutput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
                ('step_run', models.ForeignKey(related_name='outputs', to='analysis.StepRun')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='StringContent',
            fields=[
                ('dataobjectcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObjectContent')),
                ('string_value', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobjectcontent',),
        ),
        migrations.CreateModel(
            name='StringDataObject',
            fields=[
                ('dataobject_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.DataObject')),
                ('string_content', models.OneToOneField(related_name='data_object', on_delete=django.db.models.deletion.PROTECT, to='analysis.StringContent')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.dataobject',),
        ),
        migrations.CreateModel(
            name='TaskDefinitionDockerEnvironment',
            fields=[
                ('taskdefinitionenvironment_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.TaskDefinitionEnvironment')),
                ('docker_image', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.taskdefinitionenvironment',),
        ),
        migrations.CreateModel(
            name='TaskRunAttemptLogFileImport',
            fields=[
                ('abstractfileimport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractFileImport')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractfileimport',),
        ),
        migrations.CreateModel(
            name='TaskRunAttemptOutputFileImport',
            fields=[
                ('abstractfileimport_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractFileImport')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractfileimport',),
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('abstractworkflow_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractWorkflow')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractworkflow',),
        ),
        migrations.CreateModel(
            name='WorkflowRun',
            fields=[
                ('abstractworkflowrun_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractWorkflowRun')),
                ('template', models.ForeignKey(related_name='workflow_runs', to='analysis.Workflow')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractworkflowrun',),
        ),
        migrations.CreateModel(
            name='WorkflowRunInput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
                ('workflow_run', models.ForeignKey(related_name='inputs', to='analysis.WorkflowRun')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.CreateModel(
            name='WorkflowRunOutput',
            fields=[
                ('inputoutputnode_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.InputOutputNode')),
                ('workflow_run', models.ForeignKey(related_name='outputs', to='analysis.WorkflowRun')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.inputoutputnode',),
        ),
        migrations.AddField(
            model_name='taskrunoutput',
            name='data_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='analysis.DataObject', null=True),
        ),
        migrations.AddField(
            model_name='taskrunoutput',
            name='task_definition_output',
            field=models.OneToOneField(related_name='task_run_output', null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.TaskDefinitionOutput'),
        ),
        migrations.AddField(
            model_name='taskrunoutput',
            name='task_run',
            field=models.ForeignKey(related_name='outputs', to='analysis.TaskRun'),
        ),
        migrations.AddField(
            model_name='taskruninput',
            name='data_object',
            field=models.ForeignKey(to='analysis.DataObject', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='taskruninput',
            name='task_definition_input',
            field=models.OneToOneField(related_name='task_run_input', null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.TaskDefinitionInput'),
        ),
        migrations.AddField(
            model_name='taskruninput',
            name='task_run',
            field=models.ForeignKey(related_name='inputs', to='analysis.TaskRun'),
        ),
        migrations.AddField(
            model_name='taskrunattemptoutput',
            name='data_object',
            field=models.OneToOneField(related_name='task_run_attempt_output', null=True, on_delete=django.db.models.deletion.PROTECT, to='analysis.DataObject'),
        ),
        migrations.AddField(
            model_name='taskrunattemptoutput',
            name='task_run_attempt',
            field=models.ForeignKey(related_name='outputs', to='analysis.TaskRunAttempt'),
        ),
        migrations.AddField(
            model_name='taskrunattemptoutput',
            name='task_run_output',
            field=models.ForeignKey(related_name='task_run_attempt_outputs', on_delete=django.db.models.deletion.SET_NULL, to='analysis.TaskRunOutput', null=True),
        ),
        migrations.AddField(
            model_name='taskrunattemptlogfile',
            name='task_run_attempt',
            field=models.ForeignKey(related_name='log_files', to='analysis.TaskRunAttempt'),
        ),
        migrations.AddField(
            model_name='taskrunattempt',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.taskrunattempt_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='taskrunattempt',
            name='task_run',
            field=models.ForeignKey(related_name='task_run_attempts', to='analysis.TaskRun'),
        ),
        migrations.AddField(
            model_name='taskdefinitioninput',
            name='data_object_content',
            field=models.ForeignKey(to='analysis.DataObjectContent', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='taskdefinitioninput',
            name='task_definition',
            field=models.ForeignKey(related_name='inputs', to='analysis.TaskDefinition'),
        ),
        migrations.AddField(
            model_name='taskdefinitionenvironment',
            name='environment',
            field=models.OneToOneField(to='analysis.TaskDefinition'),
        ),
        migrations.AddField(
            model_name='taskdefinitionenvironment',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.taskdefinitionenvironment_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='runrequest',
            name='run',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='analysis.AbstractWorkflowRun'),
        ),
        migrations.AddField(
            model_name='runrequest',
            name='template',
            field=models.ForeignKey(to='analysis.AbstractWorkflow', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='restartrequest',
            name='run_request',
            field=models.ForeignKey(related_name='restart_requests', to='analysis.RunRequest'),
        ),
        migrations.AddField(
            model_name='requestedenvironment',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.requestedenvironment_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='inputoutputnode',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.inputoutputnode_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='filelocation',
            name='unnamed_file_content',
            field=models.ForeignKey(related_name='file_locations', on_delete=django.db.models.deletion.SET_NULL, to='analysis.UnnamedFileContent', null=True),
        ),
        migrations.AddField(
            model_name='failurenotice',
            name='run_request',
            field=models.ForeignKey(related_name='failure_notices', to='analysis.RunRequest'),
        ),
        migrations.AddField(
            model_name='dataobjectcontent',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.dataobjectcontent_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='dataobject',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.dataobject_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='channeloutput',
            name='data_objects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='analysis.DataObject', null=True),
        ),
        migrations.AddField(
            model_name='channeloutput',
            name='receiver',
            field=models.OneToOneField(related_name='from_channel', null=True, to='analysis.InputOutputNode'),
        ),
        migrations.AddField(
            model_name='channel',
            name='data_object',
            field=models.ForeignKey(to='analysis.DataObject', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='channel',
            name='sender',
            field=models.OneToOneField(related_name='to_channel', null=True, to='analysis.InputOutputNode'),
        ),
        migrations.AddField(
            model_name='cancelrequest',
            name='run_request',
            field=models.ForeignKey(related_name='cancel_requests', to='analysis.RunRequest'),
        ),
        migrations.AddField(
            model_name='abstractworkflowrun',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.abstractworkflowrun_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='abstractworkflow',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.abstractworkflow_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='abstractfileimport',
            name='file_location',
            field=models.OneToOneField(related_name='file_import', null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.FileLocation'),
        ),
        migrations.AddField(
            model_name='abstractfileimport',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_analysis.abstractfileimport_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='abstractfileimport',
            name='temp_file_location',
            field=models.OneToOneField(related_name='file_import_as_temp', null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.FileLocation'),
        ),
        migrations.CreateModel(
            name='FixedStepRunInput',
            fields=[
                ('abstractstepruninput_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractStepRunInput')),
                ('step_run', models.ForeignKey(related_name='fixed_inputs', to='analysis.StepRun')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractstepruninput',),
        ),
        migrations.CreateModel(
            name='StepRunInput',
            fields=[
                ('abstractstepruninput_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='analysis.AbstractStepRunInput')),
                ('step_run', models.ForeignKey(related_name='inputs', to='analysis.StepRun')),
            ],
            options={
                'abstract': False,
            },
            bases=('analysis.abstractstepruninput',),
        ),
        migrations.AddField(
            model_name='workflowoutput',
            name='workflow',
            field=models.ForeignKey(related_name='outputs', to='analysis.Workflow'),
        ),
        migrations.AddField(
            model_name='workflowinput',
            name='workflow',
            field=models.ForeignKey(related_name='inputs', to='analysis.Workflow'),
        ),
        migrations.AddField(
            model_name='workflow',
            name='steps',
            field=models.ManyToManyField(related_name='parent', to='analysis.AbstractWorkflow'),
        ),
        migrations.AddField(
            model_name='taskrunattemptlogfile',
            name='file_data_object',
            field=models.OneToOneField(related_name='task_run_attempt_log_file', null=True, on_delete=django.db.models.deletion.PROTECT, to='analysis.FileDataObject'),
        ),
        migrations.AddField(
            model_name='taskrun',
            name='step_run',
            field=models.ForeignKey(related_name='task_runs', to='analysis.StepRun'),
        ),
        migrations.AddField(
            model_name='steprunoutput',
            name='task_run_outputs',
            field=models.ManyToManyField(related_name='step_run_outputs', to='analysis.TaskRunOutput'),
        ),
        migrations.AddField(
            model_name='stepoutput',
            name='workflow',
            field=models.ForeignKey(related_name='outputs', to='analysis.Step'),
        ),
        migrations.AddField(
            model_name='stepinput',
            name='step',
            field=models.ForeignKey(related_name='inputs', to='analysis.Step'),
        ),
        migrations.AddField(
            model_name='runrequestoutput',
            name='run_request',
            field=models.ForeignKey(related_name='outputs', to='analysis.RunRequest'),
        ),
        migrations.AddField(
            model_name='runrequestinput',
            name='run_request',
            field=models.ForeignKey(related_name='inputs', to='analysis.RunRequest'),
        ),
        migrations.AddField(
            model_name='requestedresourceset',
            name='step',
            field=models.OneToOneField(related_name='resources', to='analysis.Step'),
        ),
        migrations.AddField(
            model_name='requestedenvironment',
            name='environment',
            field=models.OneToOneField(related_name='environment', to='analysis.Step'),
        ),
        migrations.AddField(
            model_name='fixedworkflowruninput',
            name='workflow_run',
            field=models.ForeignKey(related_name='fixed_inputs', to='analysis.WorkflowRun'),
        ),
        migrations.AddField(
            model_name='fixedworkflowinput',
            name='workflow',
            field=models.ForeignKey(related_name='fixed_inputs', to='analysis.Workflow'),
        ),
        migrations.AddField(
            model_name='fixedstepinput',
            name='step',
            field=models.ForeignKey(related_name='fixed_inputs', to='analysis.Step'),
        ),
        migrations.AddField(
            model_name='abstractworkflowrun',
            name='parent',
            field=models.ForeignKey(related_name='step_runs', to='analysis.WorkflowRun', null=True),
        ),
        migrations.AddField(
            model_name='abstractfileimport',
            name='file_data_object',
            field=models.OneToOneField(related_name='file_import', to='analysis.FileDataObject'),
        ),
        migrations.AddField(
            model_name='taskruninput',
            name='step_run_input',
            field=models.ForeignKey(related_name='task_run_inputs', on_delete=django.db.models.deletion.SET_NULL, to='analysis.StepRunInput', null=True),
        ),
    ]
