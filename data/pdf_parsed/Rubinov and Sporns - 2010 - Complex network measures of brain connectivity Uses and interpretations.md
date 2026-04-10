NeuroImage 52 (2010) 1059–1069


Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/10538119)

# NeuroImage


journal homepage: www.elsevier.com/locate/ynimg

## Complex network measures of brain connectivity: Uses and interpretations


Mikail Rubinov [a][,][b][,][c], Olaf Sporns [d][,] ⁎


a Black Dog Institute and School of Psychiatry, University of New South Wales, Sydney, Australia
b Mental Health Research Division, Queensland Institute of Medical Research, Brisbane, Australia
c CSIRO Information and Communication Technologies Centre, Sydney, Australia
d Department of Psychological and Brain Sciences, Indiana University, Bloomington, IN 47405, USA


a r t i c l e i n f - a b s t r a c t



Article history:
Received 1 August 2009
Revised 1 October 2009
Accepted 2 October 2009
Available online 9 October 2009


Introduction



Brain connectivity datasets comprise networks of brain regions connected by anatomical tracts or by
functional associations. Complex network analysis—a new multidisciplinary approach to the study of
complex systems—aims to characterize these brain networks with a small number of neurobiologically
meaningful and easily computable measures. In this article, we discuss construction of brain networks from
connectivity data and describe the most commonly used network measures of structural and functional
connectivity. We describe measures that variously detect functional integration and segregation, quantify
centrality of individual brain regions or pathways, characterize patterns of local anatomical circuitry, and test
resilience of networks to insult. We discuss the issues surrounding comparison of structural and functional
network connectivity, as well as comparison of networks across subjects. Finally, we describe a Matlab
[toolbox (http://www.brain-connectivity-toolbox.net) accompanying this article and containing a collection](http://www.brain-connectivity-toolbox.net)
of complex network measures and large-scale neuroanatomical connectivity datasets.
© 2009 Elsevier Inc. All rights reserved.



Modern brain mapping techniques—such as diffusion MRI,
functional MRI, EEG, and MEG—produce increasingly large datasets
of anatomical or functional connection patterns. Concurrent technological advancements are generating similarly large connection
datasets in biological, technological, social, and other scientific fields.
Attempts to characterize these datasets have, over the last decade, led
to the emergence of a new, multidisciplinary approach to the study of
complex systems (Strogatz, 2001; Newman, 2003; Boccaletti et al.,
2006). This approach, known as complex network analysis, describes
important properties of complex systems by quantifying topologies of
their respective network representations. Complex network analysis
has its origins in the mathematical study of networks, known as graph
theory. However, unlike classical graph theory, the analysis primarily
deals with real-life networks that are large and complex—neither
uniformly random nor ordered.
Brain connectivity datasets comprise networks of brain regions
connected by anatomical tracts or by functional associations. Brain
networks are invariably complex, share a number of common
features with networks from other biological and physical systems,
and may hence be characterized using complex network methods.
Network characterization of structural and functional connectivity
data is increasing (Bassett and Bullmore, 2006, 2009; Stam and


⁎ Corresponding author.
E-mail address: [osporns@indiana.edu](mailto:osporns@indiana.edu) (O. Sporns).


1053-8119/$ - see front matter © 2009 Elsevier Inc. All rights reserved.
[doi:10.1016/j.neuroimage.2009.10.003](http://dx.doi.org/10.1016/j.neuroimage.2009.10.003)



Reijneveld, 2007; Bullmore and Sporns, 2009) and rests on several
important motivations. First, complex network analysis promises to
reliably (Deuker et al., 2009) quantify brain networks with a small
number of neurobiologically meaningful and easily computable
measures (Sporns and Zwi, 2004; Achard et al., 2006; Bassett et al.,
2006; He et al., 2007; Hagmann et al., 2008). Second, by explicitly
defining anatomical and functional connections on the same map of
brain regions, network analysis may be a useful setting for
exploring structural–functional connectivity relationships (Zhou et
al., 2006; Honey et al., 2007, 2009). Third, comparisons of
structural or functional network topologies between subject
populations appear to reveal presumed connectivity abnormalities
in neurological and psychiatric disorders (Stam et al., 2007, 2009;
Bassett et al., 2008; Leistedt et al., 2009; Ponten et al., 2009; Wang
et al., 2009b).
In this article, we provide a non-technical introduction to complex
network analysis of brain connectivity and outline important
conceptual issues associated with its use. We begin by discussing
the construction of structural and functional brain connectivity
networks. We then describe the most commonly used measures of
local and global connectivity, as well as their neurobiological
interpretations. We focus on recently developed network measures
(Boccaletti et al., 2006; Costa et al., 2007b) and provide a freely
available Matlab toolbox, containing these measures, as well as their
weighted and directed variants (Table A1). Finally, we discuss some of
the issues associated with comparing structural and functional
connectivity in the same subject and comparing connectivity patterns
between subjects.


1060 M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069



Note that while we concentrate on the analysis of large-scale
connectivity, our discussion is equally applicable to smaller scale
connectivity, with appropriate redefinitions. For instance, small-scale
brain networks could consist of neurons linked by synapses or of
cortical columns linked by intercolumnar connections.


Construction of brain networks


A network is a mathematical representation of a real-world
complex system and is defined by a collection of nodes (vertices)
and links (edges) between pairs of nodes (Fig. 1). Nodes in large-scale
brain networks usually represent brain regions, while links represent
anatomical, functional, or effective connections (Friston, 1994),
depending on the dataset. Anatomical connections typically correspond to white matter tracts between pairs of brain regions.
Functional connections correspond to magnitudes of temporal
correlations in activity and may occur between pairs of anatomically
unconnected regions. Depending on the measure, functional connectivity may reflect linear or nonlinear interactions, as well as
interactions at different time scales (Zhou et al., 2009). Effective
connections represent direct or indirect causal influences of one
region on another and may be estimated from observed perturbations
(Friston et al., 2003).

Fig. 2 shows illustrative anatomical, functional, and effective
connectivity networks, adapted from the study by Honey et al.
(2007). The anatomical network represents large-scale connection
pathways between cortical regions in the macaque, as collated from
histological tract tracing studies. Functional and effective connectivity
networks were constructed from time series of brain dynamics
simulated on this anatomical network. The functional network
represents patterns of cross-correlations between BOLD signals
estimated from these dynamics. The effective network represents
patterns of causal interactions, as computed with transfer entropy, a
measure of directed information flow. All networks are represented
by their connectivity (adjacency) matrices. Rows and columns in
these matrices denote nodes, while matrix entries denote links. The
order of nodes in connectivity matrices has no effect on computation
of network measures but is important for network visualization
(Fig. 2A).


The nature of nodes


The nature of nodes and links in individual brain networks is
determined by combinations of brain mapping methods, anatomical parcellation schemes, and measures of connectivity. Many
combinations occur in various experimental settings (Horwitz,
2003). The choice of a given combination must be carefully
motivated, as the nature of nodes and links largely determines
the neurobiological interpretation of network topology (Butts,
2009).
Nodes should ideally represent brain regions with coherent
patterns of extrinsic anatomical or functional connections. Parcellation schemes that lump heterogeneously connected brain regions into
single nodes may be less meaningful. In addition, a parcellation
scheme should completely cover the surface of the cortex, or of the
entire brain, and individual nodes should not spatially overlap. The
use of MEG and EEG sensors may be problematic in this regard, given
that sensors may detect spatially overlapping signals and are
generally not aligned with boundaries of coherent regions (Ioannides,
2007).
Networks constructed using distinct parcellation schemes may
significantly differ in their properties (Wang et al., 2009a) and
cannot, in general, be quantitatively compared. Specifically, structural
and functional networks may only be meaningfully compared, if
these networks share the same parcellation scheme (Honey et al.,
2009).



The nature of links


In addition to the type of connectivity (anatomical, functional or
effective) and measure-specific (e.g., time scale) features of connectivity, links are also differentiated on the basis of their weight and
directionality.
Binary links denote the presence or absence of connections (Fig. 2A),
while weighted links also contain information about connection
strengths (Figs. 2B, C). Weights in anatomical networks may represent
the size, density, or coherence of anatomical tracts, while weights in
functional and effective networks may represent respective magnitudes of correlational or causal interactions. Many recent studies
discard link weights, as binary networks are in most cases simpler to
characterize and have a more easily defined null model for statistical
comparison (see below). On the other hand, weighted characterization
usually focuses on somewhat different and complementary aspects of
network organization (e.g., Saramaki et al., 2007) and may be
especially useful in filtering the influence of weak and potentially
non-significant links.
Weak and non-significant links may represent spurious connections, particularly in functional or effective networks (Figs. 2B, C—top
panels). These links tend to obscure the topology of strong and
significant connections and as a result are often discarded, by applying
an absolute, or a proportional weight threshold (Figs. 2B, C—bottom
panels). Threshold values are often arbitrarily determined, and
networks should ideally be characterized across a broad range of
thresholds. Independently, all self-connections or negative connections (such as functional anticorrelations) must currently be removed
from the networks prior to analysis. Future network methods may be
able to quantify the role of negative weights in global network
organization.
Links may also be differentiated by the presence or absence of
directionality. Thus, anatomical and effective connections may
conceptually be represented with directed links. Unfortunately,
current neuroimaging methods are unable to directly detect anatomical or causal directionality. On the other hand, directed anatomical
networks constructed from tract tracing studies (e.g., Fig. 2A) indicate
the existence of a large proportion of reciprocal connections in the
cortex, which provides some validity for the use of undirected
anatomical networks. Directed patterns of effective connectivity may
be inferred from changes in functional activity that follow localized
perturbations.


Measures of brain networks


An individual network measure may characterize one or several
aspects of global and local brain connectivity. In this section, we
describe measures that variously detect aspects of functional
integration and segregation, quantify importance of individual brain
regions, characterize patterns of local anatomical circuitry, and test
resilience of networks to insult. Fig. 3 illustrates some basic concepts
underlying these measures, while Table A1 contains mathematical
definitions of all measures.
Network measures are often represented in multiple ways. Thus,
measures of individual network elements (such as nodes or links)
typically quantify connectivity profiles associated with these
elements and hence reflect the way in which these elements are
embedded in the network. Measurement values of all individual
elements comprise a distribution, which provides a more global
description of the network. This distribution is most commonly
characterized by its mean, although other features, such as
distribution shape, may be more important if the distribution is
nonhomogeneous. In addition to these different representations,
network measures also have binary and weighted, directed and
undirected variants. Weighted and directed variants of measures
are typically generalizations of binary undirected variants and


M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069 1061



therefore reduce to the latter when computed on binary undirected
networks.
To illustrate the different representations and variants of a
network measure, we consider a basic and important measure
known as the degree. The degree of an individual node is equal to
the number of links connected to that node, which in practice is
also equal to the number of neighbors of the node. Individual
values of the degree therefore reflect importance of nodes in the
network, as discussed below. The degrees of all nodes in the
network comprise the degree distribution, which is an important
marker of network development and resilience. The mean
network degree is most commonly used as a measure of density,
or the total “wiring cost” of the network. The directed variant of
the degree distinguishes the number of inward links from the
number of outward links, while the weighted variant of the
degree, sometimes termed the strength, is defined as the sum of
all neighboring link weights.
It is important to note that values of many network measures
are greatly influenced by basic network characteristics, such as the
number of nodes and links, and the degree distribution. Consequently, the significance of network statistics should be established by comparison with statistics calculated on null-hypothesis
networks. Null-hypothesis networks have simple random or
ordered topologies but preserve basic characteristics of the
original network. The most commonly used null-hypothesis
network has a random topology but shares the size, density and
binary degree distribution of the original network (Maslov and
Sneppen, 2002). Note, however, that this network may have a
different weighted degree distribution, especially if the weight
distribution is nonhomogeneous.


Measures of functional segregation


Functional segregation in the brain is the ability for specialized
processing to occur within densely interconnected groups of brain
regions. Measures of segregation primarily quantify the presence of
such groups, known as clusters or modules, within the network.
Measures of segregation have straightforward interpretations in
anatomical and functional networks. The presence of clusters in
anatomical networks suggests the potential for functional segregation
in these networks, while the presence of clusters in functional
networks suggests an organization of statistical dependencies
indicative of segregated neural processing.
Simple measures of segregation are based on the number of
triangles in the network, with a high number of triangles implying
segregation (Fig. 3). Locally, the fraction of triangles around an
individual node is known as the clustering coefficient and is
equivalent to the fraction of the node's neighbors that are also
neighbors of each other (Watts and Strogatz, 1998). The mean
clustering coefficient for the network hence reflects, on average, the
prevalence of clustered connectivity around individual nodes. The
mean clustering coefficient is normalized individually for each node
(Table A1) and may therefore be disproportionately influenced by
nodes with a low degree. A classical variant of the clustering
coefficient, known as the transitivity, is normalized collectively and
consequently does not suffer from this problem (e.g., Newman,
2003). Both the clustering coefficient and the transitivity have been
generalized for weighted (Onnela et al., 2005) and directed (Fagiolo,
2007) networks.
More sophisticated measures of segregation not only describe
the presence of densely interconnected groups of regions, but also
find the exact size and composition of these individual groups.
This composition, known as the network's modular structure
(community structure), is revealed by subdividing the network
into groups of nodes, with a maximally possible number of withingroup links, and a minimally possible number of between-group



links (Girvan and Newman, 2002). The degree to which the
network may be subdivided into such clearly delineated and
nonoverlapping groups is quantified by a single statistic, the modularity (Newman, 2004b). Unlike most other network measures,
the optimal modular structure for a given network is typically
estimated with optimization algorithms, rather than computed
exactly (Danon et al., 2005). Optimization algorithms generally
sacrifice some degree of accuracy for computational speed. One
notable algorithm (Newman, 2006) is known to be quite accurate
and is sufficiently fast for smaller networks. Another more recently
developed algorithm (Blondel et al., 2008) performs much faster
for larger networks and is also able to detect a hierarchy of
modules (the presence of smaller modules inside larger modules).
Both of these algorithms have been generalized to detect modular
structure in weighted (Newman, 2004a) and directed (Leicht and
Newman, 2008) networks. Other algorithms detect overlapping
modular network structure, and hence acknowledge that single
nodes may simultaneously belong in multiple modules (e.g., Palla
et al., 2005).

Figure 2A shows the modular structure of the anatomical
connectivity network of a large portion of the macaque cortex,
while Figs. 2B and C shows functional and effective networks
reordered by this modular structure. These anatomical modules
correspond to groups of specialized functional areas, such as the visual
and somatomotor regions, as previously determined by physiological
recordings. Anatomical, functional, and effective modules in this
network show extensive overlap.


Measures of functional integration


Functional integration in the brain is the ability to rapidly combine
specialized information from distributed brain regions. Measures of
integration characterize this concept by estimating the ease with
which brain regions communicate and are commonly based on the
concept of a path. Paths are sequences of distinct nodes and links and
in anatomical networks represent potential routes of information flow
between pairs of brain regions. Lengths of paths consequently
estimate the potential for functional integration between brain
regions, with shorter paths implying stronger potential for integration. On the other hand, functional connectivity data, by its nature,
already contain such information for all pairs of brain regions (Fig. 2B
—top panel). Paths in functional networks represent sequences of
statistical associations and may not correspond to information flow on
anatomical connections. Consequently, network measures based on
functional paths are less straightforward to interpret. Such measures
may be easier to interpret when information about anatomical
connections is available for the same subjects (e.g., Honey et al.,
2009).
The average shortest path length between all pairs of nodes in the
network is known as the characteristic path length of the network
(e.g., Watts and Strogatz, 1998) and is the most commonly used
measure of functional integration. The average inverse shortest path
length is a related measure known as the global efficiency (Latora and
Marchiori, 2001). Unlike the characteristic path length, the global
efficiency may be meaningfully computed on disconnected networks,
as paths between disconnected nodes are defined to have infinite
length, and correspondingly zero efficiency. More generally, the
characteristic path length is primarily influenced by long paths
(infinitely long paths are an illustrative extreme), while the global
efficiency is primarily influenced by short paths. Some authors have
argued that this may make the global efficiency a superior measure of
integration (Achard and Bullmore, 2007). Note that measures such as
the characteristic path length and the global efficiency do not
incorporate multiple and longer paths, which may significantly
contribute to integration in larger and sparser networks (Estrada
and Hatano, 2008).


1062 M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069


Fig. 1. Construction of brain networks from large scale anatomical and functional connectivity datasets. Structural networks are commonly extracted from histological (tract tracing)
or neuroimaging (diffusion MRI) data. Functional networks are commonly extracted from neuroimaging (fMRI) or neurophysiological (EEG, MEG) data. For computational
convenience, networks are commonly represented by their connectivity matrices, with rows and columns representing nodes and matrix entries representing links. To simplify
analysis, networks are often reduced to a sparse binary undirected form, through thresholding, binarizing, and symmetrizing.



Paths are easily generalized for directed and weighted networks
(Fig. 3). While a binary path length is equal to the number of links in
the path, a weighted path length is equal to the total sum of individual
link lengths. Link lengths are inversely related to link weights, as large
weights typically represent strong associations and close proximity.
Connection lengths are typically dimensionless and do not represent
spatial or metric distance.
The structural, functional, and effective connectivity networks in
Fig. 2 differ in their values of the global efficiency. Structural and
effective networks are similarly organized (Honey et al., 2007) and
share a high global efficiency. In comparison, functional networks
have weaker connections between modules, and consequently a
lower global efficiency.



Small-world brain connectivity


Anatomical brain connectivity is thought to simultaneously
reconcile the opposing demands of functional integration and
segregation (Tononi et al., 1994). A well-designed anatomical
network could therefore combine the presence of functionally
specialized (segregated) modules with a robust number of
intermodular (integrating) links. Such a design is commonly
termed small-world and indeed appears to be a ubiquitous
organization of anatomical connectivity (Bassett and Bullmore,
2006). Furthermore, most studies examining functional brain
networks also report various degrees of small-world organization.
It is commonly thought that such an organization reflects an


M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069 1063


Fig. 2. Illustrative anatomical, functional, and effective connectivity networks. (A) Large-scale anatomical connection network of the macaque cortex. This network includes the ventral
and dorsal streams of visual cortex, as well as groups of somatosensory and somatomotor regions. Network modules representing these groups, form largely contiguous (color-coded)
anatomical regions. Area names and abbreviations are provided in the supporting information. (B, top) Functional connectivity network, representing cross-correlation of the regional
BOLD signal, as estimated from simulated neural mass model dynamics. Warm colors represent positive correlations, while cool colors represent negative correlations. (B, bottom) The
same network, thresholded by removing negative and self-self correlations. (C, top) Effective connectivity network, constructed by computing inter-regional transfer entropy, from the
simulated fast time-scale dynamics. (C, bottom) The same network, thresholded to preserve the strongest connections, of the same number as in the structural network. See Honey
et al. (2007) for a further exploration of these networks.



optimal balance of functional integration and segregation (Sporns
and Honey, 2006). While this is a plausible hypothesis, the
somewhat abstract nature of functional paths (see above) makes
interpretation of the small-world property less straightforward in
functional networks. A more complete understanding of the
relationship between brain dynamics and functional connectivity
will help to clarify this issue.
Small-world networks are formally defined as networks that
are significantly more clustered than random networks, yet have
approximately the same characteristic path length as random
networks (Watts and Strogatz, 1998). More generally, small-world
networks should be simultaneously highly segregated and integrated. Recently, a measure of small-worldness was proposed to
capture this effect in a single statistic (Humphries and Gurney,
2008). This measure may be useful for snapshot characterization
of an ensemble of networks, but it may also falsely report a smallworld topology in highly segregated, but poorly integrated
networks. Consequently, this measure should not in general be
regarded as a substitute for individual assessments of integration
and segregation.
Anatomical and effective networks in Fig. 2 are simultaneously
highly segregated and integrated, and consequently have small-world
topologies. In comparison, the functional network is also highly
segregated but has a lower global efficiency, and therefore weaker
small-world attributes.



Network motifs


Global measures of integration and segregation belie a rich
repertoire of underlying local patterns of connectivity. Such local
patterns are particularly diverse in directed networks. For instance,
anatomical triangles may consist of feedforward loops, feedback
loops, and bidirectional loops, with distinct frequencies of individual loops likely having specific functional implications. These
patterns of local connectivity are known as (anatomical) motifs
(Fig. 3). The significance of a motif in the network is determined
by its frequency of occurrence, usually normalized as the motif
z-score by comparison with ensembles of random null-hypothesis
networks (Milo et al., 2002). The frequency of occurrence of
different motifs around an individual node is known as the motif
fingerprint of that node and is likely to reflect the functional role of
the corresponding brain region (Sporns and Kotter, 2004). The
frequency of occurrence of different motifs in the whole network
correspondingly represents the characteristic motif profile of the
network.
Functional activations on a local anatomical circuit may at any
given time utilize only a portion of that circuit. This observation
motivated the introduction of functional motifs, defined as
possible subsets of connection patterns embedded within
anatomical motifs (Sporns and Kotter, 2004). Functional motif
significance may be optimally characterized by weighted


1064 M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069


Fig. 3. Measures of network topology. An illustration of key complex network measures (in italics) described in this article. These measures are typically based on basic properties of
network connectivity (in bold type). Thus, measures of integration are based on shortest path lengths (green), while measures of segregation are often based on triangle counts
(blue) but also include more sophisticated decomposition into modules (ovals). Measures of centrality may be based on node degree (red) or on the length and number of shortest
paths between nodes. Hub nodes (black) often lie on a high number of shortest paths and consequently often have high betweenness centrality. Patterns of local connectivity are
quantified by network motifs (yellow). An example three-node and four-link anatomical motif contains six possible functional motifs, of which two are shown—one motif containing
dashed links, and one motif containing crossed links.



measures of motif occurrence, known as the motif intensity, and
the motif intensity z-score (Onnela et al., 2005). Motif intensity
takes into account weights of all motif-comprising links and may
therefore be more sensitive in detecting consistently strong
functional configurations.
There is a source of possible confusion in motif terminology. Motifs
(“structural” and “functional”) were initially considered only in the
context of anatomical brain networks (Sporns and Kotter, 2004).
However, motif measures may also be meaningfully applied to some
effective connectivity networks. On the other hand, motifs are
generally not used in the analysis of undirected networks, due to
the paucity of local undirected connectivity patterns.


Measures of centrality


Important brain regions (hubs) often interact with many other
regions, facilitate functional integration, and play a key role in
network resilience to insult. Measures of node centrality variously
assess importance of individual nodes on the above criteria. There are
many measures of centrality, and in this section, we describe the more
commonly used measures. We also note that motif and resilience
measures, discussed in other sections, are likewise sometimes used to
detect central brain regions.
The degree, as discussed above, is one of the most common
measures of centrality. The degree has a straightforward
neurobiological interpretation: nodes with a high degree are
interacting, structurally or functionally, with many other nodes
in the network. The degree may be a sensitive measure of
centrality in anatomical networks with nonhomogeneous degree
distributions.
In modular anatomical networks, degree-based measures of
within-module and between-module connectivity may be useful
for heuristically classifying nodes into distinct functional groups
(Guimera and Amaral, 2005). The within-module degree z-score is
a localized, within-module version of degree centrality (Table A1).
The complementary participation coefficient assesses the diversity
of intermodular interconnections of individual nodes. Nodes with
a high within-module degree but with a low participation
coefficient (known as provincial hubs) are hence likely to play



an important part in the facilitation of modular segregation. On
the other hand, nodes with a high participation coefficient (known
as connector hubs) are likely to facilitate global intermodular
integration.
Many measures of centrality are based on the idea that
central nodes participate in many short paths within a network,
and consequently act as important controls of information flow
(Freeman, 1978). For instance, closeness centrality is defined as
the inverse of the average shortest path length from one node to
all other nodes in the network. A related and often more
sensitive measure is betweenness centrality, defined as the
fraction of all shortest paths in the network that pass through
a given node. Bridging nodes that connect disparate parts of the
network often have a high betweenness centrality (Fig. 3). The
notion of betweenness centrality is naturally extended to links
and could therefore also be used to detect important anatomical
or functional connections. The calculation of betweenness
centrality has been made significantly more efficient with the
recent development of faster algorithms (Brandes, 2001; Kintali,
2008).
Weighted and directed variants of centrality measures are in most
cases based on weighted and directed variants of degree and path
length (Table A1).
Measures of centrality may have different interpretations in
anatomical and functional networks. For instance, anatomically
central nodes often facilitate integration, and consequently enable
functional links between anatomically unconnected regions. Such
links in turn make central nodes less prominent and so reduce the
sensitivity of centrality measures in functional networks. In addition,
path-based measures of centrality in functional networks are subject
to the same interpretational caveats as path-based measures of
integration (see above).


Measures of network resilience


Anatomical brain connectivity influences the capacity of neuropathological lesions to affect functional brain activity. For instance, the
extent of functional deterioration is heavily determined by the
affected anatomical region in a stroke, or by the capacity of anatomical


M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069 1065



connectivity to withstand degenerative change in Alzheimer's disease.
Complex network analysis is able to characterize such network
resilience properties directly and indirectly.
Indirect measures of resilience quantify anatomical features
that reflect network vulnerability to insult. One such feature is the
degree distribution (Barabasi and Albert, 1999). For instance,
complex networks with power-law degree distributions may be
resilient to gradual random deterioration, but highly vulnerable to
disruptions of high-degree central nodes. Most real-life networks
do not have perfect power–law degree distributions. On the other
hand, many networks have degree distributions that locally
behave like a power–law—the extent to which these distributions
fit a power–law may hence be a useful marker of resilience
(Achard et al., 2006). Another useful measure of resilience is the
assortativity coefficient (Newman, 2002). The assortativity coefficient is a correlation coefficient between the degrees of all nodes
on two opposite ends of a link. Networks with a positive
assortativity coefficient are therefore likely to have a comparatively resilient core of mutually interconnected high-degree hubs.
On the other hand, networks with a negative assortativity
coefficient are likely to have widely distributed and consequently
vulnerable high-degree hubs. Related measures of assortativity
computed on individual nodes include the average neighbor degree
(Pastor-Satorras et al., 2001) and the recently introduced local
assortativity coefficient (Piraveenan et al., 2008). Individual central
nodes that score lowly on these measures may therefore
compromise global network function if disrupted. Weighted and
directed variants of assortativity measures are based on the
respective weighted and directed variants of the degree (Barrat et
al., 2004; Leung and Chau, 2007).
Direct measures of network resilience generally test the network
before and after a presumed insult. For instance, patients with a
progressive neurodegenerative disease may be imaged over a
longitudinal period. Alternatively, insults may be computationally
simulated by random or targeted removal of nodes and links. The
effects of such lesions on the network may then be quantified by
characterizing changes in the resulting anatomical connectivity, or in
the emergent simulated functional connectivity or dynamical activity
(e.g., Alstott et al., 2009). When testing resilience in such a way, it is
prudent to use measures that are suitable for the analysis of
disconnected networks. For instance, the global efficiency would be
preferable to the characteristic path length as a measure of
integration.


Network comparison


Complex network analysis may be useful for exploring
connectivity relationships in individual subjects or between
subject groups. In individual subjects, comparisons of structural
and functional networks may provide insights into structural–
functional connectivity relationships (e.g., Honey et al., 2007).
Across subject populations, comparisons may detect abnormalities
of network connectivity in various brain disorders (Bassett and
Bullmore, 2009). The increased emphasis on structure–function
and between-subject comparisons in studies of brain networks
will require the development of accurate statistical comparison
tools, similar to those in cellular and molecular biology (Sharan
and Ideker, 2006). Preliminary steps have already been taken in
this direction (Costa et al., 2007a). Here we discuss some general
issues associated with network comparison.
Differences in density between anatomical and functional
networks make global comparisons between these networks less
straightforward. Functional networks are likely to be denser than
anatomical networks, as they will typically contain numerous
connections between anatomically unconnected regions (Damoiseaux and Greicius, 2009). These differences in density are likely



to become more pronounced in larger, more highly resolved
networks, as anatomical connectivity in such networks becomes
increasingly sparse, while functional connectivity remains comparatively dense. Notably, comparisons between anatomical and
functional modular structure (e.g., Zhou et al., 2006) remain
meaningful despite differences in density. Other factors that may
affect comparisons of network topology include degree and
weight distributions.
The nontrivial relationship between structural and functional
brain connectivity and the consequent interpretational difficulties of
some functional measures (see above) make between-subject
comparisons of functional networks difficult. The significance of
such comparisons will become more obvious with increased knowledge about causal relationships between brain regions, as mediated
by direct anatomical connections. The development of a detailed
anatomical map of the human brain is an important step in this
direction (Sporns et al., 2005).


Brain connectivity analysis software


Multiple network analysis software packages are freely available
on the Web. These packages include command-line toolboxes in
popular languages, such as Matlab (Gleich, 2008) and Python
(Hagberg et al., 2008), as well as standalone graphical user interface
software (Batagelj and Mrvar, 2003; NWB-Team, 2006). Some of these
packages are especially suitable for the analysis of large networks
containing thousands of nodes, while others have powerful network
visualization capabilities.
To accompany this article, we developed a freely available and open
[source Matlab toolbox (http://www.brain-connectivity-toolbox.net).](http://www.brain-connectivity-toolbox.net)
A number of features distinguish our toolbox from most other
software packages. Our toolbox includes many recently developed
network measures, which are discussed in this article, but are not
yet widely available. In addition, we provide weighted and directed
variants for all our measures—many of these variants are likewise not
yet available in other software. In addition to these features, the
toolbox provides functions for network manipulation (such as
thresholding) and includes algorithms for generating null-hypothesis
networks of predetermined (random, ordered and other) topologies.
Finally, the toolbox contains datasets for large scale neuroanatomical
networks of the mammalian cortex of several species. The open source
nature of our toolbox allows researchers to customize individual
functions for their needs, and to incorporate functions into larger
analysis protocols.


Conclusion


Complex network analysis has emerged as an important tool for
characterization of anatomical and functional brain connectivity. We
described a collection of measures that quantify local and global
properties of complex brain networks. The accompanying brain
connectivity toolbox allows researchers to start exploring network
properties of complex structural and functional datasets. We hope
that the brain mapping community will be able to benefit from and
contribute to these tools.


Acknowledgments


We thank Rolf Kötter, Patric Hagmann, Aviad Rubinstein, and Chris
Honey for their contributions to the brain connectivity toolbox;
Jonathan Power and Vassilis Tsiaras for suggesting valuable improvements to our toolbox functions; and Alain Barrat for definitional
clarifications. M.R. is grateful to Michael Breakspear for his supervision and support during this project. M.R. and O.S. were supported by
the J.S. McDonnell Foundation Brain NRG JSMF22002082. M.R. was
supported by CSIRO ICT Centre scholarship.


1066 M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069


Appendix A.


Table A1
Mathematical definitions of complex network measures (see supplementary information for a self-contained version of this table).
























































































































































M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069 1067






































































































1068 M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069







































































































Appendix B. Supplementary data


Supplementary data associated with this article can be found, in
the online version, at [doi:10.1016/j.neuroimage.2009.10.003.](http://dx.doi.org/10.1016/j.neuroimage.2009.10.003)


References


Achard, S., Bullmore, E., 2007. Efficiency and cost of economical brain functional
networks. PLoS Comput. Biol. 3, e17.
Achard, S., Salvador, R., Whitcher, B., Suckling, J., Bullmore, E., 2006. A resilient, lowfrequency, small-world human brain functional network with highly connected
association cortical hubs. J. Neurosci. 26, 63–72.
Alstott, J., Breakspear, M., Hagmann, P., Cammoun, L., Sporns, O., 2009. Modeling the
impact of lesions in the human brain. PLoS Comput. Biol. 5, e1000408.
Barabasi, A.L., Albert, R., 1999. Emergence of scaling in random networks. Science 286,
509–512.
Barrat, A., Barthelemy, M., Pastor-Satorras, R., Vespignani, A., 2004. The architecture of
complex weighted networks. Proc. Natl. Acad. Sci. U. S. A. 101, 3747–3752.
Bassett, D.S., Bullmore, E., 2006. Small-world brain networks. Neuroscientist 12,
512–523.
Bassett, D.S., Bullmore, E.T., 2009. Human brain networks in health and disease. Curr.
Opin. Neurol. 22, 340–347.
Bassett, D.S., Meyer-Lindenberg, A., Achard, S., Duke, T., Bullmore, E., 2006. Adaptive
reconfiguration of fractal small-world human brain functional networks. Proc. Natl.
Acad. Sci. U. S. A. 103, 19518–19523.
Bassett, D.S., Bullmore, E., Verchinski, B.A.,Mattay,V.S.,Weinberger, D.R., Meyer-Lindenberg,
A., 2008. Hierarchical organization of human cortical networks in health and
schizophrenia. J. Neurosci. 28, 9239–9248.



Batagelj, V.,Mrvar,W.,2003.Pajek - analysisandvisualization oflargenetworksIn: Jünger,
M., Mutzel, P. (Eds.), Graph Drawing Software. Springer, Berlin, pp. 77–103.
Blondel, V.D., Guillaume, J.-L., Lambiotte, R., Lefebvre, E., 2008. Fast unfolding of
communities in large networks. J. Stat. Mech. 2008, P10008.
Boccaletti, S., Latora, V., Moreno, Y., Chavez, M., Hwang, D.U., 2006. Complex networks:
Structure and dynamics. Phys. Rep. 424, 175–308.
Brandes, U., 2001. A faster algorithm for betweenness centrality. J. Math. Sociol. 25,
163–177.
Bullmore, E., Sporns, O., 2009. Complex brain networks: graph theoretical analysis of
structural and functional systems. Nat. Rev., Neurosci. 10, 186–198.
Butts, C.T., 2009. Revisiting the foundations of network analysis. Science 325, 414–416.
Costa, L.d.F., Kaiser, M., Hilgetag, C., 2007a. Predicting the connectivity of primate
cortical networks from topological and spatial node properties. BMC Syst. Biol.
1, 16.
Costa, L.D.F., Rodrigues, F.A., Travieso, G., Boas, P.R.V., 2007b. Characterization of
complex networks: a survey of measurements. Adv. Phys. 56, 167–242.
Damoiseaux, J.S., Greicius, M.D., 2009. Greater than the sum of its parts: A review of
studies combining structural connectivity and resting-state functional connectivity. Brain Struct Funct. 213, 525–533 (Epub 2009 Jun 30).
Danon, L., Diaz-Guilera, A., Duch, J., Arenas, A., 2005. Comparing community structure
identification. J. Stat. Mech. 2005, P09008.
Deuker, L., Bullmore, E.T., Smith, M., Christensen, S., Nathan, P.J., Rockstroh, B., Bassett,
D.S., 2009. Reproducibility of graph metrics of human brain functional networks.
NeuroImage 47, 1460–1468.
Estrada, E., Hatano, N., 2008. Communicability in complex networks. Phys. Rev., E Stat.
Nonlinear Soft Matter Phys. 77, 036111.
Fagiolo, G., 2007. Clustering in complex directed networks. Phys. Rev., E Stat. Nonlinear
Soft Matter Phys. 76, 026107.
Freeman, L.C., 1978. Centrality in social networks: conceptual clarification. Soc. Netw. 1,
215–239.


M. Rubinov, O. Sporns / NeuroImage 52 (2010) 1059–1069 1069



Friston, K.J., 1994. Functional and effective connectivity in neuroimaging: a synthesis.
Hum. Brain Mapp. 2, 56–78.
Friston, K.J., Harrison, L., Penny, W., 2003. Dynamic causal modelling. NeuroImage 19,
1273–1302.
Girvan, M., Newman, M.E.J., 2002. Community structure in social and biological
networks. Proc. Natl. Acad. Sci. U. S. A. 99, 7821–7826.
Gleich, D., 2008. Matlabbgl (version 4.0).
Guimera, R., Amaral, L.A.N., 2005. Cartography of complex networks: modules and
universal roles. J. Stat. Mech. 2005, P02001.
Hagberg, A.A., Schult, D.A., Swart, P.J., 2008. Exploring network structure, dynamics, and
function using networkx. In: Varoquaux, G., Vaught, T., Millman, J. (Eds.),
Proceedings of the 7th Python in Science Conference (SciPy2008). Pasadena, CA
USA, pp. 11–15.
Hagmann, P., Cammoun, L., Gigandet, X., Meuli, R., Honey, C.J., Wedeen, V.J., Sporns, O.,
2008. Mapping the structural core of human cerebral cortex. PLoS Biol. 6, e159.
He, Y., Chen, Z.J., Evans, A.C., 2007. Small-world anatomical networks in the human
brain revealed by cortical thickness from MRI. Cereb. Cortex 17, 2407–2419.
Honey, C.J., Kotter, R., Breakspear, M., Sporns, O., 2007. Network structure of cerebral
cortex shapes functional connectivity on multiple time scales. Proc. Natl. Acad. Sci.
U. S. A. 104, 10240–10245.
Honey, C.J., Sporns, O., Cammoun, L., Gigandet, X., Thiran, J.P., Meuli, R., Hagmann, P.,
2009. Predicting human resting-state functional connectivity from structural
connectivity. Proc. Natl. Acad. Sci. U. S. A. 106, 2035–2040.
Horwitz, B., 2003. The elusive concept of brain connectivity. NeuroImage 19, 466–470.
Humphries, M.D., Gurney, K., 2008. Network ‘small-world-ness’: a quantitative method
for determining canonical network equivalence. PLoS ONE 3, e0002051.
Ioannides, A.A., 2007. Dynamic functional connectivity.Curr. Opin. Neurobiol. 17, 161–170.
Kintali, S., 2008. Betweenness centrality: algorithms and lower bounds. arXiv,
0809.1906v0802.
Latora, V., Marchiori, M., 2001. Efficient behavior of small-world networks. Phys. Rev.
Lett. 87, 198701.
Leicht, E.A., Newman, M.E., 2008. Community structure in directed networks. Phys. Rev.
Lett. 100, 118703.
Leistedt, S.J., Coumans, N., Dumont, M., Lanquart, J.P., Stam, C.J., Linkowski, P., 2009.
Altered sleep brain functional connectivity in acutely depressed patients. Hum.
Brain Mapp. 30, 2207–2219.
Leung, C.C., Chau, H.F., 2007. Weighted assortative and disassortative networks model.
Physica, A 378, 591–602.
Maslov, S., Sneppen, K., 2002. Specificity and stability in topology of protein networks.
Science 296, 910–913.
Milo, R., Shen-Orr, S., Itzkovitz, S., Kashtan, N., Chklovskii, D., Alon, U., 2002. Network
motifs: simple building blocks of complex networks. Science 298, 824–827.
Newman, M.E.J., 2002. Assortative mixing in networks. Phys. Rev. Lett. 89,
2087011–2087014.
Newman, M.E.J., 2003. The structure and function of complex networks. SIAM Rev. 45,
167–256.
Newman, M.E.J., 2004a. Analysis of weighted networks. Phys. Rev., E Stat. Nonlinear Soft
Matter Phys. 70, 056131.
Newman, M.E.J., 2004b. Fast algorithm for detecting community structure in networks.
Phys. Rev., E 69, 066133.
Newman, M.E.J., 2006. Modularity and community structure in networks. Proc. Natl.
Acad. Sci. U. S. A. 103, 8577–8582.



NWB-Team, 2006. Network workbench tool. Indiana university, Northeastern University, and University of Michigan.
Onnela, J.P., Saramaki, J., Kertesz, J., Kaski, K., 2005. Intensity and coherence of motifs in
weighted complex networks. Phys. Rev., E Stat. Nonlinear Soft Matter Phys. 71,
065103.
Palla, G., Derenyi, I., Farkas, I., Vicsek, T., 2005. Uncovering the overlapping community
structure of complex networks in nature and society. Nature 435, 814–818.
Pastor-Satorras, R., Vazquez, A., Vespignani, A., 2001. Dynamical and correlation
properties of the internet. Phys. Rev. Lett. 87, 258701.
Piraveenan, M., Prokopenko, M., Zomaya, A.Y., 2008. Local assortativeness in scale-free
networks. Europhys. Lett. 84, 28002.
Ponten, S.C., Douw, L., Bartolomei, F., Reijneveld, J.C., Stam, C.J., 2009. Indications for
network regularization during absence seizures: weighted and unweighted graph
theoretical analyses. Exp. Neurol. 217, 197–204.
Saramaki, J., Kivela, M., Onnela, J.P., Kaski, K., Kertesz, J., 2007. Generalizations of the
clustering coefficient to weighted complex networks. Phys. Rev., E Stat. Nonlinear
Soft Matter Phys. 75, 027105.
Sharan, R., Ideker, T., 2006. Modeling cellular machinery through biological network
comparison. Nat. Biotechnol. 24, 427–433.
Sporns, O., Kotter, R., 2004. Motifs in brain networks. PLoS Biol. 2, e369.
Sporns, O., Zwi, J.D., 2004. The small world of the cerebral cortex. Neuroinformatics 2,
145–162.
Sporns, O., Honey, C.J., 2006. Small worlds inside big brains. Proc. Natl. Acad. Sci. U. S. A.
103, 19219–19220.
Sporns, O., Tononi, G., Kotter, R., 2005. The human connectome: a structural description
of the human brain. PLoS Comput. Biol. 1, e42.
Stam, C.J., Reijneveld, J.C., 2007. Graph theoretical analysis of complex networks in the
brain. Nonlinear Biomed. Phys. 1, 3.
Stam, C.J., Jones, B.F., Nolte, G., Breakspear, M., Scheltens, P., 2007. Small-world networks
and functional connectivity in Alzheimer's disease. Cereb. Cortex 17, 92–99.
Stam, C.J., de Haan, W., Daffertshofer, A., Jones, B.F., Manshanden, I., van Cappellen
van Walsum, A.M., Montez, T., Verbunt, J.P., de Munck, J.C., van Dijk, B.W.,
Berendse, H.W., Scheltens, P., 2009. Graph theoretical analysis of magnetoencephalographic functional connectivity in Alzheimer's disease. Brain 132,
213–224.
Strogatz, S.H., 2001. Exploring complex networks. Nature 410, 268–276.
Tononi, G., Sporns, O., Edelman, G.M., 1994. A measure for brain complexity: relating
functional segregation and integration in the nervous system. Proc. Natl. Acad. Sci.
U. S. A. 91, 5033–5037.
Wang, J., Wang, L., Zang, Y., Yang, H., Tang, H., Gong, Q., Chen, Z., Zhu, C., He, Y., 2009a.
Parcellation-dependent small-world brain functional networks: a resting-state
fMRI study. Hum. Brain Mapp. 30, 1511–1523.
Wang, L., Zhu, C., He, Y., Zang, Y., Cao, Q., Zhang, H., Zhong, Q., Wang, Y., 2009b. Altered
small-world brain functional networks in children with attention-deficit/hyperactivity disorder. Hum. Brain Mapp. 30, 638–649.
Watts, D.J., Strogatz, S.H., 1998. Collective dynamics of ‘small-world’ networks. Nature
393, 440–442.
Zhou, C., Zemanova, L., Zamora, G., Hilgetag, C.C., Kurths, J., 2006. Hierarchical
organization unveiled by functional connectivity in complex brain networks.
Phys. Rev. Lett. 97, 238103.
Zhou, D., Thompson, W.K., Siegle, G., 2009. Matlab toolbox for functional connectivity.
Neuroimage. 2009 Oct 1;47(4):1590-1607. Epub 2009 Jun 8


