import os
import web
import base64
bytes
urls = (
        '/result/(.+)/(.+)/(.+)', 'url_out',
        '/servicelogs/(.+)', 'urlback'
        )

#app = web.application(urls, globals())
#app = app.wsgifunc()

class url_out:
    def POST(self,dpi,edicion,documento):
        data = web.data()
        if not os.path.exists('/home/inapdev/Docs/{}/{}'.format(dpi,edicion)):
            os.makedirs('/home/inapdev/Docs/{}/{}'.format(dpi,edicion))
            
        os.chdir('/home/inapdev/Docs/{}/{}'.format(dpi,edicion))
        with open('{}.pdf'.format(documento),'wb') as f:
            f.write(data)
        #f.close()
        return ''

class urlback:
    def POST(self,name):
        data = web.data()
        os.chdir('/home/inapdev/Docs/Logs')
        f = open('{}.txt'.format(name), 'a+')
        f.write(str(data))
        f.write(str("\n"))
        f.close()
        return ''

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
