import xml.etree.ElementTree as ET
import pynetbox
import env_file
import re
import xml.dom.minidom

def get_netbox_devices():
    nb_env = env_file.get(path='env-netbox')
    nb = pynetbox.api(
        url=nb_env['NETBOX_API_URL'],
        token=nb_env['NETBOX_API_KEY'],
        ssl_verify=False
    )

    all_devices = nb.dcim.devices.all()
    return all_devices

def strip_ip(ip):
    return re.sub(r'/\d+', '', str(ip))

def create_sub_element(device, elm):
    device_session = ET.SubElement(elm, "key")
    device_session.set("name", device.name)

    device_details = ET.SubElement(device_session, "string")
    device_details.set("name", "Hostname")
    device_details.text = strip_ip(device.primary_ip4)

def create_xml():
    tree = ET.Element("VanDyke")
    tree.set("version", "3.0")

    sessions = ET.SubElement(tree, "key")
    sessions.set("name", "Sessions")

    for device in get_netbox_devices():
        create_sub_element(device, sessions)

    mydata = ET.tostring(tree)
    dom = xml.dom.minidom.parseString(mydata)
    return dom.toprettyxml()

xml_file = create_xml()
with open("secure_crt_generated.xml", "w") as xml_write:
    xml_write.write(xml_file)
