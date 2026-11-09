# multiscale-retinex-opencv

A classical multi-scale Retinex (MSRCR) image enhancement demo built with OpenCV.

This implements the classical Retinex family of algorithms (Jobson et al., 1997)
with Gaussian surround functions. It is useful as a *baseline* for comparison
against learned low-light enhancement methods.

Important: this repository does **not** implement the illumination-prior
learning approach used in recent learned enhancement work. It is the classical
algorithm only, and there is no training code (the parameters are fixed).

Licensed under the MIT licence; see `LICENSE`.
