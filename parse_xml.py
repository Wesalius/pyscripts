from xml.etree.ElementTree import parse


def extract_from_xml(xml_file_path):
    tree = parse("{}.xml".format(xml_file_path))
    root = tree.getroot()
    for player in root.findall("player"):
        fideid = player.find("fideid").text
        rating = player.find("rating").text
