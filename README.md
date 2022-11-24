<h1 align='center'>Deep Signal Processing</h1>
<h2 align='center'>
  Accompanying notebook guides to the notes [TBA] 
</h2>


## The Atlas of Convolutions -- Part 1: Memory, Causality and Parameter Scaling
* `basics`: introduces the basic idea of a linear convolution and the different ways of implementing it
* `fft_conv`: discusses diagonalization of circulant matrices, motivating an efficient method to convolve signals
* `causality`: investigates how to enforce causality of a convolution 
* `ssm_kernel`: provides a showcase of a simple diagonal state space and the resulting kernel
* `transfer_function`: primer on transfer functions, properties and how to parametrize a convolution as a ratio of polynomials over the complex numbers
* `analysis`: explains how to leverage amplitude and phase of a frequency response to inspect input-output pairs for pure sinusoidal signals
* `parametrizations`: provides a set of minimal `nn.Module` classes implementing the different convolution parametrizations introduced in the notes.

## Other excellent resources

State spaces: 
* [state-spaces (repo)](https://github.com/HazyResearch/state-spaces).
* [Simplifying S4 (blog)](https://hazyresearch.stanford.edu/blog/2022-06-11-simplifying-s4).
