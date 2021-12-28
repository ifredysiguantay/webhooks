import os
import web
import base64
bytes
urls = (
        '/result', 'url_out',
        '/servicelogs', 'urlback'
        )

#app = web.application(urls, globals())
#app = app.wsgifunc()

class url_out:
    def POST(self):
        data = web.data()
        os.chdir('/home/inapenc/signbox-files')
        with open("test.pdf",'wb') as f:
            f.write(base64.b16decode(data))
        #f.close()
        return ''

class urlback:
    def POST(self):
        data = web.data()
        os.chdir('/home/inapenc/signbox-files/logs')
        f = open('logs.txt', 'a+')
        f.write(str(data))
        f.write(str("\n"))
        f.close()
        return ''

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
