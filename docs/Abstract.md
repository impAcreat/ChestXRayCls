## Introduction

* **Keywords**：机器学习、计算机视觉
* **Task**：自动识别胸部X射线图像中的肺炎迹象，辅助医生快速准确地诊断肺炎
* **Dataset1**：https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
  * Chest X-Ray Images (Pneumonia) 数据集包含了数千张胸部X射线图像
  * 其中**包括正常和患有肺炎**的病例
  * 为医生诊断肺炎提供了视觉证据，展示了**不同阶段和类型**的肺炎表现

* **Dataset2**：https://www.kaggle.com/datasets/redwankarimsony/chestxray8-dataframe
  * 

## Method

Guidance：

> #### Load Data
>
> * 浏览数据集，了解图像格式、大小以及标签信息
> * 预处理：包括图像大小调整、归一化、数据增强等，以便模型训练
>
> #### Construct Model
>
> * 基于卷积神经网络（CNN），包括：
>   * 自定义CNN
>   * ResNet，DenseNet
>   * iv3
> * 初始化模型参数：
>   * 设置损失函数（如交叉熵损失）
>   * 优化器（如Adam或SGD）
>
> #### Train
>
> * 监控模型在验证集上的性能（准确率、召回率等）
> * 调优：
>   * 包括调整学习率
>   * 增加数据增强策略（如随机旋转、裁剪、翻转等）
>
> #### Test
>
> * 分析模型在测试集上的表现
> * 调优模型：
>   * 模型架构
>   * 损失函数、优化器
>   * 集成学习、模型融合
>
> #### Apply
>
> 将训练好的模型集成到一个易于使用的界面或应用中，方便医生快速使用。
> 使用实际的胸部X射线图像对模型进行测试，展示其辅助医生诊断肺炎的能力。
> 编写报告或制作演示文稿，展示实训成果和模型性能。
>
> 将训练好的模型保存为可部署的格式（如TensorFlow SavedModel或PyTorch的.pth文件）。
> 编写代码加载模型，并构建一个简单的应用界面（如Web应用或GUI应用），允许用户上传胸部X光片并获取肺炎检测结果。
> 对应用进行测试，确保其能够准确、快速地处理用户上传的图像并返回检测结果。