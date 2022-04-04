---
sd_hide_title: true
---

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

## Announcements

:::::{container} full-width
::::{grid} 1 2 2 3
:gutter: 3

:::{grid-item-card} PyMC - Data Umbrella Sprint
:link: https://discourse.pymc.io/tag/office-hours
:class-header: bg-pymc-one

Event
^^^
The PyMC team has recently started hosting office hours regularly.
Subscribe on Discourse to be notified of the next event!
:::
:::{grid-item-card} Welcome to the PyMC blog
:link: welcome_post
:link-type: ref
:class-header: bg-pymc-two

Blog Post
^^^
Check out the new PyMC blog, learn what to expect from it and how to subscribe
:::
:::{grid-item-card} Probabilistic Programming in PyMC
:link: https://austinrochford.com/posts/intro-prob-prog-pymc.html
:class-header: bg-pymc-three

Talk
^^^
Austin Rochford gave the coolest talk on Probabilistic Programming in PyMC 4.0
:::

:::{grid-item-card} PyMC is participating in GSoC
:link: https://github.com/pymc-devs/pymc/wiki/GSoC-2022-projects
:class-header: bg-pymc-two

Internships
^^^
If you are interested in open source, GSoC is the perfect opportunity to dive in and get involved.
This year, anyone new to open source and over 18 years can participate!
:::
:::{grid-item-card} Sprint testimonials
:link: sprint_testimonial
:link-type: ref
:class-header: bg-pymc-three

Blog post
^^^
Read about the recent PyMC-Data Umbrella sprint directly from the participants
:::
:::{grid-item-card} PyMC 4.0 is closing in
:link: v4_announcement
:link-type: ref
:class-header: bg-pymc-one

Release announcement
^^^
Check out this blog post for a sneak preview of all the improvements PyMC 4.0 will bring!
Or install the already available beta release and try it for yourself!
:::
::::
:::::

## The PyMC library

{doc}`PyMC <pymc:index>` is a probabilistic programming library for Python that allows users
to fit Bayesian models using a variety of numerical methods,
most notably Markov chain Monte Carlo (MCMC) and variational inference (VI).
Its flexibility and extensibility make it applicable to a large suite of problems.
Along with core model specification and fitting functionality,
PyMC integrates with {doc}`ArviZ <arviz:index>` for exploratory analysis of the results.

### Features
PyMC strives to make Bayesian modeling as simple and painless as possible,
allowing users to focus on their scientific problem, rather than on the methods used to solve it.
Here is a partial list of its features:

* Modern methods for fitting Bayesian models, including MCMC and VI.
* Includes a large suite of well-documented statistical distributions.
* Uses {doc}`Aesara <aesara:index>` as the computational backend, allowing for fast expression evaluation, automatic gradient calculation, and GPU computing.
* Built-in support for Gaussian process modeling.
* Extensible: easily incorporates custom step methods and unusual probability distributions.
* Bayesian models can be embedded in larger programs, and results can be analyzed with the full power of Python.


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
:::
