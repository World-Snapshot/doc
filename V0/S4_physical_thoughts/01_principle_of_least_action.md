# Principle of Least Action

The following article is intended to popularize the principle of least action. Its content is entirely reproduced from a blog named ["The Principle of Least Action: A Unifying Bridge from Classical Mechanics to Modern Technology"](https://aerognc.blog.csdn.net/article/details/143569971).

It is well written, and the original was in Chinese. I have translated it into English, which I'm noting here.

**Note1:** I can illustrate this article with an example. Light always moves in the direction that minimizes resistance. This idea is one that many people have heard. I believe the rectified flow model also represents this concept. Its viewpoint is to straighten out the path. In fact, the path may not be straight, but it is the one with the least resistance and the fastest speed. Therefore, by using the principle of minimizing action as the loss function, I was able to obtain the wave core space that satisfies all physical systems.

**Note2:** Furthermore, Sen Fang believes and boldly conjectures that the essence of [Rectified Flow](https://arxiv.org/abs/2209.03003)/[Flow Matching](https://arxiv.org/abs/2210.02747v2) is not to straighten the paths, but to have the model generate along the path with the least resistance.

# Introduction

The principle of least action is an important concept in physics. Its core idea is that for a physical system, there exists an action (typically a function in integral form) that describes the evolution of the system from its initial state to its final state. The principle of least action states that among all possible evolutionary paths, the one that actually occurs is the path that minimizes this action.

The Principle of Least Action is a profound and elegant principle in physics that reveals the simplicity and beauty of the laws of motion in nature. This principle not only holds an important position in classical mechanics but also plays a key role in quantum mechanics, relativity, and other fields of modern science. This article will lead you into the world of the principle of least action, tracing its origins, analyzing its implications, explaining its applications, and exploring its development.

## The Origin of the Principle of Least Action

The idea of the principle of least action can be traced back to philosophers and scientists from ancient times. In the mid-4th century BCE, the Greek philosopher Aristotle proposed the view of "teleology" in his work "Physics," believing that motion and change in nature proceed toward some purpose or endpoint. This idea bears some similarity to the principle of least action, as the latter also involves a system choosing an optimal path during its evolution. Aristotle proposed the "isoperimetric problem," believing that a circle is the shape with the minimum perimeter for a given area, thus introducing the notion that nature tends to choose optimal paths. He was the first to transform belief into a "minimum quantity" hypothesis, emphasizing that "completing a task with minimal resources is most effective."

Around the 1st century BCE, the Greek scholar Hero of Alexandria explained the rectilinear propagation and law of reflection of light, emphasizing the "economic nature" of natural phenomena. Hero proposed the view that light propagates along the shortest path, which can be seen as an early formulation of the principle of least action. This theory was an early understanding of the path of light propagation in physics. Around 1650, Fermat further proposed the principle of least time for light (Fermat's principle), stating that when light propagates between two points, it takes the path that minimizes the propagation time. This principle not only explains the phenomenon of light refraction but also laid the foundation for later optical research. Fermat's principle of least time was based on his in-depth thinking about the speed of light propagation. He believed that light has different speeds in different media, so light would choose a path that minimizes the total propagation time. This idea has a profound connection with the principle of least action, as it also involves the problem of a system choosing an optimal path during evolution. Fermat's work not only attracted widespread attention at the time but also had a far-reaching influence on later scientists such as Huygens and Newton. Huygens proposed the wave theory on this basis, while Newton developed the particle theory, both of which further promoted the development of optics. Fermat's principle of least time is considered one of the early applications of the principle of least action, demonstrating the optimization principles universally present in nature.

In the 17th century, the French philosopher and mathematician René Descartes also proposed similar views, believing that motion in nature follows some principle of simplification. In 1641, Descartes proposed in his work "Meditations on First Philosophy" that the motion of objects is conducted in the simplest and most direct way set by God, a view that has profound connections with the idea of the principle of least action. Descartes believed that the laws of nature are described through the simplest geometric and mechanical principles, and this simplification principle applies not only to the motion of objects but also to phenomena such as light propagation and reflection. His ideas provided an important theoretical foundation for later scientists and promoted the development of the principle of least action.

In the 18th century, the French mathematician and physicist Pierre-Louis Moreau de Maupertuis proposed the principle of least action, pointing out that in natural phenomena, action tends toward a minimum value. He defined action as the product of an object's mass, distance moved, and velocity. In his 1741 paper, Maupertuis proposed the law of stationary objects, explaining that when objects at rest in a system change, their motion tends towards a minimum change in action. In 1744, he further proposed the theory of minimum action for the refraction path of light between different media, believing that light would choose the path of minimum action during propagation. In 1746, Maupertuis pointed out in his paper at the Berlin Academy of Sciences that the motion of particles also follows the principle of least action. He introduced the concept of particles, that is, the mass of an object concentrated at a point, thus simplifying the analysis of object motion. His original intention in proposing the principle of least action was to prove the existence of God. However, the God he referred to was not the personified God in traditional religious theology, but God as the maker and maintainer of natural laws. This view emphasized the regularity and harmony of nature, making Maupertuis in some ways closer to materialists, as he focused on the inherent order and laws of nature rather than supernatural intervention.

In the 18th century, the Swiss mathematician Leonhard Euler and the Italian mathematician Joseph-Louis Lagrange played a key role in the development of the principle of least action. Euler first proposed the concept of the calculus of variations in his 1744 paper "On the Calculus of Variations for Curves," which laid the mathematical foundation for the later principle of least action. Through the calculus of variations, Euler studied the trajectories of objects under different conditions, revealing the mathematical principles of a system choosing the optimal path during evolution. Around 1760, Lagrange further developed Euler's ideas, proposing the framework of Lagrangian mechanics, making the solution of mechanical problems more systematic and general. By introducing the concepts of generalized coordinates and generalized momentum, Lagrange transformed mechanical problems into solving Lagrangian equations. His work not only simplified the analysis of complex systems but also laid the foundation for later Hamiltonian mechanics. Lagrange's research showed that the motion of a system can be described by minimizing action, an idea that became the core content of the principle of least action.

The work of Euler and Lagrange not only promoted the development of the principle of least action but also provided an important theoretical foundation for later scientists. In the 19th century, William Rowan Hamilton further developed this principle based on their work, forming Hamiltonian mechanics. Hamilton elevated the concept of action to a new height, demonstrating the profound connection between conserved quantities and symmetry in physical systems. Poincaré's research in dynamical systems and the calculus of variations expanded the application range of the principle of least action; his work had a profound influence on chaos theory and the development of modern physics.

## The Implications of the Principle of Least Action

### The Concepts of Action and Lagrangian

In physics, the action $S$ is defined as the integral of the Lagrangian $L$ over the time interval $[t_1, t_2]$:

$$S = \int_{t_1}^{t_2} L \, dt$$

The Lagrangian $L$ is typically defined as the difference between the kinetic energy $T$ and the potential energy $V$:

$$L = T - V$$

Where kinetic energy (Kinetic Energy) $T$ is the energy that an object possesses due to its motion. For a particle with mass $m$, its kinetic energy can be expressed as:

$$T = \frac{1}{2} m v^2$$

Where $v$ is the velocity of the particle. Kinetic energy reflects the energy content of an object's state of motion.

Potential energy (Potential Energy) $V$ is the energy that an object possesses due to its position or configuration in a conservative force field. Taking gravitational potential energy as an example, for an object with mass $m$ at a height $h$ in a gravitational field, its potential energy is:

$$V = mgh$$

Where $g$ is the gravitational acceleration. Potential energy reflects the energy stored by an object due to its position or state.

The physical meaning of the Lagrangian can be understood as the system's "vitality":

- Kinetic energy represents the system's "motion vitality," that is, the energy an object possesses due to motion. The greater the kinetic energy, the more intense the object's state of motion.
- Potential energy represents the system's "stored vitality," that is, the energy stored by an object due to its position or state. The greater the potential energy, the higher the object's position in a conservative force field or the more special its state.
- Their difference (the Lagrangian) describes the overall state of the system, reflecting the energy distribution of the system at a specific moment.

This definition helps to simplify the derivation of equations of motion. The Lagrangian, as the difference between kinetic and potential energy, can eliminate the explicit influence of certain forces in the system, making the Euler-Lagrange equations obtained through the variational principle more concise. Specifically, this definition of the Lagrangian allows us to transform the problem into an extremum problem of a function of generalized coordinates and generalized velocities when dealing with complex systems. This method not only simplifies the computational process but also provides a unified framework for handling different types of physical systems.

Through the Lagrangian, we can transform the dynamical behavior of a physical system into a mathematical problem, namely, finding the extremum of the action. The action is the integral of the Lagrangian over time, describing the evolution process of a system from its initial state to its final state. According to the principle of least action, the actual evolutionary path of the system is the path that extremizes the action. By performing variation on the action, we can obtain the equation of motion of the system, namely, the Euler-Lagrange equation.

The Euler-Lagrange equation is the fundamental equation describing the dynamical behavior of a system, revealing how the system chooses the optimal path during evolution. Specifically, the Euler-Lagrange equation states that the motion of the system is determined by the rate of change of the Lagrangian. By solving the Euler-Lagrange equation, we can obtain the trajectory and dynamical characteristics of the system. This method is not only applicable to classical mechanics but can also be extended to quantum mechanics, relativity, and other fields of modern physics, demonstrating the wide application and profound influence of the principle of least action.

Besides the common form $L = T - V$, the Lagrangian can also have other definitions to adapt to different physical systems and constraints. For example, in systems with damping or non-conservative forces, the Lagrangian may need to include generalized potential energy or other forms of terms to correctly describe the dynamical behavior of the system. Another example is in electromagnetic fields, where the Lagrangian needs to include the energy terms of the electromagnetic field to fully depict the interaction between particles and fields. The choice of Lagrangian depends on the specific physical problem and the nature of the forces considered; through a reasonable choice, the principle of least action can be effectively applied to solve complex dynamical systems.

Action has profound significance in physics; it is not just a mathematical tool but a key to revealing the laws of motion in nature. Through the principle of least action, we can understand how physical systems evolve under different conditions and find the optimal path of the system. Below, we will further illustrate the application of action through several examples.

**Example 1: Free Fall Motion**

System Description

Consider an object with mass $m$ falling freely from a height $h$, neglecting air resistance.

Calculation of Kinetic and Potential Energy

Kinetic Energy $T$

The velocity $v$ of the object is:
$$v = \dot{y}$$

Therefore, the kinetic energy is:
$$T = \frac{1}{2} m v^2 = \frac{1}{2} m \dot{y}^2$$

Potential Energy $V$

The height of the object relative to the ground is $y$, so the potential energy is:
$$V = m g y$$

Expression of the Lagrangian

The Lagrangian $L$ is defined as the kinetic energy $T$ minus the potential energy $V$:
$$L = T - V = \frac{1}{2} m \dot{y}^2 - m g y$$

Application of the Euler-Lagrange Equation

According to the Euler-Lagrange equation, we can directly obtain the acceleration equation for free fall motion:
$$\ddot{y} = -g$$

This indicates that the object falls freely with a gravitational acceleration $g$. The derivation process of the Euler-Lagrange equation will be explained in detail later.

**Example 2: Simple Harmonic Oscillator**

System Description

Consider a simple harmonic oscillator with mass $m$, spring constant $k$, and displacement $x$.

Calculation of Kinetic and Potential Energy

Kinetic Energy $T$

The velocity $v$ of the oscillator is:
$$v = \dot{x}$$

Therefore, the kinetic energy is:
$$T = \frac{1}{2} m v^2 = \frac{1}{2} m \dot{x}^2$$

Potential Energy $V$

The potential energy of the spring is:
$$V = \frac{1}{2} k x^2$$

Expression of the Lagrangian

The Lagrangian $L$ is defined as the kinetic energy $T$ minus the potential energy $V$:
$$L = T - V = \frac{1}{2} m \dot{x}^2 - \frac{1}{2} k x^2$$

Application of the Euler-Lagrange Equation

According to the Euler-Lagrange equation, we can directly obtain the equation of motion for the simple harmonic oscillator:
$$\ddot{x} + \frac{k}{m} x = 0$$

This indicates that the system performs simple harmonic oscillation with an angular frequency $\omega = \sqrt{\frac{k}{m}}$. The derivation process of the Euler-Lagrange equation will be explained in detail later.

Through these examples, we can see the application of the principle of least action in different physical systems. It not only helps us understand the laws of motion of the system but also provides a unified method of description, allowing us to view physical phenomena from a higher perspective.

### Derivation of the Euler-Lagrange Equation

The Principle of Least Action is one of the fundamental principles for analyzing the motion path of physical systems. According to this principle, the actual motion path of a physical system is the path that extremizes the action $S$ (usually minimizes it). Below, we will derive the Euler-Lagrange equation in detail to show how to obtain the equation of motion from the principle of least action.

1. Definition of Action

Action $S$ is defined as the integral of the Lagrangian $L$ over the time interval $[t_1, t_2]$:

$$S = \int_{t_1}^{t_2} L \, dt$$

Where the Lagrangian $L$ is typically defined as the difference between the system's kinetic energy $T$ and potential energy $V$:

$$L = T - V$$

2. Variation of Action

According to the principle of least action, the actual motion path of a physical system extremizes the action $S$. Consider a small variation $\delta q(t)$ of the motion path, requiring the variation $\delta S = 0$.

That is:

$$\delta S = \delta \int_{t_1}^{t_2} L(q, \dot{q}, t) \, dt = 0$$

3. Partial Integration and Elimination of Boundary Terms

Performing partial integration on the variation integral, we have:

$$\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} \delta q + \frac{\partial L}{\partial \dot{q}} \delta \dot{q} \right) dt$$

Where,

$$\delta \dot{q} = \frac{d}{dt} (\delta q)$$

Performing partial integration on the second term:

$$\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt + \left[ \frac{\partial L}{\partial \dot{q}} \delta q \right]_{t_1}^{t_2}$$

Since the variation $\delta q$ is zero at the endpoints $t_1$ and $t_2$, i.e., $\delta q(t_1) = \delta q(t_2) = 0$, the boundary term vanishes, and we get:

$$\delta S = \int_{t_1}^{t_2} \left( \frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} \right) \delta q \, dt = 0$$

