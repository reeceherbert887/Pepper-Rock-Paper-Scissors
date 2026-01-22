import urllib

class myclass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tablet = None

        def onLoad(self):
            try:
                self.tablet = self.session.service("ALTabletService")
            except:
                self.tablet = None


   # Input: onScoreText (String)
    def onInput_onScoreText(self, text):
        if not self.tablet:
            return

        text = str(text)

        html = """
        <html>
          <body style="font-family: Arial; text-align:center; margin-top:80px;">
            <h2>Rock Paper Scissors</h2>
            <div style="font-size:36px;">{}</div>
          </body>
        </html>
        """.format(text)

        url = "data:text/html;charset=utf-8," + urllib.quote(html)
        self.tablet.showWebview(url)