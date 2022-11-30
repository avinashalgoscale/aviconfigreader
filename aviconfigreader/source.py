import os
import yaml
import configparser
import json

def readconfig(input_file, output_filename, output_file_extension):
    """
    reads input files and writes to output file
    compatible files are yaml, cfg and conf
    format can be ".json", ".env" or "os"
    os format will write into os environment
    """
    def read_yaml_file(input_file, output_filename, output_file_extension):
        with open(input_file, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        if output_file_extension == ".env" or ".json":
            output_path = output_filename+output_file_extension
            with open(output_path, 'w') as output_file:
                if output_file_extension == ".json":
                    json.dump(data_loaded, output_file)
                elif output_file_extension == ".env":
                    for key, value in data_loaded.items():
                        output_file.write(f"{key}={value}")
        else:
            for key, value in data_loaded.items():
                os.environ.setdefault[key] = value
    def read_conf_file(input_file, output_filename, output_file_extension):
        config = configparser.ConfigParser()
        config.read(input_file)
        flat_dict = {}
        for sect in config.sections():
            for k,v in config.items(sect):
                flat_dict[k] = v
        if output_file_extension == ".env" or ".json":
            output_path = output_filename+output_file_extension
            with open(output_path, 'w') as output_file:
                if output_file_extension == ".json":
                    json.dump(flat_dict, output_file)
                elif output_file_extension == ".env":
                    for key, value in flat_dict.items():
                        output_file.write(f"{key}={value}")
        else:
            for key, value in flat_dict.items():
                os.environ.setdefault[key] = value
    # get file extension of input file yaml/cfg/conf
    filename, extension = os.path.splitext(input_file)
    if extension == ".yaml":
        read_yaml_file(input_file, output_filename, output_file_extension)
    elif extension == ".conf" or "cfg":
        read_conf_file(input_file, output_filename, output_file_extension)
    else:
        raise IOError("invalid input file format")

# readconfig("sample.cfg", "outfile", ".json")