4. Euler-Lagrange Equation

Since the variation $\delta q(t)$ can be chosen arbitrarily, for the above equation to hold for all possible $\delta q(t)$, we must have:

$$\frac{\partial L}{\partial q} - \frac{d}{dt} \frac{\partial L}{\partial \dot{q}} = 0$$

This is the famous Euler-Lagrange equation:

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{q}} \right) - \frac{\partial L}{\partial q} = 0$$

## Applications of the Principle of Least Action

The principle of least action has wide applications in physics. It is not only a cornerstone of theoretical physics but also plays an important role in fields such as optics, electromagnetism, relativity, and thermodynamics. Through the principle of least action, we can understand and describe various phenomena in nature from a unified perspective. The following will introduce the specific applications of this principle in different fields in detail.

### Application in Classical Mechanics: Simple Pendulum System

System Description

Consider an ideal simple pendulum with length $l$, bob mass $m$, angle $\theta$, moving under the action of gravitational acceleration $g$. The system ignores air resistance and friction.

Calculation of Kinetic and Potential Energy

Kinetic Energy $T$

The velocity $v$ of the pendulum bob is:
$$v = l \dot{\theta}$$

Therefore, the kinetic energy is:
$$T = \frac{1}{2} m v^2 = \frac{1}{2} m l^2 \dot{\theta}^2$$

