#!/usr/bin/env python3

import tempfile, zipfile
import glob, os, re, sys
import datetime
import xml.etree.ElementTree as ET

word_dir = r'ref_words'
docm_dir = r'input_doc'
if len(sys.argv) == 3:
    word_dir = sys.argv[1]
    docm_dir = sys.argv[2]

def tpyos(word_dir, docm_dir):
    """
    build reference list of words
    each line from all files in word_dir is considered a word
    all words converted to lowercase, so not suitable to detect capitalization defects
    encoding assumed: UTF-8
    """
    ref_words = set()
    for word_file in glob.glob(word_dir + os.sep + '*'):
        if os.path.isfile(word_file):
            with open(word_file, 'r', encoding='UTF-8') as wf:
                ref_words.update(set(wf.read().lower().split('\n')))

    """
    build typo dictionary
    input document assumed as docx/epub, they are unzipped in temp dir
    then each filename containing xml/htm is processed --> need to improve this
    xhtml format files likely not processed correctly because of text formatting mixing
    """
    tpyo_words = dict()
    re_strip = re.compile(r'^[^a-zA-Z]*|[^a-zA-Z]*$')
    re_valid_words = re.compile(r'[a-zA-Z]')
    for doc_file in glob.glob(docm_dir + os.sep + '*'):
        if re.search(r'\.(epub|docx)$', doc_file) and os.path.isfile(doc_file):
            with zipfile.ZipFile(doc_file, 'r') as zp, tempfile.TemporaryDirectory() as td:
                zp.extractall(td)
                rp = os.sep + '**' + os.sep
                all_files = glob.glob(td + rp + '*.*htm*', recursive=True)
                all_files.extend(glob.glob(td + rp + '*.*xml*', recursive=True))

                for ip_file in all_files:
                    xml_root = ET.parse(ip_file).getroot()
                    all_text = ET.tostringlist(xml_root, encoding='unicode', method='text')

                    for item in all_text:
                        for word in re.split(r'[\s—]', item):
                            word = re_strip.sub('', word)
                            # convert to ascii single quotes and lowercase the string for ref_words comparison
                            word_l = word.translate({0x2019:0x27}).lower()

                            if re_valid_words.search(word_l) and word_l not in ref_words:
                                if word in tpyo_words:
                                    tpyo_words[word] = tpyo_words[word] + 1
                                else:
                                    tpyo_words[word] = 1
    return tpyo_words


tpyo_words = tpyos(word_dir, docm_dir)

log_dir = str(datetime.datetime.now()).translate({0x20:0x5f, 0x3a:0x5f})
os.mkdir(log_dir)
tpyo_log = log_dir + os.sep + r'tpyo_words.log'
hyph_log = log_dir + os.sep + r'hyphenated_words.log'
with open(tpyo_log, 'w', encoding='UTF-8') as tw, open(hyph_log, 'w', encoding='UTF-8') as hw:
    for word in sorted(tpyo_words.keys(), key=str.lower):
        if '-' in word:
            print('{}: {}'.format(word, tpyo_words[word]), file=hw)
        else:
            print('{}: {}'.format(word, tpyo_words[word]), file=tw)


