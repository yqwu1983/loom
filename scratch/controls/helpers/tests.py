from django.test import TestCase
import json
import jsonschema
import os

from apps.controls.helpers import links
from apps.controls.helpers import objtools
from apps.controls.helpers import runrequest
from apps.controls.helpers import substitution
from apps.controls.helpers.runrequest import RunRequestValidationError

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'testdata')

class SubstitutionHelperTestCase(TestCase):

    def setUp(self):
        with open(os.path.join(TEST_DATA_DIR, 'pipeline1_nested_with_constants.json')) as f:
            self.pipeline1_nested_with_constants_json = f.read()
        self.pipeline1_nested_with_constants = json.loads(self.pipeline1_nested_with_constants_json)
        with open(os.path.join(TEST_DATA_DIR, 'pipeline1_substituted.json')) as f:
            self.pipeline1_substituted_exp_json = f.read()
        
    def testConstantSubstitituion(self):
        pipeline1_substituted = substitution.Substitution.apply_constants_in_json(
            self.pipeline1_nested_with_constants_json)
        pipeline1_substituted_json = json.dumps(pipeline1_substituted, indent=4, separators=(',',': '))

        self.assertEqual(pipeline1_substituted_json.rstrip(), self.pipeline1_substituted_exp_json.rstrip())

class LinkHelperTestCase(TestCase):

    def setUp(self):
        with open(os.path.join(TEST_DATA_DIR, 'pipeline2_flat.json')) as f:
            self.pipeline2_flat_json = f.read()
        with open(os.path.join(TEST_DATA_DIR, 'pipeline2_nested.json')) as f:
            self.pipeline2_nested_json = f.read()
        
    def testLinksResolution(self):
        pipeline2_nested = links.Linker().resolve_links_in_json(
            self.pipeline2_flat_json)
        pipeline2_nested_json = json.dumps(pipeline2_nested, indent=4, separators=(',',': '))

        pipeline2_nested_exp_json = self.pipeline2_nested_json

        with open('act.json', 'w') as f:
            f.write(pipeline2_nested_json.rstrip())

        with open('exp.json', 'w') as f:
            f.write(pipeline2_nested_exp_json.rstrip())

        self.assertEqual(pipeline2_nested_json.rstrip(), pipeline2_nested_exp_json.rstrip())

class RunRequestHelperTestCase(TestCase):
    
    def setUp(self):
        with open(os.path.join(TEST_DATA_DIR, 'pipeline3.json')) as f:
            self.pipeline3_json = f.read()

        with open(os.path.join(TEST_DATA_DIR, 'pipeline3_clean.json')) as f:
            self.pipeline3_clean_exp = f.read()

    def testCleanJson(self):
        pipeline3_clean_json = runrequest.RunRequestHelper.clean_json(self.pipeline3_json)
        self.assertEqual(pipeline3_clean_json.rstrip(), self.pipeline3_clean_exp.rstrip())

    def testValidateRawDataJson(self):
        should_pass = [
            'pipeline1_nested_with_constants.json',
            'pipeline1_substituted.json',
            'pipeline2_flat.json',
            'pipeline2_nested.json',
            'pipeline3.json',
            'pipeline3_clean.json',
        ]
        should_fail = [
            'pipeline_invalid.json'
        ]

        validator = runrequest.RunRequestHelper._validate_raw_data_json

        for json_file in should_pass:
            print json_file
            with open(os.path.join(TEST_DATA_DIR, json_file)) as f:
                data_json = f.read()
                self.verify_passes_validation(validator, data_json)

        for json_file in should_fail:
            print json_file
            with open(os.path.join(TEST_DATA_DIR, json_file)) as f:
                data_json = f.read()
                self.verify_fails_validation(validator, data_json)

    def testValidateCleanDataJson(self):
        should_pass = [
            'pipeline3_clean.json',
        ]
        should_fail = [
            'pipeline1_nested_with_constants.json',
            'pipeline1_substituted.json',
            'pipeline2_flat.json',
            'pipeline2_nested.json',
            'pipeline3.json',
            'pipeline_invalid.json'
        ]

        validator = runrequest.RunRequestHelper._validate_clean_data_json

        for json_file in should_pass:
            print json_file
            with open(os.path.join(TEST_DATA_DIR, json_file)) as f:
                data_json = f.read()
                self.verify_passes_validation(validator, data_json)

        for json_file in should_fail:
            print json_file
            with open(os.path.join(TEST_DATA_DIR, json_file)) as f:
                data_json = f.read()
                self.verify_fails_validation(validator, data_json)

    def verify_fails_validation(self, validator, data_json):
        obj = json.loads(data_json)
        with self.assertRaises(RunRequestValidationError):
            validator(obj)

    def verify_passes_validation(self, validator, data_json):
        obj = json.loads(data_json)
        validator(obj)