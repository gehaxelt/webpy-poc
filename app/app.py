import web
from web import form
web.config.debug = False
urls = (
  '/', 'index'
)
app = web.application(urls, locals())
render = web.template.render('templates/')

template_Form = form.Form(
    form.Password("template", description="Template"),
    form.Button("submit", type="submit", description="Submit")
)

class index:
    def GET(self):
        f = template_Form()
        return render.index(f)

    def POST(self):
        f = template_Form()
        if not f.validates():
            return render.index(f)
        i = web.input()
        template = i.template
        try:
            template = web.template.Template(f"Your template is: {template}")()
        except Exception as  e:
            return str(e)
        return template
application = app.wsgifunc()
if __name__ == "__main__":
    app.run()