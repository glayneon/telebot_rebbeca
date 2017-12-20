# define variables

class DEBUG(object):
    '''class variables for DEBUG mode'''

    import os
    import time

    _FILE = 'Rebbeca_' + time.strftime('%Y%m%d%H%M%S') + '_pid_' + str(os.getpid()) + '.debug'



class LOG4(object):
    '''class variables for LogALL class'''

    _LOGFILE = 'Rebbeca_telebot.log'
    _MAXBYTES = 1024 * 1024 * 5
    _ROTATE_CNT = 4


class DB4(object):
    '''class variables for sqlite3 class'''

    _DBNAME = 'rebbeca.db'

    _INIT_AMOLANG = '''create table amolang (
    amolang_id integer primary key autoincrement,
    amolang_text text not null
    )'''

    _INIT_TODO = '''create table todo (
    todo_id integer primary key autoincrement,
    todo_text text not null
    )'''


class INFOS(object):
    '''class variables for telebot Rebbeca'''

    _ADMIN_ID = {
    }
    _TOKEN = ''

    _PUB_ROOMS = []

    _AMULANG = [
'정말.. 지긋지긋 하군요..',
'언제까지.. 절 붙잡을 수 있을것 같나요...?',
'오늘은.. 더 이상 보고 싶지 않군요..',
'당신의 그... 뻔한 거짓말... 지긋지긋 하군요..',
'잊지 말아요.. 난 당신의 돈을 사랑할 뿐이에요..!',
'지금은 당신 뜻대로 따르죠.. 하지만 내 맘은 이미 떠났다구요..',
'이제 좀 쉬고 쉽네요.. 또 시킬게 있나요..?', '당신 얼굴을 봤더니.. 현기증이 나네요. 좀 쉬어야 겠에요..' ]

    _INTRO = []

