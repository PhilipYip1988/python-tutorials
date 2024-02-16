import inspect
import pprint
import numpy as np
import pandas as pd
import sys
from fractions import Fraction
from collections import namedtuple, defaultdict, deque, Counter, OrderedDict, ChainMap
from datetime import time, date, datetime, timedelta
import os
pd.set_option('display.max_colwidth', 200)

__version__ = '1.1.4' 


def dir2(obj='default', second=object, unique_only=False, consistent_only=False, parameter='', print_output=True, show='all', exclude_external_modules=False):
    """ 
    Categorize identifiers from an object into different groups.

    Parameters:
    - obj: The object to inspect. If None, it defaults to the global namespace at runtime.
    - second: An optional second class for comparison, normally a parent class.
    - unique_only: Show only identifiers that are unique to the first class.
    - consistent_only: Show identifiers in the first class that also occur in the second class.
                     These are inherited from the second class when the second class is a parent class.
    - parameter: Filter functions by whether they have a specific parameter.
    - exclude_external_modules: Exclude identifiers in modules that do not have a __file__ attribute.
    
    Prints:
    - A dictionary with categories as keys and lists of identifiers as values.
    """
    if id(obj) == id('default'):
        frame = inspect.currentframe().f_back
        obj2 = frame.f_globals.copy()
        identifiers = list(obj2.keys())
        del frame
    else:
        try: 
            obj.__dict__.keys()
            if hasattr(obj.__dict__.keys(), '__package__'):
                identifiers = list(obj.__dict__.keys())
            else:
                identifiers = dir(obj)
        except:    
            identifiers = dir(obj)
        if isinstance(second, list):
            second_identifiers = []
            for identifier in second:
                second_identifiers.extend(dir(identifier))
            second_identifiers = list(set(second_identifiers))
            second_identifiers.sort()
        else:
            second_identifiers = dir(second)
    
    if not (unique_only or consistent_only):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if not consistent_only:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    grouping_dict = {
        'attribute': [],
        'constant': [],
        'module': [],
        'method': [],
        'lower_class': [],
        'upper_class': [],
        'datamodel_attribute': [],
        'datamodel_method': [],
        'internal_attribute': [],
        'internal_method': [],
    }

    for identifier in identifiers_to_examine:        
        if id(obj) == id('default'):
            is_method = callable(obj2[identifier])
            is_class = type(obj2[identifier]) == type
        else:
            try:
                is_method = callable(getattr(obj, identifier))
                is_class = inspect.isclass(getattr(obj, identifier))
            except Exception:
                continue  # Ignore errors and continue with the next identifier

        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__' and len(identifier) > 3
        is_internal = ((identifier[0:1] == '_') and not is_datamodel)

        if is_method and is_datamodel:
            grouping_dict['datamodel_method'].append(identifier)
        if not is_method and is_datamodel and not is_internal:
            grouping_dict['datamodel_attribute'].append(identifier)
        if is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['upper_class'].append(identifier)
        if not is_upper and is_class and not is_datamodel and not is_internal:
            grouping_dict['lower_class'].append(identifier)
        if is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            grouping_dict['method'].append(identifier)
        if not is_method and is_upper and not is_datamodel and not is_internal:
            grouping_dict['constant'].append(identifier)
        if not is_method and not is_upper and not is_class and not is_datamodel and not is_internal:
            if obj == 'default':
                grouping_dict['attribute'].append(identifier)
            else:
                if not exclude_external_modules and hasattr(getattr(obj, identifier), '__file__') and identifier != 'sys':
                    grouping_dict['module'].append(identifier)
                elif exclude_external_modules and hasattr(getattr(obj, identifier), '__file__') and identifier != 'sys':
                    if hasattr(obj, '__file__'):
                        objfilename = obj.__file__
                        filename = getattr(obj, identifier).__file__
                        objfilename = objfilename.removesuffix(r'\__init__.py').removesuffix(r'/__init__.py')
                        if objfilename in filename:
                            grouping_dict['module'].append(identifier)
                elif not exclude_external_modules and identifier in {'sys', 'time'}:
                    grouping_dict['module'].append(identifier)
                elif exclude_external_modules and identifier in {'sys', 'time'}:
                    pass    
                elif not exclude_external_modules:
                    grouping_dict['module'].append(identifier)
                else:
                    grouping_dict['attribute'].append(identifier)
        if is_method and is_internal:
            grouping_dict['internal_method'].append(identifier)
        if not is_method and is_internal:
            grouping_dict['internal_attribute'].append(identifier)
        if is_class and is_method and identifier not in grouping_dict['module']:
            try:
                is_module = inspect.ismodule(getattr(obj, identifier))
                if is_module:
                    grouping_dict['module'].append(identifier)
            except AttributeError:
                pass

    if parameter != '':
        function_with_parameter = []
        for identifier in grouping_dict['method']:
            try:
                signature = inspect.signature(getattr(obj, identifier))
                if parameter in signature.parameters:
                    function_with_parameter.append(identifier)
            except Exception:
                pass  # Ignore any errors and continue with the next identifier
        
        grouping_dict.clear()
        grouping_dict['method'] = function_with_parameter

    if show != 'all':
        if type(show) == str:
            show2 = []
            show2.append(show)
            show = show2
        grouping_dict = {key: value for key, value in grouping_dict.items() if key in show}

    grouping_dict = {key: value for key, value in grouping_dict.items() if len(value) > 0}
    if print_output:
        pprint.pprint(grouping_dict, sort_dicts=False)
    else:
        return grouping_dict

