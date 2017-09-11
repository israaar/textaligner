# -*- coding: utf-8 -*-

import logging
from flask import Flask, render_template, jsonify, request
from werkzeug.exceptions import BadRequest
from langdetect import detect

from utils import setup_logger
from splitter.splitter import SentenceSplitter
from align import align_html

app = Flask(__name__,
            static_folder='site/static',
            template_folder='site/templates',)


splitters = {}
max_text_size = 500*1000


@app.route("/")
@app.route("/split")
def split_page():
    try:
        page = render_template('split.html')
        return page
    except:
        logging.exception('')
        raise


@app.route("/align")
def align_page():
    try:
        page = render_template('align.html')
        return page
    except:
        logging.exception('')
        raise


@app.route("/ajax_split", methods=['POST'])
def split():
    try:
        text = request.form.get('text', '')

        if len(text) > max_text_size:
            raise BadRequest('Text is too long, {} symbols is maximum'.format(max_text_size))
        if len(text) == 0:
            raise BadRequest('Text is empty')

        lang = detect(text)
        logging.info('Lang: %s, text to split: %s', text[:300], lang)

        splitter = splitters.get(lang)
        if splitter is None:
            splitter = SentenceSplitter(lang)
            splitters[lang] = splitter
        output_text = splitter.process_string(text)
        output_lang = lang
        return jsonify({'text': output_text, 'lang': output_lang})
    except:
        logging.exception('')
        raise


@app.route("/ajax_align", methods=['POST'])
def align():
    try:
        left_text = request.form.get('left_text', '')
        right_text = request.form.get('right_text', '')

        if len(left_text) == 0:
            raise BadRequest('Left text is empty')

        if len(right_text) == 0:
            raise BadRequest('Right text is empty')

        logging.info("Texts to align: '%s' vs '%s'", left_text[:300], right_text[:300])
        result = align_html(left_text, right_text)
        return jsonify({'aligned_text': list(result)})
    except:
        logging.exception('')
        raise


def main():
    setup_logger()
    app.run(host='0.0.0.0', port=8000, debug=True, use_reloader=True)

if __name__ == '__main__':
    main()