Potential Energy $V$

The height change of the pendulum bob relative to the lowest point is:
$$h = l (1 - \cos\theta)$$

Therefore, the potential energy is:
$$V = mgh = m g l (1 - \cos\theta)$$

Expression of the Lagrangian $L$

The Lagrangian is defined as kinetic energy minus potential energy:
$$L = T - V = \frac{1}{2} m l^2 \dot{\theta}^2 - m g l (1 - \cos\theta)$$

Calculation of Action $S$

Substituting the Lagrangian into the definition of action:
$$S = \int_{t_1}^{t_2} \left( \frac{1}{2} m l^2 \dot{\theta}^2 - m g l (1 - \cos\theta) \right) dt$$

Variational Principle and Euler-Lagrange Equation

To extremize the action $S$, we perform variation on $\theta(t)$ to obtain the Euler-Lagrange equation:
$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}} \right) - \frac{\partial L}{\partial \theta} = 0$$

Substituting the Lagrangian $L$, we get:
$$\ddot{\theta} + \frac{g}{l} \sin\theta = 0$$

This equation describes the law of motion of a simple pendulum, consistent with our expectations for a pendulum system.

Explanation and Significance

Through the principle of least action, we can systematically derive the equation of motion for a simple pendulum, revealing the law of simple harmonic motion of the system under frictionless conditions. This method not only simplifies the process of solving mechanical problems but also demonstrates the wide application of the principle of least action in classical mechanics.

