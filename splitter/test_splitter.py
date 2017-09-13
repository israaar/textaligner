# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
from splitter import SentenceSplitter, get_command_args
import regex

class TestSplitter(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.test_number = 0
        self.en_splitter = SentenceSplitter('en')

    def testPosixClass(self):
        m = regex.match('\p{Po}', '。', regex.UNICODE)
        self.assertIsNotNone(m)
        m = regex.match('\p{Dash_Punctuation}', '—')
        self.assertIsNotNone(m)
        m = regex.match('\s', '\xA0')
        self.assertIsNotNone(m)

    def testNonPeriodEndAndCapital(self):

        text_src = 'Mr Dursley was the director? Of a firm called.'
        text_exp = 'Mr Dursley was the director?\nOf a firm called.\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)
        text_src = 'Mr Dursley was the director?Of a firm called.'
        text_exp = 'Mr Dursley was the director?\nOf a firm called.\n'
      #  res = self.en_splitter.process_string(text_src)
      #  self.assertEqual(res, text_exp)
        text_src = 'Mr Dursley was the director? "Of a firm called."'
        text_exp = 'Mr Dursley was the director?\n"Of a firm called."\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testMultiDotEndAndCapital(self):
        text_src = 'Mr Dursley was the director... Of a firm called.'
        text_exp = 'Mr Dursley was the director...\nOf a firm called.\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testEndWithingQuote(self):
        text_src = 'Mr Dursley was the director." Of a firm called.'
        text_exp = 'Mr Dursley was the director."\nOf a firm called.\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testSimpleEng(self):
        text_src = 'Mr Dursley was the director. Of a firm called . Grunnings, which made drills.'
        text_exp = 'Mr Dursley was the director.\nOf a firm called .\nGrunnings, which made drills.\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testNonBreakingChar(self):
        text_src = 'Mr. Dursley was the director. Of a firm called .'
        text_exp = 'Mr. Dursley was the director.\nOf a firm called .\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testQuotes(self):
        text_src = '"William Crosby, why, what brings you out in such a storm as this? Strip off your coat, and draw up to the fire, can\'t ye?"'
        text_exp = '"William Crosby, why, what brings you out in such a storm as this?\nStrip off your coat, and draw up to the fire, can\'t ye?"\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testKorean(self):
        text_src = '1년 만에 완전체로. 돌아온 크레용팝의. 두 번째 미니앨범 ‘FM’!'
        text_exp = '1년 만에 완전체로.\n돌아온 크레용팝의.\n두 번째 미니앨범 ‘FM’!\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testChinese(self):
        text_src = '父亲说：“这得说说……” “是得说说。”娘说。说说，什么叫“说说”，说什么呢？'
        text_exp = '父亲说：“这得说说……” “是得说说。\n”娘说。\n说说，什么叫“说说”，说什么呢？\n'
        res = self.en_splitter.process_string(text_src)
        self.assertEqual(res, text_exp)

    def testJapanese(self):
        text_src = '『ハア。』と老女は當惑した樣に眼をしよぼつかせた。『無い筈はないでせう。尤も此邊では、戸籍上の名と家で呼ぶ名と違ふのがありますよ。』と、健は喙を容れた。'
        text_exp = '『ハア。\n』と老女は當惑した樣に眼をしよぼつかせた。\n『無い筈はないでせう。\n尤も此邊では、戸籍上の名と家で呼ぶ名と違ふのがありますよ。\n』と、健は喙を容れた。\n'
        res = self.en_splitter.process_string(text_src)
        #print(res)
        self.assertEqual(res, text_exp)

    def testRussian(self):
        text_src = 'Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил. — Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.'
        text_exp = 'Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил.\n— Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.\n'
        res = self.en_splitter.process_string(text_src)
        #print(res)
        self.assertEqual(res, text_exp)
        text_src = 'Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил. — Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.\n\n\n\n\n'
        text_exp = 'Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил.\n— Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.\n\n\n'
        res = self.en_splitter.process_string(text_src)
        #print(res)
        self.assertEqual(res, text_exp)
        text_src = """Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил. — Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.



"""
        text_exp = """Впрочем, Дик Маркем, высокий молодой человек с довольно-таки буйным воображением, едва ли все это заметил.\n— Знаешь, мы жутко опаздываем, — беззаботным девичьим тоном напомнила Лесли, задыхаясь и почти смеясь.


"""
        res = self.en_splitter.process_string(text_src)
        #print(res)
        self.assertEqual(res, text_exp)
        text_src = """— Через минуту дождь хлынет, — заключила она. — Сомневаюсь, что крикетный матч состоится.
И… — И что?
— Я хочу пойти к предсказателю судеб, — объявила Лесли.
"""
        text_exp = """— Через минуту дождь хлынет, — заключила она.
— Сомневаюсь, что крикетный матч состоится.
И… — И что?
— Я хочу пойти к предсказателю судеб, — объявила Лесли.


"""
        res = self.en_splitter.process_string(text_src)
        print(res)
        self.assertEqual(res, text_exp)

    def testCommandLine(self):
        language, quiet, infile, outfile = get_command_args(['inputfile.txt'])
        self.assertEqual('en', language)
        self.assertFalse(quiet)
        self.assertEqual('inputfile.txt', infile)
        self.assertIsNone(outfile)

        language, quiet, infile, outfile = get_command_args(['-l', 'ru', 'infile.txt', 'outfile.txt'])
        self.assertEqual('ru', language)
        self.assertFalse(quiet)
        self.assertEqual('infile.txt', infile)
        self.assertEqual('outfile.txt', outfile)

    def testLargeText(self):
        text = \
"""第一章

　あとから考えてみれば、バザーでの夏の嵐、占い師のテントや射的場で起こったこと、そのほかいくつかのできごとは、事件の前兆だったのかも知れないと、ディック・マーカムには思い当たるのだった。
　しかし当時は、天候のことなどあまり気にとめていなかった。彼はそれほど有頂天だったのだ。
　彼とレスリーがグリフィンとトネリコの紋章で飾られた石柱のある、開放された門を入ると、向こうはアッシュ・ホールの敷地へと続いている。よく刈り込んだ芝生には、ごてごてした屋台と縞模様のテントが並んでいる。背後には樫の木がおいしげり、周囲には赤い煉瓦を積んだホールの低い境界線が長く続いていた。
　四、五年もたてば、この光景は苦々しくも懐かしさをもって、ディック・マーカムの脳裏に浮かぶことだろう。みずみずしい緑に燃えるイングランド。白いフランネルと、もの憂《う》い午後のイングランド。このイングランドが、いかなるたわごとのせいであれ、よりよき世界を失うことのないように祈りたい。ヒトラーの戦争がはじまる一年ほど前、そこには潤沢さがあった。その豊かさは、現アッシュ男爵ジョージ・コンヴァースの資産には当てはまらなかったが。しかし、いささか想像力過剰な長身の青年、ディック・マーカムはそんなものにはほとんど目もくれなかった。
「あら、かなり遅れてしまったわ」レスリーは息をはずませ、なかば笑いながらあっけらかんといった。
　二人はいくぶん足を急がせていたが、しばし立ち止まった。
　暑い午後の大気を涼しい突風が吹き抜け、芝生を激しく荒らしていった。レスリーはうすく透いたピクチャー・ハット〔花や羽根で飾ったつばの広い帽子〕を両手であわてて押さえた。けむりのようなゆるやかに流れる雲で、空は夕方みたいに暗くなった。
「ねえ、いま何時ごろ？」とディック。
「とにかく三時は過ぎたわ」
　彼は前方に顎をしゃくった。嵐の影はサングラスを通した日光のごとく、あたりを悪夢にも似た非現実なものに見せている。芝生には何ひとつ動くものがない。突風で人々が落ち着かなくなったせいか、テントや屋台は閑散としていた。
「でも……みんなどうしたのだろう？」
「おそらくクリケットの試合よ、ディック。急がなくちゃ、レディ・アッシュやミセス・プライスがおかんむりよ」
「こんなことで？」
「うそよ」レスリーは笑った。「そんなことはないわ」
　帽子の縁に手をやり、笑いながら息をはずませている彼女をディックは見つめた。その笑いを浮かべた口元とうらはらに、やりきれないほど真剣なまなざしを見てとった。すべての想念と感情が褐色の眼に集まっているようだ。その眼は昨夜の打ち明け話を思い出させてくれた。
　その上げた腕にもさりげない優雅さがあり、強い風のせいで白いフロックは身体の線をくっきり見せている。彼女のちょっとした唇のわななき、眼くばりにさえたまらない魅力があり、そのたびごと、さまざまな仕草がディックの脳裏に焼きつけられた。
　その午後、かたくるしいガーデン・パーティ会場、アッシュ邸の静かな庭園に入ると、レディ・アッシュはうつろな眼で二人を迎えてくれた。うわべだけでもしきたりにこだわるマーカムは、人目もはばからずレスリー・グラントを抱き、口づけする気にはならなかった。
　このとき風は庭園を吹きすさび、空はますます暗くなった。二人の会話は（だれも水をさすものがいないので）いささか取りとめのないものだった。
「愛してる？」
「もちろん。きみは？」
　昨夜からあきもせぬ同じ睦言《むつごと》のくりかえしだった。ところがそのたびごとに新しい発見があるようで、それを実感してはめくるめく想いに浸っていた。ディックは自分たちがどこにいるかをうつつにさとって、とうとう腕を解くと空を仰いだ。
「ぼくらもあのくだらないクリケット試合に行かなくてはならないのかい？」
　レスリーはためらった。極度に高揚した感情が眼から消え、空を見上げた。
「まもなく雨が降ってくるわよ。クリケット試合ができるかどうか。それに……」
「それに、なんだい？」
「占い師に見てもらいたいの」とレスリー。
"""
        res = self.en_splitter.process_string(text)
        #pprint(res)
        self.assertEqual(res.count('\n'), 49)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSplitter)
    unittest.TextTestRunner(verbosity=2).run(suite)