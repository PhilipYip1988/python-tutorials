import inspect
__version__ = '0.1.3'


def identifier_group(obj, kind='all', second=object, show_unique_identifiers=False, show_only_intersection_identifiers=False, has_parameter=''):
    
    """ Group identifiers from an obj into categories defined by the parameter kind. kind can have the possible values: 
    'all', 'datamodel_method, 'datamodel_attribute', 'upper_class', 'lower_class', 'function', 'constant', 'attribute', 'internal_attribute' or 'internal_method'.

    second class is an optional second class for comparison, normally a parent class. 
    
    show_unique_identifiers can be used to show only identifiers that are unique to the first class.

    show_only_intersection_identifiers can be used to show identifiers in the first class that also occur in the second class.
    These are inherited from the second class when the second class is a parent class.

    Returns:
        list: list of strings corresponding to identifiers in the grouping
    """

    identifiers = dir(obj)

    if isinstance(second, list):
        second_identifiers = []
        for identifier in second:
            second_identifiers.extend(dir(identifier))
        second_identifiers = list(set(second_identifiers))
        second_identifiers.sort()
    else:
        second_identifiers = dir(second)
    
    if ((show_unique_identifiers == False) and (show_only_intersection_identifiers == False)):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if (show_only_intersection_identifiers == False):
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    all_grouping = []
    datamodel_method_grouping = []
    datamodel_attribute_grouping = []
    upper_case_class_grouping = []
    lower_case_class_grouping = []
    function_grouping = []
    constant_grouping = []
    attribute_grouping = []
    internal_method_grouping = []
    internal_attribute_grouping = []

    for identifier in identifiers_to_examine:
        is_method = callable(getattr(obj, identifier))
        is_class = type(getattr(obj, identifier)) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__'
        is_internal = ((identifier[0:1] == '_') and not is_datamodel)

        all_grouping.append(identifier)
        if (is_method and is_datamodel):
            datamodel_method_grouping.append(identifier)
        if (not is_method and is_datamodel and not is_internal):
            datamodel_attribute_grouping.append(identifier)
        if (is_upper and is_class and not is_datamodel and not is_internal):
            upper_case_class_grouping.append(identifier)
        if (not is_upper and is_class and not is_datamodel and not is_internal):
            lower_case_class_grouping.append(identifier)
        if (is_method and not is_upper and not is_class and not is_datamodel and not is_internal):
            function_grouping.append(identifier)
        if (not is_method and is_upper and not is_datamodel and not is_internal):
            constant_grouping.append(identifier)
        if (not is_method and not is_upper and not is_datamodel and not is_internal):
            attribute_grouping.append(identifier)
        if (is_method and is_internal):
            internal_method_grouping.append(identifier)
        if (not is_method and is_internal):
            internal_attribute_grouping.append(identifier)

    if (has_parameter != ''):
        function_with_parameter = []
        for identifier in function_grouping:
            if (has_parameter in inspect.signature(getattr(obj, identifier)).parameters):
                function_with_parameter.append(identifier)
        function_grouping = function_with_parameter

    if (kind == 'all'):    
        return all_grouping
    elif (kind == 'datamodel_method'):   
        return datamodel_method_grouping
    elif (kind == 'datamodel_attribute'):   
        return datamodel_attribute_grouping
    elif (kind == 'class'):   
        return upper_case_class_grouping
    elif (kind == 'lower_class'):   
        return lower_case_class_grouping
    elif (kind == 'function'):   
        return function_grouping  
    elif (kind == 'constant'):   
        return constant_grouping
    elif (kind == 'attribute'):   
        return attribute_grouping
    elif (kind == 'internal_method'):   
        return internal_method_grouping
    elif (kind == 'attribute'):   
        return attribute_grouping
    elif (kind == 'internal_attribute'):   
        return internal_attribute_grouping
    else:
        raise(ValueError, "Invalid value for kind. Possible values are 'all', 'datamodel_method, 'datamodel_attribute', 'class', 'lower_class', 'function', 'constant', 'attribute', 'internal_attribute' or 'internal_method'.")
    