def variables(show_identifiers='all', show_id=False):
    standard_keys = ['In', 'Out', 'get_ipython', 'exit', 'quit', 'open', 'dir2', 'variables_df']
    frame = inspect.currentframe().f_back
    variable_dict = frame.f_globals.copy()
    if show_id:
        columns = ['Instance Name', 'Type', 'Size/Shape', 'Value', 'ID']
    else:
        columns = ['Instance Name', 'Type', 'Size/Shape', 'Value']
    variables_data = []

    supported_datatypes = [
        str, bytes, bytearray, int, float, bool, complex, tuple, list, dict, frozenset, set, np.ndarray, 
        pd.Index, pd.Series, pd.DataFrame, Fraction, defaultdict, deque, Counter, OrderedDict, ChainMap,
        range, time, date, datetime, timedelta
    ]

    for key, value in variable_dict.items():
        datatype = type(value)
        if (
            not key.startswith('_') 
            and key not in standard_keys 
            and (
                datatype in supported_datatypes 
                or value is None 
                or (isinstance(value, tuple) and hasattr(value, '_fields'))
            )
        ):
            if hasattr(value, '__len__'):
                size = len(value)
            elif isinstance(value, (np.ndarray, pd.DataFrame, pd.Series, pd.Index)):
                size = value.shape
            else:
                size = ''
            
            if isinstance(value, pd.Series):
                value = value.to_numpy()
            elif isinstance(value, pd.DataFrame):
                value = value.columns.tolist()
            elif isinstance(value, np.ndarray):
                value = value.tolist()
            else:
                value = str(value)

            datatype = str(datatype)
            datatype = datatype.split("'")[1].split(".")[-1]

            variable_id = id(value)

            if show_id:
                variables_data.append([key, datatype, size, value, variable_id])
            else:
                variables_data.append([key, datatype, size, value])

    variables_df = pd.DataFrame(variables_data, columns=columns)
    variables_df.set_index('Instance Name', inplace=True)

    if show_identifiers != 'all':
        variables_df = variables_df.loc[show_identifiers]
    
    return variables_df

def view(collection, neg_index=False):
    if (type(collection) == dict):
        print('Key'.ljust(30), '\t', 'Value'.ljust(30), '\t', 'Value Type'.ljust(20), '\t', 'Value Size'.ljust(6))
        if neg_index==False:
            for key, obj in collection.items():
                if '__len__' in dir(obj):
                    size = len(obj)
                else:
                    size = 1
                print(str(key).ljust(30), '\t', str(obj).ljust(30), '\t', str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t')
    elif (type(collection) == set) or (type(collection) == frozenset):
        print('Type'.ljust(20), '\t', 'Size'.ljust(6), '\t', 'Value'.ljust(30))
        if neg_index==False:
            for idx, obj in enumerate(collection):
                if '__len__' in dir(obj):
                    size = len(obj)
                else:
                    size = 1
                print(str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)
        else:
            for idx, obj in enumerate(collection):
                idx = idx - len(collection)
                if '__len__' in dir(obj):
                    size = len(obj)
                else:
                    size = 1
                print(str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)
    else:    
        print('Index', '\t', 'Type'.ljust(20), '\t', 'Size'.ljust(6), '\t', 'Value'.ljust(30))
        if neg_index==False:
            for idx, obj in enumerate(collection):
                if '__len__' in dir(obj):
                    size = len(obj)
                else:
                    size = 1
                print(idx, '\t', str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)
        else:
            for idx, obj in enumerate(collection):
                idx = idx - len(collection)
                if '__len__' in dir(obj):
                    size = len(obj)
                else:
                    size = 1
                print(idx, '\t', str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)
