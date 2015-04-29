from csv import DictReader

input_file = open("hp_wiki.tsv", 'r', encoding="utf-8")

num_edits = 0
num_anon = 0
for row in DictReader(input_file, delimiter="\t"):
    num_edits = num_edits + 1
    if row["anon"] == "True":
        num_anon = num_anon + 1

prop_anon = num_anon / num_edits

print("total edits: %s" % num_edits)
print("anon edits: %s" % num_anon)
print("proportion anon: %s" % prop_anon)
