from numpy import exp, inf
from scipy.stats import norm


def firstMom(loc = 0, scale = 1, a = 0, b = 1):
    return scale * (-exp(-0.5*((b-loc)/scale)**2)--exp(-0.5*((a-loc)/scale)**2))


def monteCarloIntegration(dist, loc = 0, scale = 1, a = 0, b = 1, n = 10000):
    r = dist(loc, scale).rvs(size = n)
    r = r[(r >= a) & (r <= b)]
    return r.sum() / r.size - loc , r.size / n


if __name__ == "__main__":

    a = 0
    b = 10
    loc = -2
    scale = 5
    n = 1000000

    mean, mass = monteCarloIntegration(norm, loc, scale, a, b, n)
    moment = firstMom(loc, scale, a, b)

    res = (moment / (mass*mean))**2 / 2
    
    print(res)

