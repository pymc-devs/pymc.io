(pytensor_announcement)=
# PyMC forked Aesara to PyTensor

:::{post} Nov 28, 2022
:tags: announcement
:category: news
:author: PyMC developers
:image: 0

The PyMC team would like to announce that we have forked the Aesara project.
:::

This new project is called [PyTensor](https://github.com/pymc-devs/pytensor). PyTensor will allow for new features such as labeled arrays, as well as speed up development and streamline the PyMC codebase and user experience. PyTensor is a community focused project and contributions are welcome.

Since the creation of Aesara, the PyMC and Aesara projects have been greatly intertwined. Aesara internals are critical to PyMC. In that time, however, the governance philosophies and technical goals of PyMC and Aesara diverged. PyMC is a [NumFOCUS sponsored project since 2016](https://numfocus.org/uncategorized/numfocus-announces-new-fiscally-sponsored-project-pymc3). PyMC follows a community model where consensus is formed when making key decisions and moving forward. Aesara is following a model where a select group of core developers drive most development and make key decisions while nurturing outside contributions to core infrastructure or design decisions is not a priority (see [Aesara's contributing guide](https://github.com/aesara-devs/aesara/blob/main/CONTRIBUTING.md) as well as [Rocket Ship to Mars archetype](https://opentechstrategies.com/archetypes-files/open-source-archetypes-v2.pdf#section*.10)).

While different development models can be successful for different open source software projects, the model followed by Aesara has proven to be incompatible with the collaborative process norms of the PyMC development team as well as our desire to influence key design decisions of Aesara. We believe the ability to contribute and influence the graph-engine is critical for our ability to innovate and make PyMC the best version it can be. 

Thus, after careful consideration and discussion, both among our developers and between the projects, we have decided that forking the Aesara project is the best choice for PyMC, its community, and its developers.

## What does this mean for PyMC?

For now, we still depend on Aesara. As we are working towards a 5.0 release of PyMC that will depend on PyTensor instead of Aesara there will be a new dependency installed, but the package manager will handle this seamlessly. If you are using Aesara directly, you will have to adapt some imports, but the code will remain the same as the libraries are currently almost identical code-wise. 

The long-term impact will be positive. There are many exciting changes we plan to make that will directly improve the user and developer experience of PyMC.

One example is [**Xarray**](https://xarray.dev/)-like dimension support: `Xarray` adds many useful features to arrays. Most notably, named dimensions and coordinates. This is what allows `coords` and `dims` in PyMC to give names to your arrays.  Currently, Aesara does not support this, nor are there plans to do so. But there are many benefits to having labeled tensors as well.

In addition, there are optimizations that are mostly geared towards the computations PyMC frequently perform, so we expect great speed-ups from these additions.

### Community

The PyMC project is community-led, with a [governance structure](https://github.com/pymc-devs/pymc/blob/main/GOVERNANCE.md), code of conduct and other mechanisms in place to ensure a great experience for everyone involved. We strongly believe that a welcoming and inclusive environment is critical for the long-term survival of any open-source project.

You can expect us to apply these same standards to PyTensor to make it a project people are excited to contribute to.

## Conclusion

As always, we are grateful to the amazing community of users and contributors. We continue to be humbled by the impact this project has had over the years in science, business, and personal learning. We'd like to especially thank the Aesara development team for all their tireless efforts in building this library and working with us.

We are very excited about the future of PyMC and its ecosystem. 

## Connect with PyMC

Connect with PyMC via:
- PyTensor repo:  [pymc-devs/pytensor](https://github.com/pymc-devs/pytensor)
- Join Meetup: [pymc-online-meetup](https://www.meetup.com/pymc-online-meetup/)
- Twitter: [@pymc_devs](https://twitter.com/pymc_devs)
- LinkedIn: [@pymc](https://www.linkedin.com/company/pymc/)
