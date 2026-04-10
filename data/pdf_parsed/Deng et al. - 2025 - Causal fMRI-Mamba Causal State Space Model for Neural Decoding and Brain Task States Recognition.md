# Causal fMRI-Mamba: Causal State Space Model for Neural Decoding and Brain Task States Recognition

Weihao Deng [1], Fei Han [1] _[,]_ [2] _[∗]_, Qinghua Ling [3], Qing Liu [4], Henry Han [5]

1 _School_ _of_ _Computer_ _Science_ _and_ _Communication_ _Engineering,_ _JiangSu_ _University,_ _China_
2 _Jiangsu_ _Engineering_ _Research_ _Center_ _of_ _Big_ _Data_ _Ubiquitous_ _Perception_ _and_
_Intelligent_ _Agriculture_ _Applications,_ _China_
3 _School_ _of_ _Computer,_ _Jiangsu_ _University_ _of_ _Science_ _and_ _Technology,_ _China_
4 _School_ _of_ _Electronic_ _and_ _Information_ _Engineering,_ _West_ _Anhui_ _University,_ _China_
5 _School_ _of_ _Engineering_ _and_ _Computer_ _Science,_ _Baylor_ _University,_ _USA_
vihoixixix3@163.com, hanfei@ujs.edu.cn, jsjxy lqh@just.edu.cn, clyqig2008@126.com, Henry Han@baylor.edu



_**Abstract**_ **—Deep** **learning** **advances** **neural** **decoding** **in** **func-**
**tional magnetic resonance imaging (fMRI) tasks with convolution**
**and** **attention-based** **methods.** **However,** **these** **methods** **struggle**
**with** **capturing** **global** **spatiotemporal** **information** **due** **to** **high**
**dimensionality,** **noise** **and** **inter-individual** **difference** **of** **fMRI,**
**which** **also** **increase** **computational** **complexity** **and** **prior** **bias.** **To**
**this** **end,** **a** **novel** **causal** **state** **space** **model,** **Causal** **fMRI-Mamba,**
**is** **proposed** **for** **neural** **decoding** **and** **task** **state** **mapping.** **It** **effec-**
**tively captures global spatiotemporal information via eliminating**
**local** **redundancies** **and** **capturing** **long-distance** **dependencies.**
**Meanwhile,** **a** **causal** **representation** **framework** **is** **designed** **to**
**extract** **invariant** **high-order** **features** **and** **disentangle** **related**
**causal** **features,** **enhancing** **model** **performance.** **Furthermore,** **a**
**dense connection module is expanded to prevent significant causal**
**information** **loss** **in** **hidden** **states** **of** **inter** **layers.** **On** **the** **HCP**
**brain task state classification task, Causal fMRI-Mamba achieves**
**better performance and generalization than comparison methods.**


_**Index**_ _**Terms**_ **—Neuro-decoding,** **state** **space** **model,** **causal** **rep-**
**resentation** **learning,** **task-based** **fMRI.**


I. INTRODUCTION


Over the years, neuroscientists have dedicated to explore
the relationship between external stimuli and neural activity to
understand brain functions and mechanisms [1].Development
in non-invasive techniques like EEG, MRI and fMRI [2]
have been crucial in revealing brain functional networks.
They provide valuable information for understanding the brain
function. Among them, fMRI achieves localization of active
brain regions with high spatial resolution, by monitoring blood
oxygen level-dependent (BOLD) [3], making it increasingly
significant in exploring brain activity mechanisms.
In the past decade, machine learning-based multivoxel pattern
analysis (MVPA) [4] has been widely applied in fMRI analysis
as its effectiveness in neural decoding. The method based on
support vector machines for MVPA (SVM-MVPA) [4] has
been proposed to analyze multiple variables of neural signals.
However, due to the high dimensionality, sparsity and noise of
fMRI data, SVM-MVPA performs poorly when handling such
high-dimensional data. To address this issue, a multivariate


This work was supported by the National Natural Science Foun dation of
China under Grant nos. 61976108 and 62102002.



feature selection method based on principal component analysis (PCA) [5] has been proposed, which removes redundant
features to improve SMV-MVPA’s performance on fMRI.
With advancements in deep learning, researchers utilized deep
neural networks [6] to abstract high-dimensional representations for analyzing fMRI. Inspired by natural language
processing and attention mechanisms, [7] designed a masked
sequence model with multi-head attention to extract temporal
features and identify brain functional networks. [8] proposed a
eigendecomposition-based Transformer architecture to acquire
compact features. However, they overlooks the spatial structure
of fMRI and struggles with long-range dependencies, limiting
spatial semantic extraction and computational efficiency. A
state space model Vision Mamba [9] is proposed to address
existing issues of Transformer via processing spatial position
information and captures contextual visual dependencies.
Despite above methods have certain effects, most of them
rely on the independent and identically distributed (IID) [10]
assumption. However, fMRI neural decoding tasks encounter
out-of-distribution (OOD) issue due to individual differences

