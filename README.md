# Edit Transfer

> **Edit Transfer: Learning Image Editing via Vision In-Context Relations**
> <br>
> [Lan Chen](https://github.com/Orannue), 
> [Qi Mao](https://scholar.google.com/citations?user=VTQZF6EAAAAJ&hl=zh-CN), 
> [Yuchao Gu](https:/lab/scholar.google.com/citations?user=YpfrXyQAAAAJ&hl=zh-CN)
> and 
> [Mike Zheng Shou](https://sites.google.com/view/showlab)
> <br>
> [MIPG](https://github.com/CUC-MIPG), Communication University of China;
> [Show Lab](https://github.com/showlab), National University of Singapore
> <br>

[![Project Website](https://img.shields.io/badge/Project-Website-orange
)](https://cuc-mipg.github.io/EditTransfer.github.io/)
<a href="https://arxiv.org/abs/2503.13327"><img src="https://img.shields.io/badge/arXiv-2503.13327-A42C25.svg" alt="arXiv"></a>
<a href="https://huggingface.co/CUC-MIPG/EditTransfer"><img src="https://img.shields.io/badge/🤗_HuggingFace-Model-ffbd45.svg" alt="HuggingFace"></a>
<a href="https://huggingface.co/datasets/CUC-MIPG/EditTransfer/"><img src="https://img.shields.io/badge/🤗_HuggingFace-Dataset-ffbd45.svg" alt="HuggingFace"></a>
<br>

<img src='./assets/teaser.png' width='100%' />


## Getting Started


### 1. **Environment setup**
```bash
git clone https://github.com/CUC-MIPG/Edit-Transfer.git
cd Edit-Transfer

conda create -n EditTransfer python=3.10
conda activate EditTransfer
```
### 2. **Requirements installation**
```bash
pip install requirements.txt
```

### 3. **Start training**
We use the open-source [AI-Toolkit](https://github.com/ostris/ai-toolkit) to train EditTransfer. We provide training data with a configuration file in this repo:

- **Configuration File**: `config/edit_transfer.yml` 
- **Training Data**: `data/edit_transfer.zip` 

You can start training by running:

```bash
python run.py config/edit_transfer.yml
```
You can download the trained checkpoints of EditTransfer Model for inference: https://drive.google.com/file/d/1V4HraIjlMrbPfAPivk5vYoq4bQTzcP4L/view?usp=sharing 


### 4. Inference
Once the training is done, replace file paths and run the following code:

```
python edit_transfer.py --model_dir [your_model_dir] --model_name [your_model_name] --img_path [your_img_file_path]--prompt_file [your_prompt_file_path]

```


## Results
### Single and Compositional Edit Transfer
<img src='./assets/results.png' width='100%' />

### Generalization performance
<img src='./assets/generalization.png' width='100%' />



## Citation
```
@misc{chen2025edittransferlearningimage,
      title={Edit Transfer: Learning Image Editing via Vision In-Context Relations}, 
      author={Lan Chen and Qi Mao and Yuchao Gu and Mike Zheng Shou},
      year={2025},
      eprint={2503.13327},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2503.13327}, 
}
```