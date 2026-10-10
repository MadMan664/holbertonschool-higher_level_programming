# Python - Serialization

Serialization of Python data to JSON, pickle, CSV-to-JSON and XML.

## Files

| File | Description |
|------|-------------|
| `task_00_basic_serialization.py` | `serialize_and_save_to_file(data, filename)` saves a dictionary as JSON (replacing the file); `load_and_deserialize(filename)` loads it back |
| `task_01_pickle.py` | `CustomObject` with `display()`, `serialize(filename)` and the class method `deserialize(filename)` using `pickle`; returns `None` on a missing or malformed file |
| `task_02_csv.py` | `convert_csv_to_json(csv_filename)` writes `data.json` from a CSV file; returns `True` on success, `False` on error |
| `task_03_xml.py` | `serialize_to_xml(dictionary, filename)` and `deserialize_from_xml(filename)` using `xml.etree.ElementTree` (values come back as strings) |

## Usage

```python
#!/usr/bin/env python3
from task_00_basic_serialization import (
    load_and_deserialize, serialize_and_save_to_file)

serialize_and_save_to_file({"name": "John Doe", "age": 30}, "data.json")
print(load_and_deserialize("data.json"))
```