### Application in Optics: Fermat's Principle

System Description

Fermat's principle is a fundamental principle in optics, stating that the path chosen by light during propagation is the path that minimizes the propagation time. This principle can be used to explain the phenomena of light refraction and reflection.

Calculation of Light Propagation Time

Consider light propagating from medium 1 (with refractive index $n_1$) to medium 2 (with refractive index $n_2$) at an interface, with the path as shown in the figure. Let the angle of incidence be $\theta_1$, the angle of refraction be $\theta_2$, the interface between the two media be a horizontal plane, and the distance perpendicular to the interface be $d$.

The propagation speed of light in medium 1 is $v_1 = \frac{c}{n_1}$, and in medium 2 is $v_2 = \frac{c}{n_2}$, where $c$ is the speed of light in vacuum.

If the distance light travels in medium 1 is $s_1$ and in medium 2 is $s_2$, then the propagation time $T$ is:
$$T = \frac{s_1}{v_1} + \frac{s_2}{v_2} = \frac{n_1 s_1}{c} + \frac{n_2 s_2}{c}$$

Expression of Path Length

Suppose light travels from point A to point B on the interface, and then to point C. According to geometric relationships, we have:
$$s_1 = \sqrt{d^2 + x^2}, \quad s_2 = \sqrt{d^2 + (a - x)^2}$$

Where $x$ is the horizontal distance light moves on the interface, and $a$ is the horizontal distance between points A and C.

Application of Fermat's Principle

According to Fermat's principle, the actual propagation path of light minimizes the propagation time $T$, that is:
$$\frac{dT}{dx} = 0$$

Taking the derivative of $T$ with respect to $x$:
$$\frac{dT}{dx} = \frac{n_1}{c} \cdot \frac{x}{\sqrt{d^2 + x^2}} + \frac{n_2}{c} \cdot \frac{-(a - x)}{\sqrt{d^2 + (a - x)^2}} = 0$$

Derivation of Snell's Law

Multiplying both sides of the above equation by $c$ and rearranging, we get:
$$\frac{n_1 x}{\sqrt{d^2 + x^2}} = \frac{n_2 (a - x)}{\sqrt{d^2 + (a - x)^2}}$$

Let $\sin\theta_1 = \frac{x}{\sqrt{d^2 + x^2}}$, $\sin\theta_2 = \frac{a - x}{\sqrt{d^2 + (a - x)^2}}$, then we have:
$$n_1 \sin\theta_1 = n_2 \sin\theta_2$$

This is the famous Snell's law, describing the relationship of light refraction at the interface between different media.

### Application in Electromagnetism: Maxwell's Equations

System Description

In electromagnetic fields, Maxwell's equations can be derived through the principle of action. The principle of least action for electromagnetic fields involves the Lagrangian of the electromagnetic field, which describes the energy distribution of electric and magnetic fields.

Expression of the Lagrangian

The Lagrangian $L$ for a classical electromagnetic field consists of the electric field $\boldsymbol{E}$ and the magnetic field $\boldsymbol{B}$, defined as:
$$L = \frac{1}{2} (\epsilon_0 \boldsymbol{E}^2 - \frac{1}{\mu_0} \boldsymbol{B}^2)$$

Where $\epsilon_0$ is the vacuum permittivity, and $\mu_0$ is the vacuum permeability.

Definition of Action

The action $S$ for the electromagnetic field is defined as the integral of the Lagrangian over space and time:
$$S = \int_{t_1}^{t_2} \int_{V} L \, dV \, dt$$

Application of the Variational Principle

