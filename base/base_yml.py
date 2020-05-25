import yaml

def yml_data_with_filename_key(file_name, key):
    with open("./data/" + file_name + ".yaml", "r", encoding='utf-8') as f:
        yaml.warnings({'YAMLLoadWarning': False})
        data = yaml.load(f)[key]
        case_data_list = []
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list
