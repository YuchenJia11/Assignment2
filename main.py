import task_3 as tk3


def main():
    itn_file = '/Users/jiayuchen/Desktop/Material/itn/solent_itn.json'
    user = (440000, 87000)
    hignest_point = (400000, 90000)
    nearest_user, nearest_hp, if_samepoint = tk3.itn(user, hignest_point, itn_file)
    print(nearest_user, nearest_hp, if_samepoint)


if __name__ == '__main__':
    main()