According to the principle of least action, the variation of the action $S$ with respect to the electromagnetic field variables is $\delta S = 0$. Consider the scalar potential $\phi$ and the vector potential $\boldsymbol{A}$, the electric and magnetic fields can be expressed as:
$$\boldsymbol{E} = -\nabla \phi - \frac{\partial \boldsymbol{A}}{\partial t}, \quad \boldsymbol{B} = \nabla \times \boldsymbol{A}$$

Substituting these expressions into the Lagrangian and performing variation with respect to $\phi$ and $\boldsymbol{A}$, we can obtain Maxwell's equations.

Derivation of Maxwell's Equations

Variation with respect to the scalar potential $\phi$:
$$\delta S = \int_{t_1}^{t_2} \int_{V} \left( -\epsilon_0 \nabla \phi \cdot \delta \phi + \epsilon_0 \frac{\partial \boldsymbol{A}}{\partial t} \cdot \delta \boldsymbol{A} + \frac{1}{\mu_0} (\nabla \times \boldsymbol{A}) \cdot (\nabla \times \delta \boldsymbol{A}) \right) dV \, dt = 0$$

By taking variations with respect to $\delta \phi$ and $\delta \boldsymbol{A}$ respectively, we obtain:
$$\nabla \cdot \boldsymbol{E} = \frac{\rho}{\epsilon_0}, \quad \nabla \times \boldsymbol{B} - \mu_0 \epsilon_0 \frac{\partial \boldsymbol{E}}{\partial t} = \mu_0 \boldsymbol{J}$$

These equations are two of Maxwell's equations.

Explanation and Significance

Through the principle of least action, Maxwell's equations are derived from the variational principle, demonstrating the dynamical properties of electromagnetic fields. This method not only provides an elegant mathematical framework but also reveals the fundamental symmetry and conservation laws of electromagnetic fields.

### Application in Relativity: Einstein-Hilbert Action

System Description

In general relativity, Einstein's field equations describe the relationship between the curvature of spacetime and the energy of matter. The Einstein-Hilbert action is the basis for deriving these field equations.

Definition of the Hilbert Action

The Einstein-Hilbert action $S$ consists of the contribution from the curvature of spacetime and the matter field, defined as:
$$S = \frac{1}{2\kappa} \int R \sqrt{-g} \, d^4x + S_{\text{matter}}$$

Where $R$ is the Ricci scalar, $g$ is the determinant of the metric tensor, $\kappa = 8\pi G/c^4$, $G$ is the gravitational constant, $c$ is the speed of light, and $S_{\text{matter}}$ is the action of the matter field.

Application of the Variational Principle

According to the principle of least action, variation is performed on the metric tensor $g_{\mu\nu}$ to extremize the action $S$, that is, $\delta S = 0$. This means that variation with respect to $g_{\mu\nu}$ leads to the emergence of Einstein's field equations.

Derivation of Einstein's Field Equations

The variation of $R$ involves the variation of the Riemann curvature tensor, which through complex calculations yields:
$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \kappa T_{\mu\nu}$$

Where $R_{\mu\nu}$ is the Ricci tensor, and $T_{\mu\nu}$ is the energy-momentum tensor, describing the distribution of matter and energy.

Explanation and Significance

The Einstein-Hilbert action closely connects geometric spacetime and matter energy through the principle of least action. Einstein's field equations reveal how matter affects the geometric structure of spacetime, thereby further influencing the motion of other objects, a view that is the core of general relativity.

### Application in Thermodynamics: Principle of Minimum Entropy Production

System Description

In non-equilibrium thermodynamics, a system tends to minimize the rate of entropy production to reach thermodynamic equilibrium. The principle of minimum entropy production is an important principle for describing processes such as fluid flow and heat conduction.

Expression of Entropy Production Rate

For a closed system, the entropy production rate $\sigma$ can be expressed as:
$$\sigma = \int_V \left( \frac{\boldsymbol{J}_q \cdot \nabla T}{T^2} + \sum_{i} \frac{J_i^2}{\sigma_i} \right) dV$$

Where $\boldsymbol{J}_q$ is the heat flux density, $T$ is the temperature, $J_i$ is the flux for the $i$-th process, and $\sigma_i$ is the corresponding friction coefficient.

Definition of Action

In the variational principle of thermodynamics, a Lagrangian $l$ can be introduced, defined as a combination of the entropy production rate $\sigma$ and constraint conditions:
$$l = \sigma + \sum_{k} \lambda_k C_k$$

Where $\lambda_k$ are Lagrange multipliers, and $C_k$ are the constraint conditions of the system.

Application of the Variational Principle

According to the principle of least action, the variation of the action $S$ with respect to all independent variables is $\delta S = 0$, that is:
$$\delta S = \delta \int l \, dt = 0$$

This means that the system minimizes the entropy production rate $\sigma$ subject to the constraint conditions.

Example of Practical Application

Consider a simple heat conduction system. Through the principle of minimum entropy production, the heat conduction equation can be derived. Introducing the temperature gradient $\nabla T$ and the heat flux density $\boldsymbol{J}_q = -k \nabla T$, where $k$ is the thermal conductivity. Minimizing the entropy production rate $\sigma$, we can obtain the diffusion equation for heat conduction:
$$\frac{\partial T}{\partial t} = \alpha \nabla^2 T$$

