import xml.etree.ElementTree as ET

def extract_amr(root):
	amr_list = []
	for sntamr in root.findall('sntamr'):
		sentence_element = sntamr.find('sentence')
		sentence_id = sentence_element.get('id')
		sentence = sentence_element.text.strip()
		amr = sntamr.find('amr').text.strip()
		amr_list.append((sentence_id, sentence, amr))
	return amr_list

amr_data = extract_amr(ET.parse ("amr_br-v1.0.xml"))

with open("amr_br-v1.0.txt", "w") as f:
	for sentence_id, sentence, amr in amr_data:
		f.write(f"# ::id {sentence_id}\n")
		f.write(f"# ::snt {sentence}\n")
		f.write(f"{amr}\n\n")

