import sys

def f(n, number):
    nb_list = list(str(number))
    for i in range(len(nb_list)):
        nb_list[i] = int(nb_list[i])
    result_list = list()
    for i in range(len(nb_list)):
        number = i
        new_list = list()
        for x in range(i, len(nb_list)):
            new_list = list()
            new_list.append(nb_list[i])
            result = nb_list[i]
            j = x+1
            while j < len(nb_list):
                if result + nb_list[j] > n:
                    result -= new_list[-1]
                    new_list.pop()
                    continue
                elif result + nb_list[j] == n:
                    new_list.append(nb_list[j])
                    if new_list not in result_list:
                        result_list.append(new_list)
                    break
                else:
                    result += nb_list[j]
                    new_list.append(nb_list[j])
                j+=1
    
    print(result_list)
