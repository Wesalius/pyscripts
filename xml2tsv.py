from xml.etree.ElementTree import parse


def extract_from_xml(xml_file_path):
    tree = parse("{}.xml".format(xml_file_path))
    root = tree.getroot()
    with open("{}.tsv".format(xml_file_path), "w", encoding="utf-8") as tsv_from_xml, open(
            "active.tsv".format(xml_file_path), "w", encoding="utf-8") as active_tsv_from_xml, open(
            "inactive.tsv".format(xml_file_path), "w", encoding="utf-8") as inactive_tsv_from_xml:
        for player in root.findall("player"):
            fideid = player.find("fideid").text
            name = player.find("name").text
            country = player.find("country").text
            sex = player.find("sex").text
            flag = player.find("flag").text
            birthyear = player.find("birthday").text
            rating = int(player.find("rating").text)
            if not flag == "i" or flag == "wi":
                tsv_from_xml.write(str(fideid) + "\t" + str(name) + "\t" + "active (10/2016) " + str(
                    sex) + " chess player from " + str(country) + " born in " + str(birthyear) + "\n")
                active_tsv_from_xml.write(str(fideid) + "\t" + str(name) + "\t" + "active (10/2016) " + str(
                    sex) + " chess player from " + str(country) + " born in " + str(birthyear) + "\n")
            else:
                tsv_from_xml.write(str(fideid) + "\t" + str(name) + "\t" + "inactive (10/2016) " + str(
                    sex) + " chess player from " + str(country) + " born in " + str(birthyear) + "\n")
                inactive_tsv_from_xml.write(str(fideid) + "\t" + str(name) + "\t" + "inactive (10/2016) " + str(
                    sex) + " chess player from " + str(country) + " born in " + str(birthyear) + "\n")


print("Script for extracting content from http://ratings.fide.com xml files.\n"
      "Output will be in TSV: Column 1 is FIDE ID, Column 2 is NAME and Column 3 is DESCRIPTION.\n")

extract_from_xml(input("Give path to xml file without the xml extension: "))
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
