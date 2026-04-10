Information Sciences [608](https://doi.org/10.1016/j.ins.2022.07.041) (2022) 1301–1316


Contents lists available at [ScienceDirect](http://www.sciencedirect.com/science/journal/00200255)

# Information Sciences


journal homepage: [www.elsevier.com/locate/ins](http://www.elsevier.com/locate/ins)

## FC–HAT: Hypergraph attention network for functional brain network classification


Junzhong Ji [a][,][b], Yating Ren [a], Minglong Lei [a][,][b][,][⇑]


a Beijing Municipal Key Laboratory of Multimedia and Intelligent Software Technology, Faculty of Information Technology, Beijing University of Technology,
Beijing 100124, China
b Beijing Institute of Artificial Intelligence, Beijing University of Technology, Beijing 100124, China



a r t i c l e i n f 

Article history:
Received 7 May 2021
Received in revised form 12 June 2022
Accepted 6 July 2022
Available online 9 July 2022


Keywords:
Functional Brain Networks
Hypergraphs
Graph Neural Networks
Attention Mechanism.


1. Introduction



a b s t r a c t


Recently, functional brain network analysis via graph neural networks has achieved stateof-the-art results as it can directly extract information from irregular graphs without any
approximation. However, current methods remain limited in exploring the high-order
structural information of brain networks. To address this issue, we propose a hypergraph
attention network for functional brain network classification (FC–HAT). First, we build a
dynamic hypergraph generation phase and model each brain network as a hypergraph to
preserve the high-order information. The pair-wise and community-wise similarities in
functional brain networks are separately captured by k nearest neighbors and k-means.
Theoretical analysis shows that the constructed hypergraph exhibits superior spectral
properties. Then, we design a hypergraph attention aggregation phase to further extract
information in hypergraphs. This includes node and hyperedge attention layers that can
separately aggregate features among nodes and hyperedges. Finally, the two phases are
jointly optimized in an end-to-end manner, which can dynamically update hypergraphs
and node embeddings along with the training process. Experimental results on ABIDE-I
and ADHD-200 demonstrate the effectiveness of FC–HAT in cerebral disease classification.
Moreover, the abnormal connectivity patterns and brain regions identified by FC–HAT are
found to be more likely to become biomarkers associated with cerebral diseases.

               - 2022 Elsevier Inc. All rights reserved.



The study of functional connectivity in human brains has drawn increasing attention in the fields of brain science and
neuroinformatics. The brain can be modeled as a functional network, where nodes represent brain regions and edges indicate
their functional interactions [13]. The connections within the network indicate specific topological properties, which can not
only be utilized to analyze brain functions and mechanisms but also serve as essential biomarkers for brain disease detection

[10]. For example, analyzing the abnormal functional connections has been widely used in the classification of brain diseases,
such as attention deficit hyperactivity disorder (ADHD) [26] and autism spectrum disorder (ASD) [9].
Recently, advanced deep learning methods have been used in functional brain network analysis [7,17]. Compared with
traditional machine learning methods, deep models enjoy a greater representation ability and can extract high-level features


⇑ Corresponding author at:Beijing Municipal Key Laboratory of Multimedia and Intelligent Software Technology, Faculty of Information Technology,
Beijing University of Technology, Beijing 100124, China.
E-mail addresses: [jjz01@bjut.edu.cn](mailto:jjz01@bjut.edu.cn) (J. Ji), [ET@emails.bjut.edu.cn](mailto:ET@emails.bjut.edu.cn) (Y. Ren), [leiml@bjut.edu.cn](mailto:leiml@bjut.edu.cn) (M. Lei).


[https://doi.org/10.1016/j.ins.2022.07.041](https://doi.org/10.1016/j.ins.2022.07.041)
0020-0255/� 2022 Elsevier Inc. All rights reserved.


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


that reveal discriminative information in brain networks [2]. Early methods were mainly based on fully-connected neural
networks (e.g., deep auto-encoder [42]), where functional networks are directly vectorized and fed into the model for classification. Such a process overlooks the topological structures and often requires many parameters, which can easily lead to
over-fitting because of the high-dimension and low-sample size properties of brain data [5,11]. Later methods leveraged convolutional neural networks (CNNs) to extract the structural information of functional networks. The key notion is to develop
convolution and pooling operators under the functional connectivity matrix. For example, BrainNetCNN [16] and its variants

[11,12] redefine three types of convolution layers to extract information from different perspectives. Because CNNs were
originally designed for images with regular grids, representing functional networks as regular grids fails to capture the
non-Euclidean proximities among brain regions.
More recently, the development of graph neural networks (GNNs) has provided new insight into handling irregular structures. Consequently, they have been successfully applied to many brain network analysis tasks [20,40]. The basic idea of
graph convolutions is to develop local and parameter-sharing operators on a group of adjacent nodes, by which the neighbor
information can be aggregated to the target nodes via a message-passing scheme. Compared with previous deep methods,
the success of GNNs is affirmed by the fact that the node features are updated under the guidance of graph structures [8].
Current GNNs, such as the graph convolution network (GCN) [19] and graph attention network (GAT) [38], have achieved
superior performances in many tasks based on functional brain network data.
Although effective, current GNNs still suffer from several problems when applied to brain network analysis. First, they
mainly define the operations (i.e., convolutions and pooling) under the structures constructed from pair-wise connections.
However, there often exist high-order proximities and complex structural information among brain regions [44]. For example, a set of regions is usually combined to accomplish certain brain functions. As such, the affinity relations among those
regions are no longer dyadic (pair-wise) [1]. Second, the functional connectivity matrix constructed from rs-fMRI data contains noisy connections. The performance of GNNs may be affected by such noise because the message-passing procedure in
GNNs largely depends on the quality of constructed graphs. Existing methods lack proper strategies to eliminate the effect of
noise when utilizing graph structures.
To address these issues, we propose a hypergraph attention network for functional brain network classification (FC–HAT)
using rs-fMRI data. We attempt to model the high-order structural information in functional brain networks by a hypergraph
and develop novel convolution operations on it for further information extraction. Compared with a simple graph where the
edges can only describe pair-wise relations, a hypergraph consists of a set of hyperedges that can link an arbitrary number of
related nodes [45]. Hypergraphs can abstract more information in graphs and represent more complex structures. Specifically, we designed a dynamic hypergraph generation phase and hypergraph attention aggregation phase to construct effective
GNNs based on hypergraph structures.
The dynamic hypergraph generation phase aims to build highly qualified hypergraphs that can capture complex structural
information while avoiding the disturbance of noise. To consider different aspects of structural information in brain networks, the proposed model builds the hypergraph based on both pair-wise and community-wise proximities. The pairwise proximities mainly reflect the direct neighbors, while the community-wise proximities describe the sub-graph and
group structures. To this end, we combine k nearest neighbors (KNN) similarity and k-means clustering to capture the nearest direct neighbors and similar nodes around the same centroids. Besides, the construction of hypergraphs is incorporated
into the training process, where the hypergraphs are updated in each iteration. The dynamic generation process ensures that
the hypergraphs are not constructed in advance but can be tuned with respect to different tasks. We also attempt to theoretically analyze the Laplacian matrix of the constructed hypergraph. This shows that the constructed hypergraph has better
spectrum properties and is more powerful in feature extraction when combined with GNNs.
The hypergraph attention aggregation phase defines effective GNNs based on hypergraph structures to generate representations for brain regions. Because a hyperedge contains more than two nodes, the conventional graph convolutions based on
information aggregation scheme are inapplicable. To address this problem, the proposed model breaks the hypergraph
aggregation process into a successive aggregation of hyperedges and nodes, by which GNNs can be applied to hypergraphs.
Concretely, the hyperedge representations are first formulated based on the features of brain regions included in the hyperedges. Then, the neighborhood features are propagated to the target brain region from hyperedges that share the target brain
region. To further discriminate the differences between neighbors, the attention mechanism is separately used to update
representations of hyperedges and nodes. The attention aggregation framework can formulate learnable parameters to discriminate the importance of neighbors without any prior knowledge. The learned embeddings are consequently more robust
and qualified for classification tasks.
The contributions of the study can be summarized as follows:


 - This is the first study that utilizes GNNs based on hypergraphs for functional brain network classification. The proposed
model can capture high-order functional connections that are not explicitly observable in simple graphs.

 - We design a dynamic hypergraph generation phase to consider both pair-wise and community-wise structural information
in brain networks. Further, the hypergraphs can be dynamically updated during the training process. We analyzed the
spectral property to verify the capacity of learned hypergraphs.

 - We develop a hypergraph attention aggregation phase to aggregate information via hyperedges that connect a set of brain
regions. The attention mechanism is used to distinguish the importance of adjacent regions during the aggregation
process.


1302


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


 - Extensive experiments on functional brain network classification show the effectiveness of the proposed method.


2. Related works


2.1. Brain Network Analysis based on Deep Models


Deep neural networks have been widely used in brain network analysis because of the powerful expressive ability to
learn high-level features from various types of data. Generally, functional brain networks can be constructed by functional
magnetic resonance imaging (fMRI) or electroencephalography (EEG) data. This study mainly focuses on functional brain
network analysis based on fMRI data. One main category of methods focuses on brain network classification, which can
be further used for brain disease recognition. Early methods are mainly based on fully-connected neural networks (FCNNs)
developed from multi-layer perceptrons (MLPs). Concretely, autoencoders, which contain an encoder and a decoder, are usually used to extract features [24,42]. Because of the small sample sizes and high dimensions of brain network data, FCNN
models with many parameters are easily prone to over-fitting. More unfavorably, FCNNs reshape the brain networks into
vectors, which may discard their topological structures. Later methods used convolutional neural networks (CNNs) to analyze
brain networks, which employ local connections and weight-sharing schemes to extract high-level features from grid data

[11,12,16]. Local operations can reduce the computational complexity caused by the excessive number of parameters in
FCNNs. For example, BrainNetCNN [16] employed new feature extraction structures according to the topological locality
characteristics of brain networks. Moreover, several studies have utilized CNNs for brain biomarker interpretation [11,34]
in recent years. Despite the success of existing CNN models, they still assume that the input network structures are regular
grids, which hinders their application in tasks with irregularly structured data.
GNNs were proposed as a generalization of CNNs by extending the concept of convolution from Euclidean geometry (regular structures) to general graph domains (non-regular structures) [19]. In contrast to existing deep learning architectures,
GNNs contain fewer parameters, can handle non-regular structures, and introduce relational inductive bias into data-driven
systems [4]. It is therefore commonly believed that GNNs can learn better representations of brain network data. Current
GNNs for functional brain network classification are generally divided into two categories: spectral and spatial methods.
Spectral methods extend the graph convolution to the frequency domain by Fourier transform [19]. The first method proposed in [20] incorporates graph convolutions in a Siamese network architecture. The ASD and typical controls (TC) groups
are separately fed into two GNNs that share the same model architecture. Based on this work, Yan et al. [40] further utilized
the idea of node grouping aggregation in the design of neural networks to eliminate the influence of size-limited and noisy
brain data. Spatial methods directly update the representation of each central node by aggregating the features of its adjacent nodes [38]. To select important neighbors, several studies [18,22] have introduced an attention mechanism to learn and
assign corresponding weights to different adjacent nodes so that the neighbor features can be adaptively aggregated.
Besides functional brain network classification, GNNs can be used in many other brain cognition tasks, such as brain network representation learning [28], brain graph structure learning [10], and model interpretability [40]. Despite the success of
existing GNN methods, there still exist limitations in modeling complex functional brain networks that cannot only be
described by pair-wise connections.
Another line of brain data analysis methods mainly focus on EEG, which is used to measure the electrical activity of
brains. In the data preprocessing stage, multiscale principal component analysis (MSPCA) is often used to remove noise from
the data [32,33]. Moreover, because of the temporal property of EEG signals, signal decomposition methods are applied to
extract the underlying dynamics of patterns [29,31]. After data preprocessing, various deep learning methods (e.g., recurrent
autoencoders [37]) can be used for feature learning and classification. The original EEG signals are usually modeled as
dynamic sequences with temporal properties that reveal the changes in brain functions over time [32]. The functional brain
networks are usually modeled as graphs with spatial properties that focus on the structural and functional functions of brain
regions with spatial changes [20].


2.2. Hypergraph Neural Networks


A hypergraph is the generalization of a simple graph, which has been used to characterize the high-order relations among
multiple nodes [45]. The primary difference between ordinary graphs and hypergraphs is that the hyperedges can directly
connect an arbitrary number of nodes instead of only two nodes. One critical problem of hypergraph learning is efficiently
learning deep embeddings from high-order graph-structured data, which has been explored in several studies that extend
graph-convolutional operators to hypergraphs. The hypergraph neural network (HGNN) [6] first introduces hypergraph representation learning based on deep learning models, which has outperformed conventional GNNs in some classification and
object recognition tasks. Motivated by HGNNs and GNNs, Yadati et al. [39] designed a more efficient and faster model for
training GNNs on hypergraphs (HyperGCN). In dynamic hypergraph neural networks (DHGNN) [15], the hypergraph structure can be dynamically built based on the new feature embeddings without explicitly defining the hypergraph. Recently,
hypergraph attention has further enhanced the capacity of hypergraph representation learning by leveraging an attention
module [43]. Because of its advantages, the hypergraph structure can be used in many downstream applications, such as
computer vision [47], recommendation systems [14], and medical image analysis [25]. For example, to diagnose ASD using


1303


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


T1-W MRI data, Madine et al. [25] used a hypergraph convolution layer to learn latent relationships among different subjects
based on a population hypergraph.


3. Method


3.1. Preliminaries and Framework


3.1.1. Preliminaries
A functional brain network is typically represented as a graph G ¼ ðV; EÞ with a node set V and an edge set E. A set of

graphs can be denoted as G ¼ fGig [Q] i¼1 [, where][ Q][ is the number of graphs. Each graph][ G][i] [is associated with a label][ ‘][i][. The adja-]
cency and attribute matrices can be denoted as Ai 2 R [N][i][�][N][i] and Xi 2 R [N][i][�][D], respectively, where Ni is the number of brain
regions in Gi, and D is the dimension of features. In practice, we can set all Ni equal to N.
A hypergraph can be formulated as H ¼ ðV; EÞ, where V denotes the node set, and E denotes the hyperedge set. In a brain
network, node v i denotes the i-th brain region, and hyperedge ei denotes the i-th node set, which contains a flexible number
of brain regions. The incidence matrix of a hypergraph can be denoted as I 2 R [N][�][M], where M is the number of hyperedges.

Ii;j ¼ 1 if node v i is in hyperedge ej, and Ii;j ¼ 0otherwise. The degree of v i is defined as di ¼ [P][M] j¼1 [I][i][;][j][, and the degree of hyper-]

edge ej is defined as dj ¼ [P][N] i¼1 [I][i][;][j][.] [Further,] [D][v] [2][ R][N][�][N] [denotes] [the] [diagonal] [matrices] [of] [node] [degrees.]
GNNs follow a universal message-passing architecture, which interactively aggregates information from neighbors. The
propagation rule between the ðl � 1Þ-th and l-th layers consists of two steps:

      -       a [ð Þ] i [l] ¼ f AGG zðj [l][�][1] Þjv j 2 N ðv iÞ ; ð1Þ


      -       z [ð Þ] i [l] ¼ f COM zði [l][�][1] Þ; a [ð Þ] i [l] ; ð2Þ


where N ðv iÞ is the neighbor set of node v i; zðj [l][�][1] Þ is the representation of node v j in the ðl � 1Þ-th layer, a [ð Þ] i [l] is the neighbor

information aggregated by the aggregation function f AGG, and f COMis the combine function, which combines the information

of node v i and the neighbor information a [ð Þ] i [l] [.] [After] [these] [two] [steps,] [the] [features] [of] [node][ v] [i] [are] [updated.] [To] [obtain] [a] [graph-]
level representation, the readout function is used to summarize node representations in the last layer as a vector:

       -        ^z ¼ Readout zði [L] Þ [j][v] [i] [2][ V] ; ð3Þ


where zði [L] Þ is the output of the last convolution layer.


3.1.2. Framework
Our framework is illustrated in Fig. 1, which includes the dynamic hypergraph generation and hypergraph attention aggregation phases. First, the functional brain networks are fed into the GNNs to generate initial node embeddings that keep both
the structural and attribute information from the original space. Second, the dynamic hypergraph generation phase generates hypergraphs based on the initial embeddings. The primary goal is to define appropriate distance functions that can capture high-order information in brain networks. To this end, we leverage KNN and k-means to describe the pair-wise and
community-wise information separately. Third, the hypergraph attention aggregation phase updates the node embeddings
based on the constructed hypergraphs. Because the traditional graph attention paradigm cannot be directly applied to hypergraphs, we design attention aggregation methods to separately generate hyperedge and node embeddings. Then, the
updated node embeddings from the hypergraph attention aggregation phase can be fed into the hypergraph generation
phase, which formulates a dynamic process to update the hypergraph structures. By joint optimization, we can obtain the
optimal hypergraphs and node embeddings in an end-to-end manner. Finally, the readout layer is used to obtain the representation of the entire functional brain network, which can be further fed into an MLP for the functional brain network classification. We introduce the details of these components of our model in the following subsections.


3.2. Dynamic hypergraph generation


The functional brain network in previous methods is mainly modeled as a simple graph, which may fail to consider the
complex interactions between brain regions. In this subsection, we introduce a dynamic hypergraph generation phase to represent functional brain networks as hypergraphs. There are two types of methods to generate hypergraphs. Explicit hypergraph methods attempt to generate hypergraphs based on inherent structural information, while implicit methods generate
hypergraphs based on the embeddings in the feature space. We use implicit hypergraph generation because it can avoid the
influence of noise. The hypergraph generation contains two main components. First, the embedding function Ue maps the
raw data to a feature space that can reveal the underlying structures of the raw data. Second, the distance function Ud calculates the similarities of the generated features, which can be used to generate hyperedges.


1304


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


Fig. 1. Overall framework of the proposed model. The first row gives an overview of our model, which mainly consists of the dynamic hypergraph generation
(DHG) and hypergraph attention aggregation (HAA) phases. The generation of hyperedges e1 and e2 for node v i based on KNN and k-means is described on the
left of the second row. For KNN, we select the top-k1ðk1 ¼ 2Þnearest neighbors. e1 is a node set that contains u and the above 2 neighbors. For k-means, all
nodes are first grouped into C clusters. After calculating the distances between v i and the C clusters, the top-k2 nearest clusters are selected to construct k2
hyperedges (k2 ¼ 1). e2 is a node set that contains u and the nodes in the selected clusters. The embeddings of hyperedges and nodes are calculated on the
right of the second row. The embedding of u is calculated by node attention, which aggregates information from e1 and e2. The embeddings of e1 and e2 are
calculated by hyperedge attention from u and other nodes that are also contained in e1 and e2.


The embedding function Ue is implemented based on the graph-convolutional operations that can make full use of both
structural and attribute information. Based on Eqs. (1) and (2) the embedding function can be denoted as


Z ¼ UeðX; AÞ; ð4Þ


where Z is the node embedding matrix in the feature space. The learned embeddings extract high-level information and capture salient patterns in the raw data. Consequently, they can remove noise and are more robust to different data
distributions.
The distance function Ud measures the similarities between any two nodes based on their embeddings. In general, we can
define the distance function as

       -        Sij ¼ Ud zi; zj ; ð5Þ


where Si;j denotes the similarity between nodes v i and v j, and zi and zj are the embeddings of v i and v j, respectively. Most
distances in graphs are based on local information, for example, the direct connections between nodes. To consider more
information in graphs, we aim to define a distance function that combines different aspects of similarities. Specifically,
for each node v i, we first use KNN to find the k1 nearest neighbors. The hyperedge is constructed as a node set that includes
v i and its k1 neighbors. KNN can only capture pair-wise similarities. To further extract the substructures and communitywise similarities in the graph, we use k-means to generate C clusters that serve as candidates to formulate hyperedges.
We can then calculate the distances between v i and the C cluster centroids obtained by k-means. The k2 hyperedges that
represent the nearest clusters are also selected to describe node v j. We can denote hyperedge ej constructed from KNN
and k-means as

ej ¼ fv 1; v 2; ��� ; v kg; ð6Þ


where k is the number of nodes in ej. For both the KNN and k-means algorithms, Euclidean distance is used to calculate the
node similarities:




    -     E � dist v i; v j ¼



vfi fi fi fi fi fi fi fi fi fi fi fi fi fi fi ffi
uutXDð [L] Þ - �2

zi;p � zj;p ; ð7Þ
p¼1


1305


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


where E � dist�ð Þ is the Euclidean distance between node v i and v j, and Dð [L] Þ is the feature dimension in the L-th layer. For
KNN, k ¼ k1 þ 1. By combining KNN and k-means, the generated hyperedges can better reflect multi-level interactions
among nodes.
Furthermore, we can describe a target node by multi-level interactions of hyperedges as qð v iÞ. For a given node v i; q vð iÞ
describes all hyperedges that include v i. q vð iÞ can be denoted as
q vð iÞ ¼ fe1; e2; ��� ; emg; ð8Þ


where e1 is generated by KNN, and fe2; ��� ; emg is generated by k-means.
With the help of the embedding function Ue and distance function Ud, we can build a hypergraph that contains M hyperedges. We perform such a procedure in each layer to dynamically update the hypergraph. In particular, we initialize the
hypergraph with the initial node embedding matrix. Therefore, the hyperedge set can be adjusted according to model depth.
In this manner, we can obtain better hypergraph structures to model high-order relations with deep neural networks. Based
on the constructed hypergraph, we define aggregation operators to learn node representations in the next subsection.


3.3. Hypergraph Attention Aggregation


After obtaining the hypergraphs for brain networks, we employ a hypergraph attention aggregation phase to extract highorder structure information. The uniform aggregation strategy in previous models eliminates the differences of nodes that
can distinguish the importance of neighbors during the aggregation process. Consequently, we introduce an attention mechanism to the aggregation process. The propagation rule between the ðl � 1Þ-th and l-th layers can be written as



0


@



X
z [ð Þ] i [l] ¼ r@



ai;jW [ð Þ][l] zðj [l][�][1] Þ
v j2N ðv iÞ



1


A; ð9Þ



where ai;jis the attention weight that measures the strength of connection between node v iand its neighbor v j. It can be calculated as

          -           -           - ���
ai;j ¼ ~~X~~ exp ReLU ~~�~~ a Wz ~~�~~ ~~�~~ ijjWzj ~~���~~ ; ð10Þ

exp ReLU a WzijjWzq
v q2N ðv iÞ


where a is the attention weight vector, jj is the concatenation operation, and Wis the parameter matrix.
To develop attention aggregation for hypergraphs, we separately consider node attention and hyperedge attention layers.


3.3.1. Node Attention Layer
The node attention layer updates the hyperedge embeddings based on nodes contained in the hyperedge. For each hyper
��
edge ej in qð v iÞ, we first obtain k node features Z ej ¼ fzig [k] i¼1 [, where][ v] [i] [2][ e][j][. Then, the][ k][ node feature vectors are aggregated]
to update the hyperedge features. This step can be described simply as follows:

        - ���
yj ¼ Uv!e Z ej ; ð11Þ


where yj is the representation of hyperedge ej, and Uv!eis the node aggregation function applied concurrently to all hyperedges. The attention mechanism in Uv!ecan be achieved by a fixed and precomputed transform matrix T generated from
hypergraph structures. In detail, we use MLP to learn the transform matrix T 2 R [k][�][k] from the node embedding matrix Z
for feature permutation and weighting adaptively. The transform matrix T enables both inter-node and inter-channel information flow. Then, 1-D convolution is leveraged to compress the transformed features. The implementation of Uv!ecan be
formulated as

        - ���
T ¼ MLP Z e�j ; ��� ð12Þ

yj ¼ Conv1D TZ ej ;


where Conv1Ddenotes the 1-D convolution operation.


3.3.2. Hyperedge Attention Layer
The hyperedge attention layer updates node features based on the updated hyperedge embeddings Y. Considering that
excessive aggregation can be redundant or even harmful, the self-attention mechanism is employed. Specifically, we use
MLP to generate the weight score for each hyperedge. Then, the output features of the target node are calculated as a
weighted sum of input hyperedge embeddings. The procedure can be formulated as

           -           bi;j ¼ Softmax We yj ;

Xm ð13Þ
zi ¼ bi;j yj;

j¼1


1306


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316



where bi;j is the attention score of the j-th hyperedge toward node v i; We is the weight parameter matrix in the hyperedge
attention layer, and mis the size of adjacent hyperedge set qð v iÞfor node v i.

In summary, for each hyperedge ej in the node attention layer, we transform node embeddings �zijv i 2 ej�ki¼1 [to constitute]
an embedding vector yj. Then, in the hyperedge attention layer, the weighted average of hyperedge embeddings



�yjjej 2 q�v j��m



j¼1 [is] [calculated] [to] [formulate] [node] [embedding] [z][i][.]



3.4. Algorithm and Spectral Analysis


3.4.1. Algorithm
Based on the updated node embeddings, the readout layer generates the representation [^] z for the corresponding hypergraph. [^] z can be denoted by


XN
^z ¼ ReadoutðZÞ ¼ zi: ð14Þ

i¼1


Then, by applying MLP with a Softmax layer to the hypergraph representation, we obtain the label ‘of hypergraph H. The
detailed algorithm of the proposed model is presented in Algorithm1.


Algorithm1: Hypergraph attention network for functional brain network classification (FC–HAT).


Input: Maximum number of iterations iters, total number of layers L, training data fðXi; Ai; ‘Þg [Q] i¼1 [;]

Output: Hypergraphs fHig [Q] i¼1 [,] [optimal] [parameter] [matrix] [W][�][;]
Initialization Randomly initialize parameter matrix W;
1: while iter <¼ iters do
2: Take each training sample as an input;
3: Obtain initial node embedding matrix Z by Eq. (4);
4: whilel < L do

                        -                         5: Run KNN and k-means to obtain hyperedges E ¼ ejjj ¼ 1; 2; ��� ; M ;
6: Obtain hypergraph H based on nodes V and hyperedges E;

7: Run node attention aggregation Eq. (12) to obtain hyperedge embedding matrix Y [ð Þ][l] ;

8: Run hyperedge attention aggregation of Eq. (13) to obtain node embedding matrix Z [ð Þ][l] ;
9: end while

10: Obtain ‘ [~] based on Zð [L] Þ by successively employing the readout and MLP layers;
11: Calculate the cost based on ‘ [~] and ‘;
12: Update W by stochastic gradient descent;
13: end while
14: return W [�] ¼ W.


3.4.2. Spectral Analysis
GNNs can be interpreted as low-pass filters for which the spectrum of the adjacency matrix is an essential indicator for
the success of feature propagation [41]. In the following, we give the spectral analysis of the adjacency matrix for the
obtained hypergraph. Based on the incident matrix I, the adjacency matrix A [0] of the hypergraph can be denoted as


A [0] ¼ I � I [>] ; ð15Þ


where each element can be denoted as

X
A [0] i;j [¼] Ii;kIj;k: ð16Þ

ek2E

A [0] i;j [can be viewed as the summation of the proportional weights over all hyperedges incident with both nodes][ v] [i][ and node]
v j. Thus, A [0] can be further expressed as

A [0] ¼ A þ !1 þ !2; ð17Þ


where element c1 of matrix !1 equals the i-th node degree di, and element c2 of matrix !2 equals the number of hyperedges
that node v iand node v jare simultaneously contained in. It is worth noting that A [0] is symmetric.
Similar to the Laplacian matrix symD [of] [a simple graph, let][ E][N] [denote an identity matrix, the symmetric normalized hyper-]

graph Laplacian matrix Csym is defined as


1307


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


Csym ¼ EN � D [�] v [1][=][2] A [0] D [�] v [1][=][2] : ð18Þ


For any signal z 2 R [D], it satisfies



!2


ð19Þ

:



~~pf f f f f~~ A ~~f~~ [0] ij ~~f f f f f f f~~ ~~pf f f f f~~ z ~~f~~ i ~~f f f f f f f~~ - ~~pf f f f f~~ z ~~f~~ j ~~f f f f f f f~~
di þ c1 þ c2 di þ c1 þ c2 dj þ c1 þ c2




- Csymz



i [¼] [1] 2



XN


j



The signal variation on the hypergraph is quantified by



XN

A [0] i;j
j¼1



~~pf f f f f~~ z ~~f~~ i ~~f f f f f f f~~ - ~~pf f f f f~~ z ~~f~~ j ~~f f f f f f f~~
di þ c1 þ c2 dj þ c1 þ c2



!2



Z [>] CsymZ ¼ [1] 2



XN


i¼1



ð20Þ

:



Based on the above equation, we can check that Csym is symmetric positive semidefinite (non-negativity), and 0 is the smallest eigenvalue from the non-negativity of Csym [45].
Given the eigenvalues k1 6 ��� 6 kN of the normalized graph Laplacian matrix, where k1 < 0 and kN  - 1, we can analyze
the spectrum of Csymas follows:


Theorem 1. Let k [0] 1 [and] [k][0] n [be] [the] [smallest] [and] [largest] [eigenvalues] [of] [C][sym][,] [respectively.] [We] [have]

k1 6 k [0] 1 [6][ k] n [0] [<][ k][n][:] ð21Þ


Proof. By choosing z such that jjzjj ¼ 1, we have




      -       k [0] n ¼ max
jjzjj¼1 [z][>][C][sym][ z]

      -      ¼ maxkzk¼1 [z][>] [E][ �] [c][1][D][�] v [1] [�] [c] 2 [D][�] v [1] [�] [D] v [�][1][=][2] AD [�] v [1][=][2] z

6 1 � kminzk¼1 [c][1][z][>][D] v [�][1][z][ �] k [min] zk¼1 [c][2][z][>][D] v [�][1][z][ �] k [min] zk¼1 [z][>][D] v [�][1][=][2] AD [�] v [1][=][2] z



ð22Þ



Let f ¼ D [1] v [=][2][D] a [�][1][=][2] z. Then, we have jjfjj [2] ¼ [P] i



diþcd1iþc2 [z] i [2] [and] minimindiþicd1iþc2 [6][ jj][f][jj][2] [6] maxmaxidiþicd1iþc2 [.] [Based] [on the Rayleigh] [quotient,]


ð23Þ



we have




  -  kminzk¼1 [z][>][D] v [�][1][=][2] AD [�] v [1][=][2] z




   -   ¼ min >Da�1=2ADa [�][1][=][2] f
kzk¼1 [f]



P min
kzk¼1




- - - 
f [>] D [�] a [1][=][2] AD [�] a [1][=][2] f max

kfk [2] kzk¼1 [k][f][k][2]



f [>] D [�] a [1][=][2] AD [�] a [1][=][2] f



¼ k1max
kzk¼1 [k][f][k][2]



maxdi

P ~~max~~ di iþc1þc2 [k][1]

i



Thus, Eq. (22) can be further expressed as

kn ¼ 1 � c1þ ~~max~~ c1 di [�] c2þ ~~max~~ c2 di [�] [l][1]
i i



ð24Þ



6 1 � c1þ ~~max~~ c1 di [�] c2þ ~~max~~ c2 di [�]
i i



maxdi
i

c1þc2þ ~~max~~ di [k][1]
i



< 1 �



maxdi

c1þc2þi ~~max~~ di [k][1] ðc1 - 0; c2 - 0Þ
i



< 1 � k1 ¼ knðk1 < 0Þ


This completes the proof.

Theorem 1 shows that using the incident matrix I shrinks the spectrum (eigenvalues) of the normalized graph Laplacian
generated by A (see Proof 3.4.2). This indicates that the constructed hypergraph incident matrix I affords better spectrum
properties.


4. Experiments


In this section, we conducted empirical experiments on real fMRI datasets to evaluate the effectiveness of the proposed
method. The experimental platform was a PC with an Intel Core i7-9750H 2.60 GHz CPU, NVIDIA GeForce GTX 1660Ti GPU,
and Windows 10. The code and data are available at https://github.com/uuup123/FC–HAT.


1308


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


4.1. Experimental Settings


Datasets. Two real datasets, ABIDE-I [5] and ADHD-200 [27], were used in this study. Both datasets contain rs-fMRI, sMRI,
and clinical phenotype data. More specifically, ABIDE-I includes 1,112 subjects from 17 international sites, and ADHD-200
consists of 850 subjects from 8 sites. We adopted the rs-fMRI data preprocessed by the Preprocessed Connectomes Project
(PCP). The preprocessing was performed by the Data Processing Assistant for Resting-State fMRI (DPARSF) software. Then, 90
brain regions (N ¼ 90) in the cerebral cortex were selected as brain regions of interest via Automated Anatomical Labeling
(AAL) template, and the corresponding mean time series were extracted. Finally, the Pearson correlation coefficients (PCCs)
between each pair of brain regions were calculated to produce a weighted adjacency matrix for each subject, which corre
                                 -                                  sponds to the functional brain network of the subject. Given the time series T i ¼ T i;1; T i;2; ��� ; T i;s of each node v i, where
sindicates the length of time series, the correction Pi;j of nodes v iand v jcan be obtained by



Xs







Pi;j ¼



~~sf~~ X ~~f~~ s ~~f f~~ - ~~f f f f f f f f f f� f~~ 2 ~~f~~
T i;l �T i
l¼1



~~f~~ X ~~f~~ s ~~f f~~ - ~~f f f f f f f f f f� f f~~



Xs - ~~�~~ - ~~�~~

T i;l �T i T j;l �T j
l¼1



~~sf~~ X ~~f~~ s ~~f f~~ - ~~f f f f f f f f f f� f~~ 2 ~~f~~ : ð25Þ
T j;l �T j
l¼1



~~f~~ X ~~f~~ s ~~f f~~ - ~~f f f f f f f f f f� f f~~



Because zero BOLD signal vectors will generate meaningless Pearson correlations, some samples preprocessed by PCP were
removed. Thus, we obtained 1,096 functional brain networks from the ABIDE-I dataset: 569 TCs and 527 individuals with
ASD. For the ADHD-200 dataset, we obtained 520 functional brain networks: 329 TCs and 191 individuals with ADHD.
For both datasets, we randomly selected 60%, 20%, and 20% of samples as training, validation, and testing datasets, respectively. Our method and all baseline approaches followed the same data split.
Baseline Methods. The proposed framework is compared with six typical baseline methods: SVM [36], LASSO [46], DAE

[42], BrainNetCNN [16], CKEW [11], and s-GCN [20]. For SVM and LASSO, the number of selected features was 200, and the

weight decay parameter of L1regularization was set as kL1 ¼ 5 � 10 [�][3] . For DAE [42], the number of layers was set as 4, where
two auto-encoder layers with 200 neurons were used, except in the input and output layers. For BrainNetCNN [16] and
CKEW [11], two convolutional layers and two max-pooling layers were employed, where the convolutional layers contain
64 kernels with a 3 � 3 shape. s-GCN parameters were set according to [20], including two convolutional layers consisting
of 64 features, third-order polynomial filters, and ten neighbors for the graph structure. For fair comparisons, all hyperparameters in the above methods were tuned to be optimal on the benchmark datasets.
Model Settings. In our experiment, we constructed a hyperedge set including 110 hyperedges for each person. The first
90 hyperedges were generated by KNN, and the remainders were generated by k-means. We employed a 2-layer hypergraph
attention layer with a graph convolution layer for feature dimension reduction. Initial feature dimensions were 90, which
were transformed to 32 by a graph convolution layer. RELU was selected as the non-linear activation function of the convolution layer. The dropout ratio was set to 0.5 in each layer. During the training process, we used stochastic gradient descent
(SGD) with adaptive moment estimation (ADAM) as the optimization algorithm to minimize our cross-entropy loss function
with an initial learning rate of 0.001.
Evaluation Metrics. To evaluate the classification performance, five common evaluation metrics were used: accuracy
(ACC), sensitivity (SEN), specificity (SPE), positive predictive value (PPV), and negative predictive value (NPV).


4.2. Classification performance


In this experiment, we evaluated the classification performance of our method and the six baseline methods on the
ABIDE-I and ADHD-200 datasets. The results are listed in Tables 1 and 2.
For ABIDE-I, it can be observed that FC–HAT outperformed the other six competing methods on all six metrics. Compared
with traditional methods such as SVM and LASSO, FC–HAT can extract high-level information from high-dimensional and
non-linear functional connections. Compared with the other four deep learning methods, FC–HAT achieved the most competitive performance on all metrics. Among them, FC–HAT achieved better performance than FCNN and CNN, which demonstrates that our method can learn better graph representations from irregular graph structures in functional brain networks.


Table 1
Classification performance of different methods on ABIDE-I.


Dataset Methods ACC SEN SPE PPV NPV


ABIDE-I SVM 0.634 0.644 0.664 0.623 0.699
LASSO 0.636 0.609 0.661 0.625 0.678
FCNN 0.647 0.622 0.670 0.622 0.688
BrainNetCNN 0.654 0.628 0.676 0.629 0.694
CKEW 0.683 0.647 0.717 0.647 0.717
s-GCN 0.671 0.690 0.620 0.670 0.714
FC–HAT 0.709 0.700 0.723 0.673 0.750


1309


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


Table 2
Classification performance of different methods on ADHD-200.


Dataset Methods ACC SEN SPE PPV NPV


ADHD-200 SVM 0.638 0.703 0.519 0.639 0.590
LASSO 0.676 0.703 0.603 0.682 0.627
FCNN 0.681 0.802 0.474 0.649 0.664
BrainNetCNN 0.671 0.747 0.545 0.665 0.640
CKEW 0.687 0.824 0.456 0.647 0.682
s-GCN 0.651 0.792 0.415 0.621 0.622
FC–HAT 0.692 0.830 0.468 0.654 0.695


Furthermore, the better results than s-GCN verify that FC–HAT is more powerful and capable of modeling complex data association. On the smaller ADHD-200 dataset with uneven label distribution, FC–HAT still achieved the best scores in ACC, SEN,
and NPV. Notably, LASSO achieved the highest performance in both the SPE and PPV metrics on this dataset. However, in
general, our method achieved the best performance on most of the metrics and datasets.


4.3. Classification Performance with MSPCA


Multiscale principal component analysis (MSPCA) is an effective noise removal method in many brain-related applications. In this subsection, we follow previous works [32,33] and apply MSPCA to the processed data to verify the performance
improvement. The classification results of our method and all baseline methods with and without MSPCA on ABIDE-I and
ADHD-200 are reported in Fig. 2. For ABIDE-I, it can be observed that all methods with MSPCA achieved performance
improvements: 0.005 for SVM, 0.004 for LASSO, 0.019 for FCNN, 0.023 for BrainNetCNN, 0.005 for CKEW, 0.015 for s-GCN,
and 0.018 for FC–HAT. BrainNetCNN and LASSO gained the most and the least improvements, respectively. For ADHD200, it can be observed that the ACCs of SVM, FCNN, CKEW, and s-GCN were improved by 0.004, 0.002, 0.002, and 0.003,
respectively. The ACCs of LASSO and BrainNetCNN were degraded by 0.002 and 0.003, respectively. The accuracy of FC–
HAT was unaffected. This may be because of the dynamic hypergraph generation module in our model keeping salient information and removing noises to some extent. For both datasets, FC–HAT achieved the best performance regardless of whether
MSPCA was utilized. It is notable that FC–HAT without MSPCA still achieved a better performance than the baseline models
with MSPCA, which demonstrates the effectiveness of our method.


4.4. Ablation Experiments


To evaluate the effectiveness of the dynamic hypergraph generation (DHG) and hypergraph attention aggregation (HAA)
phases in our model, we conducted two ablation experiments on the ABIDE-I dataset. For the ablated model Only-HAA,
we used the inherent graph structure of the functional brain network for convolution operation. For the ablated model
Only-DHG, we replaced the node attention and hyperedge attention layers with average pooling. We compared the two
ablated models against the complete model and investigated the influence of feature dimension in the L-th layer on classification accuracy. The results are shown in Fig. 3. We observed that both the DHG and HAA phases can improve classification

accuracy. The classification accuracies of the three models increased with increasing Dð [L] Þ and peaked when DðLÞ was 32.















Fig. 2. Classification performance of different methods with and without MSPCA on ABIDE-I and ADHD-200 datasets.


1310


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


|Only-HAA Only-DHG FC-HAT<br>0.7<br>ACC<br>0.6<br>0.5<br>0.4<br>4 8 16 32 64 90<br>D(L)|Only-HAA Only-DHG FC-HAT|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||
|4<br>8<br>16<br>32<br>64<br>90<br>0.4<br>0.5<br>0.6<br>0.7<br>ACC<br>_D_(_L_)<br>Only-HAA<br>Only-DHG<br>FC-HAT||||||||||||||||||||||||||



Fig. 3. Comparison of two ablated models and complete model on ABIDE-I dataset. Dð [L] Þ is the feature dimension in the L-th layer. Only-HAA and Only-DHG
are the ablated models with only the HAA and DHG phase, respectively.


Among them, the complete model was always better than the other two ablated models, which implies that the model with
both phases can better aggregate neighborhood features.


4.5. Parameter Analysis


To evaluate the influences of hyperparameters on classification performance, we performed controlling variable experiments on the two main hyperparameters: hyperedge degree k and number of aggregation layers L.
Hyperedge Degree k. Fig. 4 shows the performance of FC–HAT affected by different values of hyperedge degree
k ¼ f2; 3; 4; 5; 6; 7; 8; 9; 10g on the ABIDE-I dataset.
We can observe that the performance of FC–HAT is significantly affected by the hyperedge degree k. The highest accuracy
was achieved when k ¼ 4. Inadequate mining of relationships leads to poor performance when k < 4. When k > 4, the range
of information aggregation increases and different node representations tend to be homogeneous (all node representations
are almost the same in the same connected component).
Hypergraph Attention Aggregation Layers L. Fig. 5 shows the influence of the number of hypergraph attention aggregation layers on the classification accuracy on the ABIDE-I dataset. By analyzing the experimental results, we make the





















Fig. 4. Influence of increasing hyperedge degrees k from 2 to 10 on the classification accuracy on ABIDE-I.


1311


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316



Fig. 5. Influence of the number of hypergraph attention aggregation layers L in the range of 0 to 4 on the classification accuracy on ABIDE-I.


following observations: First, when L ¼ 0, the model without the HAA layer performs poorly. This suggest that adding the
HAA layer can greatly improve the model performance. Second, after the first aggregation, adding more aggregation layers
leads to performance degradation. This might result from the over-smoothing problem in deep GNN architectures, which
tends to learn homogeneous features for all nodes.


4.6. Functional Connectivity Analysis


To find brain regions and functional connectivity patterns in a brain network that can make strong contributions to discriminating individuals with ASD from TC group, we use the importance metric of features (IMF) [11] to measure the importance scores of features in each layer. The IMF metrics in the node attention and hyperedge attention layers are used to
determine the important nodes and hyperedges in the original brain network for the classification results, respectively.
We randomly selected two samples from the ABIDE-I dataset (id ¼ 50823 in ASD group and id ¼ 50817 in TC group) to
visually illustrate the top-18 abnormal connectivity patterns of ASD patients and the TC group (see Fig. 6). Furthermore,


Fig. 6. Heatmap visualization of the top-18 important functional connections of ASD and TC.


1312


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316

























Fig. 7. Important high-order connections in ASD and TC.


Fig. 7 intuitively describes the differences in high-order connections between multiple brain regions. In these figures, darker
colors and wider connections indicate regions that are more strongly correlated and vice versa. More specifically, we can
easily find that many connections are significantly reduced, that is, the functional connectivity between left angular gyrus
(ANG.L), right inferior temporal gyrus (ITG.R), right gyrus rectus (REC.R), and right supramarginal gyrus (SMG.R) in the
default mode network (DMN) subnetwork. This phenomenon can be explained through the repetitive and stereotyped
behaviors of ASD patients. This also confirms some existing research conclusions [21]. The 3-order exception connectivity
between left superior frontal gyrus (dorsolateral, SFGdor.L), REC.R, and right middle temporal gyrus (MTG.R) among DMN
and explicit congestion notification (ECN) subnetworks indicates that weak connections are associated with the task performance of selective attentions, which is consistent with recent research findings [35]. Right thalamus (THA.R), MTG.R, and left
middle temporal gyrus (MTG.L) are connected weakly between DMN and salience network (SN) subnetworks in the functional brain networks of ASD patients. The reduced connections foreshadow the defects of the individual external goalrelated behavior and self-consciousness, which again verifies the conclusion of a previous study [30]. The functional connectivity between right inferior frontal gyrus (opercular part, IFGoperc.R) and left lenticular nucleus (putamen, PUT.L) related to
mirror neuron system (MNS) subnetwork may be related to verbal communication difficulties [3]. Additionally, some connections are significantly enhanced, such as the connectivity between left cuneus (CUN.L), right cuneus (CUN.R), and MTG.R
in the DMN subnetwork and the connectivity between left superior temporal gyrus (STG.L), THA.R, and left heschel gyrus
(HES.L) related to DMN and SN subnetworks. In essence, the reduced connections may be related to some mental and behavioral impairments. The enhanced connections do not mean that ASD patients have a strong ability to regulate and control,
and may simply be a recovery mechanism.
Furthermore, we selected the top-10 important brain regions: right inferior frontal gyrus (triangular part, IFGtriang.R),
left superior frontal gyrus (medial, SFGmed.L), right superior frontal gyrus (medial orbital, ORBsupmed.R), REC.R, left posterior cingulate gyrus (PCG.L), ANG.L, right precuneus (PCUN.R), left thalamus (THA.L), THA.R, MTG.R, and ITG.R, as shown in
Fig. 8. These regions are mostly distributed in the DMN, SN, and medial temporal gyrus. Superior frontal gyrus belongs to
frontal Lobe. Liu et al. [23] concluded that children with autism showed no mirror neuron activity in the inferior frontal gyrus
while imitating and observing emotional expressions. Both IFGoperc.R and IFGtriang.R belong to the inferior frontal gyrus.
Moreover, higher brain functions in the prefrontal and temporal cortices are not fully mature until the end of youth and early
adulthood. The mature processes of ASD patients in these areas will be damaged, which will lead to social, language, and
other dysfunctions. MTG.R and ITG.R are parts of temporal cortices, and REC.R and IFGtriang.R are located in prefrontal cortices; therefore, these brain regions are closely related to the symptoms of ASD patients.


5. Conclusion


In this study, we proposed a hypergraph attention network to extract the underlying and high-order information in functional brain networks. Our first aim was to formulate informative hypergraphs while making the structures learnable. To
accomplish this goal, we built a dynamic hypergraph generation phase that captures both pair-wise and community-wise
similarities in graphs. A spectral analysis showed that the learned hypergraphs reveal better low-pass properties and are
more powerful when using GNNs. Our second aim was to develop suitable GNNs under hypergraphs. We then resorted to
a node aggregation layer and hyperedge aggregation layer to alternately update node and hyperedge embeddings. Results
on the ABIDE-I and ADHD-200 datasets demonstrate that our model achieved similar or better performance compared with


1313


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


Fig. 8. Visualization of the top-10 brain regions.


the state-of-the-art methods. Ablation studies and parameter analysis showed that the aggregation framework in our model
can extract useful connectivity patterns from hypergraphs. In addition, the identified abnormal connections demonstrated
the explainability of our classification results.
Our work can be further combined with other operations in GNNs. For example, pooling operations can be used to extract
hierarchical information in functional brain networks. Moreover, our current implementations of hypergraph generation are
mainly based on KNN and k-means, which rely on a fixed and handcrafted generation process. As a future work, we envision
an end-to-end hypergraph generation strategy that can formulate a generative model to learn parameterized hypergraphs
from data. Further, instead of using atlas-based brain region correlations as model inputs, we can design deep hypergraph
generation methods based on voxel data.


CRediT authorship contribution statement


Junzhong Ji: Methodology, Writing - original draft, Validation. Yating Ren: Methodology, Data curation, Software, Visualization, Investigation, Writing - review & editing. Minglong Lei: Conceptualization, Supervision, Validation, Writing review & editing, Funding acquisition.


Declaration of Competing Interest


The authors declare that they have no known competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.


Acknowledgments


This work was supported by the R&D Program of Beijing Municipal Education Commission (KZ202210005009).


1314


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


References


[1] S. Agarwal, K. Branson, S. Belongie, Higher order learning with [graphs,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0005) International Conference on, Machine Learning (2006) 17–24.

[2] [A.M. Anter, Y. Wei, J. Su, Y. Yuan, B. Lei, G. Duan, W. Mai, X. Nong, B. Yu, C. Li, Z. Fu, L. Zhao, D. Deng, Z. Zhang, A robust swarm intelligence-based feature](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0010)
selection model for neuro-fuzzy recognition of mild cognitive [impairment](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0010) from resting-state fmri, Information Sciences 503 (2019) 670–687.

[3] [G.J. Cler, S. Krishnan, D. Papp, C.E.E. Wiltshire, J. Chesters, K.E. Watkins, Elevated iron concentration in putamen and cortical speech motor network in](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0015)
developmental stuttering, [Brain](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0015) 144 (2021) 2979–2984.

[4] N. Dehmamy, A.L. Barabasi, R. Yu, Understanding the representation [power](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0020) of graph neural networks in learning graph topology, Neural Information
Processing Systems [(2019)](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0020) 15413–15423.

[5] A. Di Martino, C.G. Yan, Q. Li, E. Denio, F.X. Castellanos, [K. Alaerts, et al, The](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0025) autism brain imaging data exchange: Towards a large-scale evaluation of
the intrinsic brain architecture in autism, Molecular Psychiatry 19 (2014) 659–667.

[6] Y. Feng, H. You, Z. Zhang, R. Ji, Y. Gao, Hypergraph [neural](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0030) networks, in: AAAI Conference on Artificial Intelligence, 2019, pp. [3558–3565.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0030)

[7] F.E. Fernandes, G.G. Yen, Pruning of generative adversarial neural [networks](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0035) for medical imaging diagnostics with evolution strategy, Information
Sciences 558 [(2021)](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0035) 91–102.

[8] J. Gilmer, S.S. Schoenholz, P.F. Riley, O. Vinyals, G.E. Dahl, Neural [message](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0040) passing for quantum chemistry, in: International Conference on Machine
[Learning,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0040) 2017, pp. [1263–1272.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0040)

[9] T. He, R. Kong, A.J. Holmes, M. Nguyen, M.R. Sabuncu, S.B. Eickhoff, D. [Bzdok,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0045) J. Feng, B.T. Yeo, Deep neural networks and kernel regression achieve
comparable accuracies for functional connectivity prediction [of](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0045) behavior and demographics, NeuroImage 206 (2020) 116276.

[10] [J. Huang, L. Zhou, L. Wang, D. Zhang, Attention-diffusion-bilinear neural network for brain network analysis, IEEE Transactions on Medical Imaging 39](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0050)
(2020) [2541–2552.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0050)

[11] J. Ji, X. Xing, Y. Yao, J. Li, X. Zhang, Convolutional kernels with an [element-wise](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0055) weighting mechanism for identifying abnormal brain connectivity
patterns, Pattern [Recognition](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0055) 109 (2021) 107570.

[12] J. Ji, Y. Yao, Convolutional neural network with graphical lasso to [extract](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0060) sparse topological features for brain disease classification, IEEE/ACM
Transactions on Computational Biology [and](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0060) Bioinformatics 18 (2021) 2327–2338.

[13] [J. Ji, Y. Zhang, Functional brain network classification based on deep graph hashing learning, IEEE Transactions on Medical Imaging (2022), https://doi.](https://doi.org/10.1109/TMI.2022.3173428)
[org/10.1109/TMI.2022.3173428.](https://doi.org/10.1109/TMI.2022.3173428)

[14] S. Ji, Y. Feng, R. Ji, X. Zhao, W. Tang, Y. Gao, Dual channel hypergraph [collaborative filtering, in: ACM SIGKDD](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0070) International Conference on Knowledge
Discovery [and](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0070) Data Mining, 2020, pp. [2020–2029.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0070)

[15] J. Jiang, Y. Wei, Y. Feng, J. Cao, Y. Gao, Dynamic hypergraph neural [networks,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0075) International Joint Conference on, Artificial Intelligence (2019) 2635–
[2641.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0075)

[16] [J. Kawahara, C.J. Brown, S.P. Miller, B.G. Booth, V. Chau, R.E. Grunau, J.G. Zwicker, G. Hamarneh, Brainnetcnn: Convolutional neural networks for brain](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0080)
networks; towards predicting [neurodevelopment,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0080) NeuroImage 146 (2017) 1038–1049.

[17] M. Khosla, K. Jamison, A. Kuceyeski, M.R. Sabuncu, Ensemble learning [with](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0085) 3d convolutional neural networks for functional connectome-based
prediction, [NeuroImage](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0085) 199 (2019) 651–662.

[18] [B.H. Kim, J.C. Ye, J.J. Kim, Learning dynamic graph representation of brain connectome with spatio-temporal attention, Neural Information Processing](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0090)
Systems [(2021)](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0090) 4314–4327.

[19] T.N. Kipf, M. Welling, Semi-supervised classification with graph [convolutional](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0095) networks, in: International Conference on Learning [Representations,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0095)
[2017.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0095)

[20] S.I. Ktena, S. Parisot, E. Ferrante, M. Rajchl, M. Lee, B. Glocker, D. [Rueckert,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0100) Metric learning with spectral graph convolutions on brain connectivity
networks, [NeuroImage](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0100) 169 (2018) 431–442.

[21] Q. Li, B. Becker, X. Jiang, Z. Zhao, Q. Zhang, S. Yao, K.M. Kendrick, [Decreased](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0105) interhemispheric functional connectivity rather than corpus callosum
volume as a potential biomarker for autism [spectrum](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0105) disorder, Cortex 119 (2019) 258–266.

[22] [X. Li, N.C. Dvornek, Y. Zhou, J. Zhuang, P. Ventola, J.S. Duncan, Graph neural network for interpreting task-fmri biomarkers, in: International Conference](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0110)
on Medical Image Computing [and](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0110) Computer Assisted Intervention, 2019, [pp.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0110) 485–493.

[23] T. Liu, X. Liu, L. Yi, C. Zhu, P.S. Markey, M. Pelowski, Assessing autism at [its](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0115) social and developmental roots: A review of autism spectrum disorder
studies using functional near-infrared [spectroscopy,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0115) NeuroImage 185 (2019) 955–967.

[24] [H. Lu, S. Liu, H. Wei, C. Chen, X. Geng, Deep multi-kernel auto-encoder network for clustering brain functional connectivity data, Neural Networks 135](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0120)
(2021) [148–157.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0120)

[25] M. Madine, I. Rekik, N. Werghi, Diagnosing autism using t1-w mri with [multi-kernel](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0125) learning and hypergraph neural network, in: IEEE International
Conference on [Image](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0125) Processing, 2020, [pp.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0125) 438–442.

[26] Z. Mao, Y. Su, G. Xu, X. Wang, Y. Huang, W. Yue, L. Sun, N. Xiong, [Spatio-temporal](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0130) deep learning method for adhd fmri classification, Information
Sciences 499 (2019) 1–11.

[27] M. Milham, D. Fair, M. Mennes, S. Mostofsky, The adhd-200 consortium: [a](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0135) model to advance the translational potential of neuroimaging in clinical
neuroscience, Frontiers in [Systems](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0135) Neuroscience 62 (2012).

[28] Morrissey, Z.D., Zhan, L., Ajilore, O., Leow, A.D., 2021. rest2vec: Vectorizing the resting-state functional connectome using graph embedding.
NeuroImage 226, 117538–117538.

[29] D.C. Nascimento, B. Pimentel, R. Souza, J.P. Leite, D.J. Edwards, T.E. [Santos,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0145) F. Louzada, Dynamic time series smoothing for symbolic interval data
applied to neuroscience, [Information](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0145) Sciences 517 (2020) 415–426.

[30] [L. Rabany, S. Brocke, V.D. Calhoun, B. Pittman, S. Corbera, B.E. Wexler, M.D. Bell, K. Pelphrey, G.D. Pearlson, M. Assaf, Dynamic functional connectivity in](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0150)
schizophrenia and autism spectrum disorder: Convergence, [divergence](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0150) and classification, NeuroImage: Clinical 24 (2019) 101966.

[31] Sadiq, M.T., Yu, X., Yuan, Z., Aziz, M.Z., Rehman, N.u., Ding, W., Xiao, G., 2022. Motor imagery bci classification based on multivariate variational mode
decomposition. IEEE Transactions on Emerging Topics in Computational Intelligence, 1–13.

[32] M.T. Sadiq, X. Yu, Z. Yuan, M.Z. Aziz, S. Siuly, W. Ding, A matrix determinant feature extraction approach for decoding motor and mental imagery eeg in
subject specific tasks, IEEE Transactions on Cognitive and Developmental Systems (2020), [https://doi.org/10.1109/TCDS.2020.3040438.](https://doi.org/10.1109/TCDS.2020.3040438)

[33] M.T. Sadiq, X. Yu, Z. Yuan, M.Z. Aziz, S. [Siuly, W. Ding, Toward the development of versatile brain-computer interfaces, IEEE Transactions on](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0165) Artificial
Intelligence 2 [(2021)](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0165) 314–328.

[34] H. Shahamat, M. Saniee Abadeh, Brain mri analysis using a deep [learning](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0170) based evolutionary approach, Neural Networks 126 (2020) 218–234.

[35] G. Shi, X. Li, Y. Zhu, R. Shang, Y. Sun, H. Guo, J. Sui, The divided [brain: Functional brain asymmetry underlying](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0175) self-construal, NeuroImage 240 (2021)

[118382.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0175)

[36] M. Soussia, I. Rekik, High-order connectomic manifold learning for [autistic](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0180) brain state identification, Connectomics in NeuroImaging (2017) 51–59.

[37] [L. Sun, B. Jin, H. Yang, J. Tong, C. Liu, H. Xiong, Unsupervised eeg feature extraction based on echo state network, Information Sciences 475 (2019) 1–17.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0185)

[38] P. Velickovic, G. Cucurull, A. Casanova, A. Romero, P. Lio, Y. [Bengio,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0190) Graph attention networks, in: International Conference on Learning
[Representations,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0190) [2018.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0190)

[39] N. Yadati, M. Nimishakavi, P. Yadav, V. Nitin, A. Louis, P.P. Talukdar, [Hypergcn:](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0195) A new method for training graph convolutional networks on
hypergraphs, Neural Information [Processing](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0195) Systems (2019) 1511–1522.

[40] [Y. Yan, J. Zhu, M. Duda, E. Solarz, C. Sripada, D. Koutra, Groupinn: Grouping-based interpretable neural network for classification of limited, noisy brain](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0200)
data, in: ACM SIGKDD International [Conference](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0200) on Knowledge Discovery and Data Mining, 2019, [pp.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0200) 772–782.

[41] [X. Yang, C. Deng, Z. Dang, K. Wei, J. Yan, Selfsagcn: Self-supervised semantic alignment for graph convolution network, in: Proceedings of the IEEE/CVF](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0205)
Conference on Computer [Vision](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0205) and Pattern Recognition, 2021, pp. [16775–16784.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0205)


1315


J. Ji, Y. Ren and M. Lei Information Sciences 608 (2022) 1301–1316


[42] L.L. Zeng, H. Wang, P. Hu, B. Yang, W. Pu, H. Shen, X. Chen, Z. Liu, H. Yin, [Q.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0210) Tan, K. Wang, D. Hu, Multi-site diagnostic classification of schizophrenia
using discriminant deep learning with functional connectivity mri, EBioMedicine 30 (2018) 74–85.

[43] R. Zhang, Y. Zou, J. Ma, Hyper-sagnn: a self-attention based graph [neural](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0215) network for hypergraphs, in: International Conference on Learning
[Representations,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0215) [2020.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0215)

[44] Y. Zhang, H. Zhang, E. Adeli, X. Chen, M. Liu, D. Shen, Multiview feature learning with multiatlas-based functional connectivity networks for mci
diagnosis, IEEE Transactions on Cybernetics (2020) 1–12.

[45] D. Zhou, J. Huang, B. Schölkopf, Learning with hypergraphs: [Clustering, classification,](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0225) and embedding, Neural Information Processing Systems (2006)
[1601–1608.](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0225)

[46] D. Zhu, X. Li, X. Jiang, H. Chen, D. Shen, T. Liu, Exploring high-order [functional](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0230) interactions via structurally-weighted lasso models, Information
Processing in Medical Imaging (2013) 13–24.

[47] H. Zhu, X. Wang, G. Xu, L. Deng, A self-paced learning based transfer [model](http://refhub.elsevier.com/S0020-0255(22)00730-7/h0235) for hypergraph matching, Information Sciences 590 (2022) 253–266.


1316


