import random


def num_list(zav):
    """
    Делает рандомное количество номеров деталей в виде списка, заводы вытаскивает из файла
    :param zav: str - адрес файла .csv
    :return: list
    """
    result_num_list = []
    with open(zav, 'r', encoding='utf-8') as fr:
        zav_list = fr.readlines()
        for _ in range(10):
            x = []
            zav = zav_list[random.randint(0, len(zav_list) - 1)].strip()
            x.append(str(zav))
            num = random.randint(0, 999999)
            x.append(str(num))
            god = random.randint(1970, 2022)
            x.append(str(god))
            result_num_list.append('-'.join(x))
    return result_num_list


def name_list(name):
    """
    Формирует список ФИО учеников из файла
    :param name: str - адрес файла .csv
    :return: list
    """
    with open(name, 'r', encoding='utf-8') as fw:
        name_list = fw.readlines()
    result_name_list = []
    for i in range(len(name_list)):
        name = name_list[i].strip().split(',')
        result_name_list.append(' '.join(name))
    return result_name_list


def rem(vid):
    """
    Рандомно выбирает ремонт из файла vidrem.csv
    :param vid: str - ссылка на файл
    :return: str
    """
    with open(vid, 'r', encoding='utf-8') as fr:
        vid_list = fr.readlines()
        random_rem = random.choice(vid_list)
        return random_rem


def tol_kp(tol):
    """
    Рандомно выбирает толщину обода КП
    :param tol: str файл tol_kp
    :return: str
    """
    with open(tol, 'r', encoding='utf-8') as fw:
        name_list = fw.readlines()
        tol_x = random.choice(name_list).strip()
        return tol_x


def name_det(name):
    """
    Рандомно выбирает ремонт из файла namedet.csv
    :param vid: str - ссылка на файл
    :return: list
    """
    with open(name, 'r', encoding='utf-8') as fr:
        name_list = fr.readlines()
        list_x = []
        for _ in range(10):
            random_det = random.choice(name_list)
            list_x.append(random_det)
        return list_x


def det_x(det, n):
    with open(det, 'r', encoding='utf-8') as fr:
        det_list = fr.readlines()
        x = []
        for _ in range(n):
            x_det = det_list[random.randint(0, len(det_list) - 1)].strip()
            x_det.split()
            xx = x_det.split('\t')
            x.append('-'.join(xx[:3]))
        return x


def det_udv_id(det, n):
    with open(det, 'r', encoding='utf-8') as fr:
        det_list = fr.readlines()
        x = []
        for _ in range(n):
            x_det = det_list[random.randint(0, len(det_list) - 1)].strip()
            x_det.split()
            xx = x_det.split('\t')
            x.append(''.join(xx[3]))
        return x


def dog_x(dog, n):
    """
    Рандомно выбирает n договоров из списка dog.csv
    :param dog:
    :return:
    """
    with open(dog, 'r', encoding='utf-8') as fr:
        det_list = fr.readlines()
        x = []
        for _ in range(n):
            x_dog = det_list[random.randint(0, len(det_list) - 1)].strip()
            x_dog.split()
            xx = x_dog.split('\t')
            x.append('-'.join(xx))
        return x


if __name__ == '__main__':
    det = 'file/det.csv'
    print(det_udv_id(det, 2))