[11], which undermines generalization performance.
To this end, this paper proposes a state space model with
causal representation learning, named Causal fMRI-Mamba,
for neural decoding and brain task state mapping. It efficiently
captures spatiotemporal dependencies, extracts global information and accelerates inference. The causal representation
framework further disentangles causal features, eliminating
noise and individual differences. Specifically, the main contributions of this paper are as follows: (1) A state-space model
for fMRI-relative neural decoding is firstly proposed to capture
long-range dependencies and extract global spatiotemporal
information; (2) Based on dense connections, a aggregation
module is expanded to enhance information flow, enrich multilevel feature, and prevent the loss of causal factors; (3) A
causal representation learning framework with causal perturbation and disentanglement modules is designed to extract causal
factors and avoid non-casual interference; (4) A learnable
patch embedding method for spatiotemporal information is
firstly introduced for fMRI aiding state-space models sensitive
to token position information.



Authorized licensed use limited to: COLORADO STATE UNIVERSITY. Downloaded on December 05,2025 at 16:18:29 UTC from IEEE Xplore. Restrictions apply.


𝑳𝒂𝒃𝒆𝒍


|𝑇𝐺𝑈 𝐷 𝜔𝑒 𝑡𝑙𝑛𝑠𝑒𝐴 ·𝑔𝑔𝑟𝑒𝑔𝑎 ·𝑡𝑖𝑜𝑛 · + · 𝑃𝑟𝐷 𝑜𝑜 𝑑𝑡 𝑢𝑐𝑡<br>𝜎 · 𝜎 𝑆igmod 𝐺𝐶𝑃 𝐿𝑖𝑛𝑒𝑎𝑟 𝑅𝑒𝐿𝑈 𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑆𝑒𝑙𝑒𝑐𝑡 𝐿𝑖𝑛𝑒𝑎𝑟 𝐿𝑖𝑛𝑒𝑎𝑟 𝐿𝑖𝑛𝑒𝑎𝑟<br>ℎ<br>𝑝𝑎𝑠𝑡<br>x 𝑡𝑙 ℎ 𝑡𝑙−1 ℎ 𝑡𝑙−2…ℎ 𝑡𝑙−𝑚 + 𝐴𝐷𝐷<br>[𝐶𝐿𝑆] [𝐶𝐿𝑆] fMRI-Mamba 𝑳×<br>Ω<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑) ℎ𝑙<br>𝑡<br>ℎ 𝑡𝑙−1 ℎ 𝑝𝑎𝑠 𝑇𝑡<br>𝐷𝑒𝑛𝑠𝑒 ℎ 𝑡𝑙<br>𝑆𝑇𝑀 𝐺𝑈<br>TSpatial-temporal Scan 𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>…<br>𝑃𝑇 𝑜𝑒 𝑠𝑚 𝑒𝑝 𝑚𝑜 𝑏𝑟 𝑒𝑎 𝑑𝑙 𝑇𝑃1 𝑇𝑃𝑡<br>0 1 2 3 … 𝑃𝑠 … 1 2 3 … 𝑃𝑠<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑 [𝐶𝐿𝑆] 3D Patch Embedding<br>… … …|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|||||||1<br>**…**<br>**…**|1<br>**…**<br>**…**||||**…**<br>**…**<br>𝑃𝑠|**…**<br>**…**<br>𝑃𝑠|**…**<br>**…**<br>𝑃𝑠|
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|||𝑇𝑃1|𝑇𝑃1||||||𝑇𝑃𝑡|𝑇𝑃𝑡||||
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑|2|2|3<br>|3<br>|**…**<br>𝑃𝑠|**…**<br>𝑃𝑠|**…**<br>𝑃𝑠|**…**<br>𝑃𝑠|2|3<br>|3<br>|**…**<br>𝑃𝑠|**…**<br>𝑃𝑠|**…**<br>𝑃𝑠|
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑||||||**3D Pat**|**3D Pat**|** ch Embedd**<br>|** ch Embedd**<br>|**  ing**||||||
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑||||||**…**|**…**|**…**|**…**||||**…**|**…**|**…**|
|+<br>ℎ𝑡<br>𝑙<br>**fMRI-Mamba**<br>𝑆𝑇𝑀<br>𝑇𝐺𝑈<br>𝐷𝑒𝑛𝑠𝑒<br>𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛<br>𝐷𝑒𝑛𝑠𝑒𝑃𝑜𝑜𝑙(𝑠ℎ𝑎𝑟𝑒𝑑)<br>𝑳×<br>ℎ𝑡𝑙<br>ℎ𝑝𝑎𝑠𝑡<br>ℎ𝑡𝑙−1<br>1<br>**3D Patch Embedding**<br>**…**<br>2<br>3<br>1<br>2<br>3<br>**…**<br>**…**<br>**…**<br>**…**<br>**…**<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑃1<br>𝑇𝑃𝑡<br>**…**<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>**…**<br>Ω<br>T**Spatial-temporal Scan**<br>[𝐶𝐿𝑆]<br>[𝐶𝐿𝑆]<br>𝑇𝐺𝑈<br>𝐺𝐶𝑃<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝑅𝑒𝐿𝑈<br>𝐿𝑖𝑛𝑒𝑎𝑟<br>𝜎·<br>·<br>𝐷𝑜𝑡<br>𝑃𝑟𝑜𝑑𝑢𝑐𝑡<br>𝜎𝑆igmod<br>𝑃𝑠<br>𝑃𝑠<br>·<br>x𝑡𝑙<br>𝑆𝑒𝑙𝑒𝑐𝑡<br>ℎ𝑡<br>𝑙−1<br>ℎ𝑡𝑙−2<br>ℎ𝑡𝑙−𝑚<br>𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟𝐿𝑖𝑛𝑒𝑎𝑟<br>·<br>·<br>𝜔𝑡𝑙<br>+<br>ℎ𝑝𝑎𝑠𝑡<br>𝐴𝐷𝐷<br>𝐷𝑒𝑛𝑠𝑒𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑖𝑜𝑛|1<br>0<br>[𝐶𝐿𝑆]<br>𝑇𝑒𝑚𝑝𝑜𝑟𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑<br>𝑆𝑝𝑎𝑡𝑖𝑎𝑙<br>𝑃𝑜𝑠𝑒𝑚𝑏𝑒𝑑||||||||||||||||



