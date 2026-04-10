**Networks** **beyond** **pairwise** **interactions:** **structure** **and** **dynamics**


Federico Battiston [∗]

_Department_ _of_ _Network_ _and_ _Data_ _Science,_ _Central_ _European_ _University,_ _Budapest_ _1051,_ _Hungary_


Giulia Cencetti
_Mobs_ _Lab,_ _Fondazione_ _Bruno_ _Kessler,_ _Via_ _Sommarive_ _18,_ _38123,_ _Povo,_ _TN,_ _Italy_


Iacopo Iacopini
_School_ _of_ _Mathematical_ _Sciences,_ _Queen_ _Mary_ _University_ _of_ _London,_ _London_ _E1_ _4NS,_ _United_ _Kingdom_ _and_
_Centre_ _for_ _Advanced_ _Spatial_ _Analysis,_ _University_ _College_ _London,_ _London,_ _W1T_ _4TJ,_ _United_ _Kingdom_


Vito Latora [†]

_School_ _of_ _Mathematical_ _Sciences,_ _Queen_ _Mary_ _University_ _of_ _London,_ _London_ _E1_ _4NS,_ _United_ _Kingdom_
_Dipartimento_ _di_ _Fisica_ _ed_ _Astronomia,_ _Universit`a_ _di_ _Catania_ _and_ _INFN,_ _I-95123_ _Catania,_ _Italy_
_The_ _Alan_ _Turing_ _Institute,_ _The_ _British_ _Library,_ _London_ _NW1_ _2DB,_ _United_ _Kingdom_ _and_
_Complexity_ _Science_ _Hub_ _Vienna_ _(CSHV),_ _Vienna,_ _Austria_


Maxime Lucas
_Aix_ _Marseille_ _Univ,_ _CNRS,_ _CPT,_ _Turing_ _Center_ _for_ _Living_ _Systems,_ _Marseille,_ _France_
_Aix_ _Marseille_ _Univ,_ _CNRS,_ _IBDM,_ _Turing_ _Center_ _for_ _Living_ _Systems,_ _Marseille,_ _France_ _and_
_Aix_ _Marseille_ _Univ,_ _CNRS,_ _Centrale_ _Marseille,_ _I2M,_
_Turing_ _Center_ _for_ _Living_ _Systems,_ _Marseille,_ _France_


Alice Patania
_Network_ _Science_ _Institute,_ _Indiana_ _University,_ _Bloomington,_ _IN,_ _USA_


Jean-Gabriel Young
_Center_ _for_ _the_ _Study_ _of_ _Complex_ _Systems,_ _University_ _of_ _Michigan,_ _Ann_ _Arbor,_ _MI,_ _USA,_ _48109_


Giovanni Petri [‡]

_ISI_ _Foundation,_ _via_ _Chisola_ _5,_ _10126_ _Turin,_ _Italy_ _and_
_ISI_ _Global_ _Science_ _Foundation,_ _33_ _W_ _42nd_ _St,_ _10036_ _New_ _York_ _NY,_ _USA_
(Dated: June 3, 2020)


The complexity of many biological, social and technological systems stems from the richness of the
interactions among their units. Over the past decades, a great variety of complex systems has been
successfully described as networks whose interacting pairs of nodes are connected by links. Yet, in
face-to-face human communication, chemical reactions and ecological systems, interactions can occur
in groups of three or more nodes and cannot be simply described just in terms of simple dyads. Until
recently, little attention has been devoted to the higher-order architecture of real complex systems.
However, a mounting body of evidence is showing that taking the higher-order structure of these
systems into account can greatly enhance our modeling capacities and help us to understand and
predict their emerging dynamical behaviors. Here, we present a complete overview of the emerging
field of networks beyond pairwise interactions. We first discuss the methods to represent higher-order
interactions and give a unified presentation of the different frameworks used to describe higher-order
systems, highlighting the links between the existing concepts and representations. We review both
the measures designed to characterize the structure of these systems, and the models proposed in
the literature to generate synthetic structures, such as random and growing simplicial complexes,
bipartite graphs and hypergraphs. We then introduce and discuss the rapidly growing research on
higher-order dynamical systems and on dynamical topology. We focus on novel emergent phenomena
characterizing landmark dynamical processes, such as diffusion, spreading, synchronization and
games, when extended beyond pairwise interactions. We elucidate the relations between higherorder topology and dynamical properties, and conclude with a summary of empirical applications,
providing an outlook on current modeling and conceptual frontiers.


∗ [battistonf@ceu.edu](mailto:battistonf@ceu.edu)

- [v.latora@qmul.ac.uk](mailto:v.latora@qmul.ac.uk)

- [giovanni.petri@isi.it](mailto:giovanni.petri@isi.it)


2


**CONTENTS**


I. Introduction 3


II. Higher-order representations of networks 5
A. Elementary representations of higher-order interactions 5
1. Low- versus high-order representations 5
2. Graph-based representations 5
3. Explicit higher-order representations 7
B. Relations and links between representations 8


III. Measures 9
A. Matrix representations of higher-order systems 10
1. Incidence matrix 10
2. Adjacency matrix 10
B. Walks, paths and centrality measures 11
1. Degree centralities 11
2. Paths and path-based centralities 13
3. Eigenvector centralities 14
C. Triadic closure and clustering coefficient 15
D. Simplicial homology 16
1. Boundary operators and homology groups 16
2. Evolving simplicial complexes 16
3. Other measures of shape in simplicial complexes 17
E. Higher-order Laplacian operators 17
1. Hypergraph Laplacians 18
2. Combinatorial Laplacians 18


IV. Models 20
A. Equilibrium models 21
1. Bipartite models 21
2. Motifs models 24
3. Stochastic set models 25
4. Hypergraphs models 27
5. Simplicial complexes models 29
B. Out-of-equilibrium models 31
1. Bipartite models 32
2. Stochastic set models 33
3. Hypergraphs models 33
4. Simplicial complexes models 34


V. Diffusion 36
A. Higher-order diffusion 37
1. Edge-flows 38
B. Higher-order random walks 39
1. Random walks on simplicial complexes 39
2. Random walks on hypergraphs 40


VI. Synchronization 43
A. Phase oscillators 43
1. Higher-order Kuramoto model 43
2. Higher-order interactions from phase reduction 50
B. Nonlinear oscillators 52
1. Chaotic oscillators 52
2. Neuron models 53
C. Inference of nonpairwise interactions in coupled oscillators 55


VII. Spreading and social dynamics 57
A. Spreading in higher-order networks 57


3


1. Spreading on simplicial complexes 58
2. Spreading on hypergraphs 59
B. Opinion and cultural dynamics beyond pairwise interactions 61
1. Voter model 61
2. Majority models 63
3. Continuous models of opinion dynamics 64
4. Cultural dynamics 65


VIII. Evolutionary games 65
A. Multiplayer games on networks 67
1. Public goods game 67
2. Other multiplayer games 69
B. Games with higher-order interactions 69
1. Public goods game on bipartite networks 69
2. Public goods game on hypergraphs 70


IX. Applications 71
A. Social systems 72
B. Neuroscience and brain networks 75
C. Ecology 78
D. Other biological systems 83


X. Outlook and conclusions 85


Acknowledgments 87


References 88


**I.** **INTRODUCTION**


Any significant understanding of a complex system must rely on system level descriptions. Consider the following
exercise: take an ecosystem, and break it into its pieces. No matter how good or accurate our knowledge at the level
of the individual species is, chances are that our understanding of population dynamics (e.g. how the abundances of
the different species change in time) will be slim at best. The same holds true when we attempt to explain epileptic
seizures starting from the individual neurons of the human brain; or viral rumors spreading across societies from
individual human psychology. All these approaches fail because they are missing a fundamental ingredient of any
complex system, that is the rich pattern of nonlinear interactions between the system components. After many years
of reductionism, science has abandoned the idea that the collective behaviors of a complex system can be simply
understood and predicted by considering the units of the system in isolation [1], and now more than ever is embracing
the idea of complexity as one of the principles governing the world we live in.
Within this paradigm, networks have emerged as a reference modeling tool for complex systems [2]. Networks are
the maps that define the physical or virtual space where interactions take place. Add competitive and cooperative
relationships to an ecosystem, synaptic connections to the human brain, and human interactions to rumor spreading,
and readily the self-organizing patterns and the collective behavior we observe in nature begin to unravel and look
less obscure. Building on earlier work in mathematics, social network analysis and ecology, a handful of breakthrough
papers at the turn of the millennium has attracted the interest of the scientific community, triggering thousands of
contributions over the last twenty years and leading to the formation of the new multidisciplinary field of _Network_
_Science_ . This new research community has developed an unusual mixture of graph theory and statistical mechanics
into a flourishing discipline, with applications spanning the full range of science, from fundamental physics all the way
to the social sciences. The boundaries and potential applications are yet to be fully realized [2]. Still, the richness in
scope and tools has already made the field of networks an independent discipline, often referred to as a science of its
own. The growth of network science was also strengthened by the progressively wider availability of large datasets
with detailed information on social, technological and biological interactions, which provided the raw material for the
empirical validation of network models and predictions. We refer the reader interested in a first approach to network
science to the several early review papers [3–6] and textbooks [7–10] on the subject.


As exploration of real-world systems deepens, network scientists are realizing the need to further characterize and
enrich the relationships captured by a network description. This, however, creates problem: networks have originally


4


been understood as a collection of nodes, representing the elementary units of the system, and edges, describing
the existence of interactions between pairs of such units. Applications to real-world systems, however, require the
possibility to describe more details of an interaction [11], like for example: directed edges to describe the origin and
destination of a message; edge weights, to highlight the intensity of an interaction; and even signs on the edges to
distinguish whether a link encodes a productive or detrimental interaction among two units. In more recent years, a
large effort has been devoted to formalize and develop the mathematical tools to analyze _temporal_ _networks_, where
interactions are not static but unfold in the temporal dimension [12]. Similarly, many works have recently considered
the case of interacting systems where units can be connected by links of different nature, and which can be effectively
represented in terms of _multiplex_ _networks_ or _multilayer_ _networks_ [13].
All these aspects have contributed in many cases to a better network representation, but are networks themselves
enough to provide a complete description of a complex system?


The fundamental limit of networks is that they capture pairwise interactions only, while many systems display
group interactions. Indeed, in social systems, ecology and biology among other examples, many connections and
relationships do not take place between pairs of nodes, but rather are collective actions at the level of groups of nodes.
For instance, three or more species routinely compete for food and territory in complex ecosystems [14]. In other
cases, the presence of a third species influences the interaction between other two, affecting directly the interaction
(the link) rather than the species involved (the nodes). Similarly, social mechanisms, such as peer-pressure, inherently
go beyond the idea of dyadic connections. Collective interactions are not an entirely new idea, and to some degree
have appeared in early research on networks. Think for instance to the majority-rule model for the dynamics of
opinion formation, or the public goods game in evolutionary game theory. In addition to these examples, one of
the most successful streams of research in network science in recent years, complex contagion, naturally accounts
for multiple simultaneous interactions [15]. However, in all cases these applications tried to leverage the language of
pairwise networks to describe interactions of higher order, for example by using bipartite graphs [16]. Can we instead
find mathematical frameworks that can explicitly and naturally describes group interactions?


Simplicial complexes and hypergraphs are the natural candidates to provide such descriptions. And indeed, over
the last few years, a wave of enthusiasm for these representations has revolutionized our vision of and ability to tackle
real-world systems characterized by more than simple dyadic connections. The importance of high-order interactions
had been recognized already a long time ago [17–19], but this rejuvenated interest has brought a new, and much deeper
understanding of higher-order representations. There are no doubts now that moving beyond dyadic interactions is
fundamental to explain and predict collective behaviors that could not be described before.


The aim of this report is to provide a review of the state-of-the-art on the structure and dynamics of complex
networks beyond pairwise interactions, as well as a reference and perspective on crucial open questions in the field.
Together with this introduction, the report is organized as follows:


  - The first part (Sections II to IV) focuses on the structure of systems with higher-order interactions. In particular,
Section II provides an introduction to the mathematical frameworks underlying higher-order representations.
Section III describes the most common measures and properties currently used to describe the structure of
systems with many-body interactions. Finally, Section IV reviews random models of higher-order systems and
how they are used to make statistical inferences.


  - The second part (Sections V to VIII) focuses on the dynamics of systems with higher-order interactions. In
more detail, Section V discusses models of higher-order diffusion. Section VI describes the generalization of
oscillator models and synchronization. Section VII introduces recent models of spreading in social systems with
group structure. Section VIII reports on models of competition and cooperation among multiple agents.


  - Finally, Section IX is an overview of real-world applications to systems with higher-order interactions. Our final
conclusions and outlook are presented in Section X.


We conclude this preamble with a final remark. The idea to include higher-order interactions in network analysis
is very simple. To this end, going beyond pairwise interactions might not look harder than attaching weights or signs
to the edges of a graph. Yet, in practice, moving from pairs to a more complicated interaction structure is a difficult
issue, and it requires a great deal of sophistication and novel mathematical tools. This explains why the analysis of
this aspect of complex system has been heavily delayed compared to its weighted and signed, and even temporal and
multilayer counterparts. After all, classical physics already knew this: while a closed-form solution is available for the
two-body problem, solving for the trajectories of _n_ interacting bodies given their positions and momenta is still an
open problem!


5


**II.** **HIGHER-ORDER** **REPRESENTATIONS** **OF** **NETWORKS**


**A.** **Elementary** **representations** **of** **higher-order** **interactions**


_1._ _Low-_ _versus_ _high-order_ _representations_


We begin by first defining more precisely what we consider as interactions and, as a consequence, as higher-order
interactions. We define an _interaction_ as a set _I_ = [ _p_ 0 _,p_ 1 _,...,pk_ −1] containing an arbitrary number _k_ of basic
elements of the system under study, which we indicate as _nodes_ or _vertices_ . Such interactions can then describe
different situations in real systems, e.g. the coauthors of a scientific paper, a set of genes required to perform a
certain function, the coactivation of a group neurons during a specific task, etc. In a slightly counterintuive way,
we will denote the _order_ (or dimension) of an interaction involving _k_ nodes to be _k_ - 1: a node interacting with
itself only is a 0-order interaction, an interaction between two nodes has order 1, one among three nodes has order
2, and so on. Furthermore, we consider _higher-order_ _interactions_ to be _k_ -interactions with _k_ ≥ 2. Conversely, low
order interactions are those characterized by _k_ ≤ 1. In plain terms, low order systems are those in which only selfor pair-wise interactions take place (like edges in a graph), while _higher-order_ _systems_ (HOrSs, from now on) display
interactions in groups of more than two elements.


The distinction between low- and high-order interactions is needed for two reasons. First, it highlights the differences between the graph-theoretic descriptions, that shaped the study of complex systems in recent decades, and the
more recently (re)proposed descriptions based on genuine group interactions. Secondly, it allows us to clearly frame
the connections between such descriptions, their various overlaps and reciprocal mappings. Finally, our definition
explicitly leaves out other types of higher-order dependencies between the components of a system, as for example
those defined by multiple link types in multilayer networks [13, 20–23], or by non-Markovian paths in time-stamped
interaction data [12, 24]. While these are out of the scope of this review, the interested reader can find an extensive
discussion of these topics in the references mentioned above.


We define an interacting system ( _V,_ I) as the family of interactions I = { _I_ 0 _,...In_ } taking place on a node set _V_ .
To aid the intuition, let us make a specific example. Consider the node set _V_ = [ _a,b,c,d,e_ ] and the set of interactions
I = {[ _a,b,c_ ] _,_ [ _a,d_ ] _,_ [ _d,c_ ] _,_ [ _c,e_ ]} (Fig. 1A). I contains three 1-interactions and one 2-interaction. While the complete
information about the systems is included in the list above, the study of most interesting properties of the system
requires the choice of a representation. For example, measuring the collective effects of the interactions on a specific
node requires the capacity to map interactions of different orders in a way that makes them comparable to each other;
asking how dense the system is, or whether one node is reachable from another, again requires being able to compare
in a controlled way interactions of different order and composition.


_2._ _Graph-based_ _representations_


Graphs are the most common way to represent families of interactions (Fig. 1C). A graph _G_ = ( _V,E_ ) is defined by
a nodeset _V_ with _n_ elements, and an edgeset _E_ whose _m_ elements are pairs of nodes. A graph is then a collection of
edges connecting pairs of nodes. In other words, the building blocks of graph representations are 1-interactions, i.e.
interactions of the type _I_ = [ _i,j_ ]. The most natural choice is then to unfold each higher-order interaction in I in terms
of 1-interactions built from pairs of nodes in _I_ . Under this assumption, our example I = {[ _a,b,c_ ] _,_ [ _a,d_ ] _,_ [ _d,c_ ] _,_ [ _c,e_ ]}
maps to IG = {[ _a,b_ ] _,_ [ _b,c_ ] _,_ [ _c,a_ ] _,_ [ _a,d_ ] _,_ [ _d,c_ ] _,_ [ _c,e_ ]} (Fig. 1B). This mapping makes systems amenable to be studied
using tools developed in both graph theory [25] and network science [7]. Indeed, graph representations enabled the
growth, depth and breadth of results on real-world complex networks in the last two decades [8–10], with applications
spanning biology [26, 27], ecology [28, 29], social science [30, 31], engineering [32, 33], neuroscience [34–36], all the
way to cosmology [37].
Despite the power of graph representations to capture many properties of complex interacting systems, their limits
are easily identified: it is impossible to explicitly describe group interactions, or in other terms there is no direct
relationship between I and I _G_ nor any way to recover the former from the latter. For example, going back to our toy
example, at the description level provided by I _G_, it is impossible to tell (and hence to describe) whether the original
interaction set contained [ _a,c,d_ ] or not. Naturally, in some cases networks can provide information on higher-order
interactions, but these are always inferences based on the low order interactions, obtained for example by looking
for very dense subsets of nodes using community [38], clique [39] or block detection [40] techniques. However, such


6















**G**













Building blocks:









link



















1-simplex 2-simplex 3-simplex


1-hyperlink 2-hyperlink 3-hyperlink

























FIG. 1. **Representations** **of** **higher-order** **interactions.** A set of interactions of heterogeneous order (A) can be represented
using only pairwise interactions (B). Using only low order blocks, the set of interactions can be described in th simplest way
by using a graph (C). Alternatively, interactions can be encoded as nodes in one layer of a bipartite graph, where the other
layer contains the interaction vertices (D). Other examples of high-order coordinated patterns can be encoded using motifs,
small subgraphs with specific connectivity structures (E). Among motifs, cliques are especially popular as they represent the
densest subgraphs, aking to higher order bricks (F). All these representations discard information that was present in the
original interaction data (A). A solution is to consider explicitly higher order building blocks, in the form of simplices and
hyperedges (G). Collection of simplices form simplicial complexes (H), which allow to discriminate between genuine higher
order interactions and -even complex- sums of low order ones (I). Unfortunately, simplicial complexes, given a simplex, require
the presence of all possible subsimplices (J), which can be too strong an assumption in some systems. Relaxing this condition
effectively implies moving from simplices to hyperedges (K), which are the most general—and less constrained—representation
of higher-order interactions (L).


reconstructions are often incomplete and rife with problems [41–43].


Bipartite graph representations effectively describe group interactions. Solidly within the realms of low-order
interactions, bipartite graphs are graphs defined by two nodesets ( _U,W_ ) and edgeset _E_ containing only edges ( _u,w_ )
such that _u_ ∈ _U_ and _w_ ∈ _W_ . To represent higher-order interactions, one chooses _U_ to coincide with the original
nodeset _V_, i.e. _U_ = _V_, and _W_ to coincide with the set of interactions I [44, 45]. The links in the bipartite graph
connect a node (in _V_ ) to the interactions (of arbitrary order) in which it takes part (Fig. 1D). This representation
emerges naturally in many fields: it is used for example in social sciences, where it provides a way to encode the
membership of individuals to groups of different dimensions [46, 47]; or to describe the collaboration of actors (nodes)
in movies (interactions) [48]; it is also used in ecological bipartite graphs, where species linked to a common prey
represent competition for resources among more than two species [29]; in recommendation systems [49] they describe
the relations between customers and purchased products, and so on.

It is easy to see that the entire information in our toy model is preserved when interactions are described as a
bipartite graph. In fact, this representation is very general and can indeed well mimic most interaction structures.
However, at difference with other multilayer graph formulations [13, 20], in a bipartite graph the nodes of the original
system do not interact directly with each other anymore. Rather, their relation is always mediated by the interaction
layer, which is of a different nature from the node layer itself. This implies that any measure or dynamic process
define on the bipartite representation needs to take into account this additional complexity. The usual workaround
to this problem is to consider the unipartite networks obtained by projecting the bipartite on one of the two layers.


7


Each interaction becomes then a fully connected subgraph among the nodes belonging to the interaction, losing the
group structure in the same way as in the simple graph case. In addition, it is usually impossible to translate the
information contained in the standard graph operators (e.g. Laplacian) defined on a bipartite graph into the ones
corresponding to the unipartite projections [50, 51]


Motifs allows to extract additional information on the properties of an interaction. They are the—usually small—
recurrent subgraphs of a given network, or of a class of networks of similar origin [52]. Motifs are defined as specific
patterns of edges (1-interactions) between vertices that appear to be statistically significant in the network (Fig. 1E).
They are considered structural signatures of the function of a network. That is, different motifs can correspond and
reflect different functions or different optimization solutions to the same function [53]. Typically, the statistically
validated frequencies (z-scores) with which the various motifs are observed in a network are collected into a motif
profile, which can then be used for example to discriminate between different networks [54], e.g. between brain
functional networks in different states [55, 56] or between differently evolved biological networks [27, 53, 57]. Motifs
also found widespread application in the study of social [58] and temporal [59, 60] systems.
Motifs constitute a refinement of the bipartite representation of a system, since, in addition to a division in groups
akin to that of bipartite graphs, they allow to specify the interaction pattern in which a node is involved. The
drawback to this is that the number of possible motifs to investigate grows exponentially with the number of nodes
involved. This unfortunately makes them quite unwieldy as a descriptive tool for large graphs and/or motifs. As an
example, generative models aimed to quantify randomness in networks via motif-based constraints [61] were shown
to become very hard to manage, or even sample, for interactions above order 2 [62].


Because of the exponential growth in the number of motifs, a large part of the work on analyzing subgraphs focuses
on a special type of motifs: cliques (Fig. 1F). A clique of size _k_ is defined as a fully connected subgraph of _k_ nodes.
Here, we use size for cliques to avoid confusion, since a _k_ -clique usually encodes an interaction of order _k_ - 1. The
interest in cliques is justified also by the fact that they represent the most obvious definition of group from a network
point of view, because they are the densest and most uniform motif [63]. Also, they directly encode the idea that
every member of the clique interacts with every other [64, 65]. Due to these properties, cliques are privileged building
blocks of a network and its communities [39]. However, we can incur into problems if we want to use cliques to
characterize higher-order interactions. In fact, going back to our toy example, we see that both sets _a,b,c_ and _a,d,c_
form 3-cliques. Conversely, in I _G_ we only had a true 2-interaction, namely [ _a,b,c_ ], while the fictitious interaction

[ _a,d,c_ ] is emerging as a byproduct of the union of the 1-interactions [ _a,d_ ] and [ _d,c_ ] with the [ _a,c_ ] edge induced by

[ _a,b,c_ ]. We can see then that, by considering all cliques present at the graph level, we would “fill” a 2-interaction that
was not included in the original interaction set. This is somewhat opposite to what happened when we considered
the edges alone. In that case, we lost completely the notion of group. In the case of cliques instead, we risk “filling”
too much and thus creating high-order interactions that were not there to begin with.


_3._ _Explicit_ _higher-order_ _representations_


To properly describe higher-order interactions, we need to encode them explicitly. Why not encoding interactions
exactly as they are in fact? Simplices are the simplest mathematical objects to accomplishes this. The formal
definition of simplices mimicks very closely the one we gave of higher-order interactions. In fact, a _k-simplex_ _σ_
is, in its most general form, just a set of _k_ + 1 nodes _σ_ = [ _p_ 0 _,p_ 1 _,...,pk_ ] (Fig. 1G). This notation is the standard
one borrowed from the literature in algebraic topology [66], where nodes are often points in a topological space. In
applications where the interactions are purely combinatorial, one might want to draw attention to the interactions
rather than to the underlying space. Thus, in these cases, nodes are often denominated as _v_ 0 _,v_ 1 _,..._ to highlight
that they are vertices of interactions, without any reference to an underlying space. The definition of dimension
of a simplex coincides then with the definition of order of an interaction we gave earlier. Based on this parallel
between the definitions of interactions and simplices, it is easy to see that we do not incur anymore in the problems
described above. However, it is not clear how we can handle interactions of potentially different dimensions together
and which are the advantages of such representations. Just like graphs are collections of edges, _simplicial_ _complexes_
are collections of simplices (Fig. 1H). At difference with graphs, they require further properties to be considered
valid complexes: a collection of _n_ simplices _K_ = { _σ_ 0 _,σ_ 1 _...σn_ } is a valid simplicial complex if, for every _k_ -simplex
_σ_ = [ _p_ 0 _,p_ 1 _,...,pk_ ] ∈ _K_, all its subfaces of any dimensions belong to _K_ too. For example, if the triangle [ _a,b,c_ ] ∈ _K_,
then we also require [ _a_ ] _,_ [ _b_ ] _,_ [ _c_ ] _,_ [ _a,b_ ] _,_ [ _a,c_ ] _,_ [ _b,c_ ] to belong to _K_ . Note that if we were to extract cliques from a
graph and consider them as simplices (which is the operative definition of a _clique_ _complex_ ), it would be impossible to
distinguish the two cases in which respectively the triangle was present or not. Using a simplicial formalism instead


8


this distinction is immediate, as we only need to check whether the 2-interaction [ _a,b,c_ ] is included in _K_ (Fig. 1I).
Simplicial descriptions are very powerful because they come equipped with many nice mathematical gadgets. It is
in fact straight-forward to define Laplacian operators for any dimension on simplicial complexes [67, 68], they can
approximate both regular manifolds and highly irregular structures [69, 70], and they come naturally equipped with
boundary operators stringing together simplices with different dimensions. Crucially, these operators describe the
topology and shape of simplicial complexes in terms of their cycles, cavities and higher-order topological holes [71]
and are naturally related to the combinatorial Laplacians [68]. In the following sections, we will describe many of
these properties in greater detail, because they represent some the most powerful tools currently available and are the
foundation of recent advances in topological data analysis [72–74].
Although simplicial complexes overcome some of the problems encountered by other lower dimensional representations,
they are still quite limited by the requirement on the existence of all subfaces. In some cases, this constraint is too
restrictive. For instance, when studying social systems, it is important to be able to describe interactions in groups.
In this case we can use simplicial complexes as it is rather safe to assume that a group interaction also implies the
underlying pairwise interactions (Fig. 1J). The relative importance of pairwise versus group interactions can then be
encoded in weights over the simplices.
However, in other cases, the inclusion constraint can be less easily justified: suppose for example that we are
studying collaborations in scientific papers, and we observe a paper by three authors and none by the corresponding
pairs of authors; or gene pathways were exactly three genes are needed to perform a function, but the subgroups are
not responsible for any function on their own. Clearly, it would be useful to be able to describe also these situations
(Fig. 1K).


Hypergraphs provide the most general and unconstrained description of higher-order interactions. Formally, a
_hypergraph_ is defined by a nodeset _V_ and a set of hyper-edges _H_ that specify which nodes participate in which way
within an interaction. Each hyper-edge is a non-empty subset of _V_ . It is easy to see that hypergraphs are the most
appropriate description of interacting systems ( _V,_ I) that we gave at the beginning of the section (Fig. 1L). Notice
that a hypergraph can include the 2-interaction [ _a,b,c_ ] without any requirement on the existence of 1-interactions

[ _a,b_ ] _,_ [ _a,c_ ] and [ _b,c_ ]. In fact, hypergraphs are so unconstrained that it is also possible to define hyperedges that include
other hyperedges, e.g. given _v,w,z_ ∈ _V_ and _γ_ = [ _v,w_ ] ∈ _H_, it is possible to define a new hyperedge _γ_ [′] = [ _z,w,v_ ; _γ_ ] ∈ _H_ .
Such extreme flexibility comes, as expected, with an additional complexity in treating them. For example, while
many graph-theoretic concepts can be extended to the case of hypergraphs, such an endevour is often fraught with
complications [75], to the point that a proper definition of Laplacian operators [76] on hypergraphs and of their
properties, e.g. the spectral diameter, has only emerged in the few last years [77, 78] and—to the best of our
knowledge—has found few real world applications, e.g. degree-generating models [79] and hypergraph modularity

[80, 81].


**B.** **Relations** **and** **links** **between** **representations**


Naturally, many questions emerge when discussing different representations of the same interacting system: how
much overlap is there among two different representations? Is it possible to map one onto another in a canonical
way? What kind of information is preserved (and lost) when moving between representations? For example, it seems
obvious that a simplicial complex composed only by 1-dimensional simplices (edges) should be the same thing as a
graph, right?
Well, it depends. Let us illustrate the links between representations starting from simplicial complexes (Fig. 2A).
There are many ways of writing down a simplicial complex, but we focus here only on two descriptions, that are
equally valid yet carry very different meanings: the Hasse diagram and the facet representation.


The Hasse diagram of a simplicial complex _K_ is the directed acyclic graph _HD_ ( _K_ ) = ( _VHD,EHD_ ), whose nodeset
_VHD_ contains a node for each simplex in _K_ ( _VHD_ = { _σ_ }∀ _σ_ ∈ _K_ ), while the edgeset _EHD_ contains an edge for each
inclusion between simplices that differ in dimension by 1 . In other terms, for two simplices _σ,τ_ ∈ _K_ there exist an
edge ( _σ,τ_ ) ∈ _EHD_ iff _σ_ ⊂ _τ_ and dim( _τ_ ) = dim( _σ_ ) + 1. In Fig. 2B we provide an example of a Hasse Diagram for a
toy simplicial complex (Fig. 2A) . It is easy to see that the Hasse Diagram unfolds all the structure in the simplicial
complex, by making explicit the hierarchy of simplices in the complex via its multipartite structure (one layer per
dimension), and thus providing information about its internal organization. Importantly, it also gives an explicit
way to walk on a simplicial complex: starting from a node (simplex), a walker can follow the links in the Hasse
Diagram and explore the whole complex. It turns out that the structure of the Hasse Diagram directly relates to the
generalization of the graph Laplacian to simplicial complexes and to random walks on complexes. We will describe
this in detail in Sections III and V, but, even without the full theory, it is already possible to understand some of the


9





















a b c d e



FIG. 2. **Relations** **among** **representations.** A simplicial complex (A) is defined by the list of simplices that compose it. The
structure of the natural inclusions between simplices can be described as a graph (B), where nodes correspond to simplices and
edges the inclusions (in the figure, when two simplices are linked the top one contains the bottom one). Following the chain of
inclusions upward, one reaches the maximal simplices, _facets_, that are not included in any larger simplex. These facets can be
used to define a bipartite (or hypergraph) representation of the simplicial complex, identifying the facets with the hyperedges
(C).


peculiarities of diffusion on simplicial complexes. The operators that link simplices that differ by ±1 in dimension,
akin to the links in the Hasse Diagram, are (co)boundary operators. For example, given a triangle (2-simplex), the
boundary returns a combination of the three edges that form the perimeter of the triangle. Taking its boundary
again, however, gives zero, because a boundary has no boundary itself (just like in standard differential geometry).
It is easy to see now that any operator built on top of such boundary operators, like the combinatorial Laplacian,
will only be able to describe diffusion between adjacent simplices with co-dimension 1. Similarly, it is easy to imagine
that operators defined on different representations are not necessarily equivalent, as for example shown recently by
Schaub and Segarra [51], that found that the Laplacian built on a graph, on its line graph and on the corresponding
1-dimensional complex are not mutually exchangeable.

On the other extreme, the facet representation of a simplicial complex is the most parsimonious in terms of number
of stored simplices. A _facet_ for complex _K_ is a simplex that is not contained in any other simplex in _K_ . In the Hasse
Diagram, facets correspond to nodes that are not included in any other. In Fig. 2B they are indicated as the simplices
with an orange contour. In this sense, facets are akin to maximal cliques in graphs, and, just like maximal cliques, the
list of facets of a complex uniquely identifies it. It is also a compressed description because it implies the existence
of all the subsimplices without explicitly listing them. In truth, the facet representation is a directed bipartite graph
under disguise, where facets constitute one layer, vertices the other, and directed edges represent inclusion of a node
in a facet. It can also be recovered easily from the Hasse diagram, by keeping only the vertex layer and the simplices
that have zero outdegree (i.e. without anything above themselves) . This bipartite graph associated to the facet
representation can then also be studied as a hypergraph, where facet membership defines the hyperedges (Fig. 2C).
Note that the converse is generally false: a bipartite graph (or hypergraph) gives rise to a simplicial complex in the
facet representation only if no set of vertex nodes linked to a facet node (hyperedge) is a subset another set of nodes
linked to another facet node (hyperedge); in short, the incident node sets of facets need to respect the non-inclusion
properties of facets, or equivalently, no hyperedge can be included in another hyperedge.


**III.** **MEASURES**


In the previous section we have discussed the various ways and levels at which high-order interactions can be
described and represented. In this section we will focus on observables and measures that can be used to characterize
and quantify the structural properties of high-order interacting systems, at each level of their description. In particular,
in the case of cliques, hyperedges, sets, or simplices, many common notions developed for ordinary graphs have been
generalized to their higher-order counterparts. We will start by discussing how to describe interactions in terms of
matrices or tensors. We will then show how standard graph-based measures have been generalized and what are the
insights that can be extracted using them.


10


**A.** **Matrix** **representations** **of** **higher-order** **systems**


_1._ _Incidence_ _matrix_


In mathematics, the incidence matrix is the classical way to describe the relationships between two classes of objects.
First introduced by Kirchkoff in 1847 for applications to electrical circuits, the _incidence_ _matrix_ of a graph _G_ = ( _V,E_ )
is a _n_ × _m_ matrix _I_ = { _Iiα_ }, where _n_ is the number of nodes and _m_ is the number of edges. The entry _Iiα_ in row _i_
and column _α_ is 1 if node _i_ and edge _α_ are incident, and zero otherwise. The definition can be easily extended to
the case of higher-order interactions, in which case _α_ labels the most general type of interaction HOrS (Fig. 3A). For
example, in the case of hypergraphs, _n_ is the total number of nodes while _m_ is the number of hyperedges [18, 82]. In
particular, for hypergraphs allowing for a node to be represented more than once in each hyperedge, it can be useful
to weight the entries of the incidence matrix. In this case then the nonzero entries of the incidence matrix would
represent the number of times the vertex _i_ is present in the relative hyperedge [83]. Notice that the incidence matrix
can also be seen as the adjacency matrix of a bipartite graph with two node sets one of size _n_ and one of size _m_
(see Sec. II). In the case of simplicial complexes, the incidence matrix between nodes and simplices can be defined in
the same way (Fig. 3B). In the following, we will use the language of hypergraphs whenever the definitions apply to
simplicial complexes as well.
Incidence matrices come in handy when it comes to characterize the various properties of HOrSs. For instance, the
_degree_ of a node _i_ in either a graph or a HOrS can be defined as the sum of the elements of the _i_ th-row of the incidence
matrix. In a (simple) graph the column of an incidence matrix always sums to 2 as the relationships described are
always between two nodes of the graph. In a hypergraph (simplicial complex), however, the rows of the matrix can
have more than two non-zero elements as each hyperedge (simplex) can describe interactions among more than two
vertices. The sum of the elements of the columns of the incidence matrix define the size sequence of the hyperedges
(simplices) of the system. These two local measures, the degree of the nodes and the size of the hyperedges, are the
first measures one can use to study the properties of HOrSs.


_2._ _Adjacency_ _matrix_


From the incidence matrix of a graph we can also construct another matrix that fully encodes the connectivity of
the graph, the _adjacency_ _matrix_ _A_ . Since the matrix product _I_ ⋅ _I_ _[T]_ is a _n_ × _n_ matrix whose _i,j_ element is the number
of columns of the incidence matrix _I_ that contain both vertices _i_ and _j_, while _i,i_ gives the degree of node _i_, the
adjacency matrix of a simple graph can be defined as:


_A_ = _II_ _[T]_                - _D_ (1)


where _D_ is the diagonal matrix whose diagonal entries are the nodes degrees. The adjacency matrix _A_ is 0 along
the diagonal, while for _i_ ≠ _j_ the entry _aij_ = 1 iff nodes _i_ and _j_ are adjacent, that is, there exists an edge connecting
them. We can generalize the notion of adjacency matrix to the case of HOrSs by using the same expression in Eq. 1
and considering as _D_ the diagonal matrix whose diagonal entries are the number of hyperedges a vertex belongs to.
While for simple graphs there can be at most one edge connecting a pair of nodes _i_ and _j_, for HOrSs there can
be more than one hyperedge _α_ containing the two nodes. The adjacency matrix of a HOrS is then a _n_ × _n_ matrix
whose elements _aij_ are the number of hyperedges that contain both _i_ and _j_ (Figs. 3I,J for hypergraphs and simplicial
complexes respectively). When the hyperedges are weighted, the adjacency matrix of a hypergraph can be written as
_A_ = _IWI_ _[T]_ - _D_, where _I_ is the incidence matrix, _W_ is the diagonal matrix with the weights of the hyperedges along
the diagonal, and _D_ is a diagonal matrix with the degrees of the nodes along the diagonal [84].
From the incidence matrix, one can also define the _intersection_ _profile_ of a HOrS as


_P_ = _I_ _[T]_ _I,_ (2)


which is an _m_ × _m_ matrix, whose elements _Pαβ_ count the number of vertices in common between two hyperedges _α_
and _β_ and _m_ is the number of hyperedges (Fig. 3E). The intersection profile is useful in the statistical study of edge
intersections in hypergraphs [85]. The same construction also applies to simplicial complexes (Fig. 3F).


The adjacency between two vertices can be defined directly, without any dependence on the definition of an incidence
matrix. This approach is often used when the higher-order structures cannot be uniquely identified only by the set of
nodes involved, or when there is a theoretical need for a more restrictive notion of adjacency between two hyperedges
than just that they intersect in at least two vertices. For example, when studying motifs in a network, for each motif
_M_ one can construct a _n_ × _n_ adjacency matrix _AM_, where _n_ is again the number of nodes, and whose entries _aij_ are


11


the number of times _i_ and _j_ both belong to an instance of motif _M_ [54]. Such adjacency matrix can also be seen as
that of a weighted network built only of the instances of _M_ . It can be useful to notice that when _M_ is a _d_ -clique, then
_AM_ = _Ad_ is the adjacency matrix built from the incidence matrix containing only _d_ -dimensional hyperedges. This
same approach can be used to build incidence matrices representing the relationship between the nodes and HOrS
(Figs. 3C,D).
The adjacency matrices { _A_ 2 _,A_ 3 _,_ ⋯ _,Ad,_ ⋯} for each _d_ -dimensional hyperedge in the HOrS represent the weighted
networks underlying the HOrS, and can be collected in a natural way in an adjacency _tensor_ of dimension _d_, indexed
by the node labels (Figs. 3G,H). Further insights into the structure of the hypergraphs themselves [86] and into the
processes taking place over them [87, 88] can be obtained from studying the Laplacians of these networks and their
spectra, which will be introduced in Sec. III E.
Another reason for building an adjacency tensor without relying on the incidence matrix is practicality. For example,
simplicial complexes require to explicitly list all 2 _[k]_ simplices included in each _k_ -simplex and this can become very
impractical. This is due to the constraint on the existence of all subsimplices of any given simplex, which in turn is
fundamental for the correct construction of the useful algebraic structures that come with a simplicial complex (e.g.
walks and homology, see sections III B and III D 1). To avoid listing all the simplices in a simplicial complex, one could
only list the maximal simplices [89], as mentioned in section II. However, while this method effectively compresses the
global structure of a simplicial complex, it does not encode the relationships between the _k_ -simplices in the complex
and the _k_ + 1 and _k_ - 1-simplices, which are exactly the crucial ones to make the simplicial complex representation so
useful and unique among the other HOrSs.
In order to avoid this problem, one can define two _mk_ × _mk_ adjacency matrices for each dimension _k_ describing
respectively an upper adjacency _AU_ and a lower adjacency _AL_ for all _k_ -simplices. Here, _mk_ is the number of _k_ simplices. Following standard notation [90–93], two _k_ -simplices are lower adjacent if they intersect in a _k_ - 1-simplex,
they are upper adjacent if they are both faces of the same _k_ + 1-simplex. Then ( _A_ _[k]_ _L_ [)] _[αβ]_ [=][ 1] [only] [if] [the] _[k]_ [-simplices] _[α]_
and _β_ are lower adjacent, while ( _A_ _[k]_ _U_ [)] _[αβ]_ [=][ 1] [only] [if] [the] _[k]_ [-simplices] _[α]_ [and] _[β]_ [are] [upper] [adjacent] [[][94][].] [Another] [way] [of]
defining adjacency is to construct a single adjacency matrix _A_ _[k]_ that isolates lower adjacent interactions that are not
involved in upper ones, that is, _A_ _[k]_ _αβ_ [=] [1] [only] [if] [the] _[k]_ [-simplices] _[α]_ [and] _[β]_ [are] [lower] [adjacent] [but] [not] [upper] [adjacent]

[68, 94]. Both these definitions of adjacency will be instrumental in the study of node shortest path centrality defined
on paths on _k_ -dimensional simplices (Sec. III B).
It is also possible to define an adjacency matrix which generalizes the standard one used in simple graphs, that is
that an element _aij_ = 1 when the edge { _i,j_ } is present in the graph. To generalize this idea to higher-order interactions,
one needs to consider a combinatorial object _A_ indexed by all possible permutations of _α_ . Then, for each order _d_,

_d_

       - **�����������������** **�����������������**

one defines an _n_ × _n_ × ⋅⋅⋅× _n_ adjacency tensor **A** _d_ so that an entry _ai_ 1 _,...,id_ = _aα_ represents _d_ -dimensional set of nodes

participating in the higher-order interaction _α_ = { _i_ 1 _,...,id_ }. This means that _aα_ = 1 if the set _α_ is present, while
_aα_ = 0 otherwise. This definition was originally introduced in [95] in the context of ensembles of simplicial complexes
(Fig. 3L). However, it can be easily extended to hypergraphs and other set-based HOrS (Fig. 3K).


**B.** **Walks,** **paths** **and** **centrality** **measures**


Network centralities are node-related measures that quantify how “central” a node is in a network. There are many
ways in which a node can be considered so: for example, it can be central if it is connected to many other nodes
(degree centrality), or relatively to its connectivity to the rest of the network (path based centralities, eigenvector
centrality). In the following, we review some of the most common centralities and their possible generalizations to
higher orders.


_1._ _Degree_ _centralities_


The simplest centrality measure is the degree of a vertex, which counts how many other vertices are incident to it.
The degree can easily be defined from any of the adjacency matrices defined in Sec. III B as


_n_
deg( _i_ ) = ∑ _aij._ (3)
_j_ =1


Via the adjacency tensor introduced in [95], one can define a comprehensive generalized degree which incorporates
not only the dependecies of nodes to their higher-order counterparts, but also for any intermediate _δ_ < _d_ -dimension.


12



**Hypergraph**



**Simplicial** **Hypergraph** **Simplicial**
**complex** **complex**











b





b



b











b













**Incidence**
matrix


**Adjacency**
matrix
(edges)


**Adjacency**
matrix/tensor

(nodes)

















































A3(e : :) A3(d : :) A3(c : :) A3(b : : ) A3(a : :)


FIG. 3. **Matricial** **and** **tensorial** **descriptions** **of** **HOrSs** : Visualization of incidence matrices and adjacency matrices that
can be used to represent the structure of HOrSs. There are three types of matrices: (A-D) incidence matrices relating nodes
and edges, (E-H) adjacency matrices representing the connectivity of edges to edges via the nodes they share in common, and
(I-L) adjacency matrices relating nodes to nodes via edges. Furthermore, one can consider edges aggregated by dimensions (left
panels) or only subsets of edges of the same dimension, obtaining a collection of matrices, one for each of the different sizes of
hyperedges present in the HOrS (right panels).


In terms of the adjacency tensor, the generalized degree is defined as


_kd,δ_ ( _α_ ) = ∑ _a_ [′] _α_ (4)
_α_


and indicates the number of _d_ -dimensional simplices _α_ [′] that are incident on the _δ_ -dimensional simplex _α_ . For _δ_ = 0
the generalized degree reduces to the standard node degree centrality relative to _d_ -simplices. Finally, a coarser way to
quantify node degree centrality in simplicial complexes is to just count the number of maximal simplices (or _facets_ )
incident on a vertex [96].
When working with weighted hypergraphs, it is slightly trickier to properly define a degree. For example, Kapoor
et al. [97] illustrate how a node’s degree centrality can be defined it terms of either its incident hyperedges or its
adjacent nodes, where two nodes are considered adjacent if they belong to the same hyperedge. The degree centrality
of a node in a hypergraph becomes then defined as the number of nodes adjacent to it, and the weighted degree
centrality as the sum of weights of the ties of the node with the other nodes in the hypergraph.
How to define the weight of a tie is going to be important to identify the meaning of centrality. The weight can be
in the tie between two nodes as the number of hyperedges they both belong to, or on the hyperedge itself attached
as a function of its multiplicity. Kapoor et al. [97] compare degree centralities relative to five different definition of
hyperedge weight: constant, frequency based, Newman’s strength for collaboration networks, Gao’s weights for the
email dataset, the probability of a contact between the two nodes over _ℓ_ interactions in a group of size _k_ .


13



**A** **1-walk** **B** **2-walk** **C** **2-walk**



h





a



g a











FIG. 4. **Example** **of** _k_ **-walks** **on** **hyperedges.** The simplest walk, a 1-walk, is the one where hyperedges share only one
vertex (A) similarly to how walks are defined on graphs. Such walks can be generalised to larger intersections (k-walks), for
example 2-walks (B and C). Note that the size of the intersection poses no upper bound on the size of hyperedges along the
walk, for example B and C and composed hyperedges of different size while still being 2-walks. Figures adapted from Ref. [100].


Degrees in HOrSs can also be defined on hyperedges or simplices. In fact, for each hyperedge or simplex _α_ we
can define the deg( _α_ ) as the number of hyperedges that are adjacent to _α_ in some of the ways introduced earlier.
In particular, we can define a lower and upper adjacency degree in simplicial complexes [94, 98] as the number of
simplices that are either lower or upper adjacent to _α_, or the number of simplicies that are lower adjacent but not
upper adjacent to _α_ . Moreover, these adjacency definitions can be combined as done by Serrano and G´omez in

[93], where they introduce the maximal simplicial degree deg( _α_ ) = deg _A_ ( _α_ ) + deg _U_ ( _α_ ), that counts the number of
upper adjacent simplices to _α_ and the number of lower adjacent simplices that are not upper adjacent. Degree based
centralities can be defined building on any of the above definitions and generalizing on the graph based formulas. The
interested reader can find an exhaustive review of centrality measures for HOrSs in [94, 99].


_2._ _Paths_ _and_ _path-based_ _centralities_


To define a centrality relative to the entire network, we need to define an acceptable way in which one can traverse
a HOrS by defining walks along its connections. A walk in a simple graph is a sequence of vertices [ _v_ 1 _,v_ 2 _,_ ⋯ _,vℓ_ ] such
that two consecutive vertices are _vi,vi_ +1 are adjacent to each other. A walk where a vertex is present only once is
called a path.
After having introduced the concept of walks on HOrSs, then centralities can be defined using the classical definitions
as either the number of paths that go through node _i_ (betweeness centrality), or the average length of shortest path
between a vertex and all vertices in the graph (closeness centrality), the number of closed walks of different lengths
starting and ending at the same vertex (subgraph centrality). In the case of HOrSs, when defining paths, it is easier
to consider walks connecting two hyperedges (simplices) than walks connecting two vertices. This is because any pair
of nodes present in the two extremal hyperedges (simplices) of the path will be connected by exactly the same walk.
The easiest way to define a walk in a hypergraph is as a sequence of hyperedges with at least 1 vertex in common

[84, 100]. This definition follows from the notion of adjacency induced by the incidence matrix. Then, the subhypergraph centrality of vertex _v_ is the number of closed walks of different lengths in the network starting and ending
at vertex _v_ [82, 101], which can be expressed as


_Csh_ ( _vi_ ) = ∑ _u_ [2] _ij_ _[e][λ]_ _j_
_vj_


where _uij_ is the _i_ th component of the _j_ th eigenvector of the adjacency matrix.
This definition can be generalized to _k_ -walks between hyperedges as a sequence of hyperedges such that each pair
of successive hyperedges are adjacent and they intersect in at least _k_ vertices [91, 102]. This in turn requires that all
hyperedges in the walk have dimension _s_ at least _s_ = _k_ + 1, but poses no constraints on their maximum dimension
_s_ . Examples of two simple walks for regular hypergraphs, one 1-walk and two different 2-walks, are shown in Fig. 4.
The corresponding closeness centrality is then the reciprocal of the average length of the shortest path between the
node and all other nodes in the HOrS [102].
The hypergraph definition of a _k_ -walk also applies to simplicial complexes [99] and can be used to define other
measures of betweeness and closeness centrality. However, in simplicial complexes, it is more appropriate to define a
_k_ -walk only comprised of _k_ -simplices that are lower adjacent i.e. have in common _k_ vertices (remember, a _k_ simplex
contains ( _k_ + 1)vertices) [94]. Just as before, the simplicial closeness of a _k_ -simplex is then the reciprocal of the sum
of its _k_ -shortest path distance to all other _k_ -simplices. The simplicial harmonic closeness centrality of a _k_ -simplex is
instead the sum of reciprocal _s_ -shortest path distance to all other _k_ -simplices.
In Fig. 5 we provide examples of how different configurations on _k_ and _s_ can yield different connectivity structures
for the same HOrS. If we allow any hyperedge or simplex dimension ( _s_ - 1) and any size of the intersection between


14



















FIG. 5. **Walks** **in** **HOrSs.** Visualization of the different definitions of walks on an toy example of higher-order network. From
left to right, the definition of the walk gets more restrictive. For each restriction on the defining variable of a walk (what
elements are allowed to be considered for a walk and how much do they need to overlap in order to be adjacent)–we color what
parts of the HOrS are reachable by at least a walk of length greater than one, and in gray what parts do not allow any walk to
pass through them. In (C,D), some parts of the HOrS are connected only if the HOrS is a simplicial complex, and we visualize
those with a striped pattern. We can see how the less restrictive walk (A), which can pass through two edges that have at least
one vertex in common, yields the same connectivity as its underlying graph. Restricting the intersection between two adjacent
edges to have at least 2 vertices in common, example (B), already highlights different mesoscale connectivity patterns in the
HOrS, which can be further studied introducing a further restriction on the size of the edges, examples (C) and (D).


them ( _k_ - 0), then we find that all paths are valid and the whole toy HOrS is connected. In fact, we recover the
simple graph connectedness (Fig. 5A).
If we instead require that interactions share at least two vertices ( _k_  - 1), some paths are not allowed. For example, the triangle [2 _,_ 10 _,_ 12] is not connected to any of the triangles in the tetrahedron [1 _,_ 2 _,_ 3 _,_ 4], because the only
intersection is 2.
Note also at this point that whether the HOrS is a hypergraph or a simplicial complex can make a difference. In
Fig. 5C, if we consider the HOrS to be a simplicial complex, the presence of the tetrahedron [1 _,_ 2 _,_ 3 _,_ 4] implies also
the presence of all the subfaces. Combining this with the requirement _k_ = 1, this also implies that some paths will
not be walkable, e.g. all the triangles inside the tetrahedron share an edge with each other. Hence one cannot walk
from one triangle to the other (shown as the black edges). However, there exist other paths that make the HOrS
connected, for example, [1 _,_ 2 _,_ 4] is connected to [3 _,_ 4 _,_ 5]. Similar considerations also apply to Fig. 5D, which shows
an example of the simplicial _k_ -walk described earlier in this section, that is, a walk limited to jumps between lower
adjacent simplices.


_3._ _Eigenvector_ _centralities_


In some applications, it is important to quantify the influence of a node on the entire network, rather than its
centrality relative to possible paths. First introduced in a sociological context by Bonacich [103], the eigenvector
centrality tries to capture this effect using an iterative definition. In fact, the eigenvector centrality a node depends
on the centrality of its neighbours [104]. In the graph case, it can be written as



_xv_ = [1]



_λ_ [1] _t_ [∑] ∼ _v_ _xt_ = _λ_ [1]



_λ_ _t_ [∑] ∈ _G_ _avtxt_ (5)



where _xv_ is the eigen-centrality of node _v_ and _avt_ the adjacency matrix of the graph. Note that again the generalization
to higher order interactions relies only on the definition of connectivity and paths. This measure has become widely
used in a variety of situations ranging from Google’s PageRank [105] to neuron’s firing rate [106]. Interestingly,
Bonacich [103] also showed that, if association is defined in terms of walks, a family of centralities can be defined


15


based on the length of walk considered. Degree centrality counts walks of length one, while eigenvalue centrality
counts walks of length infinity. Alternative definitions of association are also reasonable. Alpha centrality allows
vertices to have an external source of influence, while Estrada’s subgraph centrality proposes only counting closed
paths (triangles, squares, etc) [94, 101].
Bonacich [107] generalized eigenvector centrality to the case of bipartite graphs using their adjacency matrix. A
feature of this definition is that one can compute centrality score for the same eigenvalue for both node sets. Using the
same technique, one can compute eigenvalue centrality scores from incidence matrices for both hypergraphs, which
will give an eigencentrality score for both vertices and hyperedges. A two-mode analysis of an incidence matrix then
enables to identify central hyperedges in addition to nodes [108].
For motifs, it is possible to use the spectral features of the weighted motif adjacency matrix _AM_ defined in III A.
For example, the clique motif eigenvector centrality score of node _i_ is given by the _i_ th component of the largest real
eigenvector of _W_ [109].
To incorporate non-linearities, we can make it so that the contribution of the centralities of two nodes in a 3-node
hyperedge is multiplicative for the third. To do so, one can define the centrality using the eigenvector of the tensor
**A** _k_, where _k_ labels the considered dimensions. There are several other types of tensor eigenvectors [110], and for this
reason Benson [109] use _Z_ - and _H_ -eigenvectors which are arguably the most well-understood and commonly used
tensor eigenvectors. The _Z_ -eigenvector centrality vector is then defined as any positive vector _c_ satisfying


_Tc_ _[m]_ [−][1] = _λc_ _[m]_ ∥ _c_ ∥1 = 1 (6)


for some eigenvalue _λ_ - 0 of the adjacency tensor _T_ = _Ak_, and respectively the _H_ -eigenvector centrality vector as the
positive real vector _c_ satisfying


_Tc_ _[m]_ [−][1] = _λc_ _[m]_ (7)


.
As we have seen before, for hypergraphs and simplicial complexes, adjacency can be defined not only at the vertex
level, but also between hyperedges. It is possible to introduce notions of centralities for simplices and hyperedges
through the components of the principal eigenvector of _Ak_ [94]. The simplicial eigenvector centrality of the _k_ simplex _α_ is given by the _α_ component of the principal eigenvector of _Ak_, and its simplicial Katz centrality as
_Kk,α_ = [∑ _p_ = 0 [∞] _x_ _[m]_ _A_ _[m]_ _k_ []] _[α]_ [where] [0][ <] _[ x]_ [ <] _λ_ 1(1 _Ak_ ) [.]


**C.** **Triadic** **closure** **and** **clustering** **coefficient**


A key concept in network analysis for going beyond node-related measures is triadic closure. It is a concept that
comes from sociology [111], which argues that a strong social tie between two persons can only occur if it is part of a
triangle. In other terms, my closest friends are the ones I share friends with. In a graph structure, triadic closure is
represented as 2-paths of length 2 that are closed by an third edge. The fraction of pairs of neighbouring nodes that
are themselves linked by an edge defines the node’s clustering coefficient. The clustering coefficient is an important
network measure, which informs on the density of a node’s neighborhood. This coefficient can also be computed
globally as the total percentage of 2-paths that are closed by and edge, i.e. are part of triangles.
This concept does not generalize well to bipartite graphs, because triangles  - as any other odd cycle  - do not exist
in bipartite graphs. The global clustering coefficient can however be defined through its one-mode projections, as the
number of 4-paths in the bipartite graph that are part of a 6-cycle [112, 113].
Other attempts to generalize the concept of clustering coefficient beyond pairwise relations focused on keeping
its close relation to the notion of triadic closure. One possibility is to define a local clustering coefficient from the
new definitions of neighborhood that a node can have in a HOrS [114]. For example, in a simplicial complex, a
neighborhood can also be defined at the maximal simplex level, and can also be defined for higher order simplices,
not only for nodes [99].
Another possibility is to redefine the notion of paths [82] as sequence of vertices ( _v_ 1 _,...,vℓ_ ) such that two adjacent
vertices _vi,vi_ +1 both belong to the same hyperedge _ei_ . Then, the clustering coefficient follows from its pairwise
definition as the ratio of 2-paths that are closed by an edge. In a HOrS, paths can also be defined as sequence of
_k_ -cliques, or _k_ - 1-simplices ( _e_ 1 _,...,eℓ_ ) such that two adjacent cliques _ei,ei_ +1 have _k_ - 1 nodes in common, which
we will call _k_ -paths as they are formed of _k_ -cliques. In this case too, the clustering coefficient is then defined as the
fraction of _k_ -paths of length _k_ that are part of a _k_ + 1-clique [115].
In simplicial complexes, we can distinguish between a closed _k_ -path of length _k_ + 1 and a _k_ -simplex. Hence, the
clustering coefficient can be defined as the ratio of closed _k_ -paths of length _k_ + 1 that are closed by a _k_ -simplex. In
particular, when considering triangles, this definition of the clustering coefficient can be used to verify the sociological


16


intuition behind the diadic triadic closure idea [96], that is, it is possible to count how many actual “full” triangles
(2-simplices) among the possible “empty” triangles constructed from three edges (a closed path of three 1-simplices).
Finally, this higher-order clustering coefficient can be further generalized to motifs in weighted or growing HOrS [116].


**D.** **Simplicial** **homology**


One of the main reasons to use simplicial complexes as representations for higher-order datasets is a new algebraic
toolset that studies the topology of the HOrS in a unique way: simplicial homology. Homology is an algebraic
topological concept that enables us to study the structure of a simplicial complex at different dimensional scales.
Before we can introduce homology, we need to define an algebraic structure on our simplicial complex. This requires
imposing an orientation for each simplex in the complex, formalized as the ordering of the vertices. The orientation
can be arbitrarily chosen, just like the choice of node labels in a network, and it is only needed in order to coherently
perform the computations. An orientations is an equivalence class on the vertex orderings, where two orderings are
equivalent if they differ by an even permutation [66, 117]. The orientation issue does not exist in a 0-simplex, since
the nodes are not oriented, and only arises when we deal with higher order graphs. For simplicity, and with no loss
of generality, we choose the orientation induced by the ordering of the vertex labels.


_1._ _Boundary_ _operators_ _and_ _homology_ _groups_


We can combine these oriented simplices in _k_ - _dimensional_ _chains_ _c_ = _r_ 1 _σ_ 1 + _r_ 2 _σ_ 2 + ⋯ where _σi_ are _k_ -dimensional
simplices and _ri_ ∈ F are coefficients in a field F. The collection of all possible _k_ -chains in _X_ is the vector space
_Ck_ = { _r_ 1 _σ_ 1 + _r_ 2 _σ_ 2 + _..._ ∣ _ri_ ∈ F _,σi_ ∈ _Xk_ } where _Xk_ is the set of _k_ -simplices in _X_ .
We can also define the dual space of _Ck_, denoted as the _co-chain_ _space_, _C_ _[k]_ as the linear space of all alternating
functions _f_ ∶ _Ck_ → R. Chain and co-chain space are just two sides of the same coin, as they encode the same
information. For instance, _C_ [1] can be interpreted as the space of edge-flow vectors and each of its elements _f_ assigns
a scalar to an edge, representing the intensity of flow along that edge with a sign which represent the agreement or
not with the chosen orientation of the edge.
We can relate the _k_ -chain space _Ck_ to the _k_ - 1 using the boundary operator, which maps each _k_ -simplex to its
_k_ - 1-dimensional faces _∂k_ ∶ _Ck_ → _Ck_ −1. When applied on a simplex _α_ = [ _v_ 0 _,...,vk_ ], it gives:


_k_
_∂k_ ([ _v_ 0 _,...,vk_ ]) = ∑(−1) _[i]_ [ _v_ 0 _,...vi_ −1 _,vi_ +1 _,...,vk_ ] _._ (8)
_i_ =0


Basically, in each term of the linear combination, we remove a vertex from the original simplex. In this way, we
obtain its boundary as an alternate sum of the _k_ - 1-order simplices. In a triangle [ _v_ 0 _,v_ 1 _,v_ 2], for instance, we get
the alternate sum of the three edges ([ _v_ 1 _,v_ 2] −[ _v_ 0 _,v_ 2] + [ _v_ 0 _,v_ 1]). The image of the boundary map, _im_ ( _∂k_ ), coincides
with the space of ( _k_ - 1)-boundaries. The kernel ker( _∂k_ ) is instead the space of _k_ -cycles, as it is easy to prove that
for every cyclic chain _c_ whose starting point coincides with the ending point _∂kc_ = 0. Moreover, _∂k_ - _∂k_ +1 = 0, which
implies that _im_ ( _∂k_ +1) ⊆ ker( _∂k_ ). The elements of ker( _∂k_ ) which are not included in _im_ ( _∂k_ +1) can be denoted with
the quotient space


H _k_ ≡ [ker][(] _[∂][k]_ [)] (9)

_im_ ( _∂k_ +1)


which takes the name of _k_ -th _homology_ _group_ . The elements of H _k_ correspond to the _k_ -cycles that are not induced
by a _k_ -boundary, namely the _k_ -dimensional _holes_ of our complex [66, 117].
The dimension of the homology group _Hk_ is called the _k_ -th Betti number and it represents a way to classify the
_k_ -dimensional topology of a HOrS. Specifically, the 0th Betti number represents the number of connected component
in the simplicial complex, the 1 _st_ Betti number is the number of cycles, the 2 _nd_ the number of voids enclosed by
2-dimensional simplices, 3 _rd_ the number of 4-dimensional voids etc.


_2._ _Evolving_ _simplicial_ _complexes_


Homology is an century old concept in algebra and is one the key tools for the study and classification of shapes
in mathematics [117]. Recently the concept has been extended to weighted and growing simplicial complexes [118].


17


Inspired by 90s shape theory [119], in the early 2000s persistent homology was invented in different research groups
around the globe [72, 120, 121] giving birth to the field of Topological Data Analysis [73]. _Persistent homology_ is a way
of computing the homology of a growing simplicial complex and to follow how its homological features evolve along
the filtration [122]. The filtration is a sequence of simplicial complexes that provide progressively finer approximations
of the data space under investigation. The persistence of certain homological features through the multiple scales
explored in the filtration is related to their relevance for the data space, with the typical assumption that more
persistent features are more important, although the exact interpretation of the persistence of a homological feature
depends crucially on how the filtration is constructed (see for example [123]). In the last 20 years the field has been
vastly developed, and new methods for tracking homological features have been introduced for cases when simplicial
complexes can also lose simplices along the filtration, _zig-zag_ _homology_ [124], or for when the growth of the simplicial
complex can be described through more than one parameter _multi-persistent_ _homology_ [125]. The interested reader
can find a good introduction to the theory and practice of persistent homology in [126] and [127]. A large fraction
of the work no HOrSs in real datasets requires some version of persistent homology. In section IX we provide some
examples of its use


_3._ _Other_ _measures_ _of_ _shape_ _in_ _simplicial_ _complexes_


Homology in all its variants (persistence, zigzag, multiparameter) is a powerful tool to classify structure according
to key mesoscale features. However, it is important to notice that it depends on the choice of coefficient field F
used to compute the homology. Moreover, homological invariants are not exhaustive in general, as they pertain
to homological equivalence classes, thus they compress some information away. This is rooted in the invariance of
topological properteis to deformations, the classical example being the topological equivalence between a mug and
a donut. Indeed, there are no complete topological classification known, and one can find examples of simplicial
complexes homologically indistinguishable from a 3-sphere (a sphere in 4-dimensions) that are not spheres at all [128].
Nonetheless, the homological invariants give unique insights in the dynamics that can exist in data spaces and as
mentioned above have found widespread application (see Sec. IX for relevant examples).
In addition to the full homological description, other invariants have been used in applications [129, 130]. Two
commonly used ones are the Euler characteristic and the Laplacian spectral entropy.
For any simplicial complex Σ, the Euler characteristic is defined as the alternating sum _χ_ = ∑ _[D]_ _k_ =0 [(−][1][)] _[k][f][k]_ [,] [where]
_fk_ is the number of simplices of dimension _k_ present in the simplicial complex, and _D_ is the maximal dimension of a
simplex in Σ [128].
The spectral entropy, first introduced by [131] for simplicial complexes, provides a measure of the degree of the
overlap between simplices in the complex via the study of the eigenvalues of the _Lk_ combinatorial laplacian. The
spectral entropy is then



1
_Hk_ = −
log( _fk_ )



_fk_
∑ _p_ ( _λ_ _[i]_ _k_ [)] [log][(] _[P]_ [(] _[λ]_ _k_ _[i]_ [))] (10)
_i_ =1



where _p_ ( _λ_ _[i]_ _k_ [) =] ∑ _λi λ_ _[i]_ _k_ _[i]_ _k_ [is] [the] [contribution] [of] [the] [eigenvalue] _[λ][i]_ _k_ [to] [the] [eigenspectrum] [of] [the] _[k]_ [th] [combinatorial] [laplacian]
_Lk_, and _fk_ the number of simplices of dimension _k_ present in the simplicial complex. The most general framework for
not _k_ -uniform hypergraphs requires a deeper analysis and the problem of generalizing a Laplacian for these structures
has been addressed by many scientists [68, 90, 132–134].


**E.** **Higher-order** **Laplacian** **operators**


The Laplacian is an operator that plays a key role in information processing of relational data, and has analogies
with the Laplacian in differential geometry. Similarly to the adjacency matrix, there is no unique way to generalize
the Laplacian to HOrSs. However, as networks can be thought of as a special subset of the larger family of HOrSs,
the graph Laplacian is a special case belonging to the more general family of Hodge Laplacians. The intuition here in
the construction of higher order Laplacians, either for hypergraphs or for simplicial complexes, is that the role played
by the nodes in the graph Laplacian is, at higher orders, played by links, triangles, tetrahedra and higher dimension
analogues.
In analogy with the standard construction in graphs, a straighforward way to introduce a higher order Laplacian
is to define a Laplacian matrix _L_ from one of the adjacency matrices introduced in Sec. III A. We can thus write:


_L_ = _D_                  - _A_ (11)


18


where _A_ is the chosen adjacency matrix, and _D_ is the diagonal matrix with the degree sequence of the nodes along
the diagonal [135, 136]. However, this approach yields a matrix _L_ that is equivalent to the Laplacian of the weighted
graph associated to the adjacency matrix _A_ [137].
The graph Laplacian can be interpreted as a particular case of the discrete Laplace operator representing the
flux density of the gradient flow of a function defined on the vertices of a graph. For hypergraphs and simplicial
complexes, because of their richer structure, there are multiple ways one can define Laplacians that are compatible with
the corresponding differential geometry operator. In particular, for _k_ -uniform hypergraphs and _k_ -regular simplicial
complexes we can define a unique adjacency tensor **A** _k_ that represents the HOrS. Then, one introduces a Laplacian
tensor which is the discretization of the higher order Laplace-Beltrami operator in differential geometry [138, 139].
This theoretical connection to the continuous operator opens the possibility to use the spectrum of this tensor to
study the diffusion properties of the HOrS. For example, in recent years, many authors have defined a Laplacian
operator on hypergraphs for specific diffusion processes [76–78, 140]. Another higher-order Laplacian, designed in
the context of synchronization in systems with higher-order interactions between oscillators places on the nodes,
and introduced in Ref. [141], is discussed in Sec. VI A. In the following subsections we provide explicit definitions
for Laplacian operators on hypergraphs and simplicial complexes. In Sec. V instead we discuss in details their
mathematical properties and their link to diffusion.


_1._ _Hypergraph_ _Laplacians_


Historically, the first attempt to generalize the Laplacian operator to hypergraphs along these lines is due to
Chung [136], who considered a simplified type of hypergraphs, the _s_ -uniform hypergraphs, where all the hyperedges
have the same size _s_ . Given an _s_ -uniform hypergraph _H_ with _N_ nodes and edge set _E_, for each ( _s_ −1)-subset of nodes,
_x_, we can define the degree _d_ ( _x_ ) as the number of edges involving vertices in _x_, and the diagonal matrix _D_ such that
_D_ ( _x,x_ ) = _d_ ( _x_ ). The adjacency matrix _A_ used in this case is a binary matrix such that _A_ ( _x,y_ ) = 1 if subsets _x_ and _y_
are connected ( _s_ - 1)-subsets that share _s_ - 2 nodes. Formally, that corresponds to _A_ ( _x,y_ ) = 1 if _x_ = [ _x_ 1 _,x_ 2 _,...,xs_ −1]
and _y_ = [ _y_ 1 _,x_ 2 _,...,xs_ −1] and _x_ ∪ _y_ ∈ _E_, and 0 otherwise. The Laplacian can then be defined as:


_L_ = _D_               - _A_ + _ρ_ ( _K_ + ( _s_               - 1) _I_ ) (12)


where _ρ_ = _d_ / _N_, _d_ is the average degree, and _K_ is the matrix of the complete graph, such that _K_ ( _x,y_ ) = 1 if
_x_ = [ _x_ 1 _,x_ 2 _,...,xs_ −1] and _y_ = [ _y_ 1 _,x_ 2 _,...,xs_ −1], and 0 otherwise.
Another possibility to define a hypergraph Laplacian is to derive the Laplacian from the transition matrix of a
random walk. For instance, Lu and Peng [100] considered _random_ _k-walks_ ( _k_ < _s_ ) on _s_ -uniform hypergraphs. These
are _k_ -walks generated as follows (Fig. 4). The walker starts from the sequence of _k_ visited vertices at the initial step
_x_ 0 edge. At each time step, let _S_ be the set of last _s_ vertices in the sequence of visited vertices in the hypergraph
_H_ = ( _V,E_ ). A random ( _s_ - _k_ )-set _T_ is chosen from the neighborhood Γ( _S_ ) of _S_ uniformly; here Γ( _S_ ) is given by
{ _T_ ∣ _S_ ∩ _T_ = ∅ and _S_ ∪ _T_ ∈ _E_ ( _H_ )}; the vertices in _T_ are added into the sequence one by one in an arbitrary order.
The definition of Laplacian is split in two cases:


  - For 1 ≤ _k_ ≤ _s_ /2 the _k_ -th Laplacian is defined as the Laplacian of a weighted undirected graph _G_ [(] _[k]_ [)] built such
that a random _k_ -walk on _H_ is essentially a random walk on _G_ [(] _[k]_ [)] .


  - For _s_ /2 ≤ _k_ ≤ _s_  - 1 the _k_ -th Laplacian is defined as the Laplacian of an Eulerian directed graph _D_ [(] _[k]_ [)] and the
random _k_ -walk on _H_ is in one-to-one correspondence to the random walk on _D_ [(] _[k]_ [)] .


Lu and Peng [100] also introduced _α_ -lazy random _k_ -walks, with 0 ≤ _α_ ≤ 1, which are modified random _k_ -walks where
with probability _α_ the walker stays at the current edge and with probability 1 - _α_ it moves by appending _s_ - _k_ vertices
to the sequence.


_2._ _Combinatorial_ _Laplacians_


For general simplicial complexes, a higher-order Laplacian can be defined for each dimension _k_ via two matrices
that encode respectively the roles of upper and lower adjacencies in dimension _k_ :


_Lk_ = _L_ _[k]_ _U_ [+] _[ L]_ _L_ _[k]_ (13)

where _L_ _[k]_ _U_ [and] _[L][k]_ _L_ [are] [called] [the] [upper] [and] [lower] [adjacency] [Laplacians.] [The] [full] [Laplacian] _[L][k]_ [is] [usually] [referred] [to]
as combinatorial, and each _k_ -order Laplacian encodes the relationships of _k_ -simplices with their adjacent ( _k_ + 1)−
(upper adjacency) and ( _k_ - 1)-simplices (lower adjacency).


19



**A**


b


**Boundary**
matrices



**Laplacians**












|-1|Col2|-1|Col4|-1|Col6|
|---|---|---|---|---|---|
|1|-1|||||
||1|1|-1||-1|
||||1|1||
||||||1|


|3|-1|-1|-1|Col5|
|---|---|---|---|---|
|-1|2|-1|||
|-1|-1|4|-1|-1|
|-1||-1|2||
|||-1||1|


|-1|1|Col3|Col4|Col5|
|---|---|---|---|---|
||**D**<br>-1|1|||
|-1||1|||
|||-1|1||
|-1|||1||
|||-1||1|












































|3|Col2|Col3|Col4|1|Col6|
|---|---|---|---|---|---|
||3||-1||-1|
|||3|-1|1|-1|
||-1|-1<br>|2|1 <br>|1|
|1||1|1<br>|2||
||-1|-1|1||2|


|-1|Col2|-1|Col4|-1|Col6|
|---|---|---|---|---|---|
|1|-1|||||
||1<br>|1|-1||-1|
||||1|1||
||||||1|





FIG. 6. **Construction** **of** **combinatorial** **Laplacian.** The first step required to define boundary operators is to endow
a simplicial complex with an orientation. Here we choose to orient our toy simplicial complex with a simple lexicographic
orientation (A). Once the orientation is fixed, it is possible to define boundary matrices; since there are only simplices with
order ≤ 2, we have two non trivial boundary matrices _B_ 1 (B) and _B_ 2 (C). Following Eq. (15), we can build the combinatorial
Laplacians corresponding to the three different dimensions of simplices in the simplicial complex: _L_ 0 defined on nodes, and
identical to the standard graph Laplacian (D); _L_ 1 defined on the edges (E); and _L_ 2 which is a scalar in this case because the
simplicial complex contains only one 2-simplex (F).


The link between _Lk_ and the simplices of dimension _k_ with those of dimension _k_ + 1 and _k_  - 1 can be readily
understood from the definition of _L_ _[k]_ _U_ / _L_ [.] [The linear boundary operators] _[ ∂][k]_ [described in Sec.][ III D 1][ can be represented]
as a matrix _Bk_, whose columns represent all the _k_ -dimensional simplices in the complex, and the rows the ( _k_ - 1)dimensional simplices. Element _β,α_ of _Bk_, ( _Bk_ ) _βα_, is non-zero if the _k_ - 1-simplex _β_ is a face of _k_ -simplex _α_, and
can be +1 or −1 according to the orientation induced on _β_ by _α_, that is the coefficient that _β_ has in the alternating
sum _∂k_ ( _α_ ). For each boundary operator, there exists also a _co-boundary_ _operator_ _∂k_ [∗] [∶] _[C][k]_ [→] _[C][k]_ [+][1][,] [that] [is,] [the] [adjoint]
of the boundary operator. In matricial form, this can be represented by the transpose conjugate matrix of _Bk_, _Bk_ _[T]_ [.]
These boundary matrices define _L_ _[k]_ _U_ [and] _[L][k]_ _L_ [as:]


_L_ _[k]_ _U_ [=] _[ B][k]_ [+][1] [∗] _[B]_ _k_ _[T]_ +1 _L_ _[k]_ _L_ [=] _[ B]_ _k_ _[T]_ [∗] _[B][k]_ (14)


The higher-order combinatorial Laplacian _Lk_ becomes then:


_Lk_ = _Bk_ _[T]_ [∗] _[B][k]_ [+] _[ B][k]_ [+][1] [∗] _[B]_ _k_ _[T]_ +1 (15)


Figure 6 shows the explicit construction of the combinatorial Laplacian for the simplicial complex in Fig. 3. We first
need to choose an orientation for the simplices in the simplicial complex. Here for simplicity we choose the orientation
to follow the lexicographic ordering on the nodes’ labels (Fig. 6A). Once fixed this, it is possible to compute the
two boundary matrices that we need in this case _B_ 1 and _B_ 2, corresponding respectively to the the boundary matrix
mapping chains of edges into chains of nodes (Fig. 6B), and to the boundary matrix mapping chains of triangles into
chains of edges (Fig. 6C). We can then easily compute the corresponding combinatorial Laplacians from Eq. (15),
obtaining the matrices in Figs. 6D-F. Note that for _L_ 0 and _L_ 2 there is only one contribution to the sum, because the
simplicial complex does not contain _k_ -simplices of order _k_ respectively less than 0 and larger than 1, hence one of the
two terms in the sum vanishes.
Since _L_ _[k]_ _U_ / _L_ [describe] [the] [relatedness] [between] [upper] [and] [lower] [adjacent] [simplices,] [they] [should] [be] [related] [to] [the]
upper and lower adjacency matrices _A_ _[k]_ _U_ / _L_ [described] [in] [section] [III A 2][.] [It] [is] [possible] [to] [rewrite] _[L][k]_ [as] [[][68][]:]


_Lk_ = _DU_ _[k]_ [−] _[A]_ _U_ _[k]_ [+ (] _[k]_ [ +][ 1][)] _[I][n]_ _k_ [+] _[ A]_ _L_ _[k]_ (16)


where _DU_ _[k]_ [is] [a] [diagonal] [matrix] [with] [on] [the] [upper] [degree] [of] [simplices] [computed] [from] _[A][k]_ _U_ [,] [and] _[n][k]_ [is] [the] [number] [of]
_k_ -simplices. Setting _k_ = 0, one recovers standard graph Laplacian of Eq. 12. In terms of boundary operators, it


20


is easy to see also how the combinatorial Laplacian is related to the Hasse Diagram (see Sec. II) of the Simplicial
complex. The first term on the rhs of Eq. (15) corresponds to moving from k-simplices down to ( _k_ - 1)-simplices and
then back up to _k_ -simplices, while the second term does the opposite, first up to ( _k_ + 1)-simplices and then back down
to _k_ -simplices.
The Laplacian is a crucial operator in the definition of diffusion processes on simplicial complexes [68, 131] which
will be discussed thoroughly in Sec. V. In particular, following from the Combinatorial Hodge theorem [66], the
combinatorial Laplacian decomposes the _k_ -chain space _Ck_ into three subspaces: _Ck_ = _im_ ( _Bd_ ) ⊕ ker( _Lk_ ) ⊕ _im_ ( _Bd_ _[T]_ +1 [)][,.]
These three subspaces represent the globally acyclic, the cyclic and locally acyclic components of the flow defined on
the combinatorial structure [131], which can be used to decompose and study the evolution of dynamical processes
on simplicial complexes [51]. Another interesting consequence comes from the fact that the kernel of the Laplacian
ker( _Lk_ ) = ker( _Bd_ _[T]_ [) ∩] [ker][(] _[B][d]_ [+][1][)] [is] [isomorphic] [to] [the] _[k]_ [-homology] [group] _[H][k]_ [.] [This] [in] [turn] [implies] [that] [the] [number]
of (homological) _k_ -holes is the same as the dimension of the kernel of _Lk_, establishing a direct link between the
homological and spectral representations of a complex’s topology. We leave to the interested reader to check that _L_ 1
in Fig. 6E has indeed a one-dimensional kernel corresponding to the one-dimensional hole in the simplicial complex
in Fig. 6A. Finally, we list a few additional spectral properties of _Lk_, which can be easily checked considering
subcomplexes of the toy complex in Fig. 6A:


  - If the simplicial complex consists of disconnected simplicial complexes, then the spectrum of _Lk_ is equal to the
union of spectra of each component’s _k_ -th Laplacian.


  - If the simplicial complex is formed by gluing two simplicial complexes along a _k_ -face, then the spectrum is the
union of the two spectra.


  - If the simplicial complex only consists of one simplex of dimension _q_, then the Laplacian spectrum only has one
eigenvalue, _µ_ = _q_ with multiplicity _q_ !/[( _q_    - 1 − _k_ )!( _k_ + 1)!] [131].


**IV.** **MODELS**


Models of HOrSs aim to reproduce, explain, and predict the structure of systems best described with interactions
that involve two or more elements of the systems. To allow for variability in their outputs, these models are often
specified as collections of random rules, i.e., as stochastic processes. Hence, they define implicit or explicit distributions
over sets of HOrSs. In what follows, we review a great many models of models for such HOrSs.
To better delineate the similarities and differences between models, we have organized them in two broad categories
based on the type of stochastic process used. In the first subsection (Sec. IV A), we review _equilibrium_ _models_ defined
as static distributions over HOrSs. In the second subsection (Sec. IV B), we review _out-of-equilibrium_ _models_, given as
sequences of distributions over HOrSs. Although the separation is not formally perfect (sequences sometimes converge
to equilibrium distributions), these models tend to be quite different in practice, which makes this classification a
natural one. Our choice is motivated also by the fact that the philosophy underlying these models are somewhat at
odd [142]. On the one hand, _equilibrium_ _models_ are usually simple and straightforward to analyze; they typically
make use of independence assumptions, which leads to distributions over HOrSs that can be written down analytically.
They are therefore well suited to making statistical inference and to acting as substrate for dynamical processes taking
place on HOrSs. On the other hand, _out-of-equilibrium_ _models_ typically lead to complicated outcomes despite their
simple specifications; this makes them ideal for explaining how the qualitative properties of real systems can emerge
from simple rules. We note, however, that this classification can sometimes be superficial, especially when there are
formal correspondence between equilibrium and growing formulation of models [143].
Under these two principal headings, we have also organized models by the representation in which they are expressed
(see Sec. II for an overview). We have found this separation useful because different threads of the literature have
historically favored a single representation, such that models given in the same representation tend to both rest
on similar assumptions, and have similar modeling objectives. At the same time, we recognize that from a strictly
mathematical point of view, the choice of representation is again superficial due to the formal correspondence between
HOrS representations [102]. Hence, we highlight formal equivalence whenever they exist.
On a final introductory note, we have limited the scope of this review by focusing on models where higher-order
interactions appear as “first-class citizen.” As a result, we have excluded network models that happen to generate
higher-order interactions as a byproduct, such as models of non-trivial clustering [144–146] or cliques [147, 148] in
networks.


21


**A.** **Equilibrium** **models**


_1._ _Bipartite_ _models_


We begin our review of equilibrium models with the bipartite configuration model (bipartite CM). It is perhaps the
best-known example of an equilibrium model described in the bipartite network representation. The bipartite CM
generates HOrSs where both the size of the interactions and the number of interactions per element can be controlled,
allowing one to investigate the impact of these quantities on the higher-order structure.
There are a number of variations on the theme of the bipartite CM [149]. In general, it is defined as some form of
maximally random distribution over all bipartite networks that have a fixed degree sequence or distribution (either
on average or exactly). For example, in one the version of the model, the degrees are fixed exactly: one provides two
sequences of degrees _**k**_ [(] _[A]_ [)] = ( _k_ 1 [(] _[A]_ [)] _,...km_ [(] _[A]_ [)][)] [and] _**[k]**_ [(] _[B]_ [)] [= (] _[k]_ 1 [(] _[B]_ [)] _,...km_ [(] _[B]_ [)][)][,] [one] [for] [the] _[m]_ [nodes] [in] [set] _[A]_ [and] [one] [for] [the] _[n]_
nodes in set _B_, but all the other properties are randomized. The probability of a bipartite graph _G_, according to this
model, is thus


1
_P_ ( _G_ ) = (17)
∣Ω( _**k**_ [(] _[A]_ [)] _,_ _**k**_ [(] _[B]_ [)] )∣


for all bipartite networks _G_ in the set Ω( _**k**_ [(] _[A]_ [)] _,_ _**k**_ [(] _[B]_ [)] ) of bipartite networks with these degree sequences, and it is 0 for
networks outside of this set. This version is sometimes called the microcanonical bipartite CM, or bipartite CM with
hard constraints [142]. The canonical (or soft constraint) version of the model only fixes the _expected_ degree of nodes

[16]; see Fosdick et al. [149] for a rigorous discussion of the various versions of the model.
Early references to the bipartite configuration model first appeared in ecology [150, 151]. Mathematically equivalent
objects—contingency table with fixed row and column sums—were also studied in statistics around the same time

[152, 153]. Network science and physics innovations in this area have included thus far: the use of probability
generating function to calculate properties of the model [16]; the introduction of statistical mechanics tools (grandcanonical ensembles) to analyze the model [154, 155]; hidden variable formalisms [156]; and the addition of fixed
degree-degree correlations to the model [157]. Direct generalizations of the bipartite configuration model have also
been proposed, focusing on networks that have more than two “parts.” Although it is typically not their explicit goal,
these generalizations allow one to model _k_ - 1 simultaneous _types_ of higher-order interactions, where _k_ is the number
of parts [158, 159] (see also Boccaletti et al. [13] for a review). They collapse back to the bipartite case when _k_ = 2.
The bipartite configuration model offers a paradigmatic example of how models of HOrSs are used to test hypotheses,
via a technique known as “null modeling.” The general idea behind null modeling is to generate maximally random
HOrSs with a few fixed properties matching that of an observed empirical system. If one observes that some other
unrelated properties are systematically reproduced in the randomized ensemble, then these properties are, in a way,
“explained” by the fixed properties. Hence, null modeling can help identify connections between the property of
HOrSs in empirical studies.
In the context of the bipartite CM, the fixed property is the degree sequence of the two node sets. By applying
this technique to bipartite networks of species co-occurrences, for example, it has been shown that the “number of
sites per species” and the “number of species per sites” determine the structure, so much so that one cannot conclude
on whether natural assembly rules drive the network formation [150, 151]. Similar conclusions have been reached
with the same method for bipartite networks of plant and pollinators species [155]. A variation on the bipartite
configuration model has also been shown to reproduce most of the properties of a network of questions and tags built
from the _stackoverflow_ knowledge database, again showing that degrees can “explain” many network properties [160].
We note, however, that slightly changing the model can alter the conclusions of network significance analyses a great
deal [85, 149]—one should carefully consider the modeling assumptions.


The bipartite CM is a special case of a much more general set of random models, known as exponential random
graphs model (ERGM), or logit models [161]. These models aim to generate networks in which one controls the
relative frequency of arbitrary small subgraphs (motifs). As we have seen in Sec. II, these motifs can be used to
encode higher-order interactions explicitly—and indeed we discuss versions of the ERGM that use motifs for this
explicit purpose in Sec. IV A 2 below. For now, however, we only focus on those versions of the ERGM that add
motifs _within_ the framework of bipartite networks. In other words, we focus on ERGMs that encode higher-order
interactions with two node sets, but that also use bipartite motifs to generate a richer distribution over HOrSs.
Formally, one defines a bipartite ERGM by choosing _Qµ_ ( _G_ ), the number of times that motif _µ_ = 1 _,...,K_ occurs in
_G_ . In the context of bipartite graphs, _Q_ 1 could refer to the number of isolated pairs of nodes, _Q_ 2 to the number of
paths of length four, and so on. The choice of motif set is, to a large extent, arbitrary, although it is usually influenced


22


by sampling and identifiability considerations [162]. An ERGM then assigns the probability


1
_P_ ( _G_ ∣ _**Q**_ _,_ _**λ**_ ) = _Z_ ( _**λ**_ ) = ∑ _e_ [∑] _[µ][ λ][µ][Q][µ]_ [(] _[G]_ [)] (18)
_Z_ ( _**λ**_ ) _[e]_ [∑] _[µ][ λ][µ][Q][µ]_ [(] _[G]_ [)] _G_


to the bipartite network _G_, where _**λ**_ = ( _λ_ 1 _,...,λK_ ) is a set of parameters that control the expected number of motifs
of each type in _G_ .
It is in the _unipartite_ network context that exponential random graphs first appeared [163, 164] (see our discussion
below in Sec. IV A 2). That said, there have since been quite a few explicit treatments of the bipartite case, coming
mainly from social network literature where bipartite networks are known as “two-mode data” [165]. A few early
models made use of small collections of local motifs, including a model that fixes the number of connected pairs
(with one node of each type at the ends) and the number of “two-stars” (number of times the pattern _v_ 1– _w_ 1– _v_ 2 is
found, where _vi_ is a node in part _A_ and _wj_ is a node in part _B_ ) [166, 167]. More complicated models controlling the
distribution of short paths [168] or that add annotations [169] soon followed.
It was eventually realized that sampling from ERGMs (both in the bipartite and the unipartite network context)
could be extremely challenging due to a _degeneracy_ _problem_ [170, 171], where the model place a high weight on empty
and fully connected networks only. This realization prompted the development of subtle physics-inspired sampling
methods for specific ERGMs specifications [172], and of entirely new specifications for the unipartite model [162].
Analogs to the new specifications were also proposed [173, 174] for the bipartite model, leading to improved inference.
Notwithstanding these problems, ERGMs have found many inferential applications. One popular use-case is generating typical network instances that match a set of motif counts _**Q**_ obtained via empirical surveys [175, 176].
Bipartite networks generated in this way have been used to quantify the significance of specific patterns of interactions found in political networks in the US [177], and in Russia during Brezhnevs era [178]. Another popular
use-case of ERGMs is to “invert the direction” of inference and consider _P_ ( _G_ ∣ _**Q**_ _,_ _**λ**_ ) as a _likelihood_ that can be
used to deduce _**λ**_ from a fully observed network _G_ with counts _**Q**_ [173]. These parameters can then inform us
about the presence and strength of structural effects in the network data [175]. It should be noted, however, that
the inference is not necessarily robust since the problems facing ERGMs, like degeneracy, can also affect inference

[179]. Additionally, it has been recently argued that if we consider—as we probably ought to—that network data we
have are usually sub-samples of a larger underlying network, then ERGMs can lead to misleading inferences [180, 181].


The two sets of models above—bipartite CMs and ERGMs—reproduce _local_ features like the number of the neighbor
of a node or the number of short loops. A different set of equilibrium models that instead focus on reproducing their
_mesoscale_ features [182]. These models control the frequency and organization of large patterns of connections
involving many of, but not all of, the nodes in a network [183]. Examples include disjoint communities of nodes,
disassortatively mixing groups [184], and separations in a core and a periphery [185].
These models are most often formulated as extensions of the well-known stochastic block model (SBM) [186] to the
bipartite case [187, 188]. The general idea is to split the node into two sets of _KA_ and _KB_ “blocks”—one set for each
part of the network—and to then connect the nodes randomly, with probabilities _**ω**_ that depend on their respective
blocks.
One simple instantiation of this idea goes as follows [189]. We denote by _**g**_ [(] _[A]_ [)] = ( _g_ 1 [(] _[A]_ [)] _,...,gm_ [(] _[A]_ [)][)] [and] _**[g]**_ [(] _[A]_ [)] [=]
( _g_ 1 [(] _[B]_ [)] _,...,gn_ [(] _[B]_ [)] ) the blocks of the nodes in each part (where _gi_ [(] _[A]_ [)] = _ℓ_ means that node _i_ of part _A_ belongs to block
_ℓ_ ∈{1 _,...,KA_ }). We then write the probability of a particular graph _G_ with incidence matrix _**B**_ = [ _bij_ ] as


_P_ ( _G_ ∣ _**ω**_ _,_ _**g**_ [(] _[A]_ [)] _,_ _**g**_ [(] _[B]_ [)] ) = ∏ ∏(1 − _ωgi_ ( _A_ ) _gj_ [(] _[B]_ [)] ) [1][−] _[b][ij]_ ( _ωgi_ ( _A_ ) _gj_ [(] _[B]_ [)] ) _[b][ij]_ _,_ (19)
_i_ ∈ _A_ _j_ ∈ _B_


meaning that an edge is placed between _i_ and _j_ with probability _ω_ ( _A_ ) . By varying the connection probably
_gi_ _gj_ [(] _[B]_ [)]

matrix _**ω**_ and the blocks, one can generate networks with arbitrary mesoscopic structure, ultimately approximating
all systems to arbitrary accuracy [190].
Equation (19) refers to a canonical or soft constraint bipartite SBM since the number of neighbors of a node is
fixed only on average by _**ω**_ and the blocks. Like the bipartite CM, the bipartite SBM, too, comes in many variants.
One can define a microcanonical version along the same lines [191], for example. Another variant considers that
edges have distinguishable types, e.g., in a user–movie bipartite network where edges represent ratings on a fixed scale

[192]. Yet another variant jointly models the degree sequence _and_ the mesoscopic structure, leading to a so-called
degree-corrected bipartite SBM [193] that, unlike the classical degree-corrected SBM, makes explicit the assumptions
that there are two node types [188, 189, 194] (Fig. 7A). Finally, it is also possible to introduce a hierarchy, with blocks
that are themselves grouped into larger blocks, and so on [195] (Fig. 7B).
The many versions of the bipartite SBM are used for what is another prototypical example of a HOrSs inference
problem: latent parameter inference. Indeed, different from the configuration models, the structure of a system does


23


FIG. 7. **Inference** **with** **the** **bipartite** **stochastic** **block** **model.** (A) The data represents people (as circle) interacting
through events (as squares). A variation on Eq. (19) assigns a likelihood to every joint partitions of the people and events.
A high likelihood partition is shown here using colors. Simpler methods incorrectly split the network along the black line.
Figure reproduced from Ref. [189]. (B) An elaborate hierarchical version of the bipartite SBM, applied to collections of words
interacting via texts. This time the blocks (indicated by vertical dotted lines) are themselves regrouped in high-level blocks,
hierarchically. Figure reproduced from Ref. [195].


not trivially determine the SBM’s parameters. In a configuration model, one calculates the degree of all the nodes of a
given bipartite network to determine what is the associated randomized ensemble of networks. In contrast, the SBM
assigns nodes to blocks via ( _**g**_ [(] _[A]_ [)] _,_ _**g**_ [(] _[B]_ [)] ), a piece of information that is typically not given—unless metadata is also
available [194]. This situation leads to a family of inference problems where the goal is to determine an assignment
of nodes to the blocks, from a networks structure alone (see Fig. 7 A). This goal has been the main driving force
behind the development of sophisticated model families [189, 191, 194], with formal equivalence to inference problems
in other fields, like topic modeling [193, 195, 196] or data biclustering [197].


The bipartite SBM assigns nodes to latent _discrete_ categories (blocks), and adds connections to the network at
random based on these categories. A somewhat related class of models instead assign continuous latent _positions_
to nodes and creates connections with probabilities parametrized by the distance between nodes in the latent space.
Much like the case of the bipartite CM and SBM, these models take the form of natural generalizations of simple
network models to the bipartite case.
The AB random geometric graph model [198], for instance, is a direct extension of the well-known random geometric
graph model [199]. In this model, two sets of nodes are first randomly embedded in a low-dimension Euclidean space.
Nodes _in_ _different_ _sets_ are then connected by edges, with a probability that depends on the distance _dij_ separating
them. The AB random geometric graph model makes use of the simplest possible connection rule: two nodes are
connected if and only if _dij_ < _r_ . But we note that some unipartite models consider more complicated functional form
for the connection probabilities [200] (see also the model that follows).
Another approach to latent space models builds on results coming from the network geometry literature [201]. In
these models, one embed nodes in an _abstract_ space of preferences (rather than a _literal_ space, like what is done in
the AB model). It is then possible to define general classes of models by specifying different connection rules and
embedding spaces [202]. The so-called S [1] × S [1] specification is perhaps the one that has been analyzed the most thus
far [202, 203]. In this version of the model, two sets of nodes are embedded uniformly at random on a circle (i.e.,
on the 1-sphere denoted S [1] ). The nodes are then assigned random hidden variables drawn at random from some
distribution [156]—denoted _φi_ if node _i_ is in set _A_ and _ψi_ if it is in set _B_ . Every pairs of nodes ( _i,j_ ) in different sets
are finally connected with a probability that depends on their distance _dij_ in S [1], as well as the value of their hidden
variables _φi_ and _ψj_ . The specific functional form analyzed in [202, 203] is


_dij_
_pij_ = _σ_ ( ) (20)
_µ_ _φiψj_


where _µ_ - 0 and _σ_ is any integrable function with image in [0 _,_ 1]. The likelihood of the whole network is therefore
_P_ ( _G_ ∣ _**d**_ _,µ,φ,ψ_ ) = ∏ _ij p_ _[b]_ _ij_ _[ij]_ [(][1][ −] _[p][ij]_ [)][1][−] _[b][ij]_ [where] _[b][ij]_ [is] [an] [entry] [of] [the] [incidence] [matrix.] [The] [role] [of] [the] [hidden] [variable] [is]
to allow for variations in the degrees [156], while the embedding helps control the level of clustering [204].


24


FIG. 8. **Example** **of** **HOrSs** **generated** **by** **the** **model** **of** **Gleeson** **and** **Melnik** **[208].** In this model a fraction _gk_ of
nodes of degree _k_ of a configuration model network [16] are replaced by cliques. Figure reproduced from Ref. [208].


The main use-case for latent space models is, again, inference. With a latent space model, one can take a real
bipartite network as input, and find the embedding in a latent space that best matches the network, using the
likelihood _P_ ( _G_ ∣ _**d**_ _,µ,φ,ψ_ ) to guide the search. This inference technique has been used to, for instance, infer the latent
geometry of bipartite networks of metabolites and of the reactions they intervene in [203].


_2._ _Motifs_ _models_


Motifs-based models are formulated as assembly rules for arbitrary collections of small graphs, like triangles,
short-loops, or cliques. They can be viewed as high-order models because they build systems from relationships that
are not strictly pairwise, even though these models are ultimately defined as distributions over classical networks.
Motifs-based models have a rich history going back to the early days of network science [205], preceded by work in
sociology [206, 207] and statistics [163].


The first motifs-based models of networks appeared in sociometry, motivated by the need for survey methods that
would categorize and quantify patterns of interaction among small subsets of individuals of a larger directed social
network [206, 207]. As we have mentioned above in Sec. IV A 1, Markov random graphs [163, 164] and their exponential
random graph model (ERGM) generalization [161] have been proposed early on to fulfill this role. In a nutshell, these
model describe maximally random distributions over networks _G_ whose properties _**Q**_ ( _G_ ) = ( _Q_ 1( _G_ ) _,...,GK_ ( _G_ )) are
fixed on average, in relative proportion controlled by the free parameters _**λ**_ = ( _λ_ 1 _,...,λK_ ). These models are therefore
quite general in what they can describe (see our discussion above and Eq. (18)).
To model higher-order interactions in the ERGM framework, one can select properties _**Q**_ that measure these
interactions directly. An example of a set of statistics could be: the number of edges _Q_ 1; the number of triangles _Q_ 2
(a closed three-way interaction); and the number of open triangle _Q_ 3 (an open three-way interaction).
The main inferential applications of the generic ERGM are the same as that of the bipartite ERGM: null modeling, and the construction of whole network description from local surveys [175]. There is also at least one further
application of ERGMs specific to unipartite networks: quantifying the significance of motifs. The idea here is to fix
the distribution of all small motifs, and compare the number of _larger_ motifs to the expected motifs counts in the
ensemble [52, 57]. This method identifies motifs that are either under- or over- represented in a graph, based on what
we expect from smaller connection patterns. The method has used to argue that some small motifs are “significant
subunits” that determine the function of the modeled system [52].


Another type of model of networks with motifs comes from the physics literature on spreading processes occurring
on clustered networks. These models tend to be very flexible and to reproduce quite a few structural characteristics of
real systems. They have been first and foremost used to study how structural changes affect the outcome of dynamical
processes unfolding on these networks.
One of the earliest model in this category [208] begins with a unipartite configuration model network, i.e., a random
network that follows some arbitrary degree distribution. After the initial network is constructed, one replaces a
fraction _gk_ of the nodes of degree _k_ with _k_ -cliques for all _k_ ≥ 3—selecting these nodes uniformly at random. The
nodes of the new cliques are then attached to one of the edges of the node they replace, which in turn leads to a
network with the same high-level structure as the original, but with added local clustering (Fig. 8). An earlier variant
of this model also exists where one controls _gk_ indirectly [209].
Another set of model also uses the configuration model to generate HOrSs, but perhaps more directly. In the
first model in this line of work, one not only specifies the degrees _**k**_ = ( _k_ 1 _,...,kn_ ) that a node should have, but also


25


the number of triangles in which it should participate **∆** = (∆1 _,...,_ ∆ _n_ ) [210, 211]. A generalization of the classical
stub-matching scheme [149] is then used to create random network respecting these sequences. Recall that in the
classical stub-matching scheme, we first assigns _k_ 1 _,k_ 2 _,...,kN_ “stubs”—half-edges—to nodes 1 _,_ 2 _,...,N_ . We then picks
a random matching of the all the stubs, in which all stubs are joined in pair to form full edges. The resulting random
network respects the degree sequences _**k**_ = ( _k_ 1 _,...,kN_ ) by construction. In the higher order stup-matching scheme, we
should think of a node _i_ as having _ki_ “edge stubs” and ∆ _i_ ‘triangle stubs’ attached to it. A network is then obtained
by matching the stubs of the all nodes: 2 partial edges form an edge, and 3 partial triangles form a triangle. One
variation on this models generalizes from triangles to generic cliques of size _c_ - 3 [212], but enforces the constraint
that nodes belong to only one clique [208], i.e., that they have a single triangle or more generally a single clique of
size _c_ ≥ 3 attached to them. The central quantity in that model is then _γ_ ( _k,c_ ), the probability that a node has degree
_k_ and belongs to a clique of _c_ nodes, with _k_ ≥ _c_ - 1.
Encompassing both the triangle and the single clique model is a generalization of the configuration model that
allows for generic distribution of motifs in the neighborhood of a node [213]. The model parameters are the number
of times a motif is attached to a node, and in which way. This can be represented, again, by ”stubs” stemming from
each node, where a stub of type ( _µ,p_ ) is attached to node _i_ when it participates in motif _µ_ in position _p_ . The final
graph is constructed by matching stubs of a same type to construct motifs. Specifically, say motif _µ_ is comprised of
_n_ 1 nodes in role _p_ 1, _n_ 2 nodes in roles _p_ 2, etc. Then one must pick _n_ 1 + _n_ 2 + _..._ stubs of the correct types at random
and create a motif connecting the nodes from which the stub stem. An even more general version of the above model
assigns _types_ (or colors) to nodes [214, 215]. The expected number of stubs of each type for a node then depends on
this type.
Inference with these general models is challenging, because it is not clear how one should select a meaningful set
of motifs to describe a given graph [213]. So far, the only proposed approach aiming to make this type of inference
relies on an information theoretic approach to “subgraph covers” [216].


There are a few other specifications of network models with motifs that do not fit squarely in any of the above
categories.


One generalizes the notion of “graphon,” a form of latent space model in which nodes are assigned random positions
_**x**_ on [0 _,_ 1] and pairs of nodes are connected with probability parametrized by these positions. The motif generalization [217] also assigns latent positions { _xi_ } _[N]_ _i_ =1 [to] [the] [nodes,] [drawn] [independently] [and] [identically] [according] [to] [some]
distribution on [0 _,_ 1]. Then, a motif _µ_ on _r_ nodes _v_ 1 _,...,vr_ in the collection of motifs _**µ**_ is added to the network with
probability


_P_ ( _µ_ ∣ _v_ 1 _,...,vr_ ) = _[κ][µ]_ [(] _[v]_ [1] _[,....,v][r]_ [)] (21)

_n_ _[r]_ [−][1]


where _κµ_ is a function of the latent positions. Although these generalized graphons do not appear to have been used
for inferential purposes, a few special cases of them (obtained by setting _r_ = 2 and only allowing edges) found extensive use. For example, one can approximate _κµ_ to identify the latent geometry likely to have generated a network [218].


A completely different motif mode known as the d _k_ -series approach fixes local motifs and maximizes randomness
otherwise [61, 62]. Formally, for a given _k_, one fixes the distribution of the number of all the motifs of _k_ [′] ≤ _k_ nodes
centered on a node. Hence with _k_ = 1, for example, one fixes the degree distribution, while with _k_ = 2 one fixes the
joint degree distribution of pairs of nodes. The d _k_ -series model crosses into high-order specifications when _k_ - 2;
for example when _k_ = 3, one fixes the distribution of wedges and triangles. This model find use in quantifying the
randomness of a network’s structure [62]. It fixes a null distribution where many local aspects are preserved, and
helps to see whether these local constraints are enough to “explain” the observed large scale structure of a network.
Actually carrying out the test for any _k_ ≥ 3 is difficult, however [62], since constructing a single example of graphs
realizing a series with _k_ ≥ 3 is NP-complete [219]. We note that there is related work in the social network literature,
in the form of models where one specifies the local structure—the “social neighborhood” of nodes [220]—up to a
certain distance [174].


_3._ _Stochastic_ _set_ _models_


Collections of motifs become rapidly intractable with growing motif sizes since there are 2 [(] _[r]_ 2 [)] possible undirected
graphs on _r_ nodes. Many models avoid this exponential blowup by specifying the motifs _stochastically_, i.e., by
assigning nodes to sets of _r_ nodes and then specifying the actual motif connecting them at random.


26



















a







a b c d e f g h i j k



a



FIG. 9. **Constructing** **random** **HOrSs** **by** **projecting** **a** **bipartite** **network** **of** **interactions** **[184].** (A) Realization of
the bipartite configuration model, (B) projected as a network, where (C) some edges are removed. The construction shown in
panels (A) and (B) is also known as a random intersection graph [225]. Figures adapted from Ref. [184].


A well-known family of models specified in terms of sets takes inspiration of hierarchies in social organizations, in
which nodes are assigned to nested groups [205, 221]. The groups are therefore proxy for higher-order interactions.
The simplest example of a model in this class only allows for one set of groups [205]. In this model, a node _i_ has
a membership number _ki_ [(] _[n]_ [)] (number of groups it belongs to), and a group _j_ has a size _kj_ [(] _[g]_ [)] (the number of nodes it
has). The rest of the structure is randomized. Hence, in other words the node–group relationships are described by
a bipartite CM [16]. Differently from the latter, however, one considers a _projection_ onto the nodes (see Sec. II), in
which edges are placed at random based on the group assignments. Specifically, one determines whether two nodes
are acquainted through a group, with probability 0 ≤ _q_ ≤ 1, and connects them in the projection if they are acquainted
through at least one group (see Fig. 9).
Among the many possible generalizations of this model, some have: considered a deeper hierarchy of groups [221];
include heterogeneities by introducing a group dependent connection probability _qr_ [222]; introduce the possibility of
forming a few ‘random’ links with nodes not in the immediate group of a node [223]; or used a mixture of groups [224].


An alternative point of view on these models comes from the mathematics literature, where they are known as
random _intersection_ _graphs_ [226]. A random intersection graph is formed by assigning a set on some alphabet—
say _Y_ = 1 _,..,m_ —to each node, and connecting two nodes if their respective sets intersect [225]. They are formally
equivalent to the bipartite projection model above, since we can think of the set of a node as the higher-order
interactions in which it participates, and of edges as arising because of these interactions (Fig. 9).
Many models of random intersections graph exist, but are somewhat less general than the projected bipartite CM
discussed above. This is because mathematically exact results are typically the goal of the authors studying these
models, rather than coming up with models of “realistic” HOrSs. An example of one such model is dubbed _G_ ( _n,m,p_ ).
It defines a distribution over HOrSs that have _m_ sets and _n_ nodes, and where every node is included independently
in each set with probability _p_ [225], yielding the likelihood



_n_ _m_
_P_ ( _**B**_ ∣ _m,n,p_ ) = ∏ ∏(1 − _p_ ) _[B][ij]_ _p_ _[B][ij]_ _,_ (22)
_i_ =1 _j_ =1



for the assignments _**B**_ of nodes to sets, where _Bij_ = 1 if node _i_ is in clique _j_ and 0 otherwise. This model is a
special case of the projected bipartite model discussed above, obtained by setting the degrees of nodes to _mp_, the
size of groups to _np_, and by connecting all nodes in a shared group with probability _q_ = 1. The properties of these
random intersection graphs have since been studied extensively, see the detailed review of Frieze and Karo´nski [227].
Inhomogeneous generalizations allow for some variations, such as inclusion probabilities _**p**_ = ( _p_ 1 _,...,pn_ ) that are node
dependent and fixed as parameters [228, 229], or where the size of the sets are drawn from a distribution and the
node in it chosen at random [230].
While the sets themselves are random in all of the random interaction graph models above, the _interior_ of sets
themselves are not random—all nodes are connected and form a clique. Other models of intersection graphs include
the possibility of noise in this process [231], and are therefore formally equivalent to the noisy version of the node–
group models discussed above [222]. For instance, one model assigns nodes to one or more cliques of varying sizes, and
two nodes are only connected in the projection with a probability that depends on the number of shared cliques [232].
A more exotic construction assigns nodes to the cliques with probabilities _pi_ that are the outcome of a stochastic beta
process [233].
As we have mentioned, in the mathematical literature, random intersection graphs are studied for their structural
properties [225]. But they also find inferential application in the epidemiological literature as models of systems with
higher-order interactions [234]. In the statistics literature, they have found application in fitting clique-cover models


27


to real networks [233], in the same spirit as the cover models used to fit models of networks with motifs [216].


We note in passing that some models of overlapping communities lead to formalisms close to that of the stochastic set
models mentioned here. However, since one seldom thinks of overlapping communities as higher-order interactions—a
typical community is far too big to classify as encoding an “interaction”—we will not review them here. The interested
reader can refer to the review of Xie et al. [235] for an overview of models of networks with overlapping communities.


_4._ _Hypergraphs_ _models_


Many equilibrium models of HOrSs incorporate multi-body interactions more directly, by encoding them in hypergraphs. Much of the work on random hypergraphs comes from the mathematical literature, where they were
introduced as immediate and natural generalizations of classical models in random graph theory.
Perhaps unsurprisingly, the earliest random model of hypergraphs was an extension of the well-known Erd˝os-R´enyi
(ER) model. In the most direct generalizations of this model, every hypergraph of _m_ hyperedges of size _k_ on _n_
nodes is given the same probability [236], with the ER case obtained by setting _k_ = 2. The structural properties of
the random hypergraphs generated in this way have been analyzed extensively, see [227] for a review. A canonical
variant, in which hyperedges are created independently at random with fixed probability _p_, also exists [147].
All hyperedges connect precisely _k_ nodes in the two models above. This is an arbitrary choice and not a constraint
of the hypergraph formalism. Other uniform models do away with this constraint, and include many sizes K =
{ _k_ 1 _,k_ 2 _,...,kℓ_ } of hyperedges simultaneously (where K ⊆ N is some choice of hyperedge sizes, with K = {2} corresponding
to a graph).
One version stipulates that all hypergraphs are equiprobable, provided that they have exactly _mk_ 1 hyperedges of
size _k_ 1, _mk_ 2 hyperedges edges of size _k_ 2, and so on for all _k_ ∈K (where _**m**_ and K are chosen at deterministically [237]
or at random [238]). Like in the classical ER case, hypergraphs that do not respect the constraint on the number
of hyperedges are assigned a probability zero. Yet another uniform model instead prescribes that each of the ( _[n]_
_k_ [)]
possible sets of size _k_ on _n_ nodes exists, with a probability _λk_ that depends on the size _k_ ⊆K of the set [239].
While the specifications of these models differ from cases to cases, the underlying goal is always to study the
properties of the generated hypergraphs, like their components structure, for example [237]. Even though these
uniform hypergraph model are somewhat crude approximation of real HOrSs, they have found extensive application
in technical fields like computer science, where they are used to generate the structure of idealized random decision
problems (random _k_ -sat) [240, 241].


Other uniform models differ from the ones above in that they ensure that the generated hypergraphs are “ _k_ -partite.”
By _k_ -partite, it is meant that the _n_ = _k_ × _r_ nodes of the hypergraph can be separated into _k_ disjoint subsets of _r_ nodes,
such that every hyperedge comprises of precisely one node in each subset. These _k_ -partite hypergraphs are useful
when one wants to encode interactions that _always_ involve nodes of different natures, for example, when modeling a
collaborative tagging system where all hyperedges connect an element, a person, and a tag [79].
One possible construction for uniform and random _k_ -partite hypergraphs was introduced in the mathematical literature, with the goal of studying “perfect matchings” in hypergraphs, i.e., minimal subsets of hyperedges connecting
every node [242, 243]. The model first singles out one the subset of nodes as “special.” Then it stipulates that, for
each node in this special subset, we should choose _d_ - 1 neighbors uniformly at random (one per subset) to form a
hyperedge, and repeats the process _z_ times per node in the special set [242]. The resulting hypergraphs are _k_ -partite
by construction, and all the nodes in the special set have precisely degree _z_ . A more general but still uniform model
of random _k_ -partite hypergraphs, coming from the information retrieval literature, eliminates this constraint [244].
Aiming for flexibility, the model assigns a different weight to every possible hyperedges, and places the hyperedges
with probability proportional to these weights. It is shown that, within this framework, under entropy maximization
constraints, one does not need all these weights: all the probabilities are identical under the so-called “uniform
random data base model” [244].


Much like their graphical counterparts, the uniform hypergraph models also admit generalizations to cases where
one controls the _degree_ of nodes, i.e., the number of hyperedges incident on each node (see Sec. III A). This lead to
configuration models (CM) for hypergraphs.
A configuration model for _k_ -partite hypergraphs was proposed early in the network science literature, with the
purpose of studying realistic _folksonomies_ (tagging databases) [79]. A related model allowing for node features soon
followed [245].
As for hypergraphs where no _k_ -partite structure is enforced, there are quite a few recent generalizations, developed
mostly with the goal of obtaining null models for community detection purposes. Indeed, one of the best-known


28


community detection methods relies on a so-called “modularity function” [246] to assign a quality to possible decompositions of a network in communities. And in particular, the modularity uses a random null model to determine
whether the number edges found within a community is significant enough to warrant isolating it as a separated
group. In the case of graphs, the most popular baseline is the configuration model, and many models have since
been proposed recently to fulfill the same role in the case of hypergraphs. For example, a recently proposed model
directly generalizes the configuration model of Chung and Lu [247] to the hypergraphical case [83]. In this version of
the model, the number of times a node participates in any given hyperedge is drawn from a multinomial distribution.
This leads to a canonical version where the degrees of nodes are fixed on average. Microcanonical variants are also
analyzed by Chodrow [85], and generalized to the case where the same node can take different roles in different edges
(like broadcaster and receiver, for example), again by Chodrow et al. in [81].

Similar models have also been recently proposed in the statistics literature, where they are used for estimation
purposes [248]. These models are collectively dubbed _β_ -models, and they are treated as generalizations of the _p_ 1
model for graphs [164] (an exponential random graph approach to the configuration model, for directed graphs).
They propose several flavors of the model, all making use of node _propensities_, i.e., of a parameter _βi_ ∈ R to control
how likely it is that node _i_ will be connected to any given hyperedge. In the simplest proposed specification, the
probability of a hypergraph _H_ is given by


_ai_ 1 _,...,ik_ _e_ _[β][i]_ [1] [+] _[...]_ [+] _[β][ik]_
_P_ ( _H_ ∣ _**β**_ ) = ∏ _pi_ 1 _,...,ik_ [(][1][ −] _[p][i]_ [1] _[,...,i]_ _k_ [)][1][−] _[a][i]_ [1] _[,...,ik]_ _pi_ 1 _,...,ik_ = (23)
_i_ 1 _,...,ij_ ∈ _Cn_ ( _k_ ) 1 + _e_ _[β][i]_ [1] [+] _[...]_ [+] _[β][ik]_


where _Cn_ ( _k_ ) is the set of all combinations of _n_ indexes. They also propose a layered and general version where edges
of different sizes co-exist. The common thread shared by all the specifications of the _β_ -model is that, the larger the
parameters _β_, the more likely we are to see the hyperedge _ai_ 1 _,...,ik_ in the final hypergraph _H_ .


The stochastic block model (SBM) is another network model that has been generalized to hypergraph extensively,
motived by the search for random processes able to produce hypergraphs with non-trivial mesoscopic patterns. The
earliest reference to the hypergraphical SBM opts for a natural generalization from the network case [249], by parameterizing the probability of hyperedges of size _k_ with a symmetric tensor _**Q**_ of dimension _k_, whose “rows” correspond
to communities. More precisely, in this SBM the probability that an edge exists between nodes _i_ 1 _,...,ik_ assigned to
communities _σ_ ( _i_ 1) _...σ_ ( _ik_ ) is given by _qσ_ ( _i_ 1) _...σ_ ( _ik_ ) ∈[0 _,_ 1]. The likelihood of a hypergraph _H_ with adjacency tensor _**A**_
is then straightforwardly:


_Bi_ 1 _,...,ik_ _e_ _[β][i]_ [1] [+] _[...]_ [+] _[β][ik]_
_P_ ( _H_ ∣ _**σ**_ ) = _i_ 1 _,...,i_ ∏ _j_ ∈ _Cn_ ( _k_ ) _qσ_ ( _i_ 1) _,...,σ_ ( _ik_ ) [(][1][ −] _[q][σ]_ [(] _[i]_ [1][)] _[,...,σ]_ [(] _[i][k]_ [)][)][1][−] _[a][i]_ [1] _[,...,ik]_ _pi_ 1 _,...,ik_ = 1 + _e_ _[β][i]_ [1] [+] _[...]_ [+] _[β][ik]_ _[,]_ (24)


where _σ_ ( _i_ ) is the index of the block to which node _i_ is assigned. Ke et al. [250] add degree-correction and modify
the probability of the hyperedges _i_ 1 _,...,ik_ is given to _qσ_ ( _i_ 1) _...σ_ ( _ik_ ) ∏ _[m]_ _j_ =1 _[β][i]_ _j_ [where] _[β][i]_ [>] [0] [is] [a] [propensity] [for] [node] _[i]_ [.]
Ahn et al. [251] consider weighted edges parametrized by the communities _σ_ . Finally, Paul et al. [252] combine the
notion of communities with hyperedges of different sizes, albeit in a limited sense: the model conditions the presence
of hyperedges of size 2 (edges) and 3 (triangles) on latent communities _σ_, but does not include interactions at any
higher orders. In all cases, the models are introduced as a benchmark, to test whether partitioning methods—say
spectral methods—can reliably recover the partition _σ_ from hypergraph generated by the model.


A recent approach to hypergraph modeling uses an abstract embedding space to create realistic HOrSs [253],
paralleling similar development in the network context (see Sec.IV A 1 above). The idea is again that if _groups_ of
nodes are close-by in the latent space, then they should tend to be connected. The specific construction considered by
Turnbull et al. [253] embeds nodes randomly in R _[d]_, and adds hyperedges by connecting all set of nodes at a distance
_dij_ < _rℓ_ from one another, for a few random choices of distances _rℓ_ (see Fig. 10). This construction allows the model
to create hyperedges included within others, such as the hyperedges ( _c,e_ ) and ( _c,e,f_ ) in Fig. 10. A last step is added
whereby hyperedges are flipped (non-hyperedges become hyperedges and vice versa) with a small probability _ϵ_ . This
step ensures that the model assigns a non-zero probability to all hypergraphs.


The last model of hypergraphs that we review generalizes the Kronecker model [254], again first introduced in the
context of networks. In the classical model Kronecker graph model, one starts with a small matrix _**P**_ [(][0][)], and repeatedly
takes the Kronecker product of the matrix with itself to generate increasingly large matrices _**P**_ [(][1][)] _,_ _**P**_ [(][2][)] _,...,_ _**P**_ [(] _[f]_ [)] . For


29



Latent space



Latent space



Latent space











































FIG. 10. **Latent** **space** **hypergraphical** **model** **[253].** (A,B) Nodes embedded in R [2], with radii of length _r_ 1 and _r_ 2 - _r_ 1
drawn around them. (C) Hypergraph obtained by connecting sets of nodes mutually at a distance of _dij_ < 2 _r_ 1 and _dij_ < 2 _r_ 2.
Notice the multiple radii allows the model to create the hyperedge { _c, e, f_ }, { _c, e_ } and { _e, f_ }. A model with only one radius
wouldn’t be able to omit { _c, f_ }. Figures adapted from Ref. [253].


example, supposing that _**P**_ [(][0][)] is a 2 × 2 matrix we have:




_[p]_ [12] _**[P]**_ [ (][0][)]
_**P**_ [(][1][)] = _**P**_ [(][0][)] ⊗ _**P**_ [(][0][)] = [ _[p]_ [11] _**[P]**_ [ (][0][)]

_p_ 21 _**P**_ [(][0][)] _p_ 22 _**P**_ [(][0][)][] =]



_p_ 11 _p_ 11 _p_ 11 _p_ 12 _p_ 12 _p_ 11 _p_ 12 _p_ 12
_p_ 11 _p_ 21 _p_ 11 _p_ 22 _p_ 12 _p_ 21 _p_ 12 _p_ 22
_p_ 21 _p_ 11 _p_ 21 _p_ 12 _p_ 22 _p_ 11 _p_ 22 _p_ 12

⎡⎢⎢⎢⎢⎢⎢⎣ _p_ 21 _p_ 21 _p_ 21 _p_ 22 _p_ 22 _p_ 21 _p_ 22 _p_ 22



⎤⎥⎥⎥⎥⎥⎥⎦



(25)



Then, once the matrix attains dimension _n_ × _n_, it is used to generate a graph on _n_ nodes in which edge ( _i,j_ ) exists
with probability _p_ [(] _ij_ _[f]_ [)][.] [The hypergraph generalization, called HyperKron [][255][],] [works essentially in the same way:] [one]
starts with a small _k_ dimensional tensor _**P**_ [(][0][)] and obtains a large final tensor of dimension _k_ and _n_ × _n_ × _.._ × _n_ . One can
then use the tensor to generate a random hypergraph, with hyperedges of size _k_ . The model has found application in
generating large realistic graphs and hypergraph quickly.


_5._ _Simplicial_ _complexes_ _models_


We complete our overview of equilibrium models with approaches formulated in the simplicial complex representation. The theoretical study of models of simplicial complexes is still in its infancy [256]. Save for some early work in
the social sciences [17], the abstract simplicial complex representation has seen little applications until recent years.
As a result, the literature is so far limited, and mostly comes from mathematics and physics.


Before we review these models, a word of warning is in order: many authors blur the line between models of
simplicial complexes and of hypergraphs. Recall that in an abstract simplicial complex, when a _facet_ encodes an
interaction between _k_ nodes, then implied is the existence of the _k_ _faces_ of _k_ - 1 nodes, _k_ ( _k_ - 1) faces of _k_ - 2 nodes,
and so on. This inclusion property means that all models of simplicial complexes are specified in terms of their
distribution over _facets_ (the top-level interactions). Many authors define facets as higher-order interactions, with
no attention to the inclusion property. This omission has no consequence when all interactions have the same size,
but can lead to different results when they do not [102]. In the interest of avoiding confusion, we have modified the
nomenclature favored by the authors where necessary.


The study of random simplicial complexes first started, perhaps unsurprisingly, with generalizations of the Erd˝osR´enyi (ER) model. The earliest model of random simplicial complexes, known as the Linial–Meshulam model, is
arguably the simplest higher-order version of the ER model one can define. In this model, one begins with a connected
graph on _n_ nodes, to which some number _m_ of triangles are added to form facets of 3 nodes [257]. The resulting
object is a prototypical example of the approach favored by mathematical literature in this topic, whose focus is to
find simple random objects with non-trivial _homology_ (see Sec. III D). There has since been many generalization and
analysis of this model, see the survey of Kahle [258] for a summary of recent results. Of particular interest is the
natural generalization in which one begins with a complete simplicial complex of dimension _k_ on _n_ nodes and adds
_k_ + 1 facets at random [259] (with the Linial–Meshulam model recovered by setting _k_ = 1).


30







FIG. 11. **Difference** **between** **(A)** **Cech** **[ˇ]** **and** **(B)** **Vietoris-Rips** **complexes.** Figures adapted from Ref. [265].


A different form of ER-like models of simplicial complexes relies on the idea of _flag_ _complexes_ (also known as clique
complexes). A flag complex is obtained by replacing all the maximal cliques of a graph by a facet. Another equivalent
definition is that a flag complex is completely defined by its 1-skeleton (the underlying graph). In the model analyzed
by Kahle [260], one first creates a classical ER network _G_, and then uses it to generate the associated flag complex.
The construction is related to much earlier work in graph theory [147], where the distribution of cliques in networks
drawn from the ER model was analyzed. However, in the case of Kahle [260], the focus is instead on the homology
and homotopy of the resulting simplicial complexes.


To organize the rapidly growing family of models of random simplicial complexes, a model known as the “∆–
ensemble” has been proposed in by Kahle [258]. In this model, one first connects the pair of nodes of a graph
with probability _p_ 1. Then, all the (edge-only) triangles created in this first step are closed by a face (2-simplex),
independently, with probability _p_ 2. All the empty pyramids created as a result of closing triangles are then replaced
by a 3-dimensional face with probability _p_ 3, and so on. One recovers the classical ER model by setting _p_ 1 = _p_ and
all other _pd_ to 0; the model of Linial–Meshulam by setting _p_ 1 = 1, _p_ 2 = _p_ and all other _pd_ to 0; and the model of
Kahle with _p_ 1 = _p_, _pd_ = 1 for all _d_ - 1. Fowler [261] and Costa and Farber [69] studied the homology of the simplicial
complexes generated by this ensemble independently. A closely related model, also introduced by Costa and Farber

[69], does not define the process recursively. It instead fixes the average number of faces in all dimensions as well as
the number of external faces, i.e., the way in which faces of different dimensions interact. Restricted versions of these
models have been used to generate simplicial complexes on which spreading process occurs [262] (see Sec. VII A), to
predict higher-order interactions in streaming data [116], and to study polymers [263].


The ∆–ensemble is not the only general model able to encompass many models as special cases. Indeed, a different
specification, in the spirit of exponential random graph discussed above, has also been introduced recently by Zuev
et al. [264]. In this model, one defines a series of functions _Qµ_ ( _S_ ) on simplicial complexes for _µ_ = 1 _,..,K_ . These
functions can be, for example, the number of 2-facets, or much more exotic functions, like the number of homological
cycles of some dimension. The _exponential_ _random_ _simplicial_ _complex_ _model_ then assigns a probability


1
_P_ ( _S_ ∣ _**Q**_ _,_ _**λ**_ ) = _Z_ ( _**λ**_ ) = ∑ _e_ [∑] _[µ][ λ][µ][Q][µ]_ [(] _[S]_ [)] (26)
_Z_ ( _**λ**_ ) _[e]_ [∑] _[µ][ λ][µ][Q][µ]_ [(] _[S]_ [)] _S_


to simplicial complex _S_ and where _**λ**_ is a vector of parameters controlling the relative importance of the functions _**Q**_
in the ensemble. Much like the ∆–ensemble, special choices of parameters and function can be made to reproduce
known models like that of Linial–Meshulam, Kahle, or even the ∆–ensemble itself [264].


Another rich line of inquiry focuses on random _geometric_ simplicial complexes. These models build on a long lineage
of work in topological data analysis [96], whose focus is the recovery of topological information, such as the number
of holes in a surface, from noisy objects on geometric objects embedded in space as point clouds.
In these models, one typically first place nodes in some metric space, e.g. R _[d]_, at random by drawing from a random
point process. Then nodes are then connected based on their distance, generating a simplicial complex. There are
two canonical ways in which this last step can be done (see Fig. 11). In random _Cech_ _[ˇ]_ _complexes_ [266], one places a


31


ball of radius _r_ around every node; whenever the intersection of _k_ balls is non-empty, one adds a ( _k_ - 1)-face between
these nodes. In random Vietoris-Rips complexes [256, 266], instead, one connects every node at a distance at most 2 _r_
from one another, and then replace cliques by facets, effectively taking the flag complex of the underlying geometrical
graph. The resulting objects have been studied for their connectivity properties and homological properties, among
other things (see the thorough survey of Bobrowski and Kahle [267] for more details). A fundamental result in this
context concerns the limiting behavior of random geometric complexes. In particular, three regimes exist that display
starkly different properties as a function of the parameter Λ = _nr_ _[d]_, where _n_ is the average number of points in a
ball of radius _r_ in _d_ -dimensional space. The three regimes correspond to different limits for Λ: for vanishing Λ,
the simplicial complexes are sparse, highly disconnected and dust-like; for constant Λ (also called thermodynamic
regime), the homology of the complexes reaches its peak growth; and for diverging Λ, higher homology displays two
phase transitions, one where the homology first appears and a second where it disappears, as cycles are progressively
filled in. Finally, Fasy et al. [268] also found statistical application in the calculation of confidence interval on the
results of persistent homology calculations .


In the physics literature, the focus thus far has been analogs to the configuration model (CM), with the goal of
introducing heterogeneities and realistic properties in the generated random simplicial complexes. By analogy with
the case of graphs, these configuration models fix the degree of nodes, defined as the number of _facets_ incident on
them. All other properties are randomized. Courtney and Bianconi [95] considered a model where every facet is of
size _k_ and the degree of nodes is fixed exactly or on average; Kami´nski et al. [83] have later proposed a hypergraphical
CM that is formally equivalent model to the previous one. A different specification fixes the degrees _exactly_, and lets
the facets have different dimensions while forbidding inclusions [89]. The resulting models have been studied for their
structural properties [95] (like the projected degree or the entropy), and have found application as a null model for the
homology of real systems [89]. A recent approach to random simplicial complex [269, 270] follows the interpretation
of the (classical) configuration model as a random branching tree [16]. In this model of random branching simplicial
complexes [270], one starts with a single edge and attaches _m_ faces of dimension _k_ to each edge of the faces created in
previous iterations. Crucially, _k_ is treated as a random variable such that the dimension of every new face is random,
leading to a simplicial analog to the configuration model. It is introduced to study the percolation properties of the
resulting “simplicial tree.”


**B.** **Out-of-equilibrium** **models**


All of the models we have seen thus far define distributions over static HOrSs. In other words, these models viewed
HOrSs not as dynamical, evolving objects, but instead as static systems, drawn from some fixed distribution. We now
turn to a different approach, mainly developed in the physics and network science literature, that adopts a dynamical
point of view of HOrSs.


Since there are several similarities between many of these out-of-equilibrium models, even across different choices
of representations (see Sec. II), it is worth going over some general notions before we delve in. The modeling goal
motivating these models is almost always the same: finding minimal rule sets such that the typical HOrSs produced
by the model reproduces the structural characteristics of empirically observed bipartite networks [44]. The rules are
often chosen to allow for analytical calculations of properties of interest. But the authors of these model also often
try to find rules that can be motivated mechanistically i.e., that could explain _why_ a HOrSs evolves the way it does

[271].


An overwhelming majority of the out-of-equilibrium models focus on _growing_ systems, in which nodes and edges
are added as time unfolds, but never removed. This is perhaps due to the influence of foundational work in network
science, where growing models were put center stage early on [272]. Hence, with very few exceptions, these outof-equilibrium are _growth_ _models_ . Furthermore, with few exceptions like the activity-driven models [273], time is
measured in discrete steps _t_ = 1 _,_ 2 _,...,T_, where each step is associated with an event. Events typically involve the
creation of a new node, or edge, or both. Echoing work on the preferential attachment model for classical networks

[272], many of the growth events somehow favor existing nodes. As we will see, this is often achieved by selecting the
nodes that receive new edges from a categorical distribution, with probabilities proportional to some growing function
of the degree of the nodes already in the network.


32


_1._ _Bipartite_ _models_


A prototypical example of out-of-equilibrium bipartite model is the model of G. Erg¨un, whose goal was to reproduce
the evolution of sexual contact networks in a heteronormative society [274]. Recall that there are two sets of nodes
(which we have called _A_ and _B_ ) in a bipartite network. The model of Erg¨un [274] postulates that the evolution of
the network can be explained with 3 types of events, occurring with probabilities _p,q_ and _r_ summing to 1. At each
time step, a new node arrives in set _A_ (with probability _p_ ), or in set _B_ (with probability _q_ ); or a new edge appears
between sets _A_ and _B_ (with probability _r_ = 1 - _p_ - _q_ ). To avoid nodes of degree 0, all new incoming nodes are initially
attached to one node in the opposite set, selected at random. Building on the well-known preferential attachment
model [272], all of the choices are made _preferentially_ . That is, whenever one or two nodes must be selected to form
an edge, they are selected with probability proportional to their current degree (plus some offset specific to the set,
called charisma in the original model [274]). Thus, the probability that a node _i_ ∈ _A_ is chosen at time _t_ is calculated
as


_ki_ ( _t_ ) + _cA_
_pi_ ( _t_ ) = (27)
∑ _j_ ∈ _A_ ( _kj_ ( _t_ ) + _cA_ )


where _ki_ ( _t_ ) is the degree of node _i_ at time _t_, and _cA_ is the offset parameter.
Many variations on this theme have since been proposed. For instance, a related—and this time system-agnostic—
model of evolving bipartite networks [44, 45] proceeds by adding new nodes to set _A_ only. Different from the sexual
network model, the degree of the incoming node is chosen from a fixed degree distribution. For each of its _k_ edges, the
new node chooses to attach to an existing node of _B_ m with probability _λ_ ∈[0 _,_ 1], or to a new one. Hence new nodes
appear in set _B_ only through their connection with incoming nodes in set _A_ . Again choices are made preferentially,
using Eq. (27) with _cA_ = 0. Ramasco et al. [275] make use of _two_ distributions instead. After drawing the degree _k_
of the new node in _A_, a second number _ℓ_ ≤ _k_ is drawn from a second distribution, determining the number of target
nodes in _B_ . These nodes are again chosen preferentially, while the _k_ - _ℓ_ remaining degrees are attributed to new nodes
in _B_ . Beguerisse D´ıaz et al. [276] instead consider node sets whose evolution is independent of node creations. In this
case, time is measured in terms of edge creation events, connecting the two sets. Different from the models above, it
mixes the preferential attachment probabilities appearing in Eq. (27) with _uniform_ _attachment_, in which nodes are
chosen uniformly from the node set, i.e.,


1
_pi_ ( _t_ ) = (28)
_N_ ( _t_ )


where _N_ ( _t_ ) is the size of the target set [276].
In all of the models above, the modeling goal is to reproduce the structure of empirically bipartite systems, be it
sexual [274], collaborative [275] or competitive [276]. Connections tend to be concentrated in these human systems,
and preferential probabilities like the one appearing in Eq. (27) are used to induce such a skewed distributions of
degrees [272]. Uniform probabilities like the one appearing in Eq. (28), on the other hand, favor more equitable
distributions, which can also be found in some bipartite systems [44, 276].


Not all out-of-equilibrium models of HOrSs can be modeled with straightforward growth models like the one above.
For instance, in one model [277] that is closer to the literature of self-organized criticality [278], nodes re-arrange
their edges following connection events, and replicate the behavior of nodes to which they are connected. As another
example, a different approach by Friel et al. [279] relies on a dynamical formulation of latent space models, in which
nodes in the two sets _A_ and _B_ move in a latent space, and in which edges and edges / non-edges tend to perpetuate
themselves (Fig. 12).


Other out-of-equilibrium models focus on _rewiring_, a process by which the edges of a bipartite network are reorganized, all the while preserving the node set. For example, Evans [280] start from some configuration where the nodes
in one of the sets _A_ have exactly one neighbor in the other. At each time step, a node in set _A_ is chosen using an
arbitrary selection process, and the edge connecting it to its sole neighbor in _B_ is disconnected. A new target in _B_
is then chosen, again arbitrarily, and a new edge is formed. It turns out that the sequence of generated bipartite
networks can be described exactly at all times [280], and that the model allows for a number of useful generalizations,
including a version of the models where the choices are driven by a superimposed unipartite network or node types

[281]. We note that for some choices of rewiring mechanism, averages over the rewiring process can be thought of
as averages over a static ensemble of bipartite networks, such that these rewiring processes straddle the boundary
between out-of-equilibrium and equilibrium models [149].


33


FIG. 12. **Boards** **and** **directors** **moving** **about** **a** **latent** **space.** Board are represented as large colored dots, going from
2003 in yellow to 2013 in red. Directors are shown as small blue dots. Edges are not shown. Figure reproduced from Ref. [279].


_2._ _Stochastic_ _set_ _models_


A different category of out-of-equilibrium models focuses on how the membership of nodes to sets evolve through
time. There has been relatively little work in this representation, since models that reproduce the evolution of set
memberships are ironically most often couched in the language of bipartite networks [279], hypergraphs [207], or
simplicial complexes [282]. That said, a few models have made explicit use of the set representation, because it turns
out to be a natural choice for higher-order interaction of limited scope, and for two-mode data [19].


These set-based models again build on the observation that the distribution of the number of sets per node and
of the number of nodes per set are often heavy-tailed [44]. Hence, the evolution of these sets can be plausibly
reproduced with a process in which rich-get-richer [2], an observation that has been supported by the empirical
analysis of evolving sets [283]. Zhou et al. [284] harness these observations to create a model of evolving networks
with communities overlain, in which nodes join communities based on their size and create connections with nodes
chosen preferentially in large communities. A simpler model, known as the structural preferential attachment (SPA)
model [285–287], incorporates the rich-get-richer mechanism without any explicit need for a network; it instead
models the evolution of the sets directly. In this particular model, every time step consists of a node joining a set,
with both the node and set being either new or old (such that are 2 × 2 = 4 possible outcomes). The particular
type of event is determined from a categorical distribution, and every choice of nodes and sets is made preferentially
with respect to the set size / membership numbers of the nodes, see Eq. (27). A hierarchical extension of the model
exists [288], where sets themselves belong to larger overlapping sets, and preferential attachment is applied at all levels.


The SPA model is closely related to the Chinese restaurant process [289] and the related Indian Buffet Process[290],
both developed to create distributions over set membership relationships, in the statistics and machine learning
literature. In the Chinese restaurant process, for instance, a new element (node) is created at each time step, and
either join an existing set with probability 1 − 1/( _t_ + 1) or create a new set by itself with probability 1/ _t_ . The specific
set to which the incoming element is attributed is chosen preferentially. The Indian Buffet Process is defined in similar
terms but allows for multiple set memberships. These process have found wide statistical applications because they
satisfy an exchangeability property. Here, exchangeability means that the probability of an observed collection of
sets is independent of the order in which the “growth” events actually occurred. This property greatly simplifies, for
instance, the calculation of expectations over the process.


_3._ _Hypergraphs_ _models_


There has been some work on out-of-equilibrium models of HOrSs in the hypergraph representation as well, mostly
confined to the physics literature. In this literature, the evolving hypergraphs are often called _hypernetworks_, but the
underlying concepts are nonetheless the same.


One of the earliest out-of-equilibrium model of hypergraphs considers the very same type of hypergraphs that were
analyzed in the first _equilibrium_ models of hypergraphs, in the physics literature: _k_ -partite hypergraphs [79], used


34


as models of folksonomies in which users tag items. In the model in question [291], users have intrinsic _activities_,
corresponding to the likelihood that they will be the next user to tag an item. At each time step, one picks a random
user proportionally to this activity, and then decide on both the type of tag to apply and the item to tag. The specific ways in which the choices are implemented allow for a rich-get-richer phenomenon, and the creation of new items.


This particular model is somewhat unique in that most models of evolving hypergraphs focus on more general
hypergraphs that need not be _k_ -partite. Work on these general out-of-equilibrium-models of hypergraph was initiated
by Wang et al. [292], where a prototypical model of growing hypergraphs was proposed. The model takes motivation
in the study of how co-authorship systems evolve (with nodes being authors and hyperedges being papers). In this
model, _k_ new nodes are added at every time step, and they form a hyperedge with precisely 1 node present in the
extant hypergraph, chosen proportional to its degree (the number of hyperedge incident on nodes, see Sec. III A). By
construction, the model generates hypergraphs in which every hyperedge has size _k_ .
There have since been countless variations on these rules, all leading to slightly different models. For instance,
Liu et al. [293] allow the sizes of the hyperedges to vary by specifying these sizes as input (the sequence can be
generated at random or deterministically). Hu et al. explore alternatives where both the size and the composition of
new hyperedges to vary at random [294]. Guang-Yong and Jian-Guo [295] introduce the notion of a “local world,”
by forming the new hyperedges with nodes selected in a small subset of nodes that is itself selected at random. In
Wu et al. [296], choices are not made preferentially but instead proportionally to the “joint degree” of nodes, i.e., the
number of hyperedges they share with the hyperedges that are already in the set. Finally, yet another model uses a
complicated choice function to decide which nodes should be involved in new hyperedges [297], namely


_f_ ( _ki_ ( _t_ ))
_pi_ ( _t_ ) = (29)
∑ _j f_ ( _ki_ ( _t_ ))

where _ki_ ( _t_ ) is the degree of node _i_ at time _t_, and _f_ ( _ki_ ( _t_ )) = ( _ki_ ( _t_ ) + _c_ ) _[γ]_ include both an offset _c_ and a non-linear
exponent _γ_ in the spirit of the classical model of Krapivsky et al. [298]. See also [299] for a version of the function
that allows for node dependent offsets and includes a node-dependent multiplicative term.


Paralleling the bipartite case (see Sec. IV B 1), these models have all been introduced to reproduce some set of characteristics of empirical systems, e.g. collaboration hypergraphs. We note, however, that the analysis of these models
has so far been limited to reproducing the degree distribution of the nodes, with matching numerical simulations.


_4._ _Simplicial_ _complexes_ _models_


The last set of out-of-equilibrium models that we review are specified in the simplicial complex representations.
Similar to the equilibrium models of simplicial complexes, some of these models can be interchangeably thought of as
hypergraphs models, when they do not make use of the inclusion property explicitly. Hence, we have again altered
the nomenclature favored by the authors when most appropriate.
There are a few approaches to dynamical models of simplicial complexes. The first work that uses simplicial
complexes to model hyperbolic network geometry comes from the physics literature, where it is studied under the
name of “Complex Quantum Network Manifolds” [282]. These models are motivated by geometric considerations

[300], the modeling goal being to specify models of how a wide variety of discrete spaces, represented as simplicial
complexes, may arise. The first model in this line of work tracks the evolution of a growing simplicial complex, made
exclusively of triangles [282]. At each step, a new node comes in and forms a triangle with two existing nodes, chosen
uniformly from the set of all connected nodes that have less than _m_ triangles together, where _m_ is called the saturation
bound. At each time step, with probability _p_ ∈[0 _,_ 1], one also closes a triangle, a process that is implemented by
choosing an edge uniformly from the set of unsaturated edges, and choosing an unsaturated edge at random in the
neighborhood of _e_ 1. With this simple model, one can create many quantitatively different outcomes, for example:
planar graphs for low _m_, or complex geometries in the limit _m_ →∞, see Fig. 13.
Many variations on this model followed [301, 302], culminating into a general model of “Network Geometry with
Flavor (NGF)” [70], in which facets have all the same dimension, but are not necessarily triangles anymore. The
existing facets have a latent (quenched) energy _ε_ that is a function of the nodes they connect to, and incoming _k_
facets are connected to an existing _k_ - 1 facet _α_, chosen with probability


_e_ [−] _[βε][α]_ (1 + _snα_ )
_pα_ ( _t_ ) = (30)
∑ _α_ [′] _e_ [−] _[βε][α]_ [′] (1 + _snα_ [′] )


where _s_ ∈{−1 _,_ 0 _,_ 1} is called the flavor of the model, _β_ is a temperature, and _nα_ is a the number of facets incident on
_α_, minus one. The models that precede the NGF model are all special cases of it. For example, the model of Bianconi


35


FIG. 13. **Different** **growing** **geometrical** **networks** **produced** **by** **the** **simple** **model** **of** **Wu** **et** **al.** Parameter _m_ controls
the maximal number of triangle per edges, and _p_ controls closure. Figure reproduced from Ref. [282].


and Rahmede [301] focused on the case of triangles _k_ = 2, with saturation parameter _m_ = 2, flavor _s_ = 0, and facets
that have latent energies. A later model of Bianconi et al. [302] is similar, but focuses on the flavor _s_ = 1.


Some models that have followed borrow much of the mechanisms from the NGF model. For instance, the model of
Courtney and Bianconi [303] functions more or less in the same way, but adds a mechanism to track the evolution of
weights on the simplices, while that of Fountoulakis et al. [304] also works in fixed dimension but is otherwise very
general, introducing the possibility to remove smaller facets when adding new ones.


Other out-of-equilibrium models of simplicial complexes favor approaches that are not related to the NGF model.
For instance, one set of methods [305, 306] by Sizemore et al. favors the flag complex approach that was also used
in the context of equilibrium models by Kahle [260] (see Sec. IV A 5). In these approaches, sequences of growing
graphs are first generated with a series of standard network models, like for example preferential attachment [272].
Then, one takes the flag complexes of these graphs by replacing every clique with a facet, yielding a sequence of
growing simplicial complexes. These models have been used to study the evolution of the topological invariants of
the resulting growing simplicial complexes [305] and their sensitivity to changes in the sequence of events [306].


Another recent—and extremely general—model moves away from the “simplicial-complexes as generalized networks” metaphor, and instead focuses on the properties of the manifold they describe, like their Hausdorff and
spectral dimensions [307]. Many basic mechanisms by which these complex manifold may evolve are explored and
classified.


A different model, introduced by Courtney and Bianconi [308], focuses on _directed_ triangular simplicial complexes.
In this model, the simplices are either created or reinforced by first selecting a source node, proportionally to its
out-strength (the total weight of triangles for which it is the source), with some probability that the node is new.
To determine whether the event leads to the creation of a new simplex or to reinforcement, one then selects an edge
at random in the simplicial complex, and reinforces the weight of the triangle this edge forms with the source, if its
exists, or creates the triangle when it doesn’t. In this case, the modeling goal is to obtain dense simplicial complexes
with scale-free degree distributions.


Finally, there are some models that consider _dynamical_ simplicial complexes—not simplicial complexes that merely
grow. These models are event-based, focusing on what happens in a time slice of a continuous process [309]. The
work of Petri and Barrat [273] is prototypical in this regard. In this model, each node _i_ is endowed with an activity
rate _ai_ drawn from some distribution treated as a parameter of the model. Then, when a node _i_ fires (at rate _ai_ ) in
continuous time, a ( _k_ - 1) − _simplex_ is created with with _k_ - 1 other nodes chosen uniformly at random. The simplex
then disappears after ∆ _t_, a parameter. In this case, the model is introduced to study the structural property of the
generated simplicial complexes like the degrees aggregated over time, as well as and dynamics taking place _on_ the
simplicial complexes generated by this model (see Sec VII).


36


**V.** **DIFFUSION**


In the previous sections we have focused on the structure of higher order interactions. We have introduced higher
order systems (HOrS) and showed their versatility in describing the structural properties of complex systems with
more than pairwise couplings among their components. We will now discuss how the dynamical processes traditionally
defined on networks can be extended to higher order systems. We will start in this section with diffusion, a linear
process that, despite its simplicity, is of high relevance in many different contexts, and also provides an useful first
approximation in the case of nonlinear dynamical systems.
Under the name of diffusion we usually indicate two distinct processes that is important to distinguish. The first
one is the pure (or standard) process of _diffusion_, also known as the “fluid model”, in which the quantity of interest
moves from one region to another following the gradient of concentration. The second one is the so-called _continuous-_
_time_ _random_ _walk_ [310]. Here, we will first discuss these two processes in the context of networks, focusing on their
similarities and differences. We will then show how to implement them on HOrS in Secs. V A and V B, respectively.


In standard diffusion on a network, a (material or immaterial) substance is allocated to the nodes of a graph and
flows over each of its edges from the node with higher concentration to the node with lower concentration [311–313].
The process produces a redistribution of the substance, which finally leads to a state where all the nodes have the same
concentration. This state of the system, which also takes the name of consensus [314], represents a stable equilibrium
of the process, subject to detailed balance condition [315, 316]. If we indicate as _xi_ ( _t_ ), with _i_ = 1 _,_ 2 _,...,N_, the
concentration at the generic vertex _vi_ at time _t_, the time evolution of the network state is governed by the following
system of _N_ coupled linear differential equations:


_x_ ˙ _i_ ( _t_ ) = ∑ _aij_ ( _xj_ ( _t_ ) − _xi_ ( _t_ )) = −∑( _kiδij_          - _aij_ ) _xj_ ( _t_ ) = −∑( _L_ [D] 0 [)] _[ij][x][j]_ [(] _[t]_ [)] (31)
_j_ _j_ _j_


where _A_ = { _aij_ } is the adjacency matrix of the network, which we assume here for simplicity to be a binary and
symmetric matrix (although it is straightforward to extend the formalism to directed and weighted networks), and
_ki_ = ∑ _j aij_ is the degree of node _i_ . In the last equality, we have defined the diffusion Laplacian matrix:



( _L_ [D] 0 [)] _[ij]_ [=]



_ki_ if _i_ = _j_
−1 if _vi_ ∼ _vj_ (32)

⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩0 otherwise



where _vi_ ∼ _vj_ indicates that vertices _vi_ and _vj_ are adjacent. In matricial form, we can write _L_ [D] 0 [=] _[D]_ [ −] _[A]_ [,] [with]
_D_ the diagonal degree matrix. Equation (31) can then be written as _**x**_ ˙ ( _t_ ) = - _L_ [D] 0 _**[x]**_ [(] _[t]_ [)][,] [where] [we] [have] [defined] [the]
concentration vector _**x**_ = ( _x_ 1 _,x_ 2 _,...xN_ ). The fact that the homogeneous solution _**x**_ [(∞)] = **1** ∑ _i xi_ (0)/ _N_ represents a
stationary equilibrium for the process is easily proven by observing that the Laplacian, by definition, is characterized by
having all the rows summing to zero, ∑ _j_ ( _L_ [D] 0 [)] _[ij]_ [=][ 0.] [For] [undirected] [networks,] [characterized] [by] [symmetric] [Laplacian,]
this implies from Eq. (31) that the total concentration ∑ _i xi_ is conserved, and in particular _**x**_ ˙ [(∞)] = 0. The stability of
such equilibrium is governed by the spectral properties of the Laplacian matrix. In fact, the solution of Eq. (31) can
be written by projecting on the Laplacian eigenvectors, which forms a basis in the case of a connected network:


_N_ _N_
_xi_ ( _t_ ) = ∑ _cα_ (0) _e_ [−] _[λ][α][t]_ _φ_ [(] _i_ _[α]_ [)] = _c_ 1(0) _φ_ [(] _i_ [1][)] + ∑ _cα_ (0) _e_ [−] _[λ][α][t]_ _φ_ [(] _i_ _[α]_ [)] (33)
_α_ =1 _α_ =2


where _λα_ and _**φ**_ [(] _[α]_ [)], with _α_ = 1 _,_ 2 _,...N_ are the _α_ -th eigenvalue and eigenvector of _L_ [D] 0 [,] [while] [the] [coefficients] _[c][α]_ [(][0][)]
depend on the initial conditions. We have used the fact that one of the eigenvalues of the Laplacian is zero, because of
the zero-row-sum property, which also implies that the corresponding eigenvector _**φ**_ [(][1][)] is homogeneous. If the network
is connected the zero eigenvalue is unique, and all the other eigenvalues are positive by definition [7]. Hence, we can
see from Eq. (33) that _**x**_ ( _t_ ) will always converge to the homogeneous solution for _t_ →∞, the convergence time being
given by the inverse of the smallest eigenvalue different from zero, _λ_ 2.


A qualitatively different class of processes arises when one considers continuous-time random walk. In this stochastic
process a single walker jumps from one node to one of its neigbours on the network, and cannot divide or distribute
itself over more than one node, as happens in standard diffusion. In this case, we consider various realizations of
the process and we describe the state of the sytem by a vector _**q**_ ( _t_ ), representing the probability for each node to
be occupied by the walker at a given time _t_ . The probability that the walker moves from the generic node _vj_ to _vi_
in one step is given by the ( _i,j_ ) entry of the transition matrix Π = { _πij_ }. In an unbiased random walk this is given


37


by _πij_ = _aij_ / _kj_, representing the fact that the walker on node _vj_ can choose equally among _kj_ neighbors. The time
evolution of the occupation probability is consequently governed by a set of differential equations:


_q_ ˙ _i_ ( _t_ ) = ∑ _πijqj_ ( _t_ ) −∑ _πjiqi_ ( _t_ ) = −∑( _δij_            - _πij_ ) _qj_ ( _t_ ) = −∑( _L_ [RW] 0 ) _ijqj_ ( _t_ ) _._ (34)
_j_ _j_ _j_ _j_


which is similar to that in Eq. (31). The last equality defines the random walk Laplacian _L_ [RW] 0, which is related to
the diffusion Laplacian by _L_ [RW] 0 = _L_ [D] 0 _[D]_ [−][1][,] [and] [for] [this] [reason] [is] [also] [called] _[normalized]_ _[Laplacian]_ [.] [In] [matricial] [form,]
Eq. (34) can be written as _**q**_ ˙( _t_ ) = − _L_ [RW] 0 _**q**_ ( _t_ ).
As well as diffusion, a random walk process is characterized by a stationary distribution where the flows of probability in each direction equal each other, and a detailed balance is reached. In this case the stationary state _**q**_ [(∞)]

corresponds to a probability distribution that is proportional to the degree of nodes: _qi_ [(∞)] = _ki_ /2 _K_, implying that, at
the equilibrium, it is more likely to find the walker on the network hubs. As for standard diffusion, also the dynamics
of a random walk process is intimately related to the spectral properties of its own Laplacian operator. Again, the
stationary state can be found as the Laplacian eigenvector _**φ**_ [(][1][)] associated to the unique (if the network is connected)
eigenvalue 0, which is indeed proportional to the vector of node degrees. The time dependent solution of Eq. (34) can
be written analogously to Eq. (33), and it is thus clear that also in a random walk the velocity at which the stationary
state is reached depends on the second eigenvalue (the smallest eigenvalue different from zero) of _L_ [RW] 0 . Summing up
in both cases of standard diffusion and random walk, the Laplacian matrix encodes the structure of the network and
its spectral properties are related to the dynamical features which ultimately govern the time evolution of the state
vector [317].


When it comes to generalizing diffusive processes to higher order structures, many authors have attempted to extend
the microscopic mechanism known to underlying diffusions in pairwise networks to larger groups of nodes. Importantly,
traditional diffusion is a linear process and consequently the simplest generalization to higher-order structures can
always be reduced to equations involving only pairwise couplings. For instance, as shown by Neuh¨auser et al in [318],
an extension of Eq. (31) to 3-body interactions can be formalized as:


_x_ ˙ _i_ ( _t_ ) = ∑ _a_ [△] _ijk_ [[(] _[x][j]_ [(] _[t]_ [) −] _[x][i]_ [(] _[t]_ [)) + (] _[x][k]_ [(] _[t]_ [) −] _[x][i]_ [(] _[t]_ [))]] (35)
_jk_


where _**A**_ [△] = { _a_ [△] _ijk_ [}] [represents] [a] [tensor] [whose] [entry] [(] _[i,j,k]_ [)] [is] [equal] [to] [1] [only] [if] [there] [is] [a] [triangle] [involving] [the] [three]
nodes _i_, _j_ and _k_ . It is easy to see that Eq. (35) can be rewritten in terms of a new Laplacian matrix _L_ [△] = { _ℓ_ [△] _ij_ [}]
as _x_ ˙ _i_ = −2 ∑ _j ℓ_ [△] _ij_ _[x][j]_ [,] [where] _[ℓ]_ [△] _ij_ [=] _[ δ][ij]_ [ ∑] _[kj]_ _[a]_ [△] _ijk_ [−∑] _[k]_ _[a]_ [△] _ijk_ [.] [The] [system] [in] [Eq.] [(][35][)] [can] [thus] [be] [reduced] [to] [a] [system] [with]
pairwise interactions, where the pairwise interactions are weighted according to the organization of the HOrS under
study.
To see the effects of multi-body coupling we need to insert a non-linearity in the equations, see Sec. VII. There are
many ways in which this can be done. As we have seen in Sec. III E, it is possible to introduce generalized Laplacians
both for diffusion and for random walk. In the next two subsections we will see how such mathematical concepts can
turn useful to talk of diffusion on HOrS, when the role played by the nodes for the network Laplacian is, at higher
orders, played by the edges, the triangles, the tetrahedra, etc.


**A.** **Higher-order** **diffusion**


A simplicial complex can be studied at different orders _k_ ≥ 0, since for each order we can define a _k_ -Laplacian with
its spectrum and consequently its own diffusive dynamics. As a consequence, the same simplicial complex can sustain
different types of diffusion, depending on the order _k_, or in other words, depending on the dimension of the simplices
over which the diffusion is defined. The idea is to indicate as _xσ_ ( _t_ ) the concentration, at time _t_, at the generic simplex
_σ_ of order _k_, and to consider the following set of coupled dynamical equations:


_x_ ˙ _σ_ ( _t_ ) = −∑ ( _L_ [D] _k_ [)] _[σσ]_ [′] _[x][σ]_ [′][(] _[t]_ [)] (36)
_σ_ [′] ∈ _Xk_


where _L_ [D] _k_ [is the combinatorial Laplacian based on the upper and lower matrices of dimension] _[ k]_ [ that we have introduced]
in Sec. III E [68]. Notice that we have _Nk_ of these equations where _Nk_ = ∣ _Xk_ ∣, and _Xk_ represents the set of all simplices
of dimension _k_ in the simplicial complex under study. The system in Eq. (36) generalizes the one in Eq. (31) and
reduces to the latter when _k_ = 0. In this more general setting the substance that is diffusing is not bounded to live


38















where _µα_ and _**φ**_ [(] _[α]_ [)] are respectively the eigenvalues and eigenvectors of the Laplacian _L_ [D] _k_ [.] [The] [authors] [of] [Ref.] [[][68][]]
have estimated how fast the system relaxes to equilibrium. If _**x**_ ( _t_ ) indicates the vector whose _Nk_ entries represent
the concentrations at time _t_ at the _Nk_ simplices of order _k_, the bounds they have found, when the systems is started
at _**x**_ (0), read:


1
∣∣ _L_ [D] _k_ _**[x]**_ [(] _[t]_ [)∣∣≤∣∣] _**[x]**_ [(∞)][ −] _**[x]**_ [(] _[t]_ [)∣∣≤] _[N][k]_ [exp][(−] _[µ]_ [2] _[t]_ [)∣∣] _**[x]**_ [(][0][)∣∣] (38)
_µ_ 2


where _**x**_ [(∞)] = lim _t_ →∞ _**x**_ ( _t_ ), _µ_ 2 is the smallest non-zero eigenvalue of _L_ [D] _k_ [,] [and] [∣∣⋅∣∣] [is] [the] [usual] [Euclidean] [norm.]
Torres and Bianconi [319] have studied Eq. (36) on simplicial complexes generated by the NGF model (see Sec. IV B 4),
and have focused on the spectral (and thus dynamical) differences between different orders _k_ . In particular, they have
generalized to HOrSs the concept of spectral dimension. In a network, the spectral dimension is the dimension of the
network “as seen by a diffusion process” and is defined from the exponent of the power-law scaling of the density _ρ_ ( _µ_ )
of the eigenvalues of the standard Laplacian (the network spectral density) when _µ_ ≪ 1 [320, 321]. Figure 14A shows
that a similar definition can be adopted for HOrSs, and that the spectral dimension of simplicial complexes generated
by the NGF model increases with the order _k_ . Moreover, the authors of Ref. [319] have found an analytical relation
between the spectral density and the return-time probability, reported in Fig. 14B. The latter is defined in HOrSs as
the probability that, starting from an initial state which is localized on a given simplex _σ_, the diffusion process comes
back to the simplex _σ_ at time _t_, averaged over all simplices _σ_ . Such a relation strengthens the link between spectral
dimensions and the dynamical behaviour of high-order diffusion processes on HOrSs.


_1._ _Edge-flows_


The special case _k_ = 1, the so-called edge-based Laplacian, is a particularly important case of the _k_ -th order Laplacian
_L_ _[D]_ _k_ [we have discussed above.] [Edge-flows turn in fact very useful in many contexts, ranging from graph-based machine]
learning to signal analysis.
In graph signal processing, although the basic approach is to consider the signals at the nodes of a graph, an
edge-based approach becomes important when we need to analyze a flow (of mass, energy, information, traffic, etc.).
In such cases, a vertex-based analysis cannot take into account notions like the orientation of flows, which is instead
considered in the edge Laplacian by the sign of the entries. The natural generalization has been studied by Schaub


39


FIG. 15. **Semi-supervised** **learning:** **vertex** **and** **edge** **perspective.** (A) In the standard graph-based semi-supervised
learning, the structure of data points is encoded in a similarity graph, where each node is a data sample and the edges represent
the similarity between pairs of nodes. (B) In the semi-supervised learning for edge-flows proposed in Ref. [322] data points are
instead assigned and inferred on the edges of a graph. Figures reproduced from Ref. [322].


and Segarra, who have used the spectrum of the combinatorial Laplacian _L_ [D] 1 [to] [decompose] [the] [space] [of] [edge-flows]
into harmonic and gradient flows [51]. Within this framework the authors have been able to address the problem
of denoising and smoothing of flow signals by means of a series of filters that enforce approximate flow-conservation
in the processed signals. They also show an application of their methods to denoise vehicular traffic flows in street
networks.
The authors of Ref. [322] have instead considered the problem of semi-supervised learning (SSL) for edge-flows in
networks. Given a graph _G_ ( _V,E_ ) edge-flows are defined by a set of real-valued functions _f_ ∶ _V_ × _V_ → R, such that:


[∀(] _[i,j]_ [) ∈] _[E]_
_f_ ( _i,j_ ) = { [−] _[f]_ [(] _[j,i]_ [)]
0 otherwise.


The authors make use of the edge-Laplacian and focus on divergence-free flows (i.e. cases in which the flow is
approximately conserved) in order to define a process where, given a set of labeled edge-flows it is possible to infer
the unlabeled edge-flows. In particular they study how to select the fraction of most informative edges in order to
accurately infer the remaining ones. Figure 15 illustrates the relation between a vertex-based and the edge-based
SSL. An application of the method to real-world street networks proves its superiority with respect to traditional
alternatives.


**B.** **Higher-order** **random** **walks**


_1._ _Random_ _walks_ _on_ _simplicial_ _complexes_


An example of higher-order random walk in which the walkers populate the edges instead of the nodes has been
proposed by Schaub et al. [134]. The Laplacian _L_ [D] 1 [defined] [in] [Sec.] [III E] [is] [characterized] [by] [positive] [and] [negative]
entries that depend on the edge orientations. Therefore, differently from the standard random walk Laplacian,
the non-diagonal entries do not reflect the transition probabilities among nodes. It is however possible to define a
normalized variant _L_ [RW] 1 of the Laplacian _L_ [D] 1 [which] [can] [be] [related] [to] [an] [edge-based] [random] [walk] [process.] [The] [idea]
is to consider a random walk in a higher dimensional lifted state space. In other words, instead of considering _L_ [D] 1
applied to an edge-flow function _f_ of the co-chain space _C_ [1], Schaub et al. propose a sequence of three operations:
the lifting of _f_ into a higher dimensional space, the action of a linear operator (playing the role fo _L_ [RW] 1 ) and the
projection back down to the original state space. The linear transformation in the lifted space can be normalized
so as to represent a random walk. This procedure allows to interpret the components of the flow in the following
way: the magnitude represents the volume of the flow, while the sign indicates the orientation, which can be aligned
or anti-aligned with the chosen reference orientation. The higher space where the co-chain vector is lifted up has
double the size of _C_ [1] since both possible orientations for each edge are present. The effect of the Laplacian can be
split in two contributions, taking into account connections at the upper and lower order respectively. At each time
step, the walker takes a step via either the upper or the lower adjacency connections, with equal probability. If the
lower connection space is chosen, the walker has probability 1/2 of moving along the reference edge orientation and


40


1/2 of moving against. The transition probability towards a target edge is, in each case, proportional to the upper
degree (or weight) of the edge. If instead the walker makes a step via the upper adjacency connections, there are two
cases: if the edge has no upper adjacent faces, the walker stays at the same edge and can change orientation with
probability 1/2; if instead the edge has upper adjacent faces, then the walker will transition to an upper adjacent
edge with a different orientation with respect to their shared face. In other words, the walker performs a random
walk with adjacency matrix _A_ _[u]_, unless there is no upper adjacent connection, in which case the walker can stay put
or move to the edge with reverse orientation. It is important to observe that the eigenvectors of _L_ [RW] 1 relative to the
eigenvalue _µ_ = 0 are associated to harmonic functions. Schaub et al. propose an application of their random walk
trajectory embedding and simplicial PageRank [134].


A second example of a higher-order random walk in which the walkers live instead on the triangles of a HOrS has
been proposed by Mukherjee et al. [323]. The authors have considered a special case of a simplicial complex where
every edge is contained in at most two triangles. At each time step _t_, a walker at a triangle _σ_ remain still with
probability 1/2, or otherwise move to a triangle on the other side of one of the three edges of _σ_ . In other words, at
each time step, the walker can move to a triangle that is lower adjacent to the current triangle. The transition matrix
Π = { _πσσ_ ′} of the walker reads:



1 _[σ]_ [ =] _[ σ]_ [′]
2 [if]



_πσσ_ ′ =



⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩



1 _[σ]_ [and] _[σ]_ [′] [share] [an] [edge] (39)
6 [if]
0 otherwise _._



and is possible to show that it can be expressed in terms of the higher order Laplacian _L_ [D] 2 [as] [Π][ =] _[ I]_ [ −] _[L]_ [D] 2 [/][6.]


_2._ _Random_ _walks_ _on_ _hypergraphs_


The hypergraph formalism is simple enough to allow to consider random walks on hypergraphs of arbitrarily large
order.
A first basic model of random walk on hypergraphs has been proposed by Zhou et al. [84]. In their implementation,
the walker selects one of the hyperedges of the current node, and then chooses to move to one of the nodes of the
selected hyperedge with a uniform probability. In principle, hyperedges can be weighted according to different criteria.
However, in their numerical experiments the authors adopt the case in which each hyperedge is assigned a weight
equal to 1. Zhou et al. use their random walk model to perform a classification task. They make use of a dataset [324],
in which the animals of a zoo are associated to a set of features (tail, hair, legs and so on), and build a hypergraph
where each animal is a node and two or more nodes are in the same hyperedge if the corresponding animals have a
common feature. The eigenvectors associated to the smallest non-zero eigenvalues _µα_ of the random walk Laplacian
on this hypergraph are then used in order to embed each animal in a two-dimensional Euclidean space. Figures 16A,B
show the classification performance of the method when the 2nd and 3rd smallest eigenvalues, _µ_ 2 and _µ_ 3, or the 3rd
and 4th smallest eigenvalues, are used respectively.


Carletti et al. have instead proposed a random walk model in which the walkers spend more time inside larger
communities [325]. In practice, this is obtained by considering the basic model of Ref [84] and assigning to each
hyperedge a weight that is proportional to its size. In this way, the transition probability reflects the interplay between
the walker’s willing to explore the network and the attractiveness of large hyperedges. The authors of Ref. [325] have
provided an analytical description of the process and of its stationary state. They make use of a different Laplacian
operator suitably defined to generalize the standard random walk, and which reduces to the traditional pairwise
Laplacian when all hyperedges are of size 2 and the hypergraph reduces to a graph. The results obtained for this
random walk on a given hypergraph are compared with those obtained by a traditional random walk on a projected
network, where the hyperedges of the original hypergraph are transformed into cliques. This is illustrated with the
example reported in Fig. 17. The hypergraph in Fig. 17A is composed of one hyperedge of size _k_, where one of
the nodes, denoted as _c_, is also connected to a hub node, _h_, which is at the center of _m_ hyperedges of size 2. The
corresponding projected network is shown in Fig. 17B. The difference between the HOrS and its projection clearly
emerges from the node rankings based on the stationary probability distribution of the walkers in the two cases. In
the case of the projected network, the equilibrium distribution _**q**_ [(∞)] is proportional to the degree of the nodes. This
means that _qh_ [(∞)] ∝ _m_ and _qc_ [(∞)] ∝ _k_, which implies that the hub node _h_ is the top node in the ranking when _m_ - _k_ .
The stationary distribution of the random walk on the hypergraph, denoted as _**p**_ [(∞)], gives instead _ph_ [(∞)] ∼ _m_ and
_p_ [(∞)] _c_ ∼ 1 + ( _k_ - 1) [2] [325]. Consequently, the hub node _h_ results the node with the highest occupation probability only


41





**A** **B** **C**











0











_ϕ_ [(3)]



_ϕ_ [(2)]





FIG. 16. **Classification** **methods** **based** **on** **random** **walks** **on** **hypergraph.** The performance of both Zhou et al. [84]
and Carletti et al. [325] models of random walk on hypergraphs is tested on a classification task performed on a zoo dataset.
Reported are the embeddings of the nodes of the hypergraph in a Euclidean space built from the Laplacian eigenvectors.
Different symbol colors and shapes represent different animal classes. (A,B) Results obtained with eigenvectors corresponding
to the 2nd and 3rd smallest eigenvalues, and the 3rd and 4th smallest eigenvalues respectively, in the model by Zhou at al.
(C) Embedding based the eigenvectors corresponding to the three smallest eigenvalues in the model by Carletti et al. Figures
adapted from Ref. [84] and Ref. [325].


when _m_ - 1 +( _k_ - 1) [2] . In general, at fixed hyperedge order _k_, the two processes provide the same ranking for _m_ < _k_ + 1
or _m_ - 1 +( _k_ - 1) [2] . Conversely, at intermediate values of _m_, the hub _h_ is the top node in the projected network, while
node _c_ is ranking first in the hypergraph. The inversion is graphically shown in Figs. 17C-F. The authors of Ref. [325]
have proposed concrete applications of their random walk model to rank nodes in large systems. For instance they
have produced a ranked list of scientists based on the hypernetwork representing co-authorship relations in published
articles (see Sec. IX A for scientific collaborations as HOrSs) . The same model has also been used for classification
task. Figure 16C shows the three-dimensional embedding (defined by the eigenvectors associated to the first three
eigenvalues) obtained for the zoo data set.


Chitra and Raphael [326] go beyond the previous approaches, and propose a model of random walks on hypergraphs
with edge-dependent vertex weights. Namely, they consider a transition probability assigning different weights even
to nodes belonging to the same hyperedge. In their random walk, a walker at node _vj_ at time _t_ move to a node
_vi_ chosen in the following way. First, a hyperedge _σ_ is selected among all the hyperedges of _vj_ with probability
_ω_ ( _σ_ )/ _d_ ( _vj_ ), where _ω_ ( _σ_ ) is the weight of the hyperedge and and _d_ ( _vj_ ) is the degree of _vj_ . Then a node _vi_ is selected
from hyperedge _σ_ with a probability _γσ_ ( _vi_ )/ _δ_ ( _σ_ ), where _γσ_ ( _vi_ ) is the weight of vertex _vi_ and _δ_ ( _σ_ ) = ∑ _vi_ ∈ _σ γσ_ ( _vi_ ) is
the degree of the hyperedge _σ_ . The novelty of this random walk with respect to previous models on hypergraphs
with edge-independent vertex weights consists in the second step, where the probability is not uniform over all the
vertices of _σ_ . Chitra and Raphael claim that for a random walk on hypergraphs with edge-independent weights is
always possible to find a choice of edge weights such that the process on the hypergraph is equivalent to a traditional
random walk on the corresponding projected network with such chosen weights. The proof of equivalence is based
on the time-reversibility of the process, which is a typical property of the associated Markov chain. Such property
cannot be extended to hypergraphs with edge-dependent weights, which happen to be not time-reversible. Therefore,
random walks on hypergraphs with edge-dependent vertex weights cannot be reduced to traditional random walks on
weighted networks. This generalizes a result already found in [327] for _k_ -uniform hypergraphs.
Notice that, without using edge-dependent weights, another way to obtain a higher order random walk which is not
reducible to the traditional model is, similarly to what happens for diffusion, to insert a non-linearity in the equations,
as it has been done by Chan et al. [77], and by Li and Milenkovic in [328], and [140].
In the model by Chitra and Raphael the stationary state _**p**_ [(∞)], can be analytically computed. If for the traditional
processes this can be written as by _p_ [(∞)] _i_ = _ρ_ ∑ _σ_ ∈ _E_ ( _vi_ ) _ω_ ( _σ_ ), with _E_ ( _vi_ ) the set of hyperedges containing _vi_, the process

proposed by Chitra and Raphael brings to _p_ [(∞)] _i_ = ∑ _σ_ ∈ _E_ ( _vi_ ) _ρσω_ ( _σ_ ) _γσ_ ( _vi_ ), i.e. the proportionality constant _ρ_ depends
on the hyperedge and each term in the sum is multiplied by the vertex weight.
By making use of this definition the authors also provide an application example, again based on scientific collaborations. They obtain the ranking of different scientists according to a hypergraph where hyperedges represent articles and


42


FIG. 17. **Example** **of** **random** **walk** **on** **hypergraphs.** (A) An hypergraph with _m_ = 7 hyperedges of size _k_ = 2 and one
hyperedge of size _k_ = 6, and (B) its corresponding projected network. (C) Probability of finding the walker on node _h_ (circles)
and _c_ (squares) for a random walk on the hypergraph (red) and on the projected network (green), and for different size _m_ of
the hub. Figure reproduced from Ref. [325].


the authors have weights which reflect their appearance order (first/last or middle authors), and they compare such
ranking to that obtained by a random walk on the corresponding edge-independent hypergraph. Other applications of
edge-dependent hypergraphs include e-commerce [329], text ranking [87], image visualisation and processing [330–334].


Random walks on hypergraphs have also been used to study graph expansion. Louis in [76] introduces a nonlinear Laplacian operator on hypergraphs as a generalization of the random walk Laplacian operator on graphs and
studies its spectrum. He in particular proves that the second smallest eigenvalue is related to the expansion of the
hypergraph, generalizing the Cheeger’s inequality. A similar process is analysed by Chan et al [335] considering a
diffusive flow from the node with maximum density to the one with minimum density within a hyperedge. The two
works are merged together in [77]. A generalization of this process is provided in [78], while in [336] the framework
is extended to directed hypergraphs. Li and Milenkovic [140] answer the same questions on a different kind of higher
order network, named submodular hypergraph, for which they define a different Laplacian and analyze its spectrum.


Higher order random walks have also been used for applications such as node ranking [87], community structure
detection [337], topological data analysis [338], machine learning [339, 340], and even quantum walks have been
extended beyond pairwise connections [341]. The traditional definition of cover time in random walk, i.e. the
maximum expected time to visit all the vertices of a graph, has been extended to hypergraphs in [342]. While Avin
et al. [88] define a higher-order random walk suitably designed to describe communication over a wireless shared
channel, which is not well captured by a traditional network.


Finally, another interesting extension would be to consider reaction-diffusion systems based simplicial complexes or
hypergraphs, which historically represent the basic processes for pattern formation [343–346]. For instance, higherorder interactions have been considered in [347], where the cumulative response of nodes to a specific signal is
investigated by means of the flow patterns stemming from the interplay between topology and dynamics in a coupled
reaction system.


43


**VI.** **SYNCHRONIZATION**


Synchronization is the emergence of order in populations of two or more coupled dynamical systems. It shows
up in many physical, biological and social systems, and at different scales, with typical examples including the
synchronized motion of weakly coupled pendulum clocks [348], the clapping of an audience [349] or the flashing of
fireflies [350]. Synchronization has been an active research topic in the last decades with successful applications
ranging from neuroscience to climatology and engineering [351–354]. Interactions play a key role in the emergence of
synchronization, which is why network science provides natural and powerful tools to inquire about the nature and
the underlying mechanisms of synchronization. In synchronization on networks, each node of a graph is a dynamical
system, and its dynamics is influenced by its neighbours through pairwise interactions. Synchronization occurs when
the interactions are such that all, or a macroscopic fraction of, the oscillators reach a coherent state. Historically,
this was made clear by Kuramoto and his mathematically tractable model of all-to-all coupled phase oscillators [355].
The Kuramoto model paved the way for others to study the effects of complex topologies [356–358]. Key results have
shed light on the relationship between network synchronizability and topology, e.g. the improved synchronizability of
small-world networks [359], and have revealed different routes to synchronization, such as abrupt synchronization in
scale-free networks [360, 361]. In addition, different types of synchronized behaviors have been identified and linked to
specific properties of the network structure, including remote synchronization [362], cluster states [363], chimera [364]
and Bellerophon [365] states. The existence and properties of these phenomena depend on the type of interactions,
but also on the topology of the network. See Refs. [354, 357, 358] for comprehensive reviews.
In this Section, we discuss how coupled dynamical systems can be extended to higher-order systems (HOrSs),
and how the presence of high-order interactions can affect synchronization in both phase oscillators and nonlinear
dynamical systems. As we will show below, higher-order interactions can change the nature of the transition to
synchronization, can favor the emergence of certain collective phenomena, e.g. cluster states, and can even give rise
to new dynamical regimes.


**A.** **Phase** **oscillators**


In this section, we report on studies that investigate synchronization in populations of phase oscillators: the most
basic oscillatory unit which is fully described by a phase.


_1._ _Higher-order_ _Kuramoto_ _model_


The Kuramoto model captures the essence of the emergence of synchronization in a mathematically tractable
setting [355]. In the original model, the state of oscillator _i_ ( _i_ = 1 _,...,N_ ) at time _t_ is described by its phase
_θi_ ( _t_ ) ∈[0 _,_ 2 _π_ [. The dynamics of each oscillator is governed by its interactions with all other oscillators (all-to-all
interactions) according to:



_θ_ ˙ _i_ = _ωi_ + _[K]_ [1]

_N_



_N_
∑ sin( _θj_ - _θi_ ) _,_ (40)
_j_ =1



where _ωi_ denotes the natural frequency associated to _i_, drawn from a given distribution _g_ ( _ω_ ), and _K_ 1 - 0 is the
(pairwise) coupling constant. In this model, two opposing driving forces are at play: heterogeneity in the natural
frequencies pushes the oscillators away from synchronization, while interactions favor synchronization. As a result
of this, we observe a phase transition. Above a critical value, _K_ 1 [∗][,] [of] [the] [coupling] [strength,] [the] [oscillators] [syn-]
chronize their frequency, so that their phase difference does not change in time (this is known as phase locking).
This phase transition from incoherence to synchronization can be captured by the usual complex order parameter
1
_Z_ 1( _t_ ) = _R_ 1( _t_ ) _e_ _[i]_ [Φ][1][(] _[t]_ [)] = _N_ [∑] _j_ _[N]_ =1 _[e][iθ][j]_ [(] _[t]_ [)][,] [a] [macroscopic] [quantity] [that] [characterizes] [the] [collective] [dynamics] [of] [the] [entire]
system. The modulus 0 ≤ _R_ 1( _t_ ) ≤ 1 measures the phase coherence, while 0 ≤ Φ( _t_ ) < 2 _π_ is the average phase of
the whole population of oscillators. When _K_ 1 < _K_ 1 [∗][,] [the] [oscillators] [behave] [incoherently] [and] _[R]_ [1] [≈] [0.] [When] _[K]_ [1] [is]
above the critical value, instead, the oscillators synchronize and _R_ 1 ≠ 0. As _K_ 1 tends to large values, _R_ 1 tends to 1,
corresponding to all oscillators having exactly identical phases, a case that can be obtained for identical oscillators,
i.e. when _ωi_ = _ω_ ∀ _i_ [366, 367]. To make the driving of the mean field explicit, the system in Eq. (40) can be rewritten
as:


_θ_ ˙ _i_ = _ωi_ + _K_ 1 _R_ 1 sin(Φ1 − _θi_ ) _._ (41)


44


**Motif**


**#** **links** 4 5 6

_K_ ˜ 1 0.22 0.18 0.14


FIG. 18. **Critical** **coupling** **and** **motifs.** In motifs, i.e. small graphs recurrent in various biological, social and technological
networks, the critical coupling strength _K_ [˜] 1 for synchronization decreases as the number of links increases. Figure adapted from
Ref. [369].


About ten years ago, Ott and Antonsen proved that the dynamics of the system in Eq. (41) reduces to a stable
low-dimensional synchronization manifold, by applying self-consistency arguments to the evolution of the distribution
of the oscillator phases [368].
The Kuramoto model can be extended from the original all-to-all interactions to the case in which the oscillators are
the nodes of a network and their couplings are governed by the adjacency matrix _A_ = { _aij_ } of the network. Formally,
this is equivalent to consider the equations:



_θ_ ˙ _i_ = _ωi_ + _[K]_ [1]

_N_



_N_
∑ _aij_ sin( _θj_ - _θi_ ) _._ (42)
_j_ =1



The Kuramoto model has been studied on different types of complex networks, and particular attention has been
devoted to investigate how the structural properties of a network affect synchronization. A review of the main results
obtained can be found in Refs. [356, 357]. In what follows, we will review more recent works that extend the Kuramoto
model to higher-order networks, starting with a short detour on synchronization on motifs.


Motifs are small graphs that appear in a statistically significant way in real networks [53]. This is why studying
synchronization in motifs can help understanding the dynamics of large networks and is also the first step towards an
explicit treatment of synchronization in a HOrS.
A first study by Moreno et al. [369] investigated if some motifs of Kuramoto oscillators are more synchronizable than
others. For each undirected small graph of _N_ = 3 and 4 nodes, the authors evaluated its probability to synchronize
by considering many random realizations of the set of natural frequencies { _ωi_ } _[N]_ _i_ =1 [drawn] [from] [a] [given] [distribution]
_g_ ( _w_ ), and computing the fraction of realizations for which the graph synchronizes. As expected, the probability
of synchronization increases with the coupling strength _K_ 1. Additionally, they have evaluated a threshold coupling
strength _K_ [˜] 1, as the value of _K_ 1 above which the probability of synchronization is greater than 0.5. The main result of
the study is that, at fixed number of nodes, the larger the number of links is, the lower the value of _K_ [˜] 1, i.e. the easier
it is for the graph to synchronize. This is shown in Fig. 18 for graphs with four nodes. The authors suggest this could
help understand why some motifs, which appear in biological networks and are more conserved across evolution, have
a higher link density than others.
In a following study, D’Huys et al. have investigated the influence of time delays in the synchronization of motifs [370]. The authors studied the existence and stability of several types of synchronized behaviors, in unidirectionally
and bidirectionally coupled small rings, pairs of oscillators, and open chains. The work showed that delays tend to
induce multistability in unidirectional rings, in contrast to what happens in bidirectional rings.


More recent works have studied variations of the Kuramoto model that explicitly include higher-order interactions.
Skardal and Arenas [371] have investigated what happens when all-to-all pairwise interactions are replaced by pure
three-body interactions, considering the system:



_N_
∑ sin( _θj_ + _θk_ - 2 _θi_ ) _,_ (43)
_k_ =1



_θ_ ˙ _i_ = _ωi_ + _[K]_ [2]

_N_ [2]



_N_

∑
_j_ =1



which is a direct generalization of the original Kuramoto model in Eq. (40). Now, the dynamics is ruled by interactions
of all possible triplets of oscillators ( _i,j,k_ ) in the system (corresponding to a hypergraph with all 3-node hyperedges).
The value of the coupling strength _K_ 2 tunes the strength of such interactions. Notice that the number of three-body
interactions node _i_ is involved in, scales as _N_ [2], which explains the presence of the normalization factor 1/ _N_ [2] to ensure
a smooth thermodynamic limit. The system in Eq. (43) can be cast into the following form:


_θ_ ˙ _i_ = _ωi_ + _K_ 2 _R_ 1 [2] [sin][[][2][(][Φ][1] [−] _[θ][i]_ [)]] _[,]_ (44)


45


FIG. 19. **Abrupt** **desynchronization** **induced** **by** **higher-order** **interactions** **in** **the** **model** **in** **Eq.** (43) **.** The two order
parameters _R_ 1 and _R_ 2 are shown as a function of the three-body coupling strength _K_ 2, in (A) and (B) respectively. The
system exhibits multistability, and each stable branch represents a two-cluster state with a proportion of _η_ oscillators in the
first cluster. Figures adapted from Ref. [371].


where _R_ 1( _t_ ) and Φ1( _t_ ) are, as in Eq. (41), the modulus and the phase of the complex order parameter _Z_ 1( _t_ ). By
arguments of continuity and self-consistency of the oscillator density, the authors then derived analytical formulae
1
for the dynamics of _Z_ ( _t_ ) and of a second order parameter _Z_ 2( _t_ ) = _R_ 2( _t_ ) _e_ _[i]_ [Φ][2][(] _[t]_ [)] = _N_ [∑] _j_ _[N]_ =1 _[e][i]_ [2] _[θ][j]_ [(] _[t]_ [)][,] [which] [is] [a] [typical]
indicator of 2-cluster states. Indeed, _R_ 2 ≈ 0 for incoherent states, while _R_ 2 ≈ 1 for 2-cluster states when the two clusters
have a phase difference equal to _π_ . Two main novel dynamical phenomena were identified. Firstly, the three-body
interactions give rise to an abrupt desynchronization transition, which is not present in the classical Kuramoto model
of Eq. (40). In other words, as shown in Fig. 19, as the coupling strength _K_ 2 is decreased from large values, the order
parameter _R_ 1 drops from positive values to zero. On the other hand, increasing _K_ 2 back does not yield a transition
to coherence since the incoherent state is stable for any coupling strength. Second, the three-body interactions yield
multistability: for large enough values of the coupling strength _K_ 2, there exist infinitely many stable coherent branches
that correspond to 2-cluster solutions. Each of these stable 2-cluster solutions can be distinguished by the relative
size _η_ of the two clusters, i.e. the relative number of oscillators in the two clusters. Interestingly, each of the stable
branches undergoes an abrupt desynchronization transition at a different value of _K_ 2, so that there is actually a
continuum of transitions. Very recently, Xu and coworkers have studied the same system using bifurcation theory and
the symmetries of the _SO_ 2 group to reveal scaling properties of the transitions [372]. The authors show that their
analysis generalizes to a coupling scheme where natural frequencies are correlated to the coupling strength.
That higher-order interactions favor multistability is a general trend, and this is also in agreement with the results
of some earlier studies [373–375]. Already in 2015, Komarov and Pikovsky [375] studied Eq. (43) in great detail for
identical and distributed frequencies, with or without common noise. The main focus of their study is different to
Ref. [371]: here, the authors show that while the incoherent state _R_ 1 = 0 is always stable in the thermodynamic
limit, finite-size fluctuations can induce a transition to synchrony ~~√~~ 0 < _R_ 1 ≤ 1. The authors explained this transition
by showing that, remarkably, the order parameter scales as _R_ 1 ∼ _N_ with the size of the system, which vanishes in

the thermodynamic limit. Even earlier, in 2011, motivated by the importance of many-body interactions in signal
transmission between neurons, Tanaka and Ayogi [373] studied a system similar to the one in Eq. (43). They have
considered a coupling function of the form sin( _θj_ - _θi_ ) cos( _θk_ - _θi_ ), which indeed corresponds to the first of the two
terms to which the original coupling function in Eq. (43) reduces when using the trigonometric identity for the sine of
a sum [373]. As shown in Fig. 20A, the model exhibits multistability similar to that in Fig. 19. Additionally, Tanaka
and Ayogi have studied the effect of having, at the same time, both all 2- and all 3-body interactions, with respective
coupling strength _K_ 1 and _K_ 2:



_N_

∑
_j_ =1



_N_
∑ sin( _θj_ - _θi_ ) cos( _θk_ - _θi_ ) _._ (45)
_k_ =1



_θ_ ˙ _i_ = _ωi_ + _[K]_ [1]

_N_



_N_
∑ sin( _θj_ - _θi_ ) + [2] _[K]_ [2]
_j_ =1 _N_ [2]



In our language this means considering all possible 2-simplices. The phase diagram of this more general model is
reported in Fig. 20B and shows the existence of different regimes, many of them exhibiting multiple coexisting stable
states. For example, in the region indicated as “Bistable”, both the incoherent state with _R_ ≈ 0 and the synchronized
state with _R_ ≈ 1 are stable.
In a second study, Skardal and Arenas added two layers of complexity to the previous models: ( _i_ ) a combination
of interactions of different orders up to four-body interactions,( _ii_ ) a microscopic description of such interactions in


46


FIG. 20. **Phase** **diagrams** **of** **the** **model** **with** **higher-order** **interactions** **in** **Eq.** (45) **.** (A) Case _K_ 1 = 0 when only
three-body interactions are present. (B) General case with both two- and three-body interactions. Vertical black lines represent
the interval [0 _,_ 1] of values the order parameter _R_ 1 can take. On these lines, black circles and boxes represent the value of _R_ 1
for all coexisting stable states. Figures adapted from Ref. [373].


the form of a simplicial complex [376]. They showed numerically that higher-order interactions were sufficient to
induce an explosive transition from incoherence to synchronization in a real-world higher-order system. In practice,
they have used a Macaque brain data set with 248 nodes and pairwise connections in which any 3-node clique was
promoted into a 2-simplex, and any 4-node clique into a 3-simplex. We refer to simplicial complexes constructed this
way as “maximal”, because from _aij_ all possible _q_ -simplices are constructed. A maximal simplicial complex cannot
thus have, e.g. any empty triangle (three 1-simplices), but only filled triangles (three 1-simplices and one 2-simplex).
The resulting network has 1-, 2-, and 3-simplex interactions, with the 2-simplex interactions term for oscillator _θi_
written as



_N_
∑ _aijk_ sin(2 _θj_ - _θk_ - _θi_ ) _,_ (46)
_k_ =1



_K_ 2
2!⟨ _k_ [(][2][)] ⟩



_N_

∑
_j_ =1



and where the 1- and 3-simplex interaction terms have similar structure. Note the choice of an asymmetrical coupling
function in Eq. (46) which is different from the symmetrical choice in Eq. (43). This will be discussed in more details
in the next paragraph. Here, _**A**_ = { _aijk_ } denotes the 2-simplex interaction tensor with _bijk_ equal to 1 if there is
a three-body interaction among oscillators _i_, _j_ and _k_, and 0 otherwise. The ⟨ _k_ [(][2][)] ⟩ represents the average degree of
2-simplex degree, i.e. the average number of distinct 2-simplices nodes are part of. In general, the average _q_ -simplex
degree is written ⟨ _k_ [(] _[q]_ [)] ⟩, and the coupling coefficient _Kq_ is rescaled by _q_ !⟨ _k_ [(] _[q]_ [)] ⟩. The complexity of the model makes it
hardly tractable analytically. However, by means of self-consistency arguments similar to those used in Ref. [371], the
authors were able to obtain a closed equation for the order parameter _R_ 1 in a simplified all-to-all version of the model.
They obtained the bifurcation diagram reported in Fig. 21, which shows the following two main findings. Firstly,
higher-order interaction are able to induce an abrupt transition from incoherence to synchronization. Indeed, above
a critical value of _K_ 2+3 = _K_ 2 + _K_ 3 = 2, the system becomes bistable and exhibits a hysteresis cycle, yielding abrupt
transitions. Since the incoherent and synchronized states have been linked to resting and active states, respectively,
such abrupt transitions provide a potential mechanism for fast switching between brain states. Second, strong enough
higher-order interactions (large enough values of _K_ 2+3) can stabilise the synchronized state even when the 1-simplex
interactions are repulsive, i.e. when _K_ 1 < 0. Notice that explosive synchronization was first observed in global coupling
with evenly spaced frenquencies [377] and then in scale-free networks with frequency-degree correlations [360]. Several
other structural or dynamical ingredients have then been identified that can also lead to explosive synchronization,
such as multilayer couplings [378] or time delays [379]. Here, Skardal and Arenas have been able to show that higherorder interactions are sufficient to induce explosive synchronization. Explosive synchronization and chimera states
have also been studied in simplicial complexes by Berec in Refs. [380, 381].
The choice of coupling function is known to affect the dynamics of coupled dynamical systems [382]. In coupled
oscillators, a typical choice at order 1 is the sinusoidal function sin( _θj_ - _θi_ ) that vanishes when oscillators are synchronized and that is 2 _π_ -periodic in its phases, as in the Kuramoto model of Eq. (40). For interactions of more
than two oscillators, however, there are more choices of functions that satisfy those requirements. Indeed, even if we
restrict ourselves to the simplest case, i.e. 2 _π_ -periodic sinusoids with no harmonics and no phase-shift, we are faced
with two possibilities for the functional form accounting for three-body interactions in the equation for oscillator _i_,
namely sin( _θj_ + _θk_ - 2 _θi_ ), or sin(2 _θj_ - _θk_ - _θi_ ). The first choice was used for example in Eq. (43). This function is
the natural generalization of the pairwise function above, in that it is symmetric in _i_, meaning that it is invariant
under any permutation of the other indices. This choice was also made in Ref. [141] where it was generalized to all


47


FIG. 21. **Phase** **diagrams** **of** **the** **simplicial** **complex** **oscillator** **model** **of** **Ref.** **[376].** (A) Higher-order interactions
induce abrupt transitions between incoherence and synchronization. (B) Moreover, higher-order interactions can stabilise the
synchronized state, even when pairwise (1-simplex) interactions are repulsive ( _K_ 1 < 0). (C) Two-parameter bifurcation diagram
identifying the region of bistability. Analytical predictions (solid curves) are in agreement with the numerical simulations (open
circles). Figures adapted from Ref. [376].


possible orders. The second choice, which was used for example in Eq. (46), is asymmetric, in the sense described
above. It can, however, arise naturally from the phase reduction of nonlinear oscillators, see for example Eq. (52)
and Refs. [383]. For coupling functions of larger numbers of oscillators, there is always one symmetric choice, but the
number of asymmetric choices increases. However, to the best of our knowledge, the implications of the precise choice
of higher-order coupling functions on the dynamics have not been investigated systematically as deserved so far. We
hope this review will encourage works in this direction.
A radically different approach from those discussed above has been proposed by Mill´an et al., who have formulated
a higher-order extension of the Kuramoto model in which the oscillators are placed not only on the nodes but also on
the higher-order simplices, such as the links or the triangles, of a simplicial complex [384]. The authors showed that
the dynamics defined on _q_ -simplices can be projected, through Hodge decomposition (also see Sec. III E 2), on the
dynamics defined on ( _q_ −1) and ( _q_ +1) dimensional simplices. This means, for instance, that the dynamics on edges can
be projected on nodes and triangles. Interestingly, when the two projected dynamics on ( _q_ - 1)- and ( _q_ + 1)-simplices
are adaptively coupled the transition to synchronization is explosive, while it is continuous in the uncoupled case.
This implies for instance that a dynamics defined on links can induce a simultaneous explosive synchronization on
the dynamics projected on nodes and triangles. The phenomenon is illustrated in Fig. 22, which reports the results
of numerical simulations on a simplicial complex generated by a configuration model (see Sec. IV).


The three authors of Ref. [384] have also studied synchronization in so-called Complex Network Manifolds (CNMs),
which are growing simplicial complexes of dimension _d_, i.e. built with _d_ -simplices [321, 385] (see Section IV B 4).
Note that simplicial complexes were only used here to construct the adjacency matrix { _aij_ } of networks with an easily
tunable spectral dimension, in addition to being small-world and having a highly modular structure. Indeed the goal
of these studies was to study the effect of the spectral dimension of the underlying graph on network synchronization.
The spectral dimension of a graph describes the power-law scaling of the eigenvalue density of the standard Laplacian
_L_ . Most complex networks have a spectral gap, i.e. the second eigenvalue _λ_ 2 of the standard Laplacian _L_ does not tend
to zero as the size of the network is increased. In CNMs, however, _λ_ 2 does tend to zero, so that a spectral dimension
_dS_ of the network can be defined. Remarkably, in CNMs, the eigenvalue density scales roughly with the dimension _d_
of the simplicial complex, _dS_ ≃ _d_ . Hence, one can investigate the effect of _dS_ just by changing the dimension of the
simplicial complex used to construct the network. In [385], the authors have reported the observation of frustrated
synchronization, a dynamical regime in which the order parameter is non-stationary and exhibits large fluctuations
even at large times. In [321], they have further shown via a linear approximation that the synchronized state is
thermodynamically stable only in networks with _dS_ - 4. In other words, for smaller spectral dimensions, the average


48


FIG. 22. **Explosive** **synchronization** **in** **the** **higher-order** **Kuramoto** **model.** In Ref. [384], the oscillators are associated
not to the nodes, but to the _q_ -simplices (with _q_ ≥ 1) of a simplicial complex. _R_ [[+]] and _R_ [[−]] denote the order parameter of the
dynamics projected on ( _q_ - 1)- and ( _q_ + 1)-simplices, respectively shown in (A) and (B). The model has been implemented on
simplicial complexes constructed by a configuration model (see Sec. IV). When the projections are uncoupled the transition is
continuous, while when the projections are adaptively coupled, the transition is explosive. Figures adapted from Ref. [384].


fluctuations of the phases diverge as the network size _N_ →∞. Hence, frustrated synchronization is only possible for
_dS_ < 4. Additionally, _dS_ - 4 is a necessary condition for a stable synchronized state in the thermodynamic limit, as
also confirmed numerically.


Higher-order interactions can yield interesting dynamics even when the oscillators have identical frequencies, as
shown by two very recent studies [141, 386].
In the first of these works [386], Gong and Pikovsky have considered the following sytem of all-to-all coupled oscillators
with identical frequencies and higher-order harmonics:


_θi_ = _ω_ ( _t_ ) + Im[ _H_ ( _t_ ) _e_ [−] _[iqθ][j]_ ] _,_ (47)


with pure harmonics of order _q_ ≥ 2. The quantity _H_ ( _t_ ) in the equations represents the coupling and depends on
1
the generalized complex order parameters _Zq_ ( _t_ ) = _Rq_ ( _t_ ) _e_ _[i]_ [Φ] _[q]_ [(] _[t]_ [)] = _N_ [∑] _j_ _[N]_ =1 _[e][iqθ][j]_ [(] _[t]_ [)][.] [The] [model] [reduces] [to] [the] [original]
Kuramoto model in Eq. (40) when _H_ = _Z_ 1 and only the first harmonic _q_ = 1 is considered. With _H_ = _Z_ 2 and only
the second order harmonic _q_ = 2, one obtains a coupling function of the type sin(2( _θj_ - _θi_ )). This does not imply
higher-order interactions, which can instead be obtained by considering nonlinear meanfield couplings, i.e. powers of
_Zq_ . For example, by taking _H_ = _Z_ 1 [2] [and] _[q]_ [ =][ 2,] [one] [recovers] [the] [system] [in] [Eq.] [(][43][)] [with] [pure] [three-body] [interactions.]
Higher-order harmonics and higher-order interactions are linked in that they both allow _q_ -cluster states at order _q_,
for example. Equation (44) can also be seen as driven by the meanfield with a second order harmonic.
In their work, the authors extend the Watanabe-Strogatz theory to account for any pure higher-order _harmonics_,
_q_ ≥ 2, for a general form of _H_ that can include higher-order interactions. The Watanabe-Strogatz theory provides
a lower-dimensional description of all-to-all coupled oscillators with identical frequencies [366, 367], similarly to the
Ott-Antonsen theory for distributed frequencies [368]. As an example, Gong and Pikovsky have applied their theory
to the cases of pure 3-body and pure 5-body interactions, and have been able to study the basin of attractions of the 3and 5-cluster states, respectively. It is worth mentioning here three other earlier but related studies by Pikovsky and
coworkers [387–389]. In Refs. [387, 388], had already considered the effect of nonlinear mean field coupling, i.e. where
_H_ is a function of powers of _Z_ 1, as opposed to only the first power as in the Kuramoto model (40). The authors found
that this additional nonlinearity yields richer dynamics, including self-organized quasiperiodic behavior. Similarly, in
Ref. [389], the authors consider coupling functions that depend nonlinearly on _R_ 1.


In the second of these works [141], Lucas et al. have focused directly on higher-order interactions rather than
harmonics, and proposed a natural generalization of the usual Laplacian formalism to account for complex topologies
(instead of all-to-all) and with a mix of orders. They introduced a multi-order Laplacian and applied it to simplicial
complexes (though the formalism is valid for hypergraphs in general) of identical phase oscillators. This Laplacian
allows to assess the stability of the fully synchronized state _θi_ ( _t_ ) = _θ_ _[S]_ ( _t_ ) = _ωt_ for all _i_ . Formally, the authors considered


the following system:



_N_
∑ _aijk_ sin( _θj_ + _θk_ - 2 _θi_ )
_j,k_ =1



49


(48)



_θ_ ˙ _i_ = _ω_ + _K_ 1
⟨ _k_ [(][1][)] ⟩



_N_ _K_ 2
∑ _aij_ sin( _θj_ - _θi_ ) +
_j_ =1 2!⟨ _k_ [(][2][)] ⟩



_K_ 3
+
3!⟨ _k_ [(][3][)] ⟩



_N_
∑ _aijkl_ sin( _θj_ + _θk_ + _θl_ - 3 _θi_ ) + _..._
_j,k,l_ =1



_q_ max+1
∑ _θjm_ - _q_ max _θi_ ) _,_
_m_ =2



_Kq_ max
+
_q_ max!⟨ _k_ [(] _[q]_ [max][)] ⟩



_N_
∑ _aij_ 2 _...jq_ max +1 sin (
_j_ 2 _,...,jq_ max +1=1



which is a natural extension of the Kuramoto model with all oscillators having identical frequencies _ω_, and _Kq_
denoting the coupling strength of _q_ -simplex interactions. Here, the complex topology, which is as in Ref. [376]
remains mathematically tractable because oscillators have identical frequencies. All cliques in the graph defined by
the adjacency tensors **A** [(] _[q]_ [)] = { _aij_ 2 _...jq_ +1} with _q_ indices: for example, at order _q_ = 2, _aijk_ = 1 if there is a triplet
interaction ( _i,j,k_ ) and 0 otherwise. Coupling functions at each order are also a natural generalization of the standard
pairwise sine function, as they are chosen to be symmetric with respect to oscillator _i_, meaning that any permutation
of the other indices leaves the coupling function invariant. The authors have shown that each term in Eq. (48) can
be rewritten in terms of a newly defined Laplacian matrix, and all such matrices can combined into a multi-order
Laplacian controlling the dynamics of the whole system. The authors denote as _ki_ [(] _[q]_ [)] the connectivity of order _q_, i.e.
the number of distinct _q_ -simplices that node _i_ is part of, and as _A_ [ˆ][(] _[q]_ [)] = { _a_ ˆ [(] _ij_ _[q]_ [)][}] [the] [adjacency] [matrix] [of] [order] _[q]_ [,] [i.e.]
the number of distinct _q_ -simplices that the pair ( _i,j_ ) is part of. These definitions recover the usual definitions for
_q_ = 1. Note that the adjacency matrices _A_ [ˆ][(] _[q]_ [)] are different objects than the adjacency tensors **A** [(] _[q]_ [)] : the former have
dimension 2 and can take any integer value, whereas the latter have dimension _q_ + 1 and only takes binary values.
Infinitesimal heterogeneous perturbations _δθi_ around the synchronized state _θ_ _[S]_ ( _t_ ) = _ωt_, defined as _δθi_ = _θi_ - _ωt_, evolve
according to the linearized dynamics. In a system with _q_ -simplex interactions, this dynamics is determined by a
Laplacian _L_ [(] _[q]_ [)] = { _lij_ [(] _[q]_ [)][}] [of] [order] _[q]_ [defined] [as:]


_lij_ [(] _[q]_ [)] [=] _[ q k]_ _i_ [(] _[q]_ [)] _δij_                                   - _a_ ˆ [(] _ij_ _[q]_ [)] _[,]_ (49)


which is a natural generalization of the usual pairwise Laplacian. For instance, in the case of pure 3-simplex interactions, _Kq_ = 0 for all _q_ ≠ 3, the linearized system reads:



_δθ_ ˙ _i_ = − _[K]_ [3]

⟨ _k_ [(][3][)] ⟩



_N_
∑ _lij_ [(3)] _[δθ][j][.]_ (50)
_j_ =1



The stability of the synchronized state is then measured by the second Lyapunov exponent _λ_ 2 [(][3][)][, which is proportional]
to the second eigenvalue Λ [(] 2 [3][)] of the Laplacian _L_ [(3)] . When interactions of all different orders are present, it is practical
to define a _multi-order Laplacian_ _L_ [(mul)] = { _lij_ [(mul)] } as _lij_ [(mul)] = ⟨ _[K]_ _k_ [1] ⟩ _[l]_ _ij_ [(][1][)] [+] ⟨ _[K]_ _k_ [2] ⟩ _[l]_ _ij_ [(][2][)] [+⋅⋅⋅+] ⟨ _[K]_ _k_ _[q]_ [max] ⟩ _[l]_ _ij_ [(] _[q]_ [max][)] . so that the linearized



⟨ _[K]_ _k_ 2 [2] ⟩ _[l]_ _ij_ [(][2][)] [+⋅⋅⋅+] ⟨ _[K]_ _kq_ _[q]_ [max]



to define a _multi-order Laplacian_ _L_ [(mul)] = { _lij_ [(mul)] } as _lij_ [(mul)] = ⟨ _[K]_ _k_ 1 [1] ⟩ _[l]_ _ij_ [(][1][)] [+] ⟨ _[K]_ _k_ 2 [2] ⟩ _[l]_ _ij_ [(][2][)] [+⋅⋅⋅+] ⟨ _[K]_ _kq_ _[q]_ max [max] ⟩ _[l]_ _ij_ [(] _[q]_ [max][)] . so that the linearized

equations read:



⟨ _[K]_ _k_ 1 [1] ⟩ _[l]_ _ij_ [(][1][)] [+] ⟨ _[K]_ _k_ 2 [2]



_N_
_δθ_ ˙ _i_ = − ∑ _lij_ [(mul)] _δθj,_ (51)
_j_ =1


and the stability of the synchronized solution can be assessed by simply computing the second Lyapunov exponent
_λ_ [(mul)] 2, which is proportional to the second eigenvalue Λ [(mul)] 2 of the multi-order Laplacian _L_ [(mul)] . The authors have
then applied the multi-order Laplacian framework to simplicial complexes of increasing complexity. In the case of
all-to-all higher-order interactions, where all possible interactions take place at each order, a full analytical spectrum
can be obtained. When only attractive couplings are present, the spectrum indicates ( _i_ ) that the higher the order
of pure interactions, the more these interactions stabilize synchronization, as shown in Figs. 23A-C, and ( _ii_ ) that
the more orders are taken into account, the more stable synchronization is, as shown in Fig. 23D. When instead the
coupling is attractive at some orders, and repulsive at others, the interplay of the different terms can either lead to
stability or instability, which confirms and extends a result found in Ref. [376]. Decaying couplings strength have
also been considered in analogy with higher-order phase reduction techniques discussed in the next section. The
multi-order Laplacian is also applied to other models of simplicial complexes, such as the simplicial star-clique model,
and real-world brain system. The multi-order Laplacian is a general tool that can be used to investigate the effects
of higher-order interactions in other oscillatory systems.


50


FIG. 23. **Higher-order** **oscillator** **model** **of** **Ref.** **[141]** **in** **the** **case** **of** **all-to-all** **higher-order** **interactions.** The higher
the order of interactions taken into account, the more stable the synchronized state. Convergence of _N_ = 100 oscillators with
(A) only 1-simplex interactions and (B) only 2-simplex interactions. Convergence is faster in the second case. (C) This is
confirmed by the analytical first non-zero Lyapunov exponent at each order _q_, which is proportional to _q_ . Here, it is plotted
against _N_ . (D) Multi-order Lyapunov exponent more negative as _q_ max is increased. Figures reproduced from Ref. [141].


_2._ _Higher-order_ _interactions_ _from_ _phase_ _reduction_


Real-life oscillators are often nonlinear, and their dynamics is more complex than that of a simple phase oscillator. However, one can obtain phase models that approximate the original dynamics by using phase reduction
techniques [390, 391]. This makes phase models very powerful since they can capture the dynamics of networks of
general nonlinear oscillators, as long as they are weakly coupled. For example, the Kuramoto-Sakaguchi model can
obtained via a phase reduction of the mean-field complex Ginzburg-Landau equations [383]. The Kuramoto-Sakaguchi
model is an extension of the original Kuramoto model obtained by the addition of a phase shift _α_ in the coupling function sin( _θj_ - _θi_ + _α_ ) in Eq. (40). However, the Kuramoto-Sakaguchi model is still a first-order phase approximation
in the weak coupling parameter limit, and it only displays full incoherence or synchronization (see Refs. [366, 367] for
the case of identical oscillators). Other nontrivial dynamics such as chaos, cluster states, or weak chimeras, have only
been observed by introducing different symmetries or more harmonics in the coupling function [392]. Ashwin et al.
have noted ahead of time that, even though adding harmonics does unfold degeneracies, there might be some that will
only unfold by considering non-pairwise interactions [392]. More recent results indicate, however, that many-body
interactions emerge naturally when considering phase reductions including higher-orders terms in the weak coupling
parameter [374, 383, 393]. Moreover, these studies show that the inclusion of higher-order terms unlock nontrivial
dynamical regimes as well as transitions between them. In this section, we will only review studies approaching
phase reduction of higher-order networks of oscillators from a theoretical point of view. Section VI C will then be
complementary to this section, as phase reduction will there be approached from the inverse-problem point of view
of network inference.
Ashwin, Bick, Rodrigues, and coworkers have produced a series of important contributions for phase reduction
of populations of identical oscillators [374, 394–397]. The authors of Ref. [392] have suggested that interactions
beyond pairwise might be the only way to unfold some degeneracies and unlock nontrivial dynamics [392]. In a paper
published in the same year [374], Aswhin and Rodrigues have shown that the application of phase reduction to a
systems of generic nonlinear identical systems with global symmetric coupling yields the Kuramoto-Sakaguchi at the
lowest order, but at the next order, terms including 2-, 3-, and 4-body interactions naturally emerge:



_N_
∑ _g_ 3( _θj_ + _θk_ - 2 _θi_ )+ _[ϵ]_
_j,k_ =1 _N_ [2]



_N_
∑ _g_ 4(2 _θj_ + _θk_ - _θi_ )+ _[ϵ]_
_j,k_ =1 _N_ [3]



_N_
∑ _g_ 5( _θj_ + _θk_ - _θl_ - _θi_ ) (52)
_j,k,l_ =1



_θ_ ˙ _i_ = ˜Ω( _θ,ϵ_ )+ _[ϵ]_

_N_



_N_
∑ _g_ 2( _θj_ - _θi_ )+ _[ϵ]_
_j_ =1 _N_ [2]



The inclusion of such terms allows for a wider range of dynamical behaviors such as cluster states, and predictions that
are valid for longer timescales. Moreover, the authors have been able to demonstrate that non-pairwise interactions
yield multistability via the coexistence of many two-cluster states, with varying cluster size, just as in Refs. [371, 373].
Here, the many-body interactions terms are traced back to cubic nonlinearities in the original nonlinear system.
Bick et al. have further investigated the dynamics of the phase reduced system of Eq. (52), looking in particular for
the possibility of chaos in small networks [394]. Previously, it was thought that for populations of identical oscillators,
higher harmonics in the coupling functions, or nontrivial amplitude dynamics, were necessary to observe chaos in
small networks ( _N_ = 4 is smallest theoretical size to exhibit chaos). In fact, for pure pairwise interactions, for _N_ = 4,


51


FIG. 24. **Switching** **dynamics** **in** **the** **Bick** **model** **of** **Ref.** **[395]** **with** **three** **populations** **of** **two** **oscillators** **each.** The
oscillators in the three populations intermittently synchronize and desynchronize. Figure reproduced from Ref. [395].


the only known coupling function to yield chaos has a minimum of four nontrivial harmonics (for larger networks, less
harmonics are needed) [398]. Remarkably, the authors of Ref. [394] were able to show that two nontrivial harmonics
are sufficient to see chaos, even in the case _N_ = 4, when many-body interactions are considered. In the last two
years, Bick and coworkers have produced three more pieces of work in the same direction, focusing in particular on
heteroclinic cycles [395–397]. In the first paper Bick has considered _M_ populations of _N_ oscillators each, with pairwise
interaction between oscillators in the same population, and non-pairwise interactions among oscillators of different
populations [395]. This setup builds on a previous work by Komarov and Pikovsky who considered populations of
oscillators with distinct frequency and focused on a specific three-population resonance [399]. In Bick’s setup, all
oscillators have identical frequencies, and it is the presence of nonpairwise interactions that yields the heteroclinic
connections joining the weak chimeras. Indeed, as shown in Fig. 24 switching between states of so-called localized
frequency synchrony were observed [395]. Bick has further built on that paper to formally prove the existence of those
heteroclinic cycles in Ref. [396], and finally to assess their stability together with Lohse in Ref. [397].


More recently, Le´on and Paz´o have produced a very thorough study of the higher-order phase reduction of the meanfield complex Ginzburg-Landau equation (MF-CGLE) [383]. To date, the phase reduction of MF-CGLE was only
known up to the first order, and produces the standard Kuramoto model of Eq. (40). The Kuramoto model exhibits
two dynamical regimes only, synchronization and incoherence, but is unable to reproduce more exotic regimes of the
MF-CGLE, such as quasiperiodic partial synchronization and cluster states. To remedy that, the two authors have
proposed a isocron-based phase reduction method up to the second and third order. Crucially, the authors demonstrate
the accuracy of their technique by showing that the obtained phase model does exhibit the exotic dynamics of the
weakly coupled MF-CGLE.


Finally, Matheny et al. have published a very complete study combining experiments, numerics, and analytics [393].
They have performed experiments with a ring of eight nano-electromechanical nonlinear oscillators, and have observed
exotic and complex dynamics including weak chimeras, decoupled states, traveling waves, and inhomogeneous synchronized states. Then, they have obtained a phase approximation of their initial nearest-neighbor (i.e. pairwise
interactions) network of so-called saturated oscillators, up to the second order in the coupling strength. As in the
other studies, terms with three-body interactions naturally emerged in the phase description, with the addition of
next-nearest neighbor and biharmonic terms as illustrated in Fig. 25. The strength of their phase model is that it is
able to qualitatively reproduce all the complex dynamics regimes observed both in the experiments and in the initial
nonlinear model.


In conclusion, phase reduction naturally yields higher-order interactions between the phases. Progress in analytical
phase reduction up to higher-order can potentially helps us understand the exotic and complex dynamics of network
of general nonlinear oscillators, which cannot be captured by first-order phase models. Moreover, it will certainly be
helpful in the future to the network inference area presented in Sec. VI C. Finally, it is also worth mentioning that
some efforts has been made to compute phase reductions numerically, when no analytical derivation is available [400].


52


FIG. 25. **Ring** **of** **eight** **nano-electromechanical** **nonlinear** **oscillators** **from** **Ref.** **[393].** The solid black lines represent
physical connections between the oscillators. Dashed and dotted lines represent effective higher-order coupling that appear in
the phase reduced model. This systems exotic complex dynamics. Figure reproduced from Ref. [393].


**B.** **Nonlinear** **oscillators**


_1._ _Chaotic_ _oscillators_


When chaotic oscillators are coupled, they can synchronize in various ways. The study of chaotic synchronization
started with two seminal papers published in the 90s [401, 402]. In the first of these works, Pecora and Carroll
discovered the phenomenon of _complete_ _synchronization_, a regime in which coupled chaotic oscillators converge to
an identical state and evolve with the same trajectory [401]. Then, Rosenblum, Pikovsky and Kurths, showed that
chaotic oscillators can _phase_ _synchronize_, while their amplitudes vary chaotically and are uncorrelated [402]. The
richness of the dynamics of chaotic oscillators allows for more complex behaviors in networked systems than those
observed with phase oscillators, and has been the object of interest in the scientific community [352]. However, all
the studies on chaotic synchronization, with very few exceptions [403–405], have considered pairwise interactions. We
will therefore start our discussion of high-order effects with a series of studies related to network motifs.
In Ref. [406] Lodato et al. have investigated whether there can be an underlying dynamical reason to explain the
existence of network motifs. In particular they have focused on synchronization and have evaluated analytically the
stability of the synchronous state in all directed and undirected 3- and 4-node graphs of chaotic oscillators. They have
then compared the results with the known abundance of these small graphs as subgraphs (motifs) of real biological
systems. Interestingly, the authors were able to show that 3- and 4-node graphs exhibiting more stable synchronous
states in general coincide with network motifs preserved across evolution, while the bifan motif, one of the three most
relevant biological motifs [53], was not compatible with synchronization for any type of chaotic dynamics. In another
study [407], Soriano et al. have investigated the link between generalized synchronization and correlation between
the oscillators present in a motif, remarkably showing that it is possible to construct small graphs of oscillators that
synchronize but at the same time do not exhibit correlations. This result, important for network inference, stresses
how indirect connections might be systematically underestimated. Finally, it is worth mentioning here one more study
on motifs [408]. Although the oscillators considered were not chaotic, a fractal topology was used. The authors were
able to analytically compute the stability of various dynamical regimes. As an example, they showed that oscillation
death was possible in that setting, even with a symmetric coupling function.
We continue with four studies of synchronization in bipartite setups representing two types of populations of
oscillators, with inter-population links. The first study considered a complete bipartite network of nonlinear maps
(chaotic or periodic) [409]. The existence and stability of synchronization and cluster synchronization was assessed
via Lyapunov exponents through the Master Stability Function (MSF) formalism [6, 359, 410]. Similarly, the second
study investigated chaotic synchronization in coupled Bernoulli maps by using the same formalism [411]. The bipartite
setting was one of the settings investigated, and the study concluded that synchronization was not possible in that
setting. In the third study [412], Sorrentino and Ott used a bipartite setting as a special case of multiple interacting
populations of oscillators. The authors found that adding intra-population links could enhance the stability of socalled multisynchronous states. Finally, bipartite networks (together with random and tree-like networks) were one
of three settings in which Pecora et al. showed the possibility for cluster synchronization and so-called isolated
desynchronization [363]. The latter is a dynamical regime in which one or more clusters desynchronize while the other
clusters remain synchronized.


53


It was as early as 1998 that the synchronization of coupled chaotic circuits was studied by Wu on hypergraphs [403].
The system under consideration consisted of indentical chaotic circuits (the nodes of the hyphergraph) coupled via
multi-terminal resistance-devices, effectively yielding multi-circuit interactions (the hyperlinks). For the sake of mathematically tractability the author restricted his study to a case with only triplet interactions. By looking at the
algebraic connectivity of the hypergraph, defined as the smallest nonzero eigenvalue of the hypergraph Laplacian, he
was then able to derive sufficient conditions for the complete synchronization of the circuits. Indeed, a large algebraic
connectivity and linear but passive coupling were required to yield synchronization. Note that all computations rely
on the hypergraph structure, even if the system was represented as a bipartite network in the figures of the original
paper. A more recent study by Krawiecki has gone much further in complexity [404]. In particular, the author has
considered a system of identical chaotic (Lorenz) oscillators placed on the nodes of scale-free _q_ -hypergraphs (with
_q_ ≥ 2), i.e. hypergraphs that exhibits only ( _q_ - 1)-simplex interactions, i.e. in which each hyperedge connect exactly
_q_ nodes, and the number of hyperedges attached to a node follows a power-law distribution. He found out that a
state of complete synchronization can be achieved and coexists with a state of oscillation death [413]. Remarkably,
the traditional Master Stability Function formalism was generalized to hypergraphs so as to investigate the stability
of the complete synchronization state. Furthermore, the study has reported the existence of other dynamical regimes
such as partial anti-synchronization.
In another study [296], Wu et al. have derived analytical criteria for the synchronization of Chua oscillators in
_q_ -hypergraphs. The hypergraphs have a power law distribution of hyperdegrees such that when _q_ = 2, the structure
reduces to that of a Barab´asi-Albert network. Recently, Mulas et al. [414] used the Master Stability formalism to
derive stability criteria in coupled nonlinear oscillators on hypergraphs with the particularity that they are directed.
Finally, very recently, Gambuzza et al. [405] have generalized the Master Stability Function formalism to the
most general case of simplicial complexes. They have considered a system of _N_ dynamical units, which are placed
on the nodes of a simplicial complex of any dimension _q_ max and can be involved in _q_ -simplex interactions, with
_q_ = 1 _,_ 2 _,...,q_ max, as described by the structure of the simplicial complex. The equations of motion of the system read:

**x** ˙ _i_ = **f** ( **x** _i_ ) + _σ_ 1 ∑ _[N]_ _j_ 1=1 _[a]_ _ij_ [(][1] 1 [)] **[g]** [(][1][)][(] **[x]** _[i][,]_ **[x]** _[j]_ [1][) +] _[ σ]_ [2][ ∑] _j_ _[N]_ 1=1 [∑] _j_ _[N]_ 2=1 _[a]_ _ij_ [(][2] 1 [)] _j_ 2 **[g]** [(][2][)][(] **[x]** _[i][,]_ **[x]** _[j]_ [1] _[,]_ **[x]** _[j]_ [2][) +] _[ ...]_
(53)
+ _σq_ max ∑ _j_ _[N]_ 1=1 _[...]_ [∑] _j_ _[N]_ _q_ max =1 _[a]_ _ij_ [(] _[q]_ 1 [max] _....j_ [)] _q_ max **[g]** [(] _[q]_ [max][)][(] **[x]** _[i][,]_ **[x]** _[j]_ [1] _[,...,]_ **[x]** _[j][q]_ max [)] _[,]_


where **x** _i_ ≡ **x** _i_ ( _t_ ) is the _m_ -dimensional vector describing the state of node (dynamical unit) _i_ at time _t_, the real valued
parameters _σ_ 1 _,...,σq_ max tune the strength of the interactions at the different orders _q_ = 1 _,...,q_ max, and _a_ [(] _ij_ _[q]_ 1 [)] _...jq_ [are] [the]

entries of the adjacency tensor **A** [(] _[q]_ [)] representing the structure of the simplicial complex. Furthermore, **f** ∶ R _[m]_ �→ R _[m]_

is the most general function describing the local dynamics, which is assumed to be identical for all units, while
**g** [(] _[q]_ [)] ∶ R [(] _[q]_ [+][1][)×] _[m]_ �→ R _[m]_, with _q_ = 1 _,....,q_ max, are the functions governing the interaction forms at different orders. The
authors have been able to study analytically the stability of the complete synchronized state **x** _i_ ( _t_ ) = **x** _[S]_ ( _t_ ) ∀ _i_, under
the only assumption that the coupling functions are synchronization non-invasive, i.e. that **g** [(] _[q]_ [)] ( **x** _[S]_ _,_ **x** _[S]_ _,...,_ **x** _[S]_ ) ≡ 0 ∀ _q_ .
Based on a set of Laplacian matrices similar to those in Eq. (49), they have derived a Master Stability Function with
the negativity of the maximum Lyapunov exponent as the stability criterion. The method has been illustrated on
simplicial complexes of coupled chaotic oscillators, such as R¨ossler and Lorenz dynamical systems, with both pairwise
and triplet interactions. When nonlinear oscillators are coupled, the Lyapunov exponents depend nonlinearly on the
eigenvalues of the Laplacian of the system. Hence, it is possible to have bounded regions of the parameter space where
synchronization is stable, as defined by a negative maximum Lyapunov exponent. The authors have investigate how
the region of stability depends on the structure of the simplicial complex and on the coupling functions. Figure 26
show an example of coupling functions for which the region of synchronization is respectivey bounded (panel (A)) and
unbounded (panels (B) and (C)), for a given node dynamics and structure of the simplicial complex. This framework
will hopefully be used in further studies along those lines, for various oscillators, topologies, and coupling functions.


_2._ _Neuron_ _models_


The brain provides a very rich and important terrain to study synchronization of neurons with higher-order interactions. However, so far, little is known about synchronization of neuron models in higher-order networks from
the theoretical side. In the theoretical study of neuronal networks, various oscillators models are used to represent
neurons, depending on the context and the goals of the modeler [415, 416]. Historically, the most famous model is
that of Hodgkin and Huxley, dating back from 1952 and for which they won a Nobel Prize in Physiology or Medicine.
Their model describes how the neurons spike, and consists of a set of nonlinear differential equations for the membrane
potential. Others models such as neural mass models have been developed since and have been used successfully to
understand synchronization phenomena in the brain. Here, we report the different higher-order settings in which
synchronization of neuron models has been carried out.


54


FIG. 26. **Coupling** **functions** **affect** **synchronization** **in** **simplicial** **complexes** **of** **coupled** **chaotic** **oscillators** **as** **in**
**the** **framework** **of** **Ref.** **[405].** Synchronization phase diagram of a system of four R¨ossler systems are coupled in pairs and
triplets according to the simplicial complex sketched. A baseline case (A) is compared to (B) where the pairwise coupling
function is changed, and (C) where the triplet coupling function is changed. The predictions of the Master Stability Function
formalism (blue lines) are in good agreement with the regions of synchronization obtained by numerical simulations (black).
Figures adapted from Ref. [405].


FIG. 27. **Synchronization** **pattern** **in** **inhibitory** **motif** **from** **Ref.** **[418].** The pacemaker neuron (blue) is the one with
the longer interburst time. Figure adapted from Ref. [418].


We start with a bipartite setting that was investigated in [417]. Here the authors use that setting as a mean to
study the interactions between two populations of neurons, and in fact study two coupled bipartite networks. The
authors concluded, by analytical and numerical calculations, that the two networks can be synchronized with the help
of adaptive feedback.
To the best of our knowledge, three studies have considered synchronization in motifs of neurons [418–420]. Shilnikov
and collaborators [418] provide a detailed analysis of synchronization in motifs of both inhibitory and excitatory, and
inhibitory-only neurons, see for example Fig. 27. The authors showed that the neurons can self-organize to designate
the pacemaker among them by shortening the burst duration of the (secondary) driven neuron. This effect hold in
inhibitory-only motifs, but the synchronous patterns can coexist with asynchronous patterns. The authors show that
the addition of excitatory links ensure synchronous patterns of bursting. Finally, the inhibitory-only motifs exhibited
multistability with as much as eight coexisting attractors. The authors suggest these attractors could be associated
with patterns known to control certain animal and human locomotion activities.
In the second study [419], stable so-called anticipated synchronization was shown to exist in biologically plausible
3-neuron motifs including inhibitory and excitatory synapses with time delays. All parameters have a clear biological
interpretation, and the authors identified a transition from delayed synchronization to anticipated synchronization
when synaptic conductances are increased withing physiological ranges.
In the third study [420], Gollo et al. identified a mechanism by which zero-lag synchronization is facilitated.
Zero-lag synchronization is of widely accepted importance in brain studies. Indeed, experimental evidence shows
zero-lag synchronization between distant regions of the brains. A mechanism called “dynamical relaying”, related
to a specific motif, was proposed to account for such phenomenon in the presence of conductance delays. However,
Gollo and coworkers showed that the motif was not always a reliable condition for zero-lag synchronization. Instead,
they narrowed down a “resonance pair” of reciprocally connected neurons, which ensures zero-lag synchronization.
They did so by systematically analyzing synchronization in small network motifs of Hodgkin-Huxley, neural mass,
and Izhikevich neurons.
Finally the few studies that considered synchronization in larger networks of neurons relied either on numerics or
phase reduction techniques, such as [373], and were described in the corresponding sections above. For more applied
studies on the higher-order structure of brain networks in neuroscience, see Sec. IX B.


55


**C.** **Inference** **of** **nonpairwise** **interactions** **in** **coupled** **oscillators**


In networks of coupled dynamical units, the standard approach is to fix the structure of the network and to study
how the system evolves. However, when modeling real oscillatory networks, we very often have to face the so-called
inverse-problem too: can we reconstruct the underlying network structure by just looking at the dynamical evolution
of the system? This is a problem with relevant applications. In neuroscience, for example, one wants to infer the brain
neuronal network from EEG data, i.e. times series of the electrical activity of neurons or cortical areas. This task,
known as network inference, is highly non trivial, and three main approaches have been proposed in the literature
to reconstruct directional pairwise interactions based on information theory [421], state-space approaches [422], and
phase dynamics [423]. Here, we report on the few studies that have addressed the inference of higher-order interactions,
i.e. of interactions between three or more oscillators, based on the third approach using phase dynamics.
Following [424], let us start by considering the general system of _N_ coupled dynamical systems:


**x** ˙ _i_ = **G** _i_ ( **x** _i_ ) + _ϵ_ **H** _i_ ( **x** 1 _,...,_ **x** _N_ ) _,_ (54)


with _i_ = 1 _,...,N_, where function **G** _i_ determines the local (uncoupled) dynamics of oscillator _i_, _ϵ_ is the coupling
strength, and **H** _i_ is the function describing the structural coupling. It is assumed that the **G** _i_ are such that each
uncoupled oscillator has a stable limit cycle, which can be parametrized by a phase _θk_ . The _structural_ _couplings_
are directed physical couplings, e.g. synapses in the case of neurons. If **H** _i_ does not depend on **x** _k_, we say there
is no structural coupling from _k_ to _i_ . In general, **H** _i_ can contain terms of pairwise coupling, **H** _ij_ ( **x** _i,_ **x** _j_ ), triplet
couplings, **H** _ijk_ ( **x** _i,_ **x** _j,_ **x** _k_ ), or coupling between any larger numbers of oscillators. For example, one can write **H** _i_ =
∑ _j_ **H** _ij_ ( **x** _i,_ **x** _j_ ), if only pairwise interactions are present in the network. In the case of weak coupling, i.e. in the small
_ϵ_ limit, each individual limit-cycle is perturbed weakly enough so that system (54) has an attracting _N_ -torus solution
which can be written in terms of _N_ phases _θ_ 1 _,...,θN_ [424] as:


_θi_ = _ωi_ + _hi_ ( _θ_ 1 _,...,θN_ ) _._ (55)


The new coupling functions can then be written as an expansion in the small coupling parameter _ϵ_


_hi_ ( _θ_ 1 _,...,θN_ ) = _ϵh_ [(] _i_ [1][)] ( _θ_ 1 _,...,θN_ ) + _ϵ_ [2] _h_ [(] _i_ [2][)] ( _θ_ 1 _,...,θN_ ) + _...,_ (56)


by performing a perturbative reduction of Eq. (54) (see Sec. VI A 2). We refer to the couplings functions _hi_ in
system (55) as _effective_ _phase_ _couplings_ . It is important to note that, as in Sec. VI A 2, the effective phase couplings
_hi_ differ from the original structural couplings **H** _i_ . More specifically, there can be an effective phase coupling from
_j_ to _i_ even if there is no structural coupling, but the opposite is not true. So, there are more effective links than
structural links. However, if _ϵ_ is sufficiently small, structural and effective couplings are practically identical. Indeed,
the additional effective links appear only in the second-order terms _hi_ [(][2][)] ( _θ_ 1 _,...,θN_ ) which is rescaled by _ϵ_ [2], and in
the higher-order terms which scale in higher powers of _ϵ_ .
The goal of the methods proposed in Refs. [424, 425] is to reconstruct the effective coupling of the system in Eq. (55),
including couplings beyond pairwise, starting from at least one scalar time series for each node of the original system
in Eq (54). A situation where only a scalar time series is available for each node is common for example in neuroscience
with EEG recordings, and is such cases, the information can be sufficient to reconstruct the phase system (55) but not
the original system (54). Such a goal is achieved in two main steps: first, by reconstructing phases from the original
time series, and second, by reconstructing the effective phase couplings _hi_ from the phases. Finally, weighted directed
links are extracted from the coupling functions by measuring the so-called partial norms [424] associated to each link.
Indeed, since the _hi_ are 2 _π_ -periodic functions of _N_ phases, they can be decomposed into a Fourier expansion for the
phases. Then, the pairwise interaction from _i_ to _j_ is determined by the coefficients in the expansion that depend
only on _i_ and _j_, and it can be measured as the sum of the square of those coefficients. More specifically, in Ref. [424]
Kralemann et al. have generalized this method of spectral decomposition of the effective coupling functions from
Ref. [426] to the case of interactions among more than two oscillators. Hence, each term corresponds to a coupling
among two or more oscillators, and its associated partial norm indicates its strength. The numerical method has been
successfully tested on networks of size 3, 5, and 9 of van der Pol oscillators. Figure 28 shows an example of the results
obtained in the case of networks with three nodes. In general, the effective links detected by the method reliably
reveal the true structural links (pairwise or higher-order). However, the method also detects some additional links,
as expected: some are true higher-order links of the phase description, while some others are spurious links, due to
a systematic error of the method. Unfortunately, no analytical derivation of the phase reduction exists yet for these
systems (see Sec. VI A 2 for other systems), so that there is no clear way to distinguish, of those additional links,
which are true and which are spurious, to date. The method also successfully avoids detecting functional links. Two
oscillators are said to be _functionally_ _coupled_ if their dynamics is correlated. Functional coupling is a concept typical
of brain activity studies, and it may only be loosely related to structural and effective coupling [427].


56















**Real** **Inferred** **Real** **Inferred**


FIG. 28. **Inference** **of** **directed** **pair** **and** **triplet** **couplings** **among** **three** **Van** **der** **Pol** **oscillators** **from** **the** **method**
**in** **Ref.** **[424].** An arrow from the center to a node _i_ indicates a directed triplet interaction from ( _j, k_ ) to _i_ . Panels (A) and
(B) show two examples of the original structural network and the reconstructed one. While the inference in the first case is
good, the method yields a spurious links from node _c_ to _a_ . Figures adapted from Ref. [424].


It is worth mentioning here that Rosenblum and Pikovsky have developed in parallel a numerical phase reduction
beyond the first order to remedy the missing analytical derivations and complement the existing ones [400]. For such a
method to work, the available time series data must satisfy two criteria: they must not come from a fully synchronized
trajectory, and it must be of sufficient length. Indeed, to infer the coupling functions, the phases must cover the _N_ torus. Hence, first, when the system is synchronized, however, the dynamics only happens on a limit-cycle, and no
information can be extracted. Second, the time series must be long enough to cover the _N_ -torus. Because of this, the
method, is practically useless for large networks, as the data needed to cover a _N_ -dimensional space rapidly grows
with _N_ . To be able to deal with networks larger than _N_ - 3, only partial phase dynamics reconstruction is possible.
Typically, one assumes pairwise interactions, and only considers the phases _θi_ and _θj_ to infer the coupling functions
_hij_ from _j_ to _i_ . The idea is to do so for all pairs of oscillators, and instead of reconstructing the full system in Eq. (55),
one only allows for pairwise links to be inferred. However, this method yields spurious effective phase links that do
not exist in the full system in Eq. (55) or the original structural connectivity of system in Eq. (54).
To overcome this, Kralemann et al. have extended their previous method discussed above, and have proposed a
partial triplet analysis [425]. They have considered all the triplets of phases of the type _θi,θj,θk_ to reconstruct the
coupling functions _hijk,hjki,hkij_ . From these functions, pairwise connections have been obtained from the partial
norm of the spectral decomposition, as above. The authors have showed that triplet partial analysis performed better
than the pairwise partial analysis in networks of 3 and 4 Van der Pol oscillators. Indeed, the true links were detected
equivalently well, but the triplet partial analysis successfully avoided detection of spurious links produced instead by
the pairwise analysis.
As mentioned above, all these methods need input data that do not come from synchronized trajectories. This
can be checked by evaluating the usual pairwise _n_ ∶ _m_ synchronization index _γj,k_ = ∣⟨ _e_ _[i]_ [(] _[nθ][j]_ [−] _[mθ][k]_ [)] ⟩∣, where ⟨⋅⟩ indicates
temporal averaging, and where _n_ and _m_ are integers [352]. This index is close to 1 if oscillators _j_ and _k_ are phase
locked. Complete network synchronization can be checked by computing the index for all pairs of oscillators. However,
triplet synchronization is not revealed by this index. Indeed, it is well possible that three phases _θi,θj,θk_ satisfy the
relation _nθi_ + _mθj_ + _lθk_ = constant for three integers _n,m,l_, even though the pairwise index of each pair is not close
to 1. To reveal triplet synchronization from data, the following triplet synchronization index has been introduced in
Ref. [428]:


_γi,j,k_ = ∣⟨ _e_ _[i]_ [(] _[nθ][i]_ [+] _[mθ][j]_ [+] _[lθ][k]_ [)] ⟩∣ _._ (57)


Notice that a value of _γi,j,k_ close to 1 is not a sufficient condition for synchronization. Indeed, it only indicates its
possibility, since a large value of the index can also be the consequence of other types of interdependence between the
phases. Finally, as mentioned by the same authors, the index can be readily extended to higher-order synchronization
indices, valid for quandruplets and higher-resonances. Jia et al. have built on that, showing experimentally the
existence of states where triplets are synchronized but pairs are not [429].
In Ref. [382], Stankovski et al. have proposed another method to reconstruct the effective phase connectivity of a
network. The specificity of their method is that it works for network of oscillators with time-varying coupling and
frequencies, and that are subject to noise. The method is based on dynamical Bayesian inference [430], and detects
coupled pairs, triplets, and quadruplets of oscillators. The method computes the values of a set of parameters that
fully determine the couplings. The values of the parameters are inferred by making use of Bayes’ theorem, which
takes a prior distribution and evolves it into a posterior distribution, by using time series of the system and building a
likelihood function. The authors have demonstrated the accuracy of the method on a simulated 5-oscillator network,
as well as on real multi-channel EEG data. The method has been shown to outperform inference based on pairwise
interactions only. Unfortunately, similarly to the other methods presented above, this method works for relatively
small networks.


57


For applications of inference methods of higher-order interactions on real brain networks data, see Sec. IX B.


**VII.** **SPREADING** **AND** **SOCIAL** **DYNAMICS**


Dynamical processes that emulate human behaviors have been the focus of many studies, where social relationships
and interactions are typically considered as an underlying structure. Social interactions are a natural testing ground
for higher-order approaches. Since individuals can interact in pairs or groups, the dynamics should in turn account
for the higher-order effects that the non-pairwise interactions might lead to. In this section, we review a broad variety
of models, initially introduced and studied on graphs, that have been extended as dynamical processes on HOrSs. We
start reviewing _spreading_ _processes_, historically embedded within the literature of epidemics on networks [431, 432],
but recently revisited to fit the dynamics of social contagions [433]. We then continue with a wider class of models of
_social_ _dynamics_ mostly devoted to the formation of opinions and consensus [434–436].


**A.** **Spreading** **in** **higher-order** **networks**


The study of spreading processes on networks is one of the branches of network science that attracted more attention
among the community. Building on top of classical epidemiological compartmental models [437–439], the recent success
of these models is partially due to the increasing availability of large scale data that opened up new research avenues
in which researchers make use of the newly available data sources to inform the models, which on turn allow us to
forecast and possibly control the disease spreading [440–444]. In light of these new advancements, network scientists
have been slowly, but extensively, introducing more and more details into the modeling framework in order to increase
its accuracy and ultimately its predictive power.
In this scenario, two of the most studied compartmental models are the Susceptible-Infected-Recovered (SIR) and
the Susceptible-Infected-Susceptible (SIS). In both models, susceptible individuals (S) can get infected by mean of an
interaction with infectious ones (I). This SI process always leads, by construction, to the absorbing state in which all
individuals are infected. The introduction of an additional transition leads to richer phenomena. More specifically,
in the case of the SIS, individuals can switch multiple times between the S and I states, eventually reaching a steady
state in which the epidemic is sustained by a non-zero number of individuals. Contrarily, in the SIR, individuals gain
immunity to reinfections after a certain amount of time, or with a given probability per unit time. These immune
individuals are then called recovered (R) and do not participate anymore to the spreading dynamics. This type of
models is therefore used when it comes to modeling infectious diseases such as Ebola, or seasonal influenza, in which
individuals can acquire immunity against reinfections. As a consequence, the SIR presents also the disease-free state
as an absorbing state.


Many theoretical approaches have been developed to analytically describe, with increasing level of complexity, the
dynamics of epidemic spreading on complex networks. An accurate analytical description should include the interplay
between the structure of the contact patterns and the dynamics of the spreading process on top. Here, instead of
going through the assumptions, advantages and drawbacks of all the possible descriptions, from the mean-field (MF)
and the heterogeneous mean-field (HMF), to the most accurate microscopic Markov-chain approaches, we refer the
interested reader to [432, 445–448] and references therein.


While the aforementioned models have been widely used to study the spread of diseases, there’s a variety of other
domains where they have been successfully applied. Indeed, another long tradition of modelers that have been using
similar frameworks to characterize the spreading of social phenomena, such as the diffusion of rumors and fads or
the adoption of novelties and technological innovations [449–452]. However, in all these situations the social nature
of the contacts that mediate these processes calls for ad-hoc modeling adjustments that are not present in simple
disease epidemics models. These approaches, developed under the name of _complex_ _contagion_, are meant to include
additional ingredients, such as mechanisms of social influence and peer pressure, already widely studied within the
social sciences [15, 46, 453]. The requirement of these new features, not needed when dealing with the spreading of a
pathogen, gave rise to a plethora of models that have been already extensively reviewed in Ref. [454].
Here, keeping the focus on the dynamics of social contagion, we shift the attention towards the structural aspect
of the social contacts on top of which the dynamics evolves. Moving from pairwise to higher-order structures, we
investigate the dynamical effects brought by the novel representations. There is a matter of discussion whether social
relationships could be better modeled by using simplicial complexes rather than hypergraphs. In the end, depending
on the situation, it might be reasonable or not to assume that in a group interaction all the sub-interactions among
the group members should be considered as well [455]. In what follows, we distinguish between the two approaches
and discuss recent developments towards the inclusion of HOrSs in the modeling approach. Our limited goal is to


Simplicial contagion







**H**



**I**



58


1.00


0.75


0.50


0.25


0.00

0 100 200 300 400 500
Time, _t_



FIG. 29. **Simplicial** **contagion** **model** **(** _D_ = 2 **)** **[262].** (A-F) Different channels of infection for a susceptible node _i_ are shown.
Notice (F), where node _i_ can get the infection from each of the two 1-simplices with probability _β_, and also from the 2-simplex
with probability _β_ ∆. Behavior on synthetic random simplicial complexes: In (H) the average fraction of infected obtained
by means of numerical simulations is plotted against the rescaled infectivity _λ_ = _β_ ⟨ _k_ ⟩/ _µ_ for different values of _λ_ ∆ ( _λ_ ∆ = 0
gives results for the standard SIS model without higher-order effects). The red lines correspond to the analytical MF solution
described by Eq. (58). When _λ_ ∆ ( _λ_ ∆ = 2 _._ 5 we observe a discontinuous transition with the formation of a bi-stable region where
healthy and endemic states co-exist. (I) Temporal evolution of the densities of infectious nodes in the bi-stable region ( _λ_ = 0 _._ 75,
_λ_ ∆ = 2 _._ 5). Different curvesand different colorscorrespond to different values of _ρ_ 0, the initial density of infectious nodes. The
dashed horizontal line corresponds to the unstable branch of the MF solution, separating the two basins of attraction. Figures
adapted from Ref. [262].


introduce some of the recent efforts in this direction without imposing selective constraints on how a “pure” higherorder dynamics should be defined on these new structures. This leads to a mixture of models based on higher-order
and not-so-higher-order dynamics on HOrSs. We explicitly distinguish between the HOrSs, starting from spreading
processes that take place on simplicial complexes and then moving to hypergraphs.


_1._ _Spreading_ _on_ _simplicial_ _complexes_


In the simplicial contagion model proposed by Iacopini et al. [262], a simplicial complex is used to represent the
social structure on top of which the contagion dynamics takes place. By definition, all the sub-interactions contained
in each group interaction are considered. Therefore, the dynamics of the model specifically relies on the different
channels of infections (1-simplex, 2-simplex, etc.) through which, with different transmission rates, a contagion can
happen. The SIS-like model of order _D_ is controlled via a set of control parameters _β_ 1 _,β_ 2 _,...,βD_, whose elements
represent the probability per unit time for a susceptible node _i_ that participates to a simplex _σ_ of dimension _D_ to get
the infection from each one of the infectious sub-faces composing _σ_ (sub-faces in which all nodes but one are infected).
At order _D_ = 2, one has _β_ 1 and _β_ 2 = _β_ ∆ corresponding respectively to the probability that a susceptible node _i_ receives
the infection from an infected node _j_ through the link ( _i,j_ ) and to the probability of receiving it from an infectious
2-simplex ( _i,j,k_ ) incident on _i_ . The recovery dynamics is controlled by the standard recovery probability _µ_, which,
being node-dependent, does not “feel” the higher-order structure (Figs. 29A-G).
Even the inclusion of only the lowest higher-order interactions (2-simplices) dramatically changes the nature of the
spreading process, going from a continuous to a discontinuous phase transition in the prevalence as a function of the 1simplex infectivity _λ_ (Fig. 29H). Notice that the nature of the transition depends on the 2-simplex infectivity _λ_ ∆. This
behavior is confirmed by numerical simulations on empirical data obtained from the Sociopatterns collaboration [456]
and on synthetic random simplicial complexes (see Sec. IV A 5), where a bi-stable region in which healthy and an
endemic states co-exist appears. This is illustrated in Fig. 29I, in which different curves represent different realizations
of the model starting from seeds of infectious nodes of different sizes (colors). Further analytical insights on this bistability can be found in Ref. [457].
The authors further explained the observed phenomenology through an analytical investigation based on an extension of the standard mean-field (MF) approach for networks, specifically adapted to the case of HOrSs. In this case,
the general equation for the evolution of the stationary density of infected _ρ_ ( _t_ ) reads


_D_
_dtρ_ ( _t_ ) = − _µρ_ ( _t_ ) + ∑ _βd_ ⟨ _kd_ ⟩ _ρ_ _[d]_ ( _t_ )[1 − _ρ_ ( _t_ )] (58)
_d_ =1


with ⟨ _kd_ ⟩ denoting the average generalized degree, i. e., the number of _d_ -dimensional simplices incident on average


59


on each 1-dimensional simplex _α_ : ⟨ _kd_ ⟩= ⟨ _kd,_ 1( _α_ )⟩ _α_ (see Sec. III B 1). This approach confirmed the results obtained
on synthetic random simplicial complexes, showing that the steady-state dynamics, the position, and the nature of
the transition can be predicted analytically on social structures characterized by homogeneous degree distributions.
This is shown in Fig. 29H, where the MF curves (red) are compared to the simulated results (points), and in Fig. 29I,
where the dashed gray line—corresponding to the unstable solution of the MF approach—correctly detects the two
basins of attraction that split the simulated curves.


Further developments of the simplicial contagion model based on probabilistic descriptions showed that more
complex analytical formulations, namely the microscopic Markov-chain approach [458] and the link equation [459],
can improve the accuracy of predictions [460]. Differently from the MF, these approaches can indeed be used to
analytically describe the contagion dynamics on higher-order heterogeneous structures.


_2._ _Spreading_ _on_ _hypergraphs_


In contrast with simplicial complexes, hypergraphs can be used to describe interactions that only take place in
groups, lifting the constraint of having to include all the sub-interactions within the groups themselves. Therefore,
hyperedges can efficiently be used to represent clusters or communities, when such sub-interactions are unlikely to
be relevant ingredients in the description of social HOrSs [461, 462]. Previous results on spreading dynamics on
networks have already showed the impact that the presence of clusters, communities and sub-graphs might have on
the epidemic threshold and on the final epidemic size [211, 213, 223, 463–468]. Hypergraphs have been also used to
model knowledge diffusion in collaboration networks [469–471].
The idea of modeling communities as hyperedges was first proposed by Bod´o et al. [472], who used the nodes of a
hypergraph to represent individuals and hyperedges to represent the different communities a node belongs to, such
as a household or a workplace [473–475]. The authors studied the behavior of an SIS model on hypergraphs under
a continuous time Markov chain formalism in which both infection and recovery are governed by Poisson processes.
However, while the recovery is a spontaneous process controlled by a fixed recovery rate _γ_, the rate of infection _r_
takes into account the higher-order connectivity patterns. In particular, they defined the probability for a susceptible
individual to become infected as 1 − exp(− _r_ ∆ _t_ ), with _r_ being _r_ = _τ_ ∑ _e f_ ( _ie_ ). The summation runs over all the
hyperedges -the communities- containing the susceptible individuals, while _f_ ( _ie_ ) denotes a generic function of _ie_, the
number of infected nodes in the hyperedge _e_ . Bod´o et al. chose _f_ to be a piece-wise linear function, with the idea
of not increasing the infection pressure for a susceptible node when the number of infected neighbors is higher than
a given threshold. This is conceptually different from the conventional threshold mechanism—largely exploited by
the complex contagion literature—in which thresholds are used in the opposite way, e. g., to set the critical amount
of exposures from the peers that an individual needs in order to adopt a new technology [476, 477]. Simulations
on hypergraphs having hyperedges of different sizes showed that heterogeneous structures might significantly fasten
the initial phase of the spreading when compared to regular hypergraphs, while leading to slightly smaller values of
prevalence in the stationary state.


Later, Suo et al. [478] investigated a similar SIS model on hypergraphs particularly designed to study the differences
between two different spreading strategies. In the global one, at each time step an infected node _i_ can infect with a
probability _β_ all the susceptible neighboring nodes that are connected to _i_ via a hyperedge (global). In the local one,
an infected node _i_ randomly chooses _e_, one of its hyperedges, and then tries to infect with _β_ all the susceptible nodes
composing _e_ (local). This is inspired by the different ways in which an individual might decide to share a content on
a social media platform, either to all the contacts or exclusively targeting a particular group. Notice that, differently
from the higher-order models previously introduced, here the HOrS is used as a structure, but the global contagion
dynamics does not specifically “feel” it. Hence, the global spreading strategy would in principle be equivalent to the
one defined on the 1-skeleton of the hypergraph, in which each hyperedge is a clique instead.
The two different strategies lead to different long term behaviors, with a vanishing epidemic threshold in the global
strategy. Contrarily, the particular positioning of the initial seed of infectious nodes—either on high or low hyperdegree
nodes—seems to affect only the early evolution of the process: as expected, choosing nodes with a high hyperdegree
as seeders can significantly speed up the contagion in the early times. No differences in the stationary states were
found.


The two models just presented made use of the HOrS to define the neighborhood of a node that might be responsible
for a contagion event, but no explicit mechanism of peer pressure was included in the modeling framework. Here, we
briefly discuss two following works in which, differently from before, the higher-order representation explicitly enters
into the contagion dynamics to account for reinforcement effects that might occur at the group level.


60


FIG. 30. **Behavior** **of** **the** **higher-order** **contagion** **model** **on** **scale-free** **uniform** **hypergraphs** **(** _D_ = 3 **)** **[479].** (A)
Stationary density of infected nodes against control parameter _λ_ ≡ _β_ / _µ_ for different values of the SF exponent _γ_ . For _γ_ = 2 _._ 2
and 2 _._ 4, the epidemic threshold vanishes ( _λc_ = 0), while _λc_ is finite for higher values of _γ_ . For _γ_ = 2 _._ 2 _,_ 2 _._ 4 and 2 _._ 6, the transition
is second-order, and for _γ_ = 2 _._ 6 and 2 _._ 8 the transition is hybrid. (B) Susceptibility _χ_ versus _λ_ . For _γ_ ≤ _γc_, _χ_ converges to a
finite value 1 + _d_ ( _d_ - 2). In contrast, for _γ_ - _γc_, the susceptibility diverges as _λ_ → _λ_ [+] . Figures adapted from Ref. [479].


Jhun et al. [479] extended the simplicial contagion model discussed in Sec. VII A 1 to the more general case of
hypergraphs. The SIS-like model works exactly as the one proposed by Iacopini et al. [262], but this time the spreading
process takes place on top of _d_ -uniform hypergraphs in which all the hyperedges have the same size _d_ . As for the
simplicial model, a susceptible node that is part of a hyperedge _α_ of size _d_ can get an infection from _α_, with rate _βd_, only
if the remaining _d_ −1 nodes composing _α_ are infectious. As for the recovery, the standard recovery probability _µ_ is used.
The authors considered the case of scale-free (SF) uniform hypergraphs. Notice that even if all the hyperedges have
the same size, different nodes can belong to a different number of these hyperedges. In this sense, the heterogeneity is
given by the number of hyperedges a node belongs to, which is distributed as ∼ _P_ ( _k_ ) _[γ]_ . The heterogeneous mean-field
formalism (HMF)—in which nodes of the same hyperdegree class as considered equivalent [431]—leads to the following
equation for the evolution of the stationary density of infected nodes of hyperdegree _k_ :


_dtρk_ = − _µρk_ + _βk_ (1 − _ρk_ ) _k_ Θ _[d]_ [−][1] (59)


The contagion term on the r.h.s. considers the probability that a susceptible node of hyperdegree _k_ gets the infection
from one of the hyperedges. This is, as usual, proportional to the infection rate _βk_, the number of hyperedges _k_, and
the probability Θ _[d]_ [−][1] to be connected to a hyperedge having all the other nodes infected. A comparison of Eq. (59)
with Eq. (58) highlights the difference in the representation used. Indeed, differently from the simplicial case, here
the contagion term does not dependent on the lower order sub-faces.
The resulting phase diagram of the model for a 3−uniform hypergraph is reported in Fig. 30A, where the stationary
density of infected nodes _ρ_ is plotted against the re-scaled control parameter _λ_ ≡ _β_ / _µ_ for different values of the SF
exponent _γ_ . The system presents a characteristic exponent _γc_ = 2 + 1/( _d_ - 2) of the degree distribution that determines
the nature of the transition. In particular, for _γ_ < _γc_ the epidemic threshold vanishes ( _λc_ = 0), as it is confirmed by
the finite value of the susceptibility _χ_ reported in Fig. 30B. By contrast, if _γ_ = _γc_ a second order transition appears,
that becomes hybrid when higher values of _γ_ are considered (see curves for _γ_ = 2 _._ 6 and 2 _._ 8). The associated values of
the susceptibility diverge at the transition point, as expected [480, 481]. These results are consistent with simulations
on SF uniform hypergraphs, confirming the validity of the HMF approach on such topologies.


Another version of the higher-order social contagion model on hypergraph was recently proposed by de Arruda
et al. [238]. Based on a similar SIS framework, the fundamental difference with respect to the other models relies on
the explicit inclusion of a critical-mass dynamics into the contagion process that generalizes the one in Ref. [262]. In
the simplicial contagion model previously discussed, a susceptible node _i_ belonging to hyperedge _α_ (or a simplex) of
size _d_ could get the infection from _α_ only if all the remaining _d_ - 1 nodes composing it are infected. Here, the authors
relax the constraints by (i) moving from simplicial complexes to hypergraphs and (ii) allowing a hyperedge _α_ to be
potentially infectious for _i_ ∈ _α_ if the number of infected nodes composing _α_ is greater or equal to a given threshold
Θ _α_ . The standard SIS model is then recovered by restricting this threshold mechanism to hyperedges of size greater
than two, so that a contagion through active links can always happen (no threshold). This model reveals a similar
phenomenology to the one on simplices, characterized by the appearance of first and second-order transitions and


61


FIG. 31. **SIR** **model** **on** **hypergraphs** **[486].** Ignorant (S), spreader (I), and stifler (R) nodes are respectively depicted in
blue, red, and green. At each time step a spreader can transmit the information to ignorant nodes within the same hyperedge
with a given probability. Figures adapted from Ref. [486].


hysteresis. Further insights on the conditions for the continuity of the phase transition and the stability of general
dynamical process on hypergraphs have been subsequently given in Ref. [482]. In addition, the authors provide further
analytical results on two particular regular hypergraphs, namely a hyperblob (a random regular network with one
hyperedge containing all the nodes) and a hyperstar (a star network with one hyperedge containing all the nodes).
The critical values analysis is then extended with the introduction of the concept of a “social latent” heat, interpreted
as the fraction of individuals to be added or removed to move the dynamics from one solution to the other.
These findings provide a possible phenomenological explanation for some apparently contradictory results previously
obtained. In fact, experimental work has shown different values of critical mass levels needed to initiate a social change,
i.e., to revert an existing equilibrium to a new one by mean of a committed minority [483–485]. These threshold values,
spanning from 10% to 40%, could be consistently seen as the effect of the interplay between a global critical mass and
the local thresholds as given by the Θ _α_, which also depend on the size of the interacting group.


Finally, Ma and Guo [486] introduced different extensions of the SIR model to hypergraphs. In their model, placed
within the framework of rumor spreading [487, 488], individuals are divided into the three standard classes corresponding to ignorant (S), spreader (I), and stifler nodes (R). In this particular context, the spreading process wants to
model the transmission of information between different members of an enterprise, whose internal structure is characterized by informal organizations (spontaneous groups). In particular, Ma and Guo consider different variations of the
mechanism of information transmission. Figure 31 reports an illustrative example of the probabilistic transmission,
as defined by the authors. At _t_ = 0 (Fig. 31A), all the nodes are ignorant (blue). At _t_ = 1 (Fig. 31B), the information
starts to spread, with a given probability, from a randomly selected spreader node (red) to the other nodes within the
same hyperedge. Subsequently, the rumor reaches more and more nodes while some nodes become stifler (green) and
can no longer spread the information. Other variations where the information passes to the entire hyperedge at once
or to a constant number nodes within the same hyperedge are also considered.


**B.** **Opinion** **and** **cultural** **dynamics** **beyond** **pairwise** **interactions**


In this subsection, we will review some of the best known models of opinion and cultural dynamics. At the core of
these agent-based models, often referred to as spin models in the physics literature or as interacting particle systems
in the mathematics literature, there is the idea of describing a social dynamics by relying on simple—yet sufficient—
rules. Many different variations and extensions have been proposed and extensively studied, therefore we will limit
our focus to those for which, in the spirit of this review, an higher-order extension exists.


_1._ _Voter_ _model_


With its origins deeply rooted in the statistical physics literature, the voter model is one of the simplest models of
opinion dynamics [489]. In the most basic version, it consists in a population of _N_ interacting individuals located on
the sites of a lattice, each endowed with a binary variable (spin) _σi_ = {−1 _,_ 1}, _i_ = 1 _,...N_, representing an opinion,
or a vote. The fundamental mechanism of the model relies in the node-update rule, according to which, at each
time step, a randomly selected node copies the opinion of a randomly selected neighbor (Fig. 32A). This dynamics is
iterated until one of the absorbing states of full consensus is reached. Despite its simplicity, this model presents a nonequilibrium dynamics leading to non-trivial behaviors [490]. Extending the voter dynamics from a lattice to a network


62











FIG. 32. **Voter** **dynamics** **on** **different** **structured** **populations.** (A) Node-update rule on a lattice and (B) on a network:
a randomly selected node copies the opinion of a randomly selected neighbor. (C) Link-update rule on a network: one of
the two nodes of a randomly selected edge adapts its opinion to the one of the other. (D) Hyperlink-update rule on a
hypergraph/simplicial complex: the nodes of a randomly selected simplex incident on a randomly selected edge adapt their
opinion to the one of the majority.


requires a change of perspective. Indeed, in order to maintain the average magnetization of the system, one has to
move from the aforementioned node-update rule to a link-update rule [491] (Figs. 32B,C). This is because the degree
heterogeneity potentially present in a network biases the random selection of the neighboring nodes in favor of the most
connected ones, ultimately making the “order of play” matter. As for many other dynamical processes on structured
populations, the interplay between structure and dynamics has been the focus of many studies [492]. Introducing the
many different—and sometimes multi-layered [493]—variations of the voter model and their applications [494] goes
beyond the scope of this review, therefore we now focus on the particular version that has been generalized in order
to account for higher-order interactions.


If we let the node variables take more than two values—going beyond binary opinions—we can call colors these
different opinions, and as a consequence the voter dynamics becomes a coloring _coordination_ _game_ (see Sec. VIII).
Motivated by coloring game experiments [495, 496] in which agents make informed decisions based on some local
information available, i.e., a subset of nodes, Chung and Tsiatas used hyperedges as a natural way to encode these
group interactions [497]. In their model, voters have non-pairwise relationships which are represented as hyperedges
of a hypergraph, and the dynamics obeys to the following hyperedge-update rule (Fig. 32D). At each time step a
hyperedge is selected, and the nodes composing it simultaneously change their vote according to a given probability.
In the simplest case this probability does not depend on the status of the voters at the time of the interactions. Further
insight on the process can be gained by using the duality of the process with a random walk on an associated weighted
graph whose weights encode the transition probabilities among different voting configurations. By performing this
mapping, Chung and Tsiatas were able to study the dynamics of the memoryless game in terms of the spectral
properties of the random walk.


Another prominent research topic in network science deals with the investigation of dynamical processes that
directly affects the structure of the network. This co-evolution of network structure with the dynamics that takes
place on it is particularly relevant when it comes to modeling social systems, in which the states of the nodes or
a behavioral change might force the network to react by changing its connectivity patterns. Voter models with
binary opinions have been widely extended in this direction, and many versions of adaptive voter models have been
proposed [498]. The minimal adaptive voter model on networks works as follows [499]. At each time step an edge
_e_ is randomly selected. If _e_ is inactive, i.e., it connects nodes with the same opinions, nothing happens. Contrarily,
if _e_ is active, there are two possible mechanisms, both leading to the death of this active link in favor of a inactive
one. More precisely, with probability _p_ ∈[0 _,_ 1] a rewiring happens. In this case a randomly selected node between the
two composing _e_ rewires to a random node in the network that shares its own opinion. Otherwise, with probability
1 − _p_ one of the two nodes of _e_, selected at random, adapts its opinion to the one of the other, ultimately making _e_
inactive. Recently, Horstmeyer and Kuehn have extended this model in order to account for higher-order structures,
such as simplicial complexes [500]. In their model, studied for simplicity up to the level of the 2-simplices, an edge
_e_ (1-simplex) is randomly selected. If _e_ is not part of a 2-simplex the standard rules just defined on networks apply.
Alternatively, if _e_ is active and part of at least one 2-simplex then a new mechanism of peer pressure might appear.
This is controlled via a second parameter _q_ ∈[0 _,_ 1] representing the probability of the higher-order structure affecting
the dynamics through a majority rule. When this happens, with probability _q_, one of the 2-simplices containing _e_ is
selected at random, and all its nodes adopt the opinion of the majority with probability _p_ . Similarly to the standard


63


case, with probability 1 − _p_ a rewiring happens, but this time on the 2-simplices. In particular, all the 2-simplices
containing _e_ are “downgraded” to three standard 1-simplices and an equal number of new 2-simplices is created by
randomly “promoting” triangles of the network formed solely by 1-simplices. However, this mechanism combined
with the rewiring leads to a natural depletion of 2-simplices that determines the stopping criterion for the simulations
(when there are no triangles left to “promote”). This models reduces to the standard one when _q_ = 0, while for _q_ - 0
the simplicial structure plays a relevant role on the dynamics. In this last regime, the characteristic behavior of the
adaptive voter model does not change and one can still observe a transition at a critical value _pc_ between an active
phase with a nonzero stationary density of active links and a frozen phase in which the system breaks up into two
disconnected components having opposite opinions. However, the higher-order structure has several effects on the
model dynamics. When _q_ - 0 the speed at which the dynamics reaches the two phases is increased, the critical _pc_
separating the phases is shifted towards lower values of rewiring, and the stationary density of active edges in the first
phase is lowered due to the peer pressure mechanism introduced.


_2._ _Majority_ _models_


A similar class of models is the one of the _majority_ _vote_ _models_, originally proposed by Galam [501]. In the
most basic formulation, individuals are endowed with binary state variables denoting opinions, and interact without
specific topological constraints. These models behave similarly to the voter-like models discussed above, but with one
fundamental difference in the updating rule. In fact, as the name suggests, here the copying mechanism is replaced
by a deterministic majority rule according to which, at each time step, a subset of _n_ individuals is chosen and their
opinion is set to the one of the majority within the subset. An additional bias—justified as social inertia—that
favors a particular opinion is usually introduced to resolve ties when _n_ is even. Typical quantities of interests are the
probability of reaching a particular type of consensus as a function of the initial configuration and the time required
to reach it. Many studies have been conducted in this regard by using models on lattices and graphs, highlighting
the key role played by the dimensionality of the system, together with changes in the dynamics when finite or infinite
systems are considered. In all these cases, i.e., when a structured population is used, the node-update consists in
adopting the opinion of the majority of the neighboring nodes. In this sense, the majority rule model can be seen
as a special case of a threshold model in which the threshold parameter of each node is set to half of the number of
neighbors [502].
The spatial version of the majority rule model proposed by Lanchier and Neufer [503] is based on the idea that
social groups are better defined in terms of hyperedges rather than dyadic interactions. Thus, they extended the
majority rule model on HOrSs defined as hypergraphs, so that nodes within each hyperedge simultaneously change
their opinion to the majority opinion of the hyperedge they are part of. By focusing on a particular regular social
structure, in which a hyperedge consists of a _n_ × ⋅⋅⋅× _n_ block on a lattice, they were able to show through analytical
results and simulations that, for each dimension, the model dynamics behaves similarly to the voter model when a
fixed odd number _n_ of interacting nodes is selected. This means that for hyperedges of even size _n_ the system always
reaches a consensus where all the nodes have the opinion favored by the bias, while if _n_ is odd, the system presents
growing clusters that eventually reach consensus. This is radically different from the voter model in high dimensions
( _d_ ≥ 3), in which the system reaches a stationary state in which the two opinions co-exists (see Sec. IX C).


A popular variation of the majority rule is the _majority vote model_ [489], in which a parameter _q_ ∈[0 _,_ 1] is introduced
so that a node changes its state to the one of the majority of its interacting nodes with probability (1 − _q_ ). Since _q_
controls the randomness, sometimes the model goes under the name of majority-vote model with noise, and it obeys
the following update-rule. At each time step, an individual _i_ is selected, and its opinion _σi_ is flipped with probability


⎛

_w_ ( _σi_ ) = [1] [sgn][(∑] _σj_ ) [⎞] (60)

2 ⎝ [1][ −(][1][ −] [2] _[q]_ [)] _[σ][i]_ _j_ ⎠


where the sum ∑ _j σj_ runs over all the nodes _j_ that are interacting with _i_ so that sgn(⋅) takes either the sign of the
argument or is equal to 0 in case of a lack of majority (zero sum).
Results on regular lattices show that the model undergoes an order-disorder phase transition at a critical value _qc_

[504], with critical exponents falling within the universality class of the corresponding equilibrium Ising model, with
_q_ acting as a temperature. A similar behavior was found on Erd˝os-R´enyi random graphs [505]. Contrarily, in small
world networks the position of the transition point was found to be a function of the rewiring probability [506, 507],
with critical exponents not belonging to the same universality class of the corresponding Ising model. The same holds
for directed and undirected networks with heterogeneous degree distributions _P_ ( _k_ ) ∝ _k_ [−] _[α]_ [508, 509].


Gradowski and Krawiecki extended the majority vote model to the case of hypergraphs [510]. They introduced two


64


FIG. 33. **Average** **node** **state** **for** **the** **3-body** **non-linear** **consensus** **dynamics** **with** **continuous-valued** **opinions**
**on** **a** **fully-connected** **hypergraph.** At _t_ = 0 an asymmetric opinion initialization is considered, such that _x_ ¯(0) = 0 _._ 2. The
interaction function is _s_ ( _x_ ) = exp( _λx_ ). Dotted red lines indicate the initial value of the average node state. Black and grey
solid lines represent the evolution of the state of nodes in the two initial configurations, one and zero respectively. Dashed
blue lines denote the approximated final state. (A) If _λ_ < 0 (similar node states reinforcing each other) the asymptotic average
opinion state drifts towards the majority opinion. (C) The opposite effect is observed for _λ_ - 0, where the dynamics shows a
drift towards balance. (B) When _λ_ = 0 the linear dynamics with a conserved average state is recovered. Figures adapted from
Ref. [318].


different higher-order versions, a first one based on a node-update rule and a second one based on a hyperedge-update
rule. According to the hyperedge-update dynamics, a hyperedge, representing a group, is randomly selected. The
majority is then checked within the group. With the node-update dynamics, a random node is selected at random
and then the majority rule acts on one of its hyperedges, selected at random as well. In both cases, when a hyperedge
_α_ is selected the opinions of all the nodes in _α_ are updated according to the standard rule, as in Eq. (60), but with the
sum ∑ _j σj_ running over all the nodes _j_ ∈ _α_ instead (including the node of the node-update rule). The main difference
between the two rules is in the interaction dynamics. While in the first case each node at each time step interacts with
all the other nodes in a shared group, in the second case just the nodes of a single group are considered. Obviously,
this difference becomes significant when heterogeneous structures are considered. Thus, Gradowski and Krawiecki
studied the model on SF hypergraphs having a hyperdegree distribution that follows a power law _P_ ( _k_ ) ∝ _k_ [−] _[γ]_ with
_N_
_γ_ = 1+ _N_ - _m_ [, constructed by using a growth model with preferential attachment [][292][] (see Sec.][ IV B 3][).] [Both dynamics]
present a similar behavior, with a second-order phase transition appearing at a finite critical value _qc_ . Notice that
here the transition appears even for a SF exponent 2 < _γ_ < 3, while the Ising model on SF networks presents a
phase transition at finite temperature only for _γ_ - 3 [511]. As expected, the heterogeneous structure affects the two
dynamics in different ways. In the case of the hyperedge-update, the topology does not have a strong influence on
the critical exponents, and the hyperedge dynamics locally behaves as a mean-field for the Ising model. In contrast,
when the node-update rule is considered the hypergraph topology matters, and the values of the critical exponents
strongly differ from the corresponding equilibrium Ising model on SF networks having the same _γ_ .


_3._ _Continuous_ _models_ _of_ _opinion_ _dynamics_


The different models discussed so far describe the dynamics of interacting agents having discrete opinions. This
approaches are suitable in those cases in which an individual can only have a clear and well-defined opinion on a
subject, such as in politics, where one could be for or against the introduction of a given policy or the adoption of a
given strategy. However, to model the more general dynamics of political orientation, discrete opinion variables might
be too restrictive, leaving only “black or white” polarized options. In these cases, the opinion of an individual might
be better represented by a continuous variable _xi_ ∈[0 _,_ 1] spanning between two extremes [512, 513]. Neuh¨auser et al.

[318] have investigated the effects of non-linear interactions in a model of continuous opinions dynamics on HOrSs.
Starting from the formalism of dynamical systems on networks (see Sec. V), they have proposed a generalization with
(3-body) higher-order interactions that captures the two important social mechanisms of peer pressure and homophily

[31, 514]. In their model, nodes interacts through the hyperedges of size 3 of a hypergraph. The evolution of the _N_
dynamical variables _xi_ is given by:



_N_
_x_ ˙ _i_ = ∑ _Aijk_ _s_ (∣ _xj_ - _xk_ ∣)
_j,k_ =1    - **�������������** **�������������**
Influence function




[( _xj_ - _xi_ ) + ( _xk_ - _xi_ )]

- **���������������������������������** - **���������������������������������** Linear term



(61)


65


where the adjacency tensor _Aijk_ restricts the interactions between nodes that share a hyperedge (see Sec. III A 2).
Notice that the standard linear term, denoting the influence of the two nodes _j_ and _k_ on _i_, is modulated by an
additional influence function _s_ ( _x_ ) which depends on the difference between the states of the other nodes composing
the hyperedge. According to the choice of _s_ ( _x_ ), this model can reproduce the reinforcing or inhibitory effects that
two nodes of a 2-simplex can have on the third one. For example, with a form _s_ (∣ _xj_ - _xk_ ∣) = exp( _λ_ ∣ _xj_ - _xk_ ∣) and
_λ_ < 0, similar states of _j_ and _k_ can accelerate the dynamics of _i_ (or decelerate if _λ_ - 0). As expected, if the influence
function is constant, i. e. _λ_ = 0, the standard linear case is recovered and the dynamics conserves the average state at
time _t_, typically defined as _x_ ¯ = [1] [Interestingly,] [this] [is] [not] [true] [when] [non-linear] [interactions] [are] [considered.]

_N_ [∑] _[i][ x][i]_ [(] _[t]_ [)][.]
Neuh¨auser et al. have showed that in the mean-field approach the higher-order interactions may produce a shift on
the average state of the system depending on the initial state of the nodes. In particular, for an unbalanced binary
initialization (¯ _x_ (0) ≠ 0 _._ 5) the asymptotic average state is shifted towards the majority if _λ_ < 0 (Fig. 33A) or towards
balance if _λ_ - 0 (Fig. 33C). These results are confirmed by numerical simulations on fully connected hypergraphs.
Further analyses on modular hypergraphs have highlighted the additional role played but local sub-graphs in driving
the system towards an asymmetric dynamics when non-trivial topologies are considered.


_4._ _Cultural_ _dynamics_


In the previous Section, we reviewed models that made use of scalar variables to represent evolving opinions. There
is a general agreement in calling models with such characteristics _opinion_ _models_ . A separate class of _cultural_ _models_,
originally proposed by Robert Axelrod [515], define the cultural profile of an individual as a vector rather than a
scalar. This approach, useful to model the emergence of multi-culturality, incorporates two basic mechanisms of
homophily and social influence into what is called now, unsurprisingly, the Axelrod model. In this model, individuals
interact through the links of a social network by imitating each other, that is by copying an element of the feature
vector of a neighbor. The imitation probability is proportional to the so-called _cultural_ _overlap_ among the two nodes,
which in the original model corresponds to the fraction of common cultural features. The model has been extended
to multi-layer networks, where interactions among individuals on different topics, such as religion, sport or politics,
happen on different layers [516]. This approach allows for interaction patterns that are topic specific, therefore limiting
the social influence among two individuals to the subset of features on which there is an actual social interaction (a
link in the topic layer).


Even if a “proper” extension of these model to HOrSs is still missing, HOrSs have still found their way into
these modeling approaches. For example, Maleti´c and Rajkovi´c [517] proposed to move away from the vectorial
representation of cultural features and adopt a higher-order representation instead. In this case, an opinion can be
represented as a set of interconnected judgments, so that different judgments forming an opinion represent the vertices
of a simplex. In this formulation, overlapping opinions sharing arguments or judgments correspond to simplices sharing
faces and ultimately forming a simpicial complex of opinions. This framework opens up new research directions in
which overlapping opinions can then be used to shape social interactions [518].


**VIII.** **EVOLUTIONARY** **GAMES**


Imitation is an important mechanism to model social dynamics, at the heart of many processes described in Section VII. Yet, in several cases individuals do not make decisions simply based on peer pressure and social influence [519].
In many contexts, they can set and update their behavior based on strategic choices. In biology, for instance, the selection of a specific physical trait among the many alternatives typically occurs because of the beneficial effects which
it brings to the survival of the species. Similarly, human decisions, or _dilemmas_, are frequently based on computing
and evaluating a trade-off between the positive and negative consequences of different scenarios.
Games are often studied in a simple dyadic setting, where pairs of individuals are given the chance to pursue either
a selfish strategy and defect (D), or a cooperative choice (C), with the selfish strategy being the more rewarding unless
both of them undertake it. In the most general set-up, pairwise games can be defined according to a payoff matrix:


_C_ _D_

_C_ _R_ _S_
_D_ ( _T_ _P_ [)] (62)


where _R_ is the _reward_ obtained by a cooperator playing against another cooperator, _S_ is the _sucker_ payoff received
by a cooperator when its opponent is a defector, _T_ is the _temptation_ a defector has to resist when it plays against a


66


cooperator, and _P_ is the _punishment_ that a defector receives when it plays against another defector. Games where
more than two strategies are possible, such as the rock-paper-scissors [520, 521], are not discussed in this section.
Games can be categorized into different classes, based on the relative order of the four payoffs previously introduced.
The most famous game is the prisoner’s dilemma [522, 523], where two members of a criminal gang are arrested and
isolated from each other. As each prisoner could be convicted of a small charge, but there are no sufficient evidence to
convict them for the main greater charge, both prisoners are given the opportunity to bargain, i.e. defecting by stating
that the other committed the crime, and being in exchange set free. Cooperation is harmed by a high _temptation_
_T_, as in this setting the payoff associated to defect against a cooperator yields a higher payoff than the _reward_ _R_
associated to both players cooperating and staying silent. Besides, cooperating against a defector gives the lowest
earning, typically known as _sucker_ _S_ payoff, and the payoff ordering of the game is _T_ - _R_ - _P_ - _S_ . As no defecting
player can benefit by changing strategy if the others keep theirs unchanged, this makes the decision of both players
to defect, i.e. _punishment_ _P_, the Nash equilibrium of the system, despite being a less rewarding situation than full
cooperation.
Many alternative real-life situation have been described as social dilemmas. The Stag-Hunt game describes the
dilemma of two hunters, which must cooperate to kill a stag and avoid going hungry [524, 525]. It is described by
the ordering _R_ - _T_ - _P_ - _S_, and suitable to formalize conflicts between cooperation and safety. Differently from the
prisoner’s dilemma, this game has two distinct pure Nash equilibria, full cooperation, leading to the highest payoff,
and full defection, which is risk dominant as it prevents from the risk to be the only hunter involved in the attempt
to kill the animal. The Stug-Hunt is a coordination game, as it requires the two individuals to coordinate in order to
converge towards the payoff dominant equilibrium.
Other games are described by the payoff ordering _T_  - _R_  - _S_  - _P_ . This ordering is associated to the chicken game,
where two individuals drive towards each other looking for a free way at the risk that both may die in the crash, but
hoping that the other swerves away (acting cowardly like a poultry). Outside the political sciences, the same ordering
of payoff is typically referred to as the snowdrift game. In this game, a snowdrift is blocking the way, and at least
one of two individuals has to shovel away snow to free the road. This setting describes well situations where defectors
benefit from cooperators without paying a cost for accomplishing a given task, but at least a cooperator is needed for
the task to be performed. Here the player’s optimal choice depends on what their opponent is doing, as one should
yield only if the opponent fails to. For this reason, the chicken game is an anti-coordination game [526]. It is worth
to notice that the same ordering is also associated to the hawk-dove game, where two players compete for a resource
to be shared, an outcome which is possible without damage only when two doves meet [527–529]. All these games
have two pure Nash equilibria, in which each player plays one of the pair of strategies, and the other player chooses
the opposite one.
These dilemmas were introduced as static games. Almost fifty years ago the pioneering work of John Maynard
Smith [530] first considered the dynamics of a population with repeated strategic interactions, a discipline now known
as evolutionary game theory. In the well-mixed scenario, where all agents have equal probability to interact with each
other, the evolution of the fraction of cooperators _xc_ can be tracked by the set of differential equations describing the
so-called replicator dynamics [531–534]


_x_ ˙ _c_ = _xc_ (1 − _xc_ )[ _π_ ¯ _C_                  - _π_ ¯ _D_ ] (63)


where _π_ ¯ _C_ is the average pay-off of a cooperator, and _π_ ¯ _D_ the average pay-off of a defector. The replicator equations
are also widely used to model species interactions, as we will discuss in Section IX C.
Numerically, the dynamics of games are often studied as agent-based models [535]. The importance of numerical
simulations, in particular in the case of agents placed on a network, is also linked to the limitations achieved by
analytical methods. A first approach is the so-called best response, where individuals choose the strategy which
produces the best outcome for them taking the strategies of the other players as given. However, more complex
update processes are often considered, where players can update their strategy by imitating the behavior of the most
successful individuals, where the higher copying probability the larger the difference in earnings. This allows to
consider more realistic scenarios, where agents can also make mistakes.
For the prisoner’s dilemma, in well-mixed population (where at each round individuals have the same probability
to play with any other agent in the population) the evolutionary dynamics brings the system into a state of full
defection [532]. This is in spite of the low payoff associated to the outcome, a situation sometimes referred to as
the tragedy of the commons [536]. However, when populations are structured, meaning that interactions between
agents—often limited by spatial constrains—can be described by a network of relationships, cooperators are able to
emerge even in adverse settings. First discovered by Nowak and May by placing agents at the nodes of a simple square
lattice, repeated games between the same pairs of individuals allow for _network_ _reciprocity_, i.e. the creation of robust
mutual interactions based on trust, even if the temptation to defect would prove to be more rewarding in a single
individual round [537]. Graphs which are heavy-tailed [538, 539] or clustered [540] provide the best conditions for


67







**B**


















|Col1|a|b|Col4|Col5|
|---|---|---|---|---|
|c|d|e|f||
|h|i|j|k|l|
|m|n|o|p||
||q|r|||



FIG. 34. **Traditional** **graph** **implementation** **of** **a** **multiplayer** **game.** At each elementary step a player _i_ and one of its
neighbors _j_ are chosen at random. Each individual accumulates earnings by playing all games in which it is involved, namely
the game in which it is the focal individual of the group, and the _k_ games where it participates in a group centered on one of
its neighbors. All groups in which _i_ and _j_ participate are listed in panels (A) and (C), for a simple two-dimensional lattice (B).
Finally, _i_ compares its payoff to that of _j_, updating its strategy by imitating the strategy of the neighbor with a probability
which depends on the relative difference of the payoff. The presence of links among neighbors of _i_ and _j_ (clustering) does not
affect the definition of the groups.


the emergence of cooperation, exploiting the beneficial effect of prosocial hubs and the presence of tightly connected
communities to sustain the formation of trust among players.
In the snowdrift game the relative values of the sucker payoff and punishment are inverted, as a lone cooperative
shoveler still has a better cost benefit ratio than an individual in a pair where both agents defect. This appearently
small difference generates the emergence of a stable state with coexisting cooperators and defectors in structuredless
population, differently from the prisoner’s dilemma [532]. Surprisingly, spatial structures were shown to be detrimental
for cooperation in the snowdrift game [541].
In the last 15 years the fields of evolutionary game theory and network science have become significantly closer, and
we are now witnessing an explosion of contributions at the boundary of these topics [542–544]. In the following of this
Section, going beyond the traditional pairwise scheme, we provide an overview of the main results on evolutionary
games in networks with group and higher-order interactions.


**A.** **Multiplayer** **games** **on** **networks**


_1._ _Public_ _goods_ _game_


Many dilemmas do not involve pairs of individuals, but occur at the level of groups. This is the case of taxes for
welfare state, which are beneficial from an individual perspective only if most individuals are willing to contribute. The
public goods game is the paradigmatic game to describe social dilemmas in the case of group interactions [545–548],
and it is considered the generalization of the prisoner’s dilemma to _N_ - 2 players. In the most simple implementation,
players, belonging to a group of size G, are asked to contribute to a common pool. Cooperators contribute with a
token _t_ whereas defectors do not contribute at all. The tokens are then multiplied by a synergy factors _R_, with _R_ < _G_,
and shared evenly across the population no matter the strategy of the agents. For this reason, if we indicate with _Nc_
the number of cooperators in the group, cooperators earn a payoff _πc_ = _t_ ( _NcR_ / _G_ - 1), whereas defectors obtain _πd_ =
_t_ ( _NcR_ / _G_ ). To simplify the payoffs and without loss of generality, _t_ can be set equal to 1. The game is fully controlled
by the effective parameter _r_ = _R_ / _G_, which is known as the reduced synergy factor. The traditional implementation of
a multiplayer game on a graph is illustrated in Fig. 34. As explained later on, different implementations are necessary
if one wants to explicitly take into account the real pattern of higher-order interactions among individuals.
Similarly to the prisoner’s dilemma, the network structure affects the emergence of cooperation also in the public
goods game [538, 549]. Simulations on lattices first showed that structured interactions sustain cooperation for
values of the synergy factor well below the critical condition _R_ = _G_ [550, 551]. Yet, interest in the public goods
game sparked when more realistic network structures with heterogeneous degree distributions were considered [552].
In heterogeneous networks, at every round each agent is involved in _k_ + 1 games (where _k_ is the degree of each
node), meaning that hubs play significantly more games than agents placed on poorly connected vertices. In the


68


implementation known as _fixed_ _cost_ _per_ _game_, in particular, ( _k_ + 1) is also the total contribution of each agent after a
full round. Because of this inequality, another set-up has also been widely investigated, where each agent has a _fixed_
_cost_ _per_ _individual_ _t_, and hence each game contributes to its total payoff as 1/( _k_ + 1). Fixed costs per individual are
considered a suitable setting to model cumulative costs, such as in the case of taxes, while fixed costs per individual
are best suited to model a scenario in which the resource associated to the cost is finite, and it is equally distributed
among players. In scale-free networks cooperation was found to be significantly enhanced through network reciprocity
if cooperators pay a fixed cost per individual, whereas the same effect is reduced when prosocial individuals pay a
fixed cost per game [538]. The enhanced cooperation of the first scenario is due to the disproportionately higher
payoff obtained by those agents participating in a very large amount of groups.


The beneficial effect from interacting according to a scale-free networks can be lost if the underlying structure is
characterized by positive degree-degree correlation, reducing the evolutionary advantages of individuals with highdegree who decide to cooperate [553]. Similarly to pairwise games, tight community structure and clustering can
sustain positive feedback and the survival of cooperators for low values of the synergy factor also in the public goods
game [554]. Prosocial behavior may be further promoted by allowing heterogeneous contributions, for instance by
making them proportional to the cooperation of each group [555, 556]. However, interestingly, increasing group size
does not always lead to the dynamics of well-mixed populations in such a multiplayer game [557].


Multiplayer games are considered to be inherently different from the corresponding pairwise games, as the emergent
collective behavior in the case of group interactions might be different [558]. This is rooted in the formation of indirect
links between players who belong to the same group but are actually disconnected. As an important consequence
of this, the details of the local topology of the network of interactions for multiplayer games are often irrelevant for
the final outcome, as discussed in Ref.[559]. Besides, multiplayer games also show qualitatively different evolutionary
dynamics, giving rise to new forms of self-criticality which have not been observed in pairwise games [560]. Among
those, we report the emergence of new temporal and spatial patterns of dominance, such as the so-called indirect
territorial competition, first reported in a modified public goods game in Ref. [561].


More recently, the role of multiplexity has also been taken into account. In this setting, different layers are associated
to different games (different values of the synergy factor) and individuals may have different neighbors depending
on the layer. While not making possible direct strategy exchanges between the networks, interconnectedness can
affect the utility function of players, who do not have access to the earnings of their neighbors on each of the
layers but only to a (possibly non-linear) combination of them [562]. Interestingly, this simple payoff coupling was
shown to further enhance cooperation in the whole system, through a mechanism dubbed _interdependent_ _network_
_reciprocity_ [563]. Despite the presence of the same synergy factors at different layers, the system naturally self-organizes
into a configuration where one layer is more cooperative than the others through spontaneous symmetry breaking [563].
However, interdependent network reciprocity is not a universal properties of all interconnected systems, but strongly
depends on the structure of the layers. In particular, interdependent network reciprocity is proportional to the fraction
of edges shared by the different layers (i.e. edge overlap [564]), and the beneficial effects of multiplexity completely
disappear when the overlap between the network structures goes to zero, no matter the number of layers [565]. In
this detrimental configuration, cooperators can appear in the system only if the synergy factors of all layers are at
least as high as the critical conditions associated to each network in isolation [565]. Further coverage on the effects of
multiplexity and network interdependence on evolutionary games is provided in Ref. [544].


Much attention has also been devoted to the case of coevolutionary games, where the structure of the networks of
social interactions may change over time as a result of the outcome of the strategic interactions among players [535].
When individuals can alter the connections in their social network in response to unsatisfactory interactions, coevolution between cooperation and spatial organization in the public goods game naturally leads to increased social
cohesion [566] and prosocial behavior [567]. A different setting is considered in Ref. [568], where a survival cost parameter is introduced, and agents with low payoff are replaced in the games by new random players. With this mechanism,
cooperation emerges if the synergy factor is higher than the average degree, and the population self-organizes into
a scale-free network of interactions, naturally more beneficial to sustain prosocial behavior. Finally, coevolutionary
rules have been implemented in the case of interdependent network of players, leading to complex social structures
where strong inter-layer links were promoted around agents performing the best [569].


As most of these results rely on numerical simulations, it is important to highlight the importance of proper
simulations practices. An important contribution to the topic is found in Ref. [570], which investigates the stability
of observations from agent-based model simulations going beyond traditional finite-size scaling, or on the role of
noise [571]. In particular, only a complete stability analysis of all subsystems solutions (solutions that are formed
by a subset of all possible individual strategies) can be explicitly linked to the existence of a phase transition in the
thermodynamic limit in multiplayer games where competing strategies are more than two. For a complete review on
the public goods game on networks, we refer the interested reader to the work by Perc et al. “Evolutionary dynamics
of group interactions on structured populations: A review” [547].


69



**A** **B**

a


b


c


d


e







FIG. 35. **Public** **goods** **game** **on** **bipartite** **graphs.** Information on the exact group structure encoded in a bipartite network
(A) is lost when its one-mode projection is considered, where two individuals are directly linked if they both participate in at
least one group (B) . Cooperation is enhanced when the game is played by considering the real group structure instead of the
projected graph, both for the fixed cost per game (C) and fixed cost per individual (D) implementation. Prosocial behavior is
greater when fixed costs per individual are considered. Figures (C) and (D) reproduced from Ref. [582].


_2._ _Other_ _multiplayer_ _games_


The public goods game is not the only multiplayer game whose evolutionary dynamics has been studied on graphs.
An interesting alternative is the generalized multiplayer snowdrift game, where individuals receive a benefit _b_ if the
task is performed by one or more agents belonging to their same group, no matter their strategy [572]. In this game
cooperators share the workload and have a payoff _πc_ = _b_ - _c_ / _Nc_, while defectors have a payoff _πd_ = _b_ as long as there
is at least a cooperator in the group, otherwise _πd_ = 0. In well-mixed populations cooperation decreases with high
cost-to-benefit ratio, as well as a function of the number of agents in a group [572]. When network structures are
considered, the introduction of an underlying homogeneous graph steadily promotes prosocial behaviors, similarly to
the corresponding game played on well-mixed populations. By contrast, heterogeneous networks typically generate
multiple new internal equilibria [573]. The introduction in the game of dynamical grouping, where agents are placed
in groups of different sizes at different times, and players of different strategies are dynamically mixed was found to
greatly enhance prosocial behavior [574]. A common modification of the traditional multiplayer snowdrift games links
the benefit of accomplishing a task to the existence of a minimum threshold of cooperative individuals [575–577].
Despite its peculiarity, the game is sometimes considered as a particular type of public goods game.
More recently, a generalization of the hawk-dove game to multiple interacting players was proposed [578]. In
particular, whereas in the corresponding pairwise settings the game is considered equivalent to the snowdrift game,
this is not true when interactions occur between groups of players. In particular, while in the snowdrift game the
accomplishment of the task benefits all individuals, in the hawk-dove problem only strategists of a particular kind
(hawks) benefit from the shared resource, excluding the opponent type (dove) from the distribution, unless a sufficiently
high number of cooperative doves is present in the group. The emerging evolutionary dynamics is very rich: different
scenarios associated to dominating hawks, coexistence, bi-stability, multiple interior equilibria and dominating doves
can be obtained as a function of the dynamical parameters describing the resource to be shared, cost and minimum
number of doves in a group for prosocial individuals to benefit.
The games discussed so far are multiplayer generalizations of pairwise dilemmas described by the payoff matrix in
Eq. (62). It is worth to mention that also different families of pairwise games have been investigated in the setting of
wider group interactions. An example is that of the ultimatum game, where two players, one acting as a proposer and
one as a receiver of an offer, bargain to split a sum of money [579, 580]. In the multiplayer case, offers can have an
arbitrary number of receivers, who can reject or accept the proposal individually. Similarly to a threshold model [476],
the offer is accepted and shared equally among responders only if the number of individual acceptances is above a
given threshold. The game is significantly affected by the value of this parameter, with higher values associated to
more generous and fair outcomes [581].


**B.** **Games** **with** **higher-order** **interactions**


_1._ _Public_ _goods_ _game_ _on_ _bipartite_ _networks_


Networked implementations of multiplayer games discussed so far lack control on the real higher-order structure of
interactions. For instance, a scale-free degree distribution _P_ ( _k_ ) ∼ _k_ [−] _[γ]_ generates a similarly heavy-tailed distribution


70


of group sizes _P_ ( _G_ ). This is not a realistic feature of many real social networks, such as collaboration networks, where
individuals tend to collaborate together in fairly small groups of homogeneous size [275].
Motivated by this finding, in Ref. [582] G´omez-Garde˜nes et al. studied the public goods game on an empirical
bipartite network of scientific collaborations, where the two sets of nodes describe respectively scientists and papers.
The authors compare the results with what obtained by implementing the game on the corresponding one-mode
projection, acting as a null-model, where scientists who co-authored at least a paper are linked together, as shown in
Figs. 35A,B. The main finding is that—no matter the details of the updating rule for the evolutionary dynamics—
cooperation is systematically enhanced by considering the real higher-order structure described by the bipartite
network. This is due to the interplay between the heterogeneous distributions of the number of games in which each
player is involved, and the homogeneous distribution of the groups. Taken together, these two features allow for the
existence of a fairly high number of agents with high payoff involved in small groups, making this scenario responsible
for further promoting prosocial behavior.
Enhanced cooperation with respect to the one-mode projection is observed consistently in both settings of fixed
cost per game (Fig. 35C) and fixed cost per individual (Fig. 35D): the degree of cooperation is always greater when
fixed costs per individual are considered rather than fixed costs per game, consistently with what found for classical
monopartite networks, though the differences are now smaller. The boost in cooperation for fixed cost per individual
is linked to the long tail in the distribution of degrees and number of games. However, this effect is mitigated when the
real structure is considered. This can be understood by considering the agents who participate in a single collaboration,
whose contribution is the same in the bipartite network both for fixed cost per individual and fixed cost per game
scenarios, while this is not the same in the projected one-mode network where a node in general participates in _k_ + 1
groups. Interestingly, the authors remark that the final cost per individual is a better setting to model collaborations,
where researchers have a limited amount of time to be shared among parallel projects, and where those involved in
only a few collaborations tend to take most of the workload. Finally, increasing the number of members of a group
leads to a decrease of the level of cooperation in a population.
In a following work, G´omez-Garde˜nes et al. deepen their investigations of higher-order structure by studying the
effect of bipartite networks which have groups of the same sizes, but where the number of groups in which which
a player can participate is a tunable parameter [583]. Surprisingly, the average level of cooperation achieved with
homogeneous connectivity is remarkably larger than that for scale-free substrates. This finding indicates that the
ability of scale-free networks to outperform the promotion of cooperators in homogeneous structures, first discussed
in Ref. [538], is not directly linked to the fat-tail in the distributions of number of games per player. At difference,
instead, it rather depends on the entanglement of social and group heterogeneities which is unavoidable in the onemode projection. Further analyses on the impact of different distributions for group sizes and the number of individual
contacts reveal the importance of overlap between groups for cooperation, similarly to the role of clustering on onemode projected networks [584].
An interesting modification of the game considers the possibility that information on the earnings is shared between
groups. This can be done by introducing an effective payoff, where the normal payoff associated to a member playing
in a group is combined with the earnings of the same agents from the other groups in which it participates. The
strength of this second term can be tuned with a parameter _α_, which describes the degree of cross-information
among groups. Interestingly, information exchange is positively correlated with an enhancement of the cooperation
in the system [585]. The positive effect induced by cross-information is analogous to that of interdependent network
reciprocity for multiplex networks, where individual payoffs are aggregated across the layers of the system.


_2._ _Public_ _goods_ _game_ _on_ _hypergraphs_


Recently, Alvarez-Rodriguez et al. introduced a new formalism to describe the evolutionary dynamics of higherorder interactions [586]. In this set up, groups of individuals are described by the hyperlinks of a hypergraph, making
explicit the lift of interaction networks to the case of non-dyadic interactions. The Monte Carlo implementation of
the dynamic is illustrated in Figs. 36A-C. In the manuscript, the authors finally normalize the payoffs by the number
of played games, in an implementation reminiscent of the fixed cost per game scenario. The update process is also
modified, and _i_ imitates the strategy of its best performing neighbor _k_ with a probability which depends on the
difference _πi_ - _πk_ .
The stable state achieved from the evolutionary dynamics is first studied on uniform random hypergraphs, where
all players are involved in the same number of hyperlinks of equal size, _G_ = 2 _,...,_ 5. Figure 37A shows the fraction
of cooperators _xc_ as a function of the reduced synergy factor _r_, where the hyperdegree of each node is the minimum
one to guarantee a connected hypergraph. As shown, the presence of larger groups promotes the onset of cooperation
in more adverse conditions described by a low value of _r_ . When density increases—no matter the group size—the
hypergraph implementation of the public goods game converges to the limit of well-mixed population, as shown in


71





**B**



































FIG. 36. **Hypergraph** **implementation** **of** **strategic** **group** **interactions.** (A) At each time step, a node _i_ is chosen
randomly, and one of the hyperlinks to which it participates is selected. (B) All the members of the hyperlink play a game for
each of the hyperlinks they are part of, and (C) accumulate payoffs accordingly.


Fig. 37B. Besides, the relaxation time _T_ of the dynamics can be computed with good analytical accuracy with a
mean-field approach.

The introduced formalism also allows for an analytical treatment of heterogeneous random hypergraphs, where
nodes participate in groups of different order with a weight described by a probability distribution. For simplicity,
the authors focus on heterogeneous hypergraphs with a different frequency of groups _fG_ of order from 2 to 5 and
∑ _G fG_ = 1, giving rise to 35 different hypergraphs classes. In this set-up, it is interesting to investigate the collective
outcome of the game in scenarios where larger or smaller collaborations can be more or less effective. These different
conditions are easily described by setting the synergy factor _R_ to be a function of the group size _G_, i.e.


_R_ ( _G_ ) = _αG_ _[β]_ _,_ (64)


where _α_ - 0 and _β_ ≥ 0 and different from 1. The emergence of cooperation is in general affected by both parameters _α_
and _β_ . In the particular case _β_ = 1, all classes of hypergraphs show the same behavior as a function of _α_ (Fig. 37C).
This is not true for different values of the exponent, such as _β_ = 2 (Fig. 37D). Besides, the average relaxation time _T_
of the dynamics as a function of the critical point _αc_ for the emergence of cooperation scales linearly with _α_ if _β_ ≠ 1.
Interestingly, while a degeneracy is observed for _β_ ≤ 1, this is broken for the superlinear case. This means that it
is possible to exploit this additional degree of freedom by choosing an adequate hypergraph to set independently a
chosen critical point and relaxation time.

Finally, the authors considered several datasets describing synergies and group tasks in the real-world. By imagining that these collaborations—ideally described by a public goods game—evolved over time to produce an optimal
hypergraph structure and that a coordination cost is added to sustain too large collaborations, they inferred the ideal
synergy factor associated to prosocial behavior. As an example, results for collaborations among physicists publishing
in different journals of the American Physical Society are shown in Fig. 37E). Journals in experimental and applied
physics typically have an optimal synergy factor for larger values of the group size _G_ .

To conclude, even more than for the dynamical processes considered in Sections (5-7), the landscape of HOrSs in the
field of social dilemmas is still widely unexplored. In the future, we foresee that an explicit treatment of higher-order
interactions could be applied to the many games discussed in Section (VIII A 2), as well as others such as the naming
game [587, 588], the sender-receiver game [589–591], or problems of collective risk [592].


**IX.** **APPLICATIONS**


Non-pairwise interactions are common in various types of systems in the real world. Important examples include
group interactions in both offline and online social networks [46, 593, 594], multi-authors scientific collaborations [96],
network motifs in transcription networks [595] and trigenic interactions in gene regulatory networks [596], beyond
pairwise mechanisms of species coexistence in ecological communities [14], and higher-order correlations in neuronal

[597] and whole-brain functional patterns [598, 599]. In this section, we present a selection of some of the possible
applications of HorSs in fields spanning from social sciences to neuroscience and biology.


72


FIG. 37. **Cooperation** **in** **the** **public** **goods** **game** **on** **hypergraphs.** (A) Average fraction of cooperators as a function of
the reduced synergy factor _r_ for homogeneous hypergraphs with interactions of different order _g_ . (B) Critical value _rc_ for the
emergence of cooperation as a function of the density of the hypergraphs _L_ / _Lc_, where _Lc_ is the critical number of hyperlinks
for a connected hypergraphs, for different values of _g_ . Classes of 35 different heterogeneous hypergraphs H with hyperlinks
of orders _g_ = {2 _,_ 3 _,_ 4 _,_ 5} are considered. The synergy factor _R_ ( _α, β_ ) scales according to Eq.(64). Results for two values of the
exponent, _β_ = 1 (C) and _β_ = 2 (D), are shown. (E) Dependency of synergy factors from hypergraphs describing co-authored
publications in journals of the American Physical Society assuming the collaboration process is optimal. Figures reproduced
from Ref. [586].


**A.** **Social** **systems**


Social scientists have realized since long time the importance of hypergraphs and simplicial complexes to describe
and study affiliation data [46]. _Affiliation_ _networks_, also known as _membership_ _networks_, are a special kind of twomode social networks representing the affiliation of a set of _n_ actors to a set of _m_ events, or social occasions. As an
example, Fig. 38A shows the bipartite network of the attendance of _n_ = 6 children to _m_ = 3 birthday parties. This
system can be naturally described as a hypergraph whose nodes are the children and the hyperedges are the set of
events (panel b). Notice that the data can be represented equally well by the dual hypergraph, obtained by reversing
the roles of nodes and edges (panel c). In this latter case the three nodes are the three parties, while each child is a
hyperdegree.


The literature on applications of hypergraphs and simplicial complexes in the social sciences is vast. We will then
limit our survey to the pioneering works and to some recent results. Ref. [600] presents one of the earliest use of
hypergraphs to investigate affiliation to voluntary organizations. The work focuses on the issue of sampling and
proposes estimators for the number and size distribution of organizations in cities, the density of relations among
individuals generated by organizations, and the amount of membership overlap among organizations. Such estimators
are then applied to data from a sample of individuals in different towns of the state of Nebraska. Results show that,
while the mean affiliation rate does not systematically vary from city to city, the number of inter-organizational links


**A**


Party 1


Party 2


Party 3



Allison


Drew


Eliot


Keith


Ross


Sarah



**B**





**C**





Party 2















73









FIG. 38. **Affiliation** **network** **of** **six** **children** **and** **three** **parties.** The interactions are shown respectively as a bipartite
network actor-events, as the hypergraph with the six children as the nodes, and as the dual hypergraph with the three parties
as the nodes. Figures adapted from Ref. [46]

.


per organization increases with the size of the city. Hypergraphs have also been used to capture the characteristic
fluidity of urban social structures arising from collections of overlapping subsets such as voluntary associations, ethnic
groups, action sets, and quasi-groups [601], and to study participation of Thai households to ritual celebrations [602].
Ref. [603] discusses the conceptualization, measurement, and interpretation of centrality in affiliation networks.
The main underlying assumption is that, in an affiliation network, also the events can acquire and transmit centrality.
Ref. [108] shows how centrality can be adapted to HOrSs and can turn very useful to capture important properties
of real-world systems. The measures proposed in this work are extensions of the Bonacich eigenvector centrality

[103, 107, 604] to the case of hypergraphs (see also Section III B). The basic idea is simple. Let _I_ be the incidence
matrix of a hypergraph. If we indicate as vectors _x_ and _y_ the centrality scores for the rows and columns, representing
the hyperedges and the nodes of the hypergraph respectively, we can write that: _I_ _[T]_ _x_ = _λy_ and _Iy_ = _λx_, which
means assuming that individuals acquire their centrality by attending important events, and important events are
attended by central individuals. The vectors _x_ and _y_ are then eigenvectors of two different matrices, although both
are associated with the same eigenvalue _λ_ [2] :


_II_ _[T]_ _x_ = _λ_ [2] _x_ _I_ _[T]_ _Iy_ = _λ_ [2] _y_ (65)


The final outcome is a measure of centrality for events, as well as an improved measure of centrality for actors.
The authors of the paper show an application to study data describing 56 attacks on European settlements occurred
between the years 1509 and 1700 and involving Caraibe from 22 different islands. Such data require a description
considering more-than-dyadic interaction, as attacks could involve more than two islands at the same time.


Simplices and simplicial complexes provide an alternative way to describe and study membership networks using
methods from algebraic topology. This approach draws heavily on the pioneering ideas of Ron Atkin [19, 605] and on
his _q-analysis_, which makes use of a geometric interpretation of the relationships between actors and events. Atkin’s
framework to study social systems is based on a fundamental distinction between what he calls the “backcloth” of
social action, namely the structure of ties among the events, and the “traffic” of social activities that can take place
over the backcloth, such as the formation of pairwise acquaintanceship between actors. The backcloth is a simplicial
complex and the q-analysis is designed to describe the patterns of relations among its constituents.
To give a concrete example, we will discuss here an application of Atkin’s framework to study the formation of
friendship in a scientific community against the backcloth of shared contacts [593]. In his analysis of friendship among
a set of 29 social science researchers, Linton Freeman looked at 19 linking events corresponding to scientists been
located in the same university department at the same time, or having attended conferences together. Each person
is then represented as a simplex of the linking events in which has been involved. 25 of the 29 persons participated
at least to one of the 19 events, with 13 of them involved in only one event. These persons are 0-simplices, but
there are also six 1-simplices (pairs of events), and four 2-simplices (persons involved in three linking events). The
highest order simplices found are two 3-dimensional tetrahedrons. These simplices form the building blocks for the
construction of a backcloth for social action. The basic idea is that conferences and universities provide the perfect
setting in which friendships between academics can be developed. Therefore to understand the formation of social ties
it is important to analyze how the simplices are intertwined into a larger structure, i.e. into a simplicial complex. The
simplicial complex corresponding to the system under study is shown in Fig.39A. The linking events are the nodes
of the simplicial complex and are labeled with a number from 1 to 19. The persons are instead indicated with the
symbols _P_ 1 − _P_ 29 and can either be represented as nodes, links, or higher order objects. Notice the two tetrahedrons


74


FIG. 39. **Early** **simplicial** **representation** **of** **interactions** **among** **social** **science** **researchers.** (A) Simplicial complex
showing the pattern of links between social science researchers, _P_ 1- _P_ 29, through shared linking events, nodes 1-19, indicating
participation to events or affiliation to university departments. (B) Table showing the q-analysis of the simplicial complex.
The first column is the dimension of components made up of chains of simplices. The second column is the number of chains
at each level, while the third column reports the names of the simplices making up each chain. Figure and table reproduced
from Ref. [593]

.


respectively corresponding to persons _P_ 13 = {11 _,_ 13 _,_ 15 _,_ 16} and _P_ 3 = {2 _,_ 8 _,_ 9 _,_ 19}. These are the highest-order simplices
present in the simplicial complex, which can then be well represented in three dimensions. Two persons can share
one or more common linking events. For instance, person _P_ 20 is linked at dimension 0 to person _P_ 4 since they have
only a node (event 3) in common. Person _P_ 13 and _P_ 21 are instead linked by two events (nodes 8 and 9). Hence they
are 1-connected, as they are glued together by a 1-dimensional line (the edge 8-9). What matter are not only direct
connections between simplices, but also chains of connections. For instance, the three simplices _P_ 4, _P_ 9 and _P_ 20 are
linked in a chain of connection of order 0, as _P_ 4 is 0-connected to _P_ 20, and _P_ 20 is 0-connected to _P_ 9. Instead _P_ 13,
_P_ 9 and _P_ 20 are in the same 1-connected component. Atkin’s q-analysis describes the sets of chains of connection and
their dimensions. The table in Fig.39B tells us that there are three components at dimension 0, with the largest one
containing 21 of the 25 persons. Moreover, there are nine components at dimension 1: the largest one made by _P_ 13,
_P_ 9 and _P_ 20, the second one by _P_ 2 and _P_ 28, and seven isolated 1-dimensional simplices (edges). No connections (of any
type) are instead observed among simplices of dimension larger than 1. Another interesting feature of the simplicial
complex is the existence of a 0-dimensional _q_ -hole (akin to a _H_ 1 cycle, see Section III D) involving the four persons
_P_ 9, _P_ 11, _P_ 13 and _P_ 20 and shown as a shaded area in Fig. 39A. This corresponds to a cycle of four nodes only pairwise
connected and is an indication of an obstruction to the free flow of social traffic on the backcloth. The main purpose
of Freeman was to correlate the formation of personal friendships to the structure of the backcloth. He had data of
12 close mutual friendships reported by the 29 researchers. And he was indeed able to show that the structure of the
backcloth constrains the choice of personal friends. In fact, none of the 12 existing social links was among the pairs
prohibited by the obstructions in the backcloth. Moreover, 11 of these 12 pairs were among the 31 adjacent pairs
which are 0-adjacent in the backcloth.
A similar application of q-analysis to study the evolution of social groups has been published by Patrick Doreian
in the same years [606]. Doreian had data on the participation of 18 women in 14 events through time, and used
q-connectivity to trace the group structure over time. His primary objective was to investigate conflict within the
group and eventually predict the observed split of the group of women into two subgroups. Differently from Ref.[593],
the approach here is dynamic: the q-connectivity analysis is applied to an enlarging set of of successive events in time.
Although, on the one hand, the work confirmed that algebraic topological approaches are flexible enough to provide
a description of structural changes, on the other hand the results showed that the data used were not rich enough to
explain the observed changes. This also pointed to the importance of collecting high-resolution temporal data [12].
Certainly one of the most original applications of simplicial complexes to social networks is the structural analysis of
a team sport presented in Ref.[607]. In their work, Gould and Gatrell used Atkin’s q-analysis to define and characterize


75


intuitive notions of structure in a soccer match. They focused on the England FA Cup Final between Liverpool and
Manchester United played on 21 May 1977 at Wembley Stadium, London. Although commentators generally rated
the play of Liverpool as superior, Manchester United won the match by 2 goals to 1. The authors considered the
22 players and defined a relation in this set using a variable threshold on the number of times the ball passed from
one player to another. Then they examined the internal structure of the two teams separately, and also the relations
between the two sets of players, defined by the loss of the ball by one team to the other. The analysis is able to show
the relevance and role of different players and group of players. The results also indicate that the injection of q-holes
by the defense of the Manchester United, created an obstruction to the free flow, contributing to the fragmentation
and loss of the Liverpool. It could be very instructive to apply and validate this type of analysis on a larger scale,
now that soccer analytics is attracting increasing interest and detailed data on all the spatio-temporal events (passes,
shots, fouls, etc.) occurring during a match are available for entire seasons and different soccer competitions [608].
More recently, simplicial complexes have also been used to investigate online social networks [594, 609] and social
resource sharing systems [610]. For instance, the authors of Ref. [594] have assessed the role of an individual in
MySpace computing what they name the node structure vector, which allows to characterize the topological space
around a node. This is defined, for a node _i_, as the vector **Q** _[i]_ = { _Q_ _[i]_ 0 _[,Q][i]_ 1 _[,...,Q][i]_ _d_ max [}] [whose] _[d]_ [max] [+][ 1] [components]
denote respectively the generalized node degree _kd,_ 0( _i_ ) of order _d_ introduced in Section III B, i.e. the number of
_d_ -dimensional simplices, with _d_ = 0 _,_ 1 _,...,q_ max, to which node _i_ participates, and _d_ max is the dimension of the largest
simplex in the complex. The study of the simplicial node degree _k_ ( _i_ ) = ∑ _[d]_ _d_ [max] =0 _[Q]_ _d_ _[i]_ [= ∑] _[d]_ _d_ = [max] 0 _[k][d,]_ [0][(] _[i]_ [)][,] [also] [known] [as] [the]
node topological dimension, provides a good measure of the social capital of the corresponding individual. In fact, it
has been found that the so called Simmelian brokerage [611], which quantifies a node’s ability to act as a broker in
a community, scales as a power of the node topological dimension. Moreover, the analysis of the components of the
node vector over the different social layers and communities of MySpace reveals that influential individuals connects
higher-order simplices and build their social capital by combining their connections in different layers.


Authorship of scientific articles is a particularly interesting type of affiliation networks, as it provides important
insights on patterns of collaboration within the academic community. In this case, the two sets of nodes represent
scientists and their publications, respectively. The basic units of scientific collaborations and of the social network
of acquaintances among scientists are co-authored publications, which often involve groups of authors rather than
just two [612, 613]. Hence, in their study on the “shape of scientific collaborations”, the authors of Ref. [96] have
proposed to complement the results that have been obtained by methods of network analysis [614–616] with an
approach based on a simplicial description of scientific publications and on the use of tools from algebraic topology.
They have considered all the papers posted on the arXiv, a repository of electronic preprints spanning from physics to
quantitative biology and mathematical finance, in the period 2007-2016, and have constructed 18 different simplicial
complexes, one for each of the different categories of arXiv. Each paper with _k_ authors corresponds to a ( _k_ - 1)simplex, and only papers with author sets not fully contained in the author sets of other papers have been retained
in the construction of the simplicial complexes in order to preserve their basic structural properties. Both the size
distribution of facets (maximal simplices, see Section II) _P_ ( _s_ ) and the simplicial node degree distributions _P_ ( _d_ ) of
the complexes display broad tails, indicating the presence of large collaborations and of authors with a large number
of different collaborations, respectively. The 18 different categories can then be grouped in only two large classes
based on their _P_ ( _d_ ), showing that the number of collaborations to which an author is able to participate is quite
well conserved across fields. Also, all the 1-dimensional homological cycles, i.e. the two-dimensional holes bounded
by edges, of the various co-authorship simplicial complexes have been studied. In particular, focusing on the shortest
possible cycles, triangles, and counting how many of the set of three edges arranged in a triangle are covered by
a full triangle (2-simplex), allows to investigate the concept of simplicial closure (the extension of triadic closure to
simplicial complexes [617]) in the data. Results indicate the presence of very strong simplicial closure for all categories
of arXiv, meaning that in the great majority of cases whenever three authors have collaborated in pairs, they also
have collaborated on a paper together. An application to collaboration networks of a similar extension to hypergraphs
of the concept of clustering coefficient, and of that of subgraph centrality can be found in Ref. [101].


**B.** **Neuroscience** **and** **brain** **networks**


Lively debated over the last decade, the question of whether high-order correlations –in addition to the basic
pairwise interactions– were needed to properly account for brain function was met with strong evidence of a positive
answer. Using higher-order connected correlation functions [597], Schneidman et al. [618] revealed that high-order
correlations exist in neural populations. Similarly, Ganmor et al. [619] and Yu et al. [620] provided evidence that
introducing higher-order interactions between neurons allowed to improve the predictions at mesoscopic scales, e.g.
for cortical dynamics such as neuronal avalanches in the awake monkeys or visual responses in the anesthetized


76





















40


30


20


10



>1(>)















0

edge density ?











FIG. 40. **Topology** **of** **hyppocampal** **cells’** **activations** **encodes** **geometrical** **information** **about** **the** **environment.**
(A) an example of construction of order complex from a full correlation matrix. At each step the order complex (top row)
encodes the topology of the density-filtered correlation graph (bottom row). (B) Betti curves of the pairwise correlation matrix
for the activity of N = 88 place cells in hippocampus during open-field spatial exploration. (C) The same Betti curves from B
(bold lines) shown overlaid on the mean Betti curves from random geometric complexes (top) and from complexes built from
shuffled correlation matrices (bottom). Note the differences in when Betti numbers emerge in the case of random geometric
complexes and in the magnitude itself for shuffled weight complexes. Figures adapted from Ref [625].


cats. More recently, further research in neural spike trains provided methods to measure the strengths of multi-spike
interactions [621], and showed their importance in shaping the dynamics of cortical columns [622] and in population
coding [623, 624].


The models used to estimate higher-order interactions in the cases mentioned above are usually tailored after the
generalized Ising model [618]. In these models, the probability of observing a pattern of firing neurons ( _σ_ 0 _,σ_ 1 _,...,σn_ )
is given by


_P_ ( _σ_ 0 _,σ_ 1 _,...,σn_ ) = [1] _αiσi_ + ∑ _βijσiσj_ + ∑ _γijkσiσjσk_ + _..._ [⎞] (66)

_Z_ [exp] ⎝ [⎛][∑] _i_ _i_ < _j_ _i_ < _j_ < _k_ ⎠


where _α,β,γ,..._ control the self-, pairwise- and third-order interactions among firing units. These models, while very
powerful, have several limitations. First, they are designed for systems with discrete states. Neurons are usually
considered to be firing or quiescent so are well described by Ising spins, which take values ±1. Conversely, continuous
data (e.g. local field potentials, EEG or BOLD signals) need to be binarized to be amenable to this type of analysis,
and this can represent an important problem when we want to deal with macroscopic brain networks. Second,
and more importantly, these models neglect the information encoded in the spatial and temporal structure of the
interactions. Third, their scalability to large networks is made more complicated by the requirement of large amounts
of data (e.g. long timeseries) to estimate model parameters.


Against this context, Giusti et al. [625] studied how the correlations of spike trains can be used to detect intrinsic
structures in neural activity, without recurring to external stimuli or receptive fields, and how they relate to the
topology and geometry of the animal’s space. In particular, they computed pairwise correlations from the crosscorrelograms of pyramidal neurons in freely roaming mice. Each correlation matrix was then transformed into an
order complex. This is a filtration of simplicial complexes, obtained in their stead from a sequence of progressively
denser graphs. At each density, only the strongest edges until the fixed density were retained. In such a way, for each
density a binary graph was built and the corresponding clique complex computed, that is, in each graph all the cliques
were considered as simplices (Fig. 40A). Giusti et al. [625] then compared the Betti curves of the real order complex
with those obtained from randomized versions, which were built by reshuffling the original correlation matrices. They
found that the Betti curves, which encode the topological complexity of the cell activation patterns, displayed consistently lower values than those from the randomized models. These observations implied that the correlation structure
of hippocampal neurons intrinsically represented the low dimensional input space (a two-dimensional roaming space
in this case).


These results confirmed previous evidence on the role of hippocampal place cells in encoding primarily a space’s
topological qualities rather than its geometry [626, 627], but also showed that some coarse geometrical information can
be encoded in the fabric of correlations. Even more interestingly, Babichev et al. [628] extended previous hypotheses


77


FIG. 41. **The** **structure** **of** **coactivation** **complexes.** (A) Simulated place field map _M_ ( _ϵ_ ) of a small planar environment
_ϵ_ with a hole in the center. The series of snapshots illustrates the temporal dynamics of the coactivity complex: the complex
goes from being from small and fragmented, in the early part of the exploration, to becoming a stable representation of the
shape of the underlying environment. (B) The timelines, encoded as barcodes, of topological persistent _H_ 0 and _H_ 1 cycles
in the coactivity simplicial complex: 0-dimensional persistent generators are shown in light-blue lines, 1-dimensional ones in
light-green. Most loops correspond to accidental, short-lasting structures, effectively representing noise in the complex. The
persistent topological loops (marked by red dots) represent physical features of the environment. The time to eliminate the
spurious cycles can be used as a theoretical estimate of the minimal time needed to learn the path connectivity of _ϵ_ . (C)
Simplices can also disappear, and hence the coactivity complex may be flickering, instead of stable. (D) The timelines of the
topological cycles in such complex may remain interrupted by opening and closing topological gaps produced by decays and
reinstatements of its simplices. Figures reproduced from Ref. [628].


on the topological nature of the hippocampal map [626, 627] to account for the temporal nature of interactions
among place cells. Indeed, the mammalian hippocampus is thought to be able to learn an internalized cognitive map
representing the ambient space. It is however unclear how such a map is conserved in time and updated due to the
transient nature of synaptic connections and of the downstream neuronal networks. To investigate this mechanism,
Babichev et al. [628] represented the instantaneous state of the internalized map as a coactivity complex, in which
simplices represent groups of coactive place cells. At the beginning only few groups of place cells, hence simplices,
are present. In time however by accumulation of activity, the coactivity complex should approximate the topology
of the underlying space in which the animal moves. An open question however is how it is possible to preserve a
consistent representation of a space while the animal is moving, place cells are constantly remapping and in general the
population coding fluctuates. Studying the robustness of the topological features of coactivity complexes, Babichev
et al. [628] strongly suggested that the temporal stability of the hippocampal map is a generic phenomenon stemming
from a compensatory mechanism in which neuronal activity compensates deterioration in the network structure to
preserve hippocampal function.
Reimann et al. [629] investigated the topology of excitation networks built from simulated activity on reconstructed
cortical micro-circuitry. They found that different stimuli elicited a surprisingly large number of high-dimensional
directed cliques and created a wide variety of high-dimensional homological holes. In particular, simulations on a
variety of synthetic and null models did not display such an array of topological responses, suggesting these topological
metrics do not emerge from traditional constraints on graph structure (e.g. degree sequences, clustering, etc..), but
rather from particular species-specific coordination among links. Moreover, they observed also that, in response to
sensory stimuli, pairwise correlations grew with the number and order of the simplices to which the neurons belonged,
suggesting that the hierarchy in physical structure results in hierarchically correlated activities.


At the macroscopic brain network level, the question of the importance (or lack thereof) of higher-order interactions
appears less settled. On the one hand, for example, Huang et al. [630] suggested that weak higher order interactions
might indeed be present in macroscopic functional networks, but also that, due their weakness, pairwise interactions
are dominant in shaping brain activities, hence justifying functional connectivity descriptions based on pairwise
interactions alone. On the other hand instead, higher order features were shown to be reliable under test-retest
analysis [631], and important as indicators of aberrant connectivity in mental disorders [632] and mild cognitive
impairment [633]. Also, higher order interactions were useful in the inference of the parameters of coupled oscillator
models of EEG signals (for example [425]), which we discussed in more detail in VI C.
Recent seminal research has shown the potential and impact of topological approaches, in particular those inspired


78


by topological data analysis. Structurally, persistent homology techniques were adopted to describe and discriminate
healthy and pathological states in developmental [634] and neurodegenerative diseases [635]. Sizemore et al. [636]
described the white matter network of fibers between brain regions as a weighted network and then studied both
its dense portions, in terms of cliques, and its cavities, in terms of homology. They found that large cliques are
much more frequent than expected in an appropriate randomized model built using biologically-inspired principles of
parsimonious wiring (Fig. 42A). These cliques were interpreted as local dense units able to perform rapid processing,
and were found to be positioned around topological cavities, which in turn acted as obstructions and guides for the
information flows. These cavities were also reproducible across subjects and appeared to connect regions belonging
to different phases of brain evolutionary history (Fig. 42B). Similarly, Bendich et al. [637] described the morphology
of brain arteries using topological observables. In particular, using persistent homology of trees, they characterized
arterial morphology using the structure of branching and looping of vessels at multiple scales, and found distinctly
different patterns at different ages.
Topological differences have been also found at both population and individual levels in functional connectivity in
healthy and pathological subjects [638, 639]. Higher dimensional topological features have been employed to detect
differences in brain functional configurations in neuropsychiatric disorders and altered states of consciousness relative
to controls [598, 640], and to characterize intrinsic geometric structures in neural correlations[625, 641].
As an example, Petri et al. [598] compared the topology of the functional connectivity of subjects that had been
subministrated with psilocybin, a psychedelic drug, with their own under placebo. They found that the topological
structure of the two conditions was very different and such difference could be quantified already at the level of persistence diagrams (Fig. 42C). While the difference between topological summaries. obtained from persistent homology,
was already discernible, it provided little information on how topological information mapped back to the underlying
brain regions. The authors solved this problem by defining a topological backbone, called _scaffold_, built on approximated minimal homological generators (Fig. 42D), which allowed them to show that altered states of consciousness
induced by psilocybin (and likely, other psychedelics) stem from very different patterns of information integration and
importance of the brain regions [642] with respect to the normal state (Fig. 42E). Other examples can be found in
the following series of works. Lee et al. [639] have proposed methods to discriminate between cohorts of children with
attention deficit hyperactivity disorder, autism spectrum disorder and pediatric control subjects on the basis of their
functional topology. Lee et al. [643] instead represented the topological substructure of brain networks through the
eigenvectors of the corresponding Hodge Laplacians and used it to discriminate between mild and progressive cognitive impairments, and Alzheimers disease. Chung et al. [644] described the heritability of differences in whole-brain
functional topology in a cohort of twins. Ib´a˜nez-Marcelo et al. [599] related the topological functional structure of
EEG data during imagery to functional equivalence in a population of skilled versus unskilled imagers [645].


Going beyond functional connectivity, Saggar et al. [646] constructed a simplified topological backbone representation of the full fMRI activation space and showed that the properties of these backbones associated with behavioral
performance in a series of cognitive tasks. In the context of event-related fMRI, Ellis et al. [647] investigated the
feasibility of topological techniques for recovering signal representations from BOLD signals. In particular, they embedded specific signal configurations by a convolution of the signal with the hemodynamic response, showing that the
persistent homology was able to recover the signal topology with high accuracy.
Finally, moving from neuroimaging to applications in cognitive neuroscience, Sizemore et al. [305] mapped the evolution of early semantic networks in toddlers by identifying words with nodes and considering higher order interactions
among them. They found that sparse regions of the resulting HOrSs displayed remarkable similarities at the topological level across subjects, and the timing of their disappearance was more closely to the patterns of connections among
words than to their actual semantic content, thus suggesting that knowledge acquisition might generally happen via
filling knowledge gaps. For an extended review of the current research on the effects of non-pairwise interactions in
neuroscience, we refer the reader to the following references [74, 648, 649].


**C.** **Ecology**


Higher-order interactions have been studied for decades in the context of ecological models [650–652]. However,
only very recently it has been highlighted their crucial role for the stability of large ecological communities and for
the remarkable biodiversity observed in nature. While pairwise interactions in ecology consider the direct effect,
either positive or negative, of a species on another, as shown in Fig. 43A, high-order interactions include all the cases
where the relation between two species can be modified by the presence of other species, which may also be not
directly affecting the former [653, 654]. For instance, this happens when there is a microbial species that produces an
antibiotic to interfere with a competing species, and a third species produces an enzyme which degrades the antibiotic
thus reducing the strength of the interaction among the other two [655]. This is illustrated in Fig. 43B, where species


79


FIG. 42. **Persistent** **homology** **of** **structural** **and** **functional** **brain** **connectivity.** (A) Distribution of maximal cliques
in the average DSI (black) and individual minimally wired (gray) networks, thresholded at an edge density of _ρ_ = 0.25. Heat
maps of node participation shown on the brain surfaces for a range of clique degrees equal to 4-6 (left), 8-10 (middle), and
12-16 (right). (B) Minimal cycles representing each persistent cavity at the density at birth represented in the brain (top)
and as a schematic (bottom) (adapted from [636]).. (C) Comparison of persistence p and birth b distributions. Left, H1
generators persistence distributions for the placebo group and psilocybin group. Right, distributions of homology cycles’
births. (D) Statistical features of group homological scaffolds. Left, probability distributions for the edge weights in the
persistence homological scaffolds (main plot) and the frequency homological scaffolds (inset). Right, scatter plot of the scaffold
edge frequency versus total persistence for both placebo and psilocybin scaffolds. (E) Simplified visualization of the persistence
homological scaffolds for subjects injected with placebo (left) and with psilocybin (right). Colours represent communities
obtained by modularity optimization on the placebo scaffold and display the departure of the psilocybin connectivity structure
from the placebo baseline. Figures adapted from Ref. [598].


1 inhibits species 2, and species 3 produces the enzyme that reduces the direct inhibitory effect of species 1 on species
2. Such a mechanism gives rise to a so-called “trait-mediated indirect interactions” (TMIIs) between species 3 and
2, which is different from a possible direct pairwise interaction between 3 and 2 (also reported in the figure), being
intrinsically a three-species interactions. As finally shown in Fig. 43C, the enzyme produced by species 3 can in turn
can be inhibited by a compound introduced by a species 4, creating a four-species inseparable/entwined interaction,
and so on [656–658]. Similar effects can also arise from an adaptive behavior, for instance a predator which changes
its target prey because another prey becomes available [659]. In this case there is no direct interaction between the
two preys but they are part of a hyper-interaction, and considering only pairwise interactions would not allow to
correctly take into account this effect.
Analyses of ecological networks almost often omit non-pairwise interactions, many classes of which are instead
fundamental to the structure, the function and the resilience of ecosystems. It has been shown that the class of threespecies interactions in which one of the three species has the effect of mitigating the negative interaction between
the other two can have a stabilizing effect [656], while it has been found that increasing the order of the interactions
reduces the fraction of extinct species [660] and increases the variance of species abundances at equilibrium [661].
The literature is growing and many scientists have shown that higher-order interactions can have a stabilizing effect
under many particular condition settings.


It has been shown that hypergraphs can be a very useful mathematical framework to represent and take into ac

80


and 2. Figures adapted from Ref. [655].


FIG. 44. **Hypergraph** **description** **of** **the** **coffee** **agroecosystem** **in** **southern** **Mexico** **[663].** Nodes in (A) represent
the different agricultural pests, while lines indicate indicate direct effects (black), modifications of direct effects (blue), and
modifications of those modifications (red). Key interactions (B) among four nodes of the system, namely Phorid, Azteca, Scale
and Beetle (Azya orbigera), are represented in the form of a hypergraph whose hyperedges (C-G) and incidence and adjacency
matrices are reported in right panel. Figures adapted from Ref. [663].


count non-pairwise ecological interactions, such as TMIIs [101, 662, 663]. As an illustrative example of the value of
hypergraphs in describing ecological communities, the authors of Ref. [663] have studied a real-world coffee agroecosystem in southern Mexico, in which resistance to agricultural pests depends upon a large number of TMIIs. Based
on field studies, they have assembled the intricate web of interactions among agricultural pests that is reported in
Fig. 44A. Black arrows indicate direct effects, while blue and red arrows represent modifications of those direct effects,
and modifications of those modifications, respectively. In particular, some protective effects attributable to TMIIs
imposed by ants of the genus Azteca (blue lines from node Azteca), some of which are further modified by antparasitizing phorid flies (three red lines from node Phorid), have been shown to be crucial for controlling agricultural
pests. Interactions within this system can be well represented by an hypergraph. The hypergraph corresponding to
key interactions involving the four nodes Phorid, Azteca, Scale and Beetle (Azya orbigera) is reported in Figs. 44B-G,
together with its adjacency and incidence matrices. Notice that positive and negative direct effects, or strengthening
and weakening TMIIs are respectively indicated by triangular and circular arrow-heads in the interaction web in the
left panel. However, this information has been omitted to produce the simpler case of an undirected system shown in
(B). Direct effects represented as black lines in (B), and corresponding to the three edge of the hypergraph, include
beetles preying on scale insects (C), Azteca ants consuming energy from Scales (D), and Phorid flies parasitizing
Azteca ants (E). Indirect effects, consisting of Azteca ants reducing the magnitude of the interaction between Scale


81


and Beetle [dashed blue line in (B)], and Phorid flies reducing the magnitude of the effect of Azteca ants on the
Scale-Beetle interaction [dashed red line in ()B)], are instead represented as the two hyperedges reported in (F) and
(G), respectively. This example immediately illustrates the straightforward way in which hyperedges can represent
TMIIs. The authors of Ref. [663] further elaborate on how the analysis of hypergraph topology, and concepts such
as shortest hyperpaths and hypergraph centrality measures, can turn very useful for studying important aspects of
ecological systems (such as how a species is affected by the removal of other species from the system) that a network
description only based on pairwise interactions alone can fail to faithfully represent.


Bairey et al. have investigated the stabilizing role of higher-order interactions in replicator equations [655]. They
have proposed a mathematical model based on random replicator dynamics to study ecosystems when both pairwise
and higher-order interactions are present. An ecosystem is described at each time by its state _**x**_ = ( _x_ 1 _,x_ 2 _,...,xN_ ),
where _xi_ ≡ _xi_ ( _t_ ) denotes the abundance of species _i_ at time _t_, with the physical constraint ∑ _i xi_ ( _t_ ) = 1∀ _t_ . The
temporal evolution of the abundances are governed by the following set of differential equations:


_N_
_x_ ˙ _i_ = _xi_ [ _fi_ ( _**x**_ ) − ∑ _xjfj_ ( _**x**_ )] _i_ = 1 _,...,N_ (67)
_j_ =1


in the usual form of replicator dynamics [531–534], already introduced in Section VIII to model the evolutionary
dynamics of strategic interactions. The first term in bracket, _fi_ represents the fitness of species _i_, which depends on
the effect of the other species through the system state _**x**_, while the second term is the average population fitness.
The key point is that the fitness function here adopted:



_N_ _N_
_fi_ ( _**x**_ ) = − _xi_ + ∑ _aijxj_ + ∑
_j_ =1 _j_ =1



_N_ _N_
∑ _bijkxjxk_ + ∑
_k_ =1 _j_ =1



_N_

∑
_k_ =1



_N_
∑ _cijklxjxk_ + _..._ (68)
_l_ =1



includes pairwise but also higher-order interactions. Entry _aij_ of matrix _A_ determines the effect of species _j_ on
species _i_ . Three-dimensional (or third-order) tensor _B_ rules three-species interactions, with the value of the entry
_bijk_ determining the joint effect of species _j_ and _k_ on species _i_, and so on with the four-dimensional tensor _C_, etc.
Notice that the negative sign of the first term, − _xi_, implies the stability of the system when interactions are turned off
(species are self-limiting in high concentrations). Limiting the analysis to hyper-interactions not involving more than
four species, random perturbations of different order to a stable ecosystem are then modeled by setting _A_ = ~~[√]~~ _αA_ [˜],
_B_ = ~~[√]~~ _βB_ [˜] and _C_ = ~~[√]~~ _γC_ [˜] . Here _A_ [˜], _B_ [˜] and _C_ [˜] are a random matrix (a two-dimensional tensor), and a random threedimensional and four-dimensional tensors respectively. The elements of _A_ [˜], _B_ [˜] and _C_ [˜] can either be positive or negative
and are drawn from a Gaussian distribution with mean 0 and variance 1. The important parameters of the model are
then the values of _α_, _β_ and _γ_, which represent the strength of the pairwise, three-species and four-species interactions,
respectively. As expected, in a system with only pairwise interactions ( _β_ = 0, _γ_ = 0), species exhibit extinctions when
the strength _α_ is larger than a critical value, and such value decreases with the system diversity, i.e. with the number
of species _N_ . Reported in Fig. 45A is the threshold _αc_ at which coexistence is lost in 5% of the simulations. When
the number of species _N_ is increased, the critical threshold _αc_ decreases as 1/ _N_, in agreement with the result by
May [664]. The situation changes when higher order interactions are considered. In particular, if only three-species
interactions are present ( _α_ = 0, _γ_ = 0), then the value of the critical strength _βc_ is not affected by the number
of species. Conversely, if only four-species interactions are considered, the threshold _γc_ increases with the system
diversity. This is a striking result: for a fixed strength of four-species interactions, an ecosystem is stabilized, rather
than destabilized, as the number species increases. Thus, while pairwise interactions introduce a higher bound on
diversity, a lower bound is instead created by high-order interactions. Or in other words while ecological communities
with a large number of species become sensitive to pairwise interactions, communities with a small number of species
are sensitive to high-order interactions.
Bairey et al. have also considered the more interesting “mixed case” in which a combination of the three types of
interactions can be present at the same time. The resulting stability region for three different sizes _N_ of the system
is graphically represented in Fig. 45B. in the space ( _γ_, _α_ ) of pairwise and four-species interaction strengths, in the
case of no three-species interactions, i.e. assuming _β_ = 0. Notice that there is a small area where an ecosystem with
_N_ = 8 species is feasible, while systems of both sizes _N_ = 5 and _N_ = 15 are unstable. Since it is plausible that, in the
most general case, an ecosystem is characterized by interactions of different orders and by a set of values ( _α,β,γ,..._ )
for the corresponding strengths, this will imply the existence of both a lower and upper bound for the number of
species, for which Bairey et al. provide an analytical estimation. They also found that, if the total strength _α_ + _β_ + _γ_
is increased, then upper and lower bounds get closer, restricting the range of allowed diversity of the ecosystem.


Grilli et al. [28] have instead studied the role of high-order interactions in a model of interacting competitors [665–
668]. Although the proposed framework is quite general, the model describes the dynamics of a forest with a large but


82


FIG. 45. **Dynamical** **effects** **of** **higher-order** **interactions** **in** **ecological** **systems.** (A) Critical strength of interactions
in the Bairey et al. [655] model in Eq. (67) and (68) beyond which the coexistence of species is lost as a function of the number
of species _N_ . The three curves represent the case of only pairwise, three-species and four-species interactions, respectively. (B)
Regions of stability for ecosystems with _N_ = 5 _,_ 8 and 18 species in the ( _γ_, _α_ ) space (assuming _β_ = 0). (C) Temporal evolution
of the abundances of five different species as given by the Grilli et al.[28] model for the competition matrix _H_ reported in the
five node graph, and when only pairwise interactions are considered. (D) Same as in the previous panel, but with sampling
three seedlings at a time instead of two. Figures adapted from Ref. [28] and Ref. [655].


fixed number of trees, in which _N_ different species of trees compete for space. As in the case of the model by Bairey
et al., the state of the system is described by the vector **x** ( _t_ ), i.e. by the proportion _xi_ ( _t_ ) of trees of each species _i_ at
time _t_, with ∑ _i xi_ ( _t_ ) = 1 ∀ _t_ . The dynamics stems from the fact that at each time step a tree, selected at random (with
all the species having the same death rate), dies leaving an empty space in the canopy, which can be filled by a new
tree. That is when the competition among seedlings begins. The simplest way to model this mechanism is through a
pairwise competition: two species are randomly selected and the winner of the competition will fill the gap. Pairwise
competitions are characterized by matrix _H_ whose entry _hij_ represents the winning probability of species _i_ on species
_j_ . In particular, Grilli et al. considers the most general case of a matrix of randomly generated positive numbers
between 0 and 1, with _hij_ + _hji_ = 1, which represents an extension of previous works [669, 670]. The dynamics of the
_N_ species is ruled by the following set of differential equation:



_N_
∑ _pijxj_ (69)
_j_ =1



_x_ ˙ _i_ = − _xi_ + 2 _xi_



_N_
∑ _hijxj_ = _xi_
_j_ =1



where the negative terms − _xi_ describes the death process, while the positive term 2 _xi_ ∑ _j hijxj_ gives the probability of
selecting two seedlings of species _i_ and _j_, with _i_ winning the competition. Notice that the competition process can be
seen as a game [671, 672], and the right hand side of the equation can be rewritten in the form of a replicator equation
for a zero-sum, symmetric matrix game with two players, where the payoffs _pij_ are the entries of the skew-symmetric
payoff matrix _P_ = _H_ - _H_ _[T]_ [673, 674], similar to the payoff matrix introduced in Eq. in Sec. VIII. Independently from
the initial conditions **x** [∗] (0), after an initial transient, Eq. (69) drives the system to a state where some of the _N_
species go extinct, while the remaining ones cycle around a unique equilibrium point **x** [∗] . This is shown for a case with
_N_ = 5 and a particular random choice of matrix _H_ in Fig. 45C. By changing _H_ the model can lead to arbitrarily many
species coexisting, and can generate any possible species-abundance distribution empirically observed. However, the


83


neutral cycling around the equilibrium is problematic, as such cycles are not observed in nature. In addition to this,
the main issue with the model is that the equilibrium is highly unrobust: any deviation from perfectly identical death
rates destabilizes the dynamics and leads to just one species surviving. Grilli et al. have shown that the problem can
be solved by going beyond the pairwise interactions and considering the simultaneous competition among more than
two species when a new empty space appears in the canopy. They propose an extension of the model in Eq. (69)
where three seedlings are picked at random, the first competes with the second and the winner with the third. The
equations now read:



_N_
∑ (2 _hijhik_ + _hijhjk_ + _hikhkj_ ) _xjxk_ = _xi_
_k_ =1



_N_

∑
_j_ =1



_N_
∑ _pijkxjxk_ (70)
_k_ =1



_x_ ˙ _i_ = − _xi_ + _xi_



_N_

∑
_j_ =1



where _hijhik_ is the probability that _i_ beats both _j_ and _k_, _hijhjk_ is the probability that first _j_ beats _k_, and then
_i_ beats _j_, and _hikhkj_ is the probability that _k_ beats _j_, and then _i_ beats _k_ . Also in this case the equations can
be rewritten in the form of a replicator dynamics for a three-player game with a three-dimensional payoff tensor
_P_ whose entry _pijk_ = 2 _hijhik_ - _hjihjk_ - _hkihkj_ gives the payoff of the first player 1 playing strategy _i_ when player
2 plays _j_ and player 3 plays _k_ . Surprisingly, the evolution of this new model leads to globally stable fixed points
instead of cycles. As shown in Fig. 45D for the same matrix _H_ as in Fig. 45C, the system converges to a fixed point
characterized by the same vector _x_ [∗] that was the center of the oscillation in the model with only pairwise interactions.
In addition to this, the fixed point is now globally stable. Hence, sampling three seedlings at a time instead of two
produces stability in a system of competitors. The same authors have also proven that the inclusion of fourth- or
higher-order terms does not change the equilibrium but simply accelerates the convergence to it. Moreover, when
transforming this deterministic. model into a stochastic one, the presence of higher-order interactions delays the
extinction time, allowing a prolonged coexistence of species. Summing up, the model in Eq. (70) clearly indicates
that the inclusion of higher-order interactions in competitive networks stabilizes dynamics, making species coexistence
robust to perturbations.


Mayfield et al. [675] have pointed out the role of high-order interactions to another important aspect, that of
estimating the values of fitness in ecological models. They have shown that it is quite difficult to explain the empirically
observed fitness outcomes by considering only pairwise interactions. The inclusion of higher-order interactions, defined
as changes to the interactions between two species mediated through a third species, can instead improve the ability
to perform such an estimation.


Very recently, Valverde et al [676] have applied a HOrS framework to the analysis of environmentally mediated hostpathogen infections. The hyperlinks of a hypergraph are used to depict three-way associations between plants (hosts),
viruses (pathogens), and different habitats. Projecting this information, it is possible to study the interactions between
viruses and different host ecotypes, explicitly including the spatial context in which host-pathogen interactions take
place. By building a neutral model for the evolution of hostpathogen networks across multiple habitats, the study
showed that real ecosystems live in a continuum between nested and modular networks, going beyond the traditional
dichotomy between modularity and nestedness in ecological networks [677]. The model has been empirically validated
by the analysis of different ecosystems in an agricultural landscape in Spain.


For a more complete review of the current research on the effects of non pairwise interactions on the mechanisms to
maintain biodiversity in ecological systems we refer the reader to the review “Beyond pairwise mechanisms of species
coexistence in complex communities” by Levine et al. [14].


**D.** **Other** **biological** **systems**


Over the last decades network science has become an established framework to describe and understand interactions
between biological agents, including proteins, metabolites and genes [678–680]. Yet, the complexity of biological
processes can only rarely be decomposed as a sum of pairwise interactions. For instance, metabolic reactions often
involve multiple partners, and proteins typically interact with each other in small groups known as complexes. As
a consequence, traditional pairwise approaches, which neglect the presence of higher-order structures, are at risk of
oversimplify the complexity of biological systems.
Among the first higher-order analyses in biology were studies showing that the hypergraphs corresponding to
mammalian protein complexes [681] had a scale-free distributions of both node degrees and hyperedge sizes [682]. The
full potential of using HOrS frameworks, in particular hypergraphs, to characterize complex biological processes taking
place in biomolecular systems, was already clear more than ten years ago [683]. An important range of applications


84


FIG. 46. **Different** **representations** **of** **biological** **signaling** **pathways.** In the simplest representation, a signaling pathway
is simply a set of proteins, with no additional information. Networks can only capture pairwise interactions between proteins.
Hypergraphs naturally encode multilateral interactions and reactions. Figure reproduced from Ref. [684].


FIG. 47. **Hypergraphlet** **representation** **of** **local** **connectivity** **patterns** **in** **hypergraphs.** Complete illustration of the
65 orbits associated to hypergraphlets of order 1, 2 and 3. More than 6000 orbits are associated to hypergraphlets of order 4,
and more than a hundred thousands to hypergraphlets of order 5. Figure reproduced from Ref. [685].


is that of signaling pathways in cell biology, where group of molecules have to work together to efficiently control cell
functions, such as death or division [684]. Different representations of signaling pathways are summarized in Fig. 46.
Gaudelet et al. [685] have investigated protein interaction hypergraphs by extending the concept of graphlets [686],
to the case of higher-order networks. Hypergraphlets were defined as small induced sub-hypergraphs of a given large
hypergraph, and an orbit identifies each different set of automorphic nodes. An example of all the hypergraphlets of
1, 2 and 3 nodes is illustrated in Fig. 47. Similarly to motifs [53], hypergraphlets allow to characterize wiring patterns
of higher-order networks at the local scale. By focusing on the case of yeast and human pathways, the authors showed
that modeling protein interactions as hypergraphs allows for better functional predictions than a description in terms
of graphs with pairwise interaction only.
Franzese et al. [687] have challenged the current approaches to molecular connectivity, which they found either too
permissive or too restrictive. As an alternative, they have proposed an intermediate optimal solution that interpolates
between graph and hypergraph approaches and allows to better capture the importance of small molecules involved in
many distinct reactions. More recently, Klimm et al. [688] have used hypergraphs to investigate multiprotein complex
data, showing how a pairwise (network) projection produces a hierarchical structure, that is instead not observed
when polyadic interactions are considered. After comparing the protein complexes with appropriate null models,
the authors found that larger complexes tend to be more essential, with a hyperdegree that better correlates with
gene-essentiality information than the standard graph degree. All these results suggest the importance of considering
the inherent higher-order structure of protein complexes to reveal complementary information.
Redundancy is an important property of biological systems that guarantees their functionality in the case of misfunctioning of some local components. Pearcy et al. [689] have used hypergraph percolation to assess the robustness of


85


empirical bacterial metabolic higher-order system to random failures. In particular, they have used site percolation,
in which a hyperedge (describing a reaction) is activated only when all metabolites involved in the hyperedge are
active. Results showed that interacting systems that have evolved in environments with a higher degree of variability
are more robust, and that, similarly to their simple network counterparts, also metabolic hypergraphs are characterized by the presence of a core-periphery structure. In another study, metabolic networks have been characterized by
the spectrum of a symmetric tensor associated to their hypergraph connectivity, successfully capturing the chemical
information of enzymes and structural changes of compounds to define novel classes of functional reactions [690].
Other higher-order topological operators such as combinatorial Laplacians (see Section III E 2) were shown to provide
a more complete characterization of chemical reaction networks [691].
The complexity of biological systems entails that the data we obtain from experiments are often incomplete or
characterized by a limited accuracy. For this reason, various works have concentrated on the problem of reconstructing
the hypergraphs associated to different kinds of cellular processes where higher-order interactions are at play [692–695].
Recently, higher-order inference frameworks have also been extended to deal with dynamic correlations of abundance
levels of genes, transcripts and metabolites changing over time. The results provide a better picture of the global
dynamic correlation patterns of the investigated biological systems [696].
Higher-order interactions have also revealed key when designing effective drug combinations to prevent or contrast
diseases. Indeed, in multiple cases, from cancer to tuberculosis, the combined action of the ingredients of a so-called
drug cocktail, even when administered at a low dose, has been shown to be more beneficial than that of single drugs
in isolation. Recently, the dose model has been developed as an efficient tool to discover effective drug combinations
based on pairwise interactions [697]. While the dose model was originally tested only on triplets and quadruplets
of antibiotics, as well as triplets of cancer drugs, very recently the model was shown to successfully predict effective
combinations of up to ten drugs used for E. coli and the M. tuberculosis pathogen [698]. However, when noise in the
dataset is more important, prediction of higher-order interactions based on pairs of drugs is less efficient [699]. Notice
that alternative approaches to detect effective drug cocktails are available, such as the so-called pairs model, which
was shown to be more noise-resistant but less precise [700].
Related to both robustness and drug resistance, the feedbacks between the different levels of genetic information
shape to a large degree the link between genotype and phenotype [701, 702]. A relevant example is that of epistasis,
which Weinreich et al. [703] have defined as “the surprise at the phenotype when mutations are combined, given the
constituent mutations individual effects”. In other words, epistasis describes the somewhat surprising observation that
the effects of multiple individual mutations appear to interact with each other in ways that cannot be quantitatively
reduced to sums of pairwise interactions [704]. While the concept of higher order epistasis is not new [705], only
recently it has become possible to start a quantitative analysis of its effects in different contexts [706]. For example,
Guerrero et al. [707] have investigated how protein quality control machinery influenced the epistasis in traits related
to bacterial antibiotic resistance, separating the mutations affecting an essential bacterial enzyme from species-specific
effects. Yitbarek et al. [708] have explored higher-order interactions among gut taxa and their effects on host infection
risk, using a theoretical model tailored to the type of data that might be empirically collected in the near future.
Mickalide and Kuehn [709] have studied a controlled microbial trophic chain and detected an increased invasion
resistance of the community, stemming not from resource allocation but from high-order interactions between its
species.
Finally, dynamical processes have been recently used to extract information on the structure of higher-order biological networks. For instance, Niu et al. [710] have considered a microbe-disease hypergraph, where nodes are microbes
and diseases are hyperedges. A higher-order random walk (see Section V B) was shown to have a greater accuracy in
the prediction of disease-microbe associations compared to that of traditional random walks.


**X.** **OUTLOOK** **AND** **CONCLUSIONS**


In this review, we have discussed ways and methods to detect, represent, measure and model systems with higherorder interactions, and we have illustrated models of higher-order systems substantially differ both structurally and
dynamically from traditional pairwise models.
We have seen time and time again that there are crucial conceptual differences between modeling pairwise and
higher-order interactions. For example, we have seen that higher-order interactions typically lead to new sources of
non-linearity in the systems under study, which are not present in standard network approaches. Further, considering
objects richer than links opens up new possibilities and questions: for example, state variables can now be defined
not only on nodes, as in standard practices, but also on edges, triangles, tetrahedra and so on, paving the way to
concepts like group states, but also necessitating a consideration about their meaning and interpretation [321]. Much
of this new landscape is yet unexplored, but we can already make a few important observations.
At the dynamical level, it is evident that the presence or absence of higher-order interactions is especially important.


86


We reviewed explicit examples in which higher-order interactions profoundly change the critical behavior of dynamical
processes in both simplicial complexes [68, 134, 262, 319, 376, 394] and hypergraphs [84, 238, 393, 586]. However,
even when a dynamical process does not explicitly contain higher-order _dynamical_ terms, it is possible to find new
effects due to higher-order terms in the _structural_ patterns underlying the dynamics. For example, simple contagion
processes are usually considered to be largely oblivious to higher-order structures (e.g. large groups, heterogeneous
and/or hierarchical clique structure) beyond clustering in the underlying contact patterns. However, St-Onge et al.

[711] recently showed that membership of nodes to cliques of heterogeneous sizes can result in unexpected mesoscopic
localization phenomena, in turn yielding possible outbreak persistence for cases in which standard diffusion models
would predict outbreak extinction. Along similar lines, Petri and Barrat [273] showed that including group activations
in a simple contagion model on a temporally evolving contact substrate can shift the critical infectivity, and that the
shift depends on a trade-off between the distributions of group sizes and of activity of the nodes.
The importance of higher-order interactions is naturally not limited to their effects on dynamics. Recent examples
include applications in which higher-order terms allowed better descriptions of group formation in scientific collaborations [96, 338, 612] and finer classification of the local environment of node [114]. In other cases, they improved the
predictions of new interactions beyond the capacity of link-based prediction models, and also significantly denoised
signals in complex environments [51, 712]. Topological descriptions have even been proposed as a convenient tool to
model epistemic models with distributed computing tasks [713, 714].


The study of higher-order systems, of their characteristic properties and their effects on dynamics is a recent field,
and there are still many open and unexplored directions. Below, we list some of them:


_Measures_ _for_ _higher-order_ _structures._ We have described the most common measures used in the description of
HOrSs. With the exception of the intrinsically algebraic ones, most of these measures however are straightforward
generalizations of those used for networks. Temporal, multiplex and multilayer measures are still lacking, and generally there is a large space to be filled. An example are measures that simply cannot be defined in pairwise networks,
the simplicial closure being one of these [96, 114, 116]. Other examples touch on state variables defined on simplices or
hyperedges of arbitrary dimensions: while we have a clear understanding of what synchronization among nodes looks
like in models of oscillators, it is much harder to have an intuitive grasp of what the state of an edge, or of a triangle,
might mean [715]. Defining measures able to capture these quantities would also be a step toward an understanding
of their role and quantitative insights about their effects. A further example is homological information obtained
from topological data analysis techniques: it is defined as an equivalence class and therein lies its power and curse,
because its resulting non-local nature makes it a powerful descriptive tool, but also very hard to localize on specific
elements of the HOrS. Efforts to find a solution to this issue already exist [598, 716, 717], but in many cases the
problem is ill-defined and the solution specific to the problem at hand. So, are there standard or, at least, acceptable
ways to localize homological features as to use them in further analysis? Or should we give up on localizing shapes,
and think only about manifolds? Finally, while hypergraph partitioning [140, 718] has a long history, little work
has focused on characterizing the mesoscopic structure of simplicial complexes, both in terms of the definition and
detection of communities (e.g. [337, 719]) and of other types of (quasi-)local (e.g. rich club, assortative behavior, etc)
and spanning structures (e.g. cores [720], minimal spanning trees [721], expander properties [722, 723]).


_Generative_ _models_ _for_ _higher-order_ _structures._ Models able to constrain various features of higher-order structures
are crucial because they provide a principled answer to the question of what constitutes a non-trivial and topologically
rich HOrS. As we have discussed in this review, there are currently few random models of simplicial complexes. Some
of the existing models of simplicial complexes reproduce the local connectivity patterns[89, 95], but none exist that
are able to reproduce or approximate more refined topological structures, like a specific target homology or mesoscopic structures. Finally, exactly like conventional networks, HOrSs can change in time or be composed by different
qualitatively different types of interactions. With few notable exceptions [273, 628], to date there are practically no
models taking into account the temporal or multiplex structure of higher-order interactions—the vast majority model
growth instead [282].


_Understanding_ _the_ _driving_ _mechanisms_ _of_ _higher-order_ _dynamics._ Developing new measures and generative models
is also important to identify the fundamental mechanisms that lie behind the patterns we observe. There is in fact
clear evidence that non-trivial higher-order topologies emerge in social [724, 725] as well as in biological systems

[598, 625, 626], but very little understanding of how or why they do emerge. Currently, only few models focus on
describing coordination, group interactions and in general growth of HOrSs at the group level, and none reproduce
higher-order topological invariants. This is in part due to the predominance of network descriptions up until now,
and in part to the actual difficulties to provide an analytical description that one encounters as soon as higher-order
terms are introduced. generalizing well-known dynamical systems. In addition to the work on contagion mentioned


87


above, early efforts in this direction are already under way [726], including generalization of Kuramoto models to
higher-order interactions [319, 371, 376] and games [586]. A particularly important and recent line of research focuses
on extending concepts from percolation to simplicial complexes, dubbed _topological_ _percolation_, both in simplicial

[269, 270] and homological terms [727]. Overall, however, we still lack a general understanding of how higher-order
terms affect dynamical systems.


_Inference from data._ What is a truly genuine higher-order interaction? And how do we tease it apart from low-order
ones in data? And if it is possible, what type of data do we need to tell the difference between low and higher-order
interactions? These are hard questions in general, but for some systems it is easier to approach them with some
confidence. Indeed, for systems where the data already comes in the form of sets, it is straightforward to extract
higher-order interactions and measure their strengths. This is the case, for instance, of affiliation networks such as
coauthorship data, where each paper constitutes an interaction among all authors, or of data about joint presence
in locations, or different ingredients in recipes. In many systems, however, interactions are not already identified,
but instead need to be inferred from the data. The most obvious example is that of timeseries: brain functional
networks are usually estimated by computing correlations, or other measures based on information theory, between
fMRI or EEG timeseries [728]; similarly, financial networks are built starting from stock option prices or timecourse
of revenues, and so on [729]. In all these cases, higher-order interactions are seldom considered relevant, or even
computed, due to various reasons. First, many-body correlations are often computed as second order approximations
of standard correlations, and hence considered as perturbations. Second, measures that can find higher-order effects

[730–732] often require long timeseries, which in many cases are not available. Third, the scarce availability of
rich data on dynamical models with and without higher-order interactions makes it impossible to define a proper
inference scheme for the presence, nature and strength of higher-order interactions. This last point is crucial and
links back to the importance of models to understand the underlying mechanisms. Just like it is hardly possible to
distinguish complex from simple contagion from prevalence and incidence data [733], it might well be the case that it
is not possible to tease apart the effects of complex contagion from those of simplicial contagion [262] in absence of
microscopic mechanistic information. However, currently there are no inference schemes, akin to Peixoto [734], able
to test hypothesis about higher-order interactions and provide guidance in these situations. Developing such schemes
is therefore paramount to the advancement of the field.


The open directions discussed above focus on theoretical, modeling and methodological issues. HOrSs have already
been fruitful in a smattering of applications, but they still need to find concrete applications to a wider range of
topics. Indeed, the real test of their relevance will be in the breadth and depth of their impact on specific problems.
While the paradigm of higher-order interactions is general, we envision that problems in biology, ecology, population
dynamics, neuroscience and computational social sciences will be the first and the foremost to benefit from these new
tools and ideas. We hope that this review will provide a guiding path for researchers interested in HOrSs, and we
look forward to seeing how HOrSs themselves will reshape the landscape of complex systems research.


**ACKNOWLEDGMENTS**


F. B. acknowledges partial support from the ERC Synergy Grant 810115 (DYNASNET). G. C. and M. L. acknowledge partial support from the European Cooperation in Science & Technology (COST): Action CA15109. I.
I. acknowledges partial support from the Urban Dynamics Lab under the EPSRC Grant No. EP/M023583/1. V.
L. acknowledges support from the Leverhulme Trust Research Fellowship “CREATE: the network components of
creativity and success”, RF-2019-059. J.-G. Y. acknowledges support from the James S. McDonnell Foundation. G.
P. acknowledges partial support from Intesa Sanpaolo Innovation Center and from Compagnia San Paolo (ADnD
project).


The authors acknowledge valuable and stimulating discussions with many members of the network science community on the topic covered in our report, including Antoine Allard, Unai Alvarez-Rodriguez, Alex Arenas, Tomaso Aste,
Paolo Bajardi, Albert-L´aszl´o Barab´asi, Andrea Baronchelli, Alain Barrat, Danielle Bassett, Demian Battaglia, Jaume
Bertranpetit, Ginestra Bianconi, Christian Bick, Jacob C.W. Billings, Stefano Boccaletti, Francesco Bonchi, Guido
Caldarelli, Timoteo Carletti, Ciro Cattuto, Mario Chavez, Guilherme Ferraz de Arruda, Fabrizio De Vico Fallani,
Tiziana Di Matteo, Tina Eliassi-Rad, Paul Expert, Duccio Fanelli, Michael Farber, Mattia Frasca, Luca Gallo, Lucia
Gambuzza, Laetitia Gauvin, Fosca Giannotti, Tommaso Gili, Corrado Gioannini, Jesus G´omez-Garde˜nes, Heather A.
Harrington, Laurent H´ebert-Dufresne, Esther Ib´a˜nez-Marcelo, Gerardo I˜niguez, Cliff Joslyn, M´arton Karsai, Sonia
K´efi, J´anos Kert´esz, Julia Koltai, Dima Krioukov, Lucas Lacasa, Renaud Lambiotte, Bruno Lepri, Michael Lesnick,
Daniele Marinazzo, Andrea Migliano, Yamir Moreno, M.E.J. Newman, Andr´e Panisson, Daniela Paolotti, Luca Pap

88


palardo, Dino Pedreschi, Tiago P. Peixoto, Matjaˇz Perc, Nicola Perra, Angkoon Phinyomark, Mason Porter, M´arton
P´osfai, Mario Rasetti, Martin Rosvall, Manish Saggar, Enrica L. Santarcangelo, Samuel S. Scarpino, Michael Schaub,
Martina Scolamiero, Ingo Scholtes, Olaf Sporns, Bosiljka Tadi´c, Stefan Thurner, Michele Tizzoni, Francesco Vaccarino,
Alessandro Vespignani, Lucio Vinicius.


[1] P. W. Anderson. More is different. _Science_, 177(4047):393–396, 1972.

[2] Albert-L´aszl´o Barab´asi. The network takeover. _Nat._ _Phys._, 8(1):14, 2011.

[3] R´eka Albert and Albert-L´aszl´o Barab´asi. Statistical mechanics of complex networks. _Rev._ _Mod._ _Phys._, 74(1):47, 2002.

[4] S. N. Dorogovtsev and J. F. F. Mendes. Evolution of networks. _Adv._ _Phys._, 51(4):1079–1187, 2002.

[5] M. E. J. Newman. The structure and function of complex networks. _SIAM_ _Rev._, 45:167–256, 2003.

[6] S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, and D-U. Hwang. Complex networks : Structure and dynamics. _Phys._
_Rep._, 424(4-5):175–308, Fervier 2006.

[7] M. E. J. Newman. _Networks:_ _An Introduction_ . Oxford University Press, Oxford; New York, 2010. ISBN 978-0-19-920665-0
0-19-920665-1.

[8] Ernesto Estrada. _The_ _Structure_ _of_ _Complex_ _Networks:_ _Theory_ _and_ _Applications_ . Oxford University Press, Inc., New
York, NY, USA, 2011. ISBN 0-19-959175-X 978-0-19-959175-6.

[9] Albert-L´aszl´o Barab´asi and M´arton P´osfai. _Network_ _Science_ . Cambridge University Press, Cambridge, 2016. ISBN
978-1-107-07626-6 1-107-07626-9.

[10] Vito Latora, Vincenzo Nicosia, and Giovanni Russo. _Complex Networks:_ _Principles, Methods and Applications_ . Cambridge
University Press, 2017.

[11] Carter T Butts. Revisiting the foundations of network analysis. _Science_, 325(5939):414–416, 2009.

[12] Petter Holme and Jari Saram¨aki. Temporal networks. _Phys._ _Rep._, 519(3):97–125, 2012.

[13] Stefano Boccaletti, Ginestra Bianconi, Regino Criado, Charo I Del Genio, Jes´us G´omez-Gardenes, Miguel Romance, Irene
Sendina-Nadal, Zhen Wang, and Massimiliano Zanin. The structure and dynamics of multilayer networks. _Phys._ _Rep._,
544(1):1–122, 2014.

[14] Jonathan M Levine, Jordi Bascompte, Peter B Adler, and Stefano Allesina. Beyond pairwise mechanisms of species
coexistence in complex communities. _Nature_, 546(7656):56, 2017.

[15] Damon Centola. The spread of behavior in an online social network experiment. _Science_, 329(5996):1194–1197, 2010.

[16] Mark E. J. Newman, Steven H. Strogatz, and Duncan J. Watts. Random graphs with arbitrary degree distributions and
their applications. _Phys._ _Rev._ _E_, 64:026118, 2001.

[17] Ronald H Atkin. From cohomology in physics to q-connectivity in social science. _Int._ _J._ _Man-Mach._ _Stud._, 4(2):139–167,
1972.

[18] Claude Berge. Graphs and hypergraphs. 1973.

[19] Ron Atkin. _Mathematical_ _Structure_ _in_ _Human_ _Affairs_ . Heinemann Educational Publishers, 1974.

[20] Mikko Kivel¨a, Alex Arenas, Marc Barthelemy, James P Gleeson, Yamir Moreno, and Mason A Porter. Multilayer networks.
_J_ _Comp_ _Netw_, 2(3):203–271, 2014.

[21] Federico Battiston, Vincenzo Nicosia, and Vito Latora. The new challenges of multiplex networks: Measures and models.
_The_ _European_ _Physical_ _Journal_ _Special_ _Topics_, 226(3):401–416, 2017.

[22] Ginestra Bianconi. _Multilayer_ _networks:_ _structure_ _and_ _function_ . Oxford university press, 2018.

[23] Alberto Aleta and Yamir Moreno. Multilayer networks in a nutshell. _Annual_ _Review_ _of_ _Condensed_ _Matter_ _Physics_, 10:
45–62, 2019.

[24] Renaud Lambiotte, Martin Rosvall, and Ingo Scholtes. From networks to optimal higher-order models of complex systems.
_Nat._ _Phys._, page 1, 2019.

[25] John Adrian Bondy, Uppaluri Siva Ramachandra Murty, et al. _Graph_ _Theory_ _with_ _Applications_, volume 290. Macmillan
London, 1976.

[26] Uri Alon. Biological networks: The tinkerer as an engineer. _Science_, 301(5641):1866–1867, 2003.

[27] Nadav Kashtan and Uri Alon. Spontaneous evolution of modularity and network motifs. _Proc._ _Natl._ _Acad._ _Sci._, 102(39):
13773–13778, 2005.

[28] Jacopo Grilli, Gy¨orgy Barab´as, Matthew J Michalska-Smith, and Stefano Allesina. Higher-order interactions stabilize
dynamics in competitive network models. _Nature_, 548(7666):210, 2017.

[29] Jos´e M Montoya, Stuart L Pimm, and Ricard V Sol´e. Ecological networks and their fragility. _Nature_, 442(7100):259,
2006.

[30] Stephen P Borgatti, Ajay Mehra, Daniel J Brass, and Giuseppe Labianca. Network analysis in the social sciences. _science_,
323(5916):892–895, 2009.

[31] Miller McPherson, Lynn Smith-Lovin, and James M Cook. Birds of a feather: Homophily in social networks. _Annu._ _Rev._
_Sociol._, 27(1):415–444, 2001.

[32] Jianxi Gao, Sergey V Buldyrev, H Eugene Stanley, and Shlomo Havlin. Networks formed from interdependent networks.
_Nat._ _Phys._, 8(1):40, 2012.

[33] Sergey V Buldyrev, Roni Parshani, Gerald Paul, H Eugene Stanley, and Shlomo Havlin. Catastrophic cascade of failures
in interdependent networks. _Nature_, 464(7291):1025, 2010.


89


[34] Ed Bullmore and Olaf Sporns. Complex brain networks: Graph theoretical analysis of structural and functional systems.
_Nat._ _Rev._ _Neurosci._, 10(3):186, 2009.

[35] Danielle S Bassett and Olaf Sporns. Network neuroscience. _Nat._ _Neurosci._, 20(3):353, 2017.

[36] John D Medaglia, Mary-Ellen Lynall, and Danielle S Bassett. Cognitive network neuroscience. _J._ _Cogn._ _Neurosci._, 27(8):
1471–1491, 2015.

[37] Mari´an Bogu˜n´a, Maksim Kitsak, and Dmitri Krioukov. Cosmological networks. _New_ _J._ _Phys._, 16(9):093031, 2014.

[38] Santo Fortunato. Community detection in graphs. _Phys._ _Rep._, 486(3-5):75–174, 2010.

[39] Gergely Palla, Imre Der´enyi, Ill´es Farkas, and Tam´as Vicsek. Uncovering the overlapping community structure of complex
networks in nature and society. _nature_, 435(7043):814, 2005.

[40] Brian Karrer and M. E. J Newman. Stochastic blockmodels and community structure in networks. _Phys._ _Rev._ _E_, 83(1):
016107, 2011.

[41] Andrea Lancichinetti and Santo Fortunato. Limits of modularity maximization in community detection. _Phys._ _Rev._ _E_,
84(6):066122, 2011.

[42] Emmanuel Abbe and Colin Sandon. Community detection in general stochastic block models: Fundamental limits and
efficient algorithms for recovery. In _2015_ _IEEE_ _56th_ _Annual_ _Symposium_ _on_ _Foundations_ _of_ _Computer_ _Science_, pages
670–688. IEEE, 2015.

[43] Andrea Lancichinetti, Santo Fortunato, and Filippo Radicchi. Benchmark graphs for testing community detection algorithms. _Phys._ _Rev._ _E_, 78(4):046110, 2008.

[44] Jean-Loup Guillaume and Matthieu Latapy. Bipartite structure of all complex networks. _Inf_ _Process_ _Lett_, 90(5):215–221,
2004.

[45] Jean-Loup Guillaume and Matthieu Latapy. Bipartite graphs as models of complex networks. _Phys._ _A_, 371(2):795–813,
2006.

[46] Stanley Wasserman and Katherine Faust. _Social_ _Network_ _Analysis_ _:_ _Methods_ _and_ _Applications_ _(Structural_ _Analysis_ _in_
_the_ _Social_ _Sciences)_ . Cambridge University Press, 1994. ISBN 0-521-38707-8.

[47] M. E. J Newman, Duncan J Watts, and Steven H Strogatz. Random graph models of social networks. _Proc._ _Natl._ _Acad._
_Sci._, 99(suppl 1):2566–2572, 2002.

[48] Roger Guimer`a, Marta Sales-Pardo, and Lu´ıs A Nunes Amaral. Module identification in bipartite and directed networks.
_Phys._ _Rev._ _E_, 76(3):036102, 2007.

[49] Tao Zhou, Jie Ren, Mat´uˇs Medo, and Yi-Cheng Zhang. Bipartite network projection and personal recommendation.
_Phys._ _Rev._ _E_, 76(4):046115, 2007.

[50] Katharina Anna Zweig and Michael Kaufmann. A systematic approach to the one-mode projection of bipartite graphs.
_Soc._ _Netw._ _Anal._ _Min._, 1(3):187–218, 2011.

[51] Michael T Schaub and Santiago Segarra. Flow smoothing and denoising: Graph signal processing in the edge-space. In
_2018_ _IEEE_ _Global_ _Conference_ _on_ _Signal_ _and_ _Information_ _Processing_ _(GlobalSIP)_, pages 735–739. IEEE, 2018.

[52] Ron Milo, Shai Shen-Orr, Shalev Itzkovitz, Nadav Kashtan, Dmitri Chklovskii, and Uri Alon. Network motifs: Simple
building blocks of complex networks. _Science_, 298(5594):824–827, 2002.

[53] Uri Alon. Network motifs: Theory and experimental approaches. _Nat._ _Rev._ _Genet._, 8(6):450, 2007.

[54] Austin R Benson, David F Gleich, and Jure Leskovec. Higher-order organization of complex networks. _Science_, 353
(6295):163–166, 2016.

[55] Sarah E Morgan, Sophie Achard, Maite Termenon, Edward T Bullmore, and Petra E V´ertes. Low-dimensional morphospace of topological motifs in human fMRI brain networks. _Netw_ _Neurosci_, 2(02):285–302, 2018.

[56] Andrea Avena-Koenigsberger, Joaqu´ın Go˜ni, Ricard Sol´e, and Olaf Sporns. Network morphospace. _J._ _R._ _Soc._ _Interface_,
12(103):20140881, 2015.

[57] Shai S Shen-Orr, Ron Milo, Shmoolik Mangan, and Uri Alon. Network motifs in the transcriptional regulation network
of Escherichia coli. _Nat._ _Genet._, 31(1):64, 2002.

[58] James H Fowler, Christopher T Dawes, and Nicholas A Christakis. Model of genetic variation in human social networks.
_Proc._ _Natl._ _Acad._ _Sci._, 106(6):1720–1724, 2009.

[59] Ashwin Paranjape, Austin R Benson, and Jure Leskovec. Motifs in temporal networks. In _Proceedings_ _of_ _the_ _Tenth_ _ACM_
_International_ _Conference_ _on_ _Web_ _Search_ _and_ _Data_ _Mining_, pages 601–610. ACM, 2017.

[60] Lauri Kovanen, M´arton Karsai, Kimmo Kaski, J´anos Kert´esz, and Jari Saram¨aki. Temporal motifs in time-dependent
networks. _J._ _Stat._ _Mech._ _Theory_ _Exp._, 2011(11):P11005, 2011.

[61] Priya Mahadevan, Dmitri Krioukov, Kevin Fall, and Amin Vahdat. Systematic topology analysis and generation using
degree correlations. In _ACM_ _SIGCOMM_ _Computer_ _Communication_ _Review_, volume 36, pages 135–146. ACM, 2006.

[62] Chiara Orsini, Marija M Dankulov, Pol Colomer-de-Sim´on, Almerima Jamakovic, Priya Mahadevan, Amin Vahdat,
Kevin E Bassler, Zolt´an Toroczkai, Mari´an Bogun´a, Guido Caldarelli, et al. Quantifying randomness in real networks.
_Nat._ _Commun._, 6:8627, 2015.

[63] Imre Der´enyi, Gergely Palla, and Tam´as Vicsek. Clique percolation in random networks. _Phys._ _Rev._ _Lett._, 94(16):160202,
2005.

[64] Robin IM Dunbar and Matt Spoors. Social networks, support cliques, and kinship. _Hum._ _Nat._, 6(3):273–290, 1995.

[65] Keith G Provan and Juliann G Sebastian. Networks within networks: Service link overlap, organizational cliques, and
network effectiveness. _Acad._ _Manage._ _J._, 41(4):453–463, 1998.

[66] A. Hatcherr. Algebraic topology. 2002.

[67] Danijela Horak and J¨urgen Jost. Spectra of combinatorial Laplace operators on simplicial complexes. _Adv._ _Math._, 244:
303–336, 2013.


90


[68] Abubakr Muhammad and Magnus Egerstedt. Control using higher order Laplacians in network topologies. In _Proc._ _of_
_17th_ _International_ _Symposium_ _on_ _Mathematical_ _Theory_ _of_ _Networks_ _and_ _Systems_, pages 1024–1038. Citeseer, 2006.

[69] Armindo Costa and Michael Farber. Random simplicial complexes. In _Configuration_ _Spaces_, pages 129–153. Springer,
Berlin, 2016.

[70] Ginestra Bianconi and Christoph Rahmede. Network geometry with flavor: From complexity to quantum geometry. _Phys._
_Rev._ _E_, 93(3):032315, 2016.

[71] R. Ghrist. _Elementary_ _Applied_ _Topology_ . CreateSpace Independent Publishing Platform, 2014. ISBN 978-1-5028-8085-7.

[72] Gunnar Carlsson. Topology and data. _Bull._ _Am._ _Math._ _Soc._, 46(2):255–308, 2009.

[73] Alice Patania, Francesco Vaccarino, and Giovanni Petri. Topological analysis of data. _EPJ_ _Data_ _Sci._, 6(1):7, 2017.

[74] Paul Expert, Louis-David Lord, Morten L. Kringelbach, and Giovanni Petri. Editorial: Topological neuroscience. _Netw_
_Neurosci_, 3(3):653–655, 2019.

[75] Akira Higuchi, Hiroyuki Miyoshi, and Toru Tsujishita. Higher dimensional hypercategories. _arXiv:math/9907150_, 1999.

[76] Anand Louis. Hypergraph Markov operators, eigenvalues and approximation algorithms. In _Proceedings_ _of_ _the_ _Forty-_
_Seventh_ _Annual_ _ACM_ _Symposium_ _on_ _Theory_ _of_ _Computing_, pages 713–722. ACM, 2015.

[77] T-H Hubert Chan, Anand Louis, Zhihao Gavin Tang, and Chenzi Zhang. Spectral properties of hypergraph Laplacian
and approximation algorithms. _J._ _ACM_ _JACM_, 65(3):15, 2018.

[78] T-H Hubert Chan and Zhibin Liang. Generalizing the hypergraph Laplacian via a diffusion process with mediators.
_Theor._ _Comput._ _Sci._, 2019.

[79] Gourab Ghoshal, Vinko Zlati´c, Guido Caldarelli, and M. E. J Newman. Random hypergraphs and their applications.
_Phys._ _Rev._ _E_, 79(6):066118, 2009.

[80] Tarun Kumar, Sankaran Vaidyanathan, Harini Ananthapadmanabhan, Srinivasan Parthasarathy, and Balaraman Ravindran. Hypergraph clustering: A modularity maximization approach. _arXiv:1812.10869_, 2018.

[81] Philip Chodrow and Andrew Mellor. Annotated hypergraphs: Models and applications. _Appl._ _Netw._ _Sci._, 5(1):9, 2020.

[82] Ernesto Estrada and Juan A Rodr´ıguez-Vel´azquez. Complex networks as hypergraphs. _arXiv:physics/0505137_, 2005.

[83] Bogumi�l Kami´nski, Val´erie Poulin, Pawe�l Pra�lat, Przemys�law Szufel, and Francois Theberge. Clustering via hypergraph
modularity. _PLOS_ _ONE_, 14(11), 2019.

[84] Dengyong Zhou, Jiayuan Huang, and Bernhard Sch¨olkopf. Learning with hypergraphs: Clustering, classification, and
embedding. In _Advances_ _in_ _Neural_ _Information_ _Processing_ _Systems_, pages 1601–1608, 2007.

[85] Philip S Chodrow. Configuration models of random hypergraphs and their applications. _arXiv:1902.09302_, 2019.

[86] Juan Alberto Rodriguez. On the Laplacian spectrum and walk-regular hypergraphs. _Linear_ _Multilinear_ _Algebra_, 51(3):
285–297, 2003.

[87] Abdelghani Bellaachia and Mohammed Al-Dhelaan. Random walks in hypergraph. In _Proceedings_ _of_ _the_ _2013_ _Interna-_
_tional_ _Conference_ _on_ _Applied_ _Mathematics_ _and_ _Computational_ _Methods,_ _Venice_ _Italy_, pages 187–194, 2013.

[88] Chen Avin, Yuval Lando, and Zvi Lotker. Radio cover time in hyper-graphs. In _Proceedings_ _of_ _the_ _6th_ _International_
_Workshop_ _on_ _Foundations_ _of_ _Mobile_ _Computing_, pages 3–12. ACM, 2010.

[89] Jean-Gabriel Young, Giovanni Petri, Francesco Vaccarino, and Alice Patania. Construction of and efficient sampling from
the simplicial configuration model. _Phys._ _Rev._ _E_, 96(3):032312, 2017.

[90] Timothy E Goldberg. Combinatorial Laplacians of simplicial complexes. _Sr._ _Thesis_ _Bard_ _Coll._, 2002.

[91] Slobodan Maleti´c, Milan Rajkovi´c, and Danijela Vasiljevi´c. Simplicial complexes of networks and their statistical properties. In _International_ _Conference_ _on_ _Computational_ _Science_, pages 568–575. Springer, 2008.

[92] Art Duval and Victor Reiner. Shifted simplicial complexes are Laplacian integral. _Trans._ _Am._ _Math._ _Soc._, 354(11):
4313–4344, 2002.

[93] Daniel Hern´andez Serrano and Dar´ıo S´anchez G´omez. Higher order degree in simplicial complexes, multi combinatorial
Laplacian and applications of TDA to complex networks. _arXiv:1908.02583_, 2019.

[94] Ernesto Estrada and Grant J Ross. Centralities in simplicial complexes. applications to protein interaction networks. _J._
_Theor._ _Biol._, 438:46–60, 2018.

[95] Owen T. Courtney and Ginestra Bianconi. Generalized network structures: The configuration model and the canonical
ensemble of simplicial complexes. _Phys._ _Rev._ _E_, 93(6):062311, 2016.

[96] Alice Patania, Giovanni Petri, and Francesco Vaccarino. The shape of collaborations. _EPJ_ _Data_ _Sci._, 6(1):18, 2017.

[97] Komal Kapoor, Dhruv Sharma, and Jaideep Srivastava. Weighted node degree centrality for hypergraphs. In _2013_ _IEEE_
_2nd_ _Network_ _Science_ _Workshop_ _(NSW)_, pages 152–155. IEEE, 2013.

[98] Bin Jiang and Itzhak Omer. Spatial topology and its structural analysis based on the concept of simplicial complex.
_Trans._ _GIS_, 11(6):943–960, 2007.

[99] Daniel Hern´andez Serrano and Dar´ıo S´anchez G´omez. Centrality measures in simplicial complexes: Applications of TDA
to Network Science. _arXiv:1908.02967_, 2019.

[100] Linyuan Lu and Xing Peng. High-ordered random walks and generalized Laplacians on hypergraphs. In _International_
_Workshop_ _on_ _Algorithms_ _and_ _Models_ _for_ _the_ _Web-Graph_, pages 14–25. Springer, 2011.

[101] Ernesto Estrada and Juan A Rodr´ıguez-Vel´azquez. Subgraph centrality and clustering in complex hyper-networks. _Phys._
_A_, 364:581–594, 2006.

[102] Sinan G Aksoy, Cliff Joslyn, Carlos Ortiz Marrero, Brenda Praggastis, and Emilie Purvine. Hypernetwork science via
high-order hypergraph walks. _arXiv:1906.11295_, 2019.

[103] Phillip Bonacich. Factoring and weighting approaches to status scores and clique identification. _J._ _Math._ _Sociol._, 2(1):
113–120, 1972.

[104] M. E. J Newman. Modularity and community structure in networks. _Proc._ _Natl._ _Acad._ _Sci._, 103(23):8577–8582, 2006.


91


[105] Amy N Langville and Carl D Meyer. Deeper inside pagerank. _Internet_ _Math._, 1(3):335–380, 2004.

[106] Jack McKay Fletcher and Thomas Wennekers. From structure to activity: Using centrality measures to predict neuronal
activity. _Int._ _J._ _Neural_ _Syst._, 28(02):1750013, 2018.

[107] Phillip Bonacich. Simultaneous group and individual centralities. _Soc._ _Netw._, 13(2):155–168, 1991.

[108] Phillip Bonacich, Annie Cody Holdren, and Michael Johnston. Hyper-edges and multidimensional centrality. _Soc_ _Netw_,
26(3):189–203, 2004.

[109] Austin R Benson. Three hypergraph eigenvector centralities. _SIAM_ _J._ _Math._ _Data_ _Sci._, 1(2):293–312, 2019.

[110] Liqun Qi and Ziyan Luo. _Tensor_ _Analysis:_ _Spectral_ _Theory_ _and_ _Special_ _Tensors_, volume 151. Siam, 2017.

[111] Mark S Granovetter. The strength of weak ties. In _Social_ _Networks_, pages 347–367. Elsevier, 1977.

[112] Tore Opsahl. Triadic closure in two-mode networks: Redefining the global and local clustering coefficients. _Soc._ _Netw._,
35(2):159–167, 2013.

[113] Stephen P Borgatti and Martin G Everett. Network analysis of 2-mode data. _Soc._ _Netw._, 19(3):243–269, 1997.

[114] Alexander P Kartun-Giles and Ginestra Bianconi. Beyond the clustering coefficient: A topological analysis of node
neighbourhoods in complex networks. _Chaos_ _Solitons_ _Fractals_ _X_, 1:100004, 2019.

[115] Hao Yin, Austin R Benson, Jure Leskovec, and David F Gleich. Local higher-order graph clustering. In _Proceedings_ _of_ _the_
_23rd_ _ACM_ _SIGKDD_ _International_ _Conference_ _on_ _Knowledge_ _Discovery_ _and_ _Data_ _Mining_, pages 555–564. ACM, 2017.

[116] Austin R Benson, Rediet Abebe, Michael T Schaub, Ali Jadbabaie, and Jon Kleinberg. Simplicial closure and higher-order
link prediction. _Proc_ _Natl_ _Acad_ _Sci_ _USA_, 115(48):E11221–E11230, 2018.

[117] H. Edelsbrunner. _A_ _Short_ _Course_ _in_ _Computational_ _Geometry_ _and_ _Topology_ . SpringerBriefs in Applied Sciences and
Technology. Springer International Publishing, 2014. ISBN 978-3-319-05957-0.

[118] Robert Ghrist. Barcodes: The persistent topology of data. _Bull._ _Am._ _Math._ _Soc._, 45(1):61–75, 2008.

[119] Alessandro Verri, Claudio Uras, Patrizio Frosini, and Massimo Ferri. On the use of size functions for shape analysis. _Biol._
_Cybern._, 70(2):99–107, 1993.

[120] Francesca Cagliari, Massimo Ferri, and Paola Pozzi. Size functions from a categorical viewpoint. _Acta_ _Appl._ _Math._, 67
(3):225–235, 2001.

[121] Herbert Edelsbrunner, David Letscher, and Afra Zomorodian. Topological persistence and simplification. In _Proceedings_
_41st_ _Annual_ _Symposium_ _on_ _Foundations_ _of_ _Computer_ _Science_, pages 454–463. IEEE, 2000.

[122] Afra Zomorodian and Gunnar Carlsson. Computing persistent homology. _Discrete_ _Comput._ _Geom._, 33(2):249–274, 2005.

[123] Michelle Feng and Mason A Porter. Persistent homology of geospatial data: A case study with voting. _arXiv:1902.05911_,
2019.

[124] Gunnar Carlsson and Vin De Silva. Zigzag persistence. _Found._ _Comput._ _Math._, 10(4):367–405, 2010.

[125] Gunnar Carlsson and Afra Zomorodian. The theory of multidimensional persistence. _Discrete_ _Comput._ _Geom._, 42(1):
71–93, 2009.

[126] Herbert Edelsbrunner and Dmitriy Morozov. Persistent homology. In _Handbook_ _of_ _Discrete_ _and_ _Computational_ _Geometry_,
pages 637–661. Chapman and Hall/CRC, 2017.

[127] Nina Otter, Mason A Porter, Ulrike Tillmann, Peter Grindrod, and Heather A Harrington. A roadmap for the computation
of persistent homology. _EPJ_ _Data_ _Sci._, 6(1):17, 2017.

[128] MR Muldoon, RS MacKay, JP Huke, and DS Broomhead. Topology from time series. _Phys._ _D_, 65(1-2):1–16, 1993.

[129] Robert J Adler, Kevin Bartz, Sam C Kou, and Anthea Monod. Estimating thresholding levels for random fields via Euler
characteristics. _arXiv:1704.08562_, 2017.

[130] Pratyush Pranav, Rien Van de Weygaert, Gert Vegter, Bernard JT Jones, Robert J Adler, Job Feldbrugge, Changbom
Park, Thomas Buchert, and Michael Kerber. Topology and geometry of Gaussian random fields I: On Betti numbers,
Euler characteristic, and Minkowski functionals. _Mon._ _Not._ _R._ _Astron._ _Soc._, 485(3):4167–4208, 2019.

[131] Slobodan Maleti´c and Milan Rajkovi´c. Combinatorial Laplacian and entropy of simplicial complexes associated with
complex networks. _Eur_ _Phys_ _J_ _ST_, (1):77–97, 2012.

[132] Lek-Heng Lim. Hodge Laplacians on graphs. _Proc._ _Symp._ _Appl._ _Math._, 2015.

[133] Ori Parzanchevski and Ron Rosenthal. Simplicial complexes: Spectrum, homology and random walks. _Random_ _Struc_
_Algorithms_, 50(2):225–261, 2017.

[134] Michael T Schaub, Austin R Benson, Paul Horn, Gabor Lippner, and Ali Jadbabaie. Random walks on simplicial
complexes and the normalized Hodge Laplacian. _SIAM_ _Rev._, 62(2):353–391, 2020.

[135] JA Rodriguez. Laplacian eigenvalues and partition problems in hypergraphs. _Appl._ _Math._ _Lett._, 22(6):916–921, 2009.

[136] Fan Chung. The Laplacian of a hypergraph. _Expand._ _Graphs_ _DIMACS_ _Ser._, pages 21–36, 1993.

[137] Shota Saito, Danilo P Mandic, and Hideyuki Suzuki. Hypergraph p-Laplacian: A differential geometry view. In _Thirty-_
_Second_ _AAAI_ _Conference_ _on_ _Artificial_ _Intelligence_, 2018.

[138] Joshua Cooper and Aaron Dutle. Spectra of uniform hypergraphs. _Linear_ _Algebra_ _Its_ _Appl._, 436(9):3268–3292, 2012.

[139] Shenglong Hu and Liqun Qi. The Laplacian of a uniform hypergraph. _J._ _Comb._ _Optim._, 29(2):331–366, 2015.

[140] Pan Li and Olgica Milenkovic. Submodular hypergraphs: P-Laplacians, Cheeger inequalities and spectral clustering. In
_Proceedings_ _of_ _the_ _35th_ _International_ _Conference_ _on_ _Machine_ _Learning_, pages 3014–3023, 2018.

[141] Maxime Lucas, Giulia Cencetti, and Federico Battiston. A multi-order Laplacian for synchronization in higher-order
networks. _arXiv:2003.09734_, 2020.

[142] Anthony CC Coolen, Alessia Annibale, and Ekaterina Roberts. _Generating_ _Random_ _Networks_ _and_ _Graphs_ . Oxford
university press, 2017.

[143] Dmitri Krioukov and Massimo Ostilli. Duality between equilibrium and growing networks. _Physical_ _Review_ _E_, 88(2):
022808, 2013.


92


[144] Ginestra Bianconi and Andrea Capocci. Number of loops of size h in growing scale-free networks. _Phys._ _Rev._ _Lett._, 90
(7):078701, 2003.

[145] Ginestra Bianconi and Matteo Marsili. Loops of any size and hamilton cycles in random scale-free networks. _Journal_ _of_
_Statistical_ _Mechanics:_ _Theory_ _and_ _Experiment_, 2005(06):P06005, 2005.

[146] M Angeles Serrano and Mari´an Bogun´a. Tuning clustering in random networks with arbitrary degree distributions. _Phys._
_Rev._ _E_, 72(3):036133, 2005.

[147] B´ela Bollob´as and Paul Erd¨os. Cliques in random graphs. In _Mathematical_ _Proceedings_ _of_ _the_ _Cambridge_ _Philosophical_
_Society_, volume 80, pages 419–427. Cambridge University Press, 1976.

[148] Ginestra Bianconi and Matteo Marsili. Emergence of large cliques in random scale-free networks. _EPL_ _(Europhysics_
_Letters)_, 74(4):740, 2006.

[149] Bailey K Fosdick, Daniel B Larremore, Joel Nishimura, and Johan Ugander. Configuring random graph models with
fixed degree sequences. _SIAM_ _Rev._, 60(2):315–355, 2018.

[150] Jared M Diamond. Assembly of species communities. _Ecol._ _Evol._ _Communities_, pages 342–444, 1975.

[151] Edward F Connor and Daniel Simberloff. The assembly of species communities: Chance or competition? _Ecology_, 60(6):
1132–1140, 1979.

[152] Mitchell Gail and Nathan Mantel. Counting the number of r× c contingency tables with fixed margins. _JASA_, 72(360a):
859–862, 1977.

[153] Albert Verbeek and Pieter M Kroonenberg. A survey of algorithms for exact distributions of test statistics in r× c
contingency tables with fixed margins. _Comput._ _Stat._ _Data_ _Anal._, 3:159–185, 1985.

[154] Fabio Saracco, Riccardo Di Clemente, Andrea Gabrielli, and Tiziano Squartini. Randomizing bipartite networks: The
case of the World Trade Web. _Sci._ _Rep._, 5:10595, 2015.

[155] Cl`audia Payrat´o-Borr`as, Laura Hern´andez, and Yamir Moreno. Breaking the spell of nestedness: The entropic origin of
nestedness in mutualistic systems. _Phys._ _Rev._ _X_, 9(3):031024, 2019.

[156] Maksim Kitsak and Dmitri Krioukov. Hidden variables in bipartite networks. _Phys._ _Rev._ _E_, 84(2):026114, 2011.

[157] Asma Azizi Boroojeni, Jeremy Dewar, Tong Wu, and James M Hyman. Generating bipartite networks with a prescribed
joint degree distribution. _J._ _Complex_ _Netw._, 5(6):839–857, 2017.

[158] Bo S¨oderberg. General formalism for inhomogeneous random graphs. _Phys._ _Rev._ _E_, 66(6):066121, 2002.

[159] Antoine Allard, Pierre-Andr´e No¨el, Louis J Dub´e, and Babak Pourbohloul. Heterogeneous bond percolation on multitype
networks with an application to epidemic dynamics. _Phys._ _Rev._ _E_, 79(3):036113, 2009.

[160] Xiang Fu, Shangdi Yu, and Austin R Benson. Modeling and analysis of tagging networks in stack exchange communities.
_J._ _Complex_ _Netw._, 12 2019. ISSN 2051-1329.

[161] Stanley Wasserman and Philippa Pattison. Logit models and logistic regressions for social networks: I. An introduction
to Markov graphs andp. _Psychometrika_, 61(3):401–425, 1996.

[162] Tom AB Snijders, Philippa E Pattison, Garry L Robins, and Mark S Handcock. New specifications for exponential
random graph models. _Sociol._ _Methodol._, 36(1):99–153, 2006.

[163] Ove Frank and David Strauss. Markov graphs. _J._ _Am._ _Stat._ _Assoc._, 81(395):832–842, 1986.

[164] Paul W Holland and Samuel Leinhardt. An exponential family of probability distributions for directed graphs. _J._ _Am._
_Stat._ _Assoc._, 76(373):33–50, 1981.

[165] Matthieu Latapy, Cl´emence Magnien, and Nathalie Del Vecchio. Basic notions for the analysis of large two-mode networks.
_Soc_ _Netw._, 30(1):31–48, 2008.

[166] Dawn Iacobucci and Stanley Wasserman. Social networks with two sets of actors. _Psychometrika_, 55(4):707–720, 1990.

[167] John Skvoretz and Katherine Faust. Logit models for affiliation networks. _Sociolo_ _Methodol_, 29(1):253–280, 1999.

[168] Garry Robins and Malcolm Alexander. Small worlds among interlocking directors: Network structure and distance in
bipartite graphs. _Comput._ _Math._ _Organ._ _Theory_, 10(1):69–94, 2004.

[169] Filip Agneessens, Henk Roose, and Hans Waege. Choices of theatre events: P* models for affiliation networks with
attributes. _Metod_ _Zv_, 1(2):419, 2004.

[170] David Strauss. On a general class of models for interaction. _SIAM_ _Rev._, 28(4):513–527, 1986.

[171] Mark S Handcock. Statistical models for social networks: Inference and degeneracy. In R. Breiger, K. Carley, and P. Pattison, editors, _Dynamic_ _Social_ _Network_ _Modeling_ _and_ _Analysis._, pages 229–240. National Academies Press, (Washington,
DC), 2003.

[172] Rico Fischer, Jorge C Leit˜ao, Tiago P Peixoto, and Eduardo G Altmann. Sampling motif-constrained ensembles of
networks. _Phys._ _Rev._ _Lett._, 115(18):188701, 2015.

[173] Peng Wang, Ken Sharpe, Garry L Robins, and Philippa E Pattison. Exponential random graph (p*) models for affiliation
networks. _Soc._ _Networks_, 31(1):12–25, 2009.

[174] Peng Wang, Philippa Pattison, and Garry Robins. Exponential random graph model specifications for bipartite networks—A dependence hierarchy. _Soc._ _Networks_, 35(2):211–222, 2013.

[175] Garry Robins, Pip Pattison, Yuval Kalish, and Dean Lusher. An introduction to exponential random graph (p*) models
for social networks. _Soc_ _Netw_, 29(2):173–191, 2007.

[176] Jeffrey A Smith. Macrostructure from microstructure: Generating whole systems from ego networks. _Sociol._ _Methodol._,
42(1):155–205, 2012.

[177] Lorien Jasny. Baseline models for two-mode social network data. _Policy_ _Stud._ _J._, 40(3):458–491, 2012.

[178] Katherine Faust, Karin E Willert, David D Rowlee, and John Skvoretz. Scaling and statistical models for affiliation
networks: Patterns of participation among Soviet politicians during the Brezhnev era. _Soc_ _Netw._, 24(3):231–259, 2002.

[179] Tom AB Snijders. Markov chain Monte Carlo estimation of exponential random graph models. _J_ _Soc_ _Struct_, 3(2):1–40,


93


2002.

[180] Cosma Rohilla Shalizi and Alessandro Rinaldo. Consistency under sampling of exponential random graph models. _Ann._
_Stat._, 41(2):508, 2013.

[181] Harry Crane. _Probabilistic_ _Foundations_ _of_ _Statistical_ _Network_ _Analysis_ . Chapman and Hall/CRC, 2018.

[182] Jean-Gabriel Young, Guillaume St-Onge, Patrick Desrosiers, and Louis J Dub´e. Universality of the stochastic block
model. _Phys._ _Rev._ _E_, 98(3):032309, 2018.

[183] M. E. J Newman. Communities, modules and large-scale structure in networks. _Nat._ _Phys._, 8(1):25–31, 2012.

[184] M. E. J Newman. Mixing patterns in networks. _Phys._ _Rev._ _E_, 67(2):026126, 2003.

[185] Stephen P Borgatti and Martin G Everett. Models of core/periphery structures. _Soc_ _Netw_, 21(4):375–395, 2000.

[186] Paul W. Holland, Kathryn Blackmond Laskey, and Samuel Leinhardt. Stochastic blockmodels: First steps. _Soc. Networks_,
5(2):109–137, 1983.

[187] Patrick Doreian, Vladimir Batagelj, and Anuˇska Ferligoj. Generalized blockmodeling of two-mode network data. _Soc._
_Networks_, 26(1):29–53, 2004.

[188] Karl Rohe, Tai Qin, and Bin Yu. Co-clustering directed graphs to discover asymmetries and directional communities.
_Proc._ _Natl._ _Acad._ _Sci._ _U._ _S._ _A._, 113(45):12679–12684, 2016.

[189] Daniel B Larremore, Aaron Clauset, and Abigail Z Jacobs. Efficiently inferring community structure in bipartite networks.
_Phys._ _Rev._ _E_, 90(1):012805, 2014.

[190] Sofia C Olhede and Patrick J Wolfe. Network histograms and universality of blockmodel approximation. _Proc._ _Natl._
_Acad._ _Sci._ _U.S.A._, 111(41):14722–14727, 2014.

[191] Tiago P Peixoto. Entropy of stochastic blockmodel ensembles. _Phys._ _Rev._ _E_, 85(5):056122, 2012.

[192] Roger Guimer`a, Alejandro Llorente, Esteban Moro, and Marta Sales-Pardo. Predicting human preferences using the
block structure of complex social networks. _PLOS_ _ONE_, 7(9):e44620, 2012.

[193] Brian Ball, Brian Karrer, and M. E. J Newman. Efficient and principled method for detecting communities in networks.
_Phys._ _Rev._ _E_, 84(3):036103, 2011.

[194] Darko Hric, Tiago P Peixoto, and Santo Fortunato. Network structure, metadata, and the prediction of missing nodes
and annotations. _Phys._ _Rev._ _X_, 6(3):031038, 2016.

[195] Martin Gerlach, Tiago P Peixoto, and Eduardo G Altmann. A network approach to topic models. _Sci._ _Adv._, 4(7):
eaaq1360, 2018.

[196] David M Blei, Andrew Y Ng, and Michael I Jordan. Latent dirichlet allocation. _J._ _Mach._ _Learn._ _Res._, 3(Jan):993–1022,
2003.

[197] Qizheng Sheng, Yves Moreau, and Bart De Moor. Biclustering microarray data by Gibbs sampling. _Bioinformatics_, 19
(suppl 2):ii196–ii205, 2003.

[198] Srikanth K Iyer and Dahandapani Yogeshwaran. Percolation and connectivity in AB random geometric graphs. _Adv._
_Appl._ _Probab._, 44(1):21–41, 2012.

[199] Mathew Penrose et al. _Random_ _Geometric_ _Graphs_, volume 5. Oxford university press, 2003.

[200] Bernard M Waxman. Routing of multipoint connections. _IEEE_ _J._ _Sel._ _Areas_ _Commun._, 6(9):1617–1622, 1988.

[201] M Angeles Serrano, Dmitri Krioukov, and Mari´an Bogun´a. Self-similarity of complex networks and hidden metric spaces.
_Phys._ _Rev._ _Lett._, 100(7):078701, 2008.

[202] Maksim Kitsak, Fragkiskos Papadopoulos, and Dmitri Krioukov. Latent geometry of bipartite networks. _Phys._ _Rev._ _E_,
95(3):032309, 2017.

[203] M Angeles [´] Serrano, Mari´an Bogun´a, and Francesc Sagu´es. Uncovering the hidden geometry behind metabolic networks.
_Mol._ _Biosyst._, 8(3):843–850, 2012.

[204] Dmitri Krioukov. Clustering implies geometry in networks. _Phys._ _Rev._ _Lett._, 116(20):208302, 2016.

[205] Mark E. J. Newman. Properties of highly clustered networks. _Phys._ _Rev._ _E_, 68(2):026121, 2003.

[206] James A Davis and Samuel Leinhardt. The structure of positive interpersonal relations in small groups. 1967.

[207] Paul W Holland and Samuel Leinhardt. Local structure in social networks. _Sociol._ _Methodol._, 7:1–45, 1976.

[208] James P Gleeson and Sergey Melnik. Analytical results for bond percolation and k-core sizes on clustered networks. _Phys._
_Rev._ _E_, 80(4):046121, 2009.

[209] Pieter Trapman. On analytical approaches to epidemics on networks. _Theor._ _Popul._ _Biol._, 71(2):160–173, 2007.

[210] M. E. J Newman. Random graphs with clustering. _Phys._ _Rev._ _Lett._, 103(5):058701, 2009.

[211] Joel C Miller. Percolation and epidemics in random clustered networks. _Phys._ _Rev._ _E_, 80(2):020901, 2009.

[212] James P Gleeson. Bond percolation on a class of clustered random networks. _Phys._ _Rev._ _E_, 80(3):036107, 2009.

[213] Brian Karrer and M. E. J Newman. Random graphs containing arbitrary distributions of subgraphs. _Phys._ _Rev._ _E_, 82
(6):066118, 2010.

[214] Antoine Allard, Laurent H´ebert-Dufresne, Pierre-Andr´e No¨el, Vincent Marceau, and Louis J Dub´e. Bond percolation on
a class of correlated and clustered random graphs. _J._ _Phys._ _Math._ _Theor._, 45(40):405005, 2012.

[215] Antoine Allard, Laurent H´ebert-Dufresne, Jean-Gabriel Young, and Louis J Dub´e. General and exact approach to
percolation on random graphs. _Phys._ _Rev._ _E_, 92(6):062807, 2015.

[216] Anatol E Wegner. Subgraph covers: An information-theoretic approach to motif analysis in networks. _Phys._ _Rev._ _X_, 4
(4):041026, 2014.

[217] B´ela Bollob´as, Svante Janson, and Oliver Riordan. Sparse random graphs with clustering. _Random_ _Struct_ _Algorithms_,
38(3):269–323, 2011.

[218] M. E. J Newman and Tiago P Peixoto. Generalized communities in networks. _Phys._ _Rev._ _Lett._, 115(8):088701, 2015.


94


[219] William Devanny, David Eppstein, and B´alint Tillman. The computational hardness of dk-series. In _NetSci_ _2016_, 2016.

[220] Philippa Pattison and Garry Robins. Neighborhood-based models for social networks. _Sociol._ _Methodol._, 32(1):301–337,
2002.

[221] Duncan J Watts, Peter Sheridan Dodds, and M. E. J Newman. Identity and search in social networks. _Science_, 296
(5571):1302–1305, 2002.

[222] Jaewon Yang and Jure Leskovec. Community-affiliation graph model for overlapping network community detection. In
_2012_ _IEEE_ _12th_ _International_ _Conference_ _on_ _Data_ _Mining_, pages 1170–1175. IEEE, 2012.

[223] Laurent H´ebert-Dufresne, Pierre-Andr´e No¨el, Vincent Marceau, Antoine Allard, and Louis J Dub´e. Propagation dynamics
on networks featuring complex topologies. _Phys._ _Rev._ _E_, 82(3):036115, 2010.

[224] Comandur Seshadhri, Tamara G Kolda, and Ali Pinar. Community structure and scale-free collections of Erd˝os-R´enyi
graphs. _Phys._ _Rev._ _E_, 85(5):056109, 2012.

[225] Micha�l Karo´nski, Edward R Scheinerman, and Karen B Singer-Cohen. On random intersection graphs: The subgraph
problem. _Comb_ _Probab_ _Comput_, 8(1-2):131–159, 1999.

[226] Paul Erd¨os, Adolph W Goodman, and Louis P´osa. The representation of a graph by set intersections. _Can._ _J._ _Math._, 18:
106–112, 1966.

[227] Alan Frieze and Micha�l Karo´nski. _Introduction_ _to_ _Random_ _Graphs_ . Cambridge University Press, 2016.

[228] S Nikoletseas, Christoforos Raptopoulos, and P Spirakis. Large independent sets in general random intersection graphs.
_Theor_ _Comput_ _Sci_, 406(3):215–224, 2008.

[229] Maria Deijfen and Willemien Kets. Random intersection graphs with tunable degree distribution and clustering. _Probab._
_Eng._ _Inf._ _Sci._, 23(4):661–674, 2009.

[230] Erhard Godehardt and Jerzy Jaworski. Two models of random intersection graphs for classification. In _Exploratory_ _Data_
_Analysis_ _in_ _Empirical_ _Research_, pages 67–81. Springer, 2003.

[231] George B Davis and Kathleen M Carley. Clearing the FOG: Fuzzy, overlapping groups for social networks. _Soc_ _Netw_, 30
(3):201–212, 2008.

[232] David Barber. Clique matrices for statistical graph decomposition and parameterising restricted positive definite matrices.
_Uncertain._ _Artif._ _Intell._, pages 26–33, 2008.

[233] Sinead A Williamson and Mauricio Tec. Random clique covers for graphs with local density and global sparsity. In
_Proceedings_ _of_ _the_ _2019_ _Conference_ _on_ _Uncertainty_ _in_ _Artificial_ _Intelligence_, 2018.

[234] Frank G Ball, David J Sirl, Pieter Trapman, et al. Epidemics on random intersection graphs. _Ann._ _Appl._ _Probab._, 24(3):
1081–1128, 2014.

[235] Jierui Xie, Stephen Kelley, and Boleslaw K Szymanski. Overlapping community detection in networks: The state-of-theart and comparative study. _Acm_ _Comput._ _Surv._ _Csur_, 45(4):43, 2013.

[236] W Fernandez De La Vega. Sur la cardinalit´e maximum des couplages d’hypergraphes al´eatoires uniformes. _Discrete_
_Math._, 40(2-3):315–318, 1982.

[237] Jeanette Schmidt-Pruzan and Eli Shamir. Component structure in the evolution of random hypergraphs. _Combinatorica_,
5(1):81–94, 1985.

[238] Guilherme Ferraz de Arruda, Giovanni Petri, and Yamir Moreno. Social contagion models on hypergraphs. _Phys_ _Rev_
_Res_, 2(2):023032, 2020.

[239] Richard WR Darling, James R Norris, et al. Structure of large random hypergraphs. _Ann_ _Appl_ _Probab_, 15(1A):125–152,
2005.

[240] Marc Mezard, Marc Mezard, and Andrea Montanari. _Information,_ _Physics,_ _and_ _Computation_ . Oxford University Press,
2009.

[241] Amir Dembo, Andrea Montanari, et al. Finite size scaling for the core of large random hypergraphs. _Ann._ _Appl._ _Probab._,
18(5):1993–2040, 2008.

[242] Jeanette Schmidt and Eli Shamir. A threshold for perfect matchings in random d-pure hypergraphs. _Discrete_ _Math._, 45
(2-3):287–295, 1983.

[243] Hui Chen and Alan Frieze. Coloring bipartite hypergraphs. In _International_ _Conference_ _on_ _Integer_ _Programming_ _and_
_Combinatorial_ _Optimization_, pages 345–358. Springer, 1996.

[244] J´anos Demetrovics, Gyula OH Katona, Dezs¨o Mikl´os, Oleg Seleznjev, and Bernhard Thalheim. Asymptotic properties of
keys and functional dependencies in random databases. _Theor._ _Comput._ _Sci._, 190(2):151–166, 1998.

[245] Serena Bradde and Ginestra Bianconi. The percolation transition in correlated hypergraphs. _J._ _Stat._ _Mech.:_ _Theory_
_Exp._, 2009(07):P07028, 2009.

[246] Mark EJ Newman and Michelle Girvan. Finding and evaluating community structure in networks. _Phys._ _Rev._ _E_, 69(2):
026113, 2004.

[247] Fan Chung and Linyuan Lu. Connected components in random graphs with given expected degree sequences. _Ann._
_Comb._, 6(2):125–145, 2002.

[248] Despina Stasi, Kayvan Sadeghi, Alessandro Rinaldo, Sonja Petrovi´c, and Stephen E Fienberg. _β_ models for random
hypergraphs with a given degree sequence. _arXiv:1407.1004_, 2014.

[249] Debarghya Ghoshdastidar and Ambedkar Dukkipati. Consistency of spectral partitioning of uniform hypergraphs under
planted partition model. In _Advances_ _in_ _Neural_ _Information_ _Processing_ _Systems_, pages 397–405, 2014.

[250] Zheng Tracy Ke, Feng Shi, and Dong Xia. Community detection for hypergraph networks via regularized tensor power
iteration. _arXiv:1909.06503_, 2019.

[251] Kwangjun Ahn, Kangwook Lee, and Changho Suh. Hypergraph spectral clustering in the weighted stochastic block
model. _IEEE_ _J._ _Sel._ _Top._ _Signal_ _Process._, 12(5):959–974, 2018.


95


[252] Subhadeep Paul, Olgica Milenkovic, and Yuguo Chen. Higher-order spectral clustering under superimposed stochastic
block model. _arXiv:1812.06515_, 2018.

[253] Kathryn Turnbull, Sim´on Lunag´omez, Christopher Nemeth, and Edoardo Airoldi. Latent space representations of hypergraphs. _arXiv:1909.00472_, 2019.

[254] Jurij Leskovec, Deepayan Chakrabarti, Jon Kleinberg, and Christos Faloutsos. Realistic, mathematically tractable graph
generation and evolution, using kronecker multiplication. In _European_ _Conference_ _on_ _Principles_ _of_ _Data_ _Mining_ _and_
_Knowledge_ _Discovery_, pages 133–145. Springer, 2005.

[255] Nicole Eikmeier, Arjun Ramani, and David Gleich. The HyperKron Graph Model for higher-order features. In _2018_
_IEEE_ _International_ _Conference_ _on_ _Data_ _Mining_ _(ICDM)_, pages 941–946. IEEE, 2018.

[256] Matthew Kahle. Random geometric complexes. _Discrete_ _Comput._ _Geom._, 45(3):553–573, 2011.

[257] Nathan Linial and Roy Meshulam. Homological connectivity of random 2-complexes. _Combinatorica_, 26(4):475–487,
2006.

[258] Matthew Kahle. Topology of random simplicial complexes: A survey. _AMS_ _Contemp_ _Math_, 620:201–222, 2014.

[259] Roy Meshulam and Nathan Wallach. Homological connectivity of random k-dimensional complexes. _Random_ _Struct_
_Algorithms_, 34(3):408–417, 2009.

[260] Matthew Kahle. Topology of random clique complexes. _Discrete_ _Math._, 309(6):1658–1671, 2009.

[261] Christopher F Fowler. Generalized random simplicial complexes. _arXiv:1503.01831_, 2015.

[262] Iacopo Iacopini, Giovanni Petri, Alain Barrat, and Vito Latora. Simplicial models of social contagion. _Nat._ _Commun._,
10(1):2485, 2019.

[263] Diego Alberici, Pierluigi Contucci, Emanuele Mingione, and Marco Molari. Aggregation models on hypergraphs. _Ann._
_Phys._, 376:412–424, 2017.

[264] Konstantin Zuev, Or Eisenberg, and Dmitri Krioukov. Exponential random simplicial complexes. _J._ _Phys._ _A_, 48(46):
465002, 2015.

[265] Fr´ed´eric Chazal and Bertrand Michel. An introduction to Topological Data Analysis: Fundamental and practical aspects
for data scientists. _arXiv:1710.04019_, 2017.

[266] Matthew Kahle, Elizabeth Meckes, et al. Limit the theorems for Betti numbers of random simplicial complexes. _Homol._
_Homotopy_ _Appl._, 15(1):343–374, 2013.

[267] Omer Bobrowski and Matthew Kahle. Topology of random geometric complexes: a survey. _J._ _Appl._ _Comput._ _Topol._, 1
(3-4):331–364, 2018.

[268] Brittany Terese Fasy, Fabrizio Lecci, Alessandro Rinaldo, Larry Wasserman, Sivaraman Balakrishnan, Aarti Singh, et al.
Confidence sets for persistence diagrams. _Ann._ _Stat._, 42(6):2301–2339, 2014.

[269] Ginestra Bianconi and Robert M Ziff. Topological percolation on hyperbolic simplicial complexes. _Physical_ _Review_ _E_, 98
(5):052308, 2018.

[270] Ginestra Bianconi, Ivan Kryven, and Robert M. Ziff. Percolation on branching simplicial and cell complexes and its
relation to interdependent percolation. _Phys._ _Rev._ _E_, 100(6):062311, 2019.

[271] Jan Overgoor, Austin Benson, and Johan Ugander. Choosing to grow a graph: Modeling network formation as discrete
choice. In _The_ _World_ _Wide_ _Web_ _Conference_, pages 1409–1420. ACM, 2019.

[272] Albert-L´aszl´o Barab´asi and R´eka Albert. Emergence of scaling in random networks. _Science_, 286(5439):509–512, 1999.

[273] Giovanni Petri and Alain Barrat. Simplicial activity driven model. _Phys._ _Rev._ _Lett._, 121(22):228301, 2018.

[274] G¨uler Erg¨un. Human sexual contact network as a bipartite graph. _Phys._ _A_, 308(1-4):483–488, 2002.

[275] Jos´e J Ramasco, Sergey N Dorogovtsev, and Romualdo Pastor-Satorras. Self-organization of collaboration networks.
_Phys._ _Rev._ _E_, 70(3):036106, 2004.

[276] Mariano Beguerisse D´ıaz, Mason A Porter, and Jukka-Pekka Onnela. Competition for popularity in bipartite networks.
_Chaos_, 20(4):043101, 2010.

[277] Kim Sneppen, Martin Rosvall, Ala Trusina, and Petter Minnhagen. A simple model for self-organization of bipartite
networks. _Europhys._ _Lett._, 67(3):349, 2004.

[278] Per Bak, Chao Tang, and Kurt Wiesenfeld. Self-organized criticality: An explanation of the 1/f noise. _Phys._ _Rev._ _Lett._,
59(4):381, 1987.

[279] Nial Friel, Riccardo Rastelli, Jason Wyse, and Adrian E Raftery. Interlocking directorates in Irish companies using a
latent space model for bipartite networks. _Proc_ _Natl_ _Acad_ _Sci_ _USA_, 113(24):6629–6634, 2016.

[280] TS Evans. Exact solutions for network rewiring models. _Eur._ _Phys._ _J._ _B_, 56(1):65–69, 2007.

[281] TS Evans and ADK Plato. Exact solution for the time evolution of network rewiring models. _Phys._ _Rev._ _E_, 75(5):056101,
2007.

[282] Zhihao Wu, Giulia Menichetti, Christoph Rahmede, and Ginestra Bianconi. Emergent complex network geometry. _Sci._
_Rep._, 5:10073, 2015.

[283] Peter Pollner, Gergely Palla, and Tamas Vicsek. Preferential attachment of communities: The same principle, but a
higher level. _Europhys._ _Lett._, 73(3):478, 2005.

[284] Xie Zhou, Li Xiang, and Wang Xiao-Fan. Weighted evolving networks with self-organized communities. _Commun._ _Theor._
_Phys._, 50(1):261, 2008.

[285] Laurent H´ebert-Dufresne, Antoine Allard, Vincent Marceau, Pierre-Andr´e No¨el, and Louis J Dub´e. Structural preferential
attachment: Network organization beyond the link. _Phys._ _Rev._ _Lett._, 107(15):158702, 2011.

[286] Laurent H´ebert-Dufresne, Antoine Allard, Vincent Marceau, Pierre-Andr´e No¨el, and Louis J Dub´e. Structural preferential
attachment: Stochastic process for the growth of scale-free, modular, and self-similar systems. _Phys. Rev. E_, 85(2):026108,
2012.


96


[287] Jean-Gabriel Young, Laurent H´ebert-Dufresne, Antoine Allard, and Louis J Dub´e. Growing networks of overlapping
communities with internal structure. _Phys._ _Rev._ _E_, 94(2):022317, 2016.

[288] Laurent H´ebert-Dufresne, Edward Laurence, Antoine Allard, Jean-Gabriel Young, and Louis J Dub´e. Complex networks
as an emerging property of hierarchical preferential attachment. _Phys._ _Rev._ _E_, 92(6):062809, 2015.

[289] David J Aldous. Exchangeability and related topics. In _Ecole_ _[´]_ _d’Et´e_ _[´]_ _de_ _Probabilit´es_ _de_ _Saint-Flour_ _XIII—1983_, pages
1–198. Springer, 1985.

[290] Thomas L Griffiths and Zoubin Ghahramani. The indian buffet process: An introduction and review. _J_ _Mach_ _Learn_ _Res_,
12(Apr):1185–1224, 2011.

[291] Zi-Ke Zhang and Chuang Liu. A hypergraph model of social tagging networks. _J._ _Stat._ _Mech.:_ _Theory_ _Exp._, 2010(10):
P10005, 2010.

[292] Jian-Wei Wang, Li-Li Rong, Qiu-Hong Deng, and Ji-Yong Zhang. Evolving hypernetwork model. _Eur._ _Phys._ _J._ _B_, 77(4):
493–498, 2010.

[293] Dajie Liu, Norbert Blenn, and Piet Van Mieghem. A social network model exhibiting tunable overlapping community
structure. _Procedia_ _Comput._ _Sci._, 9:1400–1409, 2012.

[294] Feng Hu, Jin-Li Guo, Fa-Xu Li, Hai-Xing Zhao, et al. Hypernetwork models based on random hypergraphs. _Int._ _J._ _Mod._
_Phys._ _C_ _IJMPC_, 30(08):1–15, 2019.

[295] Yang Guang-Yong and Liu Jian-Guo. A local-world evolving hypernetwork model. _Chin_ _Phys_ _B_, 23(1):018901, 2013.

[296] Zhaoyan Wu, Jinqiao Duan, and Xinchu Fu. Synchronization of an evolving complex hyper-network. _Appl._ _Math._ _Model._,
38(11-12):2961–2968, 2014.

[297] Jin-Li Guo, Xin-Yun Zhu, Qi Suo, and Jeffrey Forrest. Non-uniform evolving hypergraphs and weighted evolving hypergraphs. _Sci._ _Rep._, 6:36648, 2016.

[298] Paul L Krapivsky, Sidney Redner, and Francois Leyvraz. Connectivity of growing random networks. _Phys._ _Rev._ _Lett._, 85
(21):4629, 2000.

[299] Jin-Li Guo and Qi Suo. Brand effect versus competitiveness in hypernetworks. _Chaos_, 25(2):023102, 2015.

[300] Ginestra Bianconi. Interdisciplinary and physics challenges of network theory. _Europhys._ _Lett._, 111(5):56001, 2015.

[301] Ginestra Bianconi and Christoph Rahmede. Complex quantum network manifolds in dimension d¿ 2 are scale-free. _Sci._
_Rep._, 5:13979, 2015.

[302] Ginestra Bianconi, Christoph Rahmede, and Zhihao Wu. Complex quantum network geometries: Evolution and phase
transitions. _Phys._ _Rev._ _E_, 92(2):022815, 2015.

[303] Owen T Courtney and Ginestra Bianconi. Weighted growing simplicial complexes. _Phys._ _Rev._ _E_, 95(6):062301, 2017.

[304] Nikolaos Fountoulakis, Tejas Iyer, C´ecile Mailler, and Henning Sulzbach. Dynamical models for random simplicial complexes. _arXiv:1910.12715_, 2019.

[305] Ann E Sizemore, Elisabeth A Karuza, Chad Giusti, and Danielle S Bassett. Knowledge gaps in the early growth of
semantic feature networks. _Nat_ _Hum_ _Behav_, 2(9):682, 2018.

[306] Ann Sizemore Blevins and Danielle S Bassett. On the reorderability of node-filtered order complexes. _Phys._ _Rev._ _E_, 101:
052311, 2020.

[307] Diamantino C da Silva, Ginestra Bianconi, Rui A da Costa, Sergey N Dorogovtsev, and Jos´e FF Mendes. Complex
network view of evolving manifolds. _Phys._ _Rev._ _E_, 97(3):032316, 2018.

[308] Owen T Courtney and Ginestra Bianconi. Dense power-law networks and simplicial complexes. _Phys._ _Rev._ _E_, 97(5):
052303, 2018.

[309] Bomin Kim, Aaron Schein, Bruce A Desmarais, and Hanna Wallach. The hyperedge event model. _arXiv:1807.08225_,
2018.

[310] Naoki Masuda, Mason A Porter, and Renaud Lambiotte. Random walks and diffusion on networks. _Phys._ _Rep._, 2017.

[311] David Aldous and Jim Fill. Reversible Markov chains and random walks on graphs. _Unfinished_ _Monogr._, 2002.

[312] AN Samukhin, SN Dorogovtsev, and JFF Mendes. Laplacian spectra of, and random walks on, complex networks: Are
scale-free architectures really important? _Phys._ _Rev._ _E_, 77(3):036115, 2008.

[313] Till Hoffmann, Mason A. Porter, and Renaud Lambiotte. Generalized master equations for non-Poisson dynamics on
networks. _Phys._ _Rev._ _E_, 86(4):046102, 2012.

[314] Morris H DeGroot. Reaching a consensus. _J._ _Am._ _Stat._ _Assoc._, 69(345):118–121, 1974.

[315] Ludwig Boltzmann. Lectures on gas theory, translated by s. _Brush_ _Univ._ _Calif._ _Los_ _Angel._ _Calif_, 1964.

[316] Richard Chace Tolman. _The_ _Principles_ _of_ _Statistical_ _Mechanics_ . Courier Corporation, 1979.

[317] Fan RK Chung and Fan Chung Graham. _Spectral_ _Graph_ _Theory_ . Number 92. American Mathematical Soc., 1997.

[318] Leonie Neuh¨auser, Andrew Mellor, and Renaud Lambiotte. Multibody interactions and nonlinear consensus dynamics on
networked systems. _Phys._ _Rev._ _E_, 101(3):032310, 2020.

[319] Joaqu´ın J. Torres and Ginestra Bianconi. Simplicial complexes: Higher-order spectral dimension and dynamics. _J._ _Phys.:_
_Complex._, 1:015002, 2020.

[320] Raffaella Burioni and Davide Cassi. Universal properties of spectral dimension. _Phys._ _Rev._ _Lett._, 76(7):1091, 1996.

[321] Ana P Mill´an, Joaqu´ın J Torres, and Ginestra Bianconi. Synchronization in network geometries with finite spectral
dimension. _Phys._ _Rev._ _E_, 99(2):022307, 2019.

[322] Junteng Jia, Michael T Schaub, Santiago Segarra, and Austin R Benson. Graph-based semi-supervised & active learning
for edge flows. In _Proceedings_ _of_ _the_ _25th_ _ACM_ _SIGKDD_ _International_ _Conference_ _on_ _Knowledge_ _Discovery_ _&_ _Data_
_Mining_, pages 761–771, 2019.

[323] Sayan Mukherjee and John Steenbergen. Random walks on simplicial complexes and harmonics. _Random Struc Algorithms_,


97


49(2):379–405, 2016.

[324] Dheeru Dua and Casey Graff. UCI machine learning repository. 2017.

[325] Timoteo Carletti, Federico Battiston, Giulia Cencetti, and Duccio Fanelli. Random walks on hypergraphs. _Phys._ _Rev._ _E_,
101(2):022308, 2020.

[326] Uthsav Chitra and Benjamin J Raphael. Random walks on hypergraphs with edge-dependent vertex weights. In _Proceed-_
_ings_ _of_ _the_ _36th_ _International_ _Conference_ _on_ _Machine_ _Learning_, pages 1172–1181, 2019.

[327] Sameer Agarwal, Kristin Branson, and Serge Belongie. Higher order learning with graphs. In _Proceedings_ _of_ _the_ _23rd_
_International_ _Conference_ _on_ _Machine_ _Learning_, pages 17–24. ACM, 2006.

[328] Pan Li and Olgica Milenkovic. Inhomogeneous hypergraph clustering with applications. In _Advances in Neural Information_
_Processing_ _Systems_, pages 2308–2318, 2017.

[329] Jianbo Li, Jingrui He, and Yada Zhu. E-tail product return prediction via hypergraph-based local graph cut. In _Proceedings_
_of the 24th ACM_ _SIGKDD International_ _Conference on Knowledge Discovery & Data Mining_, pages 519–527. ACM, 2018.

[330] Lei Ding and Alper Yilmaz. Interactive image segmentation using probabilistic hypergraphs. _Pattern_ _Recognit._, 43(5):
1863–1873, 2010.

[331] Yuchi Huang, Qingshan Liu, Shaoting Zhang, and Dimitris N Metaxas. Image retrieval via probabilistic hypergraph
ranking. In _2010_ _IEEE_ _Computer_ _Society_ _Conference_ _on_ _Computer_ _Vision_ _and_ _Pattern_ _Recognition_, pages 3376–3383.
IEEE, 2010.

[332] Aur´elien Ducournau and Alain Bretto. Random walks in directed hypergraphs and application to semi-supervised image
segmentation. _Comput._ _Vis._ _Image_ _Underst._, 120:91–102, 2014.

[333] Kaiman Zeng, Nansong Wu, Arman Sargolzaei, and Kang Yen. Learn to rank images: A unified probabilistic hypergraph
model for visual search. _Math._ _Probl._ _Eng._, 2016, 2016.

[334] Zizhao Zhang, Haojie Lin, Yue Gao, and KLISS BNRist. Dynamic hypergraph structure learning. In _IJCAI_, pages
3162–3169, 2018.

[335] TH Chan, Zhihao Gavin Tang, and Chenzi Zhang. Spectral properties of Laplacian and stochastic diffusion process for
edge expansion in hypergraphs. _arXiv:1510.01520_, 2015.

[336] T-H Hubert Chan, Zhihao Gavin Tang, Xiaowei Wu, and Chenzi Zhang. Diffusion operator and spectral analysis for
directed hypergraph Laplacian. _Theor._ _Comput._ _Sci._, 784:46–64, 2019.

[337] Jacob Charles Wright Billings, Mirko Hu, Giulia Lerda, Alexey N Medvedev, Francesco Mottes, Adrian Onicas, Andrea
Santoro, and Giovanni Petri. Simplex2Vec embeddings for community detection in simplicial complexes. _arXiv:1906.09068_,
2019.

[338] Vsevolod Salnikov, Daniele Cassese, and Renaud Lambiotte. Simplicial complexes and complex systems. _Eur._ _J._ _Phys._,
40(1):014001, 2018.

[339] Loc Hoang Tran, Linh Hoang Tran, Hoang Trang, et al. Combinatorial and random walk hypergraph Laplacian eigenmaps.
_Int._ _J._ _Mach._ _Learn._ _Comput._, 5(6):462, 2015.

[340] Sai Nageswar Satchidanand, Harini Ananthapadmanaban, and Balaraman Ravindran. Extended discriminative random
walk: A hypergraph approach to multi-view multi-relational transductive learning. In _Twenty-Fourth_ _International_ _Joint_
_Conference_ _on_ _Artificial_ _Intelligence_, 2015.

[341] Ying Liu, Jiabin Yuan, Bojia Duan, and Dan Li. Quantum walks on regular uniform hypergraphs. _Sci._ _Rep._, 8(1):9548,
2018.

[342] Colin Cooper, Alan Frieze, and Tomasz Radzik. The cover times of random walks on hypergraphs. In _International_
_Colloquium_ _on_ _Structural_ _Information_ _and_ _Communication_ _Complexity_, pages 210–221. Springer, 2011.

[343] Alan Mathison Turing. The chemical basis of morphogenesis. _Philos._ _Trans._ _R._ _Soc._ _Lond._ _B_ _Biol._ _Sci._, 237(641):37–72,
1952.

[344] Hiroya Nakao and Alexander S Mikhailov. Turing patterns in network-organized activator–inhibitor systems. _Nat._ _Phys._,
6(7):544–550, 2010.

[345] Malbor Asllani, Joseph D Challenger, Francesco Saverio Pavone, Leonardo Sacconi, and Duccio Fanelli. The theory of
pattern formation on directed networks. _Nat._ _Commun._, 5(1):1–9, 2014.

[346] Giulia Cencetti, Pau Clusella, and Duccio Fanelli. Pattern invariance for reaction-diffusion systems on complex networks.
_Sci._ _Rep._, 8(1):1–9, 2018.

[347] Uzi Harush and Baruch Barzel. Dynamic patterns of information flow in complex networks. _Nat._ _Commun._, 8(1):2181,
2017.

[348] Christiaan Huygens and Horologium Oscillatorium. The pendulum clock. _Trans_ _RJ_ _Blackwell_ _Iowa_ _State_ _Univ._ _Press_
_Ames_, 1986.

[349] Zolt´an N´eda, Erzs´ebet Ravasz, Yves Brechet, Tam´as Vicsek, and A-L Barab´asi. The sound of many hands clapping.
_Nature_, 403(6772):849–850, 2000.

[350] John Buck. Synchronous rhythmic flashing of fireflies. II. _Q._ _Rev._ _Biol._, 63(3):265–289, 1988.

[351] S. Boccaletti, J. Kurths, G. Osipov, D.L. Valladares, and C.S. Zhou. The synchronization of chaotic systems. _Phys._ _Rep._,
366(1):1–101, 2002.

[352] A. Pikovsky, M. Rosenblum, and J. Kurths. _Synchronization:_ _A_ _Universal_ _Concept_ _in_ _Nonlinear_ _Sciences_, volume 12.
Cambridge University Press, Cambridge, 2003.

[353] S. H. Strogatz. _Sync:_ _The_ _Emerging_ _Science_ _of_ _Spontaneous_ _Order_ . Penguin UK, 2004.

[354] Stefano Boccaletti, Alexander N Pisarchik, Charo I Del Genio, and Andreas Amann. _Synchronization:_ _From_ _Coupled_
_Systems_ _to_ _Complex_ _Networks_ . Cambridge University Press, 2018.

[355] Y. Kuramoto. _Chemical_ _Oscillations,_ _Waves,_ _and_ _Turbulence_ . Springer-Verlag, Tokyo, 1984.


98


[356] Juan A Acebr´on, Luis L Bonilla, Conrad J P´erez Vicente, F´elix Ritort, and Renato Spigler. The Kuramoto model: A
simple paradigm for synchronization phenomena. _Rev._ _Mod._ _Phys._, 77(1):137, 2005.

[357] A. Arenas, A. D´ıaz-Guilera, J. Kurths, Y. Moreno, and C. Zhou. Synchronization in complex networks. _Phys._ _Rep._, 469
(3):93–153, 2008.

[358] F. A. Rodrigues, T. K. D. M. Peron, P. Ji, and J. Kurths. The Kuramoto model in complex networks. _Phys._ _Rep._, 610:
1–98, 2016.

[359] Mauricio Barahona and Louis M Pecora. Synchronization in small-world systems. _Phys._ _Rev._ _Lett._, 89(5):054101, 2002.

[360] Jes´us G´omez-Gardenes, Sergio G´omez, Alex Arenas, and Yamir Moreno. Explosive synchronization transitions in scalefree networks. _Phys._ _Rev._ _Lett._, 106(12):128701, 2011.

[361] S Boccaletti, JA Almendral, S Guan, I Leyva, Z Liu, I Sendi˜na-Nadal, Z Wang, and Y Zou. Explosive transitions in
complex networks’ structure and dynamics: Percolation and synchronization. _Phys._ _Rep._, 660:1–94, 2016.

[362] Vincenzo Nicosia, Miguel Valencia, Mario Chavez, Albert D´ıaz-Guilera, and Vito Latora. Remote synchronization reveals
network symmetries and functional modules. _Phys._ _Rev._ _Lett._, 110(17):174102, 2013.

[363] Louis M Pecora, Francesco Sorrentino, Aaron M Hagerstrom, Thomas E Murphy, and Rajarshi Roy. Cluster synchronization and isolated desynchronization in complex networks with symmetries. _Nat._ _Commun._, 5(1):1–8, 2014.

[364] Daniel M Abrams and Steven H Strogatz. Chimera states for coupled oscillators. _Phys._ _Rev._ _Lett._, 93(17):174102, 2004.

[365] Hongjie Bi, Xin Hu, S Boccaletti, Xingang Wang, Yong Zou, Zonghua Liu, and Shuguang Guan. Coexistence of quantized,
time dependent, clusters in globally coupled oscillators. _Phys._ _Rev._ _Lett._, 117(20):204101, 2016.

[366] S. Watanabe and S. H. Strogatz. Integrability of a globally coupled oscillator array. _Phys._ _Rev._ _Lett._, 70(16):2391, 1993.

[367] S. Watanabe and S. H. Strogatz. Constants of motion for superconducting Josephson arrays. _Phys._ _D_, 74(3-4):197–253,
1994.

[368] Edward Ott and Thomas M Antonsen. Low dimensional behavior of large systems of globally coupled oscillators. _Chaos_
_Interdiscip._ _J._ _Nonlinear_ _Sci._, 18(3):037113, 2008.

[369] Yamir Moreno Vega, Miguel V´azquez-Prada, and Amalio F Pacheco. Fitness for synchronization of network motifs. _Phys._
_A_, 343:279–287, 2004.

[370] Otti D’Huys, Raul Vicente, Thomas Erneux, Jan Danckaert, and Ingo Fischer. Synchronization properties of network
motifs: Influence of coupling delay and symmetry. _Chaos_, 18(3):037116, 2008.

[371] Per Sebastian Skardal and Alex Arenas. Abrupt desynchronization and extensive multistability in globally coupled
oscillator simplexes. _Phys._ _Rev._ _Lett._, 122(24):248301, 2019.

[372] Can Xu, Xuebin Wang, and Per Sebastian Skardal. Bifurcation and structural stability of simplicial oscillator populations:
Exact results. _arXiv:2002.03166_, 2020.

[373] Takuma Tanaka and Toshio Aoyagi. Multistable attractors in a network of phase oscillators with three-body interactions.
_Phys._ _Rev._ _Lett._, 106(22):224101, 2011.

[374] Peter Ashwin and Ana Rodrigues. Hopf normal form with SN symmetry and reduction to systems of nonlinearly coupled
phase oscillators. _Phys._ _D_, 325:14–24, 2016.

[375] Maxim Komarov and Arkady Pikovsky. Finite-size-induced transitions to synchrony in oscillator ensembles with nonlinear
global coupling. _Phys._ _Rev._ _E_, 92(2):020901, 2015.

[376] Per Sebastian Skardal and Alex Arenas. Higher-order interactions in complex networks of phase oscillators promote
abrupt synchronization switching. _arXiv:1909.08057_, 2019.

[377] Diego Paz´o. Thermodynamic limit of the first-order phase transition in the Kuramoto model. _Phys._ _Rev._ _E_, 72(4):046211,
2005.

[378] Vincenzo Nicosia, Per Sebastian Skardal, Alex Arenas, and Vito Latora. Collective phenomena emerging from the
interactions between dynamical processes in multiplex networks. _Phys._ _Rev._ _Lett._, 118(13):138302, 2017.

[379] Raissa M D’Souza, Jesus G´omez-Garde˜nes, Jan Nagler, and Alex Arenas. Explosive phenomena in complex networks.
_Adv._ _Phys._, 68(3):123–223, 2019.

[380] Vesna Berec. Chimera state and route to explosive synchronization. _Chaos_, 86:75–81, 2016.

[381] V Berec. Explosive synchronization in clustered scale-free networks: Revealing the existence of chimera state. _Eur_ _Phys_
_J_ _ST_, 225(1):7–15, 2016.

[382] Tomislav Stankovski, Valentina Ticcinelli, Peter VE McClintock, and Aneta Stefanovska. Coupling functions in networks
of oscillators. _New_ _J._ _Phys._, 17(3):035002, 2015.

[383] Iv´an Le´on and Diego Paz´o. Phase reduction beyond the first order: The case of the mean-field complex Ginzburg-Landau
equation. _Phys._ _Rev._ _E_, 100(1):012211, 2019.

[384] Ana P. Mill´an, Joaqu´ın J. Torres, and Ginestra Bianconi. Explosive higher-order Kuramoto dynamics on simplicial
complexes. _Phys._ _Rev._ _Lett._, 124:218301, May 2020.

[385] Ana P. Mill´an, Joaqu´ın J. Torres, and Ginestra Bianconi. Complex network geometry and frustrated synchronization.
_Sci._ _Rep._, 8(1):9910, 2018.

[386] Chen Chris Gong and Arkady Pikovsky. Low-dimensional dynamics for higher-order harmonic, globally coupled phaseoscillator ensembles. _Phys._ _Rev._ _E_, 100(6):062210, 2019.

[387] Michael Rosenblum and Arkady Pikovsky. Self-organized quasiperiodicity in oscillator ensembles with global nonlinear
coupling. _Phys._ _Rev._ _Lett._, 98(6):064101, 2007.

[388] Arkady Pikovsky and Michael Rosenblum. Self-organized partially synchronous dynamics in populations of nonlinearly
coupled oscillators. _Phys._ _D_, 238(1):27–37, 2009.

[389] Oleksandr Burylko and Arkady Pikovsky. Desynchronization transitions in nonlinearly coupled phase oscillators. _Phys._
_D_, 240(17):1352–1361, 2011.


99


[390] Hiroya Nakao. Phase reduction approach to synchronisation of nonlinear oscillators. _Contemp._ _Phys._, 57(2):188–214,
2016.

[391] Bastian Pietras and Andreas Daffertshofer. Network dynamics of coupled oscillators and phase reduction techniques.
_Phys._ _Rep._, 2019.

[392] Peter Ashwin, Christian Bick, and Oleksandr Burylko. Identical phase oscillator networks: Bifurcations, symmetry and
reversibility for generalized coupling. _Front_ _Appl_ _Math_ _Stat_, 2:7, 2016.

[393] Matthew H Matheny, Jeffrey Emenheiser, Warren Fon, Airlie Chapman, Anastasiya Salova, Martin Rohden, Jarvis
Li, Mathias Hudoba de Badyn, M´arton P´osfai, Leonardo Duenas-Osorio, et al. Exotic states in a simple network of
nanoelectromechanical oscillators. _Science_, 363(6431):eaav7932, 2019.

[394] Christian Bick, Peter Ashwin, and Ana Rodrigues. Chaos in generically coupled phase oscillator networks with nonpairwise
interactions. _Chaos_, 26(9):094814, 2016.

[395] Christian Bick. Heteroclinic switching between chimeras. _Phys._ _Rev._ _E_, 97(5):050201, 2018.

[396] Christian Bick. Heteroclinic dynamics of localized frequency synchrony: Heteroclinic cycles for small populations. _J_
_Nonlin_ _Sci_, 2019.

[397] Christian Bick and Alexander Lohse. Heteroclinic dynamics of localized frequency synchrony: Stability of heteroclinic
cycles and networks. _J_ _Nonlin_ _Sci_, 2019.

[398] Christian Bick and Peter Ashwin. Chaotic weak chimeras and their persistence in coupled populations of phase oscillators.
_Nonlinearity_, 29(5):1468, 2016.

[399] Maxim Komarov and Arkady Pikovsky. Dynamics of multifrequency oscillator communities. _Phys._ _Rev._ _Lett._, 110(13):
134101, 2013.

[400] Michael Rosenblum and Arkady Pikovsky. Numerical phase reduction beyond the first order approximation. _Chaos_, 29
(1):011105, 2019.

[401] Louis M Pecora and Thomas L Carroll. Synchronization in chaotic systems. _Phys._ _Rev._ _Lett._, 64(8):821, 1990.

[402] Michael G Rosenblum, Arkady S Pikovsky, and J¨urgen Kurths. Phase synchronization of chaotic oscillators. _Phys._ _Rev._
_Lett._, 76(11):1804, 1996.

[403] Chai Wah Wu. Synchronization in arrays of chaotic circuits coupled via hypergraphs: Static and dynamic coupling.
In _ISCAS’98._ _Proceedings_ _of_ _the_ _1998_ _IEEE_ _International_ _Symposium_ _on_ _Circuits_ _and_ _Systems_ _(Cat._ _No._ _98CH36187)_,
volume 3, pages 287–290. IEEE, 1998.

[404] A Krawiecki. Chaotic synchronization on complex hypergraphs. _Chaos_ _Solitons_ _Fractals_, 65:44–50, 2014.

[405] LV Gambuzza, F Di Patti, L Gallo, S Lepri, M Romance, R Criado, M Frasca, V Latora, and S Boccaletti. The master
stability function for synchronization in simplicial complexes. _arXiv:2004.03913_, 2020.

[406] Ivano Lodato, Stefano Boccaletti, and Vito Latora. Synchronization properties of network motifs. _Europhys._ _Lett._, 78(2):
28001, 2007.

[407] Miguel C Soriano, Guy Van der Sande, Ingo Fischer, and Claudio R Mirasso. Synchronization in simple network motifs
with negligible correlation and mutual information measures. _Phys._ _Rev._ _Lett._, 108(13):134101, 2012.

[408] Sanjukta Krishnagopal, Judith Lehnert, Winnie Poel, Anna Zakharova, and Eckehard Sch¨oll. Synchronization patterns:
From network motifs to hierarchical networks. _Philos._ _Trans._ _Royal_ _Soc._ _A_, 375(2088):20160216, 2017.

[409] RE Amritkar, Sarika Jalan, and Chin-Kun Hu. Synchronized clusters in coupled map networks. II. Stability analysis.
_Phys._ _Rev._ _E_, 72(1):016212, 2005.

[410] Louis M Pecora and Thomas L Carroll. Master stability functions for synchronized coupled systems. _Phys._ _Rev._ _Lett._,
80(10):2109, 1998.

[411] A Englert, S Heiligenthal, W Kinzel, and I Kanter. Synchronization of chaotic networks with time-delayed couplings: An
analytic study. _Phys._ _Rev._ _E_, 83(4):046222, 2011.

[412] Francesco Sorrentino and Edward Ott. Network synchronization of groups. _Phys_ _Rev_ _E_, 76(5):056114, 2007.

[413] Aneta Koseska, Evgeny Volkov, and J¨urgen Kurths. Oscillation quenching mechanisms: Amplitude vs. oscillation death.
_Phys._ _Rep._, 531(4):173–199, 2013.

[414] Raffaella Mulas, Christian Kuehn, and J¨urgen Jost. Coupled dynamics on hypergraphs: Master stability of steady states
and synchronization. _arXiv:2003.13775_, 2020.

[415] Peter Dayan, Laurence F Abbott, and L Abbott. Theoretical neuroscience: Computational and mathematical modeling
of neural systems. 2001.

[416] Wulfram Gerstner and Werner M Kistler. _Spiking_ _Neuron_ _Models:_ _Single_ _Neurons,_ _Populations,_ _Plasticity_ . Cambridge
university press, 2002.

[417] Qiuxiang Bian and Hongxing Yao. Adaptive synchronization of bipartite dynamical networks with distributed delays and
nonlinear derivative coupling. _Commun_ _Nonlinear_ _Sci_ _Numer_ _Simulat_, 16(10):4089–4098, 2011.

[418] Andrey Shilnikov, Ren´e Gordon, and Igor Belykh. Polyrhythmic synchronization in bursting networking motifs. _Chaos_,
18(3):037120, 2008.

[419] Fernanda S Matias, Pedro V Carelli, Claudio R Mirasso, and Mauro Copelli. Anticipated synchronization in a biologically
plausible model of neuronal motifs. _Phys._ _Rev._ _E_, 84(2):021922, 2011.

[420] Leonardo L Gollo, Claudio Mirasso, Olaf Sporns, and Michael Breakspear. Mechanisms of zero-lag synchronization in
cortical motifs. _PLoS_ _Comput._ _Biol._, 10(4):e1003548, 2014.

[421] Dmitry A. Smirnov and Ralph G. Andrzejak. Detection of weak directional coupling: Phase-Dynamics approach versus
state-space approach. _Phys._ _Rev._ _E_, 71(3):036207, 2005.

[422] Stefan Frenzel and Bernd Pompe. Partial Mutual Information for Coupling Analysis of Multivariate Time Series. _Phys._
_Rev._ _Lett._, 99(20):204101, 2007.


100


[423] Michael G. Rosenblum and Arkady S. Pikovsky. Detecting direction of coupling in interacting oscillators. _Phys._ _Rev._ _E_,
64(4):045202, 2001.

[424] Bj¨orn Kralemann, Arkady Pikovsky, and Michael Rosenblum. Reconstructing phase dynamics of oscillator networks.
_Chaos_, 21(2):025104, 2011.

[425] Bj¨orn Kralemann, Arkady Pikovsky, and Michael Rosenblum. Reconstructing effective phase connectivity of oscillator
networks from observations. _New_ _J._ _Phys._, 16(8):085013, 2014.

[426] Bj¨orn Kralemann, Laura Cimponeriu, Michael Rosenblum, Arkady Pikovsky, and Ralf Mrowka. Phase dynamics of
coupled oscillators reconstructed from data. _Phys._ _Rev._ _E_, 77(6):066205, 2008.

[427] P. Tass, M. G. Rosenblum, J. Weule, J. Kurths, A. Pikovsky, J. Volkmann, A. Schnitzler, and H.-J. Freund. Detection of
n:m Phase Locking from Noisy Data: Application to Magnetoencephalography. _Phys._ _Rev._ _Lett._, 81(15):3291–3294, 1998.

[428] Bj¨orn Kralemann, Arkady Pikovsky, and Michael Rosenblum. Detecting triplet locking by triplet synchronization indices.
_Phys._ _Rev._ _E_, 87(5):052904, 2013.

[429] Ji Jia, Zhiwen Song, Weiqing Liu, J¨urgen Kurths, and Jinghua Xiao. Experimental study of the triplet synchronization
of coupled nonidentical mechanical metronomes. _Sci._ _Rep._, 5:17008, 2015.

[430] Andrea Duggento, Tomislav Stankovski, Peter VE McClintock, and Aneta Stefanovska. Dynamical Bayesian inference of
time-evolving interactions: From a pair of coupled oscillators to networks of oscillators. _Phys._ _Rev._ _E_, 86(6):061126, 2012.

[431] Romualdo Pastor-Satorras and Alessandro Vespignani. Epidemic spreading in scale-free networks. _Phys._ _Rev._ _Lett._, 86
(14):3200, 2001.

[432] Romualdo Pastor-Satorras, Claudio Castellano, Piet Van Mieghem, and Alessandro Vespignani. Epidemic processes in
complex networks. _Rev._ _Mod._ _Phys._, 87(3):925, 2015.

[433] Damon Centola. _How_ _behavior_ _spreads:_ _The_ _science_ _of_ _complex_ _contagions_, volume 3. Princeton University Press, 2018.

[434] Parongama Sen and Bikas K Chakrabarti. _Sociophysics:_ _An_ _Introduction_ . Oxford University Press, 2014.

[435] Claudio Castellano, Santo Fortunato, and Vittorio Loreto. Statistical physics of social dynamics. _Rev._ _Mod._ _Phys._, 81(2):
591, 2009.

[436] Andrea Baronchelli. The emergence of consensus: A primer. _R._ _Soc_ _Open_ _Sci_, 5(2):172189, 2018.

[437] William Ogilvy Kermack and Anderson G McKendrick. A contribution to the mathematical theory of epidemics. _Proc._
_R._ _Soc._ _Lond._ _A_, 115(772):700–721, 1927.

[438] Roy M Anderson and Robert M May. _Infectious_ _Diseases_ _of_ _Humans:_ _Dynamics_ _and_ _Control_ . Oxford university press,
1992.

[439] Herbert W Hethcote. The mathematics of infectious diseases. _SIAM_ _Rev._, 42(4):599–653, 2000.

[440] Qian Zhang, Kaiyuan Sun, Matteo Chinazzi, Ana Pastore y Piontti, Natalie E Dean, Diana Patricia Rojas, Stefano
Merler, Dina Mistry, Piero Poletti, Luca Rossi, et al. Spread of Zika virus in the Americas. _Proc._ _Natl._ _Acad._ _Sci._ _U._ _S._
_A._, 114(22):E4334–E4343, 2017.

[441] Ana Pastore y Piontti, Nicola Perra, Luca Rossi, Nicole Samay, and Alessandro Vespignani. _Charting_ _the_ _next_ _Pandemic:_
_Modeling_ _Infectious_ _Disease_ _Spreading_ _in_ _the_ _Data_ _Science_ _Age_ . Springer, 2018.

[442] C´ecile Viboud and Alessandro Vespignani. The future of influenza forecasts. _Proc._ _Natl._ _Acad._ _Sci._ _U._ _S._ _A._, 116(8):
2802–2804, 2019.

[443] Adam J Kucharski, Timothy W Russell, Charlie Diamond, Yang Liu, John Edmunds, Sebastian Funk, Rosalind M Eggo,
Fiona Sun, Mark Jit, James D Munday, et al. Early dynamics of transmission and control of COVID-19: A mathematical
modelling study. _Lancet_ _Infect._ _Dis._, 2020.

[444] Moritz U. G. Kraemer, Chia-Hung Yang, Bernardo Gutierrez, Chieh-Hsi Wu, Brennan Klein, David M. Pigott, Louis du
Plessis, Nuno R. Faria, Ruoran Li, William P. Hanage, John S. Brownstein, Maylis Layan, Alessandro Vespignani, Huaiyu
Tian, Christopher Dye, Oliver G. Pybus, and Samuel V. Scarpino. The effect of human mobility and control measures
on the COVID-19 epidemic in China. _Science_, 2020.

[445] James P Gleeson. High-accuracy approximation of binary-state dynamics on networks. _Phys._ _Rev._ _Lett._, 107(6):068701,
2011.

[446] James P Gleeson. Binary-state dynamics on complex networks: Pair approximation and beyond. _Phys._ _Rev._ _X_, 3(2):
021004, 2013.

[447] Wei Wang, Ming Tang, H Eugene Stanley, and Lidia A Braunstein. Unification of theoretical approaches for epidemic
spreading on complex networks. _Rep._ _Prog._ _Phys._, 80(3):036603, 2017.

[448] Istv´an Z Kiss, Joel C Miller, P´eter L Simon, et al. Mathematics of epidemics on networks. _Cham_ _Springer_, 2017.

[449] Daryl J Daley and David G Kendall. Epidemics and rumours. _Nature_, 204(4963):1118–1118, 1964.

[450] Frank M Bass. A new product growth for model consumer durables. _Manag_ _Sci_, 15(5):215–227, 1969.

[451] Sushil Bikhchandani, David Hirshleifer, and Ivo Welch. A theory of fads, fashion, custom, and cultural change as
informational cascades. _J_ _Polit._ _Econ_, 100(5):992–1026, 1992.

[452] Everett M Rogers. _Diffusion_ _of_ _Innovations_ . Simon and Schuster, 2010.

[453] Damon Centola and Michael Macy. Complex contagions and the weakness of long ties. _Am._ _J._ _Sociol._, 113(3):702–734,
2007.

[454] Douglas Guilbeault, Joshua Becker, and Damon Centola. Complex contagions: A decade in review. In _Complex_ _Spreading_
_Phenomena_ _in_ _Social_ _Systems_, pages 3–25. Springer, 2018.

[455] Kerk F Kee, Lisa Sparks, Daniele C Struppa, and Mirco Mannucci. Social groups, social media, and higher dimensional
social structures: A simplicial model of social aggregation for computational communication research. _Commun_ _Q_, 61
(1):35–58, 2013.

[456] TfL. SocioPatterns collaboration. 2008.


101


[457] Pedro Cisneros-Velarde and Francesco Bullo. Multi-group sis epidemics with simplicial and higher-order interactions.
_arXiv:2005.11404_, 2020.

[458] Sergio G´omez, Alexandre Arenas, J Borge-Holthoefer, Sandro Meloni, and Yamir Moreno. Discrete-time Markov chain
approach to contact-based disease spreading in complex networks. _Europhys._ _Lett._, 89(3):38009, 2010.

[459] Joan T Matamalas, Alex Arenas, and Sergio G´omez. Effective approach to epidemic containment using link equations in
complex networks. _Sci._ _Adv._, 4(12):eaau4212, 2018.

[460] Joan T. Matamalas, Sergio G´omez, and Alex Arenas. Abrupt phase transition of epidemic spreading in simplicial
complexes. _Phys._ _Rev._ _Research_, 2(1):012049, 2020.

[461] Michelle Girvan and M. E. J Newman. Community structure in social and biological networks. _Proc._ _Natl._ _Acad._ _Sci._
_U.S.A._, 99(12):7821–7826, 2002.

[462] M. E. J Newman and Juyong Park. Why social networks are different from other types of networks. _Phys._ _Rev._ _E_, 68(3):
036122, 2003.

[463] Joel C Miller. Spread of infectious disease through clustered populations. _J_ _R._ _Soc_ _Interface_, 6(41):1121–1134, 2009.

[464] Martin Ritchie, Luc Berthouze, Thomas House, and Istvan Z Kiss. Higher-order structure and epidemic dynamics in
clustered networks. _J._ _Theor._ _Biol._, 348:21–32, 2014.

[465] David JP O’Sullivan, Gary James O’Keeffe, Peter G Fennell, and James P Gleeson. Mathematical modeling of complex
contagion on clustered networks. _Front._ _Phys._, 3:71, 2015.

[466] Laurent H´ebert-Dufresne and Benjamin M Althouse. Complex dynamics of synergistic coinfections on realistically clustered networks. _Proc._ _Natl._ _Acad._ _Sci._ _U.S.A_, 112(33):10551–10556, 2015.

[467] Guillaume St-Onge, Vincent Thibeault, Antoine Allard, Louis J. Dub´e, and Laurent H´ebert-Dufresne. Master equation
analysis of mesoscopic localization in contagion dynamics on higher-order networks. 2020.

[468] Laurent H´ebert-Dufresne, Dina Mistry, and Benjamin M Althouse. Spread of infectious disease and social awareness as
parasitic contagions on clustered networks. _arXiv:2003.10604_, 2020.

[469] Guang-Yong Yang, Zhao-Long Hu, and Jian-Guo Liu. Knowledge diffusion in the collaboration hypernetwork. _Physica_
_A_, 419:429–436, 2015.

[470] Jiang-Pan Wang, Qiang Guo, Guang-Yong Yang, and Jian-Guo Liu. Improved knowledge diffusion model based on the
collaboration hypernetwork. _Physica_ _A_, 428:250–256, 2015.

[471] Gongzhuang Peng, Hongwei Wang, Heming Zhang, and Keke Huang. A hypernetwork-based approach to collaborative
retrieval and reasoning of engineering design knowledge. _Adv._ _Eng._ _Software_, 42:100956, 2019.

[472] Agnes [´] Bod´o, Gyula Y Katona, and P´eter L Simon. SIS epidemic propagation on hypergraphs. _Bull._ _Math._ _Biol._, 78(4):
713–735, 2016.

[473] G Ghoshal, LM Sander, and IM Sokolov. Sis epidemics with household structure: the self-consistent field method. _Math._
_Bio._, 190(1):71–85, 2004.

[474] Thomas House and Matt J Keeling. Deterministic epidemic models with explicit household structure. _Math._ _Biosci._, 213
(1):29–39, 2008.

[475] Frank Ball, Tom Britton, Thomas House, Valerie Isham, Denis Mollison, Lorenzo Pellis, and Gianpaolo Scalia Tomba.
Seven challenges for metapopulation models of epidemics, including households models. _Epidemics_, 10:63–67, 2015.

[476] Mark Granovetter. Threshold models of collective behavior. _Am._ _J._ _Sociol._, 83(6):1420–1443, 1978.

[477] M´arton Karsai, Gerardo Iniguez, Kimmo Kaski, and J´anos Kert´esz. Complex contagion process in spreading of online
innovation. _J._ _R._ _Soc._ _Interface_, 11(101):20140694, 2014.

[478] Qi Suo, Jin-Li Guo, and Ai-Zhong Shen. Information spreading dynamics in hypernetworks. _Phys._ _A_, 495:475–487, 2018.

[479] Bukyoung Jhun, Minjae Jo, and B Kahng. Simplicial SIS model in scale-free uniform hypergraph. _J._ _Stat._ _Mech.:_ _Theory_
_Exp._, 2019(12):123207, 2019.

[480] Sven L¨ubeck. Universal scaling behavior of non-equilibrium phase transitions. _Int._ _J._ _Mod._ _Phys._ _B_, 18(31n32):3977–4118,
2004.

[481] Silvio C Ferreira, Claudio Castellano, and Romualdo Pastor-Satorras. Epidemic thresholds of the susceptible-infectedsusceptible model on networks: A comparison of numerical and theoretical results. _Phys._ _Rev._ _E_, 86(4):041125, 2012.

[482] Guilherme Ferraz de Arruda, Michele Tizzani, and Yamir Moreno. Phase transitions and stability of dynamical processes
on hypergraphs. _arXiv:2005.10891_, 2020.

[483] Drude Dahlerup. From a small to a large minority: Women in Scandinavian politics. _Scand_ _Polit._ _Stud_, 11(4):275–298,
1988.

[484] Sandra Grey. Numbers and beyond: The relevance of critical mass in gender research. _Polit._ _Gend._, 2(4):492–502, 2006.

[485] Damon Centola, Joshua Becker, Devon Brackbill, and Andrea Baronchelli. Experimental evidence for tipping points in
social convention. _Science_, 360(6393):1116–1119, 2018.

[486] Tao Ma and Jinli Guo. Study on information transmission model of enterprise informal organizations based on the
hypernetwork. _Chin._ _J._ _Phys._, 56(5):2424–2438, 2018.

[487] Klaus Dietz. Epidemics and rumours: A survey. _J_ _R._ _Stat_ _Soc_, 130(4):505–528, 1967.

[488] Yamir Moreno, Maziar Nekovee, and Amalio F Pacheco. Dynamics of rumor spreading in complex networks. _Phys._ _Rev._
_E_, 69(6):066130, 2004.

[489] Thomas Milton Liggett. _Interacting_ _Particle_ _Systems_, volume 276. Springer Science & Business Media, 2012.

[490] Jia Shao, Shlomo Havlin, and H Eugene Stanley. Dynamic opinion model and invasion percolation. _Phys._ _Rev._ _Lett._, 103
(1):018701, 2009.

[491] Krzysztof Suchecki, Victor M Eguiluz, and Maxi San Miguel. Conservation laws for the voter model in complex networks.
_Europhys._ _Lett._, 69(2):228, 2004.


102


[492] Krzysztof Suchecki, V´ıctor M Egu´ıluz, and Maxi San Miguel. Voter model dynamics in complex networks: Role of
dimensionality, disorder, and degree distribution. _Phys._ _Rev._ _E_, 72(3):036132, 2005.

[493] Marina Diakonova, Vincenzo Nicosia, Vito Latora, and Maxi San Miguel. Irreducibility of multilayer network dynamics:
The case of the voter model. _New_ _J._ _Phys._, 18(2):023010, 2016.

[494] Juan Fern´andez-Gracia, Krzysztof Suchecki, Jos´e J Ramasco, Maxi San Miguel, and V´ıctor M Egu´ıluz. Is the voter model
a model for voters? _Phys._ _Rev._ _Lett._, 112(15):158701, 2014.

[495] Michael Kearns, Siddharth Suri, and Nick Montfort. An experimental study of the coloring problem on human subject
networks. _Science_, 313(5788):824–827, 2006.

[496] Stephen Judd, Michael Kearns, and Yevgeniy Vorobeychik. Behavioral dynamics and influence in networked coloring and
consensus. _Proc._ _Natl._ _Acad._ _Sci._ _U.S.A._, 107(34):14978–14982, 2010.

[497] Fan Chung and Alexander Tsiatas. Hypergraph coloring games and voter models. _Internet_ _Math._, 10(1-2):66–86, 2014.

[498] Sidney Redner. Reality-inspired voter models: A mini-review. _Comptes_ _Rendus_ _Phys._, 2019.

[499] Federico Vazquez, V´ıctor M Egu´ıluz, and Maxi San Miguel. Generic absorbing transition in coevolution dynamics. _Phys._
_Rev._ _Lett._, 100(10):108702, 2008.

[500] Leonhard Horstmeyer and Christian Kuehn. Adaptive voter model on simplicial complexes. _Phys._ _Rev._ _E_, 101(2):022305,
2020.

[501] Serge Galam. Minority opinion spreading in random geometry. _Eur._ _Phys._ _J._ _B_, 25(4):403–406, 2002.

[502] Duncan J Watts. A simple model of global cascades on random networks. _Proc._ _Natl._ _Acad._ _Sci._ _U.S.A._, 99(9):5766–5771,
2002.

[503] Nicolas Lanchier and Jared Neufer. Stochastic dynamics on hypergraphs and the spatial majority rule model. _J._ _Stat._
_Phys._, 151(1-2):21–45, 2013.

[504] Mario J de Oliveira. Isotropic majority-vote model on a square lattice. _J._ _Stat._ _Phys._, 66(1-2):273–281, 1992.

[505] Luiz FC Pereira and FG Brady Moreira. Majority-vote model on random graphs. _Phys._ _Rev._ _E_, 71(1):016123, 2005.

[506] Paulo RA Campos, Viviane M de Oliveira, and FG Brady Moreira. Small-world effects in the majority-vote model. _Phys._
_Rev._ _E_, 67(2):026104, 2003.

[507] Edina MS Luz and FWS Lima. Majority-vote on directed small-world networks. _Int._ _J._ _Mod._ _Phys._ _C_, 18(08):1251–1261,
2007.

[508] FWS Lima. Majority-vote on directed Barabasi–Albert networks. _Int._ _J._ _Mod._ _Phys._ _C_, 17(09):1257–1265, 2006.

[509] FWS Lima. Majority-vote on undirected Barab´asi-Albert networks. _Commun._ _Comput._ _Phys._, 2(2):358–366, 2007.

[510] Tomasz Gradowski and Andrzej Krawiecki. Majority-vote model on scale-free hypergraphs. _Acta_ _Phys_ _Pol_, 127(3A):1–4,
2015.

[511] Hyunsuk Hong, Meesoon Ha, and Hyunggyu Park. Finite-size scaling in complex networks. _Phys._ _Rev._ _Lett._, 98(25):
258701, 2007.

[512] Guillaume Deffuant, David Neau, Frederic Amblard, and G´erard Weisbuch. Mixing beliefs among interacting agents.
_Adv._ _Complex_ _Syst._, 3(01n04):87–98, 2000.

[513] Jan Lorenz. Continuous opinion dynamics under bounded confidence: A survey. _Int._ _J._ _Mod._ _Phys._ _C_, 18(12):1819–1838,
2007.

[514] Solomon E Asch and Harold Guetzkow. Effects of group pressure upon the modification and distortion of judgments.
_Doc._ _Gestalt_ _Psychol._, pages 222–236, 1951.

[515] Robert Axelrod. The dissemination of culture: A model with local convergence and global polarization. _J_ _Confl_ _Resolut_,
41(2):203–226, 1997.

[516] Federico Battiston, Vincenzo Nicosia, Vito Latora, and Maxi San Miguel. Layered social influence promotes multiculturality in the Axelrod model. _Sci._ _Rep._, 7(1):1809, 2017.

[517] Slobodan Maleti´c and Milan Rajkovi´c. Consensus formation on a simplicial complex of opinions. _Phys._ _A_, 397:111–120,
2014.

[518] Slobodan Maleti´c and Yi Zhao. Hidden multidimensional social structure modeling applied to biased social perception.
_Phys._ _A_, 492:1419–1430, 2018.

[519] Carlos P Roca, Jos´e A Cuesta, and Angel S´anchez. Evolutionary game theory: Temporal and spatial effects beyond
replicator dynamics. _Physics_ _of_ _life_ _reviews_, 6(4):208–249, 2009.

[520] Gy¨orgy Szab´o, Attila Szolnoki, and Rudolf Izs´ak. Rock-scissors-paper game on regular small-world networks. _J._ _Phys._
_Math._ _Gen._, 37(7):2599, 2004.

[521] Attila Szolnoki, Mauro Mobilia, Luo-Luo Jiang, Bartosz Szczesny, Alastair M Rucklidge, and Matjaˇz Perc. Cyclic
dominance in evolutionary games: a review. _Journal_ _of_ _the_ _Royal_ _Society_ _Interface_, 11(100):20140735, 2014.

[522] R. Axelrod and R.M. Axelrod. _The_ _Evolution_ _of_ _Cooperation_ . Basic Books. Basic Books, 1984. ISBN 978-0-465-02121-5.

[523] A. Rapoport and M. Guyer. _A_ _Taxonomy_ _of_ _2_ _x_ _2_ _Games,_ _by_ _Anatol_ _Rapoport_ _and_ _Melvin_ _Guyer_ . Bobbs-Merrill Reprint
Series in the Social Sciences, S617. 1966.

[524] Jean-Jacques Rousseau. The discourses and other political writings. 1997.

[525] RD Luce and H Raiffa. Games and decisions: Introduction and critical survey, 2012 ed. 1957.

[526] Benedetto Gui and Robert Sugden. _Economics and Social Interaction:_ _Accounting for Interpersonal Relations_ . Cambridge
University Press, 2005.

[527] John Maynard Smith. _Evolution_ _and_ _the_ _Theory_ _of_ _Games_ . Cambridge university press, 1982.

[528] John Maynard Smith and Geoffrey A Parker. The logic of asymmetric contests. _Anim._ _Behav._, 24(1):159–175, 1976.

[529] R Cressman. Evolutionary stability for two-stage hawk-dove games. _Rocky_ _Mt._ _J._ _Math._, pages 145–155, 1995.

[530] J Maynard Smith. Game theory and the evolution of fighting. _Evol._, pages 8–28, 1972.


103


[531] Sigurd Diederich and Manfred Opper. Replicators with random interactions: A solvable model. _Phys._ _Rev._ _A_, 39(8):
4333, 1989.

[532] Josef Hofbauer and Karl Sigmund. _Evolutionary_ _Games_ _and_ _Population_ _Dynamics_ . Cambridge university press, 1998.

[533] Manfred Opper and Sigurd Diederich. Replicator dynamics. _Comput._ _Phys._ _Commun._, 121:141–144, 1999.

[534] Tsuyoshi Chawanya and Kei Tokita. Large-dimensional replicator equations with antisymmetric random interactions. _J._
_Phys._ _Soc._ _Jpn._, 71(2):429–431, 2002.

[535] Matjaˇz Perc and Attila Szolnoki. Coevolutionary gamesa mini review. _BioSystems_, 99(2):109–125, 2010.

[536] Garrett Hardin. The tragedy of the commons. _science_, 162(3859):1243–1248, 1968.

[537] Martin A Nowak and Robert M May. Evolutionary games and spatial chaos. _Nature_, 359(6398):826–829, 1992.

[538] Francisco C Santos and Jorge M Pacheco. Scale-free networks provide a unifying framework for the emergence of cooperation. _Phys._ _Rev._ _Lett._, 95(9):098104, 2005.

[539] Jes´us G´omez-Gardenes, M Campillo, LM Flor´ıa, and Yamir Moreno. Dynamical organization of cooperation in complex
topologies. _Phys._ _Rev._ _Lett._, 98(10):108103, 2007.

[540] Salvatore Assenza, Jes´us G´omez-Garde˜nes, and Vito Latora. Enhancement of cooperation in highly clustered scale-free
networks. _Phys._ _Rev._ _E_, 78(1):017101, 2008.

[541] Christoph Hauert and Michael Doebeli. Spatial structure often inhibits the evolution of cooperation in the snowdrift
game. _Nature_, 428(6983):643–646, 2004.

[542] Martin A Nowak. Five rules for the evolution of cooperation. _Science_, 314(5805):1560–1563, 2006.

[543] Gy¨orgy Szab´o and Gabor Fath. Evolutionary games on graphs. _Phys._ _Rep._, 446(4-6):97–216, 2007.

[544] Zhen Wang, Lin Wang, Attila Szolnoki, and Matjaˇz Perc. Evolutionary games on multilayer networks: a colloquium. _The_
_European_ _physical_ _journal_ _B_, 88(5):124, 2015.

[545] Karl Sigmund. _The_ _Calculus_ _of_ _Selfishness_, volume 6. Princeton University Press, 2010.

[546] M Archetti and I Scheuring. Review: Evolution of cooperation in one-shot social dilemmas without assortment. _J_ _Theor_
_Biol_, 299:9–20, 2012.

[547] Matjaˇz Perc, Jes´us G´omez-Garde˜nes, Attila Szolnoki, Luis M Flor´ıa, and Yamir Moreno. Evolutionary dynamics of group
interactions on structured populations: A review. _J._ _R._ _Soc._ _Interface_, 10(80):20120997, 2013.

[548] Matjaˇz Perc, Jillian J Jordan, David G Rand, Zhen Wang, Stefano Boccaletti, and Attila Szolnoki. Statistical physics of
human cooperation. _Physics_ _Reports_, 687:1–51, 2017.

[549] Jorge Pe˜na, Bin Wu, Jordi Arranz, and Arne Traulsen. Evolutionary games of multiplayer cooperation on graphs. _PLoS_
_Comput._ _Biol._, 12(8), 2016.

[550] Gy¨orgy Szab´o and Christoph Hauert. Phase transitions and volunteering in spatial public goods games. _Phys._ _Rev._ _Lett._,
89(11):118101, 2002.

[551] Hannelore Brandt, Christoph Hauert, and Karl Sigmund. Punishment and reputation in spatial public goods games. _Proc_
_R_ _Soc_ _Lond_ _B_, 270(1519):1099–1104, 2003.

[552] Francisco C Santos, Marta D Santos, and Jorge M Pacheco. Social diversity promotes the emergence of cooperation in
public goods games. _Nature_, 454(7201):213–216, 2008.

[553] Zhihai Rong and Zhi-Xi Wu. Effect of the degree correlation in public goods game on scale-free networks. _Europhys._
_Lett._, 87(3):30001, 2009.

[554] Zhihai Rong, Han-Xin Yang, Wen-Xu Wang, et al. Feedback reciprocity mechanism promotes the cooperation of highly
clustered scale-free networks. _Phys._ _Rev._ _E_, 82(4):047101, 2010.

[555] Jia Gao, Zhi Li, Te Wu, and Long Wang. Diversity of contribution promotes cooperation in public goods games. _Phys._
_A_, 389(16):3166–3171, 2010.

[556] Jeromos Vukov, Francisco C Santos, and Jorge M Pacheco. Escaping the tragedy of the commons via directed investments.
_J._ _Theor._ _Biol._, 287:37–41, 2011.

[557] Attila Szolnoki and Matjaˇz Perc. Group-size effects on the evolution of cooperation in the spatial public goods game.
_Phys._ _Rev._ _E_, 84(4):047102, 2011.

[558] Matja Perc and Paolo Grigolini. Collective behavior and evolutionary games an introduction. _Chaos,_ _Solitons_ _&_ _Fractals_,
56:1    - 5, 2013. ISSN 0960-0779. Collective Behavior and Evolutionary Games.

[559] Attila Szolnoki, Matjaˇz Perc, and Gy¨orgy Szab´o. Topology-independent impact of noise on cooperation in spatial public
goods games. _Physical_ _Review_ _E_, 80:056109, 2009. [doi:10.1103/PhysRevE.80.056109.](http://dx.doi.org/10.1103/PhysRevE.80.056109)

[560] Attila Szolnoki and Matjaˇz Perc. Correlation of positive and negative reciprocity fails to confer an evolutionary advantage:
Phase transitions to elementary strategies. _Physical_ _Review_ _X_, 3:041021, 2013. [doi:10.1103/PhysRevX.3.041021.](http://dx.doi.org/10.1103/PhysRevX.3.041021)

[561] Dirk Helbing, Attila Szolnoki, Matjaˇz Perc, and Gy¨orgy Szab´o. Evolutionary establishment of moral and double moral
standards through spatial interactions. _PLoS Computational Biology_, 6:e1000758, 2010. [doi:10.1371/journal.pcbi.1000758.](http://dx.doi.org/10.1371/journal.pcbi.1000758)

[562] Zhen Wang, Attila Szolnoki, and Matjaˇz Perc. Evolution of public cooperation on interdependent networks: The impact
of biased utility functions. _Europhys._ _Lett._, 97(4):48001, 2012.

[563] Zhen Wang, Attila Szolnoki, and Matjaˇz Perc. Interdependent network reciprocity in evolutionary games. _Sci._ _Rep._, 3:
1183, 2013.

[564] Federico Battiston, Vincenzo Nicosia, and Vito Latora. Structural measures for multiplex networks. _Phys._ _Rev._ _E_, 89(3):
032804, 2014.

[565] Federico Battiston, Matjaˇz Perc, and Vito Latora. Determinants of public cooperation in multiplex networks. _New_ _J._
_Phys._, 19(7):073017, 2017.

[566] Carlos P Roca and Dirk Helbing. Emergence of social cohesion in a model society of greedy, mobile individuals. _Proceedings_
_of_ _the_ _National_ _Academy_ _of_ _Sciences_, 108(28):11370–11374, 2011.


104


[567] Elgar Pichler and Avi M Shapiro. Public goods games on adaptive coevolutionary networks. _Chaos:_ _An_ _Interdisciplinary_
_Journal_ _of_ _Nonlinear_ _Science_, 27(7):073107, 2017.

[568] Guangming Ren, Lan Liu, Mingku Feng, and Yingji He. Coevolution of public goods game and networks based on survival
of the fittest. _PloS_ _one_, 13(9), 2018.

[569] Chen Shen, Chen Chu, Lei Shi, Marko Jusup, Matjaˇz Perc, and Zhen Wang. Coevolutionary resolution of the public
goods dilemma in interdependent structured populations. _EPL_ _(Europhysics_ _Letters)_, 124(4):48003, 2018.

[570] Matjaˇz Perc. Stability of subsystem solutions in agent-based models. _European_ _Journal_ _of_ _Physics_, 39:014001, 2018.
[doi:10.1088/1361-6404/aa903d.](http://dx.doi.org/10.1088/1361-6404/aa903d)

[571] Marco Alberto Javarone and Federico Battiston. The role of noise in the spatial public goods game. _Journal_ _of_ _Statistical_
_Mechanics:_ _Theory_ _and_ _Experiment_, 2016(7):073404, 2016.

[572] Da-Fang Zheng, HP Yin, Chun-Him Chan, and PM Hui. Cooperative behavior in a model of evolutionary snowdrift
games with N-person interactions. _Europhys._ _Lett._, 80(1):18002, 2007.

[573] Marta D Santos, Flavio L Pinheiro, Francisco C Santos, and Jorge M Pacheco. Dynamics of N-person snowdrift games
in structured populations. _J._ _Theor._ _Biol._, 315:81–86, 2012.

[574] Kwang Hwan Ji, Ji-In Kim, Hong Yoon Jung, Se Yeob Park, Rino Choi, Un Ki Kim, Cheol Seong Hwang, Daeseok
Lee, Hyungsang Hwang, and Jae Kyeong Jeong. Effect of high-pressure oxygen annealing on negative bias illumination
stress-induced instability of InGaZnO thin film transistors. _Appl._ _Phys._ _Lett._, 98(10):103509, 2011.

[575] Jorge M Pacheco, Francisco C Santos, Max O Souza, and Brian Skyrms. Evolutionary dynamics of collective action in
N-person stag hunt dilemmas. _Proc._ _R._ _Soc._ _B_ _Biol._ _Sci._, 276(1655):315–321, 2009.

[576] Max O Souza, Jorge M Pacheco, and Francisco C Santos. Evolution of cooperation under N-person snowdrift games. _J._
_Theor._ _Biol._, 260(4):581–588, 2009.

[577] Francisco C Santos and Jorge M Pacheco. Risk of collective failure provides an escape from the tragedy of the commons.
_Proc._ _Natl._ _Acad._ _Sci._, 108(26):10421–10425, 2011.

[578] Wei Chen, Carlos Gracia-L´azaro, Zhiwu Li, Long Wang, and Yamir Moreno. Evolutionary dynamics of n-person hawkdove games. _Sci._ _Rep._, 7(1):1–10, 2017.

[579] Werner G¨uth, Rolf Schmittberger, and Bernd Schwarze. An experimental analysis of ultimatum bargaining. _Journal_ _of_
_economic_ _behavior_ _&_ _organization_, 3(4):367–388, 1982.

[580] Roberta Sinatra, Jaime Iranzo, Jesus Gomez-Gardenes, Luis M Floria, Vito Latora, and Yamir Moreno. The ultimatum
game in complex networks. _Journal_ _of_ _Statistical_ _Mechanics:_ _Theory_ _and_ _Experiment_, 2009(09):P09012, 2009.

[581] Fernando P Santos, Francisco C Santos, Ana Paiva, and Jorge M Pacheco. Evolutionary dynamics of group fairness.
_Journal_ _of_ _theoretical_ _biology_, 378:96–102, 2015.

[582] Jesus Gomez-Gardenes, Miguel Romance, Regino Criado, Daniele Vilone, and Angel S´anchez. Evolutionary games defined
at the network mesoscale: The public goods game. _Chaos_ _Interdiscip._ _J._ _Nonlinear_ _Sci._, 21(1):016113, 2011.

[583] Jes´us G´omez-Garde˜nes, Daniele Vilone, and Angel S´anchez. Disentangling social and group heterogeneities: Public goods
games on complex networks. _Europhys._ _Lett._, 95(6):68003, 2011.

[584] Jorge Pe˜na and Yannick Rochat. Bipartite graphs as models of population structures in evolutionary multiplayer games.
_PLOS_ _ONE_, 7(9), 2012.

[585] Carlos Gracia-Lazaro, Jesus Gomez-Gardenes, Luis Mario Floria, and Yamir Moreno. Intergroup information exchange
drives cooperation in the public goods game. _Phys._ _Rev._ _E_, 90(4):042808, 2014.

[586] Unai Alvarez-Rodriguez, Federico Battiston, Guilherme Ferraz de Arruda, Yamir Moreno, Matjaz Perc, and Vito Latora.
Evolutionary dynamics of higher-order interactions. _arXiv:2001.10313_, 2020.

[587] Andrea Baronchelli, Maddalena Felici, Vittorio Loreto, Emanuele Caglioti, and Luc Steels. Sharp transition towards
shared vocabularies in multi-agent systems. _Journal_ _of_ _Statistical_ _Mechanics:_ _Theory_ _and_ _Experiment_, 2006(06):P06014,
2006.

[588] Andrea Baronchelli, Luca DallAsta, Alain Barrat, and Vittorio Loreto. Topology-induced coarsening in language games.
_Physical_ _Review_ _E_, 73(1):015102, 2006.

[589] Uri Gneezy. Deception: The role of consequences. _American_ _Economic_ _Review_, 95(1):384–394, 2005.

[590] Valerio Capraro, Matjaˇz Perc, and Daniele Vilone. The evolution of lying in well-mixed populations. _Journal_ _of_ _the_ _Royal_
_Society_ _Interface_, 16:20190211, 2019. [doi:10.1098/rsif.2019.0211.](http://dx.doi.org/10.1098/rsif.2019.0211)

[591] Valerio Capraro, Matjaˇz Perc, and Daniele Vilone. Lying on networks: The role of structure and topology in promoting
honesty. _Physical_ _Review_ _E_, 101:032305, 2020. [doi:10.1103/PhysRevE.101.032305.](http://dx.doi.org/10.1103/PhysRevE.101.032305)

[592] Manfred Milinski, Ralf D Sommerfeld, Hans-J¨urgen Krambeck, Floyd A Reed, and Jochem Marotzke. The collectiverisk social dilemma and the prevention of simulated dangerous climate change. _Proceedings_ _of_ _the_ _National_ _Academy_ _of_
_Sciences_, 105(7):2291–2294, 2008.

[593] Linton C. Freeman. Q-analysis and the structure of friendship networks. _Int._ _J._ _Man-Mach._ _Stud._, 12(4):367–378, 1980.

[594] Miroslav Andjelkovi´c, Bosiljka Tadi´c, Slobodan Maleti´c, and Milan Rajkovi´c. Hierarchical sequencing of online social
graphs. _Phys._ _A_, 436:582–595, 2015.

[595] S. Mangan and U. Alon. Structure and function of the feed-forward loop network motif. _Proc._ _Natl._ _Acad._ _Sci._, 100(21):
11980–11985, 2003.

[596] Elena Kuzmin, Benjamin VanderSluis, Wen Wang, Guihong Tan, Raamesh Deshpande, Yiqun Chen, Matej Usaj, Attila
Balint, Mojca Mattiazzi Usaj, Jolanda van Leeuwen, Elizabeth N. Koch, Carles Pons, Andrius J. Dagilis, Michael Pryszlak,
Jason Zi Yang Wang, Julia Hanchard, Margot Riggi, Kaicong Xu, Hamed Heydari, Bryan-Joseph San Luis, Ermira
Shuteriqi, Hongwei Zhu, Nydia Van Dyk, Sara Sharifpoor, Michael Costanzo, Robbie Loewith, Amy Caudy, Daniel
Bolnick, Grant W. Brown, Brenda J. Andrews, Charles Boone, and Chad L. Myers. Systematic analysis of complex


105


genetic interactions. _Science_, 360(6386), 2018.

[597] Elad Schneidman, Susanne Still, Michael J Berry, William Bialek, et al. Network information and connected correlations.
_Phys._ _Rev._ _Lett._, 91(23):238701, 2003.

[598] Giovanni Petri, Paul Expert, Federico Turkheimer, Robin Carhart-Harris, David Nutt, Peter J Hellyer, and Francesco
Vaccarino. Homological scaffolds of brain functional networks. _J._ _R._ _Soc._ _Interface_, 11(101):20140873, 2014.

[599] Esther Ib´a˜nez-Marcelo, Lisa Campioni, Angkoon Phinyomark, Giovanni Petri, and Enrica L Santarcangelo. Topology
highlights mesoscopic functional equivalence between imagery and perception: The case of hypnotizability. _NeuroImage_,
200:437–449, 2019.

[600] J.Miller McPherson. Hypernetwork sampling: Duality and differentiation among voluntary organizations. _Soc._ _Netw._, 3
(4):225–249, 1982.

[601] Brian Foster and Stephen Seidman. Urban structures derived from collections of overlapping subsets. _Urban_ _Anthropol._,
11:177–192, 1982.

[602] B.L. Foster and Stephen Seidman. Overlap structure of ceremonial events in two Thai villages. _Thai_ _J._ _Dev._ _Adm._, 24:
143–157, 1984.

[603] Katherine Faust. Centrality in affiliation networks. _Soc._ _Netw._, 19(2):157–191, 1997.

[604] Phillip Bonacich. Power and centrality: A family of measures. _Am._ _J._ _Sociol._, 92(5):1170–1182, 1987.

[605] S. Wylie. Mathematical structure in human affairs, by R. H. Atkin. _Math._ _Gaz._, 60(411):69–70, 1976.

[606] Patrick Doreian. On the evolution of group and network structure. _Soc._ _Netw._, 2(3):235–252, 1979.

[607] Peter Gould and Anthony Gatrell. A structural analysis of a game: The Liverpool v Manchester united cup final of 1977.
_Soc._ _Netw._, 2(3):253–273, 1979.

[608] Luca Pappalardo, Paolo Cintia, Alessio Rossi, Emanuele Massucco, Paolo Ferragina, Dino Pedreschi, and Fosca Giannotti.
A public data set of spatio-temporal match events in soccer competitions. _Sci._ _Data_, 6(1):236, 2019.

[609] Tianchong Gao and Feng Li. Studying the utility preservation in social network anonymization via persistent homology.
_Comput._ _Secur._, 77:49–64, 2018.

[610] Ciro Catutto, Christoph Schmitz, Andrea Baldassarri, Vito D. P. Servedio, Vittorio Loreto, and Andreas Hotho, Miranda
Grahl, and Gerd Stumme. Network properties of folksonomies. _AI_ _Commun._ _J._ _Spec._ _Issue_ _Netw._ _Anal._ _Nat._ _Sci._ _Eng._,
2007.

[611] Vito Latora, Vincenzo Nicosia, and Pietro Panzarasa. Social cohesion, structural holes, and a tale of two measures. _J_
_Stat_ _Phys_, (151):745–764, 2013.

[612] Staˇsa Milojevi´c. Principles of scientific research team formation and evolution. _Proc._ _Natl._ _Acad._ _Sci._, 111(11):3984–3989,
2014.

[613] Quan Xiao. Node importance measure for scientific research collaboration from hypernetwork perspective. _Teh._ _Vjesn._,
23(2):397–404, 2016.

[614] M. E. J. Newman. Scientific collaboration networks. I. Network construction and fundamental results. _Phys._ _Rev._ _E_, 64
(1):016131, 2001.

[615] M. E. J. Newman. Scientific collaboration networks. II. Shortest paths, weighted networks, and centrality. _Phys._ _Rev._ _E_,
64(1):016132, 2001.

[616] M. E. J. Newman. The structure of scientific collaboration networks. _Proc._ _Natl._ _Acad._ _Sci._, 98(2):404–409, 2001.

[617] Ginestra Bianconi, Richard K Darst, Jacopo Iacovacci, and Santo Fortunato. Triadic closure as a basic generating
mechanism of communities in complex networks. _Phys._ _Rev._ _E_, 90(4):042806, 2014.

[618] Elad Schneidman, Michael J Berry II, Ronen Segev, and William Bialek. Weak pairwise correlations imply strongly
correlated network states in a neural population. _Nature_, 440(7087):1007, 2006.

[619] Elad Ganmor, Ronen Segev, and Elad Schneidman. Sparse low-order interaction network underlies a highly correlated
and learnable neural population code. _Proc._ _Natl._ _Acad._ _Sci._, 108(23):9679–9684, 2011.

[620] Shan Yu, Hongdian Yang, Hiroyuki Nakahara, Gustavo S Santos, Danko Nikoli´c, and Dietmar Plenz. Higher-order
interactions characterized in cortical activity. _J._ _Neurosci._, 31(48):17514–17526, 2011.

[621] Hideaki Shimazaki, Shun-ichi Amari, Emery N Brown, and Sonja Gr¨un. State-space analysis of time-varying higher-order
spike correlation for multiple neural spike train data. _PLoS_ _Comput._ _Biol._, 8(3):e1002385, 2012.

[622] Urs K¨oster, Jascha Sohl-Dickstein, Charles M Gray, and Bruno A Olshausen. Modeling higher-order correlations within
cortical microcolumns. _PLoS_ _Comput._ _Biol._, 10(7):e1003684, 2014.

[623] Hideaki Shimazaki, Kolia Sadeghi, Tomoe Ishikawa, Yuji Ikegaya, and Taro Toyoizumi. Simultaneous silence organizes
structured higher-order interactions in neural populations. _Sci._ _Rep._, 5:9821, 2015.

[624] Natasha A Cayco-Gajic, Joel Zylberberg, and Eric Shea-Brown. Triplet correlations among similarly tuned cells impact
population coding. _Front._ _Comput._ _Neurosci._, 9:57, 2015.

[625] Chad Giusti, Eva Pastalkova, Carina Curto, and Vladimir Itskov. Clique topology reveals intrinsic geometric structure
in neural correlations. _Proc._ _Natl._ _Acad._ _Sci._, 112(44):13455–13460, 2015.

[626] Yuri Dabaghian, Facundo M´emoli, Loren Frank, and Gunnar Carlsson. A topological paradigm for hippocampal spatial
map formation using persistent homology. _PLoS_ _Comput._ _Biol._, 8(8):e1002581, 2012.

[627] Yuri Dabaghian, Vicky L Brandt, and Loren M Frank. Reconceiving the hippocampal map as a topological template.
_Elife_, 3:e03476, 2014.

[628] Andrey Babichev, Dmitriy Morozov, and Yuri Dabaghian. Robust spatial memory maps encoded by networks with
transient connections. _PLoS_ _Comput._ _Biol._, 14(9):e1006433, 2018.

[629] Michael W Reimann, Max Nolte, Martina Scolamiero, Katharine Turner, Rodrigo Perin, Giuseppe Chindemi, Pawe�l
D�lotko, Ran Levi, Kathryn Hess, and Henry Markram. Cliques of neurons bound into cavities provide a missing link


106


between structure and function. _Front._ _Comput._ _Neurosci._, 11:48, 2017.

[630] Xuhui Huang, Kaibin Xu, Congying Chu, Tianzi Jiang, and Shan Yu. Weak higher-order interactions in macroscopic
functional networks of the resting brain. _J._ _Neurosci._, 37(43):10481–10497, 2017.

[631] Han Zhang, Xiaobo Chen, Yu Zhang, and Dinggang Shen. Test-retest reliability of “high-order” functional connectivity
in young healthy adults. _Front._ _Neurosci._, 11:439, 2017.

[632] Sergey M Plis, Jing Sui, Terran Lane, Sushmita Roy, Vincent P Clark, Vamsi K Potluru, Rene J Huster, Andrew
Michael, Scott R Sponheim, Michael P Weisend, et al. High-order interactions observed in multi-task intrinsic networks
are dominant indicators of aberrant brain function in schizophrenia. _Neuroimage_, 102:35–48, 2014.

[633] Han Zhang, Xiaobo Chen, Feng Shi, Gang Li, Minjeong Kim, Panteleimon Giannakopoulos, Sven Haller, and Dinggang
Shen. Topographical information-based high-order functional connectivity and its application in abnormality detection
for mild cognitive impairment. _J._ _Alzheimers_ _Dis._, 54(3):1095–1112, 2016.

[634] Hyekyoung Lee, Hyejin Kang, Moo K Chung, Seonhee Lim, Bung-Nyun Kim, and Dong Soo Lee. Integrated multimodal
network approach to PET and MRI based on multidimensional persistent homology. _Hum. Brain Mapp._, 38(3):1387–1402,
2017.

[635] Hyekyoung Lee, Moo K Chung, Hyejin Kang, and Dong Soo Lee. Hole detection in metabolic connectivity of Alzheimer’s
disease using k- Laplacian. In _International Conference on Medical Image Computing and Computer-Assisted Intervention_,
pages 297–304. Springer, 2014.

[636] Ann E Sizemore, Chad Giusti, Ari Kahn, Jean M Vettel, Richard F Betzel, and Danielle S Bassett. Cliques and cavities
in the human connectome. _J._ _Comput._ _Neurosci._, 44(1):115–145, 2018.

[637] Paul Bendich, James S Marron, Ezra Miller, Alex Pieloch, and Sean Skwerer. Persistent homology analysis of brain artery
trees. _Ann._ _Appl._ _Stat._, 10(1):198, 2016.

[638] Hyekyoung Lee, Hyejin Kang, Moo K Chung, Bung-Nyun Kim, and Dong Soo Lee. Persistent brain network homology
from the perspective of dendrogram. _IEEE_ _Trans._ _Med._ _Imaging_, 31(12):2267–2277, 2012.

[639] Hyekyoung Lee, Moo K Chung, Hyejin Kang, Bung-Nyun Kim, and Dong Soo Lee. Discriminative persistent homology
of brain networks. In _2011_ _IEEE_ _International_ _Symposium_ _on_ _Biomedical_ _Imaging:_ _From_ _Nano_ _to_ _Macro_, pages 841–844.
IEEE, 2011.

[640] Moo K Chung, Victoria Villalta-Gil, Hyekyoung Lee, Paul J Rathouz, Benjamin B Lahey, and David H Zald. Exact
topological inference for paired brain networks via persistent homology. In _International_ _Conference_ _on_ _Information_
_Processing_ _in_ _Medical_ _Imaging_, pages 299–310. Springer, 2017.

[641] Erik Rybakken, Nils Baas, and Benjamin Dunn. Decoding of neural data using cohomological feature extraction. _Neural_
_Comput._, 31(1):68–93, 2019.

[642] Louis-David Lord, Paul Expert, Henrique M Fernandes, Giovanni Petri, Tim J Van Hartevelt, Francesco Vaccarino,
Gustavo Deco, Federico Turkheimer, and Morten L Kringelbach. Insights into brain architectures from the homological
scaffolds of functional connectivity networks. _Front._ _Syst._ _Neurosci._, 10:85, 2016.

[643] Hyekyoung Lee, Moo K Chung, Hongyoon Choi, Hyejin Kang, Seunggyun Ha, Yu Kyeong Kim, and Dong Soo Lee. Harmonic holes as the submodules of brain network and network dissimilarity. In _International_ _Workshop_ _on_ _Computational_
_Topology_ _in_ _Image_ _Context_, pages 110–122. Springer, 2019.

[644] Moo K Chung, Hyekyoung Lee, Alex DiChristofano, Hernando Ombao, and Victor Solo. Exact topological inference of
the resting-state brain networks in twins. _Netw._ _Neurosci._, 3(3):674–694, 2019.

[645] Esther Ib´a˜nez-Marcelo, Lisa Campioni, Diego Manzoni, Enrica L Santarcangelo, and Giovanni Petri. Spectral and
topological analyses of the cortical representation of the head position: Does hypnotizability matter? _Brain_ _Behav._, 9
(6):e01277, 2019.

[646] Manish Saggar, Olaf Sporns, Javier Gonzalez-Castillo, Peter A Bandettini, Gunnar Carlsson, Gary Glover, and Allan L
Reiss. Towards a new approach to reveal dynamical organization of the brain using topological data analysis. _Nat._
_Commun._, 9(1):1–14, 2018.

[647] Cameron T Ellis, Michael Lesnick, Gregory Henselman-Petrusek, Bryn Keller, and Jonathan D Cohen. Feasibility of
topological data analysis for event-related fMRI. _Netw._ _Neurosci._, 3(3):695–706, 2019.

[648] Chad Giusti, Robert Ghrist, and Danielle S Bassett. Two’s company, three (or more) is a simplex. _J._ _Comput._ _Neurosci._,
41(1):1–14, 2016.

[649] Ann E Sizemore, Jennifer E Phillips-Cremins, Robert Ghrist, and Danielle S Bassett. The importance of the whole:
Topological data analysis for the network neuroscientist. _Netw_ _Neurosci_, 3(3):656–673, 2019.

[650] Ted J. Case and Edward A. Bender. Testing for higher order interactions. _Am._ _Nat._, 118(6):920–929, 1981.

[651] Peter A. Abrams. Arguments in favor of higher order interactions. _Am._ _Nat._, 121(6):887–891, 1983.

[652] Peter Kareiva. Special feature: Higher order interactions as a foil to reductionist ecology. _Ecology_, 75(6), 1994.

[653] Ian Billick and Ted J Case. Higher order interactions in ecological communities: What are they and how can they be
detected? _Ecology_, 75(6):1529–1543, 1994.

[654] J Timothy Wootton. Indirect effects and habitat use in an intertidal community: Interaction chains and interaction
modifications. _Am._ _Nat._, 141(1):71–89, 1993.

[655] Eyal Bairey, Eric D. Kelsic, and Roy Kishony. High-order species interactions shape ecosystem diversity. _Nat._ _Commun._,
7(1):12285, 2017.

[656] Eric D Kelsic, Jeffrey Zhao, Kalin Vetsigian, and Roy Kishony. Counteraction of antibiotic production and degradation
stabilizes microbial communities. _Nature_, 521(7553):516, 2015.

[657] Michael H Perlin, Denise R Clark, Courtney McKenzie, Himati Patel, Nikki Jackson, Cecile Kormanik, Cayse Powell,
Alexander Bajorek, David A Myers, Lee A Dugatkin, et al. Protection of Salmonella by ampicillin-resistant Escherichia


107


coli in the presence of otherwise lethal drug concentrations. _Proc._ _R._ _Soc._ _B_ _Biol._ _Sci._, 276(1674):3759–3768, 2009.

[658] Monica I Abrudan, Fokko Smakman, Ard Jan Grimbergen, Sanne Westhoff, Eric L Miller, Gilles P Van Wezel, and
Daniel E Rozen. Socially mediated induction and suppression of antibiosis during bacterial coexistence. _Proc._ _Natl._ _Acad._
_Sci._, 112(35):11054–11059, 2015.

[659] Mariano Koen-Alonso. A process-oriented approach to the multispecies functional response. In _From_ _Energetics_ _to_
_Ecosystems:_ _The_ _Dynamics_ _and_ _Structure_ _of_ _Ecological_ _Systems_, pages 1–36. Springer, 2007.

[660] Viviane M. de Oliveira and J. F. Fontanari. Random replicators with high-order interactions. _Phys._ _Rev._ _Lett._, 85(23):
4984–4987, 2000.

[661] Yoshimi Yoshino, Tobias Galla, and Kei Tokita. Rank abundance relations in evolutionary dynamics of random replicators.
_Phys._ _Rev._ _E_, 78(3):031924, 2008.

[662] Martin Sonntag and Hanns-Martin Teichert. Competition hypergraphs. _Discrete_ _Appl._ _Math._, 143(1):324–329, 2004.

[663] Antonio J Golubski, Erik E Westlund, John Vandermeer, and Mercedes Pascual. Ecological networks over the edge:
Hypergraph trait-mediated indirect interaction (TMII) structure. _Trends_ _Ecol._ _Evol._, 31(5):344–354, 2016.

[664] Robert M May. Will a large complex system be stable? _Nature_, 436:413–414, 1972.

[665] John H. Vandermeer. The competitive structure of communities: An experimental approach with protozoa. _Ecology_, 50
(3):362–371, 1969.

[666] William E. Neill. The community matrix and interdependence of the competition coefficients. _Am._ _Nat._, 108(962):
399–408, 1974.

[667] Carsten F Dormann and Stephen H Roxburgh. Experimental evidence rejects pairwise modelling approach to coexistence
in plant communities. _Proc_ _Biol_ _Sci_, 272(1569):1279–1285, 2005.

[668] Alexandra Weigelt, Jens Schumacher, Tim Walther, Maik Bartelheimer, Tom Steinlein, and Wolfram Beyschlag. Identifying mechanisms of competition in multi-species communities. _J._ _Ecol._, 95(1):53–64, 2007.

[669] Stefano Allesina and Jonathan M Levine. A competitive network theory of species diversity. _Proc._ _Natl._ _Acad._ _Sci._, 108
(14):5638–5642, 2011.

[670] Benjamin Kerr, Margaret A Riley, Marcus W Feldman, and Brendan JM Bohannan. Local dispersal promotes biodiversity
in a real-life game of rock–paper–scissors. _Nature_, 418(6894):171, 2002.

[671] Josef Hofbauer and Karl Sigmund. Evolutionary game dynamics. _Bull._ _Am._ _Math._ _Soc._, 40(4):479–519, 2003.

[672] Martin A Nowak and Karl Sigmund. Evolutionary dynamics of biological games. _science_, 303(5659):793–799, 2004.

[673] Peter D Taylor and Leo B Jonker. Evolutionary stable strategies and game dynamics. _Math._ _Biosci._, 40(1-2):145–156,
1978.

[674] Josef Hofbauer, Peter Schuster, Karl Sigmund, et al. A note on evolutionary stable strategies and game dynamics.
Technical report, David K. Levine, 2010.

[675] Margaret M Mayfield and Daniel B Stouffer. Higher-order interactions capture unexplained complexity in diverse communities. _Nat._ _Ecol._ _Evol._, 1(3):0062, 2017.

[676] Sergi Valverde, Blai Vidiella, Ra´ul Monta˜nez, Aurora Fraile, Soledad Sacrist´an, and Fernando Garc´ıa-Arenal. Coexistence
of nestedness and modularity in host–pathogen infection networks. _Nat._ _Ecol._ _Evol._, pages 1–10, 2020.

[677] Manuel Sebastian Mariani, Zhuo-Ming Ren, Jordi Bascompte, and Claudio Juan Tessone. Nestedness in complex networks:
Observation, emergence, and implications. _Physics_ _Reports_, 2019.

[678] Zolt´an N Oltvai and Albert-L´aszl´o Barab´asi. Life’s complexity pyramid. _Science_, 298(5594):763–764, 2002.

[679] Tero Aittokallio and Benno Schwikowski. Graph-based methods for analysing networks in cell biology. _Brief._ _Bioinform._,
7(3):243–255, 2006.

[680] Roel Vermeulen, Emma L Schymanski, Albert-L´aszl´o Barab´asi, and Gary W Miller. The exposome and health: Where
chemistry meets biology. _Science_, 367(6476):392–396, 2020.

[681] Andreas Ruepp, Brigitte Waegele, Martin Lechner, Barbara Brauner, Irmtraud Dunger-Kaltenbach, Gisela Fobo, Goar
Frishman, Corinna Montrone, and H-Werner Mewes. CORUM: The comprehensive resource of mammalian protein
complexes—2009. _Nucleic_ _Acids_ _Res._, 38(suppl ~~1~~ ):D497–D501, 2010.

[682] Philip Wong, Sonja Althammer, Andrea Hildebrand, Andreas Kirschner, Philipp Pagel, Bernd Geissler, Pawel Smialowski, Florian Bl¨ochl, Matthias Oesterheld, Thorsten Schmidt, et al. An evolutionary and structural characterization
of mammalian protein complex organization. _Bmc_ _Genomics_, 9(1):629, 2008.

[683] Steffen Klamt, Utz-Uwe Haus, and Fabian Theis. Hypergraphs and cellular networks. _PLoS_ _Comput._ _Biol._, 5:e1000385,
2009.

[684] Anna Ritz, Allison N. Tegge, Hyunju Kim, Christopher L. Poirel, and T.M. Murali. Signaling hypergraphs. _Trends_
_Biotechnol._, 32(7):356–362, 2014.

[685] Thomas Gaudelet, Noel Malod-Dognin, and Nataˇsa Prˇzulj. Higher-order molecular organization as a source of biological
function. _Bioinformatics_, 34(17):i944–i953, 2018.

[686] Natasa Prˇzulj, Derek G Corneil, and Igor Jurisica. Modeling interactome: scale-free or geometric? _Bioinformatics_, 20
(18):3508–3515, 2004.

[687] Nicholas Franzese, Adam Groce, TM Murali, and Anna Ritz. Hypergraph-based connectivity measures for signaling
pathway topologies. _PLoS_ _Comput._ _Biol._, 15(10), 2019.

[688] Florian Klimm, Charlotte M Deane, and Gesine Reinert. Hypergraphs for predicting essential genes using multiprotein
complex data. _bioRxiv_, 2020.

[689] Nicole Pearcy, Nadia Chuzhanova, and Jonathan J Crofts. Complexity and robustness in hypernetwork models of
metabolism. _J._ _Theor._ _Biol._, 406:99–104, 2016.

[690] Tie Shen, Zhengdong Zhang, Zhen Chen, Dagang Gu, Shen Liang, Yang Xu, Ruiyuan Li, Yimin Wei, Zhijie Liu, Yin


108


Yi, et al. A genome-scale metabolic network alignment method within a hypergraph-based framework using a rotational
tensor-vector product. _Sci._ _Rep._, 8(1):1–16, 2018.

[691] J¨urgen Jost and Raffaella Mulas. Hypergraph Laplace operators for chemical reaction networks. _Adv._ _Math._, 351:870–896,
2019.

[692] Ze Tian, TaeHyun Hwang, and Rui Kuang. A hypergraph-based learning algorithm for classifying gene expression and
arrayCGH data with prior knowledge. _Bioinformatics_, 25(21):2831–2838, 2009.

[693] Alexis Battle, Martin C Jonikas, Peter Walter, Jonathan S Weissman, and Daphne Koller. Automated identification of
pathways from quantitative genetic interaction data. _Mol._ _Syst._ _Biol._, 6(1), 2010.

[694] Pavel Sumazin, Xuerui Yang, Hua-Sheng Chiu, Wei-Jen Chung, Archana Iyer, David Llobet-Navas, Presha Rajbhandari,
Mukesh Bansal, Paolo Guarnieri, Jose Silva, et al. An extensive microRNA-mediated network of RNA-RNA interactions
regulates established oncogenic pathways in glioblastoma. _Cell_, 147(2):370–381, 2011.

[695] Ahsanur Rahman, Christopher L Poirel, David J Badger, Craig Estep, and TM Murali. Reverse engineering molecular
hypergraphs. _IEEE/ACM_ _Trans._ _Comput._ _Biol._ _Bioinform._, 10(5):1113–1124, 2013.

[696] Yunchuan Kong and Tianwei Yu. A hypergraph-based method for large-scale dynamic correlation study at the transcriptomic scale. _BMC_ _Genomics_, 20(1):397, 2019.

[697] Anat Zimmer, Itay Katzir, Erez Dekel, Avraham E Mayo, and Uri Alon. Prediction of multidimensional drug dose
responses based on measurements of drug pairs. _Proc._ _Natl._ _Acad._ _Sci._, 113(37):10442–10447, 2016.

[698] Itay Katzir, Murat Cokol, Bree B Aldridge, and Uri Alon. Prediction of ultra-high-order antibiotic combinations based
on pairwise interactions. _PLoS_ _Comput._ _Biol._, 15(1):e1006774, 2019.

[699] Avichai Tendler, Anat Zimmer, Avi Mayo, and Uri Alon. Noise-precision tradeoff in predicting combinations of mutations
and drugs. _PLoS_ _Comput._ _Biol._, 15(5):e1006956, 2019.

[700] Anat Zimmer, Avichai Tendler, Itay Katzir, Avi Mayo, and Uri Alon. Prediction of drug cocktail effects when the number
of measurements is limited. _PLoS_ _Biol._, 15(10):e2002518, 2017.

[701] Jakub Otwinowski and Joshua B Plotkin. Inferring fitness landscapes by regression produces biased estimates of epistasis.
_Proc._ _Natl._ _Acad._ _Sci._, 111(22):E2301–E2309, 2014.

[702] Kristina Crona, Alex Gavryushkin, Devin Greene, and Niko Beerenwinkel. Inferring genetic interactions from comparative
fitness data. _Elife_, 6:e28629, 2017.

[703] Daniel M Weinreich, Yinghong Lan, C Scott Wylie, and Robert B Heckendorn. Should evolutionary geneticists worry
about higher-order epistasis? _Curr._ _Opin._ _Genet._ _Dev._, 23(6):700–707, 2013.

[704] Alicia Sanchez-Gorostiaga, Djordje Baji´c, Melisa L Osborne, Juan F Poyatos, and Alvaro Sanchez. High-order interactions
dominate the functional landscape of microbial consortia. _bioRxiv_, page 333534, 2018.

[705] Trudy FC Mackay and Jason H Moore. Why epistasis is important for tackling complex human disease genetics. _Genome_
_Med._, 6(6):42, 2014.

[706] Alvaro Sanchez. Defining higher-order interactions in synthetic ecology: Lessons from physics and quantitative genetics.
_Cell_ _Syst._, 9(6):519–520, 2019.

[707] Rafael F Guerrero, Samuel V Scarpino, Jo˜ao V Rodrigues, Daniel L Hartl, and C Brandon Ogbunugafor. Proteostasis
environment shapes higher-order epistasis operating on antibiotic resistance. _Genetics_, 212(2):565–575, 2019.

[708] Senay Yitbarek, John Lee Guittar, Sarah A Knutie, and C Brandon Ogbunugafor. Deconstructing higher-order interactions in the microbiota: A theoretical examination. _bioRxiv_, page 647156, 2019.

[709] Harry Mickalide and Seppe Kuehn. Higher-order interaction between species inhibits bacterial invasion of a phototrophpredator microbial community. _Cell_ _Syst._, 9(6):521–533, 2019.

[710] Yawei Niu, Guanghui Wang, Cunquan Qu, and Guiying Yan. RWHMDA: Random walk on hypergraph for microbe-disease
association prediction. _Front._ _Microbiol._, 10:1578, 2019.

[711] Guillaume St-Onge, Vincent Thibeault, Antoine Allard, Louis J Dub´e, and Laurent H´ebert-Dufresne. School closures, event cancellations, and the mesoscopic localization of epidemics in networks with higher-order structure.
_arXiv:2003.05924_, 2020.

[712] Florian T Pokorny, Majd Hawasly, and Subramanian Ramamoorthy. Topological trajectory classification with filtrations
of simplicial complexes and persistent homology. _Int._ _J._ _Robot._ _Res._, 35(1-3):204–223, 2016.

[713] Eric [´] Goubault, J´er´emy Ledent, and Sergio Rajsbaum. A simplicial complex model for dynamic epistemic logic to study
distributed task computability. In _Proceedings_ _Ninth_ _International_ _Symposium_ _on_ _Games,_ _Automata,_ _Logics,_ _and_ _Formal_
_Verification_, 2018.

[714] Hans van Ditmarsch, Eric Goubault, Jeremy Ledent, and Sergio Rajsbaum. Knowledge and simplicial complexes.
_arXiv:2002.08863_, 2020.

[715] Marcus Reitz and Ginestra Bianconi. The higher-order spectrum of simplicial complexes: A renormalization group
approach. _arXiv:200309143_, 2020.

[716] Sara Kaliˇsnik, Vitaliy Kurlin, and Davorin Leˇsnik. A higher-dimensional homologically persistent skeleton. _Adv._ _Appl._
_Math._, 102:113–142, 2019.

[717] Marco Guerra, Alessandro De Gregorio, Ulderico Fugacci, Giovanni Petri, and Francesco Vaccarino. Homological scaffold
via minimal homology bases. _arXiv:2004.11606_, 2020.

[718] George Karypis, Rajat Aggarwal, Vipin Kumar, and Shashi Shekhar. Multilevel hypergraph partitioning: Applications
in VLSI domain. _IEEE_ _Trans._ _Very_ _Large_ _Scale_ _Integr._ _VLSI_ _Syst._, 7(1):69–79, 1999.

[719] Nicolas Neubauer and Klaus Obermayer. Towards community detection in k-partite k-uniform hypergraphs. In _Proceedings_
_of_ _the_ _NIPS_ _2009_ _Workshop_ _on_ _Analyzing_ _Networks_ _and_ _Learning_ _with_ _Graphs_, pages 1–9, 2009.


109


[720] Mario Marietti and Damiano Testa. Cores of simplicial complexes. _Discrete_ _Comput._ _Geom._, 40(3):444–468, 2008.

[721] Art M Duval, Caroline J Klivans, and Jeremy L Martin. Critical groups of simplicial complexes. _Ann._ _Comb._, 17(1):
53–70, 2013.

[722] John Steenbergen, Caroline Klivans, and Sayan Mukherjee. A Cheeger-type inequality on simplicial complexes. _Adv._
_Appl._ _Math._, 56:56–77, 2014.

[723] Ori Parzanchevski. Mixing in high-dimensional expanders. _Comb._ _Probab._ _Comput._, 26(5):746–761, 2017.

[724] Ann Sizemore, Chad Giusti, and Danielle S Bassett. Classification of weighted networks through mesoscale homological
features. _J._ _Complex_ _Netw._, 5(2):245–273, 2017.

[725] Giovanni Petri, Martina Scolamiero, Irene Donato, and Francesco Vaccarino. Topological strata of weighted complex
networks. _PLOS_ _ONE_, 8(6), 2013.

[726] Christian Kuehn and Christian Bick. A universal route to explosive phenomena. _arXiv:2002.10714_, 2020.

[727] Omer Bobrowski and Primoz Skraba. Homological percolation and the Euler characteristic. _Phys._ _Rev._ _E_, 101(3):032304,
2020.

[728] Angkoon Phinyomark, Esther Ibanez-Marcelo, and Giovanni Petri. Resting-state fmri functional connectivity: Big data
preprocessing pipelines and topological data analysis. _IEEE_ _Trans._ _Big_ _Data_, 3(4):415–428, 2017.

[729] Stefano Battiston, James B Glattfelder, Diego Garlaschelli, Fabrizio Lillo, and Guido Caldarelli. The structure of financial
networks. In _Network_ _Science_, pages 131–163. Springer, 2010.

[730] Luca Faes, Dimitris Kugiumtzis, Giandomenico Nollo, Fabrice Jurysta, and Daniele Marinazzo. Estimating the decomposition of predictive information in multivariate systems. _Phys._ _Rev._ _E_, 91(3):032904, 2015.

[731] Luca Faes, Daniele Marinazzo, and Sebastiano Stramaglia. Multiscale information decomposition: Exact computation
for multivariate Gaussian processes. _Entropy_, 19(8):408, 2017.

[732] Fernando E Rosas, Pedro AM Mediano, Michael Gastpar, and Henrik J Jensen. Quantifying high-order interdependencies
via multivariate extensions of the mutual information. _Phys._ _Rev._ _E_, 100(3):032305, 2019.

[733] Laurent H´ebert-Dufresne, Samuel V Scarpino, and Jean-Gabriel Young. Macroscopic patterns of interacting contagions
are indistinguishable from social reinforcement. _Nat._ _Phys._, pages 1–6, 2020.

[734] Tiago P Peixoto. Network reconstruction and community detection from dynamics. _Phys._ _Rev._ _Lett._, 123(12):128301,
2019.


