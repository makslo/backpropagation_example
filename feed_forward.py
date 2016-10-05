import math, random as rd

class Neuron:
    def __init__(self, size):
        self.weights = [rd.random() for _ in range(size)]
        self.b = rd.random()

    def set_out(inp):
        s = sum([i*w for i,w in zip(inp,self.weights)])+self.b
        self.inp = inp
        self.out = 1/(1+math.exp(-s))
        return self.out

    def set_diff(d):
        self.diff = d*self.out*(1-self.out)

    def update(eta):
        self.weights = [w - eta*self.diff*i for w,i in zip(self.weights,self.inp)]

# fully connected multilayer feed forward network
class FeedForwardNN:
    def __init__(self, target, inputs, eta):
        self.eta = eta
        self.inputs = inputs
        self.layers = []
        self.target = target
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

    def update():
        for layer in layers:
            for n in layer:
                n.update(self.eta)

    def inspect():
        print(self.inputs)
        for layer in layers:
            print([n.weights for n in layer])
        print(self.out)

    def train():
        # cache the error from previous layer
        d_layer = [[-(t-o) for t,o in zip(self.target, self.out)]] # cache the error from previous layer
        for layer in layers:
            for i,n in enumerate(reversed(layer)):
                d = sum([dn[i] for dn in d_layer]) # add up all contributions to n from layer above
                n.set_diff(d) # update n's gradient
            d_layer = [[n.diff*w for w in n.weights] for n in layer] # backpropagate for next layer

ffnn = FeedForwardNN(target = [0.01, 0.99], inputs = [0.05, 0.1], eta = 0.5)

ffnn.add_layer([Neuron(2),[Neuron(2),[Neuron(2)] # hidden 1
ffnn.add_layer([Neuron(3),[Neuron(3),[Neuron(3)] # hidden 2
ffnn.add_layer([Neuron(3),[Neuron(3)]            # output

# print("o1: %s" % out_o1)
# print("o2: %s" % out_o2)
# print("error: %s" % e_total)
