from utils import getImage, getAA_01

def main():
    # RESIZE_RATE * 100 = PERSENT
    RESIZE_RATE = 0.2  # 원본의 20% (축소)

    img, HEI, WID = getImage('./img/lena.png', RESIZE_RATE)

    for h in range(HEI):
        for w in range(WID):
            print(getAA_01(img[h][w]), end="")
        print()

if __name__ == '__main__':
    main()