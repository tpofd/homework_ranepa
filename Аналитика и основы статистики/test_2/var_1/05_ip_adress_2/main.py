flag = True
while flag:
    ip_address = input("Введите IP: ").split(".")
    count = 0
    if len(ip_address) == 4:
        for i in ip_address:
            if i.isdigit():
                if int(i) <= 255:
                    count += 1
                    if count == 4:
                        print("IP-адрес корректен")
                        flag = False
                else:
                    print("{num} превышает 255".format(
                            num=i
                        ), "\nПопробуйте снова")
            else:
                print("{num} - не целое/отрицательное число".format(
                        num=i
                    ), "\nПопробуйте снова")
    else:
        print("Адрес - это четыре числа, разделенные точками.\nПопробуйте снова")