#coding: utf-8

import numpy as np

'''
分布
beta(a, b[, size])  
Draw samples from a Beta distribution.
贝塔分布

binomial(n, p[, size])  
Draw samples from a binomial distribution.
二项分布的样本

chisquare(df[, size])   
Draw samples from a chi-square distribution.
卡方分布样本

dirichlet(alpha[, size])    
Draw samples from the Dirichlet distribution.
狄利克雷分布

exponential([scale, size])  
Draw samples from an exponential distribution.
指数分布

f(dfnum, dfden[, size]) 
Draw samples from an F distribution.
f分布样本

gamma(shape[, scale, size]) 
Draw samples from a Gamma distribution.
伽马分布

geometric(p[, size])    
Draw samples from the geometric distribution.
几何分布

gumbel([loc, scale, size])  
Draw samples from a Gumbel distribution.
第比尔分布

hypergeometric(ngood, nbad, nsample[, size])    
Draw samples from a Hypergeometric distribution.
超几何分布样本

laplace([loc, scale, size]) 
Draw samples from the Laplace or double exponential distribution with 
specified location (or mean) and scale (decay).
拉普拉斯或双指数分布样本

logistic([loc, scale, size])    
Draw samples from a logistic distribution.
Logistic分布样本

lognormal([mean, sigma, size])  
Draw samples from a log-normal distribution.
对数正态分布

logseries(p[, size])    
Draw samples from a logarithmic series distribution.
对数级数分布

multinomial(n, pvals[, size])   
Draw samples from a multinomial distribution.
多项分布

multivariate_normal(mean, cov[, size, …)    
Draw random samples from a multivariate normal distribution.
多元正态分布

negative_binomial(n, p[, size]) 
Draw samples from a negative binomial distribution.
负二项分布

noncentral_chisquare(df, nonc[, size])  
Draw samples from a noncentral chi-square distribution.
非中心卡方分布

noncentral_f(dfnum, dfden, nonc[, size])    
Draw samples from the noncentral F distribution.
非中心F分布

normal([loc, scale, size])  
Draw random samples from a normal (Gaussian) distribution.
正态（高斯）分布

pareto(a[, size])  
Draw samples from a Pareto II or Lomax distribution with specified shape.
帕累托分布

poisson([lam, size])    
Draw samples from a Poisson distribution.
泊松分布

power(a[, size])    
Draws samples in [0, 1] from a power distribution with positive exponent a - 1.

rayleigh([scale, size]) 
Draw samples from a Rayleigh distribution.
Rayleigh 分布

standard_cauchy([size]) 
Draw samples from a standard Cauchy distribution with mode = 0.
标准柯西分布

standard_exponential([size])    
Draw samples from the standard exponential distribution.
标准指数分布

standard_gamma(shape[, size])   
Draw samples from a standard Gamma distribution.
标准伽马分布

standard_normal([size]) 
Draw samples from a standard Normal distribution (mean=0, stdev=1).
标准正态分布

standard_t(df[, size])  
Draw samples from a standard Student’s t distribution with df degrees of freedom.

triangular(left, mode, right[, size])   
Draw samples from the triangular distribution over the interval [left, right].
三角分布

uniform([low, high, size])  
Draw samples from a uniform distribution.
均匀分布

vonmises(mu, kappa[, size]) 
Draw samples from a von Mises distribution.

wald(mean, scale[, size])   
Draw samples from a Wald, or inverse Gaussian, distribution.
瓦尔德分布

weibull(a[, size])  
Draw samples from a Weibull distribution.

zipf(a[, size]) 
Draw samples from a Zipf distribution.
齐普夫分布
'''

'''
numpy.random.normal(loc=0.0, scale=1.0, size=None)
loc: float or array_like of floats 
此概率分布的均值
scale: float or array_like of floats 
此概率分布的标准差（对应于宽度，scale越大越矮胖，scale越小，越瘦高
size: int or tuple of ints, optional
'''

def normal():
  mu, sigma = 0, 0.1
  s = np.random.normal(mu, sigma, 10)
  print(s)


def test():
  mu, sigma = 22.6, 1.5
  s = np.random.normal(mu, sigma, 10)
  print(s)


if __name__ == "__main__":
  #normal()
  test()
