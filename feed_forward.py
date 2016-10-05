import math, random as rd
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, size):
        self.weights = [rd.random() for _ in range(size)]
        self.b = rd.random()

    def set_out(self,inp):
        s = sum([i*w for i,w in zip(inp,self.weights)])+self.b
        self.inp = inp
        self.out = 1/(1+math.exp(-s))
        return self.out

    def set_diff(self,d):
        self.diff = d*self.out*(1-self.out)

    def update(self,eta):
        self.weights = [w - eta*self.diff*i for w,i in zip(self.weights,self.inp)]

# fully connected multilayer feed forward network
class FeedForwardNN:
    def __init__(self, target, inputs, eta):
        self.eta = eta
        self.inputs = inputs
        self.layers = []
        self.target = target
        self.out = []

    def add_layer(self,layer):
        self.layers.append(layer)

    def predict(self):
        inp = self.inputs
        for layer in self.layers:
            out = []
            for n in layer:
                out.append(n.set_out(inp))
            inp = out
        self.out = inp
        return self.out

    def error(self):
        return 0.5*sum([math.pow((t-o),2) for t,o in zip(self.target, self.out)])

    def update(self):
        for layer in self.layers:
            for n in layer:
                n.update(self.eta)

    def inspect(self):
        print(self.inputs)
        for layer in self.layers:
            print([n.weights for n in layer])
        print(self.out)
        print(self.target)

    def train(self):
        # cache the error from previous layer
        d_layer = [[-(t-o) for t,o in zip(self.target, self.out)]] # cache the error from previous layer
        for layer in reversed(self.layers):
            for i,n in enumerate(layer):
                d = sum([dn[i] for dn in d_layer]) # add up all contributions to n from layer above
                n.set_diff(d) # update n's gradient
            d_layer = [[n.diff*w for w in n.weights] for n in layer] # backpropagate for next layer

ffnn = FeedForwardNN(target = [0.35, 0.2], inputs = [0.05, 0.1], eta = 0.5)

ffnn.add_layer([Neuron(2),Neuron(2),Neuron(2)]) # hidden 1
ffnn.add_layer([Neuron(3),Neuron(3),Neuron(3)]) # hidden 2
ffnn.add_layer([Neuron(3),Neuron(3)])            # output

ffnn.predict()

result = {"error": [ffnn.error()], "out0": [ffnn.out[0]], "out1": [ffnn.out[1]]}

for i in range(100):
    ffnn.train()
    ffnn.update()
    ffnn.predict()
    result["error"].append(ffnn.error())
    result["out0"].append(ffnn.out[0])
    result["out1"].append(ffnn.out[1])

plt.plot(result["out0"])
plt.plot(result["out1"])
plt.plot(result["error"])
plt.show()


# print("o1: %s" % out_o1)
# print("o2: %s" % out_o2)
# print("error: %s" % e_total)