**(a) Framework** **(b) Causal Intervention** **(c) Embedding & Feature Extracting**


Fig. 1. The overview of Causal fMRI-Mamba. (a) shows the framework of causal fMRI-Mamba. (b) is the visualization of causal intervention based on
Fourier Transform and the _do_ operation. (c) demonstrates the spatial-temporal embedding and the detail of causal factors extractor. The causal disentangle
module is explained in Section II-C.



II. METHODOLOGY


In this section, we introduce the overall framework of
Causal Mamba and the details of its components. As shown
in Fig.1.


_A._ _Embedding_ _for_ _fMRI_

Since the input fMRI data _X_ _∈_ R _[T][ ×][H][×][W][ ×][D]_ containing
both three-dimensional spatial structure and temporal dimension, embedding methods such as MAMSM [7] cannot simultaneously capture the spatiotemporal position information.
Following previous works [9] [12], a novel spatiotemporal
position embedding is introduced. _X_ is mapped to _t_ _×_ _L_
non-overlapping patches _Xp_ _∈_ R [(] _[t][×][L]_ [)] _[×][C]_ via 3D convolution
(i.e. 9 _×_ 9 _×_ 9), where _L_ = _t ×_ _[H]_ 9 _[×]_ _[W]_ 9 _[×]_ _[D]_ 9 [,] _[t]_ [=] _[T]_ _s_ [,] _[s]_ [is]

the sampling frequency, _C_ is the embedding dimension. Then
spatiotemporal position embeddings are added to the sequence
of patches as follows


_X_ = [ _cls, Xp_ ] + _poss_ + _post_ (1)


where _cls_ is a learnable token to represent the class of the
sequence, _poss_ _∈_ _R_ [(1+] _[L]_ [)] _[×][C]_ and _post_ _∈_ _R_ _[t][×][C]_ are the learnable spatial and temporal position embeddings, respectively.
These embeddings drive the following model to capture the
spatiotemporal features.


_B._ _fMRI-Mamba_


Global feature modeling is crucial for neural decoding
and brain task mapping. Although Transformer architectures
achieve desirable results, they struggle with computational burdens and degradation of global exploration in long sequences,
often losing important information and hindering inference
efficiency. Hence, fMRI-Mamba, a state-space model, is designed to capture long-range spatiotemporal dependencies in



fMRI sequences.
**Spatial-Temporal** **Mamba** **(STM)** To fully exploit spatiotemporal semantics in long sequences, this paper designs
a bidirectional scanning STM based on Bi Mamba [9] to
capture spatiotemporal features. Formally, Bi Mamba adopts
the following discrete ordinary differential equation to model
the input data _X_ _∈_ R _[B][×][L][×][D]_,


**A** = exp(∆ **A** )



where **A** _∈_ R _[N]_ _[×][N]_ is the evolution parameter, **B** _∈_ R _[B][×][L][×][N]_

