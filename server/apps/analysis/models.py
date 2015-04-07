'''
database model definitions for an analysis
an analysis is of a pipeline with 1-n sessions which could be running in different environment.
a Session is of several analyzing steps
a Session own its own inputs/outputs which are shared by the analyzing steps within this session.
a File is a URL pointing to persistance location of the data, could be a file path or internet URL and etc

a database entry will be generated automatically by parsing json input, by calling jsonToClass
'''

from django.db import models
import json
import copy

class File(models.Model):
    fileid = models.CharField(primary_key=True, max_length=30)
    uri = models.CharField(max_length=256)
    ownerid = models.IntegerField(default=0)
    access = models.IntegerField(default=755)
    comment = models.CharField(max_length=256, default='')
    def jsonToClass( self, aux ):
        self.fileid = aux['id']
        self.uri = aux['path']
        self.comment = aux['comment']


class Resource(models.Model):
    resourceid = models.IntegerField(primary_key=True, default=0)
    diskspace = models.IntegerField(default=1000)
    memory = models.IntegerField(default=1000)
    cores = models.IntegerField(default=1)
    ownerid = models.IntegerField(default=0)
    access = models.IntegerField(default=755)
    comment = models.CharField(max_length=256, default='')
    def jsonToClass( self, aux ):
        self.resourceid = aux['id']
        self.diskspace = aux['disk_space']
        self.momery = aux['disk_space']
        self.cores = aux['cores']

class Step(models.Model):
    stepid = models.CharField(primary_key=True, max_length=256)
    stepname = models.CharField(max_length=30)
    cmd = models.CharField(max_length=256)
    application = models.CharField(max_length=256)
    comment = models.CharField(max_length=256, default='')
    access = models.IntegerField(default=755)
    def jsonToClass( self, aux ):
        self.comment = aux['comment']
        self.cmd = aux['command']
        self.application = aux['application']
        

class Session(models.Model):
    sessionid = models.CharField(primary_key=True, max_length=256)
    sessionname = models.CharField(max_length=30)
    steps = models.ManyToManyField(Step, related_name = 'step_id')
    importfiles = models.ManyToManyField(File, related_name = 'infile_id')
    savefiles = models.ManyToManyField(File, related_name = 'outfile_id')
    resourceid = models.ForeignKey(Resource, null=True, blank=True)
    comment = models.CharField(max_length=256, default='')
    access = models.IntegerField(default=755)
    def jsonToClass( self, aux ):
        self.sessionid = aux['id']
        self.comment = aux['comment']
    

class Pipeline(models.Model):
    pipelineid = models.CharField(primary_key=True, max_length=256)
    pipelinename = models.CharField(max_length=30)
    sessionids = models.ManyToManyField(Session, related_name = "session_id")
    comment = models.CharField(max_length=256, default='')
    access = models.IntegerField(default=755)
    def jsonToClass( self, query ):
        # files
        file_dict = {'':''}
        if type(query["files"]) is list :
            for file_entry in query["files"]:
                        f = File(uri="", fileid="", ownerid=0, comment="")
                        f.jsonToClass(file_entry)
                        f.save()
                        file_dict[file_entry["id"]]=f

            # steps
            step_dict = {'':''}
            if type(query["steps"]) is list :
                for step_entry in query["steps"]:
                        s = Step(stepid="", stepname="", cmd="", application="", comment="")
                        s.jsonToClass( step_entry )
                        step_dict[step_entry['id']] = s
                        s.save()

            # sessions
            if type(query["sessions"]) is list :
                for session_entry in query["sessions"]:
                        s = Session(sessionid="", sessionname="", comment="")
                        s.jsonToClass( session_entry )
                        #init foreign keys
                        s.pipelineid = self
                        s.save()
                        for item in session_entry["input_file"]:
                            s.importfiles.add(file_dict[item])
                        for item in session_entry["output_file"]:
                            s.savefiles.add(file_dict[item])
                        for item in session_entry["steps"]:
                            s.steps.add(step_dict[item])
                        s.save()
                        self.save()
                        self.sessionids.add(s)


class AnalysisStatus(models.Model):
    serverid = models.CharField(max_length=256)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    retries = models.IntegerField(default=0)
    ramusage = models.IntegerField(default=0)
    coresusage = models.IntegerField(default=1)
    msg = models.CharField(max_length=256)


class Analysis(models.Model):
    analysisid = models.CharField(primary_key=True, max_length=256)
    pipeline = models.ForeignKey(Pipeline)
    comment = models.CharField(max_length=256)
    ownerid = models.IntegerField(default=0)
    access = models.IntegerField(default=755)
    def prepareJSON(self):
        objs_4_runner = []
        for session in self.pipeline.sessionids.all():
            for step in session.steps.all():
                obj_4_runner = {}
                obj_4_runner['container']=step.application
                obj_4_runner['command']=step.cmd
                objs_4_runner.append(obj_4_runner)
        return json.dumps(objs_4_runner)