def print_identifier_group(obj, kind='all', second=object, show_unique_identifiers=False, show_only_intersection_identifiers=False, has_parameter=''):
    
    """Group identifiers from an obj into categories defined by the parameter kind and print. kind can have the possible values: 
    'all', 'datamodel_method, 'datamodel_attribute', 'upper_class', 'lower_class', 'function', 'constant', 'attribute', 'internal_attribute' or 'internal_method'.

    second class is an optional second class for comparison, normally a parent class. 
    
    show_unique_identifiers can be used to show only identifiers that are unique to the first class.

    show_only_intersection_identifiers can be used to show identifiers in the first class that also occur in the second class.
    These are inherited from the second class when the second class is a parent class.

    Returns:
        list: list of strings corresponding to identifiers in the grouping
    """

    identifiers = dir(obj)

    if isinstance(second, list):
        second_identifiers = []
        for identifier in second:
            second_identifiers.extend(dir(identifier))
        second_identifiers = list(set(second_identifiers))
        second_identifiers.sort()
    else:
        second_identifiers = dir(second)
    
    if ((show_unique_identifiers == False) and (show_only_intersection_identifiers == False)):
        identifiers_to_examine = identifiers
    else:
        unique_identifiers = set(identifiers) - set(second_identifiers)
        inherited_identifiers = set(identifiers) & set(second_identifiers) 
        if (show_only_intersection_identifiers == False):
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in unique_identifiers]
        else:
            identifiers_to_examine = [identifier for identifier in identifiers if identifier in inherited_identifiers]

    all_grouping = []
    datamodel_method_grouping = []
    datamodel_attribute_grouping = []
    upper_case_class_grouping = []
    lower_case_class_grouping = []
    function_grouping = []
    constant_grouping = []
    attribute_grouping = []
    internal_method_grouping = []
    internal_attribute_grouping = []

    for identifier in identifiers_to_examine:
        is_method = callable(getattr(obj, identifier))
        is_class = type(getattr(obj, identifier)) == type
        is_upper = identifier[0].isupper()
        is_datamodel = identifier[0:2] == '__'
        is_internal = ((identifier[0:1] == '_') and not is_datamodel)

        all_grouping.append(identifier)
        if (is_method and is_datamodel and not is_internal):
            datamodel_method_grouping.append(identifier)
        if (not is_method and is_datamodel and not is_internal):
            datamodel_attribute_grouping.append(identifier)
        if (is_upper and is_class and not is_datamodel and not is_internal):
            upper_case_class_grouping.append(identifier)
        if (not is_upper and is_class and not is_datamodel and not is_internal):
            lower_case_class_grouping.append(identifier)
        if (is_method and not is_upper and not is_class and not is_datamodel and not is_internal):
            function_grouping.append(identifier)
        if (not is_method and is_upper and not is_datamodel and not is_internal):
            constant_grouping.append(identifier)
        if (not is_method and not is_upper and not is_datamodel and not is_internal):
            attribute_grouping.append(identifier)
        if (is_method and is_internal):
            internal_method_grouping.append(identifier)
        if (not is_method and is_internal):
            internal_attribute_grouping.append(identifier)

    if (has_parameter != ''):
        function_with_parameter = []
        for identifier in function_grouping:
            if (has_parameter in inspect.signature(getattr(obj, identifier)).parameters):
                function_with_parameter.append(identifier)
        function_grouping = function_with_parameter

    if (kind == 'all'):    
        print('datamodel attribute:', end=' ')
        print(datamodel_attribute_grouping)
        print('datamodel method:', end=' ')
        print(datamodel_method_grouping)
        print('constant:', end=' ')
        print(constant_grouping)
        print('attribute:', end=' ')
        print(attribute_grouping)
        print('method/function:', end=' ')
        print(function_grouping)
        print('upper class:', end=' ')
        print(upper_case_class_grouping)
        print('lower class:', end=' ')
        print(lower_case_class_grouping)
    elif (kind == 'datamodel_method'):   
        print(datamodel_method_grouping)
    elif (kind == 'datamodel_attribute'):   
        print(datamodel_attribute_grouping)
    elif (kind == 'upper_class'):   
        print(upper_case_class_grouping)
    elif (kind == 'lower_class'):   
        print(lower_case_class_grouping)
    elif (kind == 'function'):   
        print(function_grouping) 
    elif (kind == 'constant'):   
        print(constant_grouping)
    elif (kind == 'attribute'):   
        print(attribute_grouping)
    elif (kind == 'internal_method'):   
        print(internal_method_grouping)
    elif (kind == 'attribute'):   
        print(attribute_grouping)
    elif (kind == 'internal_attribute'):   
        print(internal_attribute_grouping)
    else:
        raise(ValueError, "Invalid value for kind. Possible values are 'all', 'datamodel_method, 'datamodel_attribute', 'class', 'lower_class', 'function', 'constant', 'attribute', 'internal_attribute' or 'internal_method'.")