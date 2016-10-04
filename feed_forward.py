import math, random

class Neuron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def set_out(inp):
        s = sum([i*w for i,w in zip(inp,self.w)])+b
        self.inp = inp
        self.out = 1/(1+math.exp(-s))
        self.diff = self.out*(1-self.out)
        return self.out

# fully connected multilayer feed forward network
class FeedForwardNN:
    def __init__(self, target, inputs, eta):
        self.eta = eta
        self.inputs = inputs
        self.layers = []
        self.target = target
        self.connections = []
        self.out = []

    def get_n(layer,pos):
        return layers[layer][pos]

    def add_layer(layer):
        self.layers.append(layer)

    def predict():
        inp = self.inputs
        for layer in self.layers:
            out = []
            for n in layer:
                out.append(n.set_out(inp))
            inp = out
        self.out = inp
        return self.out

    def error():
        return 0.5*sum([math.pow((t-o),2) for t,o in zip(self.target, self.out)])

    def train():
        d_e = [-(t-o) for t,o in zip(self.target, self.out)]
        updates = []
        for layer in layers:
            d_layer = [map(lambda i: i*n.diff, n.inp) for n in layer]
            updates.append([-self.eta*d for d in d_layer])


ffnn = FeedForwardNN(target = [0.01, 0.99], inputs = [0.05, 0.1], eta = 0.5)
ffnn.add_layer([Neuron([random.random()],random.random()] random.random()), Neuron([random.random()],random.random()] random.random()))
ffnn.add_layer([Neuron([random.random()],random.random()] random.random()), Neuron([random.random()],random.random()] random.random()))


for x in range(0, 10000):
    ffnn.predict()
    print(ffnn.error())
         = d_e[0]*n0.diff*n0.inp[0]
  de_dw5 = (out_o1-t1)*out_o1*(1-out_o1)*out_h1
  w5_new = w5-eta*de_dw5

  de_dw6 = (out_o1-t1)*out_o1*(1-out_o1)*out_h2
  w6_new = w6-eta*de_dw6

  de_dw7 = (out_o2-t2)*out_o2*(1-out_o2)*out_h1
  w7_new = w7-eta*de_dw7

  de_dw8 = (out_o2-t2)*out_o2*(1-out_o2)*out_h2
  w8_new = w8-eta*de_dw8

  (d_e[0]*n0.diff*n0.weights[0]+d_e[1]*n1.diff*n1.weights[0])*nh0.diff*inpt[0]
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