and **C** _∈_ R _[B][×][L][×][N]_ as the projection parameters. ∆ _∈_
R _[B][×][L][×][D]_ is a timescale parameter to transform the continuous
parameters A and B to their discrete versions **A** and **B** based
on the zero-order hold method.
By prioritizing spatiotemporal dimensions ( _T, H, W, D_ ) and
reordering the long sequence via a predefined order set Ω,
Bi Mamba captures hidden states based on this order set and
then restores the output sequence of Bi Mamba via the inverse
order set Ω _[−]_ [1] .


_STM_ ( _X_ ) = Ω _[−]_ [1] ( _Bi_ _M_ _amba_ (Ω( _X_ ))) (3)


where Ω is set to the dimension priority order _D_ _→_ _W_ _→_ _H_ .
**Temporal Gating Unit (TGU)** While STM captures compact
spatiotemporal features, the low temporal resolution of fMRI
may cause the model to focus on spatial features, limiting
temporal exploration. To address this, a temporal gating unit
is designed to guide the model in learning temporal dependencies. TGU uses a global contrastive pooling layer (GCP)

[13] followed by a recalibration block with two linear and two



**B** = (∆ **A** ) _[−]_ [1] (exp(∆ **A** ) _−_ **I** ) _·_ ∆ **B**


_ht_ = **A** _ht−_ 1 + **B** _xt_
_yt_ = **C** _ht_



(2)




_[W]_
9 _[×]_ 9




_[D]_
9 _[×]_ 9



9 [,] _[t]_ [=] _[T]_ _s_



Authorized licensed use limited to: COLORADO STATE UNIVERSITY. Downloaded on December 05,2025 at 16:18:29 UTC from IEEE Xplore. Restrictions apply.


normalization layers to recalibrate the sequence, which is then
weighted to emphasize useful temporal features.


_TGU_ ( _X_ ) = _X_ _∗_ _Recal_ (( _GCP_ ( _X_ ))) (4)


where _GCP_ ( _·_ ) is GCP, _Recal_ ( _·_ ) is the recalibration block.
**Dense** **Aggregation** **Module** Mamba finds long-range dependencies in hidden states, but the flow is limited to the
current layer, leading to information loss and hindering causal
disentanglement in deeper layers. Inspired by DenseSSM [14],
we expand a dense aggregation block. This block accesses a
shared Dense pool to retrieve multi-granularity hidden states
from previous layers, select useful information to fuses with
current hidden states for reducing information loss and enhancing multi-granularity perception.



Then _X_ and _X_ [ˆ] are taken as input data for the fMRI-Mamba.
**Causal** **Disentanglement** **Module** fMRI-Mamba is guided
to learn invariant features after the _do_ operation. However, the
hidden states may not fully satisfy to ICM. Hence, a causal
disentanglement is designed to separate causal factors from
invariant features. Specifically, fMRI-Mamba acts as a causal
factors extractor _g_ ( _·_ ), producing _S_ = _g_ ( _X_ ) _∈_ _R_ [1] _[×][C][s]_, where
_Cs_ is the number of causal factors. Then, CRL loss regularizes
_g_ ( _·_ ) to discover invariant and independent causal factors as
follows



_Cs_

- _Mi,j_ [2] (8)


_i_ = _j_



_LCRL_ = [1]

_Cs_




- _Cs_ ( _Mi,i −_ 1) [2] + 1

_i_ =1 _Cs_ ( _Cs −_ 1)



where _M_ = _R_ _[T]_ _R_ [ˆ] is the empirical cross-correlation matrix

[12], _M_ ( _i, j_ ) = _Cosine_ ( _ri,_ ˆ _rj_ ). _R_ = [ _r_ 1 _, r_ 2 _, ..., rn_ ] and _R_ [ˆ] =

