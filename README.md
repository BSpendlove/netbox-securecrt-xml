## Netbox SecureCRT XML

This simple script generates an XML file from Netbox that can be used to import into SecureCRT. You can achieve the same results with CSV format.

There is no filtering in place currently so all devices will be imported whether or not they have primary ipv4 address configured in Netbox, also all devices will exist in the root sessions folder (maybe I'll implement a way of allowing the user to define the folder structure based on Netbox attributes like device types/models, vendors,custom netbox tags, etc...)

### Installation

Simply install the requirements
```python
pip install -r requirements.txt
```

Add your Netbox API URL and Token KEY to `env-netbox`
Example:
```
NETBOX_API_URL=https://netbox.example.com
NETBOX_API_KEY=01j3ij2i3ji289du923u9089rh
```

and Run the script:
```console
.\generate.py
or
python .\generate.py
```

### Notes

This will create an XML called "secure_crt_generated.xml" in the directory of running the script. Please make a backup of your SecureCRT configuration prior to importing this generated file. You should only import the Sessions and nothing else (eg. global options) and then perform a mass edit to change any specific settings such as terminal apperance or SSH username/password/keys.