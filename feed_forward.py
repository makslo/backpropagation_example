import math

class FeedForwardNN:
    def __init__(self):
        self.eta = 0.5
        self.t = [0.01, 0.99]
        self.i = [0.05, 0.1]
        self.w1 = [0.15, 0.2, 0.25, 0.3]
        self.w2 = [0.4, 0.45, 0.50, 0.55]
        self.b = [0.35, 0.6]

ffnn = FeedForwardNN()

for x in range(0, 10000):

  net_h1 = w1*i1+w2*i2+b1
  out_h1 = 1/(1+math.exp(-net_h1))

  net_h2 = w3*i1+w4*i2+b1
  out_h2 = 1/(1+math.exp(-net_h2))

  net_o1 = w5*out_h1+w6*out_h2+b2
  out_o1 = 1/(1+math.exp(-net_o1))

  net_o2 = w7*out_h1+w8*out_h2+b2
  out_o2 = 1/(1+math.exp(-net_o2))

  e_total = 0.5*math.pow((t1-out_o1),2)+0.5*math.pow((t2-out_o2),2)

  de_dw5 = (out_o1-t1)*out_o1*(1-out_o1)*out_h1
  w5_new = w5-eta*de_dw5

  de_dw6 = (out_o1-t1)*out_o1*(1-out_o1)*out_h2
  w6_new = w6-eta*de_dw6

  de_dw7 = (out_o2-t2)*out_o2*(1-out_o2)*out_h1
  w7_new = w7-eta*de_dw7

  de_dw8 = (out_o2-t2)*out_o2*(1-out_o2)*out_h2
  w8_new = w8-eta*de_dw8

  de_dw1 = (((out_o1-t1)*out_o1*(1-out_o1)*w5)+((out_o2-t2)*out_o2*(1-out_o2)*w7))*out_h1*(1-out_h1)*i1
  w1_new = w1-eta*de_dw1

  de_dw2 = (((out_o1-t1)*out_o1*(1-out_o1)*w5)+((out_o2-t2)*out_o2*(1-out_o2)*w7))*out_h1*(1-out_h1)*i2
  w2_new = w2-eta*de_dw2

  de_dw3 = (((out_o1-t1)*out_o1*(1-out_o1)*w6)+((out_o2-t2)*out_o2*(1-out_o2)*w8))*out_h2*(1-out_h2)*i1
  w3_new = w3-eta*de_dw3

  de_dw4 = (((out_o1-t1)*out_o1*(1-out_o1)*w6)+((out_o2-t2)*out_o2*(1-out_o2)*w8))*out_h2*(1-out_h2)*i2
  w4_new = w4-eta*de_dw4

  w1 = w1_new
  w2 = w2_new
  w3 = w3_new
  w4 = w4_new

  w5 = w5_new
  w6 = w6_new
  w7 = w7_new
  w8 = w8_new

print("o1: %s" % out_o1)
print("o2: %s" % out_o2)
print("error: %s" % e_total)
