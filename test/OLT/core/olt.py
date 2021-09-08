import telnetlib


class OLT(object):
    def __init__(self):


    def judgement_type(selfe):
        pass

    def make_connection(self,IP,username,password='esnw'):
        ip_add = '10.159.0.'
        tn = telnetlib.Telnet(ip_add, 23)
        tn.set_debuglevel(10)





    def interactive(cmd):
        menu = '''
        1.查询ONU上线情况
        2.查询ONU口子vlan
        3.查询ONU光功率
        4.查询PON口配置
    
        5.修改ONU口子vlan
        6.
        '''

        menu_dic = {
            '1': "query_online",
            '2': "query_vlan",
            '3': "query_transceiver",
            '4': "query_PONconfig",
            '5': "modify_config",

        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            user_option = input("输入序号继续下文:").strip()
            if user_option in menu_dic:
                menu_dic[user_option]()
            else:
                print("\033[1m;31Option does not exist!\033[0m")



    def query_online(self,args):
        pass


    def start(self):
        IP = input("请输入IP地址：",).strip()
        username =  ("请输入用户名：").strip()
        if len(username)==0:
            username = 'admin'
