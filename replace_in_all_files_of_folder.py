import os
import re


def replace_in_all_files(input_regex, replace_regex, encoding_of_files, folder_path):
    regex = re.compile("{}".format(input_regex))
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        for file in filenames:
            file = os.path.join(dirpath, file)
            tempfile = file + ".temp"
            with open(tempfile, "w") as target:
                with open(file,
                          encoding="{}".format(encoding_of_files)) as source:
                    for line in source:
                        line = regex.sub("{}".format(replace_regex), line)
                        target.write(line)
            os.remove(file)
            os.rename(tempfile, file)


replace_in_all_files(input_regex=r"\d+,\d+,\d+\n",
                     replace_regex=r"",  # dont forget python takes \1 instead of $1
                     encoding_of_files="ISO-8859-1",  # ISO-8859-1, utf-8, etc.
                     folder_path="C:\\Users\\Jony\\Desktop\\process")  # dont forget double brackets
print("Done.")