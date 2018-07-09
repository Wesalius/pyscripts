from xml.etree.ElementTree import parse


def extract_from_xml(xml_file_path):
    tree = parse("{}.xml".format(xml_file_path))
    root = tree.getroot()
    with open("{}.csv".format(xml_file_path), "w") as csv_from_xml:
        for player in root.findall("player"):
            fideid = player.find("fideid").text
            rating = player.find("rating").text
            csv_from_xml.write(fideid + "," + rating + "\n")


print("Script for extracting content from http://ratings.fide.com xml files.\n"
      "Output will be in CSV: Column 1 is FIDE ID, Column 2 is RATING.\n")
extract_from_xml(input("Give path to xml file without the xml extension. The path has to be enclosed in quotes: "))
print("Done.")

"""
Valid xml from http://ratings.fide.com looks like this:
<playerslist>
	<player>
		<fideid>10207538</fideid>
		<name>A E M, Doshtagir</name>
		<country>BAN</country>
		<sex>M</sex>
		<title></title>
		<w_title></w_title>
		<o_title></o_title>
		<rating>1864</rating>
		<games>0</games>
		<k>30</k>
		<birthday></birthday>
		<flag>i</flag>
	</player>
	<player>
		<fideid>10206612</fideid>
		<name>A K M, Sourab</name>
		<country>BAN</country>
		<sex>M</sex>
		<title></title>
		<w_title></w_title>
		<o_title></o_title>
		<rating>1714</rating>
		<games>0</games>
		<k>30</k>
		<birthday></birthday>
		<flag>i</flag>
	</player>
</playerslist>
"""