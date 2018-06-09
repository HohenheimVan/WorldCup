import  datetime
import locale


# d = datetime.datetime.now()
# print(d.strftime("%A"))
# locale.setlocale(locale.LC_TIME, 'pl_PL.utf8')
# print(d.strftime("%A"))
#

groups = {
    'group_a': 'a',
    'group_b': 'b',
    'group_c': 'Team.objects.filter(group=)',
    'group_d': 'Team.objects.filter(group=)',
    'group_e': 'Team.objects.filter(group=)',
    'group_f': 'Team.objects.filter(group=)',
    'group_g': 'Team.objects.filter(group=)',
    'group_h': 'Team.objects.filter(group=)'
}
print(groups[1])