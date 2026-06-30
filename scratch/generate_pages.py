import os

details_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Semantic-Segmentation\details"
os.makedirs(details_dir, exist_ok=True)

topics = [
    {
        "filename": "heuristic_boundary_graph_cuts.md",
        "title": "Heuristic Boundary & Graph Cuts",
        "diagram": """graph TD
    A[Input Image] --> B[Edge Detection & Color Histograms]
    B --> C{Graph Construction}
    C -->|Nodes: Pixels| D[Graph Cut Minimization]
    C -->|Edges: Similarity Weights| D
    D --> E[Segmented Output Boundaries]""",
        "info": """### Overview
Early computer vision frameworks (pre-2015) relied on hand-crafted mathematical formulations. Watershed segmentation, Mean-Shift, and normalized graph cuts manually partitioned images into spatial zones based on visual gradients and color similarity.

### Key Characteristics
* **Local Gradients:** Relies heavily on edge detection and sudden histogram changes.
* **Lack of Context:** No deep semantic reasoning; segments strictly by contrast/edges.
* **Optimization:** Often formulated as energy minimization problems over a pixel-grid graph."""
    },
    {
        "filename": "fully_convolutional_networks.md",
        "title": "Fully Convolutional & Encoder-Decoder Networks (FCN/U-Net)",
        "diagram": """graph LR
    A[Input Image] --> B[Encoder: Convolution + Pooling]
    B --> C[Bottleneck: Latent Features]
    C --> D[Decoder: Upsampling + Transposed Conv]
    B -.->|Skip Connections| D
    D --> E[Pixel-wise Segmentation Mask]""",
        "info": """### Overview
The introduction of FCNs (Long et al., 2015) revolutionized semantic segmentation by replacing fully connected layers with convolutional upsampling blocks. This allowed arbitrary-sized inputs and paved the way for modern encoder-decoder designs like U-Net and DeepLab.

### Key Characteristics
* **End-to-End Learning:** Direct mapping from raw pixels to pixel classification.
* **Skip Connections:** Routes low-level spatial features directly to the decoder.
* **Efficiency:** Eliminates redundant dense layer parameter overhead."""
    },
    {
        "filename": "segment_anything_model.md",
        "title": "Segment Anything Model (SAM) & Foundation Systems",
        "diagram": """graph TD
    A[Image Input] --> B[Vision Encoder: ViT]
    C[Prompts: Points/Boxes/Text] --> D[Prompt Encoder]
    B --> E[Lightweight Mask Decoder]
    D --> E
    E --> F[Multiple Valid Segmentation Masks]""",
        "info": """### Overview
Meta's Segment Anything Model (SAM) established a promptable foundation model for image segmentation. Trained on 1.1 billion masks, it exhibits zero-shot generalization to novel objects and domains using interactive point, box, or text prompts.

### Key Characteristics
* **Promptability:** Interactive segmentation via geometric or textual cues.
* **Zero-Shot Transfer:** Generalizes immediately to unseen distributions.
* **Ambiguity Resolution:** Outputs multiple valid masks when prompts are ambiguous."""
    },
    {
        "filename": "standard_semantic_segmentation.md",
        "title": "Standard Semantic Segmentation",
        "diagram": """graph LR
    A[Input Image: Two Cars] --> B[Semantic Model]
    B --> C[Output Mask: Single Class Color for both Cars]""",
        "info": """### Overview
Standard semantic segmentation treats every pixel as an independent classification target. It assigns a class label (e.g., car, person, sky) to each pixel without distinguishing between individual objects of the same category.

### Key Characteristics
* **Class-Level Masking:** Grouping all instances of a class into one collective region.
* **Dense Labeling:** Map is spatially aligned with input.
* **Simple Outputs:** Lacks tracking or counting capability for individual objects."""
    },
    {
        "filename": "instance_segmentation.md",
        "title": "Instance Segmentation",
        "diagram": """graph LR
    A[Input Image: Two Cars] --> B[Instance Model]
    B --> C[Output Masks: Car #1 and Car #2 isolated]""",
        "info": """### Overview
Instance segmentation identifies, localizes, and segments individual objects of interest. Unlike standard semantic segmentation, it differentiates between distinct objects of the exact same category.

### Key Characteristics
* **Object Detection Integration:** Combines object localization (bounding boxes) with mask generation.
* **Unique Identifiers:** Distinguishes overlapping/adjacent instances.
* **Pioneering Work:** SDS (2014) and Mask R-CNN (2017)."""
    },
    {
        "filename": "panoptic_segmentation.md",
        "title": "Panoptic Segmentation",
        "diagram": """graph TD
    A[Input Image] --> B[Panoptic Network]
    B --> C[Stuff Segmentation: Sky, Road, Grass]
    B --> D[Things Segmentation: Car 1, Car 2, Person 1]
    C --> E[Unified Panoptic Output Map]
    D --> E""",
        "info": """### Overview
Panoptic segmentation unifies semantic and instance segmentation. It maps continuous background classes ("Stuff" e.g., sky, road) and countable object instances ("Things" e.g., cars, pedestrians) in a single coherent representation.

### Key Characteristics
* **Unified Output:** Every pixel is assigned a class label and an instance ID (if applicable).
* **No Overlapping Masks:** Each pixel belongs to exactly one segment.
* **Holistic Scene Parsing:** Replaces fragmented task-specific pipelines."""
    },
    {
        "filename": "open_vocabulary_segmentation.md",
        "title": "Open-Vocabulary Segmentation (OVS)",
        "diagram": """graph TD
    A[Image Features] --> B[Mask Proposals]
    C[Text Prompts] --> D[CLIP Text Embeddings]
    B --> E[Vision-Language Alignment]
    D --> E
    E --> F[Zero-Shot Class Segmentations]""",
        "info": """### Overview
Open-vocabulary segmentation uses vision-language models (e.g., CLIP) to segment arbitrary classes defined by natural language prompts at inference time, removing constraints of fixed label sets.

### Key Characteristics
* **Language-Aligned:** Aligns pixel/mask embeddings with rich text representations.
* **Zero-Shot:** Segments classes unseen during training.
* **Interactive:** Flexibly query the image for any object query."""
    },
    {
        "filename": "lateral_skip_connections.md",
        "title": "Lateral Skip Connections",
        "diagram": """graph LR
    A[Encoder High-Res Features] -->|Copy & Crop| B[Skip Connection Bridge]
    C[Decoder Low-Res Features] --> D[Upsampling/Transposed Conv]
    B --> E[Feature Fusing / Concatenation]
    D --> E
    E --> F[Reconstructed High-Res Features]""",
        "info": """### Overview
Skip connections (popularized by U-Net) route fine-grained spatial information from early encoder layers directly to late decoder layers, bypassing the bottleneck to preserve edge details.

### Key Characteristics
* **Spatial Recovery:** Restores lost localization details.
* **Gradient Flow:** Helps gradients propagate backward during training.
* **Symmetrical Design:** Direct bridges between encoder and decoder resolution stages."""
    },
    {
        "filename": "dilated_convolutions.md",
        "title": "Atrous / Dilated Convolutions",
        "diagram": """graph TD
    A[Input Feature Map] --> B[Kernel with Dilation Rate r]
    B --> C[Expanded Receptive Field]
    C -->|No Extra Params| D[Dense Feature Representation]""",
        "info": """### Overview
Dilated (Atrous) convolutions insert spaces (holes) between kernel elements. This allows layers to capture a wider spatial context without downsampling or increasing parameter counts.

### Key Characteristics
* **Receptive Field Expansion:** Expands context view exponentially.
* **Resolution Preservation:** Avoids excessive pooling and downsampling.
* **Parameter Efficient:** Reuses standard convolution parameters with gaps."""
    },
    {
        "filename": "atrous_spatial_pyramid_pooling.md",
        "title": "Atrous Spatial Pyramid Pooling (ASPP)",
        "diagram": """graph TD
    A[Input Features] --> B[Conv 1x1]
    A --> C[Dilated Conv r=6]
    A --> D[Dilated Conv r=12]
    A --> E[Dilated Conv r=18]
    A --> F[Image Pooling]
    B & C & D & E & F --> G[Concat + 1x1 Conv]
    G --> H[Multi-Scale Output]""",
        "info": """### Overview
ASPP (introduced in DeepLabv2) uses multiple parallel dilated convolutions with different sampling rates to capture multi-scale context simultaneously.

### Key Characteristics
* **Multi-Scale Processing:** Processes images at diverse receptive fields.
* **Pyramid Structure:** Captures local details alongside global context.
* **Robust Representation:** Essential for objects appearing at variable scales."""
    },
    {
        "filename": "activation_memory_checkpointing.md",
        "title": "Activation Memory Checkpointing",
        "diagram": """graph TD
    A[Forward Pass] --> B{Store Key Checkpoints}
    B -->|Discard Intermediate Activations| C[Saves VRAM]
    D[Backward Pass] --> E[Recompute Discarded Activations on-the-fly]
    E --> F[Calculate Gradients]""",
        "info": """### Overview
Activation checkpointing reduces peak VRAM footprint during deep network training by storing only key activations and recomputing intermediate ones during backpropagation.

### Key Characteristics
* **O(sqrt(N)) Memory:** Reduces activation memory costs dramatically.
* **Compute/Memory Trade-off:** Trades extra forward passes for reduced memory constraints.
* **Larger Batch Sizes:** Enables training large models on consumer GPUs."""
    },
    {
        "filename": "tvm_hardware_compilation.md",
        "title": "TVM & Hardware Compiler Optimization",
        "diagram": """graph LR
    A[PyTorch/ONNX Model] --> B[TVM Relay graph IR]
    B --> C[TIR schedule search & optimization]
    C --> D[Fused Kernels & Vectorized Code]
    D --> E[Target Hardware: GPU/CPU/NPU]""",
        "info": """### Overview
TVM compiles high-level neural networks into optimized machine code, merging and optimizing operators (like convolution, activation, and normalization) directly into hardware registers.

### Key Characteristics
* **Operator Fusion:** Combines sequential operations to reduce memory transfers.
* **Automated Tuning:** Optimizes kernels for specific target chips.
* **Deployment efficiency:** Lowers inference latency and memory footprints."""
    },
    {
        "filename": "autonomous_vehicle_perception.md",
        "title": "Autonomous Vehicle Perception & Navigation Stacks",
        "diagram": """graph TD
    A[LiDAR / Camera Feed] --> B[Real-Time Segmentation Network]
    B --> C[Drivable Space Mask]
    B --> D[Pedestrian & Vehicle Contours]
    B --> E[Lane Boundary Lines]
    C & D & E --> F[Path Planner & Control Stacks]""",
        "info": """### Overview
Autonomous driving relies on real-time semantic and panoptic segmentation to map free drivable areas, identify lane lines, and detect obstacles for path planning and safety.

### Key Characteristics
* **Low Latency:** Must run at 30Hz or higher.
* **Multi-Modal:** Often fuses camera imagery with LiDAR/radar point clouds.
* **High Safety Integrity:** Zero tolerance for critical boundary misclassifications."""
    },
    {
        "filename": "clinical_tissue_mapping.md",
        "title": "High-Resolution Clinical Diagnostic Tissue Mapping",
        "diagram": """graph LR
    A[High-Res MRI/CT Scan] --> B[Medical Segmentation Model: U-Net]
    B --> C[Tumor/Lesion Contours]
    B --> D[Organ & Bone Boundaries]
    C & D --> E[Radiologist Volumetric Analysis]""",
        "info": """### Overview
In clinical settings, segmentation models (such as U-Net variants) identify organ borders, track tumor growth, and highlight regions of interest from medical imaging.

### Key Characteristics
* **Spatially Precise:** Exact pixel borders are critical for surgical paths.
* **Volumetric Integration:** Handles 3D voxel grids in MRI/CT scans.
* **Robustness:** Must tolerate variance in scanner calibrations and patient anatomy."""
    },
    {
        "filename": "satellite_remote_sensing.md",
        "title": "Satellite Remote Sensing & Agricultural Zoning",
        "diagram": """graph TD
    A[Satellite Multispectral Imagery] --> B[Segmentation Network]
    B --> C[Deforestation Boundaries]
    B --> D[Crop Health Zoning]
    B --> E[Urban Growth Maps]""",
        "info": """### Overview
Earth observation and satellite imaging systems apply semantic segmentation to analyze forest cover, monitor agricultural health, track urban sprawl, and assist in disaster response.

### Key Characteristics
* **Hyperspectral Inputs:** Operates on channels beyond standard RGB (e.g., near-infrared).
* **Vast Scale:** Processes gigapixel-sized satellite maps.
* **Temporal Tracking:** Detects changes across multi-temporal historical feeds."""
    }
]

for t in topics:
    filepath = os.path.join(details_dir, t["filename"])
    content = f"""# {t["title"]}

[⬅️ Back to Main README](../README.md)

## 📊 Overview & Concept
{t["info"]}

## 🧬 Architectural Workflow
```mermaid
{t["diagram"]}
```

---
*Created as part of the Semantic Segmentation Evolution database.*
[⬅️ Back to Main README](../README.md)
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {filepath}")
