import matplotlib.pyplot as plt
import math

divs = [16, 256, 1024]
exe_time = ['O(Log n)', 'O(n)', 'O(n * Log n)', 'O(n^2)']

system = True

while system:
    op_results = []
    print("1 - O(Log n)\n"
          "2 - O(n)\n"
          "3 - O(n * Log n)\n"
          "4 - O(n^2)\n"
          "0 - Exit")
    choice = input("Choose one Big O notation:")


    def log_time():
        for i in divs:
            result = math.log2(i)
            result = result / 10
            op_results.append(result)
        return op_results


    def linear_time():
        for i in divs:
            result = i / 10
            op_results.append(result)
        return op_results


    def n_times_log_n():
        for i in divs:
            result = i * math.log2(i)
            result = result / 10
            op_results.append(result)
        return op_results


    def exp_log():
        for i in divs:
            result = math.pow(i, 2)
            result = result / 10
            op_results.append(result)
        return op_results


    if choice == "1":
        big_o_exe = log_time()

        plt.plot(divs, big_o_exe)
        plt.ylabel('Divisions')
        plt.xlabel(exe_time[int(choice) - 1])
        plt.show()
    elif choice == "2":
        big_o_exe = linear_time()

        plt.plot(divs, big_o_exe)
        plt.ylabel('Divisions')
        plt.xlabel(exe_time[int(choice) - 1])
        plt.show()

    elif choice == "3":
        big_o_exe = n_times_log_n()

        plt.plot(divs, big_o_exe)
        plt.ylabel('Divisions')
        plt.xlabel(exe_time[int(choice) - 1])
        plt.show()

    elif choice == "4":
        big_o_exe = exp_log()

        plt.plot(divs, big_o_exe)
        plt.ylabel('Divisions')
        plt.xlabel(exe_time[int(choice) - 1])
        plt.show()

    elif choice == "0":
        system = False

    else:
        print("Opção inválida!")
