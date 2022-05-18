---
sd_hide_title: true
---

## The PyMC library

{doc}`PyMC <pymc:index>` is a probabilistic programming library for Python that allows users to build Bayesian models with a simple Python API and fit them using Markov chain Monte Carlo (MCMC) methods.
PyMC focuses on usability, flexibility, scalability, and extensibility.
Along with core model specification and fitting functionality,
PyMC integrates with {doc}`ArviZ <arviz:index>` for exploratory analysis of the results.

### Interactive Demo
```{retrolite} pymc_example.ipynb
---
width: 100%
height: 250px
```

### Features
PyMC strives to make Bayesian modeling as simple and painless as possible,
allowing users to focus on their scientific problem, rather than on the methods used to solve it.
Here is what sets it apart:

* **Modern**: Includes state-of-the-art inference algorithms, including MCMC (NUTS) and variational inference (ADVI).
* **User friendly**: Simple syntax and documentation with many examples and tutorials for building various models.
* **Fast**: Uses {doc}`Aesara <aesara:index>` as its computational backend, which supports compilation to C and JAX, automatic gradient calculation, GPU computing, and complex graph-optimizations.
* **Batteries included**: Comes with a suite of probability distributions, support Gaussian processes, ABC, SMC and much more.
* **Extensible**: easily incorporates custom step methods and unusual probability distributions.
* **Deployable**: Bayesian models can be embedded in larger programs, and results can be analyzed with the full power of Python.

## Announcements

:::::{container} full-width
::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} PyMC 4.0 is officially released!
:link: v4_announcement
:link-type: ref
:class-header: bg-pymc-three

Release announcement
^^^
Check out the offical release announcement with all the improvements PyMC 4.0 brings.
:::

:::{grid-item-card} PyMC - Data Umbrella Sprint
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

# The PyMC project
PyMC is a community driven project with the goal of making Bayesian modeling
and probabilistic programming intuitive and performant.

The flagship of the PyMC project is the PyMC library, but PyMC also coordinates
many other activities:

* Organizing [PyMCon](https://pymcon.com)
* Curating the {doc}`PyMC example gallery <nb:index>`
* Answer questions and moderate discussions on [PyMC Discourse](https://discourse.pymc.io/)
* Translating the code examples of Bayesian statistics books in
  [PyMC resources](https://github.com/pymc-devs/pymc-resources)
* [Office hours](https://discourse.pymc.io/tag/office-hours) and
  [sprints](https://pymc-data-umbrella.xyz/en/latest/) to encourage people to contribute to open source


:::{toctree}
:hidden:
:caption: About PyMC

about/ecosystem
about/history
about/testimonials
:::

:::{toctree}
:hidden:
:caption: Blog

Recent posts <blog>
Blog feed <https://www.pymc.io/blog/atom.xml>
:::

:::{toctree}
:hidden:
:caption: External links

PyMC documentation <https://docs.pymc.io>
Discourse <https://discourse.pymc.io>
Twitter <https://twitter.com/pymc_devs>
YouTube <https://www.youtube.com/c/PyMCDevelopers>
LinkedIn <https://www.linkedin.com/company/pymc/>
Meetup <https://www.meetup.com/pymc-online-meetup/>
Website repo <https://github.com/pymc-devs/pymc.io>
:::
