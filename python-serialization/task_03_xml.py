#!/usr/bin/python3
"""
python program
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    this function serialize the dictionary into XML and
    save it to the given filename.
    """

    root = ET.Element("data")

    def add_dict_to_element(element, data):
        """
        read the XML data from that file,
        and return a deserialized Python dictionary.
        """
        for key, value in data.items():
            child = ET.SubElement(element, key)
            if isinstance(value, dict):
                add_dict_to_element(child, value)
            else:
                child.text = str(value)

    add_dict_to_element(root, dictionary)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    def element_to_dict(element):
        result = {}
        for child in element:
            if len(child) == 0:
                result[child.tag] = child.text
            else:
                result[child.tag] = element_to_dict(child)
        return result

    return element_to_dict(root)
