import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.optimizers import Adam

# 检查 GPU 是否可用
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"Number of GPUs available: {len(gpus)}")
    for gpu in gpus:
        print(gpu)
else:
    print("No GPU available, using CPU instead.")

# 构建简单的卷积神经网络
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# 编译模型
model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 打印模型摘要
model.summary()

# 假设有训练数据集 X_train 和 y_train
# X_train = ... (28, 28, 1) 的输入数据
# y_train = ... 对应的标签

# 训练模型
# model.fit(X_train, y_train, epochs=5, batch_size=32)
