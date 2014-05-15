"""
    mrbob_flask.hooks

    custom hooks for mrbob template files
"""
from datetime import date

class FakeCfg(object):
    def __init__(self):
        self.variables = {'project.type':'app'}

        self.template_dir = '/root'



def set_template(cfg):
    template_base = '/root/projects/github/mrbob-flask-templates/mrbob_flask/'
    template_map = {
            'small_app':template_base+'small_app',
            'app':template_base+'app',
            'package':template_base+'package',
            'project':template_base+'project',
            'blueprint':template_base+'blueprint'
    }

    
    template = cfg.variables['project.type']
    cfg.template_dir = template_map[template]

def set_year_default(cfg,q):
    q.default = date.today().year


