import os

class BaseInput(object):

    def __init__(self, data_contents, task_attempt):
        self.data_contents = data_contents
        self.filemanager = task_attempt.filemanager
        self.settings = task_attempt.settings


class FileInput(BaseInput):

    def copy(self):
        data_object = self.data_contents
        data_object_id = '@%s' % data_object['uuid']
        self.filemanager.export_file(
            data_object_id,
            destination_url=self.settings['WORKING_DIR'],
            retry=True)


class FileListInput(BaseInput):

    def copy(self):
        data_object_list = self.data_contents
        filename_array = [data_object['value']['filename']
                          for data_object in data_object_list]
        duplicates = self._get_duplicates(filename_array)

        filename_counts = {}
        for data_object in data_object_list:
	    filename = data_object['value']['filename']
            # Increment filenames if there are duplicates in an array,       
            # e.g. file__0__.txt, file__1__.txt, file__2__.txt
            if filename in duplicates:
                counter = filename_counts.setdefault(filename, 0)
                filename_counts[filename] += 1
                filename = self._rename_duplicate(filename, counter)

            data_object_id = '@%s' % data_object['uuid']
            self.filemanager.export_file(
                data_object_id,
                destination_url=os.path.join(
                    self.settings['WORKING_DIR'], filename),
                retry=True)

    def _get_duplicates(self, array):
        seen = set()
        duplicates = set()
        for member in array:
            if member in seen:
                duplicates.add(member)
            seen.add(member)
        return duplicates

    def _rename_duplicate(self, filename, counter):
        parts = filename.split('.')
        assert len(parts) > 0, 'missing filename'
        if len(parts) == 1:
            return parts[0] + '(%s)' % counter
        else:
            return '.'.join(parts[0:len(parts)-1]) + '__%s__.' % counter + parts[-1]


class NoOpInput(BaseInput):

    def copy(self):
        return


def _get_input_info(input):
    assert 'type' in input, 'invalid input: "type" is missing'
    assert 'mode' in input, 'invalid input: "mode" is missing'
    data_type = input['type']
    assert data_type in ['file', 'boolean', 'string', 'integer', 'float'], \
        'input has invalid type "%s"' % data_type
    mode = input['mode']
    assert mode == 'no_gather' or mode.startswith('gather'), \
        'input has invalid mode "%s"' % mode
    return (data_type, mode)

def _expand_data_contents(input, connection):
    input['data'] = connection.get_data_node(input['data']['uuid'], expand=True)
    

def TaskAttemptInput(input, task_attempt):
    """Returns the correct Input class for a given
    data type and gather mode
    """

    _expand_data_contents(input, task_attempt.connection)
    
    (data_type, mode) = _get_input_info(input)

    if data_type != 'file':
        return NoOpInput(None, task_attempt)

    if mode == 'no_gather':
        return FileInput(input['data']['contents'], task_attempt)
    else:
        assert mode.startswith('gather')
        return FileListInput(input['data']['contents'], task_attempt)
