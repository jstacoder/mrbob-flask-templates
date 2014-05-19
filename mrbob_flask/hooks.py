"""
    mrbob_flask.hooks

    custom hooks for mrbob template files
"""
from mrbob.configurator import Question,Configurator
import mrbob.bobexceptions as mrbob
from datetime import date

# for testing
class FakeCfg(object):
    def __init__(self):
        self.variables = {'project.type':'app'}

        self.template_dir = '/root'

# pre-render hooks
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
    
def dynamic_delete(cfg):
    filename = cfg.templateconfig.get('delete_file','')
    if filename and os.path.exists(filename):
        os.remove(filename)

#pre ask question hooks
def set_year_default(cfg,q):
    q.default = date.today().year

def skip_question(cfg,question):
    raise mrbob.SkipQuestion

def start_question_loop(cfg,question):
    pass

def set_server_root_from_name(cfg,question):
    if cfg.variables['project.server_root']:
        if question.extras.prefix:
            question.default = os.path.join(question.extras.prefix,cfg.variables['project.server_root'])

# post_ask_questions
def quit(cfg,q,a):
    if cfg.mrbobconfig.stop_question == q:
        for q in range(len(cfg.questions)):
            cfg.questions[q].pre_ask_question = 'flask_mrbob.hooks:skip_question'

def change_template_dir(cfg,question,answer):
    if answer in question.extras.dirs.split(';'):
        cfg.template_dir = os.path.abspath(answer)
    return answer

def load_questions(cfg,question,answer):
    questions_map = {
        'flask-project':flask_project,
        'flask-app': flask_app,
        'flask-small':flask_small,
    }
    if answer in questions_map.keys():
        for question in questions_map[answer]:
            cfg.questions.insert(0,Question(**question))
    else:
        raise mrbob.ValidationError('need to choose from an installed template')

    

