import json
import xmltodict
import sys
import os
import xml

def parse_xml_to_json(xml_string):
    """
        For parse XML to Json. Use xmltodict library for parse.
    """
    try:     
        return json.dumps(xmltodict.parse(xml_string, attr_prefix=''), indent=4)
    except xml.parsers.expat.ExpatError: # If the file content is not in xml format
        print('Incorrect xml file content format')
        sys.exit()

if __name__ == '__main__':
    """
        Check file that user input from command line argument, Open file and 
        Write json file to the new one with the same name but in json type.
    """
    if len(sys.argv) < 2:
        print('Usage: python weather.py [XML file]')
        sys.exit()

    filename = sys.argv[1]

    if not os.path.exists(filename): #If the file is not existed.
        print('The file is not existed')
        sys.exit()


    with open(filename, 'r') as f: 
        xml_string = f.read()

    filename_without_type = filename.split('.')[0]

    with open('{}.json'.format(filename_without_type), 'w') as f:
        f.write(parse_xml_to_json(xml_string))
    print('Parse finished')