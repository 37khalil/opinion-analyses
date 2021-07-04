from facebook_scraper import get_posts
import io

with io.open('arabic_fb.json' , "w" , encoding='utf-8') as file:
    file.write("[ \n")
    for post in get_posts('CSMDMaroc'):
        if (post['text'] is not None):
            file.write('{"content": "'+post['text']+'" , \n "date" : "'+(str)(post['time'].strftime('%x'))+'"},\n')
    for post in get_posts('النمودج-التنموي-الجديد-والهيئات-السياسية-أية-علاقة--109621010573656'):
        if (post['text'] is not None):
            file.write(
                '{"content": "' + post['text'] + '" , \n "date" : "' + (str)(post['time'].strftime('%x')) + '"},\n')
    for post in get_posts('ندوة-حول-موضوع-الشباب-والنموذج-التنموي-الجديد-انتظارات-ورهانات-200215-108733884030065'):
        if (post['text'] is not None):
            file.write(
                '{"content": "' + post['text'] + '" , \n "date" : "' + (str)(post['time'].strftime('%x')) + '"},\n')
    for post in get_posts('صدى-العالم-القروي-في-النموذج-التنموي-الجديد-102243404865816'):
        if (post['text'] is not None):
            file.write(
                '{"content": "' + post['text'] + '" , \n "date" : "' + (str)(post['time'].strftime('%x')) + '"},\n')
    for post in get_posts('Idees2019'):
        if (post['text'] is not None):
            file.write(
                '{"content": "' + post['text'] + '" , \n "date" : "' + (str)(post['time'].strftime('%x')) + '"},\n')
    for post in get_posts('MoDevMaroc'):
        if (post['text'] is not None):
            file.write(
                '{"content": "' + post['text'] + '" , \n "date" : "' + (str)(post['time'].strftime('%x')) + '"},\n')
    file.write("]")