Where $\alpha = \frac{k}{\rho c_p}$, $\rho$ is the density, and $c_p$ is the specific heat capacity at constant pressure.

Explanation and Significance

The principle of minimum entropy production provides a powerful tool in thermodynamics for predicting the direction of system evolution and the final state. By treating the entropy production rate as an action and applying the variational principle, the basic equations of thermodynamic processes can be systematically derived, revealing the fundamental driving forces and constraint relationships in non-equilibrium processes.

### Application in Astrophysics: Kepler's Laws

System Description

Consider two celestial bodies with masses $M$ and $m$ respectively, interacting with each other through gravity. The system can be simplified to a central celestial body of mass $M$ and a small celestial body of mass $m$ orbiting around it.

Expression of the Lagrangian

Assume that the mass $M$ is fixed at the origin, and the motion of the small celestial body is described as motion in a two-dimensional plane, with position vector $\boldsymbol{r}$. The Lagrangian $L$ is the kinetic energy $T$ minus the potential energy $V$:

$$L = T - V = \frac{1}{2} m \dot{\boldsymbol{r}}^2 - \left( -\frac{G M m}{r} \right) = \frac{1}{2} m (\dot{r}^2 + r^2 \dot{\theta}^2) - \left( -\frac{G M m}{r} \right)$$

Where $G$ is the universal gravitational constant, $r = |\boldsymbol{r}|$, and $\theta$ is the polar coordinate angle.

Solving the Euler-Lagrange Equations

For the generalized coordinates $r$ and $\theta$, solve the Euler-Lagrange equations:

For the Euler-Lagrange equation for $\theta$:

$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}} \right) - \frac{\partial L}{\partial \theta} = 0 \\ \Rightarrow \frac{d}{dt} (m r^2 \dot{\theta}) = 0 \\ \Rightarrow m r^2 \dot{\theta} = \text{constant} = L$$

This is a manifestation of angular momentum conservation.

For the Euler-Lagrange equation for $r$:

$$\frac{d}{dt} (m \dot{r}) - (m r \dot{\theta}^2 - \frac{G M m}{r^2}) = 0 \\ \Rightarrow m \ddot{r} = m r \dot{\theta}^2 - \frac{G M m}{r^2} \\ \Rightarrow \ddot{r} = r \dot{\theta}^2 - \frac{G M}{r^2}$$

Derivation of Kepler's Third Law

Using the conservation of angular momentum $L = m r^2 \dot{\theta}$, we can solve the above equation to obtain the orbital equation. For an elliptical orbit, through further derivation, we can obtain Kepler's third law:

$$T^2 = \frac{4 \pi^2}{G(M + m)} a^3$$

Where $T$ is the orbital period, and $a$ is the semi-major axis of the ellipse.

Explanation and Significance

Through the principle of least action, we have successfully derived the laws of motion of celestial bodies, especially Kepler's laws. This demonstrates the important application of the principle of least action in classical celestial mechanics and also laid the foundation for Newton's theory of universal gravitation.

## Modern Development of the Principle of Least Action

With the rapid development of science and technology, the application domain of the principle of least action continues to expand, penetrating deeply into multiple frontier areas of modern physics and engineering. It not only provides powerful mathematical tools for theoretical physics but also plays an important role in practical engineering design and optimization. The following will explore in detail the specific applications and developments of the principle of least action in quantum mechanics, general relativity and geometric physics, as well as modern engineering and optimization.

### Action in Quantum Mechanics

In quantum mechanics, the principle of least action has been widely applied and deepened through the path integral method. This method was proposed by Richard Feynman in the 1940s, providing a new perspective for understanding and calculating the behavior of quantum systems. Unlike the single deterministic trajectory in classical mechanics, the path integral method considers that a particle, in moving from an initial point to a final point, traverses all possible paths, with each path's contribution to physical quantities being proportional to the exponential of its action.

The mathematical expression of the path integral is:
$$\langle q_f, t_f | q_i, t_i \rangle = \int \mathcal{D}[q(t)] \, e^{\frac{i}{\hbar} S[q(t)]}$$

Where $S[q(t)]$ is the action, and $\mathcal{D}[q(t)]$ represents the integral over all possible paths. Through this expression, Feynman successfully transformed quantum mechanical problems into extremal problems of action in classical mechanics, thus presenting complex quantum phenomena in a more intuitive way.

Advantages and Applications of the Path Integral Method:

Applications in Quantum Field Theory: In quantum field theory, the path integral method simplifies calculations of particle interactions, especially showing its unique advantages when dealing with non-perturbative problems. For example, in quantum chromodynamics (QCD), the path integral provides a powerful tool for studying strong interactions, helping physicists understand bound states between quarks and gluons.

Applications in Statistical Physics: Path integrals are not only used in quantum mechanics but also widely applied in statistical physics. By introducing imaginary time path integrals, researchers can analyze the thermodynamic properties of systems, such as phase transitions and critical phenomena.

Quantum Computing and Information: With the development of quantum computing, the path integral method also shows potential in quantum algorithm design and optimization. By viewing the evolution process of quantum states as a superposition of paths, engineers can design more efficient quantum computing schemes.

Practical Cases:

