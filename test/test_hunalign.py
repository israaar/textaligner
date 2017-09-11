# -*- coding: utf-8 -*-
import os.path
import unittest
import sys
from pprint import  pprint
import operator
sys.path.append(os.path.abspath('..'))

from align import align, align_html
from hunalign import align_with_lang


class TestHunalign(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        pass

    def testUnalignedText(self):
        left_text = \
            """シャーロックホームズにとって、彼女はいつも「あの女」である。ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。しかし、彼はアイリーン・アドラーに愛のような激情は一切感じていなかった。すべての激情は、そして特に愛というものは、 相容れなかった、彼の冷静で厳格だが見事に調整された心とは。
            """
        right_text = \
"""TO SHERLOCK HOLMES she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind.
"""

        split_text = align(left_text, right_text)
        split_text = list(split_text)
        self.assertEqual(
            split_text,
            [('シャーロックホームズにとって、彼女はいつも「あの女」である。',
              'TO SHERLOCK HOLMES she is always the woman.'),
             ('ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。',
              'I have seldom heard him mention her under any other name.'),
             ('彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。',
              'In his eyes she eclipses and predominates the whole of her sex.'),
             ('しかし、彼はアイリーン・アドラーに愛のような激情は一切感じていなかった。',
              'It was not that he felt any emotion akin to love for Irene Adler.'),
             ('すべての激情は、そして特に愛というものは、 相容れなかった、彼の冷静で厳格だが見事に調整された心とは。',
              'All emotions, and that one particularly, were abhorrent to his cold, '
              'precise but admirably balanced mind.'),
             ('', '')]
        )

    def testAlignedText(self):
        left_text = \
"""シャーロックホームズにとって、彼女はいつも「あの女」である。
ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。
彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。
しかし、彼はアイリーン・アドラーに愛のような激情は一切感じていなかった。
すべての激情は、そして特に愛というものは、 相容れなかった、彼の冷静で厳格だが見事に調整された心とは。"""

        right_text = \
"""TO SHERLOCK HOLMES she is always the woman.
I have seldom heard him mention her under any other name.
In his eyes she eclipses and predominates the whole of her sex.
It was not that he felt any emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind."""

        split_text = align_with_lang('ja', left_text, 'en', right_text)
        split_text = list(split_text)
       # pprint(split_text)
        self.assertEqual(
            split_text,
            [('シャーロックホームズにとって、彼女はいつも「あの女」である。',
              'TO SHERLOCK HOLMES she is always the woman.'),
             ('ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。',
              'I have seldom heard him mention her under any other name.'),
             ('彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。',
              'In his eyes she eclipses and predominates the whole of her sex.'),
             ('しかし、彼はアイリーン・アドラーに愛のような激情は一切感じていなかった。',
              'It was not that he felt any emotion akin to love for Irene Adler.'),
             ('すべての激情は、そして特に愛というものは、 相容れなかった、彼の冷静で厳格だが見事に調整された心とは。',
              'All emotions, and that one particularly, were abhorrent to his cold, '
              'precise but admirably balanced mind.')]
        )
       # pprint(list(split_text))

    def testHtmlText(self):
        left_text = \
            """シャーロックホームズにとって、彼女はいつも「あの女」である。<br>ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。<br><br>彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。
            """

        right_text = \
            """TO SHERLOCK HOLMES she is always the woman.<br>I have seldom heard him mention her under any other name.<br><br>In his eyes she eclipses and predominates the whole of her sex."""

        split_text = align_html(left_text, right_text)
        split_text = list(split_text)
        self.assertEqual(
            split_text,
            [('シャーロックホームズにとって、彼女はいつも「あの女」である。',
              'TO SHERLOCK HOLMES she is always the woman.'),
             ('ホームズが彼女を他の名前で呼ぶのはほとんど聞いたことがない。',
              'I have seldom heard him mention her under any other name.'),
             ('彼の目には、 彼女がそびえ立って女という性全体を覆い隠している。',
              'In his eyes she eclipses and predominates the whole of her sex.'),
             ('しかし、彼はアイリーン・アドラーに愛のような激情は一切感じていなかった。',
              'It was not that he felt any emotion akin to love for Irene Adler.')]
        )

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHunalign)
    unittest.TextTestRunner(verbosity=2).run(suite)
