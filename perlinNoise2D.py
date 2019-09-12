import matplotlib.pyplot as plt
import numpy as np
import copy

"""柏林噪声2D"""

permutation = [151, 160, 137, 91, 90, 15,  # arranged array of all numbers from 0-255 inclusive.
               131, 13, 201, 95, 96, 53, 194, 233, 7, 225, 140, 36, 103, 30, 69, 142, 8, 99, 37, 240, 21, 10, 23,
               190, 6, 148, 247, 120, 234, 75, 0, 26, 197, 62, 94, 252, 219, 203, 117, 35, 11, 32, 57, 177, 33,
               88, 237, 149, 56, 87, 174, 20, 125, 136, 171, 168, 68, 175, 74, 165, 71, 134, 139, 48, 27, 166,
               77, 146, 158, 231, 83, 111, 229, 122, 60, 211, 133, 230, 220, 105, 92, 41, 55, 46, 245, 40, 244,
               102, 143, 54, 65, 25, 63, 161, 1, 216, 80, 73, 209, 76, 132, 187, 208, 89, 18, 169, 200, 196,
               135, 130, 116, 188, 159, 86, 164, 100, 109, 198, 173, 186, 3, 64, 52, 217, 226, 250, 124, 123,
               5, 202, 38, 147, 118, 126, 255, 82, 85, 212, 207, 206, 59, 227, 47, 16, 58, 17, 182, 189, 28, 42,
               223, 183, 170, 213, 119, 248, 152, 2, 44, 154, 163, 70, 221, 153, 101, 155, 167, 43, 172, 9,
               129, 22, 39, 253, 19, 98, 108, 110, 79, 113, 224, 232, 178, 185, 112, 104, 218, 246, 97, 228,
               251, 34, 242, 193, 238, 210, 144, 12, 191, 179, 162, 241, 81, 51, 145, 235, 249, 14, 239, 107,
               49, 192, 214, 31, 181, 199, 106, 157, 184, 84, 204, 176, 115, 121, 50, 45, 127, 4, 150, 254,
               138, 236, 205, 93, 222, 114, 67, 29, 24, 72, 243, 141, 128, 195, 78, 66, 215, 61, 156, 180]


def fade(t):
    return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3


# 根据h%16的结果，随机选择一条标准梯度向量
def grad(h, x, y):
    s = h & 0x3
    if s == 0x0:
        return x + y
    elif s == 0x1:
        return -x + y
    elif s == 0x2:
        return x - y
    elif s == 0x3:
        return -x - y



def lerp(a, b, w):
    return a + (b - a) * w


class Perlin:
    def __init__(self, repeat = -1):
        self.p = permutation + permutation  # 用于挑选最终选用哪个梯度向量
        print(len(self.p))

        self.repeat = repeat

    # repeat是做什么的？
    def perlin(self, x, y):
        if self.repeat > 0:
            x = x % self.repeat
            y = y % self.repeat

        # 取x,y,z整数部分，并限制在0-255范围内
        xi = int(x) & 255
        yi = int(y) & 255

        # 取x,y,z小数部分
        xf = x - int(x)
        yf = y - int(y)

        """
        fade函数f(x)+f(1-x)在x<0,1>时十分接近于1，所以可以做插值
        u,v,w为小数部分在晶格中的位置，以此来确定噪声值。噪声值由晶格8个顶点决定
        """
        u = fade(xf)
        v = fade(yf)

        # 哈希函数(根据xi,yi,zi,产生一个伪随机的0-255值）
        # 确定一个晶格，晶格的唯一作用是确定一套梯度向量
        aa = self.p[self.p[xi] + yi]
        ab = self.p[self.p[xi] + self.inc(yi)]
        ba = self.p[self.p[self.inc(xi)] + yi]
        bb = self.p[self.p[self.inc(xi)] + self.inc(yi)]

        #选出一个晶格（为了确定标准梯度向量），三次插值选出一值
        y1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
        y2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)

        #选出真正的值
        return (lerp(y1, y2, v) + 1) / 2  # 保证其值在0-1中

    def perlinTest(self,x,y,frequency):
        return self.perlin(x*frequency,y*frequency)

    # octaves 倍频数量
    # persistence i = amplitude
    # def octavePerlin(self, x, y, z, octaves=1, persistence=2):
    #     total = 0
    #     frequency = 1 #频率
    #     amplitude = 1 #振幅
    #     maxValue = 0
    #
    #     for i in range(octaves):
    #         total += self.perlin(x * frequency, y * frequency, z * frequency) * amplitude
    #         maxValue += amplitude
    #         amplitude *= persistence
    #         frequency *= 2
    #
    #     return total / maxValue



    def inc(self, m):
        m += 1
        if self.repeat > 0:
            m %= self.repeat
        return m


if __name__ == "__main__":
    p = Perlin()

    # 二维柏林噪声
    x = np.arange(0,128,0.1)
    y = np.arange(0,128,0.1)
    z = np.zeros([x.size,y.size])
    count = 0
    for i in range(len(x)):
        for j in range(len(y)):
            z[i,j] = p.perlinTest(x[i],y[j],1)
            print(count)
            count+=1

    # p.perlinTest(0.9,1.1,0,1)


    plt.imshow(z, cmap="gray")
    plt.show()

