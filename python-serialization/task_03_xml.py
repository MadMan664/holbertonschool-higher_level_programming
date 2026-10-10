#!/usr/bin/env python3
"""Module that serializes a dictionary to XML and back."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file with a <data> root."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, str(key))
        child.text = str(value)
    tree = ET.ElementTree(root)
    if hasattr(ET, "indent"):
        ET.indent(tree)
    tree.write(filename, encoding="utf-8")


def deserialize_from_xml(filename):
    """Read an XML file and return the dictionary it describes.

    XML has no types, so every value comes back as a string.
    """
    root = ET.parse(filename).getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text if child.text is not None else ""
    return result