For example, in studying the double-slit interference experiment, the path integral method not only retains the intuitive explanation of classical interference but can also explain the probability distribution characteristics in quantum interference. By considering all possible paths comprehensively, the path integral provides profound insights into understanding quantum superposition and measurement mechanisms.

### General Relativity and Geometric Physics

Einstein's general relativity is a modern theory describing gravity, with one of its core ideas being to describe gravitational phenomena as the curvature of spacetime. The principle of least action plays a crucial role in the framework of general relativity, through which Einstein's field equations can be derived, revealing the profound connection between matter and spacetime geometry.

The Einstein-Hilbert action is defined as:
$$S = \frac{1}{16\pi G} \int R \sqrt{-g} \, d^4x + S_{\text{matter}}$$

Where $R$ is the scalar curvature, $g$ is the determinant of the metric tensor, and $S_{\text{matter}}$ represents the action of the matter field. By performing variation on the action $S$ with respect to the metric tensor $g_{\mu\nu}$, we can obtain Einstein's field equations:
$$R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R = \frac{8\pi G}{c^4} T_{\mu\nu}$$

These equations reveal how the energy-momentum tensor $T_{\mu\nu}$ of matter affects the geometric structure of spacetime, thus describing the gravitational action.

Specific Applications of the Principle of Least Action in General Relativity:

Prediction and Observation of Gravitational Waves: Through the principle of least action, Einstein predicted the existence of gravitational waves. These spacetime waves were first directly observed by the LIGO experiment in 2015, verifying an important prediction of general relativity.

Black Hole Physics: The principle of least action helps physicists gain a deeper understanding of the properties of black holes, such as event horizons, singularity structures, and black hole thermodynamics. This is important for studying the most extreme physical conditions in the universe.

Applications in Cosmology: In the study of large-scale structure formation and cosmic expansion, the principle of least action provides a unified mathematical framework, helping to explain the existence of dark energy and dark matter and their effects on cosmic evolution.

String Theory and Quantum Gravity: In geometric physics, string theory views particles as one-dimensional strings, describing the vibration modes of strings through the principle of least action. This theory attempts to unify general relativity and quantum mechanics, becoming one of the main approaches to exploring quantum gravity.

Practical Cases:

For example, in studying the binary black hole merger process, the principle of least action, through numerical relativity methods, helps scientists simulate and predict the characteristics of gravitational wave signals. These simulation results highly match actual observational data, further verifying the accuracy of the theoretical model.

### Modern Engineering and Optimization

The principle of least action not only plays an important role in theoretical physics but also has wide applications in modern engineering, especially in structural optimization, control system design, and mechanical engineering. By modeling the behavior of physical systems as extremal problems of action, engineers can more effectively design efficient, stable, and reliable systems.

Structural Optimization:

In civil and mechanical engineering, the principle of least action is used to optimize structural design. For example, in bridge design, by minimizing the stress energy of the structure, the optimal distribution of materials can be found to achieve minimal material usage and optimal structural strength. This not only improves the economic efficiency of the structure but also ensures its safety and stability under various loads.

Control System Design:

In the field of automatic control, the principle of least action is closely related to optimal control theory. By defining appropriate performance indicators (such as energy consumption, response time, etc.), engineers can transform control problems into extremal problems of action. Using the calculus of variations and optimization algorithms, excellent control laws can be designed. For example, in drone flight control, by minimizing action, robust and efficient flight path planning can be achieved, enhancing the autonomy and response speed of the aircraft.

Robotics and Dynamic Systems:

In robotics, the principle of least action is used to plan the motion trajectory of robots, minimizing energy consumption and mechanical wear while completing tasks. This is important for improving the overall efficiency of robotic systems and extending their service life. Additionally, in the design of complex dynamic systems, by minimizing action, the dynamic response characteristics of the system can be optimized, enhancing its stability and reliability.

Materials Science and Nanotechnology:

In materials science, the principle of least action is used to study the microstructural evolution process of materials. For example, by minimizing the total energy of a material, the distribution of different phases in alloys and their interface morphology can be predicted, guiding material processing and heat treatment processes. Furthermore, in nanotechnology, the principle of least action helps researchers design nanostructures and nanodevices, achieving high-performance and high-efficiency functions.

Energy System Optimization:

In energy engineering, the principle of least action is used to optimize the design and operation of energy systems. For example, in wind power and solar power generation systems, by minimizing energy loss and maximizing energy conversion efficiency, the utilization rate of renewable energy can be improved, reducing energy costs. Additionally, in power grid optimization, the principle of least action helps engineers design efficient power transmission and distribution schemes, ensuring the stability and reliability of the power grid.

Biomedical Engineering:

In biomedical engineering, the principle of least action is used to optimize medical equipment and treatment plans. For example, in artificial joint design, by minimizing joint friction and wear, the service life of artificial joints can be extended, improving patients' quality of life. Additionally, in radiation therapy, by minimizing radiation doses to healthy tissues and maximizing therapeutic effects on tumors, the precision and effectiveness of treatment can be improved.

Transportation Optimization:

In transportation engineering, the principle of least action is used to optimize traffic flow and transportation routes. For example, in urban traffic management, by minimizing traffic congestion and maximizing road utilization, the efficiency of the transportation system can be improved, reducing traffic accidents and environmental pollution. Additionally, in logistics transportation, by minimizing transportation costs and time, the efficiency and reliability of the logistics system can be improved.

