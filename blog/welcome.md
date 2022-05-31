(welcome_post)=
# Welcome to the PyMC blog

:::{post} 31 January, 2022
:author: oriol
:tags: community, communication
:category: news
:::

The PyMC project is creating a project website to complement our
documentation!

## What can you expect from this website?
This website `pymc.io` will be used mostly to showcase important news about
the project and to host a blog (this being the first post) where
we will expand on details for project news, write about our initiatives,
share testimonials about PyMC usage...

Blog posts will be available at `pymc.io/blog.html` and each will contain metadata
with tags, categories, authors... For now we are starting with three categories:

* `news` for news and announcements about PyMC, new major releases, grants,
  council elections...
* `event` arguably a type of news, we will use this category to give special
  emphasis to PyMC related events such as PyMCon, contribution sprints,
  PyData or Scipy conferences with participation from PyMC members...
* `testimonial` will be used for people to explain their relation and
  journey with PyMC, be it how they discovered and started contributing
  to the project or how they improved the models at their company
  thanks to PyMC.

Subscribe to the blog feed clicking [here](https://www.pymc.io/blog/atom.xml)

## How can you contribute to the blog?
If you have a blog post about using PyMC that doesn't fit the documentation but
could fit here and would like us to consider adding it because you believe it is
of interest to all the PyMC community, let us know on [Discourse](https://discourse.pymc.io/)
using the category `sharing`

## About the blog itself
Let's now showcase some of the cool features of the blog.

### Multiple formats supported
Blog posts can be written as Markdown, Jupyter notebooks or restructured text. All are
rendered without problem and can easily link to posts using different types of files.

### Flexible content layout
:::{sidebar} **Our own "PyMC book"**
We have also improved the [PyMC example gallery](https://docs.pymc.io/projects/examples/en/latest/)
thinking of the notebooks as book chapters. Check it out!
:::

The blog uses the [sphinx-book-theme](https://sphinx-book-theme.readthedocs.io/en/latest/index.html)
which is designed to write beautiful online books and is inspired in the Eduard Tufte CSS guide.

Moreover, we use sphinx to generate the website. We flexibility in the layout with all the
features provided by sphinx and its extensions such as [sphinx-design](https://sphinx-design.readthedocs.io/en/furo-theme/)
which brings many bootstrap features like cards, grids or dropdowns to sphinx sites.
