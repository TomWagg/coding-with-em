survival
========

*Difficulty*: ★★★★☆

.. figure:: ../../_static/boardroom_survival.png
    :align: center

    Survival of the fittest!

Welcome to the survival problem - where only the fittest survive!

Nah just kidding. In this problem you're going to simulate the spread of a mutation in a population of alleles and track genetic drift and natural selection. Not too tricky right?

Concepts
--------

For this problem, we're going to be implementing a Moran process. This is a simple model of genetic drift in a fixed-size population. In this population, individuals can have one of two alleles: :math:`A` or :math:`a`.

The population size is constant, and at each time step, one individual is chosen to reproduce and one individual is chosen to die. During reproduction, mutations can occur, changing an allele from :math:`A` to :math:`a` or vice versa. The rate of an :math:`A` allele mutating to :math:`a` is given by :math:`\mu`, and the rate of an :math:`a` allele mutating to :math:`A` is given by :math:`\nu`.

We can also model natural selection by assigning a relative fitness to the alleles. Let's say allele :math:`A` has a relative fitness of :math:`s` compared to allele :math:`a`, such that during each timestep, the probability of choosing an individual with allele :math:`A` to reproduce is proportional to :math:`1 + s`, while the probability of choosing an individual with allele :math:`a` is proportional to :math:`1`. Clearly, if :math:`s > 0`, allele :math:`A` is favored by selection and is likely to increase in frequency over time.

We **could** do some maths here to write out a diffusion equation for the allele frequency dynamics...

.. dropdown:: Warning: Maths is hidden here!

    If you really want to get into the nitty-gritty of the maths behind this process, the allele frequency dynamics can be described by the following diffusion equation which has terms for selection, mutation, and genetic drift:

    .. math::

        \begin{split}
            \bar{\omega} \cdot \frac{\partial P(x, \tau)}{\partial \tau} = &- \underbrace{s \frac{\partial}{\partial x}\bigg(P(x, \tau)\cdot x(1-x)\bigg)}_{\text{selection}} \\
            &+ \underbrace{ \mu \frac{\partial}{\partial x} \bigg( x \cdot P(x, \tau) \bigg) - \nu \frac{\partial}{\partial x} \bigg( (1 - x) \cdot P(x, \tau) \bigg)}_{\text{mutation}} \\ 
            &+ \underbrace{ \frac{1}{N} \frac{\partial^2}{\partial^2 x}\bigg(P(x, \tau)\cdot x(1-x)\bigg) }_{\text{drift}},
        \end{split}

    where :math:`\bar{\omega}` is the average fitness, which is given by

    .. math::

        \bar{\omega} =  \frac{1}{N} \bigg( n(1 + s) + (N - n) \bigg),

    :math:`P(x, \tau)` is the probability that the frequency of allele :math:`A` is :math:`x` at time :math:`\tau`, :math:`s` is the relative fitness of allele :math:`A`, :math:`\mu` is the mutation rate from :math:`A` to :math:`a`, :math:`\nu` is the mutation rate from :math:`a` to :math:`A`, :math:`N` is the population size, and :math:`n` is the number of individuals with allele :math:`A`.

    For more details and an animation of this whole process, check out `this link <https://www.tomwagg.com/html/moran_circles.html>`_.
                                                
...or we can just simulate it!

Your Task
---------

