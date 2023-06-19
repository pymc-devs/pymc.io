---
sd_hide_title: true
---

# Home

<center><img src="https://raw.githubusercontent.com/pymc-devs/brand/main/pymc/pymc_logos/PyMC_banner.svg" width="75%"/></center>

{doc}`PyMC <pymc:index>` is a probabilistic programming library for Python that allows users to build Bayesian models with a simple Python API and fit them using Markov chain Monte Carlo (MCMC) methods.

## Features
PyMC strives to make Bayesian modeling as simple and painless as possible, allowing users to focus on their problem rather than the methods.

Here is what sets it apart:

* **Modern**: Includes state-of-the-art inference algorithms, including MCMC (NUTS) and variational inference (ADVI).
* **User friendly**: Write your models using friendly Python syntax. [Learn Bayesian modeling](https://www.pymc.io/projects/docs/en/latest/learn.html#) from the many [example notebooks](https://www.pymc.io/projects/examples/en/latest/gallery.html).
* **Fast**: Uses {doc}`PyTensor <pytensor:index>` as its computational backend to compile through C, Numba or JAX, [run your models on the GPU](https://www.pymc-labs.io/blog-posts/pymc-stan-benchmark/), and benefit from complex graph-optimizations.
* **Batteries included**: Includes probability distributions, Gaussian processes, ABC, SMC and much more. It integrates nicely with {doc}`ArviZ <arviz:index>` for visualizations and diagnostics, as well as {doc}`Bambi <bambi:index>` for high-level mixed-effect models.
* **Community focused**: Ask questions on [discourse](https://discourse.pymc.io), join [MeetUp events](https://meetup.com/pymc-online-meetup/), follow us on [Twitter](https://twitter.com/pymc_devs), and start [contributing](https://www.pymc.io/projects/docs/en/latest/contributing/index.html).


## Interactive Demo
```{retrolite} pymc_example.ipynb
---
width: 100%
height: 300px
```

## Get started
* [Installation instructions](https://www.pymc.io/projects/docs/en/latest/installation.html)
* [Beginner guide (if you **do not** know Bayesian modeling)](https://www.pymc.io/projects/docs/en/latest/learn/core_notebooks/pymc_overview.html)
* [API quickstart (if you **do** know Bayesian modeling)](https://www.pymc.io/projects/examples/en/latest/howto/api_quickstart.html)
* [Example gallery](https://www.pymc.io/projects/examples/en/latest/gallery.html)
* [Discourse help forum](https://discourse.pymc.io)

## Announcements

:::::{container} full-width
::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} PyMC forked Aesara to PyTensor
:link: pytensor_announcement
:link-type: ref
:class-header: bg-pymc-three

Release announcement
^^^
PyTensor will allow for new features such as labeled arrays, as well as speed up development and streamline the PyMC codebase and user experience.
:::


:::{grid-item-card} PyMC 4.0 is officially released!
:link: v4_announcement
:link-type: ref
:class-header: bg-pymc-three

Release announcement
^^^
PyMC 4.0 is a major rewrite of the library with many great new features while keeping the same modeling API of PyMC3.
:::

:::{grid-item-card} PyMC - Office Hours
:link: https://discourse.pymc.io/tag/office-hours
:class-header: bg-pymc-one

Event
^^^
The PyMC team has recently started hosting office hours regularly.
Subscribe on Discourse to be notified of the next event!
:::

:::{grid-item-card} Probabilistic Programming in PyMC
:link: https://austinrochford.com/posts/intro-prob-prog-pymc.html
:class-header: bg-pymc-two

Talk
^^^
Austin Rochford gave the coolest talk on Probabilistic Programming in PyMC 4.0
:::

:::{grid-item-card} Sprint testimonials
:link: sprint_testimonial
:link-type: ref
:class-header: bg-pymc-one

Blog post
^^^
Read about the recent PyMC-Data Umbrella sprint in this interview with
Sandra Meneses, one of the participants who submitted a PR
:::

::::
:::::

## Sponsors
:::::{container} full-width
::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card} NumFOCUS
:link: https://numfocus.org

<img src="https://www.numfocus.org/wp-content/uploads/2017/03/1457562110.png"/>

NumFOCUS is our non-profit umbrella organization.
:::

:::{grid-item-card} PyMC Labs
:link: https://pymc-labs.io

<img src="https://github.com/pymc-labs/brand/blob/main/logos/4-pymc-labs-transp-black.png?raw=true"/>

PyMC Labs offers professional consulting services for PyMC.
:::
:::{grid-item-card} Mistplay
:link: https://www.mistplay.com/

<img src="https://github.com/pymc-devs/brand/blob/main/sponsors/sponsor_logos/mistplay2_white.png?raw=true"/>

Mistplay is the world's leading Loyalty Program for mobile gamers.
:::
:::{grid-item-card} ODSC
:link: https://odsc.com/california/?utm_source=pymc&utm_medium=referral

<img src="https://github.com/pymc-devs/brand/blob/main/sponsors/sponsor_logos/odsc/odsc_blue.png?raw=true"/>

The future of AI gathers here.
:::

::::
:::::

:::{toctree}
:hidden:

about/ecosystem
about/history
about/testimonials
:::

:::{toctree}
:hidden:
:caption: External links

Discourse <https://discourse.pymc.io>
Twitter <https://twitter.com/pymc_devs>
YouTube <https://www.youtube.com/c/PyMCDevelopers>
LinkedIn <https://www.linkedin.com/company/pymc/>
Meetup <https://www.meetup.com/pymc-online-meetup/>
GitHub <https://www.github.com/pymc-devs/pymc>
:::
