import os
from django.test import TestCase
from django.core.exceptions import ValidationError

from api.models.data_objects import DataObject, FileResource


md5_1 = 'd8e8fca2dc0f896fd7cb4cb0031ba249'
filename_1 = 'mydata.txt'


class TestDataObject(TestCase):

    VALUE_SETS = [
        # (type, valid_value, invalid_value)
        ('boolean', True, 'True'),
        ('float', 3.7, '3.7'),
        ('integer', 3, '3'),
        ('string', ':D', 7),
    ]

    def testGetByValue(self):
        for (type, value, invalid_value) in self.VALUE_SETS:
            do = DataObject.get_by_value(value, type)
            self.assertEqual(do.contents, value)

    def testSubstitutionValue(self):
        for (type, value, invalid_value) in self.VALUE_SETS:
            do = DataObject.get_by_value(value, type)
            self.assertEqual(do.substitution_value, str(value))

    def testIsReady(self):
        for (type, value, invalid_value) in self.VALUE_SETS:
            do = DataObject.get_by_value(value, type)
            self.assertTrue(do.is_ready)

    def testGetByValue_invalidValue(self):
        for (type, value, invalid_value) in self.VALUE_SETS:
            with self.assertRaises(ValidationError):
                DataObject.get_by_value(invalid_value, type)

    def testGetByValue_invalidType(self):
        with self.assertRaises(ValidationError):
            DataObject.get_by_value('cantelope', 'fruit')

    def testCreateAndInitializeFileResource_import(self):
        imported_from_url = 'file:///data/'+filename_1
        comments = 'Test data'
        do = DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result',
            imported_from_url=imported_from_url,
            comments=comments)
        self.assertEqual(do.file_resource.md5, md5_1)
        self.assertEqual(do.file_resource.upload_status, 'incomplete')
        self.assertTrue('work' in do.file_resource.file_url)
        self.assertEqual(do.file_resource.comments, comments)
        self.assertEqual(
            do.file_resource.imported_from_url, imported_from_url)

    def testValue_file(self):
        do = DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result')
        self.assertEqual(do.contents, do.file_resource)

    def testSubstitutionValue_file(self):
        do = DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result')
        self.assertEqual(do.substitution_value, filename_1)

    def testGetByValue_file(self):
        do = DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result')
        file_identifiers = [
            filename_1,
            '$%s' % md5_1,
            '@%s' % do.uuid,
            '%s@%s' % (filename_1, do.uuid),
            '%s$%s' % (filename_1, md5_1),
            '%s$%s@%s' % (filename_1, md5_1, do.uuid),
            '$%s@%s' % (md5_1, do.uuid),
        ]
        for identifier in file_identifiers:
            retrieved_do = DataObject.get_by_value(identifier, 'file')
            self.assertEqual(do.uuid, retrieved_do.uuid)

    def testGetByValue_noMatch(self):
        with self.assertRaises(ValidationError):
            DataObject.get_by_value('noMatch', 'file')

    def testGetByValue_twoMatches(self):
        do = DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result')
        retrieved_do = DataObject.get_by_value(filename_1, 'file')
        self.assertEqual(do.uuid, retrieved_do.uuid)
        DataObject.create_and_initialize_file_resource(
            filename=filename_1, md5=md5_1, source_type='result')
        with self.assertRaises(ValidationError):
            DataObject.get_by_value(filename_1, 'file')


class TestFileResource(TestCase):

    def testInitialize(self):
        data_object = DataObject.objects.create(type='file')
        resource = FileResource.initialize(
            data_object=data_object, filename=filename_1,
            md5=md5_1, source_type='result')
        self.assertEqual(resource.md5, md5_1)
        self.assertEqual(resource.filename, filename_1)
        self.assertEqual(resource.data_object.uuid, data_object.uuid)
        self.assertTrue('work' in resource.file_url)
        self.assertEqual(resource.upload_status, 'incomplete')
        self.assertEqual(resource.source_type, 'result')

    def testIsReady(self):
        data_object = DataObject.objects.create(type='file')
        resource = FileResource.initialize(
            data_object=data_object, filename=filename_1,
            md5=md5_1, source_type='result')
        self.assertFalse(data_object.is_ready)
        self.assertFalse(resource.is_ready)
        resource.upload_status='complete'
        self.assertTrue(data_object.is_ready)
        self.assertTrue(resource.is_ready)

    def testGetUuid(self):
        data_object = DataObject.objects.create(type='file')
        resource = FileResource.initialize(
            data_object=data_object, filename=filename_1,
            md5=md5_1, source_type='result')
        self.assertEqual(resource.get_uuid(), data_object.uuid)

    
    
"""
class TestArrayDataObject(TestCase):

    def testSubstitutionValue(self):
        values = [1,2,3]
        data_object_list = [
            DataObject.get_by_value(i, 'integer')
            for i in values
        ]
        array_data_object = ArrayDataObject.create_from_list(
            data_object_list, 'integer')

        self.assertEqual(array_data_object.substitution_value, values)

    def testIsReady(self):
        values = [1,2,3]
        data_object_list = [
            DataObject.get_by_value(i, 'integer')
            for i in values
        ]
        array_data_object = ArrayDataObject.create_from_list(
            data_object_list, 'integer')
        self.assertTrue(array_data_object.is_ready())

    def testTypeMismatchError(self):
        data_object_list = [
            DataObject.get_by_value(3, 'integer'),
            DataObject.get_by_value(False, 'boolean')
        ]
        with self.assertRaises(TypeMismatchError):
            array_data_object = ArrayDataObject.create_from_list(
                data_object_list, 'integer')

    def testAddToArrayNonArrayError(self):
        member = DataObject.get_by_value(3, 'integer')
        non_array = DataObject.get_by_value(4, 'integer')
        with self.assertRaises(NonArrayError):
            member.add_to_array(non_array)
        
    def testAddToArrayNestedArraysError(self):
        array1 = DataObject.objects.create(
            type='integer',
            is_array=True
        )
        array2 = DataObject.objects.create(
            type='integer',
            is_array=True
        )
        with self.assertRaises(NestedArraysError):
            array1.add_to_array(array2)

    def testCreateFromListNestedArraysError(self):
        list1 = [
            DataObject.get_by_value(3, 'integer'),
            DataObject.get_by_value(5, 'integer')
        ]
        array1 = ArrayDataObject.create_from_list(
            list1, 'integer')

        list2=[
            DataObject.get_by_value(7, 'integer'),
            array1
        ]
        with self.assertRaises(NestedArraysError):
            array2 = ArrayDataObject.create_from_list(
                list2, 'integer')

    def testDuplicateFilenames(self):
        file_data_object_list = []
        for i in range(3):
            file_data_object_list.append(
                FileDataObject.objects.create(
                    type='file',
                    filename='same.txt',
                    source_type='imported',
                    file_import={'source_url': 'file:///data/somewhere.txt',
                                 'note': 'Test data'},
                    md5='abcde'
                )
            )

        array = ArrayDataObject.create_from_list(file_data_object_list, 'file')
        
        self.assertEqual(array.substitution_value,
                         ['same.txt','same__1__.txt','same__2__.txt'])
"""