[ˆ _r_ 1 _,_ ˆ _r_ 2 _, ...,_ ˆ _rn_ ] are the transpose of _S_ = [ _s_ _[T]_ 1 _[, s]_ 2 _[T]_ _[, ..., s]_ _B_ _[T]_ []] [and]
_S_ ˆ = [ˆ _s_ _[T]_ 1 _[,]_ [ ˆ] _[s]_ 2 _[T]_ _[, ...,]_ [ ˆ] _[s]_ _B_ _[T]_ []] [after] [normalization,] [respectively.] _[B]_ [is]
the number of samples. Since the ultimate goal is the brain
task state classification, a label classifier layer _h_ ( _·_ ) is added
behind the disentanglement module. And we define a crossentropy loss function as _LCLS_ = _−EX∼P_ [ _Y ·_ log( _h_ ( _g_ ( _X_ ))] to
further identify causal factors _S_ that provide sufficient causal
information for the classification task. In summary, the overall
optimization objective is formulated as


min [+] _[ αL][CRL]_ (9)
_g,h_ _[Loss]_ [ =] _[ L][CLS]_


where _α_ is the trade-off parameter. Noting that it is set as 0.5.


III. EXPERIMENTS


**Datasets** **and** **Preprocessing** This study uses the HCP
task-fMRI dataset in S1200 version contains imaging and
behavioral data from a large population of young healthy
adults [18]. We employed data of 1,034 participants who had
performed seven tasks: emotion, gambling, language, motor,
relational, social and working memory. For each task, an input
sample is a continuous BOLD series that covers the entire
block and 8s past the block, including the post-signal of the
hemodynamic response function. Furthermore, each BOLD
volume is cropped from 91 _×_ 109 _×_ 91 to 75 _×_ 93 _×_ 81 to
exclude the area that is not part of the brain.
**Implementation** **Details** The proposed framework is implemented with Pytorch, all the experiments are executed on
NVIDIA RTX 4090 GPUs (24GB). In this work, we employ
a fivefold cross-validation across subjects, one-fold is taken
as testing set, and the rest four folds were used for training
(70%), validating (20%) and testing (10%). We adopt an
AdamW optimizer with an initial learning rate of 0.001 and
a weight decay of 1 _e_ _[−]_ [4] for training. The training runs 200
epochs with a batch size of 32 for the dataset. To avoid
overfitting, an early stopping approach is adopted when the
validation loss reached a minimum. Code is available at:
https://github.com/VIHOIX3/Causal-fMRI-Mamba.
**Comparison** **Experiment** We compared the proposed model
with state-of-the-art (SOTA) fMRI methods, including fMRIDNN [6], BrainNetCNN [19], BrainNetFormer [20], STAGIN



_h_ _[l]_ _t_ [=] _[ Fuse]_ - _h_ _[l]_ _t_ _[, H]_ _t_ _[l]_ - = _h_ _[l]_ _t_ [+]



_m_

- _select_ ( _x_ _[l]_ _t_ [)] _[ ·][ ϕ]_ [(] _[h]_ _t_ _[l][−][i]_ ) (5)


_i_ =1



where _h_ _[l]_ _t_ [is] [the] [hidden] [state] [of] _[l][th]_ [fMRI-Mamba] [block,] _[H]_ _t_ _[l]_ [is]
the hidden states before the current block, _select_ ( _·_ ) includes
two MLP layers with SiLu function, _ϕ_ is a linear layer.


_C._ _Causal_ _representation_ _learning_ _framework_


To learn stable and invariant features, the Independent
Causal Mechanisms (ICM) principle [15] is applied by constructing a structural causal model (SCM) to discover causal
relationships among hidden states. As shown in Eq.6. SCM
identifies stable causal factors by learning the causal relationship between variables _X_ and labels _Y_,


_X_ := _f_ ( _S, U, E_ 1)

(6)
_Y_ := _h_ ( _S, E_ 2) = _h_ ( _g_ ( _X_ ) _, E_ 2)


where _S_ is invariant causal factors affecting _X_ and _Y_, _E_ 1 and
_E_ 2 as independent noise. _S_, _U_ and _E_ 1 are jointly independent.
_f_, _h_ and _g_ are unknown structural functions. The optimization
goal is formulated as arg min _h EP_ [ _ℓ_ ( _h_ ( _g_ ( _X_ )) _, Y_ )], where _ℓ_
is the cross-entropy loss. Since causal factors in fMRI are
not intuitive, a causal representation learning framework with
causal intervention and disentanglement modules is proposed
to discover causal factors.
**Causal** **Intervention** **Module** To separate causal factors _S_
from entangled features, the _do_ operations are necessary.
According to [16], the phase spectrum retains the global
structure and high-order features, while the amplitude spectrum contains basic statistics. Signals can be reconstructed
from phase spectrum, as degradation mainly affects the amplitude spectrum. To achieve the _do_ operation on _U_, _X_ is
transformed to extract phase components _P_ ( _X_ ) and amplitude components _A_ ( _X_ ) via Fast Fourier Transform [16], as
_F_ ( _X_ ) = _A_ [ˆ] ( _X_ ) _·e_ _[−][j][·][P]_ [ (] _[X]_ [)] . And _A_ ( _X_ ) is intervened via Mixup
_′_

[17] with amplitude spectrum of arbitrary subject data _X_, as
_A_ ˆ( _X_ ) = _λA_ ( _X_ ) + (1 _−_ _λ_ ) _A_ ( _X_ _′_ ), where _λ∼U_ (0 _, η_ ) and _η_
is the intervention strength. Then the intervention fMRI _X_ [ˆ] is
generated by inverse Fourier Transform from _P_ ( _X_ ) and _A_ [ˆ] ( _X_ )
as follows
_X_ ˆ = _F_ _[−]_ [1][�] _A_ ˆ( _X_ ) _· e_ _[−][j][·][P]_ [ (] _[X]_ [)][�] (7)



Authorized licensed use limited to: COLORADO STATE UNIVERSITY. Downloaded on December 05,2025 at 16:18:29 UTC from IEEE Xplore. Restrictions apply.


[21], and ESTA [8]. Fig.2 shows the confusion matrix of
the proposed model in the classification task. Table I shows


1.0



0.8


0.6


0.4


0.2


0.0



Emotion


Gambling


Language


Motor


Relational


Social


WM




|Col1|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|~~03 0.~~<br>~~00 0.~~|~~89 0.~~<br>~~00 1.~~|~~01 0.~~<br>~~00 0.~~|~~05 0.~~<br>~~00 0.~~|~~00 0.~~<br>~~00 0.~~|~~00 0.~~<br>~~00 0.~~|
|<br>~~03 0.~~|<br>~~12 0.~~|<br>~~00 0.~~|<br>~~78 0.~~|<br>~~04 0.~~|<br>~~03 0.~~|
|<br>~~00 0.~~|<br>~~00 0.~~|<br>~~00 0.~~|<br>~~08 0.~~|<br>~~88 0.~~|<br>~~03 0.~~|
|<br>~~01 0.0~~|<br>~~03 0.0~~|<br>~~05 0.0~~|<br>~~03 0.0~~|<br>~~03 0.9~~|<br>~~82 0.0~~|
|<br>~~00 0.~~|<br>~~00 0.~~|<br>~~02 0.~~|<br>~~04 0.~~|<br>~~02 0.~~|<br>~~08 0.~~|



Predict


Fig. 2. The average confusion matrix on HCP-task dataset.


the experimental result of each method on HCP-Task dataset.
It is obviously that Causal fMRI-Mamba outperforms other
SOTA methods, achieving the highest accuracy and the best
stability.The results demonstrates the effectiveness of Mamba
and causal representation learning framework. While fMRIDNN and BrainNetCNN use convolutions to extract fMRI
features, they lack global information capture. STAGIN and
BrainNetFormer apply spatiotemporal attention mechanisms
but show limitations in extracting global information from
long-sequence data. ESTA integrates feature decomposition
with spatiotemporal attention, but the decomposed features are
not guaranteed to provide stable representations.


TABLE I
**THE** **RESULT** **OF** **EACH** **METHOD** **ON HCP-TASK** **DATASET.**


**Method** **Accuracy** (%) **F1-score** (%) **AUC** (%)


BrainNetCNN 89.99 _±_ 0.48 90.92 _±_ 0.49 98.87 _±_ 0.17
fMRI-DNN 93.7 _±_ 0.19 92.95 _±_ 0.22 99.54 _±_ 0.21
STGIN 96.25 _±_ 0.32 96.24 _±_ 0.33 99.79 _±_ 0.03
ESTA 97.86 _±_ 0.62 97.85 _±_ 0.65 99.91 _±_ 0.24
**Ours** **98.89** _±_ **0.18** **98.93** _±_ **0.20** **99.96** _±_ **0.17**


**Ablation Study** To investigate the contribution of components
in Causal fMRI-Mamba, we conduct step-wise elimination of
the causal framework and Mamba module. A Transformer
architecture with attention mechanism is taken as a reference.
Noting that Causal Transformer is the reference model with the
proposed causal framwork. Table II indicates that both components positively contribute to classification performance.
Specifically, the Mamba module plays a crucial role in capturing long-range dependencies and enhancing classification
performance, while the causal framework extracts invariant
causal factors and improve the model stability.
**Generalization** **Analysis** To validate the generalization capability of the proposed model, we conducted transfer learning



TABLE II
**RESULT** **OF** **THE** **ABLATION** **STUDY.**


**Method** **Accuracy** (%)


Transformer 95.19 _±_ 0.67
Causal Transformer 96.64 _±_ 0.24
fMRI-Mamba 97.34 _±_ 0.59
**Causal** **fMRI-Mamba** **98.89** _±_ **0.18**


experiments on a few-shot dataset, the HCP Test-RETEST
dataset [16], focusing on the classification of four substates
(left-foot, left-hand, right-foot and tongue) on Motor tasks.
The experiment used five-fold cross-validation, with 60% of
the subjects as the training set, 20% as the validation set,
and 20% as the test set. The model is finetuned on the
dataset, and the results are compared with fMRI-DNN and
SVM-MVPA. Fig.3(a) shows the average confusion matrix for
the transfer tasks. Fig.3(b) compares the average classification accuracy with baseline methods, Causal fMRI-Mamba
achieves the highest classification (96 _._ 45 _±_ 1 _._ 8%) among
them, while the accuracy of fMRI-DNN and SVM-MVPA
only reach at 95 _._ 79 _±_ 1 _._ 7% and 81 _._ 60 _±_ 7 _._ 1%, respectively.
The results demonstrate that Causal fMRI-Mamba has better
generalization than the baseline methods.



|41 0.0<br>09 0.9|17 0.0<br>73 0.0|33 0.0<br>12 0.0|
|---|---|---|
||||
|~~31~~<br>~~0.~~<br>~~01~~<br>~~0.~~|~~16~~<br>~~0.~~<br>~~11~~<br>~~0.~~|~~58~~<br>~~0.~~<br>~~02~~<br>~~0.~~|


Predict


(a) Confusion matrix



0.8


0.6


0.4


0.2



|94.70 ± 1.7 81.60 ± 7.1 96.45±|94.70 ± 1.7 81.60 ± 7.1 96.45±|Col3|Col4|
|---|---|---|---|
|94.70± 1.7<br>81.60 ± 7.1<br>96.45±|94.70± 1.7<br>81.60 ± 7.1<br>96.45±|||


(b) Accuracy of each method



Fig. 3. The result of transfer experiment on HCP TEST-RETEST dataset.


IV. CONCLUSIONS


In this paper, a space state model with a causal representation framework, Causal fMRI-Mamba, is firstly proposed for
neural decoding and task state classification on fMRI. The
model proposes a novel fMRI-Mamba model and introduces
spatiotemporal embedding to capture long-range dependencies
and global spatiotemporal features. It also extends a dense
aggregation module to enhance the information flow in hidden
states, preventing the causal factors loss. Meanwhile, a causal
perturbation and disentanglement framework is designed to extract invariant causal factors, addressing the OOD problem. On
the HCP-Task dataset, the model outperforms SOTA methods,
achieving the best performance. Generalization analysis on
the HCP TEST-RETEST dataset demonstrates that the model
maintains excellent performance when transferred to few-shot
datasets.



Authorized licensed use limited to: COLORADO STATE UNIVERSITY. Downloaded on December 05,2025 at 16:18:29 UTC from IEEE Xplore. Restrictions apply.


REFERENCES


[1] Lu Cao, Dandan Huang, and Yue Zhang, “When computational
representation meets neuroscience: A survey on brain encoding and
decoding.,” in _IJCAI_, 2021, pp. 4339–4347.

[2] Elias Ebrahimzadeh, Saber Saharkhiz, Lila Rajabion, Homayoun Baghaei Oskouei, Masoud Seraji, Farahnaz Fayaz, Sarah Saliminia,
Seyyed Mostafa Sadjadi, and Hamid Soltanian-Zadeh, “Simultaneous
electroencephalography-functional magnetic resonance imaging for assessment of human brain function,” _Frontiers_ _in_ _Systems_ _Neuroscience_,
vol. 16, pp. 934266, 2022.

[3] Federico De Martino, Giancarlo Valente, No¨el Staeren, John Ashburner,
Rainer Goebel, and Elia Formisano, “Combining multivariate voxel
selection and support vector machines for mapping and classification of
fmri spatial patterns,” _Neuroimage_, vol. 43, no. 1, pp. 44–58, 2008.

[4] Martin N Hebart, Kai G¨orgen, and John-Dylan Haynes, “The decoding
toolbox (tdt): a versatile software package for multivariate analyses of
functional imaging data,” _Frontiers_ _in_ _neuroinformatics_, vol. 8, pp. 88,
2015.

[5] Lijun Wang, Yu Lei, Ying Zeng, Li Tong, and Bin Yan, “Principal
feature analysis: a multivariate feature selection method for fmri data,”
_Computational_ _and_ _mathematical_ _methods_ _in_ _medicine_, vol. 2013, no.
1, pp. 645921, 2013.

[6] Xiaoxiao Wang, Xiao Liang, Zhoufan Jiang, Benedictor A Nguchu,
Yawen Zhou, Yanming Wang, Huijuan Wang, Yu Li, Yuying Zhu, Feng
Wu, et al., “Decoding and mapping task states of the human brain via
deep learning,” _Human_ _brain_ _mapping_, vol. 41, no. 6, pp. 1505–1519,
2020.

[7] Mengshen He, Xiangyu Hou, Enjie Ge, Zhenwei Wang, Zili Kang, Ning
Qiang, Xin Zhang, and Bao Ge, “Multi-head attention-based masked
sequence model for mapping functional brain networks,” _Frontiers_ _in_
_Neuroscience_, vol. 17, pp. 1183145, 2023.

[8] Jiwon Lee, Eunsong Kang, Junyeong Maeng, and Heung-Il Suk,
“Eigendecomposition-based spatial-temporal attention for brain cognitive states identification,” in _ICASSP_ _2024-2024_ _IEEE_ _International_
_Conference_ _on_ _Acoustics,_ _Speech_ _and_ _Signal_ _Processing_ _(ICASSP)_ .
IEEE, 2024, pp. 1921–1925.

[9] Lianghui Zhu, Bencheng Liao, Qian Zhang, Xinlong Wang, Wenyu
Liu, and Xinggang Wang, “Vision mamba: Efficient visual representation learning with bidirectional state space model,” _arXiv_ _preprint_
_arXiv:2401.09417_, 2024.

[10] Peng Cui and Susan Athey, “Stable learning establishes some common ground between causal inference and machine learning,” _Nature_
_Machine_ _Intelligence_, vol. 4, no. 2, pp. 110–115, 2022.

[11] Ladan Shams and Ulrik Beierholm, “Bayesian causal inference: A
unifying neuroscience theory,” _Neuroscience_ _&_ _Biobehavioral_ _Reviews_,
vol. 137, pp. 104619, 2022.

[12] Kunchang Li, Xinhao Li, Yi Wang, Yinan He, Yali Wang, Limin Wang,
and Yu Qiao, “Videomamba: State space model for efficient video
understanding,” _arXiv_ _preprint_ _arXiv:2403.06977_, 2024.

[13] Hyunjong Park and Bumsub Ham, “Relation network for person reidentification,” in _Proceedings_ _of_ _the_ _AAAI_ _conference_ _on_ _artificial_
_intelligence_, 2020, vol. 34, pp. 11839–11847.

[14] Wei He, Kai Han, Yehui Tang, Chengcheng Wang, Yujie Yang, Tianyu
Guo, and Yunhe Wang, “Densemamba: State space models with dense
hidden connection for efficient large language models,” _arXiv_ _preprint_
_arXiv:2403.00818_, 2024.

[15] Fangrui Lv, Jian Liang, Shuang Li, Bin Zang, Chi Harold Liu, Ziteng
Wang, and Di Liu, “Causality inspired representation learning for
domain generalization,” in _2022_ _IEEE/CVF_ _Conference_ _on_ _Computer_
_Vision_ _and_ _Pattern_ _Recognition_ _(CVPR)_, 2022, pp. 8036–8046.

[16] Jing Zou, Lanqing Liu, Qi Chen, Shujun Wang, Xiaohan Xing, and Jing
Qin, “Mmr-mamba: Multi-contrast mri reconstruction with mamba and
spatial-frequency information fusion,” _arXiv preprint arXiv:2406.18950_,
2024.

[17] Hongyi ZHANG, “mixup: Beyond empirical risk minimization,” _arXiv_
_preprint_ _arXiv:1710.09412_, 2017.

[18] Deanna M Barch, Gregory C Burgess, Michael P Harms, Steven E
Petersen, Bradley L Schlaggar, Maurizio Corbetta, Matthew F Glasser,
Sandra Curtiss, Sachin Dixit, Cindy Feldt, et al., “Function in the
human connectome: task-fmri and individual differences in behavior,”
_Neuroimage_, vol. 80, pp. 169–189, 2013.

[19] Jeremy Kawahara, Colin J Brown, Steven P Miller, Brian G Booth,
Vann Chau, Ruth E Grunau, Jill G Zwicker, and Ghassan Hamarneh,



“Brainnetcnn: Convolutional neural networks for brain networks; towards predicting neurodevelopment,” _NeuroImage_, vol. 146, pp. 1038–
1049, 2017.

[20] Leheng Sheng, Wenhan Wang, Zhiyi Shi, Jichao Zhan, and Youyong
Kong, “Brainnetformer: Decoding brain cognitive states with spatialtemporal cross attention,” in _ICASSP_ _2023-2023_ _IEEE_ _International_
_Conference_ _on_ _Acoustics,_ _Speech_ _and_ _Signal_ _Processing_ _(ICASSP)_ .
IEEE, 2023, pp. 1–5.

[21] Byung-Hoon Kim, Jong Chul Ye, and Jae-Jin Kim, “Learning dynamic
graph representation of brain connectome with spatio-temporal attention,” _Advances_ _in_ _Neural_ _Information_ _Processing_ _Systems_, vol. 34, pp.
4314–4327, 2021.



Authorized licensed use limited to: COLORADO STATE UNIVERSITY. Downloaded on December 05,2025 at 16:18:29 UTC from IEEE Xplore. Restrictions apply.


