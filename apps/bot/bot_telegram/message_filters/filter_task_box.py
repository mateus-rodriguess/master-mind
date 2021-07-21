import re
from apps.bot.bot_telegram.services.task_box.task_box import \
    add_metas_task_box


def filter_task_box(message, id_user):
    """
        ⏱
        é isso ai
        :param message:
        :param id_user:
        :return: lista
    """
    global metas_pro, start
    if "ProMode" in message:
        pro_mode = re.search(r"ProMode", message)
        start = pro_mode.start()
        end = len(message)
        message_pro_mode = message[start:end]
        meta_pro_list_incomplete = re.findall("⏱", message_pro_mode)
        metas_pro = len(meta_pro_list_incomplete)

    if "Metas" in message:
        metas_list = re.findall("⏱", message[0:start])
        metas = len(metas_list)
    else:
        return False

    return add_metas_task_box(id_user, metas, metas_pro)




