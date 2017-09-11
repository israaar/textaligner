
import logging
import re

from langdetect import detect
from hunalign import align_with_lang
from splitter.splitter import SentenceSplitter


re_br = re.compile('<br>')

def align(left_text, right_text):
    left_text = left_text.strip()
    right_text = right_text.strip()

    left_lang = detect(left_text)
    logging.info("Text: '{}', detected language: {}'", left_text[0:10], left_lang)
    right_lang = detect(right_text)
    logging.info("Text: '{}', detected language: {}'", right_text[0:10], right_lang)

    left_splitter = SentenceSplitter(left_lang)
    left_text = left_splitter.process_string(left_text)
    right_splitter = SentenceSplitter(right_lang)
    right_text = right_splitter.process_string(right_text)

    return align_with_lang(left_lang, left_text, right_lang, right_text)


def align_html(left_text, right_text):
    left_text = re_br.sub('\n', left_text)
    right_text = re_br.sub('\n', right_text)
    return align(left_text, right_text)
    #for split_text in align(left_text, right_text):
    #    yield split_text[0], split_text[1]
