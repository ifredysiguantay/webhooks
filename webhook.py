import web
import os
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
        f = open('test.pdf','w')
        print('\n\n\n\n val of data',data)
        print('\n\n\n\n\n',type(data))
        for line in open(data , 'wb').readlines():
            f.write(line)
        f.close()
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
