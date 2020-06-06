import random as ran

if __name__ == '__main__':
    def main():

        random_num = ran.randint(1, 100)
        i = 1

        while True:
            input_num = int(input())
            if input_num > random_num:
                print("Down")
            elif input_num < random_num:
                print("Up")
            elif input_num == random_num:
                print("{}회째 정답".format(i))
                break
            else:
                print("잘못된 접근입니다.")

            i += 1

    main()