Financial Engineering and Economics:

In financial engineering and economics, the principle of least action is used to optimize investment portfolios and risk management. For example, by minimizing portfolio risk and maximizing expected returns, optimal investment strategies can be designed. Additionally, in option pricing and risk hedging of financial derivatives, the principle of least action helps financial engineers construct complex mathematical models to achieve accurate pricing and effective risk control.

Environmental Science and Ecology:

In environmental science and ecology, the principle of least action is used to study the dynamic equilibrium of ecosystems and resource optimization. For example, by minimizing the energy consumption of ecosystems and maximizing biodiversity, sustainable environmental protection strategies can be formulated. Additionally, in climate change research, the principle of least action helps scientists simulate and predict the evolution process of climate systems, providing scientific basis for addressing global warming.

Aerospace Engineering:

In aerospace engineering, the principle of least action is used to optimize the design of aircraft and orbital planning. For example, by minimizing fuel consumption and maximizing flight efficiency, efficient flight paths and orbits can be designed. Additionally, in the attitude control and orbital correction of spacecraft, the principle of least action helps engineers design precise control strategies to ensure the success of space missions.

Computer Science and Artificial Intelligence:

In computer science and artificial intelligence, the principle of least action is used to optimize algorithms and machine learning models. For example, by minimizing loss functions and maximizing model accuracy, efficient learning algorithms and prediction models can be designed. Additionally, in image processing and natural language processing, the principle of least action helps researchers develop advanced technologies and tools, improving the intelligence level of computer systems.

Chemical Engineering and Process Optimization:

In chemical engineering, the principle of least action is used to optimize chemical reaction processes and process design. For example, by minimizing reaction time and energy consumption, the efficiency and yield of chemical reactions can be improved. Additionally, in process control and optimization, the principle of least action helps engineers design efficient control strategies, ensuring the safety and economy of chemical production.

Social Science and Behavioral Research:

In social science and behavioral research, the principle of least action is used to analyze and predict human behavior and social phenomena. For example, by minimizing individual action costs and maximizing social welfare, reasonable social policies and behavioral models can be constructed. Additionally, in psychology and cognitive science, the principle of least action helps researchers understand and explain human decision-making processes and behavioral patterns.

Education and Learning Optimization:

In the field of education, the principle of least action is used to optimize teaching methods and learning strategies. For example, by minimizing students' learning burden and maximizing learning effects, efficient teaching plans and learning schedules can be designed. Additionally, in the development of educational technology and online learning platforms, the principle of least action helps educators create personalized and intelligent learning environments, improving educational quality and learning efficiency.

Logistics and Supply Chain Management:

In logistics and supply chain management, the principle of least action is used to optimize transportation routes and inventory management. For example, by minimizing transportation costs and time, the efficiency and reliability of logistics systems can be improved. Additionally, in supply chain design and optimization, the principle of least action helps businesses achieve optimal resource allocation and efficient supply chain operation, reducing operating costs and improving service levels.

Agriculture and Food Engineering:

In agriculture and food engineering, the principle of least action is used to optimize agricultural production and food processing. For example, by minimizing resource consumption and maximizing yield, the efficiency and sustainability of agricultural production can be improved. Additionally, in food processing and storage, the principle of least action helps engineers design efficient process flows and storage solutions, ensuring food quality and safety.

With its strong theoretical foundation and broad application prospects, the principle of least action has become an indispensable tool in modern engineering optimization and design. It not only improves the overall performance of engineering systems but also promotes the integration and development of interdisciplinary technologies, providing solid support for achieving more efficient and more innovative engineering solutions.

## Conclusion

The principle of least action is not only a brilliant jewel in physics but also a crystallization of scientists' wisdom. From Aristotle's philosophical thinking, to Euler and Lagrange's mathematical foundation, to Hamilton and Feynman's modern extensions, this principle has run through the course of physics development. It has not only helped us reveal the laws of motion in nature but also played an important role in fields such as optics, electromagnetism, relativity, and more. In the future, the principle of least action is expected to continue to shine in frontier areas such as quantum gravity, string theory, and new materials science. Through continuous exploration and innovation, we will further deepen our understanding of this principle, open up new scientific horizons, and inspire more scientific inspiration and technological breakthroughs.

## References

Xu Liang. The Principle of Least Action and the Development of Physics [M]. Sichuan Education Press, 2001.

Rojo A, Bloch A. The Principle of Least Action: History and Physics [J]. Cambridge University Press, 2018.

Xu Liang. The Principle of Least Action and the Development of Physics (I) - The Origin and Development of the Principle of Least Action [J]. Physics, 1993, 22(5): 281-285.

Zhu Shiliang, Wen Yongli, Yan Hui. The Principle of Least Action and Its Quantum Experiment [J]. Physics, 2023, 52(7).

Wu Niu Chuan Yue. The Principle of Least Action: The Invariant Cornerstone of the Physical Building [EB/OL]. [2021-12-09]. (https://zhuanlan.zhihu.com/p/443110537).

Y.Galbort. The Principle of Least Action [EB/OL]. [2020-08-05]. (https://zhuanlan.zhihu.com/p/168781828).